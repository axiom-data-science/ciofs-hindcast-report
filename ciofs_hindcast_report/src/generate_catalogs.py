from intake.catalog.local import LocalCatalogEntry
from intake.catalog import Catalog
import intake
import pandas as pd
import ciofs_hindcast_report as chr
import pathlib
import numpy as np


def line_depth_dict(x, y, dd, hover=True):
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
    }
    return d


def line_time_dict(x, y, dd=None, hover=True):
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
        "subplots": True,
        "width": 600,
        "height": 300,
        "shared_axes": False,
        "hover": hover,
    }
    return d


def scatter_dict(var, dd, x, y, flip_yaxis=False, hover=False):
    d = {"kind": "scatter",
          "x": dd.cf[x].name,
          "y": dd.cf[y].name,
          "c": [dd.cf[ele].name for ele in var] if isinstance(var, list) else dd.cf[var].name,
          "clabel": dd.cf[var].name,
          "cmap": chr.cmap[var],
          "width": 400,# 500,
          "height": 300,#400,
          "flip_yaxis": flip_yaxis,
          "shared_axes": False,
          "hover": hover,
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


def quadmesh_dict(var, x, y, cmap=None, flip_yaxis=True,dd=None, ):
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
        
    d = {"kind": "quadmesh",
          "x": xuse,
          "y": yuse,
          "z": varuse,
          "clabel": varuse,
          "cmap": cmapuse,
          "width": 500,# 500,
          "height": 300,#400,
          "flip_yaxis": flip_yaxis,
        #   "rasterize": True,
          "shared_axes": False,
          "symmetric": True,
          "hover": False,
          "rasterize": True,
          }
    return d


def add_metadata(dd, maptype, featuretype):
    # import pdb; pdb.set_trace()
    d = {"minLongitude": float(dd.cf["longitude"].min()),
        "minLatitude": float(dd.cf["latitude"].min()),
        "maxLongitude": float(dd.cf["longitude"].max()),
        "maxLatitude": float(dd.cf["latitude"].max()),
        "minTime": str(dd.cf["T"].values.min()),
        "maxTime": str(dd.cf["T"].values.max()),
        "maptype": maptype,
        "featuretype": featuretype}
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


def ctd_profiles_gwa(slug):
    # make catalog
    slug = "ctd_profiles_gwa"
    project_name = "CTD profiles 2012-2021 - GWA"  
    overall_desc = "GWA: Six repeat transects in Cook Inlet"
    time = "Quarterly repeats from 2012 to 2021"
    included = True
    notes = "Not used in the NWGOA model/data comparison."
    urls = ["https://workspace.aoos.org/published/file/fb5057ac-0c59-42cf-bf35-efbb38089ee9/CookInletKachemakBay_CTD_2012.csv",
            "https://workspace.aoos.org/published/file/476d2d43-02b2-48ef-8a74-5b6ab1f0eee0/CookInletKachemakBay_CTD_2013.csv",
            "https://workspace.aoos.org/published/file/1a5d6c6c-7f5a-4277-8107-84906a05f60b/CookInletKachemakBay_CTD_2014.csv",
            "https://workspace.aoos.org/published/file/09fbcf0e-7f69-4d1a-a152-798134b16a93/CookInletKachemakBay_CTD_2015.csv",
            "https://workspace.aoos.org/published/file/3c574a94-b352-4f80-8025-0162643a9fed/CookInletKachemakBay_CTD_2016.csv",
            "https://workspace.aoos.org/published/file/9694df98-9f53-4754-839f-89a8905b4360/CookInletKachemakBay_CTD_2017.csv",
            "https://workspace.aoos.org/published/file/f0702df6-c57e-4b79-bb71-02aad49f95c7/CookInletKachemakBay_CTD_2018.csv",
            "https://workspace.aoos.org/published/file/7b956e3a-0be4-4a43-af1f-36694027a321/CookInletKachemakBay_CTD_2019.csv",
            "https://workspace.aoos.org/published/file/8d870168-43ae-4825-a7d6-5b13282814a8/CookInletKachemakBay_CTD_2020.csv",
            "https://workspace.aoos.org/published/file/83a85c3c-8b83-4cc4-a5ee-ccaa00107252/CookInletKachemakBay_CTD_2021.csv",
            "https://workspace.aoos.org/published/file/582f3a27-04b3-4e03-940f-9122f83fd6bc/CookInletKachemakBay_CTD_2022.csv"]
    cols = ["Date", "Time", "Latitude_DD", "Longitude_DD", "Transect", "StationN", "Bottom.Depth", "Depth", 'Temperature_ITS90_DegC', 'Salinity_PSU']
    csv_kwargs = dict(header=1, usecols=cols, dtype={'Transect': 'object', 'Bottom.Depth': 'float64'}, parse_dates=[["Date","Time"]])
    maptype = "line"
    featuretype = "trajectoryProfile"
    map_description = "Transects"
    summary = """
The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    """

    # read in all data together
    dfs = []
    for url in urls:
        dfs.append(pd.read_csv(url, **csv_kwargs))
    df = pd.concat(dfs)

    # assess transect occurrences 
    # transect_list = [sorted(list(set(df["Transect"])))[-2]]
    # transects = {}  # defines transects for dataset
    # # A transect is defined by an identifying number and a date
    # for transect in transect_list:
    #     itransect = df["Transect"] == transect
    #     dates = list(set(df.loc[itransect,:]["Date_Time"].dt.date))
    #     transects[transect] = [dates[i] for i in [0,1,-2,-1]]
    #     # transects[transect] = dates
    # header_names = ["transect_9"]
    # header_names = ["Transect 3", "Transect 4", "Transect 6", "Transect 7", "Transect 9", "Transect AlongBay"]
    header_names = ["transect_3", "transect_4", "transect_6", "transect_7", "transect_9", "transect_AlongBay"]
    # assess transect occurrences 
    transect_list = list(set(df["Transect"]))
    transects = {}  # defines transects for dataset
    # A transect is defined by an identifying number and a date
    for transect in transect_list:
        itransect = df["Transect"] == transect
        dates = list(set(df.loc[itransect,:]["Date_Time"].dt.date))
        transects[transect] = dates

    entries = {}
    for transect, dates in transects.items():
        for date in dates:
            name = f"transect_{transect}-{date}"
            # title = f"Date {date}, Transect {transect}"
            
            # select transect/date to get metadata
            ddf = getattr(chr.src.process, slug)(df, transect, date)

            metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="T", y="Z", flip_yaxis=True),
                                "temp": scatter_dict("temp", ddf, x="T", y="Z", flip_yaxis=True),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            entries[name] = {"description": f"Transect {transect}, {date}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(transect=transect, date=date),},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": [url for url in urls if str(pd.Timestamp(date).year) in url][0],
                                             "csv_kwargs": csv_kwargs}}

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
    overall_desc = "NOAA: Single CTD profiles across Cook Inlet"
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
    csv_kwargs = dict(encoding = "ISO-8859-1", sep="\t", parse_dates={'date_time' : [3, 4]})
        
    # read in all data together
    dfs = []
    for url in urls:
        dfs.append(pd.read_csv(url, **csv_kwargs))
    df = pd.concat(dfs)


    # split into single CTD cast units by station
    stations = sorted(list(set(df["Station"])))

    entries = {}

    # inds = [0,1,-2,-1]
    # for ind in inds:
    #     station = stations[ind]
    for station in stations:
        name = f"{station}"
        # name = f"station_{station}"
        title = f"Station {station}" 

        # select transect/date to get metadata
        ddf = getattr(chr.src.process, slug)(df, station)
        lon, lat = float(ddf.cf["longitude"].min()), float(ddf.cf["latitude"].min())
        # use *_south file for lat<60.2
        if lat < 60.2:
            urlpath = [url for url in urls if "south" in url][0]
        else:
            urlpath = [url for url in urls if "north" in url][0]

        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": urlpath,
                                            "csv_kwargs": csv_kwargs}}

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
    # slug = "ctd_profiles_usgs_boem"
    project_name = "CTD profiles - USGS BOEM"
    overall_desc = "USGS BOEM: Single CTD profiles across Cook Inlet"
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

    url = "https://researchworkspace.com/files/41842273/Arimitsu_CookInlet_CTD.csv"
    cols = ["date","ctd_time [local]", 'station_number', 'location', 'ctd_latitude',
        'ctd_longitude', 'PrdM', 'Tv290C', 'Sal00']
    csv_kwargs = dict(usecols=cols)

    # read in data 
    df = pd.read_csv(url, **csv_kwargs)
    df = getattr(chr.src.process, slug)(df)
    df = df.sort_values(df.cf["T"].name)

    # split into single CTD cast units by station
    stations = sorted(list(set(df["station_number"])))

    entries = {}

    # inds = [0,1,-2,-1]
    # for ind in inds:
    #     station = stations[ind]
    for station in stations:
        name = f"{station}"
        # name = f"station_{station}"
        # title = f"Station {station}" 
        # process dataframe so can get metadata
        ddf = df[df["station_number"] == station]
        metadata = {"plots": {"data": line_depth_dict("Z", ["temp", "salt"], ddf),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        entries[name] = {"description": f"Station {station}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": dict(station=station),},
                        "metadata": metadata}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": url,
                                            "csv_kwargs": csv_kwargs}}

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


def ctd_towed_otf_kbnerr(slug):

    project_name = "CTD Towed 2003 - OTF KBNERR"
    overall_desc = "OTF KBNERR: Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths"
    time = "July 2003, 5min sampling frequency"
    included = True
    notes = "Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency."
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "Towed CTD Profiles"
    summary = """Towed CTD Profiles.
"""

    urls = [
            # "https://researchworkspace.com/files/39891466/mic071203.txt",  # about 30 min long — too short so skipping!
            "https://researchworkspace.com/files/39891468/mic071303.txt",
            "https://researchworkspace.com/files/39891469/mic071903.txt",
            "https://researchworkspace.com/files/39891471/mic072003.txt",
            "https://researchworkspace.com/files/39891473/mic072103.txt",
            "https://researchworkspace.com/files/39891475/mic072203.txt",
            "https://researchworkspace.com/files/39891476/mic072403.txt",
            "https://researchworkspace.com/files/39891478/mic072503.txt",
            "https://researchworkspace.com/files/39891480/mic072603.txt",
            # "https://researchworkspace.com/files/39891481/mic072803_4-5.txt",  # about 30 min long — too short so skipping!
            "https://researchworkspace.com/files/39891483/mic072803_65-8.txt",
            "https://researchworkspace.com/files/39891484/mic072903.txt",
            "https://researchworkspace.com/files/39891464/mic073003.txt",
        ]
    csv_kwargs = dict(sep="\t", parse_dates={"date_time": ['date ', ' time ']}, na_values='      NaN ')

    entries = {}
    for url in urls:
        name = pathlib.PurePath(url).stem

        df = pd.read_csv(url, **csv_kwargs)
        df = getattr(chr.src.process, slug)(df)

        metadata = {"plots": {"salt": scatter_dict("salt", df, x="T", y="Z", flip_yaxis=True),
                            "temp": scatter_dict("temp", df, x="T", y="Z", flip_yaxis=True),
                            "map": map_dict(df),}}
        metadata.update(add_metadata(df, maptype, featuretype))
        entries[name] = {"description": f"File {name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": dict()},
                        "metadata": metadata,}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": url,
                                         "csv_kwargs": csv_kwargs}}

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
    

def ctd_towed_ferry_noaa_pmel(slug):
    
    project_name = "CTD Towed 2004-2008 Ferry in-line - NOAA PMEL"
    overall_desc = "NOAA PMEL: Towed CTD on ferry at nominal 4m depth"
    time = "Continuous 2004 to 2008, 5min sampling frequency"
    included = True
    notes = "The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency."
    maptype = "point"
    featuretype = "trajectory"
    url = "https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Tustumena_t_s_chl_cdom_tr_final_data.nc"
    xarray_kwargs = dict(drop_variables=["CHLOROPHYLL","CDOM","C_C_FW"])
    map_description = "Towed CTD Paths"
    bbox = [-156.0, 57.0, -150.5, 61.5]
    summary = """
An oceanographic monitoring system aboard the Alaska Marine Highway System ferry Tustumena operated for four years in the Alaska Coastal Current (ACC) with funding from the Exxon Valdez Oil Spill Trustee Council's Gulf Ecosystem Monitoring Program, the North Pacific Research Board and the National Oceanic and Atmospheric Administration. An electronic public display aboard the ferry educated passengers about the local oceanography and mapped the ferry's progress. Sampling water at 4 m, the underway system measured: (1) temperature and salinity (used in the present report), and (2) nitrate,
(3) chlorophyll fluorescence, (4) colored dissolved organic matter fluorescence, and (5) optical beam transmittance (not used in report).

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

    # Make an initial catalog because it's easier to read in the data that way
    # then make another catalog that is curated for monthly datasets
    entries = {}
    name = slug
    entries[name] = {"description": f"{project_name}",
                    "driver": "ciofs_hindcast_report.src.process.DatasetTransform",
                    "args": {"targets": [f"{name}_base"],
                             "transform": f"ciofs_hindcast_report.src.process.{slug}",
                             "transform_kwargs": dict(doresampling=False)},
                    "metadata": {"maptype": "point",
                                "minLongitude": bbox[0],
                                "minLatitude": bbox[1],
                                "maxLongitude": bbox[2],
                                "maxLatitude": bbox[3]},
                    }
    entries[f"{name}_base"] = {"description": f"Base for {name}",
                               "driver": "netcdf",
                               "args": {"urlpath": url,
                                        "xarray_kwargs": xarray_kwargs}}
    cat_name_initial = f"{slug}_initial"
    save_catalog(entries, cat_name=cat_name_initial, cat_desc=overall_desc)

    # read in data (more easily from intake) to get yearmonth to create individual monthly sources for dataset
    catname = chr.CAT_NAME(cat_name_initial)
    cat = intake.open_catalog(catname)
    ds = cat[slug].read()

    yearmonths = sorted(list(set([(pd.Timestamp(t).year, str(pd.Timestamp(t).month).zfill(2)) for t in ds.cf["T"].values])))

    entries = {}
    header_names = ["2004", "2005", "2006", "2007", "2008"]
    # header_names = ["2004", "2008"]
    # make one entry per month
    # for ind in [0,1,-2,-1]:
    #     year, month = yearmonths[ind]
    for year, month in yearmonths:

        # dsd = getattr(chr.src.process, slug)(ds, yearmonth=(year,month))
        dsd = ds.cf.sel(T=slice(f"{year}-{month}", f"{year}-{month}"))

        name = f"{year}-{month}"
        
        metadata = {"plots": {"salt": scatter_dict("salt", dsd, x="longitude", y="latitude", flip_yaxis=False),
                              "temp": scatter_dict("temp", dsd, x="longitude", y="latitude", flip_yaxis=False),}}
        metadata.update(add_metadata(dsd, maptype, featuretype))
        entries[name] = {"description": f"{year}, month {month}",
                        "driver": "ciofs_hindcast_report.src.process.DatasetTransform",
                        "args": {"targets": [f"{slug}_base"],
                                 "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                 "transform_kwargs": dict(yearmonth=(year, month))},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {slug}",
                               "driver": "netcdf",
                               "args": {"urlpath": url,
                                        "xarray_kwargs": xarray_kwargs}}

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


def ctd_profiles_otf_kbnerr(slug):

    project_name = "CTD profiles 2003-2006 - OTF KBNERR"
    overall_desc = "OTF KBNERR: Repeat CTD transect from Anchor Point in Cook Inlet"
    time = "Daily in July, 2003 to 2006"
    included = True
    notes = "These data were not included in the NWGOA model/data comparison"
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "CTD Profiles in Consistent Transect"
    summary = """CTD Profiles Across Anchor Point Transect, for GEM Project 030670.

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
                    dtype={'Depth [m]': 'float64', 'O2 [%sat]': 'float64', 'Station': 'float64'},
                    )
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
            if len(ddf) == 0:
                continue
            # ddf = df.set_index("date_time").loc[f"{year}-{month}-{day}"].reset_index()

            metadata = {"plots": {"salt": scatter_dict("salt", df, x="T", y="Z", flip_yaxis=True),
                                "temp": scatter_dict("temp", df, x="T", y="Z", flip_yaxis=True),}}
            # metadata.update({"minLongitude": minlon, "minLatitude": minlat, 
            #                  "maxLongitude": maxlon, "maxLatitude": maxlat,
            #                  "minTime": str(ddf.cf["T"].values.min()),
            #                  "maxTime": str(ddf.cf["T"].values.max()),
            #                  "maptype": maptype, "featuretype": featuretype})
            metadata.update(add_metadata(ddf, maptype, featuretype))
            entries[name] = {"description": f"{name}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(year=year, day=day),},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": url,
                                             "csv_kwargs": csv_kwargs}}

    # more catalog-level metadata
    cat_meta = {"map_description": map_description,
                "summary": summary,
                "header_names": ["2003", "2004", "2005", "2006"],
                "project_name": project_name,
                "time": time,
                "included": included,
                "notes": notes,
                "featuretype": featuretype,
                }
        
    save_catalog(entries, cat_name=slug, cat_desc=overall_desc, cat_meta=cat_meta)


def ctd_profiles_cmi_uaf(slug):
    project_name = "CTD profiles 2004-2005 - CMI UAF"
    overall_desc = "CMI UAF: CTD transect from East Foreland Lighthouse in Cook Inlet"
    time = "10 cruises, approximately monthly for summer months, in 2004 and 2005"
    included = True
    notes = "Used in the NWGOA model/data comparison."
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = ["2004", "2005"]
    map_description = "CTD Profiles in a Transect"
    summary = """Seasonality of Boundary Conditions for Cook Inlet, Alaska: Transect (3) at East Foreland Lighthouse.

9 CTD profiles at stations across 10 cruises in (approximately) the same locations. Approximately monthly for summer months, 2004 and 2005.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf
"""

    entries = {}
    url = "https://researchworkspace.com/files/39886038/all_forelands_ctd.txt"
    csv_kwargs = dict(sep="\t", dtype={"Month": "str", "Year": "str", "Day": "str", "Hour": "str", "Minute": "str"})
    # df = pd.read_csv(url, **csv_kwargs)
    # df = getattr(chr.src.process, slug)(df)
    # we can just know this
    cruises = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for cruise in cruises:

        # select cruise to get metadata
        df = pd.read_csv(url, **csv_kwargs)
        ddf = getattr(chr.src.process, slug)(df, cruise)
        name = f"Cruise-{str(cruise).zfill(2)}_{str(ddf.cf['T'].iloc[0].date())}"

        metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="T", y="Z", flip_yaxis=True),
                            "temp": scatter_dict("temp", ddf, x="T", y="Z", flip_yaxis=True),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))

        entries[name] = {"description": f"Cruise {cruise}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": dict(cruise=cruise),},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for all sources",
                            "driver": "csv",
                            "args": {"urlpath": url,
                                        "csv_kwargs": csv_kwargs}}

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


def ctd_profiles_cmi_kbnerr(slug):
    
    project_name = "CTD profiles 2004-2006 - CMI KBNERR"
    overall_desc = "CMI KBNERR: Six repeat transects, one single transect, and one time series of CTD profiles in Cook Inlet"
    time = "From 2004 to 2006"
    included = True
    notes = "Used in the NWGOA model/data comparison."
    maptype = "point"
    featuretype = "trajectoryProfile"
    header_names = ["Kbay_timeseries", "Cruise_00", "Cruise_01", "Cruise_02", "Cruise_03", "Cruise_04", "Cruise_05", "Cruise_06", "Cruise_07",
                    "Cruise_08", "Cruise_09", "Cruise_10", "Cruise_11", "Cruise_12", "Cruise_13", "Cruise_14", "Cruise_15", "Cruise_16", "sue_shelikof"]
    map_description = "CTD Profiles in Transects"
    summary = f"""Seasonality of Boundary Conditions for Cook Inlet, Alaska

During 2004 to 2006 we collected hydrographic measurements along transect lines crossing: 1) Kennedy Entrance and Stevenson Entrance from Port Chatham to Shuyak Island; 2) Shelikof Strait from Shuyak Island to Cape Douglas; 3) Cook Inlet from Red River to Anchor Point; 4) Kachemak Bay from Barbara Point to Bluff Point, and 5) the Forelands from East Foreland to West Foreland. During the third year we added two additional lines; 6) Cape Douglas to Cape Adams, and 7) Magnet Rock to Mount Augustine. The sampling in 2006 focused on the differences in properties during the spring and neap tide periods.

CTD profiles 2004-2005 - CMI UAF seems to be transect 5 of this project.

Note
Line 4 has an incorrect latitude for station 65. This can be seen with the following if the correction is not made:
```
df = cat['cmi_full_v2-Cruise_16-Line_4'].read()
df.drop_duplicates(subset="Station")
```
because the longitude is fixed and the latitude increases linearly until station 65 and then repeats the latitude value of station 56. The values are the same for the line in all datasets, and in the report. Since the difference in latitude across line 4 is about 0.0167, I will apply that difference from station 64 and use the resulting latitude for line 4, station 65.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>
"""
    urls = ["https://researchworkspace.com/files/39885976/cmi_full_v2.txt",
            "https://researchworkspace.com/files/39886046/Kbay_timeseries.txt",
            "https://researchworkspace.com/files/39886061/sue_shelikof.txt",
            ]

    cols = ['hh:mm', 'mon/day/yr', 'Cruise', 'Station', 'Type', 'Longitude [degrees_east]',
        'Latitude [degrees_north]', 'Bot. Depth [m]', 
        'Temperature [C]', 'Depth [m]', 'Salinity [psu]']
    csv_kwargs = []
    csv_kwargs.append(dict(header=2, sep="\t", parse_dates={"date_time": ["mon/day/yr","hh:mm"]}, usecols=cols, na_values=-9999.0))
    csv_kwargs.append(dict(encoding = "ISO-8859-1", sep="\t", parse_dates={"date_time": ["mon/day/yr","hh:mm [utc]"]}))
    csv_kwargs.append(dict(encoding = "ISO-8859-1", sep="\t", parse_dates={"date_time": ["mon/day/yr","hh:mm"]}))
    
    entries = {} 
    
    # sue_shelikof
    name, ind = "sue_shelikof", 2
    df = pd.read_csv(urls[ind], **csv_kwargs[ind])
    metadata = {"plots": {"salt": scatter_dict("salt", df, x="T", y="Z", flip_yaxis=True),
                        "temp": scatter_dict("temp", df, x="T", y="Z", flip_yaxis=True),}}
    metadata.update(add_metadata(df, maptype, featuretype))
    entries[name] = {"description": f"{name} line",
                    "driver": "csv",
                    "args": {"urlpath": urls[ind],
                             "csv_kwargs": csv_kwargs[ind]},
                    "metadata": metadata}
    
    # Kbay_timeseries
    name, ind = "Kbay_timeseries", 1
    df = pd.read_csv(urls[ind], **csv_kwargs[ind])
    metadata = {"plots": {"salt": scatter_dict("salt", df, x="T", y="Z", flip_yaxis=True),
                        "temp": scatter_dict("temp", df, x="T", y="Z", flip_yaxis=True),}}
    metadata.update(add_metadata(df, maptype, featuretype))
    entries[name] = {"description": f"{name} line",
                    "driver": "csv",
                    "args": {"urlpath": urls[ind],
                             "csv_kwargs": csv_kwargs[ind]},
                    "metadata": metadata}
    
    # cmi_full_v2
    name, ind = "cmi_full_v2", 0
    cruises = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    # stations making up lines/transects
    lines = {1: np.arange(1,23).tolist(),
            2: np.arange(23,29).tolist(),
            3: np.arange(39,56).tolist(),
            4: np.arange(56,66).tolist(),
            6: np.arange(90,118).tolist(),
            7: np.arange(66,90).tolist(),
            }
    df = pd.read_csv(urls[ind], **csv_kwargs[ind])
    df.cf["longitude"] -= 360
    df = df.sort_values("date_time").reset_index(drop=True)
    entries[f"{name}_base"] = {"description": f"Base for {name} sources",
                               "driver": "csv",
                               "args": {"urlpath": urls[ind],
                                        "csv_kwargs": csv_kwargs[ind]}}
    for cruise in cruises:
        for line in lines:
            # import pdb; pdb.set_trace()
            name_line = f"{name}-Cruise_{str(cruise).zfill(2)}-Line_{line}"
            # pull out source by Cruise and the stations making up the line/transect
            ddf = df[(df["Cruise"] == cruise) & (df.Station.isin(lines[line]))]
            # some cruise-line combinations don't exist
            if len(ddf)==0:
                continue
            metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="T", y="Z", flip_yaxis=True),
                                "temp": scatter_dict("temp", ddf, x="T", y="Z", flip_yaxis=True),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            entries[name_line] = {"description": f"{name_line}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": dict(cruise=cruise, line=line, stations=lines[line]),},
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


def ctd_moored_circac(slug):
    
    project_name = "CTD Moored 2006 - CIRCAC"
    overall_desc = "CIRCAC: Central Cook Inlet Mooring"
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
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

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
                               "args": {"urlpath": url,
                                        "csv_kwargs": csv_kwargs}}
    metadata = {"plots": {"data": line_time_dict("T", ["temp", "salt"], ddf),}}
    metadata.update(add_metadata(ddf, maptype, featuretype))
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


def ctd_moored_kbnerr(slug):
    
    project_name = "CTD Moored 2006-2008 - KBNERR"
    overall_desc = "KBNERR: Lower Cook Inlet Mooring"
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
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

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
                                "args": {"urlpath": url,
                                         "csv_kwargs": csv_kwargs}}
        metadata = {"plots": {"data": line_time_dict("T", ["temp", "salt"], ddf),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
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


def ctd_time_series_uaf(slug):
    project_name = "CTD time series UAF"
    overall_desc = "UAF: Repeat CTD profile transect along an east-west section in central Cook Inlet"
    time = "26-hour period on 9-10 August 2003"
    included = True
    notes = "Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison."
    maptype = "line"
    featuretype = "trajectoryProfile"
    header_names = None
    map_description = "Transect of CTD Profiles"
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

    url = "https://researchworkspace.com/files/41842203/TS%20downcasts.txt"
    csv_kwargs = dict(sep="\t", parse_dates={"date_time": ["mon/day/yr", "hh:mm [utc]"]})
    df = pd.read_csv(url, **csv_kwargs)
    df = getattr(chr.src.process, slug)(df)

    transects = [1,2,3,4,5,6,7,8,9]
    
    entries = {}
    for transect in transects:
        name = f"Transect_{str(transect).zfill(2)}"
        ddf = df[df["transect"] == transect]
        metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="T", y="Z", flip_yaxis=True),
                              "temp": scatter_dict("temp", ddf, x="T", y="Z", flip_yaxis=True),}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        entries[name] = {"description": f"{name}",
                         "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                         "args": {"targets": [f"{slug}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                "transform_kwargs": {"transect": transect},},
                        "metadata": metadata}
    entries[f"{slug}_base"] = {"description": f"Base for {slug}",
                               "driver": "csv",
                               "args": {"urlpath": url,
                                        "csv_kwargs": csv_kwargs}}

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
    overall_desc = "OSU: Time series of CTD profiles at several locations in Cook Inlet"
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
            entries[name] = {"description": f"{name}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
                                    "transform_kwargs": {"date": date, "lon": lon, "lat": lat},},
                            "metadata": metadata}
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": url,
                                                "csv_kwargs": csv_kwargs}}

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
    overall_desc = "GWA: Towed CTD at nominal 7m depth"
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
    
    # 2017
    urls = ["https://researchworkspace.com/files/42182639/2017_AprCTD.csv",
            "https://researchworkspace.com/files/42182642/2017_MayCTD.csv",
            "https://researchworkspace.com/files/42182641/2017_JulCTD.csv",
            "https://researchworkspace.com/files/42182640/2017_AugCTD.csv",
            "https://researchworkspace.com/files/42182614/2017_SepCTD.csv",
            "https://researchworkspace.com/files/42182643/2017_OctCTD.csv"]
    csv_kwargs = dict(parse_dates=[0])
    entries = {}
    for url in urls:
        df = pd.read_csv(url, **csv_kwargs)
        ddf = getattr(chr.src.process, f"{slug}_2017")(df)
        name = f"{str(ddf.cf['T'].dt.date[0])}"
        metadata = {"plots": {"salt": scatter_dict("salt", ddf, x="longitude", y="latitude", flip_yaxis=False),
                              "temp": scatter_dict("temp", ddf, x="longitude", y="latitude", flip_yaxis=False)}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        entries[name] = {"description": f"{name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}_2017",
                                "transform_kwargs": {},},
                        "metadata": metadata}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": url,
                                            "csv_kwargs": csv_kwargs}}
    
    urls = [
        "https://workspace.aoos.org/published/file/a58fd5f1-fc56-4bcb-9fac-8006cc610a9a/CPR_physical_data_2018.csv",
        "https://workspace.aoos.org/published/file/9be9b538-1b51-44a8-9f50-b2db2562adaa/CPR_physical_data_2019.csv",
        "https://workspace.aoos.org/published/file/14a9999c-d952-47ee-ad29-aeb6fa66b1d6/CPR_physical_data_2020.csv"]

    # 2018, 2019, 2020
    years = [2018, 2019, 2020]
    months = {2018: [4,5,6,7],
              2019: [4,5,8,9],
              2020: [7,8,9],}
    for year, url in zip(years, urls):
        if year == 2019:
            csv_kwargs = {}
        else:
            csv_kwargs = dict(parse_dates=[0])
        entries[f"{slug}_{year}_base"] = {"description": f"Base for {slug}_{year}",
                                "driver": "csv",
                                "args": {"urlpath": url,
                                            "csv_kwargs": csv_kwargs}}
        for month in months[year]:
                df = pd.read_csv(url, **csv_kwargs)
                ddf = getattr(chr.src.process, f"{slug}_{year}")(df, month)
                name = f"{str(ddf.cf['T'].dt.date[0])}"
                metadata = {"plots": {"temp": scatter_dict("temp", ddf, x="longitude", y="latitude", flip_yaxis=False)}}
                if year == 2018:
                    metadata["plots"].update({"salt": scatter_dict("salt", ddf, x="longitude", y="latitude", flip_yaxis=False),})
                metadata.update(add_metadata(ddf, maptype, featuretype))
                entries[name] = {"description": f"{name}",
                                "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                                "args": {"targets": [f"{slug}_{year}_base"],
                                        "transform": f"ciofs_hindcast_report.src.process.{slug}_{year}",
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


def temp_towed_gwa(slug):
    project_name = "Temperature towed 2011-2016 - GWA"
    overall_desc = "GWA: Towed CTD at nominal 7m depth, temperature only"
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
    entries = {}
    # 2011. months 6, 7, 8 (skip 2 rows in 9)
    year = 2011
    slug_year = f"{slug}_{year}"
    url = "https://workspace.aoos.org/published/file/15f607c5-405e-4db8-b83b-0ce70a6015ac/CPR_TemperatureData_2011.csv"
    csv_kwargs = dict(encoding="ISO-8859-1")
    df = pd.read_csv(url, **csv_kwargs)
    df = getattr(chr.src.process, slug_year)(df)
    months = [6, 7, 8]
    for month in months:
        # df = chr.src.process.temp_towed_gwa(df, month=month)
        # df = pd.read_csv(url, **csv_kwargs)
        # ddf = getattr(chr.src.process, f"{slug}_2011")(df, month=month)
        ddf = df.set_index(df.cf["T"].name).loc[f"{year}-{month}"].reset_index()
        name = f"{str(ddf.cf['T'].dt.date[0])}"
        metadata = {"plots": {"temp": scatter_dict("temp", ddf, x="longitude", y="latitude", flip_yaxis=False)}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        entries[name] = {"description": f"{name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{slug_year}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug_year}",
                                "transform_kwargs": {"month": month},},
                        "metadata": metadata}
    entries[f"{slug_year}_base"] = {"description": f"Base for {name}",
                            "driver": "csv",
                            "args": {"urlpath": url,
                                        "csv_kwargs": csv_kwargs}}
    
    # 2012, 2013, 2014, 2015, 2016
    urls = ["https://researchworkspace.com/files/42182615/2012_Apr.csv",
            "https://researchworkspace.com/files/42182617/2012_May.csv",
            "https://researchworkspace.com/files/42182616/2012_Jun.csv",
            "https://researchworkspace.com/files/42182619/2012_Sep.csv",
            "https://researchworkspace.com/files/42182618/2012_Oct.csv",
            "https://researchworkspace.com/files/42182620/2013_Apr.csv",
            "https://researchworkspace.com/files/42182624/2013_May.csv",
            "https://researchworkspace.com/files/42182623/2013_Jun.csv",
            "https://researchworkspace.com/files/42182622/2013_Jul.csv",
            "https://researchworkspace.com/files/42182621/2013_Aug.csv",
            "https://researchworkspace.com/files/42182625/2014_Apr.csv",
            "https://researchworkspace.com/files/42182629/2014_May.csv",
            "https://researchworkspace.com/files/42182628/2014_Jun.csv",
            "https://researchworkspace.com/files/42182627/2014_Jul.csv",
            "https://researchworkspace.com/files/42182626/2014_Aug.csv",
            "https://researchworkspace.com/files/42182630/2015_AugA.csv",
            "https://researchworkspace.com/files/42182631/2015_AugB.csv",
            "https://researchworkspace.com/files/42182632/2016_Apr.csv",
            "https://researchworkspace.com/files/42182637/2016_May.csv",
            "https://researchworkspace.com/files/42182636/2016_Jun.csv",
            "https://researchworkspace.com/files/42182635/2016_Jul.csv",
            "https://researchworkspace.com/files/42182633/2016_Aug.csv",
            "https://researchworkspace.com/files/42182638/2016_Sep.csv",]
    csv_kwargs = dict(encoding = "ISO-8859-1")
    # csv_kwargs = dict(parse_dates= [[0,1]], encoding = "ISO-8859-1", skip_blank_lines=True)
    # # df = pd.read_csv(urls[22], )
    # df = pd.read_csv(url, **csv_kwargs)
    # df = getattr(chr.src.process, slug_year)(df)
    # months = [6, 7, 8]
    for url in urls:
        # print(url)
        df = pd.read_csv(url, **csv_kwargs)
        ddf = chr.src.process.temp_towed_gwa_others(df)
        # ddf = getattr(chr.src.process, f"{slug}_2011")(df, month=month)
        # ddf = df.set_index(df.cf["T"].name).loc[f"{year}-{month}"].reset_index()
        name = f"{str(ddf.cf['T'].dt.date[0])}"
        metadata = {"plots": {"temp": scatter_dict("temp", ddf, x="longitude", y="latitude", flip_yaxis=False)}}
        metadata.update(add_metadata(ddf, maptype, featuretype))
        entries[name] = {"description": f"{name}",
                        "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                        "args": {"targets": [f"{name}_base"],
                                "transform": f"ciofs_hindcast_report.src.process.{slug}_others",
                                "transform_kwargs": {},},
                        "metadata": metadata}
        entries[f"{name}_base"] = {"description": f"Base for {name}",
                                "driver": "csv",
                                "args": {"urlpath": url,
                                            "csv_kwargs": csv_kwargs}}

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
    overall_desc = "OTF ADF&G: Long term station sampling"
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
                        header_names, map_description, summary, stations, open_kwargs):
    
    cat = intake.open_erddap_cat(server="https://erddap.sensors.ioos.us/erddap", 
                                 search_for=stations, 
                                 query_type="union",
                                 name=slug,
                                 description=overall_desc,
                                 use_source_constraints=True,
                                 start_time = "1999-01-01T00:00:00Z",
                                 open_kwargs=open_kwargs,
                                 dropna=True,
                                 mask_failed_qartod=True,
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

        cat[source_name].describe()["metadata"].update({"maptype": maptype,
                                     "featuretype": featuretype,
                                     "plots": {"data": line_time_dict("T", vars_to_use, ddf),}})

        cat[source_name].describe()["args"].update({"variables": var_names})
        
        # read in the last 2 hours of data and make another entry that is exactly like this one but subsampled
        # for plotting

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


# def make_axds_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
#                         header_names, map_description, summary, stations, open_kwargs):
    
#     cat = intake.open_axds_cat(datatype="sensor_station", 
#                            search_for=stations, 
#                            page_size=1,
#                         query_type="union",
#                         name=slug,
#                         description=overall_desc,
#                         )
    
#     # cat = intake.open_erddap_cat(server="https://erddap.sensors.ioos.us/erddap", 
#     #                              search_for=stations, 
#     #                              query_type="union",
#     #                              name=slug,
#     #                              description=overall_desc,
#     #                              use_source_constraints=True,
#     #                              start_time = "1999-01-01T00:00:00Z",
#     #                              open_kwargs=open_kwargs)
#     source_names = chr.src.utils.get_source_names(cat)
    
#     for source_name in source_names:
#         # this creates an empty DataFrame with column names of the variables in the dataset
#         # these can be checked with cf-pandas to fill in variable names in the metadata plots
#         ddf = pd.DataFrame(columns=cat[source_name].metadata["variables"] + ["Time [s]",])
        
#         # add some metadata
#         # first find which variables are available to use in plots for metadata
#         all_vars = ["ssh","temp","salt","u","v","speed"]
#         vars_to_use = []
#         for Var in all_vars:
#             try:
#                 # print(source_name, Var, ddf.cf[Var].shape)
#                 ddf.cf[Var].name
#                 vars_to_use.append(Var)
#             except ValueError:
#                 pass

#         cat[source_name].describe()["metadata"].update({"maptype": maptype,
#                                      "featuretype": featuretype,
#                                      "plots": {"data": line_time_dict("T", vars_to_use, ddf),}})

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
#     cat.metadata.update(cat_meta)
#     cat.save(chr.CAT_NAME(slug))


def moorings_aoos_cdip(slug):
    project_name = "Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP)"
    overall_desc = "CDIP Buoys: Lower Cook Inlet, Kodiak, Central Cook Inlet"
    time = "From , variable"
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
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)


def moorings_noaa(slug):
    project_name = "Moorings from NOAA"
    overall_desc = "NOAA Moorings: Miscellaneous locations"
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
                "noaa_nos_co_ops_kdaa2",
                "noaa_nos_co_ops_9457804",
                "noaa_nos_co_ops_9455500",
                "old-harbor-1",
                "boulder-point",
                # "wmo_46078",  # outside domain
                "wmo_46077",]
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)


def moorings_nps(slug):
    project_name = "Moorings from National Parks Service (NPS)"
    overall_desc = "NPS Moorings: Chinitna Bay and Aguchik Island, Cook Inlet"
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
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)


def moorings_uaf(slug):
    project_name = "Moorings from University of Alaska Fairbanks (UAF)"
    overall_desc = "UAF Moorings: Kodiak Island and Peterson Bay, Cook Inlet"
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
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)
    
    
def moorings_kbnerr_bear_cove_seldovia(slug):
    project_name = "Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)"
    overall_desc = "KBNERR Moorings: Kachemak Bay, Bear Cove and Seldovia"
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
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)
    
    
def moorings_kbnerr_homer(slug):
    project_name = "Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)"
    overall_desc = "KBNERR Moorings: Kachemak Bay, Homer stations"
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
    open_kwargs = {"parse_dates": [0], "response": "csv", "skiprows": [1]}
    
    make_erddap_catalog(slug, project_name, overall_desc, time, included, notes, maptype, featuretype,
                        header_names, map_description, summary, stations, open_kwargs)
    
    
def moorings_kbnerr_historical(slug):
    project_name = "Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)"
    overall_desc = "Historical KBNERR Moorings: Kachemak Bay"
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
 
    # set up location info
    loc = "https://researchworkspace.com/files/40335130/sampling_stations.csv"
    sites = pd.read_csv(loc, encoding = "ISO-8859-1")
    # strip white space
    sites["Station Code"] = sites["Station Code"].str.strip()

    stations = {"kacbcwq": ["https://researchworkspace.com/files/40335131/kacbcwq2002.csv",
                        "https://researchworkspace.com/files/40335132/kacbcwq2003.csv",],
            "kacdlwq": ["https://researchworkspace.com/files/40335133/kacdlwq2002.csv",],
            "kachowq": ["https://researchworkspace.com/files/40335163/kachowq2001.csv",
                        "https://researchworkspace.com/files/40335164/kachowq2002.csv",],
            "kacpgwq": ["https://researchworkspace.com/files/40335173/kacpgwq2002.csv",
                        "https://researchworkspace.com/files/40335174/kacpgwq2003.csv",],
            "kacsewq": ["https://researchworkspace.com/files/40335192/kacsewq2001.csv",
                        "https://researchworkspace.com/files/40335193/kacsewq2002.csv",
                        "https://researchworkspace.com/files/40335194/kacsewq2003.csv",],}
    cols = ["DateTimeStamp","StationCode","Temp","Sal","Depth","F_Temp","F_Sal","F_Depth"]
    csv_kwargs = dict(parse_dates=["DateTimeStamp"], usecols=cols)
    entries = {}
    for station_name, urls in stations.items():
        for url in urls:
            df = pd.read_csv(url, **csv_kwargs)
            lat, lon = sites[sites["Station Code"] == station_name][["Latitude "," Longitude"]].values[0].tolist()
            # functionname = "add_location_columns"
            ddf = getattr(chr.src.process, slug)(df, lon, lat)
            name = pathlib.PurePath(url).stem
            
            entries[f"{name}_base"] = {"description": f"Base for {name}",
                                    "driver": "csv",
                                    "args": {"urlpath": url,
                                            "csv_kwargs": csv_kwargs}}
            metadata = {"plots": {"data": line_time_dict("T", ["temp", "salt"], ddf),}}
            metadata.update(add_metadata(ddf, maptype, featuretype))
            entries[name] = {"description": f"{name}",
                            "driver": "ciofs_hindcast_report.src.process.DataFrameTransform",
                            "args": {"targets": [f"{name}_base"],
                                    "transform": f"ciofs_hindcast_report.src.process.{slug}",
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


def adcp_moored_noaa_coi_2005(slug):
    project_name = "Cook Inlet 2005 Current Survey"
    overall_desc = "NOAA ADCP survey Cook Inlet: 2005"
    time = "2005, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet
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
                    "maptype": maptype,
                    "featuretype": featuretype,}
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"]),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"]),}})
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
    overall_desc = "NOAA ADCP survey Cook Inlet: multiple years"
    time = "From 2002 to 2012, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet
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
                    "maptype": maptype,
                    "featuretype": featuretype,}
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"]),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"]),}})
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
    overall_desc = "NOAA ADCP survey Kodiak Island: Set 1"
    time = "2009, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet
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
                    "maptype": maptype,
                    "featuretype": featuretype,}
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"]),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"]),}})
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
    overall_desc = "NOAA ADCP survey Kodiak Island: Set 2"
    time = "2009, each for one or a few months"
    included = True
    notes = ""
    maptype = "point"
    featuretype = "timeSeriesProfile"
    header_names = None
    map_description = "Moored ADCPs"
    summary = f"""Moored NOAA ADCP surveys in Cook Inlet
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
                    "maptype": maptype,
                    "featuretype": featuretype,}
        md_new.update({"plots": {"ualong": quadmesh_dict("ualong_subtidal", "t", "depth", chr.cmap["u"]),
                                 "vacross": quadmesh_dict("vacross_subtidal", "t", "depth", chr.cmap["u"]),}})
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
   

# Generate all catalogs
if __name__ == "__main__":
    from time import time
    for slug in chr.slugs:
        if not chr.CAT_NAME(slug).is_file():
            start_time = time()
            getattr(chr.src.generate_catalogs, slug)(slug)
            print(f"Catalog: Slug {slug} required time {time() - start_time}")
