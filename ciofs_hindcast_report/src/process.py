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

from .utils import calculate_julian_days, resample, calculate_distance


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


def ctd_profiles_gwa(df, visit_transect):
    df = df.set_index(["Visit", "Transect"]).sort_index()
    dft = df.loc[visit_transect].copy()
    dft["distance [km]"] = calculate_distance(dft.cf["longitude"], 
                                              dft.cf["latitude"])
    return dft.reset_index(drop=True)


def ctd_profiles_2005_noaa(df, station):
    return df[df["Station"] == station]


def ctd_profiles_usgs_boem(df, station):
    return df[df["station_number"] == station]


def ctd_towed_ferry_noaa_pmel(ds, year, month):
    return ds.cf.sel(T=slice(f"{year}-{month}", f"{year}-{month}"))


def ctd_profiles_otf_kbnerr(df, year, day):
    dfd = df.set_index("date_time").loc[f"{year}-07-{day}"].reset_index() 
    dfd["distance [km]"] = calculate_distance(dfd.cf["longitude"], 
                                        dfd.cf["latitude"])
    return dfd


def ctd_towed_gwa(df, month):
    dfd = df.set_index(df.cf["T"].name).loc[f"{df.cf['T'].dt.year[0]}-{month}"].reset_index()
    dfd["distance [km]"] = calculate_distance(dfd.cf["longitude"], 
                                        dfd.cf["latitude"])
    return dfd


def ctd_towed_gwa_temp(df, month):
    ddf = df.set_index(df.cf["T"].name).loc[f"{df.cf['T'].dt.year[0]}-{month}"].reset_index()
    ddf["distance [km]"] = calculate_distance(ddf.cf["longitude"], 
                                         ddf.cf["latitude"])
    return ddf


def add_location_columns(df, lon, lat):
    df["longitude"] = lon
    df["latitude"] = lat
    return df


def ctd_profiles_cmi_uaf(df, cruise=None):
    df["date_time"] = pd.to_datetime(df["Month"].str.zfill(2)+df["Day"].str.zfill(2)+df["Year"]+df["Hour"].str.zfill(2)+df["Minute"].str.zfill(2), format="%m%d%Y%H%M", exact=False)
    df.drop(columns=["Month","Day","Year","Hour","Minute"], inplace=True)
    if cruise is not None:
        dfd = df.loc[df["Cruise"] == cruise].copy().reset_index(drop=True)
        dfd["distance [km]"] = calculate_distance(dfd.cf["longitude"], 
                                                  dfd.cf["latitude"])
        return dfd
    else:
        return df
    

def subtract_360_from_longitude(df):
    """Subtract 360 degrees from longitude to shift from 0 to 360 to -180 to 180."""
    df.cf["longitude"] -= 360
    return df


def ctd_profiles_cmi_kbnerr(df, cruise, line):
    dff = df[(df["Cruise"] == cruise) & (df.line == line)].copy().reset_index(drop=True)
    dff["distance [km]"] = calculate_distance(dff.cf["longitude"], 
                                              dff.cf["latitude"])
    return dff


def ctd_profiles_cmi_kbnerr_sue_shelikof(df):
    df["distance [km]"] = calculate_distance(df.cf["longitude"], 
                                              df.cf["latitude"])
    return df
    

def ctd_profiles_uaf(df, transect):
    dfd = df[df["transect"] == transect].copy().reset_index(drop=True)
    dfd["distance [km]"] = calculate_distance(dfd.cf["longitude"], 
                                        dfd.cf["latitude"])
    return dfd


def ctd_profiles_2005_osu(df, date, lon=None, lat=None):
    df['UTC/GMT_Time'] = [pd.Timestamp(date) + pd.Timedelta(f"{val*24} hour") for val in df['UTC/GMT_Time']]
    df.cf["longitude"] *= -1
    # lonkey, latkey = df.cf["longitude"].name, df.cf["latitude"].name
    if lon is not None and lat is not None:
        return df[(df.cf["longitude"] == lon) & (df.cf["latitude"] == lat)]
    else:
        return df
