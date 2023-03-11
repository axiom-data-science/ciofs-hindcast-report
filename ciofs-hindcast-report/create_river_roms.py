import dataretrieval.nwis as nwis
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import logging

logging.captureWarnings(True)




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


def repeat_years_return_range(values: np.array, start: str, end: str) -> pd.Series:
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
    
    logging.info("calculating mean time series")
    
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
    temps = stats_repeated.resample("15T").interpolate().loc[start.replace("Z",""):end.replace("Z","")]
    
    return temps


def extrapolate_rating_curve(ratingDataOrig: pd.DataFrame, extreme_val: float, which_dir: str) -> pd.DataFrame:
    """Extrapolate rating curve up or down.

    Parameters
    ----------
    ratingDataOrig : pd.DataFrame
        rating curve data from USGS
    extreme_val : float
        Max or min values of gage data, which is being extrapolated to.
    which_dir : str
        Extrapolate "up" or "down"?

    Returns
    -------
    pd.DataFrame
        extended rating curve to accommodate more extreme values than measured.
    """

    dd = 0.01  # resolution of rating curves
    
    # create a linear fit to the last points of the rating curve to use for extrapolation
    if which_dir == "up":
        logging.info(f"max data value: {extreme_val}, max INDEP value is {ratingDataOrig['INDEP'].max()}")
        p = np.polyfit(ratingDataOrig["INDEP"][-10:], ratingDataOrig["DEP"][-10:], 3)
        indep_extension = np.arange(ratingDataOrig["INDEP"].max()+dd, extreme_val+dd, dd).round(2)
        dep_extension = np.polyval(p, indep_extension)
        df_extension = pd.DataFrame(data={"INDEP": indep_extension, "DEP": dep_extension})
        ratingData = pd.concat([ratingDataOrig, df_extension], axis=0)    
        
    elif which_dir == "down":
        logging.info(f"min data value: {extreme_val}, min INDEP value is {ratingDataOrig['INDEP'].min()}")
        # create a linear fit to the last points of the rating curve to use for extrapolation
        p = np.polyfit(ratingDataOrig["INDEP"][:10], ratingDataOrig["DEP"][:10], 3)
        indep_extension = np.arange(extreme_val, ratingDataOrig["INDEP"].min(), dd).round(2)
        if indep_extension[-1] == ratingDataOrig["INDEP"].min():
            indep_extension = np.delete(indep_extension, -1)
        dep_extension = np.polyval(p, indep_extension)
        df_extension = pd.DataFrame(data={"INDEP": indep_extension, "DEP": dep_extension})
        ratingData = pd.concat([df_extension, ratingDataOrig], axis=0)    
        
    return ratingData


def find_na_groups(df: pd.Series, plus1=False):
    """Find groups of consecutive nans.
    
    https://stackoverflow.com/questions/29007830/identifying-consecutive-nans-with-pandas

    Parameters
    ----------
    df : Series
        Time series to evaluate for nans.
    plus1 : bool
        If True, widen the indices considered to include one before and one after each group of nans. If False, only include the nans in the groups. Default False.

    Returns
    -------
    tuple
        groups of nans, number of nans in each group, time only nans are present

    Raises
    ------
    ValueError
        If the index isn't consistent in time.
    """
    
    if plus1:
        # # groups of nans plus one on either side (so we can interpolate)
        ind = df.shift(periods=-1, fill_value=False).isna() | \
                df.isna() | \
                df.shift(periods=1, fill_value=False).isna()
        
    else:
        ind = df.isna()
    # actual groups of nans
    na_groups = df.notna().cumsum().loc[ind].copy()
    
    lengths_consecutive_na = na_groups.groupby(na_groups).agg(len)
    
    dt = df.index[1] - df.index[0]
    # make sure dt's are all equal
    if not all(df.index.to_series().diff()[1:] == dt):
        raise ValueError("delta times in indices are not all equal.")
    
    times_consecutive_na = lengths_consecutive_na*dt
    return na_groups, lengths_consecutive_na, times_consecutive_na


def return_nwis_data(station: str, parameter: str, start: str, end: str) -> pd.DataFrame:
    """Get the data.

    Parameters
    ----------
    station : str
        which station
    parameter : str
        which parameter ("00010" is temp in Celsius, "00060" is discharge in cubic feet per second), "00065" is gage height in feet.
    start : str
        string of datetime like "2000-1-1T00:00".
    end : str
        string of datetime like "2000-1-1T00:00". To get all of a day use "2000-1-1T23:00".

    Returns
    -------
    pd.DataFrame
        DataFrame of data. Includes flags and other info columns.
    """
    data = nwis.get_iv(sites=station, parameterCd=parameter, start=start, end=end)[0]
    if data.index.dtype == "O":
        data.index = pd.to_datetime(data.index, utc=True)
    data = data.tz_convert(None)
    return data


def find_mean_time_series(station: str, start: str, end: str, parameter: str) -> pd.Series:
    """Return mean signal for station in 15 min intervals.

    Parameters
    ----------
    station : str
        which station
    start : str
        string of datetime like "2000-1-1T00:00".
    end : str
        string of datetime like "2000-1-1T00:00". To get all of a day use "2000-1-1T23:00".
    parameter : str
        which parameter ("00010" is temp in Celsius, "00060" is discharge in cubic feet per second), "00065" is gage height in feet.

    Returns
    -------
    pd.Series
        mean signal for station in 15 min intervals.
    """
    
    # if data is not available at all (outside window of availability) use annual mean
    # Retrieve the statistics
    stats = nwis.get_stats(sites=station, parameterCd=parameter, statReportType="daily", statTypeCd="mean")[0]
    discharge = repeat_years_return_range(stats["mean_va"].values, start, end)
    return discharge


def estimate_discharge_from_gage_data(station: str, gage_data: pd.Series, index: pd.Index) -> pd.Series:
    """Estimate discharge using gage data and the rating curve.

    Parameters
    ----------
    station : str
        which station
    gage_data : pd.Series
        Gage data.
    index : pd.Index
        index of times needed

    Returns
    -------
    pd.Series
        Estimate of discharge from gage data.
    """
    
    # try to use gage data instead, but need rating curve data to do so
    ratingDataOrig = nwis.get_ratings(site=station, file_type="exsa")[0]

    # create estimate using rating curve and gage height if discharge data not fully available
    if not ratingDataOrig.empty:
        
        # see if rating curve needs to be extrapolated. Maybe have a warning to check the reasonableness of the
        # output in this case
        if gage_data.max() > ratingDataOrig["INDEP"].max():
            logging.info(f"Extrapolating ratingData upward for station {station}.")
            ratingData = extrapolate_rating_curve(ratingDataOrig, gage_data.max(), "up")
            
        else:
            ratingData = ratingDataOrig

        if gage_data.min() < ratingData["INDEP"].min():
            logging.info(f"Extrapolating ratingData downward for station {station}.")

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
            logging.info("Some estimated discharge values from gage data were capped at twice the rating curve max.")
            streamflow_estimate_for_gage_data.loc[ind] = ratingDataOrig["DEP"].max()*2
        
        # cap min values at 0
        ind = streamflow_estimate_for_gage_data < 0
        if ind.sum() > 0:
            logging.info("Some estimated discharge values from gage data were brought to 0.")
            streamflow_estimate_for_gage_data.loc[ind] = 0

        # combine. Use streamflow estimate anywhere discharge_data has nan's
        # streamflow_estimate_for_gage_data.index = data.index
        streamflow_estimate_for_gage_data.index = gage_data[gage_data.notnull()].index
        
        # reindex to full set of indices
        streamflow_estimate_for_gage_data = streamflow_estimate_for_gage_data.reindex(index)
    else:
        streamflow_estimate_for_gage_data = pd.Series(index=index, data=np.nan)
    
    return streamflow_estimate_for_gage_data


def replace_over_with_function(time_series: pd.Series, function, function_inputs: tuple, ndays: int) -> pd.Series:
    """Replace groups of nans in time_series longer than ndays with function.

    Parameters
    ----------
    time_series : pd.Series
        time series with values to replace.
    function : function
        what function to use to replace values from time_series
    function_inputs : tuple
        inputs needed for function
    ndays : int
        number of days over which a group of nans should be replaced by function.

    Returns
    -------
    pd.Series
        time_series but possibly with some values replaced using function
    """
    
    # characterize groups of consecutive nans
    na_groups, lengths_consecutive_na, times_consecutive_na = find_na_groups(time_series)
    
    # only use gage data if consecutive nan's over ndays days. In this case create estimate for full time range
    # (as available) and then use whichever parts of it are needed.
    if times_consecutive_na.max() > pd.Timedelta(f"{ndays} days"):
        # logging.info(f"fill consecutive nan gaps of over {ndays} days with function {function}.")
        
        other_time_series = function(*function_inputs)
                    
        ind = times_consecutive_na.loc[na_groups] > pd.Timedelta(f"{ndays} days")
        ind2 = na_groups.loc[ind.values].index
        logging.info(f"fill consecutive nan gaps of over {ndays} days with function {function}.")
        logging.info(f"Dates replaced: {ind2}.")
        
        time_series.loc[ind2] = other_time_series.loc[ind2]

        # # rolling mean of start and stop of new time series to stick in, to ease transitions
        # time_series.loc[ind2] = time_series.rolling(window=f"{ndays}D", center=True).mean().loc[ind2]

    return time_series


def replace_under_with_interpolation(time_series: pd.Series, ndays: int) -> pd.Series:
    """Replace groups of nans in time_series shorter than ndays by interpolation.

    Parameters
    ----------
    time_series : pd.Series
        time series with values to replace.
    ndays : int
        number of days under which a group of nans should be replaced by interpolation.

    Returns
    -------
    pd.Series
        time_series but possibly with some values replaced by interpolation
    """
    # characterize groups of consecutive nans
    na_groups, lengths_consecutive_na, times_consecutive_na = find_na_groups(time_series)

    # import pdb; pdb.set_trace()
    # check for under 2 days gaps for interpolation
    if times_consecutive_na.min() <= pd.Timedelta(f"{ndays} days"):
        # logging.info("interpolation")
        
        # characterize groups of consecutive nans (plus one on either side so we can interpolate!)
        na_groupsp1, lengths_consecutive_nap1, times_consecutive_nap1 = find_na_groups(time_series, plus1=True)

        # a little more time since have an extra index on either side of the window, not exact
        ind = times_consecutive_nap1.loc[na_groupsp1] <= pd.Timedelta(f"{ndays+.1} days")
        ind2 = na_groupsp1.loc[ind.values].index
        logging.info(f"fill consecutive nan gaps of under {ndays} days by interpolating.")
        logging.info(f"Dates replaced: {ind2}.")

        # time_series.loc[ind2].interpolate(inplace=True)
        time_series.loc[ind2] = time_series.loc[ind2].interpolate()
    return time_series


def discharge_from_gage_or_mean(station: str, start: str, end: str, ndays) -> pd.Series:
    """Find discharge from either gage estimate or mean time series.

    Parameters
    ----------
    station : str
        which station
    start : str
        string of datetime like "2000-1-1T00:00".
    end : str
        string of datetime like "2000-1-1T00:00". To get all of a day use "2000-1-1T23:00".
    ndays : _type_
        number of days under which a group of nans should be replaced by interpolation.

    Returns
    -------
    pd.Series
        Discharge time series 
    """

    # Read in gage data
    data = return_nwis_data(station, "00065", start, end)
    logging.info("Accessed gage data.")

    # if empty use mean data for discharge
    if data.empty:
        logging.info("Gage dataset is empty. Use mean time series.")
        discharge_mean = find_mean_time_series(station, start, end, "00060")
        return discharge_mean
        
    # Make sure there is a row for every 15 min in the time range
    index = pd.date_range(start.replace("Z",""), end.replace("Z",""), freq="15T")
    data = data.reindex(index)
   
    # Fill ice flags with 0s
    flags = (data["00065_cd"] == "P, Ice") | (data["00065_cd"] == "A, Ice")
    if flags.any():
        logging.info("Replacing gage values flagged as iced with nan.")
        data.loc[flags,:] = 0.0
    
    # Fill Eqp flags with nans (to be filled in later)
    flags = (data["00065_cd"] == "P, Eqp") | (data["00065_cd"] == "A, Eqp")
    if flags.any():
        logging.info("Replacing gage values flagged as equipment values with nan.")
        data.loc[flags,:] = np.nan
    
    # Calculate estimate
    discharge_estimate = estimate_discharge_from_gage_data(station, data.loc[:,"00065"], index)
    
    discharge_estimate = replace_over_with_function(discharge_estimate.copy(), find_mean_time_series, (station, start, end, "00060"), ndays)
    
    discharge_estimate = replace_under_with_interpolation(discharge_estimate.copy(), ndays)

    return discharge_estimate


def process_discharge(discharge_data: pd.Series, window: int) -> pd.Series:
    """Run final processing on discharge time series.

    Parameters
    ----------
    discharge_data : pd.Series
        Optimal discharge time series
    window : int
        How many data points to rolling mean over. 1 is to not do a rolling mean.

    Returns
    -------
    pd.Series
        Cleaned-up time series
    """
    
    logging.info("processing final discharge data\n")

    # average to hourly
    dischargeh = discharge_data.groupby(pd.Grouper(freq='1H')).mean("numeric_only")

    # convert from cubic feet per second to cubic meters per second
    dischargeh *= 0.3048**3

    # 24 hours is 24*4 data points
    dischargeh = dischargeh.rolling(window=window, center=True).mean()
    
    # fill in nan's if less than 8 days on front or back
    dischargeh = dischargeh.interpolate(method="ffill", limit=8*24*4)
    dischargeh = dischargeh.interpolate(method="bfill", limit=8*24*4)
    
    return dischargeh


def process_temp(data: pd.Series, window: int) -> pd.Series:
    """Run final processing on temperature time series.

    Parameters
    ----------
    data : pd.Series
        Optimal temp time series
    window : int
        How many data points to rolling mean over. 1 is to not do a rolling mean.

    Returns
    -------
    pd.Series
        Cleaned-up time series
    """
    
    logging.info("processing final temp data\n")
        
    # bump temps below 1 up to 1 to match NOAA file
    data.loc[data<1] = 1
     
    # average to hourly
    temph = data.groupby(pd.Grouper(freq='1H')).mean("numeric_only")

    temph = temph.rolling(window=window, center=True).mean()
    
    # fill in nan's if less than 8 days on front or back
    temph = temph.interpolate(method="ffill", limit=8*24*4)
    temph = temph.interpolate(method="bfill", limit=8*24*4)
    
    return temph


def find_discharge(station: str, start: str, end: str, ndays: int, window: int = 12) -> pd.Series:
    """Return a cleaned discharge time series

    Parameters
    ----------
    station : str
        which station
    start : str
        string of datetime like "2000-1-1T00:00".
    end : str
        string of datetime like "2000-1-1T00:00". To get all of a day use "2000-1-1T23:00".
    ndays : int
        number of days under which a group of nans should be replaced by interpolation.
    window : int, optional
        How many data points to rolling mean over. 1 is to not do a rolling mean.

    Returns
    -------
    pd.Series
        Final version of discharge time series
    """
    
    logging.info(f"Processing discharge for station {station} from {start} to {end}.")

    if pd.Timedelta(f"{ndays} days") < pd.Timestamp(start) - pd.Timestamp(end):
        raise UserWarning("Time range for file creation is shorter than cutoff for interpolation vs. alternative time series.")
    
    # Read in streamflow data
    data1 = return_nwis_data(station, "00060", start, end)
    logging.info("Accessed discharge data.")
    
    # if empty try gage data for full time range
    if data1.empty:
        logging.info("Discharge dataset is empty. Check for gage data or use mean time series.")
        discharge = discharge_from_gage_or_mean(station, start, end, ndays)  # for full time range
        
    else:
        
        # there might be missing times in the return index
        # Make sure there is a row for every 15 min in the time range
        index = pd.date_range(start.replace("Z",""), end.replace("Z",""), freq="15T")
        data1 = data1.reindex(index)
            
            
        # are all flags "A" or "P"?
        if ((data1["00060_cd"] == "A") | (data1["00060_cd"] == "P")).all():
            logging.info("All discharge flags are good.")
            discharge = data1.loc[:,"00060"]
            
        else:

            # check for questionable estimated data
            flags = (data1["00060_cd"] == "A, e") | (data1["00060_cd"] == "P, e")
            if flags.any():
                logging.info("Some questionable flags present for discharge data.")
                
                # is there good gage data during estimated times?
                data2 = return_nwis_data(station, "00065", 
                                        data1[flags].index[0].strftime("%Y-%m-%dT%H:%MZ"), 
                                        data1[flags].index[-1].strftime("%Y-%m-%dT%H:%MZ"))
                
                # is there gage data and if so, is it good when flags True? (at least 75%)
                if not data2.empty:
                    if ((data2.loc[flags, "00065_cd"] == "A") | (data2.loc[flags, "00065_cd"] == "P")).sum() > len(data2.loc[flags])*.75:
                        
                        # then fill questionable discharge data with nans
                        data1.loc[flags,:] = np.nan
                        logging.info("There is over 75 percent good gage data for the time range of the questionable flags, so naning out the discharge data to use gage data instead.")
                    
                    # otherwise we are just keeping the questionable data
                    else:
                        logging.info("Keeping the discharge data with questionable flags.")
                    
            # check for bad flag data and fill any with nans
            flags = (data1["00060_cd"] == "P, Ice") | (data1["00060_cd"] == "P, Eqp") | (data1["00060_cd"] == "A, Ice") | (data1["00060_cd"] == "A, Eqp")
            if flags.any():
                logging.info("Replacing discharge values flagged as iced with nan.")
                data1.loc[flags,:] = np.nan
            
            discharge = replace_over_with_function(data1["00060"].copy(), discharge_from_gage_or_mean, (station, start, end, ndays), ndays)
            
            discharge = replace_under_with_interpolation(discharge.copy(), ndays)
    
    dischargeh = process_discharge(discharge, window=window)
    
    # check if there are any nan's left
    if dischargeh.isnull().any():
        logging.info('STILL NANS')

    return dischargeh


def find_temp(station: str, start: str, end: str, ndays: int, window: int = 4) -> pd.DataFrame:
    """Return a cleaned temp time series

    Parameters
    ----------
    station : str
        which station
    start : str
        string of datetime like "2000-1-1T00:00".
    end : str
        string of datetime like "2000-1-1T00:00". To get all of a day use "2000-1-1T23:00".
    ndays : int
        number of days under which a group of nans should be replaced by interpolation.
    window : int, optional
        How many data points to rolling mean over. 1 is to not do a rolling mean.

    Returns
    -------
    pd.Series
        Final version of temp time series
    """
    
    logging.info(f"Processing temp for station {station} from {start} to {end}.")

    if pd.Timedelta(f"{ndays} days") < pd.Timestamp(start) - pd.Timestamp(end):
        raise UserWarning("Time range for file creation is shorter than cutoff for interpolation vs. alternative time series.")
    
    data = return_nwis_data(station, "00010", start, end)
    logging.info("Accessed temp data.")

    if station == "15239900":
        logging.info("this station has temp data for several years but the stats don't contain a realistic mean so we have to calculate it ourselves")
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
        logging.info("Temp dataset is empty. Use mean time series.")
        # logging.info(f"Using stats for station {station}")
        # if data is not available at all (outside window of availability) use annual mean
        # Retrieve the statistics
        temps = find_mean_time_series(station, start, end, "00010")
        
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
        logging.info('STILL NANS')
        
    return temph


def create_river_forcing_file(start: str, end: str, ndays: int, window: int=24, skip_last: bool=False) -> xr.DataArray:
    """Make river forcing file for ROMS.

    Parameters
    ----------
    start : str
        string of datetime like "2000-1-1T00:00".
    end : str
        string of datetime like "2000-1-1T00:00". To get all of a day use "2000-1-1T23:00".
    ndays : int
        number of days under which a group of nans should be replaced by interpolation.
    window : int, optional
        How many data points to rolling mean over. 1 is to not do a rolling mean. Default 24.
    skip_last : bool, optional
        True to leave off last time in time range, by default False

    Returns
    -------
    xr.DataArray
        Contains all river forcing data for ROMS run
    """

    # create log file for each river forcing file
    fname = pd.Timestamp(start).strftime("axiom.ciofs.river.%Y%m%d.txt")
    fname = f"output/river/{fname}"
    file_handler = logging.FileHandler(filename=fname, mode="w")
    handlers = [file_handler]

    logging.basicConfig(
        level=logging.INFO,
        # format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
        format="{L:%(lineno)d} %(message)s",
        handlers=handlers,
    )
        
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
    loc = 'data/nos.ciofs.river.20221216.t00z.nc'
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
    dsnew.attrs["source_code"] = "Created using create_river_roms.py."
    dsnew.attrs["reference"] = "Created by Kristen M. Thyng, Axiom Data Science."

    # stop logging!
    log = logging.getLogger() 
    log.removeHandler(handlers[0])
    handlers[0].flush()
    handlers[0].close()
    return dsnew
