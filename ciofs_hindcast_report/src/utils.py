from typing import Union
import pandas as pd
import xarray as xr
import numpy as np
import intake
import regex
import ciofs_hindcast_report as chr



def mk_fig(path, label, caption):

    text = f"""

```{{figure}} {path}
---
name: {label}
---
{caption}
```

"""
    return text

def mk_fig_wide(path, label, caption):

    text = f"""

````{{div}} full-width                
```{{figure}} {path}
---
name: {label}
---
{caption}
```
````

"""
    return text

def mk_video_wide(path, label, caption):

    text = f"""

````{{div}} full-width                
```{{figure}} {path}
---
name: {label}
class: video controls
width: 1000px
---
{caption}
```
````

"""
    return text


def get_source_names(cat):
    return sorted([source_name for source_name in list(cat) if "_base" not in source_name and "_all" not in source_name and "_full" not in source_name])


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


def decode_path(path):
    loc = path.stem
    base = path.parent
    suffix = path.suffix
    slug = [slug for slug in chr.slugs if slug in loc][-1]
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    source_name = [source_name for source_name in source_names if source_name in loc][0]
    key_variable = [key_variable for key_variable in chr.vocab.vocab.keys() if key_variable in loc][0]
    stem = f"{slug}_{source_name}_{key_variable}"
    therest = loc.split(stem)[1]
    if len(therest)>0:
        # if there are numbers in the remainder of the file name, we know there is a start and end date
        # and we know the form of it
        if bool(regex.search(r'\d', therest)):
            start_time, end_time = therest.split("_")[1:3]
            ts_mods = "_".join(therest.split("_")[3:])
        else:
            start_time, end_time = None, None
            ts_mods = "_".join(therest.split("_")[1:])
    else:
        start_time, end_time, ts_mods = None, None, None
    return slug, source_name, key_variable, ts_mods, start_time, end_time, base, suffix, path


def group_decoded_paths(paths):
    cols = ["slug", "source_name", "key_variable", "ts_mods", "start_time", "end_time", "base", "suffix", "path"]
    all_desc = pd.DataFrame([chr.src.utils.decode_path(path) for path in paths], columns=cols)
    return all_desc

# Snippet to use for renaming model cache files
# import pathlib
# import re

# # # rename files to update Z index
# # paths = pathlib.Path("/Users/kthyng/Library/Caches/ocean-model-skill-assessor/nwgoa/model_output/").glob("*s_rho_-1.nc")
# # # path = list(paths)[0]
# # for path in paths:
# #     path.rename(str(path).replace("s_rho_-1","s_rho_49"))
# #     # path.rename(str(path).replace("s_rho_-1","s_rho_29"))
# # #     path.rename(path.with_suffix('.txt'))


# # rename files to remove times and leave dates
# paths = pathlib.Path("/Users/kthyng/Library/Caches/ocean-model-skill-assessor/nwgoa/model_output/").glob("*.nc")
# # path = list(paths)[0]
# for path in paths:
#     path.rename(re.sub("(T\d\d:\d\d)", "", str(path)))
