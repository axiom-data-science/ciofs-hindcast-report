---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import dataretrieval.nwis as nwis
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Functions

```{code-cell} ipython3
# found these by visual inspection of the `river_transport` variable which has negative signs on the
# 0s so I could read them off there.
river_sign = [-1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 
              -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1, 1,
              1, 1, 1, 1, 1, 1]

stations = ['15276000', '15290000', '15271000', '15239900', '15281000', '15295700',
            '15239070', '15275100', '15266300', '15284000', '15292780', '15274600']

station_list_file = ['15295700', '15239070', '15239900', '15266300', '15266300',
                     '15271000', '15274600', '15275100', '15276000', '15281000',
                     '15281000', '15281000', '15281000', '15281000', '15281000',
                     '15281000', '15281000', '15281000', '15281000', '15284000',
                     '15284000', '15284000', '15284000', '15284000', '15284000',
                     '15284000', '15284000', '15284000', '15284000', '15290000',
                     '15290000', '15292780', '15292780', '15292780', '15292780', '15292780']

# station "in model": station actually used
discharge_stations = {'15276000': "15276000", '15290000': "15290000", 
                      '15271000': "15271000", '15239900': "15239900", 
                      '15281000': "15281000", '15295700': "15295700",
                      '15239070': "15239070", '15275100': "15275100", 
                      '15266300': "15266300", '15284000': "15284000", 
                      '15292780': "15292000", '15274600': "15274600"}

# station "in model": station actually used
temp_stations = {'15276000': "15276000", '15290000': "15290000", 
                      '15271000': "15258000", '15239900': "15239900", 
                      '15281000': "15284000", '15295700': "15295700",
                      '15239070': "15239070", '15275100': "15276000", 
                      '15266300': "15266300", '15284000': "15284000", 
                      '15292780': "15292780", '15274600': "15276000"}

nsrho = 30  # number depths
nrivers = len(station_list_file) 
```

```{code-cell} ipython3
def repeat_years_return_range(values: np.array, start: str, end: str):
    """Repeat values over years represented in start to end and return subset.
    
    The year after the year in end will be included in case hours are needed to be interpolated on the end.
    
    Interpolate to 15 min increments.

    Parameters
    ----------
    values : np.array
        values to match days of year 1 to 366 (includes leap year)
    start : str
        start date time
    end : str
        end date time
    """
    
    print("calculating mean time series")
    
    if len(values) != 366:
        raise ValueError("values should be 366 to match days of year with leap year.")

    # find years covered by requested dates and then repeated stats for necessary 
    # years coverage
    years = sorted(list(set(pd.date_range(start=start, end=end).year)))
    
    # add one more year on so that final day from user date range will for sure have
    # hours included in the interpolation. Otherwise if the end date is 12-31, it will 
    # not have the hours of that day included.
    years += [years[-1] + 1]
    dfs = []
    for year in years:
        time = pd.date_range(start=f"{year}-1-1", end=f"{year}-12-31")
        if not time[0].is_leap_year:
            values_to_use = np.delete(values, 59)  # drop feb 29 if not leap year
        else:
            values_to_use = values

        df = pd.Series(index=time, data=values_to_use)
        dfs.append(df)
        
    stats_repeated = pd.concat(dfs, axis=0)
    # import pdb; pdb.set_trace()
    temps = stats_repeated.resample("15T").interpolate().loc[start.replace("Z",""):end.replace("Z","")]
    
    return temps
```

```{code-cell} ipython3
def extrapolate_rating_curve(ratingDataOrig, extreme_val, which_dir: str):

    dd = 0.01  # resolution of rating curves
    
    # create a linear fit to the last points of the rating curve to use for extrapolation
    if which_dir == "up":
        print(f"max data value: {extreme_val}, max INDEP value is {ratingDataOrig['INDEP'].max()}")
        p = np.polyfit(ratingDataOrig["INDEP"][-10:], ratingDataOrig["DEP"][-10:], 3)
        indep_extension = np.arange(ratingDataOrig["INDEP"].max()+dd, extreme_val+dd, dd).round(2)
        dep_extension = np.polyval(p, indep_extension)
        df_extension = pd.DataFrame(data={"INDEP": indep_extension, "DEP": dep_extension})
        ratingData = pd.concat([ratingDataOrig, df_extension], axis=0)    
        
    elif which_dir == "down":
        print(f"min data value: {extreme_val}, min INDEP value is {ratingDataOrig['INDEP'].min()}")
        # create a linear fit to the last points of the rating curve to use for extrapolation
        p = np.polyfit(ratingDataOrig["INDEP"][:10], ratingDataOrig["DEP"][:10], 3)
        indep_extension = np.arange(extreme_val, ratingDataOrig["INDEP"].min(), dd).round(2)
        if indep_extension[-1] == ratingDataOrig["INDEP"].min():
            indep_extension = np.delete(indep_extension, -1)
        dep_extension = np.polyval(p, indep_extension)
        df_extension = pd.DataFrame(data={"INDEP": indep_extension, "DEP": dep_extension})
        ratingData = pd.concat([df_extension, ratingDataOrig], axis=0)    
        
    return ratingData
```

find_na_groups

```{code-cell} ipython3
def find_na_groups(df):
    """
    
    https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas

    Parameters
    ----------
    df : _type_
        _description_

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    ValueError
        _description_
    """
    # actual groups of nans
    na_groups = df.notna().cumsum().loc[df.isna()].copy()
    
    # # groups of nans plus one on either side (so we can interpolate)
    # ind_wide = df.shift(periods=-1, fill_value=False).isna() | df.shift(periods=1, fill_value=False).isna()
    # nap1_groups = df.notna().cumsum()[ind_wide]
    
    lengths_consecutive_na = na_groups.groupby(na_groups).agg(len)
    
    dt = df.index[1] - df.index[0]
    # make sure dt's are all equal
    if not all(df.index.to_series().diff()[1:] == dt):
        raise ValueError("delta times in indices are not all equal.")
    
    times_consecutive_na = lengths_consecutive_na*dt
    return na_groups, lengths_consecutive_na, times_consecutive_na
```

```{code-cell} ipython3
def find_nap1_groups(df):
    """
    UPDATE
    https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas

    Parameters
    ----------
    df : _type_
        _description_

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    ValueError
        _description_
    """
    # actual groups of nans
    # na_groups = df.notna().cumsum()[df.isna()]
    # import pdb; pdb.set_trace()
    # # groups of nans plus one on either side (so we can interpolate)
    ind_wide = df.shift(periods=-1, fill_value=False).isna() | \
               df.isna() | \
               df.shift(periods=1, fill_value=False).isna()
    # ind_wide = df.shift(periods=-1, fill_value=False).isna() | df.shift(periods=1, fill_value=False).isna()
    na_groups = df.notna().cumsum().loc[ind_wide].copy()
    
    lengths_consecutive_na = na_groups.groupby(na_groups).agg(len)
    
    dt = df.index[1] - df.index[0]
    # make sure dt's are all equal
    if not all(df.index.to_series().diff()[1:] == dt):
        raise ValueError("delta times in indices are not all equal.")
    
    times_consecutive_na = lengths_consecutive_na*dt
    return na_groups, lengths_consecutive_na, times_consecutive_na
```

```{code-cell} ipython3
def return_nwis_data(station, parameter, start, end):
    data = nwis.get_iv(sites=station, parameterCd=parameter, start=start, end=end)[0]
    if data.index.dtype == "O":
        data.index = pd.to_datetime(data.index, utc=True)
    data = data.tz_convert(None)
    return data
    
```

```{code-cell} ipython3
def find_mean_time_series(station: str, start: str, end: str, parameter: str) -> pd.Series:
    """in 15 min intervals

    Parameters
    ----------
    station : str
        _description_
    start : str
        _description_
    end : str
        _description_

    Returns
    -------
    pd.Series
        _description_
    """
    
    # if data is not available at all (outside window of availability) use annual mean
    # Retrieve the statistics
    stats = nwis.get_stats(sites=station, parameterCd=parameter, statReportType="daily", statTypeCd="mean")[0]
    discharge = repeat_years_return_range(stats["mean_va"].values, start, end)
    return discharge
```

```{code-cell} ipython3
def estimate_discharge_from_gage_data(station, gage_data, index):
    
    # try to use gage data instead, but need rating curve data to do so
    ratingDataOrig = nwis.get_ratings(site=station, file_type="exsa")[0]

    # create estimate using rating curve and gage height if discharge data not fully available
    if not ratingDataOrig.empty:
        
        # see if rating curve needs to be extrapolated. Maybe have a warning to check the reasonableness of the
        # output in this case
        if gage_data.max() > ratingDataOrig["INDEP"].max():
            print(f"Extrapolating ratingData upward for station {station}.")
            ratingData = extrapolate_rating_curve(ratingDataOrig, gage_data.max(), "up")
            
        else:
            ratingData = ratingDataOrig

        if gage_data.min() < ratingData["INDEP"].min():
            print(f"Extrapolating ratingData downward for station {station}.")

            ratingData2 = extrapolate_rating_curve(ratingData, gage_data.min(), "down")

        else:
            ratingData2 = ratingData
            
        # Do a little rolling mean to smooth the data — sometimes it's really jumpy
        gage_data = gage_data.rolling(window="24H", center=True).mean()

        streamflow_estimate_for_gage_data = ratingData2.set_index("INDEP")["DEP"].loc[gage_data[gage_data.notnull()].round(2)]

        # cap values more than twice the max measured discharge value
        # https://kacv.net/brad/nws/lesson7.html
        ind = streamflow_estimate_for_gage_data > ratingDataOrig["DEP"].max()*2
        if ind.sum() > 0:
            print("Some estimated discharge values from gage data were capped at twice the rating curve max.")
            streamflow_estimate_for_gage_data.loc[ind] = ratingDataOrig["DEP"].max()*2
        
        # cap min values at 0
        ind = streamflow_estimate_for_gage_data < 0
        if ind.sum() > 0:
            print("Some estimated discharge values from gage data were brought to 0.")
            streamflow_estimate_for_gage_data.loc[ind] = 0

        # combine. Use streamflow estimate anywhere discharge_data has nan's
        # streamflow_estimate_for_gage_data.index = data.index
        streamflow_estimate_for_gage_data.index = gage_data[gage_data.notnull()].index
        
        # reindex to full set of indices
        streamflow_estimate_for_gage_data = streamflow_estimate_for_gage_data.reindex(index)
    else:
        streamflow_estimate_for_gage_data = pd.Series(index=index, data=np.nan)
    
    return streamflow_estimate_for_gage_data
```

```{code-cell} ipython3
# ndays = 8

def replace_over_with_function(time_series, function, function_inputs, ndays):
    # characterize groups of consecutive nans
    na_groups, lengths_consecutive_na, times_consecutive_na = find_na_groups(time_series)
    
    # only use gage data if consecutive nan's over ndays days. In this case create estimate for full time range
    # (as available) and then use whichever parts of it are needed.
    if times_consecutive_na.max() > pd.Timedelta(f"{ndays} days"):
        # print(f"fill consecutive nan gaps of over {ndays} days with function {function}.")
        
        other_time_series = function(*function_inputs)
                    
        ind = times_consecutive_na.loc[na_groups] > pd.Timedelta(f"{ndays} days")
        ind2 = na_groups.loc[ind.values].index
        print(f"fill consecutive nan gaps of over {ndays} days with function {function}.")
        print(f"Dates replaced: {ind2}.")
        
        time_series.loc[ind2] = other_time_series.loc[ind2]

        # # rolling mean of start and stop of new time series to stick in, to ease transitions
        # time_series.loc[ind2] = time_series.rolling(window=f"{ndays}D", center=True).mean().loc[ind2]

    return time_series


def replace_under_with_interpolation(time_series, ndays):
    # characterize groups of consecutive nans
    na_groups, lengths_consecutive_na, times_consecutive_na = find_na_groups(time_series)

    # import pdb; pdb.set_trace()
    # check for under 2 days gaps for interpolation
    if times_consecutive_na.min() <= pd.Timedelta(f"{ndays} days"):
        # print("interpolation")
        
        # characterize groups of consecutive nans (plus one on either side so we can interpolate!)
        na_groupsp1, lengths_consecutive_nap1, times_consecutive_nap1 = find_nap1_groups(time_series)

        # a little more time since have an extra index on either side of the window, not exact
        ind = times_consecutive_nap1.loc[na_groupsp1] <= pd.Timedelta(f"{ndays+.1} days")
        ind2 = na_groupsp1.loc[ind.values].index
        print(f"fill consecutive nan gaps of under {ndays} days by interpolating.")
        print(f"Dates replaced: {ind2}.")

        # time_series.loc[ind2].interpolate(inplace=True)
        time_series.loc[ind2] = time_series.loc[ind2].interpolate()
    return time_series

    
```

```{code-cell} ipython3
def discharge_from_gage_or_mean(station: str, start: str, end: str, ndays):

    # Read in gage data
    data = return_nwis_data(station, "00065", start, end)
    print("Accessed gage data.")

    # if empty use mean data for discharge
    if data.empty:
        print("Gage dataset is empty. Use mean time series.")
        discharge_mean = find_mean_time_series(station, start, end, "00060")
        return discharge_mean
        
    # Make sure there is a row for every 15 min in the time range
    index = pd.date_range(start.replace("Z",""), end.replace("Z",""), freq="15T")
    data = data.reindex(index)
   
    # Fill ice flags with 0s
    flags = (data["00065_cd"] == "P, Ice") | (data["00065_cd"] == "A, Ice")
    if flags.any():
        print("Replacing gage values flagged as iced with nan.")
        data.loc[flags,:] = 0.0
    
    # Fill Eqp flags with nans (to be filled in later)
    flags = (data["00065_cd"] == "P, Eqp") | (data["00065_cd"] == "A, Eqp")
    if flags.any():
        print("Replacing gage values flagged as equipment values with nan.")
        data.loc[flags,:] = np.nan
    
    # Calculate estimate
    discharge_estimate = estimate_discharge_from_gage_data(station, data.loc[:,"00065"], index)
    
    discharge_estimate = replace_over_with_function(discharge_estimate.copy(), find_mean_time_series, (station, start, end, "00060"), ndays)
    
    discharge_estimate = replace_under_with_interpolation(discharge_estimate.copy(), ndays)

    return discharge_estimate
        
```

```{code-cell} ipython3
def process_discharge(discharge_data, window):
    
    print("processing final discharge data\n")

    # average to hourly
    dischargeh = discharge_data.groupby(pd.Grouper(freq='1H')).mean("numeric_only")

    # convert from cubic feet per second to cubic meters per second
    dischargeh *= 0.3048**3

    # messes up the end points
    # # Do a little rolling mean to smooth the data — sometimes it's really jumpy
    # # 3 hours is 3 data points
    # 24 hours is 24*4 data points
    dischargeh = dischargeh.rolling(window=window, center=True).mean()
    # dischargeh = dischargeh.rolling(window=3, center=True).mean()
    
    # fill in nan's if less than 8 days on front or back
    dischargeh = dischargeh.interpolate(method="ffill", limit=8*24*4)
    dischargeh = dischargeh.interpolate(method="bfill", limit=8*24*4)
    
    return dischargeh


def process_temp(data, window):
    
    print("processing final temp data\n")
        
    # bump temps below 1 up to 1 to match NOAA file
    data.loc[data<1] = 1
     
    # average to hourly
    temph = data.groupby(pd.Grouper(freq='1H')).mean("numeric_only")

    # messes up the end points
    # # Do a little rolling mean to smooth the data — sometimes it's really jumpy
    # # 4 hours is 4 data points
    temph = temph.rolling(window=window, center=True).mean()
    
    # fill in nan's if less than 8 days on front or back
    temph = temph.interpolate(method="ffill", limit=8*24*4)
    temph = temph.interpolate(method="bfill", limit=8*24*4)
    
    return temph

```

Discharge function

```{code-cell} ipython3
def find_discharge(station: str, start: str, end: str, ndays, window=24) -> pd.DataFrame:
    
    print(f"Processing discharge for station {station} from {start} to {end}.")

    if pd.Timedelta(f"{ndays} days") < pd.Timestamp(start) - pd.Timestamp(end):
        raise UserWarning("Time range for file creation is shorter than cutoff for interpolation vs. alternative time series.")
    
    # CHANGE VARIABLE NAMES ONCE UPDATED. Also update function names.
    # Read in streamflow data
    data1 = return_nwis_data(station, "00060", start, end)
    print("Accessed discharge data.")
    
    # Check for different scenarios for streamflow data
    
    # if empty try gage data for full time range
    if data1.empty:
        print("Discharge dataset is empty. Check for gage data or use mean time series.")
        discharge = discharge_from_gage_or_mean(station, start, end, ndays)  # for full time range
        # dischargeh = process_discharge(discharge, window=window)
        # return dischargeh
        
    else:
        
        # there might be missing times in the return index
        # Make sure there is a row for every 15 min in the time range
        index = pd.date_range(start.replace("Z",""), end.replace("Z",""), freq="15T")
        data1 = data1.reindex(index)
            
            
        # are all flags "A" or "P"?
        if ((data1["00060_cd"] == "A") | (data1["00060_cd"] == "P")).all():
            print("All discharge flags are good.")
            discharge = data1.loc[:,"00060"]
            
        else:

            # check for questionable estimated data
            flags = (data1["00060_cd"] == "A, e") | (data1["00060_cd"] == "P, e")
            if flags.any():
                print("Some questionable flags present for discharge data.")
                
                # is there good gage data during estimated times?
                data2 = return_nwis_data(station, "00065", 
                                        data1[flags].index[0].strftime("%Y-%m-%dT%H:%MZ"), 
                                        data1[flags].index[-1].strftime("%Y-%m-%dT%H:%MZ"))
                
                # is there gage data and if so, is it good when flags True? (at least 75%)
                if not data2.empty:
                    if ((data2.loc[flags, "00065_cd"] == "A") | (data2.loc[flags, "00065_cd"] == "P")).sum() > len(data2.loc[flags])*.75:
                        
                        # then fill questionable discharge data with nans
                        data1.loc[flags,:] = np.nan
                        print("There is over 75 percent good gage data for the time range of the questionable flags, so naning out the discharge data to use gage data instead.")
                    
                    # otherwise we are just keeping the questionable data
                    else:
                        print("Keeping the discharge data with questionable flags.")
                    
            # check for bad flag data and fill any with nans
            flags = (data1["00060_cd"] == "P, Ice") | (data1["00060_cd"] == "P, Eqp") | (data1["00060_cd"] == "A, Ice") | (data1["00060_cd"] == "A, Eqp")
            if flags.any():
                print("Replacing discharge values flagged as iced with nan.")
                data1.loc[flags,:] = np.nan
            
            discharge = replace_over_with_function(data1["00060"].copy(), discharge_from_gage_or_mean, (station, start, end, ndays), ndays)
            
            discharge = replace_under_with_interpolation(discharge.copy(), ndays)
    
    dischargeh = process_discharge(discharge, window=window)
    
    # check if there are any nan's left
    if dischargeh.isnull().any():
        print('STILL NANS')

    return dischargeh
```

Temperature function

```{code-cell} ipython3
def find_temp(station: str, start: str, end: str, ndays, window=4) -> pd.DataFrame:
    
    print(f"Processing temp for station {station} from {start} to {end}.")

    if pd.Timedelta(f"{ndays} days") < pd.Timestamp(start) - pd.Timestamp(end):
        raise UserWarning("Time range for file creation is shorter than cutoff for interpolation vs. alternative time series.")
    
    data = return_nwis_data(station, "00010", start, end)
    print("Accessed temp data.")

    if station == "15239900":
        print("this station has temp data for several years but the stats don't contain a realistic mean so we have to calculate it ourselves")
        start_local = "2018-4-22T00:00Z"
        end_local = "2023-3-1T00:00Z"
        data = nwis.get_iv(sites="15239900", parameterCd="00010", start=start_local, end=end_local)[0]
        if data.index.dtype == "O":
            data.index = pd.to_datetime(data.index, utc=True)
        data = data.tz_convert(None)

        # catch all non-data values in data and make sure they are nans
        data["00010"] = data["00010"].where(data["00010"] != -999999.0, np.nan)        
        
        # get mean temps by day of year
        vals = data["00010"].groupby(data.index.dayofyear).mean()
        
        temps = repeat_years_return_range(vals.values, start, end)
 

    elif data.empty:
        print("Temp dataset is empty. Use mean time series.")
        # print(f"Using stats for station {station}")
        # if data is not available at all (outside window of availability) use annual mean
        # Retrieve the statistics
        temps = find_mean_time_series(station, start, end, "00010")
        # stats = nwis.get_stats(sites=station, parameterCd="00010", statReportType="daily", statTypeCd="mean")[0]
        # temps = repeat_years_return_range(stats["mean_va"].values, start, end)
        
    else:

        # this will hold the final combined time series
        temps = data["00010"].copy()
        # name will break groupby since starts with 0
        # https://github.com/pandas-dev/pandas/issues/51818
        temps.name = None

        # catch all non-data values in data and make sure they are nans
        temps = temps.where(temps != -999999.0, np.nan)
        
        # might be missing data
        index = pd.date_range(start.replace("Z",""), end.replace("Z",""), freq="15T")
        temps = temps.reindex(index)

        # replace long gaps with mean signal
        temps = replace_over_with_function(temps.copy(), find_mean_time_series, (station, start, end, "00010"), ndays)
        
        temps = replace_under_with_interpolation(temps.copy(), ndays)

    # processing
    temph = process_temp(temps, window=window)
   
    # check if there are any nan's left
    if temph.isnull().any():
        print('STILL NANS')

    # # If there are still nan's, fill with 1s
    # temps = temps.fillna(1)
        
    return temph
```

# Compare with river files

```{code-cell} ipython3
def create_river_forcing_file(start, end, ndays, window=24, skip_last=False):
        
    # create arrays to input in the netcdf files
    index = pd.date_range(start.replace("Z",""), end.replace("Z",""), freq="1H")

    if skip_last:
        index = index[:-1]
        end = index[-1].isoformat()[:16]
    ntimes = len(index)

    # get river data for the time period
    station_discharge, station_temp = {}, {}
    for station in discharge_stations.values():
        station_discharge[station] = find_discharge(station, start, end, ndays, window=window)
    for station in temp_stations.values():
        station_temp[station] = find_temp(station, start, end, ndays, window=window)

    river_transport = np.zeros((ntimes, nrivers))
    river_temp = np.zeros((ntimes, nsrho, nrivers))

    # stations are repeated in a certain order in station_list_file
    for i, station_file in enumerate(station_list_file):
        if discharge_stations[station_file] == "15292780":
            factor = 2
        else:
            factor = 1
        nrepeats = station_list_file.count(station_file)
        river_transport[:,i] = factor*river_sign[i]*station_discharge[discharge_stations[station_file]]/nrepeats
        river_temp[:,:,i] = station_temp[temp_stations[station_file]].values[:,np.newaxis].repeat(nsrho, axis=1)

    # create netcdf files starting from the acquired data
    loc = '../data/nos.ciofs.river.20221216.t00z.nc'
    ds = xr.open_dataset(loc)
    
    vars_to_keep = ["river_names", "river_Xposition", "river_Eposition", "river_direction",
    "river_flag", "river_sign", "river_Vshape"]
    dsnew = ds[vars_to_keep].copy(deep=True)

    # add new variables that include time
    dsnew["river_time"] = ("time", index)
    dsnew["river_transport"] = (("time","river"), river_transport)
    dsnew["river_transport"] = dsnew["river_transport"].astype(np.float32)
    dsnew["river_temp"] = (("time","s_rho","river"), river_temp)
    dsnew["river_temp"] = dsnew["river_temp"].astype(np.float32)
    dsnew["river_salt"] = xr.full_like(dsnew["river_temp"], 0.005)
    dsnew["river_pass"] = xr.full_like(dsnew["river_temp"], 9.96921e+36)
    new_vars = ["river_time", "river_transport", "river_temp", "river_salt", "river_pass"]
    for var in new_vars:
        dsnew[var].attrs = ds[var].attrs
    
    # Update global attributes
    dsnew.attrs["data_source"] = "River discharge from USGS real time, estimated using gage height and rating curve, or from daily statistical mean."
    dsnew.attrs["Temp_source"] = "River T from USGS real time or daily statistical mean."
    dsnew.attrs["Salt_source"] = "Always 0.005"
    dsnew.attrs["institution"] = "Axiom Data Science"
    now = str(pd.Timestamp.now())
    dsnew.attrs["history"] = f"Created {now}. Run using `dataretrieval-python` package and code from Axiom Data Science."
    fname = pd.Timestamp(start).strftime("axiom.ciofs.river.%Y%m%d.nc")
    dsnew.attrs["output_file"] = f"River Forcing file: {fname}"
    dsnew.attrs["source_code"] = "Created using Axiom Data Science software."
    dsnew.attrs["reference"] = "Created by Kristen M. Thyng, Axiom Data Science."

    return dsnew, fname
```

# Make monthly forcing files for 1998 and check them

```{code-cell} ipython3
:tags: [hide-output]



# start_overall, end_overall = "1998-1-1T00:00", "1998-12-31T23:00"
year = 1998
for i in range(1,2):
    if i == 12:
        start, end = f"{year}-{i}-1T00", f"{year+1}-{1}-1T00"
    else:
        start, end = f"{year}-{i}-1T00", f"{year}-{i+1}-1T00"

    ds, fname = create_river_forcing_file(start, end, ndays=8, skip_last=True)
    ds.to_netcdf(fname)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
