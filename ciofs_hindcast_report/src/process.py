"""intake.source.derived from intake package. Taking to use DataFrameTransform."""

# from functools import lru_cache
# from . import import_name
# from .. import open_catalog
# from .base import DataSource, Schema

import cf_pandas
from intake.source.derived import GenericTransform
import pandas as pd
import numpy as np
import ciofs_hindcast_report as chr
import xarray as xr
import ocean_model_skill_assessor as omsa

from .utils import calculate_julian_days, resample


class DataFrameTransform(GenericTransform):
    """Transform where the input and output are both Dask-compatible dataframes

    This derives from GenericTransform, and you mus supply ``transform`` and
    any ``transform_kwargs``.
    """

    input_container = "dataframe"
    container = "dataframe"
    optional_params = {}
    _df = None

    def to_dask(self):
        if self._df is None:
            self._pick()
            self._df = self._transform(self._source.to_dask().compute(),
                                       **self._params["transform_kwargs"])
        return self._df

    def _get_schema(self):
        """load metadata only if needed"""
        self.to_dask()
        return Schema(dtype=self._df.dtypes,
                      shape=(None, len(self._df.columns)),
                      npartitions=self._df.npartitions,
                      metadata=self.metadata)

    def read(self):
        if self._df is None:
            self._pick()
            self._df = self._transform(self._source.read(),
                                       **self._params["transform_kwargs"])
        return self._df


class DatasetTransform(GenericTransform):
    """Transform where the input and output are both xarray Datasets

    This derives from GenericTransform, and you mus supply ``transform`` and
    any ``transform_kwargs``.
    """

    input_container = "xarray"
    container = "xarray"
    optional_params = {}
    _df = None

    def to_dask(self):
        if self._df is None:
            self._pick()
            self._df = self._transform(self._source.to_dask().compute(),
                                       **self._params["transform_kwargs"])
        return self._df

    # def _get_schema(self):
    #     """load metadata only if needed"""
    #     self.to_dask()
    #     return Schema(dtype=self._df.dtypes,
    #                   shape=(None, len(self._df.columns)),
    #                   npartitions=self._df.npartitions,
    #                   metadata=self.metadata)

    def read(self):
        return self.to_dask()


def ctd_transects_gwa(df, visit_transect):
    df = df.set_index(["Visit", "Transect"]).sort_index()
    dft = df.loc[visit_transect].copy()
    dft["distance [km]"] = omsa.utils.calculate_distance(dft.cf["longitude"], 
                                              dft.cf["latitude"])
    dft = dft.reset_index()#.set_index("Date_Time")#.set_index(["Date_Time", "Depth", "Latitude_DD", "Longitude_DD"], drop=False)
    return dft#.reset_index(drop=True)


def ctd_profiles_2005_noaa(df, station):
    """Using multiindex for time and depth since CTD profile.
    
    There can be a duplicated entry, at least in 518.
    """
    # import pdb;pdb.set_trace()
    dd = df[df["Station"] == station]
    idup = ~dd.index.duplicated()
    return dd.iloc[idup]
    # df = df[df["Station"] == station]
    # return df.set_index([df.cf["T"], df.cf["Z"]])


def ctd_profiles_usgs_boem(df, station):
    return df[df["station_number"] == station]#.reset_index(drop=True)


def select_by_station(df, station):
    return df[df.cf["station"] == station]#.reset_index(drop=True)


# def select_by_station_ak2utc(df, station):
#     # can't overwrite multi index values with repeated entries so work around:
#     index_names = df.index.names
#     df = df.reset_index()
#     df = df.set_index(df.cf["T"].name).tz_localize("US/Alaska").tz_convert("UTC").tz_localize(None).reset_index()
#     df = df.set_index(index_names)
#     return df[df.cf["station"] == station]


def ctd_profiles_emap_2002_all(df):
    stations_to_remove = [32, 34, 35, 36, 38, 40, 41, 45, 46, 
                            50, 51, 53, 54, 55, 56, 58, 59,
                            60, 61, 62, 63, 64,
                            70,71,72,73,74,75]

    return df[~df["Station"].isin(stations_to_remove)]
    

def ctd_towed_ferry_noaa_pmel(ds, year, month):
    return ds.cf.sel(T=slice(f"{year}-{month}", f"{year}-{month}"))


def ctd_transects_otf_kbnerr(df, year, day):
    dfd = df.set_index("date_time").loc[f"{year}-07-{day}"].reset_index() 
    dfd["distance [km]"] = omsa.utils.calculate_distance(dfd.cf["longitude"], 
                                        dfd.cf["latitude"])
    # dfd = dfd.reset_index().set_index(["date_time","Depth [m]", dfd.cf["latitude"].name, dfd.cf["longitude"].name], drop=False)
    dfd = dfd.drop(columns=['Pressure [m]', 'Sigma-é00', 'Pressure ', 'Density [sigma]'], errors="ignore")
    return dfd


def ctd_towed_gwa(df, month):
    dfd = df.set_index(df.cf["T"].name).loc[f"{df.cf['T'].dt.year[0]}-{month}"].reset_index()
    dfd["distance [km]"] = omsa.utils.calculate_distance(dfd.cf["longitude"], 
                                        dfd.cf["latitude"])
    return dfd


def ctd_towed_gwa_temp(df, month):
    ddf = df.set_index(df.cf["T"].name).loc[f"{df.cf['T'].dt.year[0]}-{month}"].reset_index()
    ddf["distance [km]"] = omsa.utils.calculate_distance(ddf.cf["longitude"], 
                                         ddf.cf["latitude"])
    return ddf


def add_location_columns(df, lon, lat):
    df["longitude"] = lon
    df["latitude"] = lat
    return df


def ctd_transects_cmi_uaf(df, cruise=None):
    df["date_time"] = pd.to_datetime(df["Month"].str.zfill(2)+df["Day"].str.zfill(2)+df["Year"]+df["Hour"].str.zfill(2)+df["Minute"].str.zfill(2), format="%m%d%Y%H%M", exact=False)
    df.drop(columns=["Month","Day","Year","Hour","Minute"], inplace=True)
    df.drop(columns=["Water Depth", "Sigma-t"], inplace=True)
    if cruise is not None:
        dfd = df.loc[df["Cruise"] == cruise].copy()
        # dfd = df.loc[df["Cruise"] == cruise].copy().reset_index(drop=True)
        dfd["distance [km]"] = omsa.utils.calculate_distance(dfd.cf["longitude"], 
                                                  dfd.cf["latitude"])
        # dfd = dfd.set_index(["date_time","Depth [m]", dfd.cf["latitude"].name, dfd.cf["longitude"].name], drop=False)
        return dfd
    else:
        # df = df.set_index(["date_time","Depth [m]"], drop=False)
        return df
    

def subtract_360_from_longitude(df):
    """Subtract 360 degrees from longitude to shift from 0 to 360 to -180 to 180."""
    df.cf["longitude"] -= 360
    return df


def ctd_transects_cmi_kbnerr(df, cruise, line):
    dff = df[(df["Cruise"] == cruise) & (df.line == line)].copy().reset_index(drop=True)
    dff["distance [km]"] = omsa.utils.calculate_distance(dff.cf["longitude"], 
                                              dff.cf["latitude"])
    # dff = dff.reset_index().set_index(["date_time","Depth [m]","Latitude [degrees_north]","Longitude [degrees_east]"], drop=False)
    return dff


def ctd_transects_cmi_kbnerr_sue_shelikof(df):
    df["distance [km]"] = omsa.utils.calculate_distance(df.cf["longitude"], 
                                              df.cf["latitude"])
    return df
    

def ctd_transects_uaf(df, transect):
    dfd = df[df["transect"] == transect].copy().reset_index(drop=True)
    # downsample the output to 0.5 in pressure
    dfcasts = []
    datetime_casts = dfd["date_time"].unique()
    dP = 0.5  # delta Pressure for rows
    # loop over each CTD cast so it can have its own depths interpolated to
    for datetime_cast in datetime_casts:
        dfcast = dfd[dfd["date_time"] == datetime_cast]
        dfcast = dfcast.drop_duplicates(subset="Pressure")
        dfcast = dfcast.set_index(["Pressure"])
        if dfcast.index.min() < 0.5:
            start_depth = 0.5
        else:
            start_depth = 1.0
        # import pdb; pdb.set_trace()
        new_index = np.arange(start_depth, dfcast.index.max().round() + dP, dP)
        dfcast = dfcast.reindex(dfcast.index.union(new_index)).interpolate().reindex(new_index)
        dfcast = dfcast.reset_index()
        dfcasts.append(dfcast)

    dfd = pd.concat(dfcasts)

    dfd["distance [km]"] = omsa.utils.calculate_distance(dfd.cf["longitude"].values, 
                                        dfd.cf["latitude"].values)
    dfd = dfd.set_index([dfd.cf["T"].name, dfd.cf["Z"].name, dfd.cf["latitude"].name, dfd.cf["longitude"].name], drop=True)
    return dfd


def ctd_profiles_2005_osu(df, date, lon=None, lat=None):
    df['UTC/GMT_Time'] = [pd.Timestamp(date) + pd.Timedelta(f"{val*24} hour") for val in df['UTC/GMT_Time']]
    df.cf["longitude"] *= -1
    # lonkey, latkey = df.cf["longitude"].name, df.cf["latitude"].name
    if lon is not None and lat is not None:
        return df[(df.cf["longitude"] == lon) & (df.cf["latitude"] == lat)]
    else:
        return df


def ctd_transects_misc_2002(df):
    # convert from local time zone to UTC
    df = df.tz_localize("US/Alaska").tz_convert("UTC").tz_localize(None)
    df["distance [km]"] = omsa.utils.calculate_distance(df.cf["longitude"], 
                                        df.cf["latitude"])
    df = df.reset_index()
    # df = df.reset_index().set_index(["date_time","Depth","Lat (N)","Long (E)"], drop=False)
    return df


def ctd_transects_barabara_to_bluff_2002_2003(df, cruise):
    dfd = df[df["Cruise"] == cruise]
    dfd["distance [km]"] = omsa.utils.calculate_distance(dfd.cf["longitude"], 
                                        dfd.cf["latitude"])
    # dfd = dfd.reset_index().set_index(["date_time","Depth (m)","Lat (N)","Long (E)"], drop=False)
    return dfd
