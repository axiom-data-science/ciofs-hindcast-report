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
        # return self.read()
        return self.to_dask()


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


def ctd_profiles_gwa(df, transect, date):
    df["jday"] = calculate_julian_days(df.cf["T"])
    itransect = df["Transect"] == str(transect)
    dft = df.loc[itransect]
    idate = dft["Date_Time"].dt.strftime("%Y-%m-%d") == str(date)
    return dft[idate]


def ctd_profiles_2005_noaa(df, station):
    return df[df["Station"] == station]


def ctd_profiles_usgs_boem(df, station=None):
    df = df.rename(columns={'PrdM': "pressure", 'Tv290C': "temp", 'Sal00': "salt"})
    inds = df.index[df["ctd_time [local]"].isnull()]
    df = df.drop(index=df.index[inds]).reset_index(drop=True)
    df["date_time"] = pd.to_datetime(df["date"] + " " + df["ctd_time [local]"])
    df = df.drop(columns=["date","ctd_time [local]"])
    if station is None:
        return df
    else:
        return df[df["station_number"] == station]


def ctd_towed_otf_kbnerr(df):
    df = resample(df, to="5T")
    df.columns = df.columns.str.replace(r'\s', '', regex=True)
    df = df.dropna(axis=0, subset='lat').reset_index(drop=True)
    df["jday"] = calculate_julian_days(df.cf["T"])
    return df


def ctd_towed_ferry_noaa_pmel(ds, yearmonth=None, doresampling=True):
    ds["depth"] = ((ds.cf["T"].name), np.ones(ds.cf["T"].size)*4, {"axis": "Z"})
    ds = ds.assign_coords({"LAT": ds["LAT"], "LON": ds["LON"], "depth": ds["depth"]})
    ds = ds.cf.guess_coord_axis()
    
    bbox = [-156.5, 56.5, -148.5, 61.5]
    inbox = (ds["LON"] > bbox[0]) & (ds["LAT"] > bbox[1]) & (ds["LON"] < bbox[2]) & (ds["LAT"] < bbox[3])
    ds = xr.where(inbox, ds, np.nan)
    ds = ds.dropna(dim=ds.cf["T"].name)
    ds["jday"] = calculate_julian_days(ds.cf["T"])

    if yearmonth is not None:
        year, month = yearmonth
        dss = ds.cf.sel(T=slice(f"{year}-{month}", f"{year}-{month}"))
        if doresampling:
            return resample(dss, to="5T")
        else:
            return dss
    else:
        if doresampling:
            ds = resample(ds, to="5T")
        return ds


def ctd_profiles_otf_kbnerr(df, year, day):
    return df.set_index("date_time").loc[f"{year}-07-{day}"].reset_index()    


def multiply_longitude_n1(df):
    """Multiply the longitude column by -1."""
    # import pdb; pdb.set_trace()
    df.cf["longitude"] *= -1
    return df


def ctd_towed_gwa_2017(df):
    df = resample(df, to="5T")
    if df.cf["T"].dt.month[0] in (4,5):
        df.loc[df.cf["Z"] < 3] = np.nan
        df.cf["longitude"] *= -1
        df[df.cf["longitude"] > -150.5] = np.nan  # discard points outside domain
        df = df.dropna().reset_index(drop=True)
    else:
        df.loc[df.cf["Z"] < 3] = np.nan
        df.cf["longitude"] *= -1
        df[df.cf["longitude"] > -150.5] = np.nan  # discard points outside domain
        df = df.dropna(axis=1, how="all").dropna(subset=df.cf["latitude"].name).reset_index(drop=True)
        df.cf["T"] = df.cf["T"].dt.tz_localize("US/Alaska").dt.tz_convert("UTC").dt.tz_localize(None)
        df.rename(columns={df.cf["T"].name: df.cf["T"].name.replace("Alaska","UTC")}, inplace=True)
    df["jday"] = calculate_julian_days(df.cf["T"])
    return df


def ctd_towed_gwa_2018(df, month=None):
    """Specific processing for this dataset."""
    
    df = resample(df, to="5T")
    df.loc[df.cf["Z"] < 3] = np.nan
    df.cf["longitude"] *= -1
    df[df.cf["longitude"] > -150.5] = np.nan  # discard points outside domain
    df = df.dropna().reset_index(drop=True)
    df["jday"] = calculate_julian_days(df.cf["T"])
    if month is not None:
        return df.set_index(df.cf["T"].name).loc[f"2018-{month}"].reset_index()  # april, may, june, july
    else:
        return df


def ctd_towed_gwa_2019(df, month=None):
    """Specific processing for this dataset."""
    
    df.drop(index=df.index[df["date_mm_dd_yy"] == "43774"], inplace=True)
    df.drop(index=df.index[df["date_mm_dd_yy"] == "43804"], inplace=True)
    df.cf["longitude"] *= -1
    df["date_time"] = pd.to_datetime(df["date_mm_dd_yy"] + " " + df["time_hh_mm_ss"] + " " + df["time_am_pm"], format="%m/%d/%y %I:%M:%S %p")
    df.drop(columns=["date_mm_dd_yy","time_hh_mm_ss","time_am_pm"], inplace=True)
    df["depth [m]"] = 7
    df = resample(df, to="5T")
    df["jday"] = calculate_julian_days(df.cf["T"])
    if month is not None:
        return df.set_index(df.cf["T"].name).loc[f"2019-{month}"].reset_index()
    else:
        return df


def ctd_towed_gwa_2020(df, month=None):
    """Specific processing for this dataset."""
    
    df.cf["T"] = df.cf["T"].dt.tz_localize("US/Alaska").dt.tz_convert("UTC").dt.tz_localize(None)
    df.rename(columns={df.cf["T"].name: df.cf["T"].name.replace("-08:00","")}, inplace=True)
    df["depth"] = 7
    df[df.cf["longitude"] > -150.5] = np.nan  # discard points outside domain
    df = df.dropna(subset="latitude_degN", axis=0).reset_index(drop=True)
    df = resample(df, to="5T")
    df["jday"] = calculate_julian_days(df.cf["T"])
    if month is not None:
        return df.set_index(df.cf["T"].name).loc[f"2020-{month}"].reset_index()
    else:
        return df


def temp_towed_gwa_2011(df, month=None):
    """Specific processing."""
    df = df.dropna()
    df = pd.DataFrame(data=df.values.reshape((-1,5)), columns=df.columns[:5])
    df["date_time"] = pd.to_datetime(df["Date(dd/mm/yyyy)"] + " " + df["Time(hh:mm:ss)"])
    df.drop(columns=["Date(dd/mm/yyyy)", "Time(hh:mm:ss)"], inplace=True)
    df["depth [m]"] = 7
    df[df.cf["longitude"] > -150.5] = np.nan  # discard points outside domain
    df = df.dropna().sort_values(by="date_time", axis=0).reset_index(drop=True)
    df["jday"] = calculate_julian_days(df.cf["T"])
    # temp name seems to be causing an issue
    df.rename(columns={df.cf["temp"].name: "temperature"}, inplace=True)
    df.cf["temp"] = df.cf["temp"].astype(np.float64)
    if month is not None:
        return df.set_index(df.cf["T"].name).loc[f"2011-{month}"].reset_index()
    else:
        return df


def temp_towed_gwa_others(df):
    if "T" in df.columns:
        df.rename(columns={"T": "temp"}, inplace=True)
    df[df.cf["longitude"] > -150.5] = np.nan  # discard points outside domain
    df = df.dropna(subset=df.cf["longitude"].name).dropna(axis=1)
    converttoUTC = False
    if "ak" in df.iloc[:,1].name.lower() or "alaska" in df.iloc[:,1].name.lower():
        converttoUTC = True
    df["month"] = df.iloc[:,0].str.split("/").str.get(0)
    df["day"] = df.iloc[:,0].str.split("/").str.get(1)
    df["year"] = df.iloc[:,0].str.split("/").str.get(2)
    df["hour"] = df.iloc[:,1].str.split(":").str.get(0)
    df["minute"] = df.iloc[:,1].str.split(":").str.get(1)
    df["second"] = df.iloc[:,1].str.split(":").str.get(2)
    df["date_time"] = pd.to_datetime(df[["month","day","year","hour","minute","second"]])
    df.drop(columns=["month","day","year","hour","minute","second"], inplace=True)
    df.drop(columns=df.columns[0:2], inplace=True)
    if converttoUTC:
        df.cf["T"] = df.cf["T"].dt.tz_localize("US/Alaska").dt.tz_convert("UTC").dt.tz_localize(None)
    df["depth"] = 7
    df = df.reset_index(drop=True)
    year, month = df.cf["T"].dt.year[0], df.cf["T"].dt.month[0]
    return df.set_index(df.cf["T"].name).loc[f"{year}-{month}"].reset_index()


def add_depth_column(df, depth):
    df["depth [m]"] = depth
    return df


def add_location_columns(df, lon, lat):
    df["longitude"] = lon
    df["latitude"] = lat
    return df


def ctd_profiles_cmi_uaf(df, cruise=None):
    df["date_time"] = pd.to_datetime(df["Month"].str.zfill(2)+df["Day"].str.zfill(2)+df["Year"]+df["Hour"].str.zfill(2)+df["Minute"].str.zfill(2), format="%m%d%Y%H%M", exact=False)
    df.drop(columns=["Month","Day","Year","Hour","Minute"], inplace=True)
    if cruise is not None:
        return df[df["Cruise"] == cruise]
    else:
        return df
    

def subtract_360_from_longitude(df):
    """Subtract 360 degrees from longitude to shift from 0 to 360 to -180 to 180."""
    df.cf["longitude"] -= 360
    return df


def moorings_kbnerr_historical(df, lon, lat):
    df = df.dropna(axis=1, how="all").dropna(subset="Temp").reset_index(drop=True)
    df["Depth"] = df["Depth"].astype(float)
    df["Sal"] = df["Sal"].astype(float)
    df["StationCode"] = df["StationCode"].astype('object')
    df["StationCode"] = df["StationCode"].str.strip()

    # station = stations[0]
    lon *= -1
    df["lat"] = lat
    df["lon"] = lon
    
    # set bad values to nan for each variable
    # ind = df["F_Temp"].str.contains("-3")  # catch bad values
    df["Temp"] = df["Temp"].where(~df["F_Temp"].str.contains("-3"), np.nan)
    # df.loc[ind, "Temp"] = np.nan

    # ind = df["F_Sal"].str.contains("-3")  # catch bad values
    df["Sal"] = df["Sal"].where(~df["F_Sal"].str.contains("-3"), np.nan)
    # df.loc[ind, "Sal"] = np.nan
    
    df = df.drop(columns=["F_Temp","F_Sal", "F_Depth"])

    return df


def ctd_profiles_cmi_kbnerr(df, cruise, line, stations):
    """ 
    Line 4 has an incorrect latitude for station 65. This can be seen with:
    ```
    df = cat['cmi_full_v2-Cruise_16-Line_4'].read()
    df.drop_duplicates(subset="Station")
    ```
    because the longitude is fixed and the latitude increases linearly until station 65 and then repeats the latitude value of station 56. The values are the same for the line in all datasets, and in the report. Since the difference in latitude across line 4 is about 0.0167, I will apply that difference from station 64 and use the resulting latitude for line 4, station 65.    
    """
    df.cf["longitude"] -= 360
    df["line"] = line
    df = df.sort_values("date_time").reset_index(drop=True)
    if line == 4:
        station65lat = (df[df["Station"] == 64].cf["latitude"] + 0.0167).iloc[0]
        df.loc[df["Station"] == 65, "Latitude [degrees_north]"] = station65lat
    return df[(df["Cruise"] == cruise) & (df.Station.isin(stations))]


def ctd_time_series_uaf(df, transect=None):
    
    # lon and lat are named backwards
    df.rename(columns={"Lon": "Lat", "Lat": "Lon"}, inplace=True)

    # change year from 2003 to 2004
    df["date_time"] = [t.replace(year=2003) for t in df["date_time"]]

    # create a transect field
    transects = {1: np.arange(1,15).tolist(), 2: np.arange(15,28).tolist(), 3: np.arange(28,44).tolist(),
                4: np.arange(44,59).tolist(), 5: np.arange(59,72).tolist(), 6: np.arange(72,85).tolist(),
                7: np.arange(85,101).tolist(), 8: np.arange(101,114).tolist(), 9: np.arange(114,127).tolist()}
    for transectloop in transects:
        df.loc[df["Station"].isin(transects[transectloop]), "transect"] = transectloop
    df["transect"] = df["transect"].astype(int)
    
    if transect is not None:
        return df[df["transect"] == transect]
    else:
        return df
        

def ctd_profiles_2005_osu(df, date, lon=None, lat=None):
    df['UTC/GMT_Time'] = [pd.Timestamp(date) + pd.Timedelta(f"{val*24} hour") for val in df['UTC/GMT_Time']]
    df.cf["longitude"] *= -1
    # lonkey, latkey = df.cf["longitude"].name, df.cf["latitude"].name
    if lon is not None and lat is not None:
        return df[(df.cf["longitude"] == lon) & (df.cf["latitude"] == lat)]
    else:
        return df
