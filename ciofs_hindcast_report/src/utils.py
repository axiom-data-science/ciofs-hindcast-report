import pandas as pd
import xarray as xr
import pyproj
import numpy as np


def get_source_names(cat):
    return sorted([source_name for source_name in list(cat) if "_base" not in source_name])


def calculate_julian_days(date_time):
    # date_time = pd.to_datetime(date_time)
    return (date_time - pd.to_datetime(date_time.dt.strftime("%Y-01-01")))/pd.Timedelta("1 day") + 1


def resample(dd, to="5T"):
    if isinstance(dd, (pd.Series,pd.DataFrame)):
        return dd.set_index(dd.cf["T"].name).resample(to).mean().reset_index()
    elif isinstance(dd, (xr.Dataset,xr.DataArray)):
        tkey, xkey, ykey = dd.cf["T"].name, dd.cf["longitude"].name, dd.cf["latitude"].name
        zkey = dd.cf["Z"].name
        # ddtemp = dd.resample({tkey: to}).mean(keep_attrs=True)
        # # also bring along lon, lat, depth in case they have been dropped 
        # if xkey not in ddtemp.coords:
        #     ddtemp[xkey] = dd[xkey].resample({tkey: to}).mean(keep_attrs=True)
        
        # for key in [tkey, xkey, ykey, zkey]:
        #     ddtemp[key].attrs = dd[key].attrs
        # in the case that coords besides time are varying with time but aren't independent, they will be 
        # dropped unless forced to come along as data variables. In this case we need to reassign
        # as coordinates afterward.
        # Not sure this solution will work for gridded datasets — might need another case for that
        return dd.reset_coords([zkey, ykey, xkey]).resample({tkey: to}).mean(keep_attrs=True).assign_coords({xkey: dd[xkey], ykey: dd[ykey], zkey: dd[zkey]})
    

def calculate_distance(lons, lats):
    """Calculate distance (km), esp for transects."""

    G = pyproj.Geod(ellps='WGS84')
    distance = G.inv(lons[:-1], lats[:-1], lons[1:], lats[1:], )[2]
    distance = np.hstack((np.array([0]), distance))
    distance = distance.cumsum()/1000 # km
    return distance