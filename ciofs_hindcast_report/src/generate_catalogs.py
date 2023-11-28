from intake.catalog.local import LocalCatalogEntry
from intake.catalog import Catalog
import intake
import pandas as pd
import ciofs_hindcast_report as chr
import pathlib
import numpy as np
import xarray as xr
import fsspec


key_variables = ["u","v","east","north","along","across", "ssh", "temp","salt"]

def line_depth_dict(x, y, dd, hover=True, title=None, xlabel=None):
    """for property(ies) vs. depth"""

    d = {"kind": "line",
        "y": [dd.cf[ele].name for ele in y] if isinstance(y, list) else dd.cf[y].name,
        "x": [dd.cf[ele].name for ele in x] if isinstance(x, list) else dd.cf[x].name,
        "invert": True,
        "flip_yaxis": True,
        "subplots": True,
        "width": 300,
        "height": 400,
        "shared_axes": False,
        "hover": hover,
        "title": title,
        "value_label": xlabel,
    }
    return d


def line_time_dict(x, y, dd=None, hover=True, subplots=True, title=None):
    """for property(ies) vs. time"""
    if dd is None:
        xuse = x
        yuse = y
    elif dd is not None:
        xuse = [dd.cf[ele].name for ele in x] if isinstance(x, list) else dd.cf[x].name
        yuse = [dd.cf[ele].name for ele in y] if isinstance(y, list) else dd.cf[y].name
    d = {"kind": "line",
        "y": yuse,
        "x": xuse,
        # "invert": True,
        # "flip_yaxis": True,
        "subplots": subplots,
        "width": 900,
        "height": 300,
        "shared_axes": False,
        "hover": hover,
        "title": title,
        "legend": "top",  # legend at top of plot on outside
    }
    return d


def scatter_dict(var, dd, x, y, flip_yaxis=False, hover=False, title=None):
    d = {"kind": "scatter",
          "x": dd.cf[x].name,
          "y": dd.cf[y].name,
          "c": [dd.cf[ele].name for ele in var] if isinstance(var, list) else dd.cf[var].name,
          "clabel": dd.cf[var].name,
          "cmap": chr.cmap[var],
          "width": 500,# 500,
          "height": 300,#400,
          "flip_yaxis": flip_yaxis,
          "shared_axes": False,
          "hover": hover,
          "title": title,
          }
    return d


def map_dict(dd):
    d = {"kind": "scatter",
         "x": dd.cf["longitude"].name,
         "y": dd.cf["latitude"].name,
         "c": "jday",
         "clabel": "Julian Day",
         "cmap": "gray",
         "width": 400,# 500,
         "height": 300,#400, 
         "title": f"Locations",
         "aspect": 'equal',}
    return d


def quadmesh_dict(var, x, y, cmap=None, flip_yaxis=True,dd=None, width=500, height=300, vmax=None,
                  rasterize=True, symmetric=True, dynamic=True, geo=False, tiles=False,
                  xlabel=None, ylabel=None, hover=False, title=None, shared_axes=False):
    title = title or ""
    if vmax is not None:
        clim = (0, vmax)
    else:
        clim = None
    if dd is None:
        varuse = var
        xuse = x
        yuse = y
        cmapuse = cmap
    elif dd is not None:
        xuse = dd.cf[x].name
        yuse = dd.cf[y].name
        varuse = [dd.cf[ele].name for ele in var] if isinstance(var, list) else dd.cf[var].name
        cmapuse = chr.cmap[var]
    
    xlabel = xlabel or xuse
    ylabel = ylabel or yuse
        
    d = {"kind": "quadmesh",
          "x": xuse,
          "y": yuse,
          "z": varuse,
          "clabel": varuse,
          "cmap": cmapuse,
          "width": width,# 500,
          "height": height,#400,
          "flip_yaxis": flip_yaxis,
        #   "rasterize": True,
        "title": title,
          "shared_axes": shared_axes,
          "symmetric": symmetric,
          "hover": hover,
          "rasterize": rasterize, 
          "clim": clim,
          "dynamic": dynamic, # True: dynamicmap if widget, False: converts from dynamicmap to holomap
        #   "widget_location": "bottom",
        "geo": geo,
        "tiles": tiles,
        "xlabel": xlabel,
        "ylabel": ylabel,
          }
    return d


def vector_dict(xname, yname, anglename, magname, dynamic=True, width=500, height=300, 
                geo=False, tiles=False, xlabel=None, ylabel=None):
    xlabel = xlabel or xname
    ylabel = ylabel or yname
    # will come through as dynamicmap if widget
    d = {"kind": "vectorfield",
         "x": xname,
         "y": yname,
         "angle": anglename,
         "mag": magname,
         "hover": False,
       "dynamic": dynamic, # True: dynamicmap if widget, False: converts from dynamicmap to holomap
        #   "widget_location": "bottom",
                  "width": width,# 500,
          "height": height,#400,
        "geo": geo,
        "tiles": tiles,
        "xlabel": xlabel,
        "ylabel": ylabel,
         }
    return d


def add_metadata(dd, maptype, featuretype):
    d = {"minLongitude": float(dd.cf["longitude"].min()),
        "minLatitude": float(dd.cf["latitude"].min()),
        "maxLongitude": float(dd.cf["longitude"].max()),
        "maxLatitude": float(dd.cf["latitude"].max()),
        "minTime": str(dd.cf["T"].values.min()),
        "maxTime": str(dd.cf["T"].values.max()),
        "maptype": maptype,
        "featuretype": featuretype,
        "key_variables": [key_variable for key_variable in key_variables if key_variable in dd.cf.keys()],
        }
    return d


def save_catalog(entries, cat_name, cat_desc=None, cat_meta=None):
    entries_cat = {source_name: LocalCatalogEntry(name=source_name,
                                                  description=values["description"],
                                                  driver=values["driver"],
                                                  args=values["args"],
                                                  metadata=values["metadata"] if "metadata" in values else {},
                                                  direct_access="allow",)
                   for source_name, values in entries.items()}

    # create catalog
    cat = Catalog.from_dict(
        entries_cat,
        name=cat_name,
        description=cat_desc,
        metadata=cat_meta or {},
    )
    
    cat.save(chr.CAT_NAME(cat_name))


def ctd_transects_gwa(slug):
    project_name = "CTD profiles 2012-2021 - GWA"  
    overall_desc = "CTD Transects (GWA): Six repeat transects in Cook Inlet"
    time = "Quarterly repeats from 2012 to 2021"
    included = True
    notes = "Not used in the NWGOA model/data comparison."
    maptype = "line"
    featuretype = "trajectoryProfile"
    map_description = "CTD Transects"
    summary = """
The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    """
    header_names = ["transect_3", "transect_4", "transect_6", "transect_7", "transect_9", "transect_AlongBay"]
    
    urls = ["https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv",
            "https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv",
            "https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv",
            "https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv",
            "https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv",
            "https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv",
            "https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv",
            "https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv",
            "https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv",
            "https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv",
            "https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv",
    ]
    csv_kwargs = dict(parse_dates=[0], dtype={'Transect': 'object'})

    entries = {}
    for url in urls:
        year = pathlib.Path(url).stem.split("_")[-2]
        df = pd.read_csv(url, **csv_kwargs)
        # "Visit" and "Transect" uniquely identify each transect
        for i in set(df.set_index(["Visit", "Transect"]).index):
            visit, transect = i
            name = f"transect_{transect}-{visit}"
            # select transect/date to get metadata
            ddf = getattr(chr.src.process, slug)(df, i)
            
            metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True, title=name),
                                "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True, title=name),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            metadata.update({"urlpath": url})
            entries[name] = {"description": f"Transect {transect}, {visit}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{year}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(visit_transect=i),
                                    },
                            "metadata": metadata}
        entries[f"{year}_base"] = {"description": f"Base for {year}",
                                "driver": "csv",
                                "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                    }
        }

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names or None,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }

    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_2005_noaa(slug):
    project_name = "CTD profiles 2005 - NOAA"
    overall_desc = "CTD Profiles (NOAA): across Cook Inlet"
    time = "One-off CTD profiles in June and July 2005"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles from NOAA.
"""
    urls = ["https://researchworkspace.com/files/39886023/noaa_north.txt",
            "https://researchworkspace.com/files/39886022/noaa_south.txt"]
    # skipping bottom depth, sigma, press
    cols = ["Cruise", "Station", "Type", "mon/day/yr", "hh:mm", "Lon (°E)",	"Lat (°N)", 
            "Temperature [C]", "tran [v]", "fluor [v]", "Depth [m]",  "Salinity [psu]",]
    csv_kwargs = dict(encoding = "ISO-8859-1", sep="\t", parse_dates={'date_time' : [3, 4]},
                      usecols=cols)
                    #   index_col=["date_time","Depth [m]"], usecols=cols)
    
    entries = {}
    for url in urls:
        df = pd.read_csv(url, **csv_kwargs)

        # split into single CTD cast units by station
        stations = sorted(list(set(df["Station"])))
        for station in stations:
            name = f"{station}"
            # select transect/date to get metadata
            ddf = getattr(chr.src.process, slug)(df, station)
            xlabel = str(ddf.cf["T"].iloc[0])
            # xlabel = str(ddf.cf["T"].iloc[0])
            metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            metadata.update({"urlpath": url})
            entries[name] = {"description": f"Station {station}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(station=station),},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": f"simplecache://::{url}",
                                                "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                                }}

        # more catalog-level metadata
        cat_meta = {"map_description": map_description,
                    "summary": summary,
                    "header_names": header_names,
                    "project_name": project_name,
                    "time": time,
                    "included": included,
                    "notes": notes,
                    "featuretype": featuretype,
                    }
            
        save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_usgs_boem(slug):
    project_name = "CTD profiles - USGS BOEM"
    overall_desc = "CTD Profiles (USGS BOEM): across Cook Inlet"
    time = "One-off CTD profiles from 2016 to 2021 in July"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = ["2016", "2017", "2018", "2019", "2021"]
    map_description = "CTD Profiles"
    summary = """USGS Cook Inlet fish and bird survey CTD profiles.
    
CTD profiles collected in Cook Inlet from 2016-2021 by Mayumi Arimitsu as part of BOEM sponsored research on fish and bird distributions in Cook Inlet. The profiles are collected in July for the years 2016-2021.

The scientific project is described here: https://www.usgs.gov/centers/alaska-science-center/science/cook-inlet-seabird-and-forage-fish-study#overview.
"""

    url = "https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv"
    usecols = ['date_time', 'station_number', 'location', 'ctd_latitude',
       'ctd_longitude', 'pressure', 'temp', 'C0Sm', 'DzdtM', 'Par',
       'Sbeox0MgL', 'Sbeox0PS', 'SvCM', 'CStarAt0', 'CStarTr0', 'salt',
       'FlECOAFL', 'TurbWETntu0', 'Ph', 'OxsatMgL']
    csv_kwargs = dict(parse_dates=[0], usecols=usecols)
    # csv_kwargs = dict(parse_dates=[0], index_col=["date_time","pressure"], usecols=usecols)
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = sorted(list(set(df["station_number"])))

    entries = {}

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, slug)(df, station)
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_piatt_speckman_1999(slug):
    project_name = "Piatt Speckman 1995-99"
    overall_desc = "CTD Profiles (Piatt Speckman)"
    time = "One-off CTD profiles April to September 1999"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""

    url = "https://researchworkspace.com/files/42400652/Piatt1999.csv"
    names = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon', 'Lat', 'Bot. Depth',
        'Depth [m]', 'Temperature [C]', 'Salinity [psu]', 'Sigma',
        'Backscatter', 'CHL', 'empty']
    usecols = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon', 'Lat', 'Bot. Depth',
        'Depth [m]', 'Temperature [C]', 'Salinity [psu]', 'Backscatter', 'CHL']
    csv_kwargs = dict(encoding = 'unicode_escape', names=names, header=0, usecols=usecols,
                      parse_dates={"date_time": ["mon/day/yr","hh:mm"]})#, index_col=["date_time", "Depth [m]"])
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = sorted(df["Station"].unique())
    transform_name = "select_by_station"



    entries = {}

    for station in stations:
        name = station
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.select_by_station",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_emap_2002(slug):
    project_name = "emap 2002"
    overall_desc = "CTD Profiles (emap 2002)"
    time = "One-off CTD profiles June to August 2002"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""

    url = "https://researchworkspace.com/files/42199527/emap.csv"
    names = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Depth [m]', 'Press', 'Temperature [C]',
       'Salinity [psu]', 'Sigma', 'O2sat [%]', 'obs [ntu]', 'tobs [ntu]',
       'chl [mg/m3]']
    usecols = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Depth [m]', 'Temperature [C]',
       'Salinity [psu]', 'O2sat [%]', 'obs [ntu]', 'tobs [ntu]',
       'chl [mg/m3]']
    csv_kwargs = dict(encoding = 'unicode_escape',
                      parse_dates={"date_time": ["mon/day/yr","hh:mm"]}, 
                    #   index_col=["date_time", "Depth [m]"],
                      header=0, names=names, usecols=usecols)
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = df["Station"].unique().tolist()
    # these are outside the model domain
    stations_to_remove = [32, 34, 35, 36, 38, 40, 41, 45, 46, 
                          50, 51, 53, 54, 55, 56, 58, 59,
                          60, 61, 62, 63, 64,
                          70,71,72,73,74,75]
    stations = list(set(stations) - set(stations_to_remove))

    entries = {}
    transform_name = "select_by_station"

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        xlabel = str(ddf.cf["T"][0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all_base"] = {"description": f"Base for all stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_all_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}_all",
                                "transform_kwargs": dict(),},
                        }

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_emap_2008(slug):
    project_name = "emap 2008"
    overall_desc = "CTD Profiles (emap 2008)"
    time = "One-off CTD profiles August to October 2008"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""

    url = "https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv"
    usecols = ['StationID', 'Lat', 'Lon', 'Temperature', 'Date', 'Time',"Depth (m)",
       'Salinity (PSU)', 'Oxygen (mg/L)']
    csv_kwargs = dict(parse_dates={"date_time": ["Date","Time"]}, 
                    #   index_col=["date_time","Depth (m)"],
                      usecols=usecols)
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = df["StationID"].unique().tolist()

    entries = {}
    transform_name = "select_by_station"

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        # at least one station (AKCI08-026) is missing location data. 
        # check for this and skip if missing.
        if ddf.cf["longitude"].isnull().all() or ddf.cf["latitude"].isnull().all():
            continue
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_kb_small_mesh_2006(slug):
    project_name = "KB small mesh 2006"
    overall_desc = "CTD Profiles (KB small mesh 2006)"
    time = "One-off CTD profiles May 2006"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""

    url = "https://researchworkspace.com/files/42200009/KBsmallmesh.csv"
    names = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Press', 'Temperature [C]', 'fluor [v]',
       'tran [v]', 'sbeoxv', 'PAR', 'Depth [m]', 'Salinity [psu]', 'Sigma',
       'oxconc', 'oxper [%]']
    usecols = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Temperature [C]', 'fluor [v]',
       'tran [v]', 'sbeoxv', 'PAR', 'Depth [m]', 'Salinity [psu]', 
       'oxconc', 'oxper [%]']
    csv_kwargs = dict(encoding = 'unicode_escape',
                      parse_dates={"date_time": ["mon/day/yr","hh:mm"]}, 
                    #   index_col=["date_time", "Depth [m]"],
                      header=0, names=names, usecols=usecols)
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = df["Station"].unique().tolist()

    entries = {}
    transform_name = "select_by_station"

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_kbay_osu_2007(slug):
    project_name = "Kbay OSU 2007"
    overall_desc = "CTD Profiles (Kbay OSU 2007)"
    time = "One-off CTD profiles September 2007"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""

    url = "https://researchworkspace.com/files/39888023/kbay_odv.txt"
    names = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Pressure [dB]', 'Temperature [C]',
       'Conductivity', 'Chlorophyll', 'Turbidity', 'Oxygen [%]', 'Par',
       'Depth', 'Salinity [PSU]', 'Sigma-theta', 'Decent Rate']
    usecols = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Temperature [C]',
       'Conductivity', 'Chlorophyll', 'Turbidity', 'Oxygen [%]', 'Par',
       'Depth', 'Salinity [PSU]', 'Decent Rate']
    csv_kwargs = dict(encoding = 'unicode_escape', sep="\t",
                      parse_dates={"date_time": ["mon/day/yr","hh:mm"]}, 
                    #   index_col=["date_time", "Depth"],
                      header=0, names=names, usecols=usecols)
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = df["Station"].unique().tolist()

    entries = {}
    transform_name = "select_by_station"

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_north_gulf_small_mesh_2005(slug):
    project_name = "North Gulf small mesh 2005"
    overall_desc = "CTD Profiles (North Gulf small mesh 2005)"
    time = "One-off CTD profiles May 2005"
    included = False
    notes = "Outside the model domain"
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""

    url = "https://researchworkspace.com/files/42200015/NGASS.csv"
    names = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Depth [m]', 'Temp [c]',
       'Density [sigma]', 'Salinity [PSU]', 'Flourometer [v]',
       'Transmissometer [v]', 'PAR']
    usecols = ['Cruise', 'Station', 'Type', 'mon/day/yr', 'hh:mm', 'Lon',
       'Lat', 'Bot. Depth [m]', 'Depth [m]', 'Temp [c]',
       'Salinity [PSU]', 'Flourometer [v]',
       'Transmissometer [v]', 'PAR']
    csv_kwargs = dict(encoding = 'unicode_escape',
                      parse_dates={"date_time": ["mon/day/yr","hh:mm"]}, 
                    #   index_col=["date_time", "Depth [m]"],
                      header=0, names=names, usecols=usecols)
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = df["Station"].unique().tolist()

    entries = {}
    transform_name = "select_by_station"

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_kachemack_kuletz_2005_2007(slug):
    project_name = "Kachemak Kuletz 2005-2007"
    overall_desc = "CTD Profiles (Kachemak Kuletz 2005-2007)"
    time = "One-off CTD profiles June-July 2005 and July 2006 and 2007"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "profile"
    header_names = None
    map_description = "CTD Profiles"
    summary = """CTD Profiles in Cook Inlet"""
    
    url = "https://researchworkspace.com/files/42403574/Kuletz.csv"

    csv_kwargs = dict(parse_dates=["date_time"], 
                    #   index_col=["date_time", "Depth [m]"],
                      )
    df = pd.read_csv(url, **csv_kwargs)    
    # split into single CTD cast units by station
    stations = df["Station"].unique().tolist()

    entries = {}
    transform_name = "select_by_station"

    for station in stations:
        name = f"{station}"
        # process dataframe so can get metadata
        ddf = getattr(chr.src.process, transform_name)(df, station)
        xlabel = str(ddf.cf["T"].iloc[0])
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    entries[f"{slug}_all"] = {"description": f"All stations",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


# def ctd_profiles_pogibshi_2002(slug):
#     project_name = "Pogibshi 2002"
#     overall_desc = "CTD Profiles (Pogibshi 2002)"
#     time = "One-off CTD profiles July 25, 2002"
#     included = True
#     notes = ""
#     maptype = "point"
#     featuretype = "profile"
#     header_names = None
#     map_description = "CTD Profiles"
#     summary = """CTD Profiles in Cook Inlet"""

#     url = "https://researchworkspace.com/files/42199989/pogibshi_Jul-02.csv"
#     csv_kwargs = dict(encoding = 'unicode_escape',
#                       parse_dates={"date_time": ["Date","Time (local 24 hr)"]}, 
#                       index_col=["date_time", "Depth"])
#     df = pd.read_csv(url, **csv_kwargs)    
#     # split into single CTD cast units by station
#     stations = df["Station"].unique().tolist()

#     entries = {}
#     transform_name = "select_by_station_ak2utc"

#     for station in stations:
#         name = f"{station}"
#         # process dataframe so can get metadata
#         ddf = getattr(chr.src.process, transform_name)(df, station)
#         xlabel = str(ddf.cf["T"][0])
#         metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf, xlabel=xlabel),}}
#         metadata.update(add_metadata(ddf, maptype, featuretype))
#         metadata.update({"urlpath": url})
#         entries[name] = {"description": f"Station {station}",
#                         "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
#                         "args": {"targets": [f"{slug}_base"],
#                                 "transform": f"ciofs_hindcast_report.src.process.{transform_name}",
#                                 "transform_kwargs": dict(station=station),},
#                         "metadata": metadata}
#     entries[f"{slug}_base"] = {"description": f"Base for {name}",
#                             "driver": "csv",
#                             "args": {"urlpath": f"simplecache://::{url}",
#                                         "csv_kwargs": csv_kwargs,
#                                         "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
#                                                                                 "same_names": True,}}
#                                         }}
#     entries[f"{slug}_all"] = {"description": f"All stations",
#                             "driver": "csv",
#                             "args": {"urlpath": f"simplecache://::{url}",
#                                         "csv_kwargs": csv_kwargs,
#                                         "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
#                                                                                 "same_names": True,}}
#                                         }}

#     # more catalog-level metadata
#     cat_meta = {"map_description": map_description,
#                 "summary": summary,
#                 "header_names": header_names,
#                 "project_name": project_name,
#                 "time": time,
#                 "included": included,
#                 "notes": notes,
#                 "featuretype": featuretype,
#                 }
        
#     save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_towed_otf_kbnerr(slug):
    project_name = "CTD Towed 2003 - OTF KBNERR"
    overall_desc = "Towed CTD (OTF KBNERR): central Cook Inlet"
    time = "July 2003, 5min sampling frequency"
    included = True
    notes = "Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency."
    maptype = "point"
    featuretype = "trajectoryProfile"
    # header_names = None
    map_description = "Towed CTD Profiles"
    summary = """Towed CTD Profiles.

Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths
"""

    urls = ["https://researchworkspace.com/files/42202371/mic071303_subsampled.csv",
            "https://researchworkspace.com/files/42202372/mic071903_subsampled.csv",
            "https://researchworkspace.com/files/42202373/mic072003_subsampled.csv",
            "https://researchworkspace.com/files/42202374/mic072103_subsampled.csv",
            "https://researchworkspace.com/files/42202375/mic072203_subsampled.csv",
            "https://researchworkspace.com/files/42202376/mic072403_subsampled.csv",
            "https://researchworkspace.com/files/42202377/mic072503_subsampled.csv",
            "https://researchworkspace.com/files/42202378/mic072603_subsampled.csv",
            "https://researchworkspace.com/files/42202379/mic072803_65-8_subsampled.csv",
            "https://researchworkspace.com/files/42202380/mic072903_subsampled.csv",
            "https://researchworkspace.com/files/42202381/mic073003_subsampled.csv",]
    csv_kwargs = dict(parse_dates=[0])

    entries = {}
    header_names = []
    for url in urls:
        name = pathlib.PurePath(url).stem

        df = pd.read_csv(url, **csv_kwargs)
        title = str(df.cf["T"].iloc[0])
        metadata = {"plots": {"salt": scatter_dict("salt", df, x="distance", y="Z", flip_yaxis=True, title=title),
                            "temp": scatter_dict("temp", df, x="distance", y="Z", flip_yaxis=True, title=title),
                            "map": map_dict(df),}}
        metadata.update(add_metadata(df, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"File {name}",
                        "driver": "csv",
                        "args": {"urlpath": f"simplecache://::{url}",
                                "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                },
                        "metadata": metadata,}
        header_names.extend([name.rstrip("_subsampled")])

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }

    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)    


def adcp_towed_otf_kbnerr(slug):
    project_name = "ADCP towed 2003-2005 - OTF KBNERR"
    overall_desc = "Towed ADCP (OTF KBNERR): central Cook Inlet"
    time = "July 2003"
    included = False
    notes = "There are processed files from 2003. However, they are too short in duration to be useful in comparison to the model output. There are unprocessed files from 2004 and 2005. No further steps were taken with these datasets."
    maptype = "point"
    featuretype = "trajectoryProfile"
    # header_names = None
    map_description = "Towed ADCPs"
    summary = """Towed ADCPs

Short, high resolution towed ADCP in the middle of Cook Inlet
"""

    urls = ["https://researchworkspace.com/files/40337509/OTF20030708110414_000_bp.mat",
            "https://researchworkspace.com/files/40337510/OTF20030708132652_000_bp.mat",
            "https://researchworkspace.com/files/40337511/OTF20030708152426_000_bp.mat",
            "https://researchworkspace.com/files/40337512/OTF20030709062221_000_bp.mat",
            "https://researchworkspace.com/files/40337513/OTF20030709062804_000_bp.mat",
            "https://researchworkspace.com/files/40337514/OTF20030710113053_000_bp.mat",
            "https://researchworkspace.com/files/40337515/OTF20030710133148_000_bp.mat",
            "https://researchworkspace.com/files/40337516/OTF20030710143516_000_bp.mat",
            "https://researchworkspace.com/files/40337517/OTF20030710144435_000_bp.mat",
            "https://researchworkspace.com/files/40337518/OTF20030710164039_000_bp.mat",
            "https://researchworkspace.com/files/40337519/OTF20030711071931_000_bp.mat",
            "https://researchworkspace.com/files/40337520/OTF20030711074806_000_bp.mat",
            "https://researchworkspace.com/files/40337521/OTF20030711100411_000_bp.mat",
            "https://researchworkspace.com/files/40337522/OTF20030711112007_000_bp.mat",
            "https://researchworkspace.com/files/40337523/OTF20030711112103_000_bp.mat",
            "https://researchworkspace.com/files/40337524/OTF20030714132157_000_bp.mat",
            "https://researchworkspace.com/files/40337525/OTF20030719064121_000_bp.mat",
            "https://researchworkspace.com/files/40337526/OTF20030722111506_000_bp.mat",
            "https://researchworkspace.com/files/40337527/OTF20030724113401_000_bp.mat",
            "https://researchworkspace.com/files/40337528/OTF20030724134054_000_bp.mat",
            "https://researchworkspace.com/files/40337529/OTF20030724141257_000_bp.mat",
            "https://researchworkspace.com/files/40337530/OTF20030724150005_000_bp.mat",
            "https://researchworkspace.com/files/40337531/OTF20030725065556_000_bp.mat",
            "https://researchworkspace.com/files/40337532/OTF20030725074445_000_bp.mat",
            "https://researchworkspace.com/files/40337533/OTF20030726110828_000_bp.mat",
            "https://researchworkspace.com/files/40337534/OTF20030728113330_000_bp.mat",
            "https://researchworkspace.com/files/40337508/OTF20030728145659_000_bp.mat"]

    entries = {}
    for url in urls:
        name = pathlib.PurePath(url).stem

        metadata = {"featuretype": featuretype, "urlpath": url}
        entries[name] = {"description": f"File {name}",
                        "driver": "csv",
                        "args": {"urlpath": url},
                        "metadata": metadata,}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": None,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }

    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)    
    

def ctd_towed_ferry_noaa_pmel(slug):
    project_name = "CTD Towed 2004-2008 Ferry in-line - NOAA PMEL"
    overall_desc = "Underway CTD (NOAA PMEL): Towed on ferry"
    time = "Continuous 2004 to 2008, 5min sampling frequency"
    included = True
    notes = "The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency."
    maptype = "point"
    featuretype = "trajectory"
    map_description = "Towed CTD Paths"
    summary = """
An oceanographic monitoring system aboard the Alaska Marine Highway System ferry Tustumena operated for four years in the Alaska Coastal Current (ACC) with funding from the Exxon Valdez Oil Spill Trustee Council's Gulf Ecosystem Monitoring Program, the North Pacific Research Board and the National Oceanic and Atmospheric Administration. An electronic public display aboard the ferry educated passengers about the local oceanography and mapped the ferry's progress. Sampling water at 4 m, the underway system measured: (1) temperature and salinity (used in the present report), and (2) nitrate,
(3) chlorophyll fluorescence, (4) colored dissolved organic matter fluorescence, and (5) optical beam transmittance (not used in report).

Nominal 4 meter depth.

NORTH PACIFIC RESEARCH BOARD PROJECT FINAL REPORT
Alaskan Ferry Oceanographic Monitoring in the Gulf of Alaska
NPRB Project 707 Final Report
Edward D. Cokelet and Calvin W. Mordy.
https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Final_Report_NPRB_0707.pdf

Exxon Valdez Oil Spill Gulf Ecosystem
Monitoring and Research Project Final Report
Biophysical Observations Aboard Alaska Marine Highway System Ferries
Gulf Ecosystem Monitoring and Research Project 040699
Final Report
Edward D. Cokelet, Calvin W. Mordy, Antonio J. Jenkins, W. Scott Pegau
https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Final_Report_GEM_040699.pdf

Archive: https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.nodc%3A0070122/html

![pic](https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/about/0070122_map.jpg)
"""
    
    url = "https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc"
    with fsspec.open(url) as f:
        ds = xr.open_dataset(f)
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        entries = {}
        header_names = ["2004", "2005", "2006", "2007", "2008"]
        for year in header_names:
            for month in months:

                dsd = getattr(chr.src.process, slug)(ds, year, month)
                # not all month-years present in data
                if dsd["T_30_EQ_AX"].size == 0:
                    continue

                name = f"{year}-{month}"
                metadata = {"plots": {"salt": scatter_dict("salt", dsd, x="longitude", y="latitude", flip_yaxis=False),
                                    "temp": scatter_dict("temp", dsd, x="longitude", y="latitude", flip_yaxis=False),}}
                metadata.update(add_metadata(dsd, maptype, featuretype))
                metadata.update({"urlpath": url})
                entries[name] = {"description": f"{year}, month {month}",
                                "driver": "ciofs_hindcast_report.src.process.DatasetTransform",
                                "args": {"targets": [f"{slug}_base"],
                                        "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                        "transform_kwargs": dict(year=year, month=month),
                                            "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                    "same_names": True,}}
                                        },
                                "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {slug}",
                               "driver": "netcdf",
                               "args": {"urlpath": f"simplecache://::{url}"}}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names or None,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
    
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_transects_otf_kbnerr(slug):
    project_name = "CTD profiles 2003-2006 - OTF KBNERR"
    overall_desc = "CTD Transect (OTF KBNERR): Repeated from Anchor Point"
    time = "Daily in July, 2003 to 2006"
    included = True
    notes = "These data were not included in the NWGOA model/data comparison"
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = ["2003", "2004", "2005", "2006"]
    map_description = "CTD Transects"
    summary = """CTD Transect Across Anchor Point, for GEM Project 030670.

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf
Project description: https://evostc.state.ak.us/restoration-projects/project-search/monitoring-dynamics-of-the-alaska-coastal-current-and-development-of-applications-for-management-of-cook-inlet-salmon-040670/
"""

    urls = ["https://researchworkspace.com/files/39890736/otf2003_sbe19.txt",
            "https://researchworkspace.com/files/39890793/otf2003_sbe25.txt",
            "https://researchworkspace.com/files/39886054/otf2004.txt",
            "https://researchworkspace.com/files/39886055/otf2005.txt",
            "https://researchworkspace.com/files/39886053/otf2006.txt"]
    csv_kwargs = dict(encoding = "ISO-8859-1", sep="\t", parse_dates={"date_time": ["mon/day/yr","hh:mm"]},
                    dtype={'Depth [m]': 'float64', 'O2 [%sat]': 'float64', 'Station': 'float64'})
    # minlon, minlat, maxlon, maxlat = -152.438333, 59.825, -152.151667, 59.87333
    years = [2003, 2004, 2005, 2006]
    entries = {}
    # month = 7
    for year in years:            
        for day in np.arange(1,31):
            day = int(day)
            name = f"{year}-07-{str(day).zfill(2)}"        
            # 2003 is split into two files
            if year == 2003:
                if day <= 15:
                    url = "https://researchworkspace.com/files/39890736/otf2003_sbe19.txt"
                else:
                    url = "https://researchworkspace.com/files/39890793/otf2003_sbe25.txt"
            else:
                url = [url for url in urls if str(year) in url][0]
            df = pd.read_csv(url, **csv_kwargs)
            ddf = getattr(chr.src.process, slug)(df, year, day)
            # at least one day is missed
            if len(ddf.reset_index(drop=True).dropna(subset="date_time")) == 0:
                continue
            metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True),
                                "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            metadata.update({"urlpath": url})
            entries[name] = {"description": f"{name}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(year=year, day=day),},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": f"simplecache://::{url}",
                                             "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                             }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_transects_cmi_uaf(slug):
    project_name = "CTD profiles 2004-2005 - CMI UAF"
    overall_desc = "CTD Transect (CMI UAF): from East Foreland Lighthouse"
    time = "10 cruises, approximately monthly for summer months, in 2004 and 2005"
    included = True
    notes = "Used in the NWGOA model/data comparison."
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "CTD Transects"
    summary = """Seasonality of Boundary Conditions for Cook Inlet, Alaska: Transect (3) at East Foreland Lighthouse.

9 CTD profiles at stations across 10 cruises in (approximately) the same locations. Approximately monthly for summer months, 2004 and 2005.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf
"""

    entries = {}
    url = "https://researchworkspace.com/files/39886038/all_forelands_ctd.txt"
    csv_kwargs = dict(sep="\t", dtype={"Month": "str", "Year": "str", "Day": "str", "Hour": "str", "Minute": "str"})
    df = pd.read_csv(url, **csv_kwargs)
    # we can just know this
    cruises = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for cruise in cruises:

        # select cruise to get metadata
        ddf = getattr(chr.src.process, slug)(df.copy(), cruise)
        name = f"Cruise-{str(cruise).zfill(2)}"
        title = f"{str(ddf.cf['T'].iloc[0].date())}"
        # title = f"{str(ddf.cf['T'].iloc[0].date())}"
        metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True, title=title),
                            "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True, title=title),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"Cruise {cruise}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": dict(cruise=cruise),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for all sources",
                            "driver": "csv",
                            "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_transects_cmi_kbnerr(slug):
    project_name = "CTD profiles 2004-2006 - CMI KBNERR"
    overall_desc = "CTD Transects, Moored CTD (CMI KBNERR): Six repeat, one single transect, one moored CTD"
    time = "From 2004 to 2006"
    included = True
    notes = "Used in the NWGOA model/data comparison."
    maptype = "point"
    header_names = ["Cruise_00", "Cruise_01", "Cruise_02", "Cruise_03", "Cruise_05", "Cruise_06", "Cruise_07",
                    "Cruise_08", "Cruise_09", "Cruise_10", "Cruise_11", "Cruise_12", "Cruise_13", "Cruise_14", "Cruise_15", "Cruise_16", "Kbay_timeseries", "sue_shelikof"]
    map_description = "CTD Transects"
    summary = f"""Seasonality of Boundary Conditions for Cook Inlet, Alaska

During 2004 to 2006 we collected hydrographic measurements along transect lines crossing: 1) Kennedy Entrance and Stevenson Entrance from Port Chatham to Shuyak Island; 2) Shelikof Strait from Shuyak Island to Cape Douglas; 3) Cook Inlet from Red River to Anchor Point; 4) Kachemak Bay from Barbara Point to Bluff Point, and 5) the Forelands from East Foreland to West Foreland. During the third year we added two additional lines; 6) Cape Douglas to Cape Adams, and 7) Magnet Rock to Mount Augustine. The sampling in 2006 focused on the differences in properties during the spring and neap tide periods.

CTD profiles 2004-2005 - CMI UAF seems to be transect 5 of this project.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>
"""
    urls = ["https://researchworkspace.com/files/42202067/cmi_full_v2.csv",
            "https://researchworkspace.com/files/39886046/Kbay_timeseries.txt",
            "https://researchworkspace.com/files/39886061/sue_shelikof.txt",
            ]

    csv_kwargs = []
    csv_kwargs.append(dict(parse_dates=[0]))
    csv_kwargs.append(dict(encoding = "ISO-8859-1", sep="\t", parse_dates={"date_time": ["mon/day/yr","hh:mm [utc]"]}))
    csv_kwargs.append(dict(encoding = "ISO-8859-1", sep="\t", parse_dates={"date_time": ["mon/day/yr","hh:mm"]}))
    
    entries = {} 
    
    # sue_shelikof
    name, ind = "sue_shelikof", 2
    featuretype = "trajectoryProfile"
    process_function = "ctd_transects_cmi_kbnerr_sue_shelikof"
    df = pd.read_csv(urls[ind], **csv_kwargs[ind])
    ddf = getattr(chr.src.process, process_function)(df)
    metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True),
                        "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True),}}
    metadata.update(add_metadata(ddf, maptype, featuretype))
    metadata.update({"urlpath": urls[ind]})
    entries[name] = {"description": f"{name} line",
                    "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{process_function}",
                                    "transform_kwargs": dict(),},
                    "metadata": metadata}
    entries[f"{name}_base"] = {"description": f"Base for {name} sources",
                               "driver": "csv",
                               "args": {"urlpath": f"simplecache://::{urls[ind]}",
                                        "csv_kwargs": csv_kwargs[ind],
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    
    # Kbay_timeseries
    name, ind = "Kbay_timeseries", 1
    featuretype = "trajectoryProfile"
    df = pd.read_csv(urls[ind], **csv_kwargs[ind])
    metadata = {"plots": {"salt": scatter_dict("salt", df, x="T", y="Z", flip_yaxis=True),
                        "temp": scatter_dict("temp", df, x="T", y="Z", flip_yaxis=True),}}
    metadata.update(add_metadata(df, maptype, featuretype))
    metadata.update({"urlpath": urls[ind]})
    entries[name] = {"description": f"{name} line",
                    "driver": "csv",
                    "args": {"urlpath": f"simplecache://::{urls[ind]}",
                             "csv_kwargs": csv_kwargs[ind],
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                             },
                    "metadata": metadata}
    
    # cmi_full_v2
    name, ind = "cmi_full_v2", 0
    featuretype = "trajectoryProfile"
    cruises = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    lines = [1,2,3,4,6,7]
    df = pd.read_csv(urls[ind], **csv_kwargs[ind])
    
    entries[f"{name}_base"] = {"description": f"Base for {name} sources",
                               "driver": "csv",
                               "args": {"urlpath": f"simplecache://::{urls[ind]}",
                                        "csv_kwargs": csv_kwargs[ind],
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    for cruise in cruises:
        for line in lines:
            name_line = f"Cruise_{str(cruise).zfill(2)}-Line_{line}"
            ddf = getattr(chr.src.process, slug)(df, cruise, line)
            # some cruise-line combinations don't exist
            if len(ddf.dropna())==0:
                continue
            title = f"Cruise {str(cruise)}, Line {line} ({str(ddf.cf['T'].dt.date.iloc[0])})"
            metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True, title=title),
                                "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True, title=title),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            metadata.update({"urlpath": urls[ind]})
            entries[name_line] = {"description": f"{name_line}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(cruise=cruise, line=line),},
                            "metadata": metadata}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def moorings_circac(slug):
    project_name = "Mooring from CIRCAC"
    overall_desc = "Mooring (CIRCAC): Central Cook Inlet Mooring"
    time = "Two weeks in August 2006, 15 min sampling"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Time Series Location"
    summary = f"""Central Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

CIRCAC is the Cook Inlet Regional Citizens Advisory Council. It was funded by MMS (pre-BOEM), OCS Study MMS 2009-041 funneled through the Coastal Marine Institute (University of Alaska Fairbanks).

This mooring was damaged so it was removed.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>

"""
    url = "https://researchworkspace.com/files/39886029/xto_mooring_2006.txt"

    csv_kwargs = dict(sep="\t", parse_dates=["Date UTC"])
    df = pd.read_csv(url, **csv_kwargs)
    lon, lat = -(151 + 30.3/60), 60 + 45.7/60
    functionname = "add_location_columns"
    ddf = getattr(chr.src.process, functionname)(df, lon, lat)
    
    entries = {} 
    entries[f"{slug}_base"] = {"description": f"Base for {slug}",
                               "driver": "csv",
                               "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}
    metadata = {"plots": {"data": line_time_dict("T", ["temp", "salt"], ddf, subplots=True),}}
    metadata.update(add_metadata(ddf, maptype, featuretype))
    metadata.update({"urlpath": url})
    entries[slug] = {"description": f"{project_name}",
                    "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                    "args": {"targets": [f"{slug}_base"],
                            "transform": f"ciofs_hindcast_report.src.process.{functionname}",
                            "transform_kwargs": {"lon": lon,
                                                 "lat": lat},},
                    "metadata": metadata}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def moorings_kbnerr(slug):
    
    project_name = "Mooring from KBNERR"
    overall_desc = "Mooring (KBNERR): Lower Cook Inlet Mooring"
    time = "Aug to Oct 2006 and June 2007 to Feb 2008, 15 min sampling"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Time Series Location"
    summary = f"""Lower Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

CIRCAC is the Cook Inlet Regional Citizens Advisory Council. It was funded by MMS (pre-BOEM), OCS Study MMS 2009-041 funneled through the Coastal Marine Institute (University of Alaska Fairbanks).

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>

"""

    urls = ["https://researchworkspace.com/files/39886044/chrome_bay_mooring_deployment_1.txt",
            "https://researchworkspace.com/files/39886045/chrome_bay_mooring_deployment_2.txt"]
    names = ["Deployment1", "Deployment2"]
    csv_kwargs = dict(sep="\t", parse_dates=[0])
    entries = {}
    for url, name in zip(urls, names):
        # print(url, name)
        df = pd.read_csv(url, **csv_kwargs)
        lon, lat = -(151 + 50.860/60), 59 + 12.161/60
        functionname = "add_location_columns"
        ddf = getattr(chr.src.process, functionname)(df, lon, lat)
        # import pdb; pdb.set_trace()
        
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": f"simplecache://::{url}",
                                         "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                         }}
        metadata = {"plots": {"data": line_time_dict("T", ["temp", "salt"], ddf, subplots=True),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"{name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{functionname}",
                                "transform_kwargs": {"lon": lon,
                                                    "lat": lat},},
                        "metadata": metadata}
    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_transects_uaf(slug):
    project_name = "CTD time series UAF"
    overall_desc = "CTD Transects (UAF): Repeated in central Cook Inlet"
    time = "26-hour period on 9-10 August 2003"
    included = True
    notes = "Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison."
    maptype = "line"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "CTD Transects"
    summary = f"""Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles

Surface-to-bottom measurements of temperature, salinity, and transmissivity, as well as measurements of surface currents (vessel drift speeds) were acquired along an east-west section in central Cook Inlet, Alaska during a 26-hour period on 9-10 August 2003. These measurements are used to describe the evolution of frontal features (tide rips) and physical properties along this section during semidiurnal and diurnal tidal cycles. The observation that the amplitude of surface currents is a function of water depth is used to show that strong frontal features occur in association with steep bathymetry. The positions and strengths of these fronts vary with the semidiurnal tide. The presence of freshwater gradients alters the phase and duration of tidal currents across the section. Where mean density-driven flow is northward (along the eastern shore and near Kalgin Island), the onset of northward tidal flow (flood tide) occurs earlier and has longer duration than the onset and duration of northward tidal flow where mean density-driven flow is southward (in the shipping channel). Conversely, where mean density-driven flow is southward (in the shipping channel), the onset of southward tidal flow (ebb tide) occurs earlier and has longer duration than the onset and duration of southward tidal flow along the eastern shore and near Kalgin Island. 

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles
Stephen R. Okkonen
Institute of Marine Science
University of Alaska Fairbanks
Report: https://www.circac.org/wp-content/uploads/Okkonen_2005_hydrography-and-currents-in-Cook-Inlet.pdf
"""

    csv_kwargs = dict(parse_dates=["date_time"])
    url = "https://researchworkspace.com/files/42202256/TS%20downcasts.csv"
    df = pd.read_csv(url, **csv_kwargs)

    transects = [1,2,3,4,5,6,7,8,9]    
    entries = {}
    for transect in transects:
        name = f"Transect_{str(transect).zfill(2)}"
        ddf = getattr(chr.src.process, slug)(df, transect)
        title = f"{str(ddf.cf['T'][0])}"
        metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True, title=title),
                              "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True, title=title),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"{name}",
                         "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                         "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": {"transect": transect},},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {slug}",
                               "driver": "csv",
                               "args": {"urlpath": f"simplecache://::{url}",
                                        "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                        }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_2005_osu(slug):
    project_name = "CTD profiles 2005 - OSU"
    overall_desc = "Moored CTDs (OSU): Time series of CTD profiles at several locations in Cook Inlet"
    time = "June 2005"
    included = False
    notes = "Locations given are too low resolution making them incorrectly on land."
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Repeat CTD Profiles at Several Locations"
    summary = f""""""

    urls = [
            "https://researchworkspace.com/files/39886080/AK060605_001_final_header.txt",  # less than 1 hour, 2 locations
            "https://researchworkspace.com/files/39886081/AK060605_003_final_header.txt",  # 1.5 hrs at 1 location
            "https://researchworkspace.com/files/39886085/AK060605_004_final_header.txt",
            "https://researchworkspace.com/files/39886086/AK060705_001_final_header.txt",
            "https://researchworkspace.com/files/39886087/AK060705_002_final_header.txt",  # 1:13:26.4
            "https://researchworkspace.com/files/39886089/AK060805_001_final_header.txt",  # 4:56:38.4
            "https://researchworkspace.com/files/39886090/AK060805_002_final_header.txt",  # 1:48, 2 locations found
            "https://researchworkspace.com/files/39886092/AK060905_001_final_header.txt",  # 1:55:12, 2 locations
        ]
    dates = [
        "2005-06-06", 
        "2005-06-06", 
        "2005-06-06", 
        "2005-06-07", 
        "2005-06-07", 
        "2005-06-08", 
        "2005-06-08", 
        "2005-06-09"
    ]    

    cols = ["P(dbars)", "Temp-C", "Sal(PSU)", "Latitude", "Longitude", "UTC/GMT_Time"]
    csv_kwargs = dict(sep="\t", usecols=cols)
    entries = {}
    for date, url in zip(dates, urls):
        df = pd.read_csv(url, **csv_kwargs)
        df = getattr(chr.src.process, slug)(df, date)
        # df['UTC/GMT_Time'] = [pd.Timestamp(date) + pd.Timedelta(f"{val*24} hour") for val in df['UTC/GMT_Time']]
        # df.cf["longitude"] *= -1
        lonkey, latkey = df.cf["longitude"].name, df.cf["latitude"].name
        # ll[:,0] longitude, ll[:,1] latitude
        lls = df.drop_duplicates(subset=[lonkey, latkey])[[lonkey, latkey]].values
        for i, ll in enumerate(lls):
            lon, lat = ll
            lon, lat = float(lon), float(lat)
            name = f"{url.split('/')[-1].split('_')[0]}_{i}"
            
            ddf = df[(df.cf["longitude"] == lon) & (df.cf["latitude"] == lat)]
            metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="T", y="Z", flip_yaxis=True),
                                "temp": scatter_dict("temp", ddf, x="T", y="Z", flip_yaxis=True),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            metadata.update({"urlpath": url})
            entries[name] = {"description": f"{name}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": {"date": date, "lon": lon, "lat": lat},},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": f"simplecache://::{url}",
                                                "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                                }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_transects_misc_2002(slug):
    project_name = "CTD transects 2002"
    overall_desc = "CTD transects (2002)"
    time = "2002"
    included = True
    notes = ""
    maptype = "line"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "CTD Transects"
    summary = f"""Miscellaneous CTD transects in Cook Inlet from 2002
"""

    urls = ["https://researchworkspace.com/files/42186319/Bear_Jul-02.csv",
            "https://researchworkspace.com/files/42186397/Cohen.csv",
            "https://researchworkspace.com/files/42199559/Glacier.csv",
            "https://researchworkspace.com/files/42199566/Peterson_Jul-02.csv",
            "https://researchworkspace.com/files/42199989/pogibshi_Jul-02.csv",
            "https://researchworkspace.com/files/42200000/PtAdam_jul-02.csv",]
    
    csv_kwargs = dict(parse_dates={"date_time": ["Date","Time (local 24 hr)"]}, index_col="date_time") 

    # each file is a transect so this is easier than usual for transects
    entries = {}
    for url in urls:
        df = pd.read_csv(url, **csv_kwargs)
        df = getattr(chr.src.process, slug)(df)
        name = pathlib.Path(url).stem
        
        metadata = {"plots": {"salt": scatter_dict("salt", df, x="distance", y="Z", flip_yaxis=True, hover=True),
                            "temp": scatter_dict("temp", df, x="distance", y="Z", flip_yaxis=True, hover=True),}}
        metadata.update(add_metadata(df, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"{name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": {},},
                        "metadata": metadata}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": f"simplecache://::{url}",
                                            "csv_kwargs": csv_kwargs,
                                    "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                            "same_names": True,}}
                                            }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_transects_barabara_to_bluff_2002_2003(slug):
    project_name = "Barabara to Bluff 2002-2003"
    overall_desc = "CTD transects: Barabara to Bluff"
    time = "2002-2003"
    included = True
    notes = ""
    maptype = "line"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "CTD Transects"
    summary = f"""Repeat CTD transect from Barabara to Bluff Point in Cook Inlet from 2002 tp 2003.
"""

    url = "https://researchworkspace.com/files/42396691/barabara.csv"
    csv_kwargs = dict(parse_dates=["date_time"])#, index_col="date_time") 
    df = pd.read_csv(url, **csv_kwargs)

    # each file is a transect so this is easier than usual for transects
    entries = {}
    for cruise in np.arange(1,12):
        # df[df["Cruise"] == f"Cruise {cruise}"]
        name = f"Cruise {cruise}"
        ddf = getattr(chr.src.process, slug)(df, name)
        
        metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="distance", y="Z", flip_yaxis=True, hover=True),
                            "temp": scatter_dict("temp", ddf, x="distance", y="Z", flip_yaxis=True, hover=True),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"{name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": {"cruise": name},},
                        "metadata": metadata}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": f"simplecache://::{url}",
                                            "csv_kwargs": csv_kwargs,
                                    "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                            "same_names": True,}}
                                            }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_towed_gwa(slug):
    project_name = "CTD Towed 2017-2019 - GWA"
    overall_desc = "Underway CTD (GWA): Towed CTD"
    time = "Approximately monthly in summer from 2017 to 2020, 5min sampling frequency"
    included = True
    notes = "Made all longitudes negative west values, converted some local times, 2019 and 2020 only have temperature, ship track outside domain is not included, resampled from 2min to 5min."
    maptype = "point"
    featuretype = "trajectory"
    header_names = ["2017", "2018", "2019", "2020"]
    map_description = "Flow through on Ship of Opportunity"
    summary = f"""Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2017-2020. 2017 and 2018 have salinity and temperature, 2019 and 2020 have only temperature.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project
"""
    
    urls = ["https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv",
            "https://researchworkspace.com/files/42202337/CPR_physical_data_2018_subsetted.csv",
            "https://researchworkspace.com/files/42202339/CPR_physical_data_2019_subsetted.csv",
            "https://researchworkspace.com/files/42202341/CPR_physical_data_2020_subsetted.csv",
            ]
    entries = {}
    csv_kwargs = dict(parse_dates=[0])
    for url in urls:
        year = pathlib.Path(url).stem.split("_")[-2]
        entries[f"{slug}_{year}_base"] = {"description": f"Base for {slug}_{year}",
                                "driver": "csv",
                                "args": {"urlpath": f"simplecache://::{url}",
                                            "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                            }}
        df = pd.read_csv(url, **csv_kwargs)
        # loop over months
        for month in sorted(set(df.cf["T"].dt.month)):
                ddf = getattr(chr.src.process, f"{slug}")(df, month)
                name = f"{str(ddf.cf['T'].dt.date[0])}"
                metadata = {"plots": {"temp": scatter_dict("temp", ddf, x="longitude", y="latitude", flip_yaxis=False, title=name)}}
                if int(year) in [2017,2018]:
                    metadata["plots"].update({"salt": scatter_dict("salt", ddf, x="longitude", y="latitude", flip_yaxis=False, title=name),})
                metadata.update(add_metadata(ddf, maptype, featuretype))
                metadata.update({"urlpath": url})
                entries[name] = {"description": f"{name}",
                                "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                                "args": {"targets": [f"{slug}_{year}_base"],
                                        "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                        "transform_kwargs": {"month": month},},
                                "metadata": metadata}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_towed_gwa_temp(slug):
    project_name = "Temperature towed 2011-2016 - GWA"
    overall_desc = "Underway CTD (GWA): Towed, temperature only"
    time = "Approximately monthly in summer from 2011 to 2016, 5min sampling frequency"
    included = True
    notes = "Converted some local times, ship track outside domain is not included."
    maptype = "point"
    featuretype = "trajectory"
    header_names = ["2011", "2012", "2013", "2014", "2015", "2016"]
    map_description = "Flow through on Ship of Opportunity"
    summary = f"""Temperature only: Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska.

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2011-2016.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project
"""
    
    urls = ["https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv",
            "https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv",
            "https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv",
            "https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv",
            "https://researchworkspace.com/files/42202624/CPR_TemperatureData_2015_subsetted.csv",
            "https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv",]
    csv_kwargs = dict(parse_dates=[0])
    entries = {}
    for url in urls:
        df = pd.read_csv(url, **csv_kwargs)
        for month in sorted(set(df.cf["T"].dt.month)):
            ddf = getattr(chr.src.process, slug)(df, month)
            name = f"{str(ddf.cf['T'].dt.date[0])}"
            metadata = {"plots": {"temp": scatter_dict("temp", ddf, x="longitude", y="latitude", flip_yaxis=False, title=name)}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            metadata.update({"urlpath": url})
            entries[name] = {"description": f"{name}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(month=month),},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": f"simplecache://::{url}",
                                                "csv_kwargs": csv_kwargs,
                                        "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                                                                                "same_names": True,}}
                                                }}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def surface_otf_adfg(slug):
    project_name = "surface Temp Sal - OTF ADF&G"
    overall_desc = "Station Sampling (OTF ADF&G): Long term station sampling"
    time = "Daily sampling mostly in July 1979 to 2021"
    included = False
    notes = "Not used because no times associated with data."
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "Stations"
    summary = """Long term surface sampling

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf
"""

    # only making a pseudo catalog
    entries = {}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs,
                        transform_source_names=None, transform_function=None, transform_kwargs=None):
    # import pdb; pdb.set_trace()
    cat = intake.open_erddap_cat(server="https://erddap.aoos.org/erddap",
        # server="https://erddap.sensors.ioos.us/erddap", # this includes bad stations starting with `ism-`
                                 search_for=stations, 
                                 query_type="union",
                                 name=slug,
                                 description=overall_desc,
                                 use_source_constraints=True,
                                 start_time = "1999-01-01T00:00:00Z",
                                 open_kwargs=open_kwargs,
                                 dropna=True,
                                 mask_failed_qartod=True,
                                 cache_kwargs=dict(cache_storage=f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}")#, same_names=True)
                                 )
    source_names = chr.src.utils.get_source_names(cat)
    
    for source_name in source_names:
        
        # read in info url instead of pinging the actual data
        ddf = pd.read_csv(cat[source_name].metadata["info_url"])
        # this creates an empty DataFrame with column names of the variables in the dataset
        # these can be checked with cf-pandas to fill in variable names in the metadata plots
        ddf = pd.DataFrame(columns=ddf[ddf["Row Type"] == "variable"]["Variable Name"])
        
        # add some metadata
        # first find which variables are available to use in plots for metadata
        all_vars = ["ssh","temp","salt","u","v","speed"]
        vars_to_use, var_names = [], []
        # start with time, longitude, latitude, and depth
        for key in ["T", "longitude","latitude","Z"]:
            var_names.append(ddf.cf[key].name)
        for Var in all_vars:
            try:
                # print(source_name, Var, ddf.cf[Var].shape)
                ddf.cf[Var].name
                vars_to_use.append(Var)
                var_names.append(ddf.cf[Var].name)
                qc_var = ddf.cf[Var].name + "_qc_agg"
                if qc_var in ddf.columns:
                    var_names.append(qc_var)
            except ValueError:
                pass
            # except AttributeError:
            #     import pdb; pdb.set_trace()

        cat[source_name].describe()["metadata"].update({"maptype": maptype,
                                     "featuretype": featuretype,
                                     "plots": {"data": line_time_dict("T", vars_to_use, ddf, subplots=True),},
                                     "urlpath": cat[source_name].metadata["tabledap"],
                                     "key_variables": vars_to_use,},
                                                       )

        cat[source_name].describe()["args"].update({"variables": var_names})        

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
    cat.metadata.update(cat_meta)
    cat.save(chr.CAT_NAME(slug))
    
    # # for select source names, duplicate the entry, make one _base and the other a transform of the base entry
    # # have to recreate the catalog entirely to do this though
    # if transform_source_names is not None:
    #     entries = {}
    #     for source_name in source_names:        
            
    #         if source_name in transform_source_names:
    #             entries[source_name] = {"description": cat[source_name].describe()["description"],
    #                             "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
    #                             "args": {"targets": [f"{source_name}_base"],
    #                                     "transform": f"ciofs_hindcast_report.src.process.{transform_function}",
    #                                     "transform_kwargs": transform_kwargs,},
    #                             "metadata": cat[source_name].describe()["metadata"]}
    #             entries[f"{source_name}_base"] = {"description": f"Base for {cat[source_name].describe()['description']}",
    #                                     "driver": cat[source_name].describe()["driver"],
    #                                     "args": cat[source_name].describe()["args"],}
    #         else:
    #             entries[source_name] = {"description": cat[source_name].describe()["description"],
    #                             "driver": cat[source_name].describe()["driver"],
    #                             "args": cat[source_name].describe()["args"],
    #                             "metadata": cat[source_name].describe()["metadata"],}

    # save_catalog(entries, cat_name=slug, cat_desc=cat.description, cat_meta=cat.metadata)



def moorings_aoos_cdip(slug):
    project_name = "Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP)"
    overall_desc = "Moorings (CDIP): Lower and Central Cook Inlet, Kodiak Island"
    time = "From 2011 to 2023, variable"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Moorings from AOOS/CDIP
"""

    stations = ["aoos_204", 
                "edu_ucsd_cdip_236",
                "central-cook-inlet-175"]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}#, "index_col": "time"}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)


def moorings_noaa(slug):
    project_name = "Moorings from NOAA"
    overall_desc = "Moorings (NOAA): across Cook Inlet"
    time = "From 1999 (and earlier) to 2023, variable"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Moorings from NOAA

Geese Island, Sitkalidak Island, Bear Cove, Anchorage, Kodiak Island, Alitak, Seldovia, Old Harbor, Boulder Point, Albatross Banks, Shelikof Strait
"""

    stations = ["geese-island-gps-tide-buoy", # ssh
                "sitkalidak-island-gps-tide-bu", # ssh
                "noaa_nos_co_ops_9455595", # ssh
                "noaa_nos_co_ops_9455920", # ssh
                # "noaa_nos_co_ops_kdaa2",  # not in our system anymore
                "noaa_nos_co_ops_9457292",
                "noaa_nos_co_ops_9457804",
                "noaa_nos_co_ops_9455500",
                "old-harbor-1",
                "boulder-point",
                # "wmo_46078",  # outside domain
                "wmo_46077",]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}#, "index_col": "time"}
    
    # # if I want to transform any sources
    # transform_source_names=["noaa_nos_co_ops_9455500",
    #                         "noaa_nos_co_ops_9455920",
    #                         "noaa_nos_co_ops_9457804",
    #                         "noaa_nos_co_ops_kdaa2",
    #                         "old-harbor-1",
    #                         "wmo_46077",]
    # transform_function="calculate_anomaly"
    # transform_kwargs = dict()
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs,)
                        # transform_source_names=transform_source_names, transform_function=transform_function,
                        # transform_kwargs=transform_kwargs)


def moorings_nps(slug):
    project_name = "Moorings from National Parks Service (NPS)"
    overall_desc = "Moorings (NPS): Chinitna Bay, Aguchik Island"
    time = "From 2018 to 2019, variable"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Moorings from NPS
"""
    stations = ["chinitna-bay-ak-tide-station-945",
                "aguchik-island-ak-tide-station-9",]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}#, "index_col": "time"}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)


def moorings_uaf(slug):
    project_name = "Moorings from University of Alaska Fairbanks (UAF)"
    overall_desc = "Moorings (UAF): Kodiak Island, Peterson Bay"
    time = "From 2013 to present, variable"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Moorings from UAF
"""

    stations = ["uaf_ocean_acidification_resea_ko",
                "kodiak-burke-o-lator-kodiak-ak",
                "peterson-bay-ak-gnss-r",]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}#, "index_col": "time"}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)
    
    
def moorings_kbnerr_bear_cove_seldovia(slug):
    project_name = "Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)"
    overall_desc = "Moorings (KBNERR): Kachemak Bay: Bear Cove, Seldovia"
    time = "From 2004 to present day, variable"
    included = True
    notes = "These are accessed through AOOS portal/ERDDAP server."
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
* nerrs_kacsdwq :: kacsdwq
* nerrs_kacsswq :: kacsswq

* cdmo_nerrs_bearcove :: This is a different station than kacbcwq, which was active 2002-2003 while this is in 2015. They are also in different locations.
    
More information: https://accs.uaa.alaska.edu/kbnerr/
"""

    stations = ["cdmo_nerrs_bearcove",
                "nerrs_kacsdwq",
                "nerrs_kacsswq"]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}#, "index_col": "time"}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)
    
    
def moorings_kbnerr_homer(slug):
    project_name = "Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)"
    overall_desc = "Moorings (KBNERR): Kachemak Bay, Homer stations"
    time = "From 2003 to present day, variable"
    included = True
    notes = "These are accessed through AOOS portal/ERDDAP server."
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
* nerrs_kachdwq :: kachdwq
* homer-dolphin-surface-water-q :: kachswq
* nerrs_kach3wq :: kach3wq
    
More information: https://accs.uaa.alaska.edu/kbnerr/
"""

    stations = ["nerrs_kachdwq",
                "homer-dolphin-surface-water-q",
                "nerrs_kach3wq",]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}#, "index_col": "time"}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)
    
    
def moorings_kbnerr_historical(slug):
    project_name = "Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)"
    overall_desc = "Moorings (KBNERR): Historical, Kachemak Bay"
    time = "From 2001 to 2003, variable"
    included = True
    notes = "These are accessed from Research Workspace."
    maptype = "point"
    featuretype = "timeSeries"
    header_names = None
    map_description = "Moorings"
    summary = f"""Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
More information: https://accs.uaa.alaska.edu/kbnerr/
"""

    urls = ["https://researchworkspace.com/files/42202441/kacbcwq_subsetted.csv",
            "https://researchworkspace.com/files/42202443/kacdlwq_subsetted.csv",
            "https://researchworkspace.com/files/42202445/kachowq_subsetted.csv",
            "https://researchworkspace.com/files/42202447/kacpgwq_subsetted.csv",
            "https://researchworkspace.com/files/42202449/kacsewq_subsetted.csv",
    ]
    csv_kwargs = dict(parse_dates=[0])#, index_col="DateTimeStamp")
    entries = {}
    for url in urls:
        name = pathlib.PurePath(url).stem.rstrip("_subsetted")
        df = pd.read_csv(url, **csv_kwargs)
        metadata = {"plots": {"data": line_time_dict("T", ["temp", "salt"], df, subplots=True),}}
        metadata.update(add_metadata(df, maptype, featuretype))
        metadata.update({"urlpath": url})
        entries[name] = {"description": f"{name}",
                        "driver": "csv",
                        "args": {"urlpath": url,
                                "csv_kwargs": csv_kwargs},
                        "metadata": metadata}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def adcp_moored_noaa_coi_2005(slug):
    project_name = "Cook Inlet 2005 Current Survey"
    overall_desc = "Moored ADCP (NOAA): ADCP survey Cook Inlet 2005"
    time = "2005, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.
"""

    station_list = ["COI0501", "COI0502", "COI0503", "COI0504", "COI0505",
                "COI0506", "COI0507", "COI0508", "COI0509", "COI0510", "COI0511",
                "COI0512", "COI0513", "COI0514", "COI0515", "COI0516", "COI0517",
                "COI0518", "COI0519", "COI0520", "COI0521", "COI0522", "COI0523",
                "COI0524"]
    
    cat = intake.open_coops_cat(station_list, include_source_metadata=True, description=overall_desc,
                                name=slug, process_adcp=True)
    
    source_names = chr.src.utils.get_source_names(cat)
    for source_name in source_names:
        md_new = {"minLongitude": cat[source_name].metadata["lon"],
                    "maxLongitude": cat[source_name].metadata["lon"],
                    "minLatitude": cat[source_name].metadata["lat"],
                    "maxLatitude": cat[source_name].metadata["lat"],
                    "minTime": cat[source_name].metadata["first_good_data"],
                    "maxTime": cat[source_name].metadata["last_good_data"],
                    "maptype": maptype,
                    "featuretype": featuretype,
                    "key_variables": ["east","north","along","across","speed"],
                    "depths": [bin["depth"] for bin in cat[source_name].s.metadata["bins"]["bins"]],
                    }
        start_date = str(pd.Timestamp(cat[source_name].metadata["first_good_data"]).date())
        title = f"lon: {cat[source_name].metadata['lon']}, lat: {cat[source_name].metadata['lat']}, start date: {start_date}"
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),},
                       "urlpath": f"https://tidesandcurrents.noaa.gov/stationhome.html?id={source_name}"})
        cat[source_name].describe()["metadata"].update(md_new)

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
    cat_meta.update(cat.metadata)
    cat.metadata.update(cat_meta)
    cat.save(chr.CAT_NAME(slug))


def adcp_moored_noaa_coi_other(slug):
    project_name = "Cook Inlet 2002/2003/2004/2008/2012 Current Survey"
    overall_desc = "Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years"
    time = "From 2002 to 2012, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.
"""

    station_list = ["COI0206", "COI0207", "COI0213", "COI0301", "COI0302", "COI0303",
                "COI0306", "COI0307", "COI0418", "COI0419", "COI0420", "COI0421",
                "COI0422", "COI0801", "COI0802", "COI1201", "COI1202", "COI1203",
                "COI1204", "COI1205", "COI1207", "COI1208", "COI1209", "COI1210"]
    
    cat = intake.open_coops_cat(station_list, include_source_metadata=True, description=overall_desc,
                                name=slug, process_adcp=True)
    
    source_names = chr.src.utils.get_source_names(cat)
    for source_name in source_names:
        md_new = {"minLongitude": cat[source_name].metadata["lon"],
                    "maxLongitude": cat[source_name].metadata["lon"],
                    "minLatitude": cat[source_name].metadata["lat"],
                    "maxLatitude": cat[source_name].metadata["lat"],
                    "minTime": cat[source_name].metadata["first_good_data"],
                    "maxTime": cat[source_name].metadata["last_good_data"],
                    "maptype": maptype,
                    "featuretype": featuretype,
                    "key_variables": ["east","north","along","across","speed"],
                    "depths": [bin["depth"] for bin in cat[source_name].s.metadata["bins"]["bins"]],
                    }
        start_date = str(pd.Timestamp(cat[source_name].metadata["first_good_data"]).date())
        title = f"lon: {cat[source_name].metadata['lon']}, lat: {cat[source_name].metadata['lat']}, start date: {start_date}"
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),},
                       "urlpath": f"https://tidesandcurrents.noaa.gov/stationhome.html?id={source_name}"})
        cat[source_name].describe()["metadata"].update(md_new)

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
    cat_meta.update(cat.metadata)
    cat.metadata.update(cat_meta)
    cat.save(chr.CAT_NAME(slug))


def adcp_moored_noaa_kod_1(slug):
    project_name = "Kodiak Island 2009 Current Survey (1)"
    overall_desc = "Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 1"
    time = "2009, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.

Stations "KOD0914", "KOD0915", "KOD0916", "KOD0917", "KOD0918", "KOD0919", "KOD0920" are not included because they are just outside or along the model domain boundary.
"""

    station_list = ["KOD0901", "KOD0902", "KOD0903", "KOD0904", "KOD0905", "KOD0906", "KOD0907", 
                    "KOD0910", "KOD0911", "KOD0912", "KOD0913", 
                    # "KOD0914", "KOD0915", "KOD0916", "KOD0917", "KOD0918", "KOD0919", "KOD0920",  # just outside domain
                    "KOD0921", "KOD0922", "KOD0923", "KOD0924", "KOD0925", ]
                    # "KOD0924", "KOD0925", "KOD0926", "KOD0927", "KOD0928", "KOD0929", "KOD0930", 
                    # "KOD0931", "KOD0932", "KOD0933", "KOD0934", "KOD0935", "KOD0936", "KOD0937", 
                    # "KOD0938", "KOD0939", "KOD0940", "KOD0941", "KOD0942", "KOD0943", "KOD0944", ]
    
    cat = intake.open_coops_cat(station_list, include_source_metadata=True, description=overall_desc,
                                name=slug, process_adcp=True)
    
    source_names = chr.src.utils.get_source_names(cat)
    for source_name in source_names:
        md_new = {"minLongitude": cat[source_name].metadata["lon"],
                    "maxLongitude": cat[source_name].metadata["lon"],
                    "minLatitude": cat[source_name].metadata["lat"],
                    "maxLatitude": cat[source_name].metadata["lat"],
                    "minTime": cat[source_name].metadata["first_good_data"],
                    "maxTime": cat[source_name].metadata["last_good_data"],
                    "maptype": maptype,
                    "featuretype": featuretype,
                    "key_variables": ["east","north","along","across","speed"],
                    "depths": [bin["depth"] for bin in cat[source_name].s.metadata["bins"]["bins"]],
                    }
        start_date = str(pd.Timestamp(cat[source_name].metadata["first_good_data"]).date())
        title = f"lon: {cat[source_name].metadata['lon']}, lat: {cat[source_name].metadata['lat']}, start date: {start_date}"
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),},
                       "urlpath": f"https://tidesandcurrents.noaa.gov/stationhome.html?id={source_name}"})
        cat[source_name].describe()["metadata"].update(md_new)

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
    cat_meta.update(cat.metadata)
    cat.metadata.update(cat_meta)
    cat.save(chr.CAT_NAME(slug))


def adcp_moored_noaa_kod_2(slug):
    project_name = "Kodiak Island 2009 Current Survey (2)"
    overall_desc = "Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 2"
    time = "2009, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.
"""

    station_list = [
                    # "KOD0901", "KOD0902", "KOD0903", "KOD0904", "KOD0905", "KOD0906", "KOD0907", 
                    # "KOD0910", "KOD0911", "KOD0912", "KOD0913", "KOD0914", "KOD0915", "KOD0916", 
                    # "KOD0917", "KOD0918", "KOD0919", "KOD0920", "KOD0921", "KOD0922", "KOD0923", 
                    "KOD0926", "KOD0927", "KOD0928", "KOD0929", "KOD0930", 
                    "KOD0931", "KOD0932", "KOD0933", "KOD0934", "KOD0935", "KOD0936", "KOD0937", 
                    "KOD0938", "KOD0939", "KOD0940", "KOD0941", "KOD0942", "KOD0943", "KOD0944", ]
    
    cat = intake.open_coops_cat(station_list, include_source_metadata=True, description=overall_desc,
                                name=slug, process_adcp=True)
    
    source_names = chr.src.utils.get_source_names(cat)
    for source_name in source_names:
        md_new = {"minLongitude": cat[source_name].metadata["lon"],
                    "maxLongitude": cat[source_name].metadata["lon"],
                    "minLatitude": cat[source_name].metadata["lat"],
                    "maxLatitude": cat[source_name].metadata["lat"],
                    "minTime": cat[source_name].metadata["first_good_data"],
                    "maxTime": cat[source_name].metadata["last_good_data"],
                    "maptype": maptype,
                    "featuretype": featuretype,
                    "key_variables": ["east","north","along","across","speed"],
                    "depths": [bin["depth"] for bin in cat[source_name].s.metadata["bins"]["bins"]],
                    }
        start_date = str(pd.Timestamp(cat[source_name].metadata["first_good_data"]).date())
        title = f"lon: {cat[source_name].metadata['lon']}, lat: {cat[source_name].metadata['lat']}, start date: {start_date}"
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"],
                                                        width=600, title=title),},
                       "urlpath": f"https://tidesandcurrents.noaa.gov/stationhome.html?id={source_name}"})
        cat[source_name].describe()["metadata"].update(md_new)

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
    cat_meta.update(cat.metadata)
    cat.metadata.update(cat_meta)
    cat.save(chr.CAT_NAME(slug))
    

def hfradar(slug):
    project_name = "HF Radar - UAF"
    overall_desc = "HF Radar (UAF)"
    time = "2002-2009"
    included = True
    notes = "These are accessed from Research Workspace where they have already been processed."
    maptype = "box"
    featuretype = "grid"
    header_names = ["Lower CI/System B, 2006-2007: Weekly Subtidal Means",
                    "Lower CI/System B, 2006-2007: Tidal Constituents",
                    "Upper CI/System A, 2002-2003: Weekly Subtidal Means",
                    "Upper CI/System A, 2002-2003: Tidal Constituents",
                    "Upper CI/System A, 2009: Weekly Subtidal Means",
                    "Upper CI/System A, 2009: Tidal Constituents",
                    ]
    map_description = "HF Radar Data Areas"
    summary = f"""HF Radar from UAF.

Files are:
* Upper Cook Inlet (System A): 2002-2003 and 2009
* Lower Cook Inlet (System B): 2006-2007

Data variables available include tidally filtered and weekly averaged along with tidal constituents calculated from hourly data.
    
Some of the data is written up in reports:
* https://espis.boem.gov/final%20reports/5009.pdf
* https://www.govinfo.gov/app/details/GOVPUB-I-47b721482d69e308aec1cca9b3e51955

![pic](https://researchworkspace.com/files/40338104/UAcoverage.gif)
"""

    urls = ["https://researchworkspace.com/files/42712165/lower-ci_system-B_2006-2007.nc",
            "https://researchworkspace.com/files/42712210/lower-ci_system-B_2006-2007_subtidal_weekly_mean.nc",
            "https://researchworkspace.com/files/42712190/lower-ci_system-B_2006-2007_tidecons_base.nc",
            "https://researchworkspace.com/files/42712163/upper-ci_system-A_2002-2003.nc",
            "https://researchworkspace.com/files/42712206/upper-ci_system-A_2002-2003_subtidal_weekly_mean.nc",
            "https://researchworkspace.com/files/42712182/upper-ci_system-A_2002-2003_tidecons_base.nc",
            "https://researchworkspace.com/files/42712167/upper-ci_system-A_2009.nc",
            "https://researchworkspace.com/files/42712214/upper-ci_system-A_2009_subtidal_weekly_mean.nc",
            "https://researchworkspace.com/files/42712200/upper-ci_system-A_2009_tidecons_base.nc",
            ]

    # urls = ["https://researchworkspace.com/files/42394322/upper-ci_system-A_2002-2003_subtidal_weekly_mean.nc",
    #         "https://researchworkspace.com/files/42393592/upper-ci_system-A_2002-2003_tidecons.nc",
    #         "https://researchworkspace.com/files/42394327/lower-ci_system-B_2006-2007_subtidal_weekly_mean.nc",
    #         "https://researchworkspace.com/files/42393598/lower-ci_system-B_2006-2007_tidecons.nc",
    #         "https://researchworkspace.com/files/42394329/upper-ci_system-A_2009_subtidal_weekly_mean.nc",
    #         "https://researchworkspace.com/files/42393604/upper-ci_system-A_2009_tidecons.nc",
    #         "https://researchworkspace.com/files/42390223/upper-ci_system-A_2002-2003.nc",
    #         "https://researchworkspace.com/files/42390219/lower-ci_system-B_2006-2007.nc",
    #         "https://researchworkspace.com/files/42390224/upper-ci_system-A_2009.nc",
    #         ]
            

    # urls = ["https://researchworkspace.com/files/42393590/upper-ci_system-A_2002-2003_subtidal_daily_mean.nc",
    #         "https://researchworkspace.com/files/42393592/upper-ci_system-A_2002-2003_tidecons.nc",
    #         "https://researchworkspace.com/files/42393596/lower-ci_system-B_2006-2007_subtidal_daily_mean.nc",
    #         "https://researchworkspace.com/files/42393598/lower-ci_system-B_2006-2007_tidecons.nc",
    #         "https://researchworkspace.com/files/42393602/upper-ci_system-A_2009_subtidal_daily_mean.nc",
    #         "https://researchworkspace.com/files/42393604/upper-ci_system-A_2009_tidecons.nc"]

    # urls = ["https://researchworkspace.com/files/42392906/upper-ci_system-A_2002-2003_subtidal_daily_mean_tidecons.nc",
    #         "https://researchworkspace.com/files/42392911/lower-ci_system-B_2006-2007_subtidal_daily_mean_tidecons.nc",
    #         "https://researchworkspace.com/files/42392915/upper-ci_system-A_2009_subtidal_daily_mean_tidecons.nc"]
    # urls = ["https://researchworkspace.com/files/42390223/upper-ci_system-A_2002-2003.nc",
    #         "https://researchworkspace.com/files/42390219/lower-ci_system-B_2006-2007.nc",
    #         "https://researchworkspace.com/files/42390224/upper-ci_system-A_2009.nc",]
    # dss = []

    entries = {}
    for url in urls:

        of_local = fsspec.open_local(f"simplecache://::{url}", mode="rb")
        ds = xr.open_dataset(of_local)              
        if "tidecons" in url:
            name = pathlib.Path(url).stem.split("_subtidal")[0]
            metadata = {"plots": {"tidecons": quadmesh_dict("tidecons", ds.cf["longitude"].name, ds.cf["latitude"].name, 
                                                        "cmo.tarn", flip_yaxis=False, rasterize=False, 
                                                        width=700, height=550, dynamic=False, geo=True, tiles=True,
                                                        xlabel="Longitude", ylabel="Latitude", hover=True),
                                                        }}
            metadata.update({"maptype": maptype, "featuretype": featuretype})
        # picking out the full time resolution files so can use them in OMSA
        elif "tidecons" not in url and "subtidal" not in url:
            name = pathlib.Path(url).stem + f"_all"
            metadata = add_metadata(ds, maptype, featuretype)
            metadata["key_variables"] = ["east","north"]
        else:
            name = pathlib.Path(url).stem.split("_subtidal")[0]
            # speed is changed into holomap (static plot) in the data page
            metadata = {"plots": {"speed": quadmesh_dict("speed_subtidal", ds.cf["longitude"].name, ds.cf["latitude"].name, 
                                                        chr.cmap["speed"], width=700, height=550,flip_yaxis=False, rasterize=False, 
                                                        vmax=round(float(ds.speed_subtidal.max())), symmetric=False,
                                                        dynamic=False, geo=True, tiles=True,
                                                        xlabel="Longitude", ylabel="Latitude"),
                                "direction": vector_dict(ds.cf["longitude"].name, ds.cf["latitude"].name, 
                                                        "direction_subtidal", "speed_subtidal", width=700, height=550, 
                                                        geo=True, tiles=True, dynamic=False, 
                                                        xlabel="Longitude", ylabel="Latitude"),}}
            metadata.update(add_metadata(ds, maptype, featuretype))
            metadata["key_variables"] = ["east","north"]
        metadata.update({"urlpath": url})
        entries[name] = {"description": name,
                                "driver": "netcdf",
                                "args": {"urlpath": f"simplecache://::{url}"},
                        # "driver": "ciofs_hindcast_report.src.process.DatasetTransform",
                        # "args": {"targets": [f"{slug}_base"],
                        #         "transform": f"ciofs_hindcast_report.src.process.{slug}",
                        #         "transform_kwargs": dict(year=year, month=month),
                        #             "storage_options": {"simplecache": {"cache_storage": f"{chr.PATH_OUTPUTS_DATA_CACHE / slug}",
                        #                                                     "same_names": True,}}
                        #         },
                        "metadata": metadata}
        # entries[f"{slug}_base"] = {"description": f"Base for {slug}",
        #                         "driver": "netcdf",
        #                         "args": {"urlpath": f"simplecache://::{url}"}
        #                         }

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": header_names or None,
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)
   

# Generate all catalogs
if __name__ == "__main__":
    from time import time
    for slug in chr.slugs:
        if not chr.CAT_NAME(slug).is_file():
            start_time = time()
            getattr(chr.src.generate_catalogs, slug)(slug)
            print(f"Catalog: Slug {slug} required time {time() - start_time}")
