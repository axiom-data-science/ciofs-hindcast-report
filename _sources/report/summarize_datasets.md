---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
---

```{code-cell}
:tags: [remove-input]

import ciofs_hindcast_report as chr
import intake
import pandas as pd
import numpy as np
import hvplot.pandas
```

# Datasets Considered

## Table of All Datasets

```{div} full-width

|    | description                                                                             | slug                                      | project_name                                                                                | time                                                                       | featuretype       | included   | notes                                                                                                                                                                                                                         |
|---:|:----------------------------------------------------------------------------------------|:------------------------------------------|:--------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|:------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Moored ADCP (NOAA): ADCP survey Cook Inlet 2005                                         | adcp_moored_noaa_coi_2005                 | Cook Inlet 2005 Current Survey                                                              | 2005, each for one or a few months                                         | timeSeriesProfile | True       |                                                                                                                                                                                                                               |
|  2 | Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years                              | adcp_moored_noaa_coi_other                | Cook Inlet 2002/2003/2004/2008/2012 Current Survey                                          | From 2002 to 2012, each for one or a few months                            | timeSeriesProfile | True       |                                                                                                                                                                                                                               |
|  3 | Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 1                                    | adcp_moored_noaa_kod_1                    | Kodiak Island 2009 Current Survey (1)                                                       | 2009, each for one or a few months                                         | timeSeriesProfile | True       |                                                                                                                                                                                                                               |
|  4 | Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 2                                    | adcp_moored_noaa_kod_2                    | Kodiak Island 2009 Current Survey (2)                                                       | 2009, each for one or a few months                                         | timeSeriesProfile | True       |                                                                                                                                                                                                                               |
|  5 | Towed ADCP (OTF KBNERR): central Cook Inlet                                             | adcp_towed_otf_kbnerr                     | ADCP towed 2003-2005 - OTF KBNERR                                                           | July 2003                                                                  | trajectoryProfile | False      | There are processed files from 2003. However, they are too short in duration to be useful in comparison to the model output. There are unprocessed files from 2004 and 2005. No further steps were taken with these datasets. |
|  6 | Mooring (CIRCAC): Central Cook Inlet Mooring                                            | ctd_moored_circac                         | CTD Moored 2006 - CIRCAC                                                                    | Two weeks in August 2006, 15 min sampling                                  | timeSeries        | True       |                                                                                                                                                                                                                               |
|  7 | Mooring (KBNERR): Lower Cook Inlet Mooring                                              | ctd_moored_kbnerr                         | CTD Moored 2006-2008 - KBNERR                                                               | Aug to Oct 2006 and June 2007 to Feb 2008, 15 min sampling                 | timeSeries        | True       |                                                                                                                                                                                                                               |
|  8 | CTD Profiles (NOAA): across Cook Inlet                                                  | ctd_profiles_2005_noaa                    | CTD profiles 2005 - NOAA                                                                    | One-off CTD profiles in June and July 2005                                 | profile           | True       |                                                                                                                                                                                                                               |
|  9 | Moored CTDs (OSU): Time series of CTD profiles at several locations in Cook Inlet       | ctd_profiles_2005_osu                     | CTD profiles 2005 - OSU                                                                     | June 2005                                                                  | timeSeriesProfile | False      | Locations given are too low resolution making them incorrectly on land.                                                                                                                                                       |
| 10 | CTD Profiles (emap 2002)                                                                | ctd_profiles_emap_2002                    | emap 2002                                                                                   | One-off CTD profiles June to August 2002                                   | profile           | True       |                                                                                                                                                                                                                               |
| 11 | CTD Profiles (emap 2008)                                                                | ctd_profiles_emap_2008                    | emap 2008                                                                                   | One-off CTD profiles August to October 2008                                | profile           | True       |                                                                                                                                                                                                                               |
| 12 | CTD Profiles (Kachemak Kuletz 2005–2007)                                                | ctd_profiles_kachemack_kuletz_2005_2007   | Kachemak Kuletz 2005–2007                                                                   | One-off CTD profiles June-July 2005 and July 2006 and 2007                 | profile           | True       |                                                                                                                                                                                                                               |
| 13 | CTD Profiles (KB small mesh 2006)                                                       | ctd_profiles_kb_small_mesh_2006           | KB small mesh 2006                                                                          | One-off CTD profiles May 2006                                              | profile           | True       |                                                                                                                                                                                                                               |
| 14 | CTD Profiles (Kbay OSU 2007)                                                            | ctd_profiles_kbay_osu_2007                | Kbay OSU 2007                                                                               | One-off CTD profiles September 2007                                        | profile           | True       |                                                                                                                                                                                                                               |
| 15 | CTD Profiles (North Gulf small mesh 2005)                                               | ctd_profiles_north_gulf_small_mesh_2005   | North Gulf small mesh 2005                                                                  | One-off CTD profiles May 2005                                              | profile           | False      | Outside the model domain                                                                                                                                                                                                      |
| 16 | CTD Profiles (Piatt Speckman)                                                           | ctd_profiles_piatt_speckman_1999          | Piatt Speckman 1995-99                                                                      | One-off CTD profiles April to September 1999                               | profile           | True       |                                                                                                                                                                                                                               |
| 17 | CTD Profiles (USGS BOEM): across Cook Inlet                                             | ctd_profiles_usgs_boem                    | CTD profiles - USGS BOEM                                                                    | One-off CTD profiles from 2016 to 2021 in July                             | profile           | True       |                                                                                                                                                                                                                               |
| 18 | Towed CTD (OTF KBNERR): central Cook Inlet                                              | ctd_towed_otf_kbnerr                      | CTD Towed 2003 - OTF KBNERR                                                                 | July 2003, 5min sampling frequency                                         | trajectoryProfile | True       | Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency.                   |
| 19 | Underway CTD (NOAA PMEL): Towed on ferry                                                | ctd_towed_ferry_noaa_pmel                 | CTD Towed 2004-2008 Ferry in-line - NOAA PMEL                                               | Continuous 2004 to 2008, 5min sampling frequency                           | trajectory        | True       | The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency.                                                                      |
| 20 | Underway CTD (GWA): Towed CTD                                                           | ctd_towed_gwa                             | CTD Towed 2017-2019 - GWA                                                                   | Approximately monthly in summer from 2017 to 2020, 5min sampling frequency | trajectory        | True       | Made all longitudes negative west values, converted some local times, 2019 and 2020 only have temperature, ship track outside domain is not included, resampled from 2min to 5min.                                            |
| 21 | Underway CTD (GWA): Towed, temperature only                                             | ctd_towed_gwa_temp                        | Temperature towed 2011-2016 - GWA                                                           | Approximately monthly in summer from 2011 to 2016, 5min sampling frequency | trajectory        | True       | Converted some local times, ship track outside domain is not included.                                                                                                                                                        |
| 22 | CTD transects: Barabara to Bluff                                                        | ctd_transects_barabara_to_bluff_2002_2003 | Barabara to Bluff 2002-2003                                                                 | 2002-2003                                                                  | trajectoryProfile | True       |                                                                                                                                                                                                                               |
| 23 | CTD Transects, Moored CTD (CMI KBNERR): Six repeat, one single transect, one moored CTD | ctd_transects_cmi_kbnerr                  | CTD profiles 2004-2006 - CMI KBNERR                                                         | From 2004 to 2006                                                          | trajectoryProfile | True       | Used in the NWGOA model/data comparison.                                                                                                                                                                                      |
| 24 | CTD Transect (CMI UAF): from East Foreland Lighthouse                                   | ctd_transects_cmi_uaf                     | CTD profiles 2004-2005 - CMI UAF                                                            | 10 cruises, approximately monthly for summer months, in 2004 and 2005      | trajectoryProfile | True       | Used in the NWGOA model/data comparison.                                                                                                                                                                                      |
| 25 | CTD Transects (GWA): Six repeat transects in Cook Inlet                                 | ctd_transects_gwa                         | CTD profiles 2012-2021 - GWA                                                                | Quarterly repeats from 2012 to 2021                                        | trajectoryProfile | True       | Not used in the NWGOA model/data comparison.                                                                                                                                                                                  |
| 26 | CTD transects                                                                           | ctd_transects_misc_2002                   | CTD transects 2002                                                                          | 2002                                                                       | trajectoryProfile | True       |                                                                                                                                                                                                                               |
| 27 | CTD Transect (OTF KBNERR): Repeated from Anchor Point                                   | ctd_transects_otf_kbnerr                  | CTD profiles 2003-2006 - OTF KBNERR                                                         | Daily in July, 2003 to 2006                                                | trajectoryProfile | True       | These data were not included in the NWGOA model/data comparison                                                                                                                                                               |
| 28 | CTD Transects (UAF): Repeated in central Cook Inlet                                     | ctd_transects_uaf                         | CTD time series UAF                                                                         | 26-hour period on 9-10 August 2003                                         | trajectoryProfile | True       | Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison.                                                                                                                                  |
| 29 | HF Radar (UAF)                                                                          | hfradar                                   | HF Radar - UAF                                                                              | 2002-2009                                                                  | grid              | True       | These are accessed from Research Workspace where they have already been processed.                                                                                                                                            |
| 30 | Moorings (CDIP): Lower and Central Cook Inlet, Kodiak Island                            | moorings_aoos_cdip                        | Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP) | From 2011 to 2023, variable                                                | timeSeries        | True       |                                                                                                                                                                                                                               |
| 31 | Moorings (KBNERR): Kachemak Bay: Bear Cove, Seldovia                                    | moorings_kbnerr_bear_cove_seldovia        | Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)                     | From 2004 to present day, variable                                         | timeSeries        | True       | These are accessed through AOOS portal/ERDDAP server.                                                                                                                                                                         |
| 32 | Moorings (KBNERR): Historical, Kachemak Bay                                             | moorings_kbnerr_historical                | Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)          | From 2001 to 2003, variable                                                | timeSeries        | True       | These are accessed from Research Workspace.                                                                                                                                                                                   |
| 33 | Moorings (KBNERR): Kachemak Bay, Homer stations                                         | moorings_kbnerr_homer                     | Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)                     | From 2003 to present day, variable                                         | timeSeries        | True       | These are accessed through AOOS portal/ERDDAP server.                                                                                                                                                                         |
| 34 | Moorings (NOAA): across Cook Inlet                                                      | moorings_noaa                             | Moorings from NOAA                                                                          | From 1999 (and earlier) to 2023, variable                                  | timeSeries        | True       |                                                                                                                                                                                                                               |
| 35 | Moorings (NPS): Chinitna Bay, Aguchik Island                                            | moorings_nps                              | Moorings from National Parks Service (NPS)                                                  | From 2018 to 2019, variable                                                | timeSeries        | True       |                                                                                                                                                                                                                               |
| 36 | Moorings (UAF): Kodiak Island, Peterson Bay                                             | moorings_uaf                              | Moorings from University of Alaska Fairbanks (UAF)                                          | From 2013 to present, variable                                             | timeSeries        | True       |                                                                                                                                                                                                                               |
| 37 | Station Sampling (OTF ADF&G): Long term station sampling                                | surface_otf_adfg                          | surface Temp Sal - OTF ADF&G                                                                | Daily sampling mostly in July 1979 to 2021                                 | trajectoryProfile | False      | Not used because no times associated with data.                                                                                                                                                                               |

```

## Summary of Each Dataset

+++


### Moored ADCP (NOAA): ADCP survey Cook Inlet 2005

* Cook Inlet 2005 Current Survey
* 2005, each for one or a few months
* Slug: adcp_moored_noaa_coi_2005
* Included: True
* Feature type: timeSeriesProfile
* See the full dataset page for more information: {ref}`page:adcp_moored_noaa_coi_2005`

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   |   depth | depths                                                                                                                                                                                                          | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | key_variables                                 | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude | maxTime             |   measured_depth |   minLatitude |   minLongitude | minTime             | name                       | observe_dst   | orientation   | ping_int   | project                        | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   | urlpath                                                       |
|---:|:----------|--------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------------|--------------------------:|---------------------:|:----------------------------------------------|:--------------------|--------:|---------:|--------------:|---------------:|:--------------------|-----------------:|--------------:|---------------:|:--------------------|:---------------------------|:--------------|:--------------|:-----------|:-------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|:--------------------------------------------------------------|
|  0 | COI0501   |    33.5 | [19.39, 17.4, 15.39, 13.41, 11.4, 9.39, 7.41, 5.4, 3.41]                                                                                                                                                        | timeSeriesProfile | 2005-05-19 00:24:00 |                       349 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-28 20:06:00 | 60.722  | -151.647 |       60.722  |       -151.647 | 2005-06-28 20:06:00 |            29.53 |       60.722  |       -151.647 | 2005-05-19 00:24:00 | West Foreland              | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0501/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0501 |
|  1 | COI0502   |    33.8 | [20.18, 17.19, 14.2, 11.19, 8.2, 5.18, 2.19]                                                                                                                                                                    | timeSeriesProfile | 2005-05-18 23:23:00 |                         3 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-07-18 16:11:00 | 60.7207 | -151.557 |       60.7207 |       -151.557 | 2005-07-18 16:11:00 |            31.27 |       60.7207 |       -151.557 | 2005-05-18 23:23:00 | The Forelands              | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0502/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0502 |
|  2 | COI0503   |    44.2 | [36.24, 33.25, 30.24, 27.25, 24.23, 21.24, 18.23, 15.24, 12.25, 9.24, 6.25, 3.23]                                                                                                                               | timeSeriesProfile | 2005-05-18 22:36:00 |                         6 |                  7.4 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-29 22:54:00 | 60.7173 | -151.433 |       60.7173 |       -151.433 | 2005-06-29 22:54:00 |            48.61 |       60.7173 |       -151.433 | 2005-05-18 22:36:00 | East Foreland              | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0503/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0503 |
|  3 | COI0504   |    33.5 | [27.98, 25.97, 23.96, 21.98, 19.96, 17.98, 15.97, 13.96, 11.98, 9.97, 7.96, 5.97, 3.96]                                                                                                                         | timeSeriesProfile | 2005-05-18 21:24:00 |                       345 |                  7.4 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-29 23:30:00 | 60.6834 | -151.418 |       60.6834 |       -151.418 | 2005-06-29 23:30:00 |            39.42 |       60.6834 |       -151.418 | 2005-05-18 21:24:00 | Nikiski, .8 nm west of     | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0504/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0504 |
|  4 | COI0505   |    22.6 | [11.46, 9.48, 7.47, 5.46, 3.47, 1.46]                                                                                                                                                                           | timeSeriesProfile | 2005-05-19 01:23:00 |                        58 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-07-22 18:41:00 | 60.5967 | -151.74  |       60.5967 |       -151.74  | 2005-07-22 18:41:00 |            21.61 |       60.5967 |       -151.74  | 2005-05-19 01:23:00 | West Foreland, south of    | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0505/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0505 |
|  5 | COI0506   |    27.1 | [13.75, 11.73, 9.75, 7.74, 5.76, 3.75, 1.74]                                                                                                                                                                    | timeSeriesProfile | 2005-05-18 20:06:00 |                        21 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-30 01:54:00 | 60.5808 | -151.445 |       60.5808 |       -151.445 | 2005-06-30 01:54:00 |            23.88 |       60.5808 |       -151.445 | 2005-05-18 20:06:00 | Kenai River, north of      | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0506/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0506 |
|  6 | COI0507   |    27.4 | [16.64, 14.66, 12.65, 10.64, 8.66, 6.64, 4.66, 2.65]                                                                                                                                                            | timeSeriesProfile | 2005-05-19 03:00:00 |                        51 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-30 20:36:00 | 60.5517 | -152.128 |       60.5517 |       -152.128 | 2005-06-30 20:36:00 |            26.78 |       60.5517 |       -152.128 | 2005-05-19 03:00:00 | Drift River Terminal       | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0507/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0507 |
|  7 | COI0508   |    51.5 | [35.63, 32.64, 29.63, 26.64, 23.65, 20.64, 17.65, 14.63, 11.64, 8.63, 5.64]                                                                                                                                     | timeSeriesProfile | 2005-05-18 18:54:00 |                        33 |                  7.4 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-30 14:24:00 | 60.483  | -151.673 |       60.483  |       -151.673 | 2005-06-30 14:24:00 |            48    |       60.483  |       -151.673 | 2005-05-18 18:54:00 | Kalgin Island, east of     | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0508/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0508 |
|  8 | COI0509   |    96.3 | [79.04, 76.02, 73.03, 70.01, 67.03, 64.01, 61.02, 58.03, 55.02, 52.03, 49.01, 46.03, 43.01, 40.02, 37.03, 34.02, 31.03, 28.01, 25.02, 22.01, 19.02, 16.03, 13.02, 10.03, 7.01]                                  | timeSeriesProfile | 2005-05-19 04:53:00 |                        15 |                 10.7 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-29 14:35:00 | 60.3792 | -152.182 |       60.3792 |       -152.182 | 2005-06-29 14:35:00 |            94.67 |       60.3792 |       -152.182 | 2005-05-19 04:53:00 | Harriot Pt., west of       | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0509/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0509 |
|  9 | COI0510   |    34.5 | [17.62, 15.61, 13.62, 11.61, 9.63, 7.62, 5.61, 3.63]                                                                                                                                                            | timeSeriesProfile | 2005-05-18 16:42:00 |                        33 |                  7.4 | ['east', 'north', 'along', 'across', 'speed'] | 2005-06-29 04:48:00 | 60.248  | -151.755 |       60.248  |       -151.755 | 2005-06-29 04:48:00 |            29.04 |       60.248  |       -151.755 | 2005-05-18 16:42:00 | Kalgin Island, SE of       | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0510/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0510 |
| 10 | COI0511   |    68.6 | [56.02, 53.01, 50.02, 47.0, 44.01, 41.0, 38.01, 35.02, 32.0, 29.02, 26.0, 23.01, 20.0, 17.01, 14.02, 11.0, 8.02, 5.0]                                                                                           | timeSeriesProfile | 2005-06-29 02:54:00 |                        31 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-15 15:42:00 | 60.0233 | -152.12  |       60.0233 |       -152.12  | 2005-08-15 15:42:00 |            67.08 |       60.0233 |       -152.12  | 2005-06-29 02:54:00 | Cape Ninilchik, west of    | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0511/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0511 |
| 11 | COI0512   |    17.4 | [6.13, 3.14]                                                                                                                                                                                                    | timeSeriesProfile | 2005-07-05 07:06:00 |                       320 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-15 05:48:00 | 59.5666 | -153.422 |       59.5666 |       -153.422 | 2005-08-15 05:48:00 |            17.19 |       59.5666 |       -153.422 | 2005-07-05 07:06:00 | Iliamna Bay                | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0512/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0512 |
| 12 | COI0513   |    31.2 | [16.95, 13.96, 10.94, 7.96, 4.94, 1.95]                                                                                                                                                                         | timeSeriesProfile | 2005-07-04 01:30:00 |                        40 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-13 19:18:00 | 59.4828 | -151.755 |       59.4828 |       -151.755 | 2005-08-13 19:18:00 |            28.06 |       59.4828 |       -151.755 | 2005-07-04 01:30:00 | Seldovia                   | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0513/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0513 |
| 13 | COI0514   |    80.2 | [63.25, 60.23, 57.24, 54.26, 51.24, 48.25, 45.23, 42.25, 39.23, 36.24, 33.25, 30.24, 27.25, 24.23, 21.24, 18.23, 15.24, 12.25, 9.24, 6.25]                                                                      | timeSeriesProfile | 2005-07-05 11:12:00 |                         5 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-15 02:12:00 | 59.3018 | -152.93  |       59.3018 |       -152.93  | 2005-08-15 02:12:00 |            74.3  |       59.3018 |       -152.93  | 2005-07-05 11:12:00 | Augustine Island           | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0514/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0514 |
| 14 | COI0515   |    87.7 | [74.31, 71.32, 68.31, 65.32, 62.3, 59.31, 56.3, 53.31, 50.32, 47.31, 44.32, 41.3, 38.31, 35.3, 32.31, 29.32, 26.3, 23.32, 20.3, 17.31, 14.3, 11.31, 8.32, 5.3]                                                  | timeSeriesProfile | 2005-07-05 14:06:00 |                        10 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-13 23:24:00 | 59.3149 | -152.365 |       59.3149 |       -152.365 | 2005-08-13 23:24:00 |            85.36 |       59.3149 |       -152.365 | 2005-07-05 14:06:00 | Kachemak Bay, southwest of | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0515/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0515 |
| 15 | COI0516   |    47.1 | [34.75, 31.76, 28.74, 25.76, 22.74, 19.75, 16.76, 13.75, 10.76, 7.74, 4.75]                                                                                                                                     | timeSeriesProfile | 2005-07-04 03:00:00 |                        30 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-13 21:00:00 | 59.4    | -151.966 |       59.4    |       -151.966 | 2005-08-13 21:00:00 |            45.79 |       59.4    |       -151.966 | 2005-07-04 03:00:00 | Port Graham                | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0516/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0516 |
| 16 | COI0517   |   177.9 | [138.72, 132.71, 126.71, 120.7, 114.7, 108.72, 102.72, 96.71, 90.71, 84.7, 78.7, 72.7, 66.72, 60.72, 54.71, 12.71]                                                                                              | timeSeriesProfile | 2005-07-05 00:36:00 |                       340 |                 20   | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 22:00:00 | 58.8901 | -153.184 |       58.8901 |       -153.184 | 2005-08-14 22:00:00 |           166.82 |       58.8901 |       -153.184 | 2005-07-05 00:36:00 | Cape Douglas               | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0517/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0517 |
| 17 | COI0518   |   170.8 | [137.59, 131.58, 125.58, 119.6, 113.6, 107.6, 101.59, 95.59, 89.58, 83.58, 77.6, 71.6, 65.59, 59.59, 53.58, 47.58, 41.61, 35.6, 29.6, 23.59, 17.59]                                                             | timeSeriesProfile | 2005-07-04 22:18:00 |                       312 |                 20   | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 19:30:00 | 58.9805 | -152.728 |       58.9805 |       -152.728 | 2005-08-14 19:30:00 |           165.68 |       58.9805 |       -152.728 | 2005-07-04 22:18:00 | Cape Douglas, NE           | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0518/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0518 |
| 18 | COI0519   |   146.6 | [128.17, 123.17, 118.17, 113.17, 108.17, 103.18, 98.15, 93.15, 88.15, 83.15, 78.15, 73.15, 68.15, 63.16, 58.16, 53.16, 48.16, 43.16, 38.16, 33.16, 28.16, 23.17, 18.17, 13.17]                                  | timeSeriesProfile | 2005-07-04 20:24:00 |                       300 |                  8   | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 17:36:00 | 58.808  | -152.408 |       58.808  |       -152.408 | 2005-08-14 17:36:00 |           143.26 |       58.808  |       -152.408 | 2005-07-04 20:24:00 | Stevenson Passage          | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0519/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0519 |
| 19 | COI0520   |   162.4 | [148.62, 144.6, 140.61, 136.61, 132.62, 128.6, 124.6, 120.61, 116.62, 112.62, 108.6, 104.61, 100.62, 96.62, 92.6, 88.61, 84.61, 80.62, 76.6, 72.6, 68.61, 64.62, 60.63, 56.6, 52.61, 48.62, 44.62, 40.6, 36.61] | timeSeriesProfile | 2005-07-04 17:18:00 |                       300 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 13:54:00 | 59.0492 | -152.152 |       59.0492 |       -152.152 | 2005-08-14 13:54:00 |           160.72 |       59.0492 |       -152.152 | 2005-07-04 17:18:00 | West Amatuli Island, North | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0520/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0520 |
| 20 | COI0521   |    87   | [69.71, 65.72, 61.72, 57.7, 53.71, 49.71, 45.72, 41.7, 37.7, 33.71, 29.72, 25.73, 21.7, 17.71, 13.72, 9.72, 5.7]                                                                                                | timeSeriesProfile | 2005-07-04 06:12:00 |                       306 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 02:54:00 | 59.1207 | -151.895 |       59.1207 |       -151.895 | 2005-08-14 02:54:00 |            81.83 |       59.1207 |       -151.895 | 2005-07-04 06:12:00 | Cape Elizabeth             | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0521/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0521 |
| 21 | COI0522   |    37.8 | [21.28, 18.29, 15.3, 12.28, 9.3, 6.28]                                                                                                                                                                          | timeSeriesProfile | 2005-07-04 08:54:00 |                        45 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 04:36:00 | 59.2112 | -151.787 |       59.2112 |       -151.787 | 2005-08-14 04:36:00 |            32.37 |       59.2112 |       -151.787 | 2005-07-04 08:54:00 | Port Chatham               | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0522/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0522 |
| 22 | COI0523   |    82.1 | [67.3, 63.31, 59.31, 55.32, 51.3, 47.31, 43.31, 39.32, 35.3, 31.3, 27.31, 23.32, 19.32, 15.3, 11.31, 7.32]                                                                                                      | timeSeriesProfile | 2005-07-04 08:12:00 |                       350 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 05:17:00 | 59.1666 | -151.775 |       59.1666 |       -151.775 | 2005-08-14 05:17:00 |            79.44 |       59.1666 |       -151.775 | 2005-07-04 08:12:00 | Chugach Passage            | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0523/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0523 |
| 23 | COI0524   |    30.9 | [15.79, 12.77, 9.78, 6.77, 3.78]                                                                                                                                                                                | timeSeriesProfile | 2005-07-04 07:42:00 |                       270 |                  6.1 | ['east', 'north', 'along', 'across', 'speed'] | 2005-08-14 06:06:00 | 59.1339 | -151.706 |       59.1339 |       -151.706 | 2005-08-14 06:06:00 |            26.83 |       59.1339 |       -151.706 | 2005-07-04 07:42:00 | Chugach Passage, east of   | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0524/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0524 |

```
````

+++




**Map of Moored ADCPs**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_coi_2005")("adcp_moored_noaa_coi_2005")
```


### Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years

* Cook Inlet 2002/2003/2004/2008/2012 Current Survey
* From 2002 to 2012, each for one or a few months
* Slug: adcp_moored_noaa_coi_other
* Included: True
* Feature type: timeSeriesProfile
* See the full dataset page for more information: {ref}`page:adcp_moored_noaa_coi_other`

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   |   depth | depths                                                                                                                                                                                            | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | key_variables                                 | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude | maxTime             |   measured_depth |   minLatitude |   minLongitude | minTime             | name                       | observe_dst   | orientation   | ping_int   | project                        | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   | urlpath                                                       |
|---:|:----------|--------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------------|--------------------------:|---------------------:|:----------------------------------------------|:--------------------|--------:|---------:|--------------:|---------------:|:--------------------|-----------------:|--------------:|---------------:|:--------------------|:---------------------------|:--------------|:--------------|:-----------|:-------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|:--------------------------------------------------------------|
|  0 | COI0206   |   35.05 | [30.69, 28.71, 26.7, 24.69, 22.71, 20.7, 18.71, 16.7, 14.69, 12.71, 10.7, 8.69, 6.71]                                                                                                             | timeSeriesProfile | 2002-07-13 01:18:00 |                        90 |                 0.5  | ['east', 'north', 'along', 'across', 'speed'] | 2002-08-13 17:48:00 | 61.2169 | -149.984 |       61.2169 |       -149.984 | 2002-08-13 17:48:00 |            35.14 |       61.2169 |       -149.984 | 2002-07-13 01:18:00 | Point Woronzof             | True          | up            |            | Cook Inlet 2002 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0206/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0206 |
|  1 | COI0207   |   11.4  | [8.44, 7.44, 6.43, 5.43, 4.42, 3.44, 2.44, 1.43, 0.43]                                                                                                                                            | timeSeriesProfile | 2002-07-13 00:32:00 |                        90 |                 0.5  | ['east', 'north', 'along', 'across', 'speed'] | 2002-10-05 22:08:00 | 61.1792 | -150.126 |       61.1792 |       -150.126 | 2002-10-05 22:08:00 |            11.4  |       61.1792 |       -150.126 | 2002-07-13 00:32:00 | Fire Island, 1 nm E        | True          | up            |            | Cook Inlet 2002 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0207/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0207 |
|  2 | COI0213   |   23.8  | [14.66, 13.66, 12.65, 11.67, 10.67, 9.66, 8.66, 7.65, 6.68, 5.67, 4.66]                                                                                                                           | timeSeriesProfile | 2002-07-13 00:00:00 |                        90 |                 9.4  | ['east', 'north', 'along', 'across', 'speed'] | 2002-08-14 15:12:00 | 61.1922 | -150.176 |       61.1922 |       -150.176 | 2002-08-14 15:12:00 |            26.02 |       61.1922 |       -150.176 | 2002-07-13 00:00:00 | Fire Island                | True          | up            |            | Cook Inlet 2002 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0213/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0213 |
|  3 | COI0301   |   18.9  | [10.97, 9.97, 8.96, 7.96, 6.95, 5.97, 4.97, 3.96, 2.96, 1.95, 0.94]                                                                                                                               | timeSeriesProfile | 2003-07-16 00:22:00 |                        17 |                 7.5  | ['east', 'north', 'along', 'across', 'speed'] | 2003-08-20 16:16:00 | 61.2782 | -149.895 |       61.2782 |       -149.895 | 2003-08-20 16:16:00 |            21.42 |       61.2782 |       -149.895 | 2003-07-16 00:22:00 | Knik Arm, NW of POA        | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0301/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0301 |
|  4 | COI0302   |   21.1  | [12.04, 11.03, 10.03, 9.02, 8.02, 7.04, 6.04, 5.03, 4.02, 3.02, 2.04, 1.04, 0.03]                                                                                                                 | timeSeriesProfile | 2003-07-16 00:14:00 |                        20 |                 7.5  | ['east', 'north', 'along', 'across', 'speed'] | 2003-08-20 04:26:00 | 61.2746 | -149.882 |       61.2746 |       -149.882 | 2003-08-20 04:26:00 |            22.49 |       61.2746 |       -149.882 | 2003-07-16 00:14:00 | Knik Arm, East Side        | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0302/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0302 |
|  5 | COI0303   |   31.1  | [21.58, 20.57, 19.57, 18.59, 17.59, 16.58, 15.58, 14.57, 13.59, 12.59, 11.58, 10.58, 9.57, 8.56, 7.59, 6.58, 5.58, 4.57, 3.57, 2.59, 1.58, 0.58]                                                  | timeSeriesProfile | 2003-07-16 00:52:00 |                        30 |                 7.5  | ['east', 'north', 'along', 'across', 'speed'] | 2003-08-21 05:52:00 | 61.2522 | -149.921 |       61.2522 |       -149.921 | 2003-08-21 05:52:00 |            32.04 |       61.2522 |       -149.921 | 2003-07-16 00:52:00 | Port Mackenzie, South of   | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0303/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0303 |
|  6 | COI0306   |   23.8  | [11.86, 10.85, 9.85, 8.84, 7.86, 6.86, 5.85, 4.85, 3.84, 2.87, 1.86]                                                                                                                              | timeSeriesProfile | 2003-07-14 20:18:00 |                        80 |                 7.2  | ['east', 'north', 'along', 'across', 'speed'] | 2003-08-23 02:24:00 | 61.1609 | -150.565 |       61.1609 |       -150.565 | 2003-08-23 02:24:00 |            22.01 |       61.1609 |       -150.565 | 2003-07-14 20:18:00 | Fire Island Shoal, NW of   | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0306/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0306 |
|  7 | COI0307   |   22.3  | [13.41, 12.41, 11.4, 10.42, 9.42, 8.41, 7.41, 6.4, 5.4, 4.42, 3.41, 2.41, 1.4, 0.4]                                                                                                               | timeSeriesProfile | 2003-07-14 21:54:00 |                        45 |                 7.2  | ['east', 'north', 'along', 'across', 'speed'] | 2003-08-23 01:06:00 | 61.1014 | -150.562 |       61.1014 |       -150.562 | 2003-08-23 01:06:00 |            23.57 |       61.1014 |       -150.562 | 2003-07-14 21:54:00 | Beluga Shoal, S. of        | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0307/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0307 |
|  8 | COI0418   |  203    | [86.38, 82.36, 78.37, 74.37, 70.38, 66.36, 62.36, 58.37, 54.38, 50.38, 46.36, 42.37, 38.37, 34.38, 30.36, 26.37, 22.37, 18.38, 14.36, 10.36, 6.37]                                                | timeSeriesProfile | 2004-06-22 01:31:00 |                       295 |               100    | ['east', 'north', 'along', 'across', 'speed'] | 2004-08-03 17:25:00 | 59.0658 | -151.982 |       59.0658 |       -151.982 | 2004-08-03 17:25:00 |           192.5  |       59.0658 |       -151.982 | 2004-06-22 01:31:00 | Kennedy Entrance           | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0418/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0418 |
|  9 | COI0419   |   51.5  | [39.01, 37.03, 35.02, 33.01, 31.03, 29.02, 27.01, 25.02, 23.01, 21.03, 19.02, 17.01, 15.03, 13.02, 11.03, 9.02, 7.01]                                                                             | timeSeriesProfile | 2004-08-05 21:36:00 |                         0 |                 8.53 | ['east', 'north', 'along', 'across', 'speed'] | 2004-09-15 14:54:00 | 59.8393 | -152.368 |       59.8393 |       -152.368 | 2004-09-15 14:54:00 |            51.77 |       59.8393 |       -152.368 | 2004-08-05 21:36:00 | Anchor Point West          | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0419/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0419 |
| 10 | COI0420   |   41.4  | [29.87, 27.86, 25.88, 23.87, 21.88, 19.87, 17.86, 15.88, 13.87, 11.86, 9.88, 7.86, 5.88, 3.87]                                                                                                    | timeSeriesProfile | 2004-08-05 20:06:00 |                         0 |                 8.54 | ['east', 'north', 'along', 'across', 'speed'] | 2004-09-15 14:42:00 | 59.8187 | -152.156 |       59.8187 |       -152.156 | 2004-09-15 14:42:00 |            42.62 |       59.8187 |       -152.156 | 2004-08-05 20:06:00 | Anchor Point East          | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0420/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0420 |
| 11 | COI0421   |   61.6  | [44.93, 42.95, 40.94, 38.95, 36.94, 34.93, 32.95, 30.94, 28.93, 26.94, 24.93, 22.95, 20.94, 18.93, 16.95, 14.94, 12.95, 10.94, 8.93, 6.95, 4.94]                                                  | timeSeriesProfile | 2004-08-05 16:59:00 |                        80 |                 8.5  | ['east', 'north', 'along', 'across', 'speed'] | 2004-09-15 19:23:00 | 59.5754 | -151.652 |       59.5754 |       -151.652 | 2004-09-15 19:23:00 |            57.63 |       59.5754 |       -151.652 | 2004-08-05 16:59:00 | Barabara Point             | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0421/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0421 |
| 12 | COI0422   |   56.7  | [44.41, 42.4, 40.39, 38.41, 36.39, 34.41, 32.4, 30.39, 28.41, 26.4, 24.41, 22.4, 20.39, 18.41, 16.4, 14.39, 12.41, 10.39, 8.41, 6.4, 4.39]                                                        | timeSeriesProfile | 2004-08-06 21:05:00 |                        50 |                 8.5  | ['east', 'north', 'along', 'across', 'speed'] | 2004-09-15 21:29:00 | 59.6667 | -151.192 |       59.6667 |       -151.192 | 2004-09-15 21:29:00 |            57.13 |       59.6667 |       -151.192 | 2004-08-06 21:05:00 | Glacier Split              | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0422/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0422 |
| 13 | COI0801   |   22    | [16.64, 14.63, 12.65, 10.64, 8.63, 6.64, 4.63, 2.65]                                                                                                                                              | timeSeriesProfile | 2008-07-15 22:36:00 |                       345 |                 3.9  | ['east', 'north', 'along', 'across', 'speed'] | 2008-09-17 22:30:00 | 60.6869 | -151.404 |       60.6869 |       -151.404 | 2008-09-17 22:30:00 |            23.64 |       60.6869 |       -151.404 | 2008-07-15 22:36:00 | Tesoro Pier, N of          | True          | up            |            | Cook Inlet 2008 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0801/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0801 |
| 14 | COI0802   |   22    | [15.61, 13.62, 11.61, 9.63, 7.62, 5.61, 3.63, 1.62]                                                                                                                                               | timeSeriesProfile | 2008-07-15 23:24:00 |                       345 |                 3.9  | ['east', 'north', 'along', 'across', 'speed'] | 2008-09-17 22:30:00 | 60.6678 | -151.392 |       60.6678 |       -151.392 | 2008-09-17 22:30:00 |            22.62 |       60.6678 |       -151.392 | 2008-07-15 23:24:00 | Unocal Pier, S of          | True          | up            |            | Cook Inlet 2008 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0802/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0802 |
| 15 | COI1201   |   77.3  | [60.38, 58.37, 56.39, 54.38, 52.4, 50.38, 48.37, 46.39, 44.38, 42.37, 40.39, 38.37, 36.39, 34.38, 32.37, 30.39, 28.38, 26.37, 24.38, 22.37, 20.39, 18.38, 16.37, 14.39, 12.38, 10.39, 8.38, 6.37] | timeSeriesProfile | 2012-06-14 00:54:00 |                        35 |                10.35 | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-14 18:29:00 | 59.5925 | -151.4   |       59.5925 |       -151.4   | 2012-08-14 18:29:00 |            74.93 |       59.5925 |       -151.4   | 2012-06-14 00:54:00 | Homer Spit                 | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1201/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1201 |
| 16 | COI1202   |   43.3  | [30.63, 28.62, 26.61, 24.63, 22.62, 20.64, 18.62, 16.61, 14.63, 12.62, 10.61, 8.63, 6.61, 4.63]                                                                                                   | timeSeriesProfile | 2012-06-13 20:12:00 |                        45 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-14 20:30:00 | 59.4225 | -151.917 |       59.4225 |       -151.917 | 2012-08-14 20:30:00 |            40.82 |       59.4225 |       -151.917 | 2012-06-13 20:12:00 | Pt. Pogishi, SW of         | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1202/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1202 |
| 17 | COI1203   |   44.7  | [31.79, 29.78, 27.8, 25.79, 23.81, 21.79, 19.78, 17.8, 15.79, 13.78, 11.8, 9.78, 7.8, 5.79, 3.78]                                                                                                 | timeSeriesProfile | 2012-06-14 18:42:00 |                        10 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-14 22:06:00 | 59.7438 | -152.034 |       59.7438 |       -152.034 | 2012-08-14 22:06:00 |            40.87 |       59.7438 |       -152.034 | 2012-06-14 18:42:00 | Anchor Point, W of         | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1203/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1203 |
| 18 | COI1204   |   31.7  | [20.03, 19.02, 18.01, 17.01, 16.03, 15.03, 14.02, 13.02, 12.01, 11.03, 10.03, 9.02, 8.02, 7.01, 6.04, 5.03, 4.02, 3.02, 2.01]                                                                     | timeSeriesProfile | 2012-06-16 01:06:00 |                        55 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-17 01:06:00 | 61.0598 | -151.081 |       61.0598 |       -151.081 | 2012-08-17 01:06:00 |            28.13 |       61.0598 |       -151.081 | 2012-06-16 01:06:00 | North Forelands            | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1204/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1204 |
| 19 | COI1205   |   69.5  | [51.54, 49.56, 47.55, 45.54, 43.56, 41.54, 39.56, 37.55, 35.54, 33.56, 31.55, 29.54, 27.55, 25.54, 23.56, 21.55, 19.54, 17.56, 15.54, 13.56, 11.55, 9.54, 7.56, 5.55, 3.54]                       | timeSeriesProfile | 2012-06-15 01:48:00 |                        10 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-15 23:00:00 | 60.4718 | -151.706 |       60.4718 |       -151.706 | 2012-08-15 23:00:00 |            61.74 |       60.4718 |       -151.706 | 2012-06-15 01:48:00 | Kalgin Island, 4nm E of    | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1205/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1205 |
| 20 | COI1207   |   53.3  | [41.73, 39.75, 37.73, 35.75, 33.74, 31.73, 29.75, 27.74, 25.73, 23.74, 21.73, 19.75, 17.74, 15.73, 13.75, 11.73, 9.75, 7.74, 5.73]                                                                | timeSeriesProfile | 2012-06-16 20:12:00 |                        50 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-17 17:24:00 | 61.0566 | -150.36  |       61.0566 |       -150.36  | 2012-08-17 17:24:00 |            51.95 |       61.0566 |       -150.36  | 2012-06-16 20:12:00 | Point Possession           | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1207/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1207 |
| 21 | COI1208   |   31.6  | [24.26, 23.26, 22.25, 21.28, 20.27, 19.26, 18.26, 17.25, 16.25, 15.27, 14.26, 13.26, 12.25, 11.25, 10.27, 9.27, 8.26, 7.25, 6.25, 5.27, 4.27, 3.26]                                               | timeSeriesProfile | 2012-06-16 21:18:00 |                        90 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-17 18:30:00 | 61.1036 | -150.265 |       61.1036 |       -150.265 | 2012-08-17 18:30:00 |            32.37 |       61.1036 |       -150.265 | 2012-06-16 21:18:00 | Fire Island, South of      | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1208/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1208 |
| 22 | COI1209   |   29.4  | [15.94, 14.94, 13.96, 12.95, 11.95, 10.94, 9.94, 8.96, 7.96, 6.95, 5.94, 4.94, 3.96, 2.96, 1.95]                                                                                                  | timeSeriesProfile | 2012-06-17 02:54:00 |                        65 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-17 05:30:00 | 61.1848 | -150.202 |       61.1848 |       -150.202 | 2012-08-17 05:30:00 |            24.05 |       61.1848 |       -150.202 | 2012-06-17 02:54:00 | Fire Island, North of      | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1209/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1209 |
| 23 | COI1210   |   43.3  | [31.15, 29.14, 27.13, 25.15, 23.13, 21.15, 19.14, 17.13, 15.15, 13.14, 11.13, 9.14, 7.13, 5.15, 3.14]                                                                                             | timeSeriesProfile | 2012-06-15 22:12:00 |                        45 |                 6    | ['east', 'north', 'along', 'across', 'speed'] | 2012-08-16 23:35:00 | 60.887  | -151.233 |       60.887  |       -151.233 | 2012-08-16 23:35:00 |            41.34 |       60.887  |       -151.233 | 2012-06-15 22:12:00 | Middle Ground Shoal, E of. | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1210/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1210 |

```
````

+++




**Map of Moored ADCPs**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_coi_other")("adcp_moored_noaa_coi_other")
```


### Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 1

* Kodiak Island 2009 Current Survey (1)
* 2009, each for one or a few months
* Slug: adcp_moored_noaa_kod_1
* Included: True
* Feature type: timeSeriesProfile
* See the full dataset page for more information: {ref}`page:adcp_moored_noaa_kod_1`

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.

Stations "KOD0914", "KOD0915", "KOD0916", "KOD0917", "KOD0918", "KOD0919", "KOD0920" are not included because they are just outside or along the model domain boundary.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   |   depth | depths                                                                                                                                                                                                                   | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | key_variables                                 | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude | maxTime             |   measured_depth |   minLatitude |   minLongitude | minTime             | name                               | observe_dst   | orientation   | ping_int   | project                           | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   | urlpath                                                       |
|---:|:----------|--------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------------|--------------------------:|---------------------:|:----------------------------------------------|:--------------------|--------:|---------:|--------------:|---------------:|:--------------------|-----------------:|--------------:|---------------:|:--------------------|:-----------------------------------|:--------------|:--------------|:-----------|:----------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|:--------------------------------------------------------------|
|  0 | KOD0901   |    81.3 | [63.52, 61.51, 59.5, 57.52, 55.5, 53.52, 51.51, 49.5, 47.52, 45.51, 43.5, 41.51, 39.5, 37.52, 35.51, 33.5, 31.52, 29.5, 27.52, 25.51, 23.5, 21.52, 19.51, 17.5, 15.51, 13.5, 11.52, 9.51, 7.5]                           | timeSeriesProfile | 2009-05-29 18:06:00 |                       250 |                11.52 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-10 22:30:00 | 57.7356 | -152.385 |       57.7356 |       -152.385 | 2009-07-10 22:30:00 |            79.22 |       57.7356 |       -152.385 | 2009-05-29 18:06:00 | Chiniak Bay                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0901/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0901 |
|  1 | KOD0902   |    18.4 | [12.16, 11.16, 10.15, 9.14, 8.14, 7.16, 6.16, 5.15, 4.15, 3.14, 2.16]                                                                                                                                                    | timeSeriesProfile | 2009-05-29 00:54:00 |                        20 |                 3    | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-10 21:30:00 | 57.7746 | -152.435 |       57.7746 |       -152.435 | 2009-07-10 21:30:00 |            17.24 |       57.7746 |       -152.435 | 2009-05-29 00:54:00 | St. Paul Harbor                    | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0902/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0902 |
|  2 | KOD0903   |    13.3 | [9.94, 8.93, 7.92, 6.95, 5.94, 4.94, 3.93, 2.93, 1.95]                                                                                                                                                                   | timeSeriesProfile | 2009-05-29 03:42:00 |                        56 |                 0.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-20 01:11:00 | 57.7892 | -152.394 |       57.7892 |       -152.394 | 2009-08-20 01:11:00 |            12.64 |       57.7892 |       -152.394 | 2009-05-29 03:42:00 | Kodiak Harbor Narrows, Chiniak Bay | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0903/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0903 |
|  3 | KOD0904   |    47.3 | [30.11, 28.1, 26.12, 24.11, 22.1, 20.12, 18.11, 16.12, 14.11, 12.1, 10.12, 8.11, 6.1, 4.11]                                                                                                                              | timeSeriesProfile | 2009-05-29 03:00:00 |                        60 |                11.52 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-10 23:54:00 | 57.8058 | -152.334 |       57.8058 |       -152.334 | 2009-07-10 23:54:00 |            45.82 |       57.8058 |       -152.334 | 2009-05-29 03:00:00 | Woody Island, N of                 | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0904/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0904 |
|  4 | KOD0905   |    31.2 | [25.97, 24.99, 23.99, 22.98, 21.98, 20.97, 20.0, 18.99, 17.98, 16.98, 15.97, 14.97, 13.99, 12.98, 11.98, 10.97, 9.97, 8.99, 7.99, 6.98, 5.97, 4.97, 3.99, 2.99]                                                          | timeSeriesProfile | 2009-05-29 17:30:00 |                        20 |                 4.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-10 23:24:00 | 57.7804 | -152.366 |       57.7804 |       -152.366 | 2009-07-10 23:24:00 |            32.58 |       57.7804 |       -152.366 | 2009-05-29 17:30:00 | Woody Channel                      | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0905/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0905 |
|  5 | KOD0906   |    77.7 | [68.06, 66.05, 64.04, 62.06, 60.05, 58.07, 56.05, 54.04, 52.06, 50.05, 48.04, 46.06, 44.04, 42.06, 40.05, 38.04, 36.06, 34.05, 32.07, 30.05, 28.04, 26.06, 24.05, 22.04, 20.06, 18.04, 16.06, 14.05, 12.04, 10.06, 8.05] | timeSeriesProfile | 2009-05-29 20:24:00 |                        20 |                 5.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-11 19:17:00 | 57.6078 | -152.09  |       57.6078 |       -152.09  | 2009-07-11 19:17:00 |            77.74 |       57.6078 |       -152.09  | 2009-05-29 20:24:00 | Cape Chiniak                       | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0906/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0906 |
|  6 | KOD0907   |    73.9 | [62.24, 60.23, 58.22, 56.24, 54.22, 52.24, 50.23, 48.22, 46.24, 44.23, 42.22, 40.23, 38.22, 36.24, 34.23, 32.22, 30.24, 28.22, 26.24, 24.23, 22.22, 20.24, 18.23, 16.22, 14.23, 12.22, 10.24, 8.23]                      | timeSeriesProfile | 2009-05-30 00:18:00 |                       220 |                 5.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-12 01:06:00 | 57.3995 | -152.535 |       57.3995 |       -152.535 | 2009-07-12 01:06:00 |            71.92 |       57.3995 |       -152.535 | 2009-05-30 00:18:00 | Ugak Bay Entrance                  | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0907/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0907 |
|  7 | KOD0910   |   119   | [80.65, 76.63, 72.63, 68.64, 64.65, 60.66, 56.63, 52.64, 48.65, 44.65, 40.63, 36.64, 32.64, 28.65, 24.63, 20.64, 16.64, 12.65, 8.63]                                                                                     | timeSeriesProfile | 2009-05-30 19:00:00 |                       260 |                29.44 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-12 19:12:00 | 57.2309 | -152.884 |       57.2309 |       -152.884 | 2009-07-12 19:12:00 |           116.24 |       57.2309 |       -152.884 | 2009-05-30 19:00:00 | Left Cape, E of                    | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0910/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0910 |
|  8 | KOD0911   |   123   | [84.22, 80.22, 76.23, 72.21, 68.22, 64.22, 60.23, 56.21, 52.21, 48.22, 44.23, 40.23, 36.21, 32.22, 28.22, 24.23, 20.21, 16.22, 12.22, 8.23]                                                                              | timeSeriesProfile | 2009-05-30 17:36:00 |                       250 |                29.44 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-12 17:41:00 | 57.1978 | -153.105 |       57.1978 |       -153.105 | 2009-07-12 17:41:00 |           119.83 |       57.1978 |       -153.105 | 2009-05-30 17:36:00 | Cathedral Island, E of             | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0911/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0911 |
|  9 | KOD0912   |    74.2 | [55.66, 53.65, 51.66, 49.65, 47.64, 45.66, 43.65, 41.64, 39.65, 37.64, 35.66, 33.65, 31.64, 29.66, 27.65, 25.66, 23.65, 21.64, 19.66, 17.65, 15.64, 13.66, 11.64, 9.66, 7.65]                                            | timeSeriesProfile | 2009-05-31 01:30:00 |                       330 |                11.52 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-13 02:05:00 | 57.1787 | -153.325 |       57.1787 |       -153.325 | 2009-07-13 02:05:00 |            71.36 |       57.1787 |       -153.325 | 2009-05-31 01:30:00 | Old Harbor                         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0912/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0912 |
| 10 | KOD0913   |   120   | [79.22, 75.23, 71.2, 67.21, 63.22, 59.22, 55.2, 51.21, 47.21, 43.22, 39.2, 35.2, 31.21, 27.22, 23.2, 19.2, 15.21, 11.22, 7.22]                                                                                           | timeSeriesProfile | 2009-05-31 00:06:00 |                        30 |                29.44 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-13 00:36:00 | 57.0732 | -153.451 |       57.0732 |       -153.451 | 2009-07-13 00:36:00 |           114.81 |       57.0732 |       -153.451 | 2009-05-31 00:06:00 | Natalia Peninsula, W of            | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0913/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0913 |
| 11 | KOD0921   |    71.9 | [60.11, 58.1, 56.11, 54.1, 52.09, 50.11, 48.1, 46.09, 44.11, 42.09, 40.11, 38.1, 36.09, 34.11, 32.1, 30.11, 28.1, 26.09, 24.11, 22.1, 20.09, 18.11, 16.09, 14.11, 12.1, 10.09, 8.11]                                     | timeSeriesProfile | 2009-06-02 02:48:00 |                       350 |                 5.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-15 01:24:00 | 57.2861 | -154.828 |       57.2861 |       -154.828 | 2009-07-15 01:24:00 |            69.79 |       57.2861 |       -154.828 | 2009-06-02 02:48:00 | Cape Ikolik                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0921/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0921 |
| 12 | KOD0922   |    62.6 | [49.84, 47.82, 45.84, 43.83, 41.82, 39.84, 37.83, 35.84, 33.83, 31.82, 29.84, 27.83, 25.82, 23.84, 21.82, 19.84, 17.83, 15.82, 13.84, 11.83, 9.85, 7.83]                                                                 | timeSeriesProfile | 2009-06-02 17:36:00 |                        10 |                 5.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-15 02:54:00 | 57.4172 | -154.766 |       57.4172 |       -154.766 | 2009-07-15 02:54:00 |            59.52 |       57.4172 |       -154.766 | 2009-06-02 17:36:00 | Cape Grant                         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0922/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0922 |
| 13 | KOD0923   |    25   | [17.19, 16.19, 15.18, 14.2, 13.2, 12.19, 11.19, 10.18, 9.21, 8.2, 7.19, 6.19, 5.18, 4.18, 3.2, 2.19]                                                                                                                     | timeSeriesProfile | 2009-06-03 01:18:00 |                       315 |                 4.42 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-15 21:36:00 | 57.6373 | -153.995 |       57.6373 |       -153.995 | 2009-07-15 21:36:00 |            23.71 |       57.6373 |       -153.995 | 2009-06-03 01:18:00 | Uyak Anchorage                     | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0923/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0923 |
| 14 | KOD0924   |    16.8 | [10.12, 9.11, 8.11, 7.1, 6.1, 5.12, 4.11, 3.11, 2.1]                                                                                                                                                                     | timeSeriesProfile | 2009-06-03 02:42:00 |                       290 |                 2.95 | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-15 23:00:00 | 57.5422 | -153.988 |       57.5422 |       -153.988 | 2009-07-15 23:00:00 |            15.16 |       57.5422 |       -153.988 | 2009-06-03 02:42:00 | Larsen Bay                         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0924/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0924 |
| 15 | KOD0925   |    63   | [51.63, 49.65, 47.64, 45.63, 43.65, 41.64, 39.65, 37.64, 35.63, 33.65, 31.64, 29.63, 27.65, 25.63, 23.65, 21.64, 19.63, 17.65, 15.64, 13.66, 11.64, 9.63, 7.65]                                                          | timeSeriesProfile | 2009-06-02 23:36:00 |                        45 |                 5.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-07-16 21:48:00 | 57.7935 | -154.032 |       57.7935 |       -154.032 | 2009-07-16 21:48:00 |            61.33 |       57.7935 |       -154.032 | 2009-06-02 23:36:00 | Cape Kuliuk                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0925/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0925 |

```
````

+++




**Map of Moored ADCPs**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_kod_1")("adcp_moored_noaa_kod_1")
```


### Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 2

* Kodiak Island 2009 Current Survey (2)
* 2009, each for one or a few months
* Slug: adcp_moored_noaa_kod_2
* Included: True
* Feature type: timeSeriesProfile
* See the full dataset page for more information: {ref}`page:adcp_moored_noaa_kod_2`

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   |   depth | depths                                                                                                                                                                              | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | key_variables                                 | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude | maxTime             |   measured_depth |   minLatitude |   minLongitude | minTime             | name                                      | observe_dst   | orientation   | ping_int   | project                           | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   | urlpath                                                       |
|---:|:----------|--------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|:--------------------|--------------------------:|---------------------:|:----------------------------------------------|:--------------------|--------:|---------:|--------------:|---------------:|:--------------------|-----------------:|--------------:|---------------:|:--------------------|:------------------------------------------|:--------------|:--------------|:-----------|:----------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|:--------------------------------------------------------------|
|  0 | KOD0926   |    59   | [46.88, 44.9, 42.89, 40.9, 38.89, 36.88, 34.9, 32.89, 30.88, 28.9, 26.88, 24.9, 22.89, 20.88, 18.9, 16.89, 14.9, 12.89, 10.88, 8.9, 6.89]                                           | timeSeriesProfile | 2009-06-03 23:36:00 |                        50 |                 5.5  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-30 01:06:00 | 58.2145 | -153.22  |       58.2145 |       -153.22  | 2009-08-30 01:06:00 |            56.58 |       58.2145 |       -153.22  | 2009-06-03 23:36:00 | Steep Cape                                | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0926/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0926 |
|  1 | KOD0927   |    86.2 | [74.49, 71.48, 68.49, 65.47, 62.48, 59.47, 56.48, 53.49, 50.48, 47.49, 44.47, 41.48, 38.47, 35.48, 32.49, 29.47, 26.49, 23.47, 20.48, 17.47, 14.48, 11.49]                          | timeSeriesProfile | 2009-07-17 02:00:00 |                       270 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-29 20:18:00 | 58.019  | -153.43  |       58.019  |       -153.43  | 2009-08-29 20:18:00 |            85.28 |       58.019  |       -153.43  | 2009-07-17 02:00:00 | Raspberry Cape, S of                      | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0927/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0927 |
|  2 | KOD0928   |    61.8 | [47.64, 45.66, 43.65, 41.64, 39.65, 37.64, 35.66, 33.65, 31.64, 29.66, 27.65, 25.66, 23.65, 21.64, 19.66, 17.65, 15.64, 13.66, 11.64, 9.66, 7.65, 5.64]                             | timeSeriesProfile | 2009-07-17 03:30:00 |                       285 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-01 18:06:00 | 57.9976 | -153.156 |       57.9976 |       -153.156 | 2009-09-01 18:06:00 |            57.46 |       57.9976 |       -153.156 | 2009-07-17 03:30:00 | Kupreanof Strait                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0928/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0928 |
|  3 | KOD0929   |    28.9 | [21.61, 20.64, 19.63, 18.62, 17.62, 16.61, 15.61, 14.63, 13.62, 12.62, 11.61, 10.61, 9.63, 8.63, 7.62, 6.61, 5.61, 4.63, 3.63]                                                      | timeSeriesProfile | 2009-07-22 04:48:00 |                       280 |                 4.52 | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-01 20:54:00 | 57.9604 | -152.901 |       57.9604 |       -152.901 | 2009-09-01 20:54:00 |            28.24 |       57.9604 |       -152.901 | 2009-07-22 04:48:00 | Kupreanof Strait, 0.8 mi. off Chernof Pt. | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0929/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0929 |
|  4 | KOD0930   |    32.9 | [25.36, 23.38, 21.37, 19.36, 17.37, 15.36, 13.38, 11.37, 9.36, 7.38, 5.36]                                                                                                          | timeSeriesProfile | 2009-07-22 15:48:00 |                       280 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-01 20:54:00 | 57.9396 | -152.863 |       57.9396 |       -152.863 | 2009-09-01 20:54:00 |            34.04 |       57.9396 |       -152.863 | 2009-07-22 15:48:00 | Whale Passage, Northwest Entrance         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0930/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0930 |
|  5 | KOD0931   |    31.3 | [22.13, 21.12, 20.12, 19.14, 18.14, 17.13, 16.12, 15.12, 14.14, 13.14, 12.13, 11.13, 10.12, 9.14, 8.14, 7.13, 6.13, 5.12, 4.11, 3.14, 2.13]                                         | timeSeriesProfile | 2009-07-17 17:24:00 |                       285 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-02 02:24:00 | 57.9188 | -152.795 |       57.9188 |       -152.795 | 2009-09-02 02:24:00 |            29.83 |       57.9188 |       -152.795 | 2009-07-17 17:24:00 | Whale Passage, off Bird Point             | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0931/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0931 |
|  6 | KOD0932   |    59.1 | [51.42, 49.41, 47.43, 45.42, 43.43, 41.42, 39.41, 37.43, 35.42, 33.41, 31.43, 29.41, 27.43, 25.42, 23.41, 21.43, 19.42, 17.43, 15.42, 13.41, 11.43, 9.42, 7.41]                     | timeSeriesProfile | 2009-07-17 17:54:00 |                       330 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-02 01:00:00 | 57.9075 | -152.777 |       57.9075 |       -152.777 | 2009-09-02 01:00:00 |            61.22 |       57.9075 |       -152.777 | 2009-07-17 17:54:00 | Shag Rocks                                | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0932/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0932 |
|  7 | KOD0933   |    34.1 | [25.63, 23.62, 21.64, 19.63, 17.62, 15.64, 13.62, 11.64, 9.63, 7.62, 5.64, 3.63]                                                                                                    | timeSeriesProfile | 2009-07-17 20:12:00 |                       290 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-01 23:30:00 | 57.9121 | -152.524 |       57.9121 |       -152.524 | 2009-09-01 23:30:00 |            34.32 |       57.9121 |       -152.524 | 2009-07-17 20:12:00 | Narrow Strait, off Ouzinkie Point         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0933/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0933 |
|  8 | KOD0934   |    41.1 | [29.41, 27.43, 25.42, 23.41, 21.43, 19.42, 17.43, 15.42, 13.41, 11.43, 9.42, 7.41, 5.43, 3.41]                                                                                      | timeSeriesProfile | 2009-07-17 18:54:00 |                       260 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-09-01 01:30:00 | 57.9947 | -152.684 |       57.9947 |       -152.684 | 2009-09-01 01:30:00 |            39.22 |       57.9947 |       -152.684 | 2009-07-17 18:54:00 | Afognak Strait, East Entrance             | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0934/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0934 |
|  9 | KOD0935   |    64.3 | [51.63, 49.62, 47.64, 45.63, 43.62, 41.64, 39.62, 37.64, 35.63, 33.62, 31.64, 29.63, 27.62, 25.63, 23.62, 21.64, 19.63, 17.62, 15.64, 13.62, 11.64, 9.63, 7.62]                     | timeSeriesProfile | 2009-07-21 21:06:00 |                       160 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-29 23:06:00 | 58.0718 | -153.065 |       58.0718 |       -153.065 | 2009-08-29 23:06:00 |            61.43 |       58.0718 |       -153.065 | 2009-07-21 21:06:00 | Raspberry Strait                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0935/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0935 |
| 10 | KOD0936   |    42.2 | [28.86, 26.88, 24.87, 22.86, 20.88, 18.87, 16.86, 14.87, 12.86, 10.88, 8.87, 6.86, 4.88]                                                                                            | timeSeriesProfile | 2009-07-20 23:24:00 |                       180 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-30 17:42:00 | 58.4057 | -152.907 |       58.4057 |       -152.907 | 2009-08-30 17:42:00 |            38.67 |       58.4057 |       -152.907 | 2009-07-20 23:24:00 | Black Cape                                | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0936/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0936 |
| 11 | KOD0937   |    43.8 | [30.69, 28.68, 26.7, 24.69, 22.68, 20.7, 18.68, 16.7, 14.69, 12.68, 10.7, 8.69, 6.68, 4.69]                                                                                         | timeSeriesProfile | 2009-07-20 22:30:00 |                       235 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-30 18:30:00 | 58.4611 | -152.826 |       58.4611 |       -152.826 | 2009-08-30 18:30:00 |            40.49 |       58.4611 |       -152.826 | 2009-07-20 22:30:00 | Alligator Island                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0937/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0937 |
| 12 | KOD0938   |   109   | [90.22, 87.23, 84.22, 81.23, 78.24, 75.23, 72.24, 69.22, 66.23, 63.22, 60.23, 57.24, 54.22, 51.24, 48.22, 45.23, 42.22, 39.23, 36.24, 33.22, 30.24, 27.22, 24.23, 21.24]            | timeSeriesProfile | 2009-07-20 21:30:00 |                       250 |                25.17 | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-31 00:29:00 | 58.4852 | -152.67  |       58.4852 |       -152.67  | 2009-08-31 00:29:00 |           120.59 |       58.4852 |       -152.67  | 2009-07-20 21:30:00 | Lighthouse Point                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0938/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0938 |
| 13 | KOD0939   |    36   | [30.3, 29.29, 28.29, 27.28, 26.3, 25.3, 24.29, 23.29, 22.28, 21.28, 20.3, 19.29, 18.29, 17.28, 16.28, 15.3, 14.3, 13.29, 12.28, 11.28, 10.3, 9.3, 8.29, 7.28, 6.28, 5.3, 4.3, 3.29] | timeSeriesProfile | 2009-07-20 20:12:00 |                       275 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-31 02:23:00 | 58.4669 | -152.495 |       58.4669 |       -152.495 | 2009-08-31 02:23:00 |            37.99 |       58.4669 |       -152.495 | 2009-07-20 20:12:00 | Cape Current Narrows, Shuyak Strait       | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0939/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0939 |
| 14 | KOD0940   |   108   | [70.74, 67.73, 64.74, 61.75, 58.74, 55.75, 52.73, 49.74, 46.73, 43.74, 40.75, 37.73, 34.75, 31.73, 28.74, 25.73, 22.74, 19.75, 16.73, 13.75, 10.73, 7.74]                           | timeSeriesProfile | 2009-07-20 00:00:00 |                       215 |                29.67 | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-31 02:17:00 | 58.4579 | -152.428 |       58.4579 |       -152.428 | 2009-08-31 02:17:00 |           105.6  |       58.4579 |       -152.428 | 2009-07-20 00:00:00 | East Shuyak Strait                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0940/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0940 |
| 15 | KOD0941   |    50.5 | [42.0, 39.99, 38.01, 36.0, 33.99, 32.0, 29.99, 28.01, 26.0, 23.99, 22.01, 20.0, 18.01, 16.0, 13.99, 12.01, 10.0, 7.99]                                                              | timeSeriesProfile | 2009-07-19 00:24:00 |                       350 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-31 19:12:00 | 58.346  | -151.915 |       58.346  |       -151.915 | 2009-08-31 19:12:00 |            51.8  |       58.346  |       -151.915 | 2009-07-19 00:24:00 | Tonki Cape, E of                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0941/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0941 |
| 16 | KOD0942   |    63.2 | [51.42, 49.41, 47.4, 45.42, 43.4, 41.42, 39.41, 37.4, 35.42, 33.41, 31.43, 29.41, 27.4, 25.42, 23.41, 21.4, 19.42, 17.4, 15.42, 13.41, 11.4, 9.42, 7.41]                            | timeSeriesProfile | 2009-07-18 23:12:00 |                         0 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-31 20:36:00 | 58.2444 | -151.932 |       58.2444 |       -151.932 | 2009-08-31 20:36:00 |            61.21 |       58.2444 |       -151.932 | 2009-07-18 23:12:00 | Marmot Island, W of                       | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0942/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0942 |
| 17 | KOD0943   |    66.2 | [54.71, 52.73, 50.72, 48.71, 46.73, 44.71, 42.73, 40.72, 38.71, 36.73, 34.72, 32.71, 30.72, 28.71, 26.73, 24.72, 22.71, 20.73, 18.71, 16.73, 14.72, 12.71, 10.73, 8.72, 6.71]       | timeSeriesProfile | 2009-07-18 22:06:00 |                         5 |                 5.6  | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-31 21:47:00 | 58.1709 | -151.969 |       58.1709 |       -151.969 | 2009-08-31 21:47:00 |            64.52 |       58.1709 |       -151.969 | 2009-07-18 22:06:00 | Marmot Island, SW of                      | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0943/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0943 |
| 18 | KOD0944   |    63.1 | [44.01, 42.03, 40.02, 38.01, 36.03, 34.02, 32.03, 30.02, 28.01, 26.03, 24.02, 22.01, 20.03, 18.01, 16.03, 14.02, 12.01, 10.03, 8.02, 6.04]                                          | timeSeriesProfile | 2009-07-19 19:42:00 |                       270 |                11.52 | ['east', 'north', 'along', 'across', 'speed'] | 2009-08-30 21:24:00 | 58.6511 | -152.397 |       58.6511 |       -152.397 | 2009-08-30 21:24:00 |            59.74 |       58.6511 |       -152.397 | 2009-07-19 19:42:00 | Perevalnie Island, N of                   | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0944/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0944 |

```
````

+++




**Map of Moored ADCPs**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_kod_2")("adcp_moored_noaa_kod_2")
```


### Towed ADCP (OTF KBNERR): central Cook Inlet

* ADCP towed 2003-2005 - OTF KBNERR
* July 2003
* Slug: adcp_towed_otf_kbnerr
* Included: False
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:adcp_towed_otf_kbnerr`

Towed ADCPs

Short, high resolution towed ADCP in the middle of Cook Inlet


Notes:

There are processed files from 2003. However, they are too short in duration to be useful in comparison to the model output. There are unprocessed files from 2004 and 2005. No further steps were taken with these datasets.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                  | featuretype       | urlpath                                                                   |
|---:|:-------------------------|:------------------|:--------------------------------------------------------------------------|
|  0 | OTF20030708110414_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337509/OTF20030708110414_000_bp.mat |
|  1 | OTF20030708132652_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337510/OTF20030708132652_000_bp.mat |
|  2 | OTF20030708152426_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337511/OTF20030708152426_000_bp.mat |
|  3 | OTF20030709062221_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337512/OTF20030709062221_000_bp.mat |
|  4 | OTF20030709062804_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337513/OTF20030709062804_000_bp.mat |
|  5 | OTF20030710113053_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337514/OTF20030710113053_000_bp.mat |
|  6 | OTF20030710133148_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337515/OTF20030710133148_000_bp.mat |
|  7 | OTF20030710143516_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337516/OTF20030710143516_000_bp.mat |
|  8 | OTF20030710144435_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337517/OTF20030710144435_000_bp.mat |
|  9 | OTF20030710164039_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337518/OTF20030710164039_000_bp.mat |
| 10 | OTF20030711071931_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337519/OTF20030711071931_000_bp.mat |
| 11 | OTF20030711074806_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337520/OTF20030711074806_000_bp.mat |
| 12 | OTF20030711100411_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337521/OTF20030711100411_000_bp.mat |
| 13 | OTF20030711112007_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337522/OTF20030711112007_000_bp.mat |
| 14 | OTF20030711112103_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337523/OTF20030711112103_000_bp.mat |
| 15 | OTF20030714132157_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337524/OTF20030714132157_000_bp.mat |
| 16 | OTF20030719064121_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337525/OTF20030719064121_000_bp.mat |
| 17 | OTF20030722111506_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337526/OTF20030722111506_000_bp.mat |
| 18 | OTF20030724113401_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337527/OTF20030724113401_000_bp.mat |
| 19 | OTF20030724134054_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337528/OTF20030724134054_000_bp.mat |
| 20 | OTF20030724141257_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337529/OTF20030724141257_000_bp.mat |
| 21 | OTF20030724150005_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337530/OTF20030724150005_000_bp.mat |
| 22 | OTF20030725065556_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337531/OTF20030725065556_000_bp.mat |
| 23 | OTF20030725074445_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337532/OTF20030725074445_000_bp.mat |
| 24 | OTF20030726110828_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337533/OTF20030726110828_000_bp.mat |
| 25 | OTF20030728113330_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337534/OTF20030728113330_000_bp.mat |
| 26 | OTF20030728145659_000_bp | trajectoryProfile | https://researchworkspace.com/files/40337508/OTF20030728145659_000_bp.mat |

```
````

+++


### Mooring (CIRCAC): Central Cook Inlet Mooring

* CTD Moored 2006 - CIRCAC
* Two weeks in August 2006, 15 min sampling
* Slug: ctd_moored_circac
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:ctd_moored_circac`

Central Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

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



Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset           | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                           |
|---:|:------------------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------------------|
|  0 | ctd_moored_circac | timeSeries    | ['temp', 'salt'] |       60.7617 |       -151.505 | 2006-08-28 18:32:00 |       60.7617 |       -151.505 | 2006-08-11 23:32:00 | https://researchworkspace.com/files/39886029/xto_mooring_2006.txt |

```
````

+++




**Map of Time Series Location**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_moored_circac")("ctd_moored_circac")
```


### Mooring (KBNERR): Lower Cook Inlet Mooring

* CTD Moored 2006-2008 - KBNERR
* Aug to Oct 2006 and June 2007 to Feb 2008, 15 min sampling
* Slug: ctd_moored_kbnerr
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:ctd_moored_kbnerr`

Lower Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

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



Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset     | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                          |
|---:|:------------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:---------------------------------------------------------------------------------|
|  0 | Deployment1 | timeSeries    | ['temp', 'salt'] |       59.2027 |       -151.848 | 2006-10-28 10:22:00 |       59.2027 |       -151.848 | 2006-08-12 18:22:00 | https://researchworkspace.com/files/39886044/chrome_bay_mooring_deployment_1.txt |
|  1 | Deployment2 | timeSeries    | ['temp', 'salt'] |       59.2027 |       -151.848 | 2008-02-25 05:28:00 |       59.2027 |       -151.848 | 2007-06-20 21:00:00 | https://researchworkspace.com/files/39886045/chrome_bay_mooring_deployment_2.txt |

```
````

+++




**Map of Time Series Location**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_moored_kbnerr")("ctd_moored_kbnerr")
```


### CTD Profiles (NOAA): across Cook Inlet

* CTD profiles 2005 - NOAA
* One-off CTD profiles in June and July 2005
* Slug: ctd_profiles_2005_noaa
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_2005_noaa`

CTD Profiles from NOAA.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                     |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------------|
|  0 |       501 | profile       | ['temp', 'salt'] |       60.722  |       -151.647 | 2005-06-16 15:34:00 |       60.722  |       -151.647 | 2005-06-16 15:34:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  1 |       502 | profile       | ['temp', 'salt'] |       60.7207 |       -151.557 | 2005-06-16 15:08:00 |       60.7207 |       -151.557 | 2005-06-16 15:08:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  2 |       503 | profile       | ['temp', 'salt'] |       60.7173 |       -151.433 | 2005-06-16 14:34:00 |       60.7173 |       -151.433 | 2005-06-16 14:34:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  3 |       504 | profile       | ['temp', 'salt'] |       60.6834 |       -151.418 | 2005-06-16 14:01:00 |       60.6834 |       -151.418 | 2005-06-16 14:01:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  4 |       505 | profile       | ['temp', 'salt'] |       60.5967 |       -151.739 | 2005-06-16 16:33:00 |       60.5967 |       -151.739 | 2005-06-16 16:33:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  5 |       506 | profile       | ['temp', 'salt'] |       60.5871 |       -151.445 | 2005-06-16 12:47:00 |       60.5871 |       -151.445 | 2005-06-16 12:47:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  6 |       507 | profile       | ['temp', 'salt'] |       60.5517 |       -152.128 | 2005-06-16 18:14:00 |       60.5517 |       -152.128 | 2005-06-16 18:14:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  7 |       508 | profile       | ['temp', 'salt'] |       60.483  |       -151.673 | 2005-06-16 11:07:00 |       60.483  |       -151.673 | 2005-06-16 11:07:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  8 |       509 | profile       | ['temp', 'salt'] |       60.3792 |       -152.182 | 2005-06-16 20:07:00 |       60.3792 |       -152.182 | 2005-06-16 20:07:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  9 |       510 | profile       | ['temp', 'salt'] |       60.248  |       -151.755 | 2005-06-16 09:05:00 |       60.248  |       -151.755 | 2005-06-16 09:05:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
| 10 |       511 | profile       | ['temp', 'salt'] |       60.0233 |       -152.12  | 2005-07-28 20:04:00 |       60.0233 |       -152.12  | 2005-07-28 20:04:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 11 |       512 | profile       | ['temp', 'salt'] |       59.5661 |       -153.422 | 2005-07-29 05:12:00 |       59.5661 |       -153.422 | 2005-07-29 05:12:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 12 |       513 | profile       | ['temp', 'salt'] |       59.4828 |       -151.755 | 2005-07-30 23:40:00 |       59.4828 |       -151.755 | 2005-07-30 23:40:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 13 |       514 | profile       | ['temp', 'salt'] |       59.3018 |       -152.92  | 2005-07-29 10:51:00 |       59.3018 |       -152.92  | 2005-07-29 10:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 14 |       515 | profile       | ['temp', 'salt'] |       59.3149 |       -152.365 | 2005-07-30 19:51:00 |       59.3149 |       -152.365 | 2005-07-30 19:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 15 |       516 | profile       | ['temp', 'salt'] |       59.4001 |       -151.966 | 2005-07-30 22:32:00 |       59.4001 |       -151.966 | 2005-07-30 22:32:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 16 |       517 | profile       | ['temp', 'salt'] |       58.8901 |       -153.184 | 2005-07-29 14:36:00 |       58.8901 |       -153.184 | 2005-07-29 14:36:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 17 |       518 | profile       | ['temp', 'salt'] |       58.9305 |       -152.728 | 2005-07-30 09:24:00 |       58.9305 |       -152.728 | 2005-07-30 09:24:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 18 |       519 | profile       | ['temp', 'salt'] |       58.808  |       -152.408 | 2005-07-30 04:08:00 |       58.808  |       -152.408 | 2005-07-30 04:08:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 19 |       520 | profile       | ['temp', 'salt'] |       59.0492 |       -152.152 | 2005-07-30 11:51:00 |       59.0492 |       -152.152 | 2005-07-30 11:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 20 |       521 | profile       | ['temp', 'salt'] |       59.1207 |       -151.895 | 2005-07-30 17:33:00 |       59.1207 |       -151.895 | 2005-07-30 17:33:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 21 |       522 | profile       | ['temp', 'salt'] |       59.2112 |       -151.787 | 2005-07-30 15:36:00 |       59.2112 |       -151.787 | 2005-07-30 15:36:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 22 |       523 | profile       | ['temp', 'salt'] |       59.0129 |       -151.775 | 2005-07-30 16:03:00 |       59.0129 |       -151.775 | 2005-07-30 16:03:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 23 |       524 | profile       | ['temp', 'salt'] |       59.1339 |       -151.706 | 2005-07-30 16:51:00 |       59.1339 |       -151.706 | 2005-07-30 16:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_2005_noaa")("ctd_profiles_2005_noaa")
```


### Moored CTDs (OSU): Time series of CTD profiles at several locations in Cook Inlet

* CTD profiles 2005 - OSU
* June 2005
* Slug: ctd_profiles_2005_osu
* Included: False
* Feature type: timeSeriesProfile
* See the full dataset page for more information: {ref}`page:ctd_profiles_2005_osu`



Notes:

Locations given are too low resolution making them incorrectly on land.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset    | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime                    |   minLatitude |   minLongitude | minTime                    | urlpath                                                                    |
|---:|:-----------|:------------------|:-----------------|--------------:|---------------:|:---------------------------|--------------:|---------------:|:---------------------------|:---------------------------------------------------------------------------|
|  0 | AK060605_0 | timeSeriesProfile | ['temp', 'salt'] |          59.6 |           -152 | 2005-06-06 22:56:38.400000 |          59.6 |           -152 | 2005-06-06 20:00:57.600000 | https://researchworkspace.com/files/39886085/AK060605_004_final_header.txt |
|  1 | AK060605_1 | timeSeriesProfile | ['temp', 'salt'] |          59.6 |           -151 | 2005-06-06 23:54:14.400000 |          59.6 |           -151 | 2005-06-06 22:56:38.400000 | https://researchworkspace.com/files/39886085/AK060605_004_final_header.txt |
|  2 | AK060705_0 | timeSeriesProfile | ['temp', 'salt'] |          59.4 |           -152 | 2005-06-07 22:40:48        |          59.4 |           -152 | 2005-06-07 22:13:26.400000 | https://researchworkspace.com/files/39886087/AK060705_002_final_header.txt |
|  3 | AK060705_1 | timeSeriesProfile | ['temp', 'salt'] |          59.5 |           -152 | 2005-06-07 23:26:52.800000 |          59.5 |           -152 | 2005-06-07 22:40:48        | https://researchworkspace.com/files/39886087/AK060705_002_final_header.txt |
|  4 | AK060805_0 | timeSeriesProfile | ['temp', 'salt'] |          59.5 |           -152 | 2005-06-08 21:41:45.600000 |          59.5 |           -152 | 2005-06-08 20:55:40.800000 | https://researchworkspace.com/files/39886090/AK060805_002_final_header.txt |
|  5 | AK060805_1 | timeSeriesProfile | ['temp', 'salt'] |          59.6 |           -152 | 2005-06-08 22:43:40.800000 |          59.6 |           -152 | 2005-06-08 21:41:45.600000 | https://researchworkspace.com/files/39886090/AK060805_002_final_header.txt |
|  6 | AK060905_0 | timeSeriesProfile | ['temp', 'salt'] |          59.4 |           -151 | 2005-06-09 20:26:52.800000 |          59.4 |           -151 | 2005-06-09 19:40:48        | https://researchworkspace.com/files/39886092/AK060905_001_final_header.txt |
|  7 | AK060905_1 | timeSeriesProfile | ['temp', 'salt'] |          59.5 |           -151 | 2005-06-09 21:36:00        |          59.5 |           -151 | 2005-06-09 20:26:52.800000 | https://researchworkspace.com/files/39886092/AK060905_001_final_header.txt |

```
````

+++


### CTD Profiles (emap 2002)

* emap 2002
* One-off CTD profiles June to August 2002
* Slug: ctd_profiles_emap_2002
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_emap_2002`

CTD Profiles in Cook Inlet

Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                               |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------|
|  0 |        10 | profile       | ['temp', 'salt'] |       57.7088 |       -155.568 | 2002-08-18 22:21:00 |       57.7088 |       -155.568 | 2002-08-18 22:21:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  1 |        11 | profile       | ['temp', 'salt'] |       61.0326 |       -151.235 | 2002-08-01 22:50:00 |       61.0326 |       -151.235 | 2002-08-01 22:50:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  2 |        12 | profile       | ['temp', 'salt'] |       60.7028 |       -151.86  | 2002-08-01 03:50:00 |       60.7028 |       -151.86  | 2002-08-01 03:50:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  3 |        15 | profile       | ['temp', 'salt'] |       60.4996 |       -151.964 | 2002-08-01 17:00:00 |       60.4996 |       -151.964 | 2002-08-01 17:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  4 |        16 | profile       | ['temp', 'salt'] |       60.2494 |       -151.528 | 2002-07-31 16:08:00 |       60.2494 |       -151.528 | 2002-07-31 16:08:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  5 |        17 | profile       | ['temp', 'salt'] |       59.9748 |       -152.344 | 2002-07-10 18:00:00 |       59.9748 |       -152.344 | 2002-07-10 18:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  6 |        19 | profile       | ['temp', 'salt'] |       59.2895 |       -152.841 | 2002-06-17 05:20:00 |       59.2895 |       -152.841 | 2002-06-17 05:20:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  7 |         2 | profile       | ['temp', 'salt'] |       60.2097 |       -152.738 | 2002-07-10 23:00:00 |       60.2097 |       -152.738 | 2002-07-10 23:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  8 |        20 | profile       | ['temp', 'salt'] |       59.1081 |       -153.552 | 2002-07-07 16:43:00 |       59.1081 |       -153.552 | 2002-07-07 16:43:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  9 |        21 | profile       | ['temp', 'salt'] |       59.1419 |       -152.331 | 2002-06-14 22:30:00 |       59.1419 |       -152.331 | 2002-06-14 22:30:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 10 |        23 | profile       | ['temp', 'salt'] |       59.0887 |       -153.089 | 2002-06-15 01:45:00 |       59.0887 |       -153.089 | 2002-06-15 01:45:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 11 |        24 | profile       | ['temp', 'salt'] |       58.7848 |       -152.817 | 2002-06-15 16:23:00 |       58.7848 |       -152.817 | 2002-06-15 16:23:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 12 |        26 | profile       | ['temp', 'salt'] |       58.5051 |       -152.833 | 2002-07-06 22:15:00 |       58.5051 |       -152.833 | 2002-07-06 22:15:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 13 |        27 | profile       | ['temp', 'salt'] |       58.0897 |       -153.502 | 2002-08-18 15:14:00 |       58.0897 |       -153.502 | 2002-08-18 15:14:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 14 |        28 | profile       | ['temp', 'salt'] |       57.9256 |       -154.29  | 2002-08-17 19:37:00 |       57.9256 |       -154.29  | 2002-08-17 19:37:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 15 |        29 | profile       | ['temp', 'salt'] |       57.8523 |       -154.552 | 2002-08-18 00:06:00 |       57.8523 |       -154.552 | 2002-08-18 00:06:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 16 |         3 | profile       | ['temp', 'salt'] |       59.8293 |       -153.128 | 2002-07-09 00:30:00 |       59.8293 |       -153.128 | 2002-07-09 00:30:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 17 |        30 | profile       | ['temp', 'salt'] |       57.6196 |       -155.186 | 2002-08-19 02:00:00 |       57.6196 |       -155.186 | 2002-08-19 02:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 18 |         4 | profile       | ['temp', 'salt'] |       59.6204 |       -151.248 | 2002-07-30 16:28:00 |       59.6204 |       -151.248 | 2002-07-30 16:28:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 19 |         5 | profile       | ['temp', 'salt'] |       59.2097 |       -151.822 | 2002-07-14 14:31:00 |       59.2097 |       -151.822 | 2002-07-14 14:31:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 20 |        65 | profile       | ['temp', 'salt'] |       58.4439 |       -152.349 | 2002-07-02 19:00:00 |       58.4439 |       -152.349 | 2002-07-02 19:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 21 |        67 | profile       | ['temp', 'salt'] |       57.1963 |       -153.207 | 2002-06-30 01:00:00 |       57.1963 |       -153.207 | 2002-06-30 01:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 22 |        68 | profile       | ['temp', 'salt'] |       57.0624 |       -153.576 | 2002-06-29 16:30:00 |       57.0624 |       -153.576 | 2002-06-29 16:30:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 23 |         7 | profile       | ['temp', 'salt'] |       58.3883 |       -152.981 | 2002-07-06 18:06:00 |       58.3883 |       -152.981 | 2002-07-06 18:06:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 24 |         8 | profile       | ['temp', 'salt'] |       57.9768 |       -154.956 | 2002-08-17 16:34:00 |       57.9768 |       -154.956 | 2002-08-17 16:34:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 25 |         9 | profile       | ['temp', 'salt'] |       57.9808 |       -153.071 | 2002-07-06 02:05:00 |       57.9808 |       -153.071 | 2002-07-06 02:05:00 | https://researchworkspace.com/files/42199527/emap.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_emap_2002")("ctd_profiles_emap_2002")
```


### CTD Profiles (emap 2008)

* emap 2008
* One-off CTD profiles August to October 2008
* Slug: ctd_profiles_emap_2008
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_emap_2008`

CTD Profiles in Cook Inlet

Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset     | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                |
|---:|:------------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------------|
|  0 | AKCI08-001  | profile       | ['temp', 'salt'] |       58.8677 |       -153.314 | 2008-08-06 15:09:00 |       58.8677 |       -153.314 | 2008-08-06 15:09:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  1 | AKCI08-002  | profile       | ['temp', 'salt'] |       59.1065 |       -153.417 | 2008-08-06 18:08:00 |       59.1065 |       -153.417 | 2008-08-06 18:08:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  2 | AKCI08-003  | profile       | ['temp', 'salt'] |       60.5112 |       -151.852 | 2008-08-14 14:51:00 |       60.5112 |       -151.852 | 2008-08-14 14:51:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  3 | AKCI08-004  | profile       | ['temp', 'salt'] |       60.9415 |       -151.508 | 2008-08-20 10:59:00 |       60.9415 |       -151.508 | 2008-08-20 10:59:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  4 | AKCI08-005  | profile       | ['temp', 'salt'] |       60.2248 |       -151.425 | 2008-08-28 10:01:00 |       60.2248 |       -151.425 | 2008-08-28 10:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  5 | AKCI08-007  | profile       | ['temp', 'salt'] |       60.8294 |       -151.679 | 2008-08-24 08:40:00 |       60.8294 |       -151.679 | 2008-08-24 08:40:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  6 | AKCI08-008  | profile       | ['temp', 'salt'] |       60.9409 |       -151.109 | 2008-08-19 18:33:00 |       60.9409 |       -151.109 | 2008-08-19 18:33:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  7 | AKCI08-009  | profile       | ['temp', 'salt'] |       59.4453 |       -152.145 | 2008-08-04 12:57:00 |       59.4453 |       -152.145 | 2008-08-04 12:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  8 | AKCI08-011  | profile       | ['temp', 'salt'] |       60.8088 |       -151.717 | 2008-08-24 19:40:00 |       60.8088 |       -151.717 | 2008-08-24 19:40:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  9 | AKCI08-012  | profile       | ['temp', 'salt'] |       60.8944 |       -151.171 | 2008-08-19 15:23:00 |       60.8944 |       -151.171 | 2008-08-19 15:23:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 10 | AKCI08-013  | profile       | ['temp', 'salt'] |       59.3351 |       -152.772 | 2008-08-05 13:53:00 |       59.3351 |       -152.772 | 2008-08-05 13:53:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 11 | AKCI08-015  | profile       | ['temp', 'salt'] |       60.7357 |       -151.663 | 2008-08-23 16:20:00 |       60.7357 |       -151.663 | 2008-08-23 16:20:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 12 | AKCI08-016  | profile       | ['temp', 'salt'] |       60.7442 |       -151.334 | 2008-08-25 15:52:00 |       60.7442 |       -151.334 | 2008-08-25 15:52:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 13 | AKCI08-017  | profile       | ['temp', 'salt'] |       59.7346 |       -152.474 | 2008-08-10 12:11:00 |       59.7346 |       -152.474 | 2008-08-10 12:11:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 14 | AKCI08-018  | profile       | ['temp', 'salt'] |       59.2343 |       -153.805 | 2008-08-08 15:05:00 |       59.2343 |       -153.805 | 2008-08-08 15:05:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 15 | AKCI08-021  | profile       | ['temp', 'salt'] |       60.2332 |       -152.453 | 2008-08-27 16:26:00 |       60.2332 |       -152.453 | 2008-08-27 16:26:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 16 | AKCI08-023  | profile       | ['temp', 'salt'] |       60.8161 |       -151.721 | 2008-08-24 14:52:00 |       60.8161 |       -151.721 | 2008-08-24 14:52:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 17 | AKCI08-024  | profile       | ['temp', 'salt'] |       60.9327 |       -151.318 | 2008-08-19 20:50:00 |       60.9327 |       -151.318 | 2008-08-19 20:50:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 18 | AKCI08-026  | profile       | ['temp', 'salt'] |      nan      |        nan     | 2008-10-07 14:57:00 |      nan      |        nan     | 2008-10-07 14:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 19 | AKCI08-027  | profile       | ['temp', 'salt'] |       60.806  |       -151.688 | 2008-08-24 19:17:00 |       60.806  |       -151.688 | 2008-08-24 19:17:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 20 | AKCI08-028  | profile       | ['temp', 'salt'] |       60.8132 |       -151.257 | 2008-08-20 16:01:00 |       60.8132 |       -151.257 | 2008-08-20 16:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 21 | AKCI08-029  | profile       | ['temp', 'salt'] |       59.2728 |       -153.239 | 2008-08-06 20:51:00 |       59.2728 |       -153.239 | 2008-08-06 20:51:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 22 | AKCI08-031  | profile       | ['temp', 'salt'] |       60.7403 |       -151.56  | 2008-08-23 15:23:00 |       60.7403 |       -151.56  | 2008-08-23 15:23:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 23 | AKCI08-032  | profile       | ['temp', 'salt'] |       60.8086 |       -151.75  | 2008-08-24 13:53:00 |       60.8086 |       -151.75  | 2008-08-24 13:53:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 24 | AKCI08-033  | profile       | ['temp', 'salt'] |       59.8117 |       -151.853 | 2008-08-29 09:45:00 |       59.8117 |       -151.853 | 2008-08-29 09:45:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 25 | AKCI08-035  | profile       | ['temp', 'salt'] |       60.8567 |       -151.631 | 2008-08-24 06:55:00 |       60.8567 |       -151.631 | 2008-08-24 06:55:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 26 | AKCI08-037A | profile       | ['temp', 'salt'] |       60.1194 |       -152.035 | 2008-08-27 20:41:00 |       60.1194 |       -152.035 | 2008-08-27 20:41:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 27 | AKCI08-037B | profile       | ['temp', 'salt'] |       60.2001 |       -152.13  | 2008-08-13 13:00:00 |       60.2001 |       -152.13  | 2008-08-13 13:00:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 28 | AKCI08-039  | profile       | ['temp', 'salt'] |       60.2001 |       -152.13  | 2008-08-24 09:35:00 |       60.2001 |       -152.13  | 2008-08-24 09:35:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 29 | AKCI08-040  | profile       | ['temp', 'salt'] |       60.8302 |       -151.696 | 2008-08-24 22:26:00 |       60.8302 |       -151.696 | 2008-08-24 22:26:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 30 | AKCI08-041  | profile       | ['temp', 'salt'] |       59.0867 |       -153     | 2008-08-05 17:15:00 |       59.0867 |       -153     | 2008-08-05 17:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 31 | AKCI08-042  | profile       | ['temp', 'salt'] |       61.1948 |       -150.164 | 2008-09-16 09:36:00 |       61.1948 |       -150.164 | 2008-09-16 09:36:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 32 | AKCI08-043  | profile       | ['temp', 'salt'] |       60.7986 |       -151.585 | 2008-08-23 18:32:00 |       60.7986 |       -151.585 | 2008-08-23 18:32:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 33 | AKCI08-044  | profile       | ['temp', 'salt'] |       60.817  |       -151.207 | 2008-08-20 18:28:00 |       60.817  |       -151.207 | 2008-08-20 18:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 34 | AKCI08-045  | profile       | ['temp', 'salt'] |       59.4423 |       -153.34  | 2008-08-07 12:25:00 |       59.4423 |       -153.34  | 2008-08-07 12:25:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 35 | AKCI08-047  | profile       | ['temp', 'salt'] |       60.8552 |       -151.395 | 2008-08-20 14:21:00 |       60.8552 |       -151.395 | 2008-08-20 14:21:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 36 | AKCI08-048  | profile       | ['temp', 'salt'] |       60.815  |       -151.749 | 2008-08-24 13:34:00 |       60.815  |       -151.749 | 2008-08-24 13:34:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 37 | AKCI08-049  | profile       | ['temp', 'salt'] |       59.9768 |       -151.894 | 2008-08-12 16:28:00 |       59.9768 |       -151.894 | 2008-08-12 16:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 38 | AKCI08-050  | profile       | ['temp', 'salt'] |       59.7616 |       -152.94  | 2008-08-09 16:57:00 |       59.7616 |       -152.94  | 2008-08-09 16:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 39 | AKCI08-051  | profile       | ['temp', 'salt'] |       60.8364 |       -151.719 | 2008-08-24 20:11:00 |       60.8364 |       -151.719 | 2008-08-24 20:11:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 40 | AKCI08-052  | profile       | ['temp', 'salt'] |       60.9262 |       -150.952 | 2008-08-23 11:13:00 |       60.9262 |       -150.952 | 2008-08-23 11:13:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 41 | AKCI08-054  | profile       | ['temp', 'salt'] |       60.9524 |       -150.926 | 2008-08-23 11:50:00 |       60.9524 |       -150.926 | 2008-08-23 11:50:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 42 | AKCI08-055  | profile       | ['temp', 'salt'] |       60.8109 |       -151.601 | 2008-08-23 19:07:00 |       60.8109 |       -151.601 | 2008-08-23 19:07:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 43 | AKCI08-056  | profile       | ['temp', 'salt'] |       61.0415 |       -151.017 | 2008-08-22 10:06:00 |       61.0415 |       -151.017 | 2008-08-22 10:06:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 44 | AKCI08-057  | profile       | ['temp', 'salt'] |       58.9358 |       -153.228 | 2008-08-06 11:56:00 |       58.9358 |       -153.228 | 2008-08-06 11:56:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 45 | AKCI08-058  | profile       | ['temp', 'salt'] |       61.1952 |       -150.818 | 2008-10-07 13:15:00 |       61.1952 |       -150.818 | 2008-10-07 13:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 46 | AKCI08-059  | profile       | ['temp', 'salt'] |       60.7365 |       -151.372 | 2008-08-25 16:15:00 |       60.7365 |       -151.372 | 2008-08-25 16:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 47 | AKCI08-060  | profile       | ['temp', 'salt'] |       60.763  |       -151.281 | 2008-08-25 20:01:00 |       60.763  |       -151.281 | 2008-08-25 20:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 48 | AKCI08-061  | profile       | ['temp', 'salt'] |       59.4014 |       -153.652 | 2008-08-08 21:57:00 |       59.4014 |       -153.652 | 2008-08-08 21:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 49 | AKCI08-063  | profile       | ['temp', 'salt'] |       60.8503 |       -151.444 | 2008-08-20 12:48:00 |       60.8503 |       -151.444 | 2008-08-20 12:48:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 50 | AKCI08-065  | profile       | ['temp', 'salt'] |       59.2405 |       -153.516 | 2008-08-08 17:25:00 |       59.2405 |       -153.516 | 2008-08-08 17:25:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 51 | AKCI08-066  | profile       | ['temp', 'salt'] |       60.6011 |       -151.883 | 2008-08-14 17:19:00 |       60.6011 |       -151.883 | 2008-08-14 17:19:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 52 | AKCI08-067  | profile       | ['temp', 'salt'] |       60.9769 |       -151.441 | 2008-08-20 09:12:00 |       60.9769 |       -151.441 | 2008-08-20 09:12:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 53 | AKCI08-069  | profile       | ['temp', 'salt'] |       60.8257 |       -151.716 | 2008-08-24 12:58:00 |       60.8257 |       -151.716 | 2008-08-24 12:58:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 54 | AKCI08-070  | profile       | ['temp', 'salt'] |       60.9609 |       -151.143 | 2008-08-19 16:39:00 |       60.9609 |       -151.143 | 2008-08-19 16:39:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 55 | AKCI08-071  | profile       | ['temp', 'salt'] |       59.318  |       -152.315 | 2008-08-05 11:15:00 |       59.318  |       -152.315 | 2008-08-05 11:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 56 | AKCI08-072  | profile       | ['temp', 'salt'] |       60.7895 |       -151.686 | 2008-08-23 17:24:00 |       60.7895 |       -151.686 | 2008-08-23 17:24:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 57 | AKCI08-073  | profile       | ['temp', 'salt'] |       60.8552 |       -151.121 | 2008-08-23 09:51:00 |       60.8552 |       -151.121 | 2008-08-23 09:51:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 58 | AKCI08-074  | profile       | ['temp', 'salt'] |       59.5334 |       -153.034 | 2008-08-07 15:06:00 |       59.5334 |       -153.034 | 2008-08-07 15:06:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 59 | AKCI08-076  | profile       | ['temp', 'salt'] |      nan      |        nan     | 2008-08-20 16:32:00 |      nan      |        nan     | 2008-08-20 16:32:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 60 | AKCI08-079  | profile       | ['temp', 'salt'] |       60.9406 |       -151.547 | 2008-08-20 10:30:00 |       60.9406 |       -151.547 | 2008-08-20 10:30:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 61 | AKCI08-080  | profile       | ['temp', 'salt'] |       60.9699 |       -150.637 | 2008-08-22 13:39:00 |       60.9699 |       -150.637 | 2008-08-22 13:39:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 62 | AKCI08-081  | profile       | ['temp', 'salt'] |       60.815  |       -151.694 | 2008-08-24 08:01:00 |       60.815  |       -151.694 | 2008-08-24 08:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 63 | AKCI08-083  | profile       | ['temp', 'salt'] |       59.6899 |       -152.383 | 2008-08-12 12:16:00 |       59.6899 |       -152.383 | 2008-08-12 12:16:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 64 | AKCI08-084  | profile       | ['temp', 'salt'] |       60.793  |       -151.72  | 2008-08-24 15:28:00 |       60.793  |       -151.72  | 2008-08-24 15:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 65 | AKCI08-086  | profile       | ['temp', 'salt'] |       59.5548 |       -152.581 | 2008-08-10 15:14:00 |       59.5548 |       -152.581 | 2008-08-10 15:14:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 66 | AKCI08-087  | profile       | ['temp', 'salt'] |       60.489  |       -151.319 | 2008-08-26 15:47:00 |       60.489  |       -151.319 | 2008-08-26 15:47:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 67 | AKCI08-088  | profile       | ['temp', 'salt'] |       60.8052 |       -151.738 | 2008-08-24 14:15:00 |       60.8052 |       -151.738 | 2008-08-24 14:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 68 | KB01        | profile       | ['temp', 'salt'] |       59.6007 |       -151.387 | 2008-08-03 13:44:00 |       59.6007 |       -151.387 | 2008-08-03 13:44:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 69 | KB02        | profile       | ['temp', 'salt'] |       59.6091 |       -151.316 | 2008-08-02 15:22:00 |       59.6091 |       -151.316 | 2008-08-02 15:22:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 70 | KB03        | profile       | ['temp', 'salt'] |       59.6425 |       -151.32  | 2008-08-03 10:14:00 |       59.6425 |       -151.32  | 2008-08-03 10:14:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 71 | KB04        | profile       | ['temp', 'salt'] |       59.6575 |       -151.236 | 2008-08-03 11:39:00 |       59.6575 |       -151.236 | 2008-08-03 11:39:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 72 | KB05        | profile       | ['temp', 'salt'] |       59.7198 |       -151.136 | 2008-08-03 13:56:00 |       59.7198 |       -151.136 | 2008-08-03 13:56:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 73 | KRM         | profile       | ['temp', 'salt'] |       60.547  |       -151.283 | 2008-08-06 14:28:00 |       60.547  |       -151.283 | 2008-08-06 14:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_emap_2008")("ctd_profiles_emap_2008")
```


### CTD Profiles (Kachemak Kuletz 2005–2007)

* Kachemak Kuletz 2005–2007
* One-off CTD profiles June-July 2005 and July 2006 and 2007
* Slug: ctd_profiles_kachemack_kuletz_2005_2007
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_kachemack_kuletz_2005_2007`

CTD Profiles in Cook Inlet

Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                 |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:--------------------------------------------------------|
|  0 |      1    | profile       | ['temp', 'salt'] |       59.7383 |       -151.095 | 2005-06-20 18:44:00 |       59.7383 |       -151.095 | 2005-06-20 18:44:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  1 |      1.1  | profile       | ['temp', 'salt'] |       59.7367 |       -151.067 | 2006-07-23 21:40:00 |       59.7367 |       -151.067 | 2006-07-23 21:40:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  2 |     10    | profile       | ['temp', 'salt'] |       59.555  |       -151.67  | 2005-06-21 15:38:00 |       59.555  |       -151.67  | 2005-06-21 15:38:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  3 |  10000    | profile       | ['temp', 'salt'] |       59.4917 |       -151.65  | 2007-07-24 21:31:00 |       59.4917 |       -151.65  | 2007-07-24 21:31:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  4 |  10001    | profile       | ['temp', 'salt'] |       59.4967 |       -151.65  | 2007-07-24 21:37:00 |       59.4967 |       -151.65  | 2007-07-24 21:37:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  5 |  10002    | profile       | ['temp', 'salt'] |       59.5083 |       -151.65  | 2007-07-24 21:46:00 |       59.5083 |       -151.65  | 2007-07-24 21:46:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  6 |  10003    | profile       | ['temp', 'salt'] |       59.525  |       -151.65  | 2007-07-24 22:01:00 |       59.525  |       -151.65  | 2007-07-24 22:01:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  7 |  10004    | profile       | ['temp', 'salt'] |       59.5417 |       -151.65  | 2007-07-24 22:14:00 |       59.5417 |       -151.65  | 2007-07-24 22:14:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  8 |  10005    | profile       | ['temp', 'salt'] |       59.5583 |       -151.65  | 2007-07-24 22:26:00 |       59.5583 |       -151.65  | 2007-07-24 22:26:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
|  9 |  10006    | profile       | ['temp', 'salt'] |       59.575  |       -151.65  | 2007-07-24 22:38:00 |       59.575  |       -151.65  | 2007-07-24 22:38:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 10 |  10007    | profile       | ['temp', 'salt'] |       59.5917 |       -151.65  | 2007-07-24 22:47:00 |       59.5917 |       -151.65  | 2007-07-24 22:47:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 11 |  10008    | profile       | ['temp', 'salt'] |       59.6083 |       -151.65  | 2007-07-24 22:56:00 |       59.6083 |       -151.65  | 2007-07-24 22:56:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 12 |  10009    | profile       | ['temp', 'salt'] |       59.625  |       -151.65  | 2007-07-24 23:08:00 |       59.625  |       -151.65  | 2007-07-24 23:08:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 13 |  10010    | profile       | ['temp', 'salt'] |       59.7317 |       -151.133 | 2007-07-25 17:42:00 |       59.7317 |       -151.133 | 2007-07-25 17:42:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 14 |  10011    | profile       | ['temp', 'salt'] |       59.7167 |       -151.133 | 2007-07-25 17:50:00 |       59.7167 |       -151.133 | 2007-07-25 17:50:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 15 |  10012    | profile       | ['temp', 'salt'] |       59.7    |       -151.133 | 2007-07-25 18:00:00 |       59.7    |       -151.133 | 2007-07-25 18:00:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 16 |  10013    | profile       | ['temp', 'salt'] |       59.6833 |       -151.133 | 2007-07-25 18:11:00 |       59.6833 |       -151.133 | 2007-07-25 18:11:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 17 |  10014    | profile       | ['temp', 'salt'] |       59.65   |       -151.2   | 2007-07-25 18:35:00 |       59.65   |       -151.2   | 2007-07-25 18:35:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 18 |  10015    | profile       | ['temp', 'salt'] |       59.6667 |       -151.2   | 2007-07-25 18:44:00 |       59.6667 |       -151.2   | 2007-07-25 18:44:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 19 |  10016    | profile       | ['temp', 'salt'] |       59.6833 |       -151.2   | 2007-07-25 18:54:00 |       59.6833 |       -151.2   | 2007-07-25 18:54:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 20 |  10017    | profile       | ['temp', 'salt'] |       59.7    |       -151.2   | 2007-07-25 19:08:00 |       59.7    |       -151.2   | 2007-07-25 19:08:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 21 |    101    | profile       | ['temp', 'salt'] |       59.7367 |       -151.067 | 2005-07-23 22:28:00 |       59.7367 |       -151.068 | 2005-07-23 22:28:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 22 |    103    | profile       | ['temp', 'salt'] |       59.7    |       -151.2   | 2005-07-23 20:57:00 |       59.7    |       -151.2   | 2005-07-23 20:57:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 23 |    104    | profile       | ['temp', 'salt'] |       59.6733 |       -151.267 | 2005-07-23 23:20:00 |       59.6733 |       -151.267 | 2005-07-23 23:20:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 24 |    105    | profile       | ['temp', 'salt'] |       59.6533 |       -151.333 | 2005-07-23 19:12:00 |       59.6533 |       -151.333 | 2005-07-23 19:12:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 25 |    107    | profile       | ['temp', 'salt'] |       59.6    |       -151.467 | 2005-07-23 01:01:00 |       59.6    |       -151.467 | 2005-07-23 01:01:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 26 |    109    | profile       | ['temp', 'salt'] |       59.6167 |       -151.6   | 2005-07-22 23:26:00 |       59.6167 |       -151.6   | 2005-07-22 23:26:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 27 |     11    | profile       | ['temp', 'salt'] |       59.535  |       -151.732 | 2005-06-16 16:47:00 |       59.535  |       -151.732 | 2005-06-16 16:47:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 28 |    111    | profile       | ['temp', 'salt'] |       59.6333 |       -151.733 | 2005-07-22 23:06:00 |       59.6333 |       -151.733 | 2005-07-22 23:06:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 29 |     12.1  | profile       | ['temp', 'salt'] |       59.6667 |       -151.8   | 2006-07-22 18:32:00 |       59.6667 |       -151.8   | 2006-07-22 18:32:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 30 |     12.2  | profile       | ['temp', 'salt'] |       59.6167 |       -151.8   | 2006-07-22 18:48:00 |       59.6167 |       -151.8   | 2006-07-22 18:48:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 31 |     12.3  | profile       | ['temp', 'salt'] |       59.5667 |       -151.8   | 2006-07-22 19:06:00 |       59.5667 |       -151.8   | 2006-07-22 19:06:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 32 |     12.4  | profile       | ['temp', 'salt'] |       59.5    |       -151.8   | 2006-07-22 19:30:00 |       59.5    |       -151.8   | 2006-07-22 19:30:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 33 |     12.5  | profile       | ['temp', 'salt'] |       59.4567 |       -151.8   | 2006-07-22 19:51:00 |       59.4567 |       -151.8   | 2006-07-22 19:51:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 34 |      2    | profile       | ['temp', 'salt'] |       59.7183 |       -151.133 | 2005-06-20 18:33:00 |       59.7183 |       -151.133 | 2005-06-20 18:33:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 35 |      2.02 | profile       | ['temp', 'salt'] |       59.7    |       -151.133 | 2006-07-23 20:19:00 |       59.7    |       -151.133 | 2006-07-23 20:19:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 36 |      2.03 | profile       | ['temp', 'salt'] |       59.7317 |       -151.133 | 2006-07-23 21:26:00 |       59.7317 |       -151.133 | 2006-07-23 21:26:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 37 |      2.2  | profile       | ['temp', 'salt'] |       59.7167 |       -151.133 | 2006-07-23 21:11:00 |       59.7167 |       -151.133 | 2006-07-23 21:11:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 38 |      2.3  | profile       | ['temp', 'salt'] |       59.6833 |       -151.133 | 2006-07-23 20:36:00 |       59.6833 |       -151.133 | 2006-07-23 20:36:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 39 |    202    | profile       | ['temp', 'salt'] |       59.7167 |       -151.133 | 2005-07-23 21:21:00 |       59.7167 |       -151.133 | 2005-07-23 21:21:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 40 |    203    | profile       | ['temp', 'salt'] |       59.65   |       -151.2   | 2005-07-23 20:07:00 |       59.65   |       -151.2   | 2005-07-23 20:07:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 41 |    204    | profile       | ['temp', 'salt'] |       59.65   |       -151.267 | 2005-07-23 19:27:00 |       59.65   |       -151.267 | 2005-07-23 19:27:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 42 |    205    | profile       | ['temp', 'salt'] |       59.6169 |       -151.333 | 2005-07-23 18:22:00 |       59.6167 |       -151.333 | 2005-07-23 18:22:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 43 |    206    | profile       | ['temp', 'salt'] |       59.6167 |       -151.4   | 2005-07-23 17:11:00 |       59.6167 |       -151.4   | 2005-07-23 17:11:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 44 |    207    | profile       | ['temp', 'salt'] |       59.5333 |       -151.467 | 2005-07-23 00:40:00 |       59.5333 |       -151.467 | 2005-07-23 00:40:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 45 |    209    | profile       | ['temp', 'salt'] |       59.5667 |       -151.6   | 2005-07-22 23:42:00 |       59.5667 |       -151.6   | 2005-07-22 23:42:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 46 |    211    | profile       | ['temp', 'salt'] |       59.5667 |       -151.733 | 2005-07-22 22:42:00 |       59.5667 |       -151.733 | 2005-07-22 22:42:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 47 |      3    | profile       | ['temp', 'salt'] |       59.6867 |       -151.2   | 2005-06-20 18:18:00 |       59.6867 |       -151.2   | 2005-06-20 18:18:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 48 |      3.01 | profile       | ['temp', 'salt'] |       59.6667 |       -151.2   | 2006-07-23 19:27:00 |       59.6667 |       -151.2   | 2006-07-23 19:27:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 49 |      3.02 | profile       | ['temp', 'salt'] |       59.6833 |       -151.2   | 2006-07-23 19:39:00 |       59.6833 |       -151.2   | 2006-07-23 19:39:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 50 |      3.1  | profile       | ['temp', 'salt'] |       59.7    |       -151.2   | 2006-07-23 20:04:00 |       59.7    |       -151.2   | 2006-07-23 20:04:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 51 |      3.2  | profile       | ['temp', 'salt'] |       59.65   |       -151.2   | 2006-07-23 23:31:00 |       59.65   |       -151.2   | 2006-07-23 23:31:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 52 |    302    | profile       | ['temp', 'salt'] |       59.6833 |       -151.133 | 2005-07-23 21:09:00 |       59.6816 |       -151.133 | 2005-07-23 21:09:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 53 |    304    | profile       | ['temp', 'salt'] |       59.6    |       -151.267 | 2005-07-23 19:46:00 |       59.6    |       -151.267 | 2005-07-23 19:46:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 54 |    305    | profile       | ['temp', 'salt'] |       59.5833 |       -151.337 | 2005-07-23 18:01:00 |       59.5833 |       -151.337 | 2005-07-23 18:01:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 55 |    306    | profile       | ['temp', 'salt'] |       59.56   |       -151.4   | 2005-07-23 17:42:00 |       59.56   |       -151.4   | 2005-07-23 17:42:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 56 |    309    | profile       | ['temp', 'salt'] |       59.5    |       -151.6   | 2005-07-23 00:03:00 |       59.5    |       -151.6   | 2005-07-23 00:03:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 57 |    311    | profile       | ['temp', 'salt'] |       59.485  |       -151.732 | 2005-07-22 22:09:00 |       59.485  |       -151.732 | 2005-07-22 22:09:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 58 |      4    | profile       | ['temp', 'salt'] |       59.6583 |       -151.267 | 2005-06-20 18:05:00 |       59.6583 |       -151.267 | 2005-06-20 18:05:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 59 |      4.1  | profile       | ['temp', 'salt'] |       59.6733 |       -151.267 | 2006-07-23 17:41:00 |       59.6733 |       -151.267 | 2006-07-23 17:41:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 60 |      5    | profile       | ['temp', 'salt'] |       59.6317 |       -151.335 | 2005-06-20 17:46:00 |       59.6317 |       -151.335 | 2005-06-20 17:46:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 61 |      6    | profile       | ['temp', 'salt'] |       59.5983 |       -151.4   | 2005-06-21 16:41:00 |       59.5983 |       -151.4   | 2005-06-21 16:41:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 62 |      7    | profile       | ['temp', 'salt'] |       59.5817 |       -151.467 | 2005-06-21 16:27:00 |       59.5817 |       -151.467 | 2005-06-21 16:27:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 63 |      8    | profile       | ['temp', 'salt'] |       59.5667 |       -151.533 | 2005-06-21 16:10:00 |       59.5667 |       -151.533 | 2005-06-21 16:10:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |
| 64 |      9    | profile       | ['temp', 'salt'] |       59.5617 |       -151.6   | 2005-06-21 15:54:00 |       59.5617 |       -151.6   | 2005-06-21 15:54:00 | https://researchworkspace.com/files/42396000/Kuletz.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_kachemack_kuletz_2005_2007")("ctd_profiles_kachemack_kuletz_2005_2007")
```


### CTD Profiles (KB small mesh 2006)

* KB small mesh 2006
* One-off CTD profiles May 2006
* Slug: ctd_profiles_kb_small_mesh_2006
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_kb_small_mesh_2006`

CTD Profiles in Cook Inlet

Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                      |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------|
|  0 |      1001 | profile       | ['temp', 'salt'] |       59.6743 |       -151.2   | 2006-05-10 19:11:00 |       59.6743 |       -151.2   | 2006-05-10 19:11:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  1 |      1002 | profile       | ['temp', 'salt'] |       59.6467 |       -151.22  | 2006-05-10 20:10:00 |       59.6467 |       -151.22  | 2006-05-10 20:10:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  2 |      1003 | profile       | ['temp', 'salt'] |       59.636  |       -151.266 | 2006-05-10 21:18:00 |       59.636  |       -151.266 | 2006-05-10 21:18:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  3 |      1004 | profile       | ['temp', 'salt'] |       59.6227 |       -151.264 | 2006-05-10 22:25:00 |       59.6227 |       -151.264 | 2006-05-10 22:25:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  4 |      1005 | profile       | ['temp', 'salt'] |       59.6058 |       -151.307 | 2006-05-10 23:31:00 |       59.6058 |       -151.307 | 2006-05-10 23:31:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  5 |      1006 | profile       | ['temp', 'salt'] |       59.5847 |       -151.529 | 2006-05-11 17:37:00 |       59.5847 |       -151.529 | 2006-05-11 17:37:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  6 |      1007 | profile       | ['temp', 'salt'] |       59.5506 |       -151.572 | 2006-05-11 18:42:00 |       59.5506 |       -151.572 | 2006-05-11 18:42:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  7 |      1008 | profile       | ['temp', 'salt'] |       59.5385 |       -151.598 | 2006-05-11 19:46:00 |       59.5385 |       -151.598 | 2006-05-11 19:46:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  8 |      1009 | profile       | ['temp', 'salt'] |       59.5338 |       -151.655 | 2006-05-11 20:54:00 |       59.5338 |       -151.655 | 2006-05-11 20:54:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  9 |      1010 | profile       | ['temp', 'salt'] |       59.522  |       -151.584 | 2006-05-11 21:55:00 |       59.522  |       -151.584 | 2006-05-11 21:55:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 10 |      1011 | profile       | ['temp', 'salt'] |       59.5112 |       -151.628 | 2006-05-11 23:02:00 |       59.5112 |       -151.628 | 2006-05-11 23:02:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 11 |      1012 | profile       | ['temp', 'salt'] |       59.5691 |       -151.471 | 2006-05-12 17:33:00 |       59.5691 |       -151.471 | 2006-05-12 17:33:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 12 |      1013 | profile       | ['temp', 'salt'] |       59.5505 |       -151.572 | 2006-05-12 18:42:00 |       59.5505 |       -151.572 | 2006-05-12 18:42:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 13 |      1014 | profile       | ['temp', 'salt'] |       59.5545 |       -151.5   | 2006-05-12 19:52:00 |       59.5545 |       -151.5   | 2006-05-12 19:52:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 14 |      1015 | profile       | ['temp', 'salt'] |       59.5557 |       -151.505 | 2006-05-12 21:29:00 |       59.5557 |       -151.505 | 2006-05-12 21:29:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 15 |      1017 | profile       | ['temp', 'salt'] |       59.6645 |       -151.233 | 2006-05-15 19:37:00 |       59.6645 |       -151.233 | 2006-05-15 19:37:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 16 |      1018 | profile       | ['temp', 'salt'] |       59.6832 |       -151.2   | 2006-05-15 20:49:00 |       59.6832 |       -151.2   | 2006-05-15 20:49:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 17 |      1019 | profile       | ['temp', 'salt'] |       59.7024 |       -151.162 | 2006-05-15 22:05:00 |       59.7024 |       -151.162 | 2006-05-15 22:05:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 18 |      1020 | profile       | ['temp', 'salt'] |       59.7227 |       -151.115 | 2006-05-15 23:31:00 |       59.7227 |       -151.115 | 2006-05-15 23:31:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 19 |      1021 | profile       | ['temp', 'salt'] |       59.6296 |       -151.282 | 2006-05-16 01:06:00 |       59.6296 |       -151.282 | 2006-05-16 01:06:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 20 |      1022 | profile       | ['temp', 'salt'] |       59.6137 |       -151.277 | 2006-05-16 02:07:00 |       59.6137 |       -151.277 | 2006-05-16 02:07:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 21 |      1023 | profile       | ['temp', 'salt'] |       59.6068 |       -151.332 | 2006-05-16 16:39:00 |       59.6068 |       -151.332 | 2006-05-16 16:39:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 22 |      1024 | profile       | ['temp', 'salt'] |       59.6115 |       -151.305 | 2006-05-16 17:31:00 |       59.6115 |       -151.305 | 2006-05-16 17:31:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 23 |      1025 | profile       | ['temp', 'salt'] |       59.6278 |       -151.302 | 2006-05-16 18:30:00 |       59.6278 |       -151.302 | 2006-05-16 18:30:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 24 |      1026 | profile       | ['temp', 'salt'] |       59.639  |       -151.297 | 2006-05-16 19:33:00 |       59.639  |       -151.297 | 2006-05-16 19:33:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 25 |      1027 | profile       | ['temp', 'salt'] |       59.5309 |       -151.565 | 2006-05-16 22:21:00 |       59.5309 |       -151.565 | 2006-05-16 22:21:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 26 |      1028 | profile       | ['temp', 'salt'] |       59.5496 |       -151.555 | 2006-05-16 23:46:00 |       59.5496 |       -151.555 | 2006-05-16 23:46:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_kb_small_mesh_2006")("ctd_profiles_kb_small_mesh_2006")
```


### CTD Profiles (Kbay OSU 2007)

* Kbay OSU 2007
* One-off CTD profiles September 2007
* Slug: ctd_profiles_kbay_osu_2007
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_kbay_osu_2007`

CTD Profiles in Cook Inlet

Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                   |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------|
|  0 |         1 | profile       | ['temp', 'salt'] |       59.3482 |       -151.973 | 2007-09-06 09:05:00 |       59.3482 |       -151.973 | 2007-09-06 09:05:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  1 |        10 | profile       | ['temp', 'salt'] |       59.3587 |       -152     | 2007-09-06 13:03:00 |       59.3587 |       -152     | 2007-09-06 13:03:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  2 |        11 | profile       | ['temp', 'salt'] |       59.358  |       -152.002 | 2007-09-06 13:52:00 |       59.358  |       -152.002 | 2007-09-06 13:52:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  3 |        12 | profile       | ['temp', 'salt'] |       59.3567 |       -152.004 | 2007-09-06 14:00:00 |       59.3567 |       -152.004 | 2007-09-06 14:00:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  4 |        13 | profile       | ['temp', 'salt'] |       59.3557 |       -152.005 | 2007-09-06 14:10:00 |       59.3557 |       -152.005 | 2007-09-06 14:10:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  5 |        14 | profile       | ['temp', 'salt'] |       59.3557 |       -152.005 | 2007-09-07 14:12:00 |       59.3557 |       -152.005 | 2007-09-07 14:12:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  6 |        15 | profile       | ['temp', 'salt'] |       59.4377 |       -151.879 | 2007-09-07 09:12:00 |       59.4377 |       -151.879 | 2007-09-07 09:12:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  7 |        16 | profile       | ['temp', 'salt'] |       59.4407 |       -151.87  | 2007-09-07 09:23:00 |       59.4407 |       -151.87  | 2007-09-07 09:23:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  8 |        17 | profile       | ['temp', 'salt'] |       59.4407 |       -151.87  | 2007-09-07 09:23:00 |       59.4407 |       -151.87  | 2007-09-07 09:23:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  9 |        18 | profile       | ['temp', 'salt'] |       59.4385 |       -151.955 | 2007-09-07 10:00:00 |       59.4385 |       -151.955 | 2007-09-07 10:00:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 10 |        19 | profile       | ['temp', 'salt'] |       59.4343 |       -151.95  | 2007-09-07 10:13:00 |       59.4343 |       -151.95  | 2007-09-07 10:13:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 11 |         2 | profile       | ['temp', 'salt'] |       59.3563 |       -151.998 | 2007-09-06 10:30:00 |       59.3563 |       -151.998 | 2007-09-06 10:30:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 12 |        20 | profile       | ['temp', 'salt'] |       59.4402 |       -151.945 | 2007-09-07 10:25:00 |       59.4402 |       -151.945 | 2007-09-07 10:25:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 13 |        21 | profile       | ['temp', 'salt'] |       59.4355 |       -151.933 | 2007-09-07 11:10:00 |       59.4355 |       -151.933 | 2007-09-07 11:10:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 14 |        22 | profile       | ['temp', 'salt'] |       59.4402 |       -151.926 | 2007-09-07 11:18:00 |       59.4402 |       -151.926 | 2007-09-07 11:18:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 15 |        23 | profile       | ['temp', 'salt'] |       59.4457 |       -151.918 | 2007-09-07 11:29:00 |       59.4457 |       -151.918 | 2007-09-07 11:29:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 16 |        24 | profile       | ['temp', 'salt'] |       59.436  |       -151.883 | 2007-09-07 12:14:00 |       59.436  |       -151.883 | 2007-09-07 12:14:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 17 |        25 | profile       | ['temp', 'salt'] |       59.4383 |       -151.883 | 2007-09-07 12:23:00 |       59.4383 |       -151.883 | 2007-09-07 12:23:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 18 |        26 | profile       | ['temp', 'salt'] |       59.4398 |       -151.883 | 2007-09-07 12:29:00 |       59.4398 |       -151.883 | 2007-09-07 12:29:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 19 |        27 | profile       | ['temp', 'salt'] |       59.4415 |       -151.881 | 2007-09-07 12:34:00 |       59.4415 |       -151.881 | 2007-09-07 12:34:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 20 |        28 | profile       | ['temp', 'salt'] |       59.4433 |       -151.879 | 2007-09-07 12:41:00 |       59.4433 |       -151.879 | 2007-09-07 12:41:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 21 |        29 | profile       | ['temp', 'salt'] |       59.4458 |       -151.875 | 2007-09-07 12:49:00 |       59.4458 |       -151.875 | 2007-09-07 12:49:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 22 |         3 | profile       | ['temp', 'salt'] |       59.3607 |       -151.993 | 2007-09-06 10:38:00 |       59.3607 |       -151.993 | 2007-09-06 10:38:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 23 |        30 | profile       | ['temp', 'salt'] |       59.4483 |       -151.869 | 2007-09-08 12:58:00 |       59.4483 |       -151.869 | 2007-09-08 12:58:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 24 |        31 | profile       | ['temp', 'salt'] |       59.4522 |       -151.85  | 2007-09-08 09:26:00 |       59.4522 |       -151.85  | 2007-09-08 09:26:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 25 |        32 | profile       | ['temp', 'salt'] |       59.4538 |       -151.846 | 2007-09-08 09:35:00 |       59.4538 |       -151.846 | 2007-09-08 09:35:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 26 |        33 | profile       | ['temp', 'salt'] |       59.4553 |       -151.841 | 2007-09-08 09:46:00 |       59.4553 |       -151.841 | 2007-09-08 09:46:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 27 |        34 | profile       | ['temp', 'salt'] |       59.441  |       -151.875 | 2007-09-08 10:08:00 |       59.441  |       -151.875 | 2007-09-08 10:08:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 28 |        35 | profile       | ['temp', 'salt'] |       59.4437 |       -151.865 | 2007-09-08 10:17:00 |       59.4437 |       -151.865 | 2007-09-08 10:17:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 29 |        36 | profile       | ['temp', 'salt'] |       59.4455 |       -151.855 | 2007-09-08 10:26:00 |       59.4455 |       -151.855 | 2007-09-08 10:26:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 30 |        37 | profile       | ['temp', 'salt'] |       59.449  |       -151.854 | 2007-09-08 11:37:00 |       59.449  |       -151.854 | 2007-09-08 11:37:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 31 |        38 | profile       | ['temp', 'salt'] |       59.4512 |       -151.845 | 2007-09-08 11:49:00 |       59.4512 |       -151.845 | 2007-09-08 11:49:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 32 |        39 | profile       | ['temp', 'salt'] |       59.4525 |       -151.839 | 2007-09-08 11:59:00 |       59.4525 |       -151.839 | 2007-09-08 11:59:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 33 |         4 | profile       | ['temp', 'salt'] |       59.3637 |       -151.992 | 2007-09-06 10:46:00 |       59.3637 |       -151.992 | 2007-09-06 10:46:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 34 |        40 | profile       | ['temp', 'salt'] |       59.4482 |       -151.875 | 2007-09-08 12:18:00 |       59.4482 |       -151.875 | 2007-09-08 12:18:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 35 |        41 | profile       | ['temp', 'salt'] |       59.4545 |       -151.86  | 2007-09-08 12:31:00 |       59.4545 |       -151.86  | 2007-09-08 12:31:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 36 |        42 | profile       | ['temp', 'salt'] |       59.4512 |       -151.849 | 2007-09-08 12:44:00 |       59.4512 |       -151.849 | 2007-09-08 12:44:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 37 |        43 | profile       | ['temp', 'salt'] |       59.4327 |       -151.891 | 2007-09-08 13:05:00 |       59.4327 |       -151.891 | 2007-09-08 13:05:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 38 |        44 | profile       | ['temp', 'salt'] |       59.4352 |       -151.891 | 2007-09-08 13:18:00 |       59.4352 |       -151.891 | 2007-09-08 13:18:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 39 |        45 | profile       | ['temp', 'salt'] |       59.4393 |       -151.889 | 2007-09-08 13:29:00 |       59.4393 |       -151.889 | 2007-09-08 13:29:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 40 |         5 | profile       | ['temp', 'salt'] |       59.3577 |       -151.999 | 2007-09-06 11:38:00 |       59.3577 |       -151.999 | 2007-09-06 11:38:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 41 |         6 | profile       | ['temp', 'salt'] |       59.3608 |       -151.995 | 2007-09-06 11:49:00 |       59.3608 |       -151.995 | 2007-09-06 11:49:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 42 |         7 | profile       | ['temp', 'salt'] |       59.3642 |       -151.994 | 2007-09-06 12:01:00 |       59.3642 |       -151.994 | 2007-09-06 12:01:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 43 |         8 | profile       | ['temp', 'salt'] |       59.3577 |       -152.001 | 2007-09-06 12:45:00 |       59.3577 |       -152.001 | 2007-09-06 12:45:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 44 |         9 | profile       | ['temp', 'salt'] |       59.3582 |       -152.001 | 2007-09-06 12:53:00 |       59.3582 |       -152.001 | 2007-09-06 12:53:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_kbay_osu_2007")("ctd_profiles_kbay_osu_2007")
```


### CTD Profiles (North Gulf small mesh 2005)

* North Gulf small mesh 2005
* One-off CTD profiles May 2005
* Slug: ctd_profiles_north_gulf_small_mesh_2005
* Included: False
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_north_gulf_small_mesh_2005`

CTD Profiles in Cook Inlet

Notes:

Outside the model domain

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                |
|---:|:----------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------|
|  0 | NWFjord   | profile       | ['temp', 'salt'] |       59.8265 |       -150.06  | 2005-05-02 20:05:00 |       59.8265 |       -150.06  | 2005-05-02 20:05:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  1 | b06       | profile       | ['temp', 'salt'] |       59.9157 |       -149.433 | 2005-04-30 17:44:00 |       59.9157 |       -149.433 | 2005-04-30 17:44:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  2 | d06       | profile       | ['temp', 'salt'] |       59.874  |       -149.456 | 2005-04-30 19:32:00 |       59.874  |       -149.456 | 2005-04-30 19:32:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  3 | f07       | profile       | ['temp', 'salt'] |       59.8483 |       -149.485 | 2005-05-01 09:29:00 |       59.8483 |       -149.485 | 2005-05-01 09:29:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  4 | h07       | profile       | ['temp', 'salt'] |       59.8158 |       -149.489 | 2005-05-01 11:19:00 |       59.8158 |       -149.489 | 2005-05-01 11:19:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  5 | i03       | profile       | ['temp', 'salt'] |       59.7988 |       -149.364 | 2005-05-01 14:33:00 |       59.7988 |       -149.364 | 2005-05-01 14:33:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  6 | i05       | profile       | ['temp', 'salt'] |       59.7833 |       -149.428 | 2005-05-01 12:59:00 |       59.7833 |       -149.428 | 2005-05-01 12:59:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  7 | i14       | profile       | ['temp', 'salt'] |       59.7875 |       -149.712 | 2005-05-01 10:02:00 |       59.7875 |       -149.712 | 2005-05-01 10:02:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  8 | j04       | profile       | ['temp', 'salt'] |       59.7738 |       -149.373 | 2005-05-01 16:08:00 |       59.7738 |       -149.373 | 2005-05-01 16:08:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
|  9 | j22       | profile       | ['temp', 'salt'] |       59.7811 |       -150.009 | 2005-05-02 19:37:00 |       59.7811 |       -150.009 | 2005-05-02 19:37:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 10 | k13       | profile       | ['temp', 'salt'] |       59.756  |       -149.667 | 2005-05-02 11:37:00 |       59.756  |       -149.667 | 2005-05-02 11:37:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 11 | m12       | profile       | ['temp', 'salt'] |       59.7227 |       -149.637 | 2005-05-02 13:03:00 |       59.7227 |       -149.637 | 2005-05-02 13:03:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 12 | o11       | profile       | ['temp', 'salt'] |       59.6855 |       -149.609 | 2005-05-01 20:16:00 |       59.6855 |       -149.609 | 2005-05-01 20:16:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 13 | p09       | profile       | ['temp', 'salt'] |       59.6661 |       -149.56  | 2005-05-01 18:26:00 |       59.6661 |       -149.56  | 2005-05-01 18:26:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 14 | p19       | profile       | ['temp', 'salt'] |       59.6812 |       -149.887 | 2005-05-02 17:00:00 |       59.6812 |       -149.887 | 2005-05-02 17:00:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 15 | r19       | profile       | ['temp', 'salt'] |       59.6522 |       -149.888 | 2005-05-02 15:33:00 |       59.6522 |       -149.888 | 2005-05-02 15:33:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 16 | t19       | profile       | ['temp', 'salt'] |       59.5962 |       -149.895 | 2005-05-03 10:04:00 |       59.5962 |       -149.895 | 2005-05-03 10:04:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 17 | v19       | profile       | ['temp', 'salt'] |       59.5653 |       -149.898 | 2005-05-03 11:11:00 |       59.5653 |       -149.898 | 2005-05-03 11:11:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 18 | x20       | profile       | ['temp', 'salt'] |       59.5513 |       -149.908 | 2005-05-03 15:14:00 |       59.5513 |       -149.908 | 2005-05-03 15:14:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 19 | z17       | profile       | ['temp', 'salt'] |       59.496  |       -149.82  | 2005-05-03 12:43:00 |       59.496  |       -149.82  | 2005-05-03 12:43:00 | https://researchworkspace.com/files/42200015/NGASS.csv |
| 20 | z19       | profile       | ['temp', 'salt'] |       59.5251 |       -149.896 | 2005-05-03 14:06:00 |       59.5251 |       -149.896 | 2005-05-03 14:06:00 | https://researchworkspace.com/files/42200015/NGASS.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_north_gulf_small_mesh_2005")("ctd_profiles_north_gulf_small_mesh_2005")
```


### CTD Profiles (Piatt Speckman)

* Piatt Speckman 1995-99
* One-off CTD profiles April to September 1999
* Slug: ctd_profiles_piatt_speckman_1999
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_piatt_speckman_1999`

CTD Profiles in Cook Inlet

Notes:



````{div} full-width
```{dropdown} Dataset metadata

|     | Dataset   | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                    |
|----:|:----------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------|
|   0 | 10159900  | profile       | ['temp', 'salt'] |       59.6413 |       -151.36  | 1999-08-26 17:51:00 |       59.6413 |       -151.36  | 1999-08-26 17:51:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   1 | 10159901  | profile       | ['temp', 'salt'] |       59.6205 |       -151.351 | 1999-08-26 18:01:00 |       59.6205 |       -151.351 | 1999-08-26 18:01:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   2 | 10159902  | profile       | ['temp', 'salt'] |       59.5952 |       -151.349 | 1999-08-26 18:12:00 |       59.5952 |       -151.349 | 1999-08-26 18:12:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   3 | 10159903  | profile       | ['temp', 'salt'] |       59.5807 |       -151.341 | 1999-08-26 18:33:00 |       59.5807 |       -151.341 | 1999-08-26 18:33:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   4 | 10159904  | profile       | ['temp', 'salt'] |       59.5712 |       -151.336 | 1999-08-26 18:41:00 |       59.5712 |       -151.336 | 1999-08-26 18:41:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   5 | 10159905  | profile       | ['temp', 'salt'] |       59.6217 |       -151.626 | 1999-08-26 19:16:00 |       59.6217 |       -151.626 | 1999-08-26 19:16:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   6 | 10159907  | profile       | ['temp', 'salt'] |       59.5733 |       -151.599 | 1999-08-26 19:28:00 |       59.5733 |       -151.599 | 1999-08-26 19:28:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   7 | 10159908  | profile       | ['temp', 'salt'] |       59.5532 |       -151.589 | 1999-08-26 19:38:00 |       59.5532 |       -151.589 | 1999-08-26 19:38:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   8 | 10159909  | profile       | ['temp', 'salt'] |       59.519  |       -151.581 | 1999-08-26 19:54:00 |       59.519  |       -151.581 | 1999-08-26 19:54:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|   9 | 10159910  | profile       | ['temp', 'salt'] |       59.4895 |       -151.582 | 1999-08-26 20:04:00 |       59.4895 |       -151.582 | 1999-08-26 20:04:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  10 | 10159911  | profile       | ['temp', 'salt'] |       59.4853 |       -151.577 | 1999-08-28 12:16:00 |       59.4853 |       -151.577 | 1999-08-28 12:16:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  11 | 10159913  | profile       | ['temp', 'salt'] |       59.6202 |       -151.349 | 1999-08-30 11:47:00 |       59.6202 |       -151.349 | 1999-08-30 11:47:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  12 | 10159914  | profile       | ['temp', 'salt'] |       59.5132 |       -151.476 | 1999-08-30 12:43:00 |       59.5132 |       -151.476 | 1999-08-30 12:43:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  13 | 10159915  | profile       | ['temp', 'salt'] |       59.62   |       -151.351 | 1999-09-13 15:20:00 |       59.62   |       -151.351 | 1999-09-13 15:20:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  14 | 10159916  | profile       | ['temp', 'salt'] |       59.5135 |       -151.478 | 1999-09-13 16:17:00 |       59.5135 |       -151.478 | 1999-09-13 16:17:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  15 | 9051600   | profile       | ['temp', 'salt'] |       59.5122 |       -151.48  | 1999-04-26 15:30:00 |       59.5122 |       -151.48  | 1999-04-26 15:30:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  16 | 9051601   | profile       | ['temp', 'salt'] |       59.6188 |       -151.351 | 1999-04-26 17:00:00 |       59.6188 |       -151.351 | 1999-04-26 17:00:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  17 | 9051602   | profile       | ['temp', 'salt'] |       59.6233 |       -151.626 | 1999-04-27 09:45:00 |       59.6233 |       -151.626 | 1999-04-27 09:45:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  18 | 9051603   | profile       | ['temp', 'salt'] |       59.5818 |       -151.602 | 1999-04-27 10:00:00 |       59.5818 |       -151.602 | 1999-04-27 10:00:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  19 | 9051604   | profile       | ['temp', 'salt'] |       59.5535 |       -151.591 | 1999-04-27 10:10:00 |       59.5535 |       -151.591 | 1999-04-27 10:10:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  20 | 9051605   | profile       | ['temp', 'salt'] |       59.5192 |       -151.583 | 1999-04-27 10:28:00 |       59.5192 |       -151.583 | 1999-04-27 10:28:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  21 | 9051606   | profile       | ['temp', 'salt'] |       59.4895 |       -151.581 | 1999-04-27 10:43:00 |       59.4895 |       -151.581 | 1999-04-27 10:43:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  22 | 9051607   | profile       | ['temp', 'salt'] |       59.4857 |       -151.576 | 1999-04-27 10:50:00 |       59.4857 |       -151.576 | 1999-04-27 10:50:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  23 | 9051608   | profile       | ['temp', 'salt'] |       59.5717 |       -151.336 | 1999-04-27 11:30:00 |       59.5717 |       -151.336 | 1999-04-27 11:30:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  24 | 9051609   | profile       | ['temp', 'salt'] |       59.58   |       -151.34  | 1999-04-27 11:35:00 |       59.58   |       -151.34  | 1999-04-27 11:35:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  25 | 9051610   | profile       | ['temp', 'salt'] |       59.595  |       -151.351 | 1999-04-27 11:45:00 |       59.595  |       -151.351 | 1999-04-27 11:45:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  26 | 9051611   | profile       | ['temp', 'salt'] |       59.62   |       -151.351 | 1999-04-27 12:05:00 |       59.62   |       -151.351 | 1999-04-27 12:05:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  27 | 9051612   | profile       | ['temp', 'salt'] |       59.5753 |       -151.361 | 1999-04-27 12:16:00 |       59.5753 |       -151.361 | 1999-04-27 12:16:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  28 | 9051613   | profile       | ['temp', 'salt'] |       59.62   |       -151.351 | 1999-05-05 16:50:00 |       59.62   |       -151.351 | 1999-05-05 16:50:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  29 | 9051614   | profile       | ['temp', 'salt'] |       59.6197 |       -151.35  | 1999-05-05 18:44:00 |       59.6197 |       -151.35  | 1999-05-05 18:44:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  30 | 9051615   | profile       | ['temp', 'salt'] |       59.5132 |       -151.477 | 1999-05-11 10:08:00 |       59.5132 |       -151.477 | 1999-05-11 10:08:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  31 | 9051616   | profile       | ['temp', 'salt'] |       59.6197 |       -151.35  | 1999-05-11 12:30:00 |       59.6197 |       -151.35  | 1999-05-11 12:30:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  32 | 9060400   | profile       | ['temp', 'salt'] |       59.5122 |       -151.48  | 1999-05-23 16:40:00 |       59.5122 |       -151.48  | 1999-05-23 16:40:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  33 | 9060401   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-05-23 18:09:00 |       59.6203 |       -151.351 | 1999-05-23 18:09:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  34 | 9060402   | profile       | ['temp', 'salt'] |       59.5122 |       -151.48  | 1999-05-28 17:20:00 |       59.5122 |       -151.48  | 1999-05-28 17:20:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  35 | 9060403   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-05-28 19:13:00 |       59.6203 |       -151.351 | 1999-05-28 19:13:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  36 | 9060404   | profile       | ['temp', 'salt'] |       59.622  |       -151.627 | 1999-06-01 16:46:00 |       59.622  |       -151.627 | 1999-06-01 16:46:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  37 | 9060405   | profile       | ['temp', 'salt'] |       59.5818 |       -151.602 | 1999-06-01 17:02:00 |       59.5818 |       -151.602 | 1999-06-01 17:02:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  38 | 9060406   | profile       | ['temp', 'salt'] |       59.5535 |       -151.591 | 1999-06-01 17:19:00 |       59.5535 |       -151.591 | 1999-06-01 17:19:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  39 | 9060407   | profile       | ['temp', 'salt'] |       59.5192 |       -151.583 | 1999-06-01 17:36:00 |       59.5192 |       -151.583 | 1999-06-01 17:36:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  40 | 9060408   | profile       | ['temp', 'salt'] |       59.4895 |       -151.582 | 1999-06-01 17:51:00 |       59.4895 |       -151.582 | 1999-06-01 17:51:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  41 | 9060409   | profile       | ['temp', 'salt'] |       59.4853 |       -151.577 | 1999-06-01 17:59:00 |       59.4853 |       -151.577 | 1999-06-01 17:59:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  42 | 9060410   | profile       | ['temp', 'salt'] |       59.5713 |       -151.336 | 1999-06-01 18:44:00 |       59.5713 |       -151.336 | 1999-06-01 18:44:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  43 | 9060411   | profile       | ['temp', 'salt'] |       59.5807 |       -151.341 | 1999-06-01 18:50:00 |       59.5807 |       -151.341 | 1999-06-01 18:50:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  44 | 9060412   | profile       | ['temp', 'salt'] |       59.595  |       -151.351 | 1999-06-01 19:00:00 |       59.595  |       -151.351 | 1999-06-01 19:00:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  45 | 9060413   | profile       | ['temp', 'salt'] |       59.6205 |       -151.352 | 1999-06-01 19:17:00 |       59.6205 |       -151.352 | 1999-06-01 19:17:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  46 | 9060414   | profile       | ['temp', 'salt'] |       59.5753 |       -151.361 | 1999-06-01 19:29:00 |       59.5753 |       -151.361 | 1999-06-01 19:29:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  47 | 9060415   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-06-05 09:00:00 |       59.5132 |       -151.476 | 1999-06-04 12:06:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  48 | 9063000   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-06-29 13:04:00 |       59.6203 |       -151.351 | 1999-06-29 13:04:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  49 | 9063001   | profile       | ['temp', 'salt'] |       59.5127 |       -151.477 | 1999-06-29 14:45:00 |       59.5127 |       -151.477 | 1999-06-29 14:45:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  50 | 9063002   | profile       | ['temp', 'salt'] |       59.6088 |       -153.165 | 1999-06-30 12:52:00 |       59.6088 |       -153.165 | 1999-06-30 12:52:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  51 | 9063003   | profile       | ['temp', 'salt'] |       59.6102 |       -153.046 | 1999-06-30 13:24:00 |       59.6102 |       -153.046 | 1999-06-30 13:24:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  52 | 9063004   | profile       | ['temp', 'salt'] |       59.6083 |       -152.928 | 1999-06-30 13:45:00 |       59.6083 |       -152.928 | 1999-06-30 13:45:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  53 | 9063005   | profile       | ['temp', 'salt'] |       59.6088 |       -152.808 | 1999-06-30 14:12:00 |       59.6088 |       -152.808 | 1999-06-30 14:12:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  54 | 9063006   | profile       | ['temp', 'salt'] |       59.6098 |       -152.689 | 1999-06-30 14:43:00 |       59.6098 |       -152.689 | 1999-06-30 14:43:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  55 | 9063007   | profile       | ['temp', 'salt'] |       59.6098 |       -152.572 | 1999-06-30 15:25:00 |       59.6098 |       -152.572 | 1999-06-30 15:25:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  56 | 9063008   | profile       | ['temp', 'salt'] |       59.6117 |       -152.45  | 1999-06-30 16:01:00 |       59.6117 |       -152.45  | 1999-06-30 16:01:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  57 | 9063009   | profile       | ['temp', 'salt'] |       59.609  |       -152.332 | 1999-06-30 16:29:00 |       59.609  |       -152.332 | 1999-06-30 16:29:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  58 | 9063010   | profile       | ['temp', 'salt'] |       59.613  |       -152.213 | 1999-06-30 17:00:00 |       59.613  |       -152.213 | 1999-06-30 17:00:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  59 | 9063011   | profile       | ['temp', 'salt'] |       59.6093 |       -152.094 | 1999-06-30 17:26:00 |       59.6093 |       -152.094 | 1999-06-30 17:26:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  60 | 9063012   | profile       | ['temp', 'salt'] |       59.6082 |       -151.973 | 1999-06-30 17:52:00 |       59.6082 |       -151.973 | 1999-06-30 17:52:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  61 | 9063013   | profile       | ['temp', 'salt'] |       59.608  |       -151.856 | 1999-06-30 18:19:00 |       59.608  |       -151.856 | 1999-06-30 18:19:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  62 | 9063014   | profile       | ['temp', 'salt'] |       59.6077 |       -151.82  | 1999-06-30 18:43:00 |       59.6077 |       -151.82  | 1999-06-30 18:43:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  63 | 9063015   | profile       | ['temp', 'salt'] |       59.6158 |       -151.616 | 1999-06-30 19:07:00 |       59.6158 |       -151.616 | 1999-06-30 19:07:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  64 | 9072201   | profile       | ['temp', 'salt'] |       59.4888 |       -151.58  | 1999-07-14 13:20:00 |       59.4888 |       -151.58  | 1999-07-14 13:20:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  65 | 9072202   | profile       | ['temp', 'salt'] |       59.5181 |       -151.581 | 1999-07-14 13:36:00 |       59.5181 |       -151.581 | 1999-07-14 13:36:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  66 | 9072203   | profile       | ['temp', 'salt'] |       59.5538 |       -151.591 | 1999-07-14 13:50:00 |       59.5538 |       -151.591 | 1999-07-14 13:50:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  67 | 9072204   | profile       | ['temp', 'salt'] |       59.5818 |       -151.599 | 1999-07-14 14:04:00 |       59.5818 |       -151.599 | 1999-07-14 14:04:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  68 | 9072205   | profile       | ['temp', 'salt'] |       59.622  |       -151.627 | 1999-07-14 14:18:00 |       59.622  |       -151.627 | 1999-07-14 14:18:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  69 | 9072206   | profile       | ['temp', 'salt'] |       59.5713 |       -151.336 | 1999-07-14 14:52:00 |       59.5713 |       -151.336 | 1999-07-14 14:52:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  70 | 9072207   | profile       | ['temp', 'salt'] |       59.58   |       -151.339 | 1999-07-14 14:58:00 |       59.58   |       -151.339 | 1999-07-14 14:58:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  71 | 9072208   | profile       | ['temp', 'salt'] |       59.595  |       -151.35  | 1999-07-14 15:07:00 |       59.595  |       -151.35  | 1999-07-14 15:07:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  72 | 9072209   | profile       | ['temp', 'salt'] |       59.6205 |       -151.352 | 1999-07-14 15:23:00 |       59.6205 |       -151.352 | 1999-07-14 15:23:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  73 | 9072210   | profile       | ['temp', 'salt'] |       59.6425 |       -151.361 | 1999-07-14 15:34:00 |       59.6425 |       -151.361 | 1999-07-14 15:34:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  74 | 9072211   | profile       | ['temp', 'salt'] |       59.6198 |       -151.35  | 1999-07-17 13:27:00 |       59.6198 |       -151.35  | 1999-07-17 13:27:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  75 | 9072212   | profile       | ['temp', 'salt'] |       59.5123 |       -151.478 | 1999-07-17 14:57:00 |       59.5123 |       -151.478 | 1999-07-17 14:57:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  76 | 9072213   | profile       | ['temp', 'salt'] |       59.62   |       -151.35  | 1999-07-17 11:17:00 |       59.62   |       -151.35  | 1999-07-17 11:17:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  77 | 9072214   | profile       | ['temp', 'salt'] |       59.5125 |       -151.479 | 1999-07-17 12:47:00 |       59.5125 |       -151.479 | 1999-07-17 12:47:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  78 | 90729a00  | profile       | ['temp', 'salt'] |       59.5    |       -151.972 | 1999-07-25 14:12:00 |       59.5    |       -151.972 | 1999-07-25 14:12:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  79 | 90729a01  | profile       | ['temp', 'salt'] |       59.3448 |       -152.252 | 1999-07-26 14:05:00 |       59.3448 |       -152.252 | 1999-07-26 14:05:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  80 | 90729a02  | profile       | ['temp', 'salt'] |       59.2543 |       -152.318 | 1999-07-26 16:29:00 |       59.2543 |       -152.318 | 1999-07-26 16:29:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  81 | 90729a03  | profile       | ['temp', 'salt'] |       59.2374 |       -151.966 | 1999-07-26 17:59:00 |       59.2374 |       -151.966 | 1999-07-26 17:59:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  82 | 90729a04  | profile       | ['temp', 'salt'] |       59.187  |       -151.969 | 1999-07-26 18:26:00 |       59.187  |       -151.969 | 1999-07-26 18:26:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  83 | 90729a05  | profile       | ['temp', 'salt'] |       59.1303 |       -151.968 | 1999-07-26 18:58:00 |       59.1303 |       -151.968 | 1999-07-26 18:58:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  84 | 90729a06  | profile       | ['temp', 'salt'] |       59.0628 |       -151.963 | 1999-07-26 19:42:00 |       59.0628 |       -151.963 | 1999-07-26 19:42:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  85 | 90729a07  | profile       | ['temp', 'salt'] |       58.9967 |       -151.961 | 1999-07-26 20:20:00 |       58.9967 |       -151.961 | 1999-07-26 20:20:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  86 | 90729a08  | profile       | ['temp', 'salt'] |       58.934  |       -151.958 | 1999-07-26 20:54:00 |       58.934  |       -151.958 | 1999-07-26 20:54:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  87 | 90729a09  | profile       | ['temp', 'salt'] |       59.185  |       -151.496 | 1999-07-27 15:39:00 |       59.185  |       -151.496 | 1999-07-27 15:39:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  88 | 90729a10  | profile       | ['temp', 'salt'] |       59.1122 |       -151.608 | 1999-07-27 18:20:00 |       59.1122 |       -151.608 | 1999-07-27 18:20:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  89 | 90729a11  | profile       | ['temp', 'salt'] |       59.1364 |       -151.719 | 1999-07-28 16:14:00 |       59.1364 |       -151.719 | 1999-07-28 16:14:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  90 | 90729a12  | profile       | ['temp', 'salt'] |       59.1385 |       -151.639 | 1999-07-28 17:42:00 |       59.1385 |       -151.639 | 1999-07-28 17:42:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  91 | 90729a13  | profile       | ['temp', 'salt'] |       59.1541 |       -151.569 | 1999-07-28 19:36:00 |       59.1541 |       -151.569 | 1999-07-28 19:36:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  92 | 90729a14  | profile       | ['temp', 'salt'] |       58.9131 |       -151.742 | 1999-07-29 09:06:00 |       58.9131 |       -151.742 | 1999-07-29 09:06:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  93 | 9082101   | profile       | ['temp', 'salt'] |       59.6205 |       -151.35  | 1999-08-16 17:38:00 |       59.6205 |       -151.35  | 1999-08-16 17:38:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  94 | 9082102   | profile       | ['temp', 'salt'] |       59.4685 |       -151.745 | 1999-08-17 10:42:00 |       59.4685 |       -151.745 | 1999-08-17 10:42:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  95 | 9082103   | profile       | ['temp', 'salt'] |       59.4532 |       -151.726 | 1999-08-17 12:03:00 |       59.4532 |       -151.726 | 1999-08-17 12:03:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  96 | 9082104   | profile       | ['temp', 'salt'] |       59.4551 |       -151.754 | 1999-08-17 12:30:00 |       59.4551 |       -151.754 | 1999-08-17 12:30:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  97 | 9082106   | profile       | ['temp', 'salt'] |       59.475  |       -151.781 | 1999-08-17 13:30:00 |       59.475  |       -151.781 | 1999-08-17 13:30:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  98 | 9082107   | profile       | ['temp', 'salt'] |       59.554  |       -151.396 | 1999-08-17 14:56:00 |       59.554  |       -151.396 | 1999-08-17 14:56:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
|  99 | 9082108   | profile       | ['temp', 'salt'] |       59.5595 |       -151.378 | 1999-08-17 15:18:00 |       59.5595 |       -151.378 | 1999-08-17 15:18:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 100 | 9082109   | profile       | ['temp', 'salt'] |       59.5554 |       -151.404 | 1999-08-17 15:55:00 |       59.5554 |       -151.404 | 1999-08-17 15:55:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 101 | 9082110   | profile       | ['temp', 'salt'] |       59.5617 |       -151.38  | 1999-08-17 16:34:00 |       59.5617 |       -151.38  | 1999-08-17 16:34:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 102 | 9082111   | profile       | ['temp', 'salt'] |       59.618  |       -151.196 | 1999-08-20 10:59:00 |       59.618  |       -151.196 | 1999-08-20 10:59:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 103 | 9082112   | profile       | ['temp', 'salt'] |       59.6083 |       -151.194 | 1999-08-20 11:11:00 |       59.6083 |       -151.194 | 1999-08-20 11:11:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 104 | 9082113   | profile       | ['temp', 'salt'] |       59.5804 |       -151.33  | 1999-08-20 12:43:00 |       59.5804 |       -151.33  | 1999-08-20 12:43:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 105 | 9082114   | profile       | ['temp', 'salt'] |       59.5798 |       -151.313 | 1999-08-20 12:52:00 |       59.5798 |       -151.313 | 1999-08-20 12:52:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 106 | 9082115   | profile       | ['temp', 'salt'] |       59.5781 |       -151.294 | 1999-08-20 13:32:00 |       59.5781 |       -151.294 | 1999-08-20 13:32:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 107 | 9082116   | profile       | ['temp', 'salt'] |       59.5235 |       -151.447 | 1999-08-20 15:20:00 |       59.5235 |       -151.447 | 1999-08-20 15:20:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 108 | 9082117   | profile       | ['temp', 'salt'] |       59.4778 |       -151.492 | 1999-08-20 15:37:00 |       59.4778 |       -151.492 | 1999-08-20 15:37:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 109 | 9082118   | profile       | ['temp', 'salt'] |       59.4839 |       -151.583 | 1999-08-21 09:28:00 |       59.4839 |       -151.583 | 1999-08-21 09:28:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 110 | 9082119   | profile       | ['temp', 'salt'] |       59.4903 |       -151.608 | 1999-08-21 10:36:00 |       59.4903 |       -151.608 | 1999-08-21 10:36:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 111 | 9082120   | profile       | ['temp', 'salt'] |       59.4929 |       -151.609 | 1999-08-21 11:36:00 |       59.4929 |       -151.609 | 1999-08-21 11:36:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 112 | 9082121   | profile       | ['temp', 'salt'] |       59.4977 |       -151.633 | 1999-08-21 12:38:00 |       59.4977 |       -151.633 | 1999-08-21 12:38:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 113 | 9082122   | profile       | ['temp', 'salt'] |       59.4886 |       -151.638 | 1999-08-21 13:40:00 |       59.4886 |       -151.638 | 1999-08-21 13:40:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |
| 114 | 9082123   | profile       | ['temp', 'salt'] |       59.5032 |       -151.631 | 1999-08-21 14:41:00 |       59.5032 |       -151.631 | 1999-08-21 14:41:00 | https://researchworkspace.com/files/42202163/Piatt1999.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_piatt_speckman_1999")("ctd_profiles_piatt_speckman_1999")
```


### CTD Profiles (USGS BOEM): across Cook Inlet

* CTD profiles - USGS BOEM
* One-off CTD profiles from 2016 to 2021 in July
* Slug: ctd_profiles_usgs_boem
* Included: True
* Feature type: profile
* See the full dataset page for more information: {ref}`page:ctd_profiles_usgs_boem`

USGS Cook Inlet fish and bird survey CTD profiles.
    
CTD profiles collected in Cook Inlet from 2016-2021 by Mayumi Arimitsu as part of BOEM sponsored research on fish and bird distributions in Cook Inlet. The profiles are collected in July for the years 2016-2021.

The scientific project is described here: https://www.usgs.gov/centers/alaska-science-center/science/cook-inlet-seabird-and-forage-fish-study#overview.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    |    Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                 |
|---:|-----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------------------------|
|  0 | 2016102001 | profile       | ['temp', 'salt'] |       60.2743 |       -152.356 | 2016-01-01 00:00:00 |       60.2743 |       -152.356 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  1 | 2016106001 | profile       | ['temp', 'salt'] |       59.8774 |       -152.579 | 2016-01-01 00:00:00 |       59.8774 |       -152.579 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  2 | 2016120001 | profile       | ['temp', 'salt'] |       60.3062 |       -152.192 | 2016-01-01 00:00:00 |       60.3062 |       -152.192 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  3 | 2016122201 | profile       | ['temp', 'salt'] |       60.1779 |       -151.915 | 2016-01-01 00:00:00 |       60.1779 |       -151.915 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  4 | 2016123001 | profile       | ['temp', 'salt'] |       60.057  |       -152.524 | 2016-01-01 00:00:00 |       60.057  |       -152.524 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  5 | 2016123002 | profile       | ['temp', 'salt'] |       60.1052 |       -152.241 | 2016-01-01 00:00:00 |       60.1052 |       -152.241 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  6 | 2016125001 | profile       | ['temp', 'salt'] |       59.9135 |       -152.194 | 2016-01-01 00:00:00 |       59.9135 |       -152.194 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  7 | 2016126001 | profile       | ['temp', 'salt'] |       59.8026 |       -152.757 | 2016-01-01 00:00:00 |       59.8026 |       -152.757 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  8 | 2016126002 | profile       | ['temp', 'salt'] |       59.8295 |       -152.538 | 2016-01-01 00:00:00 |       59.8295 |       -152.538 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
|  9 | 2016205701 | profile       | ['temp', 'salt'] |       59.6646 |       -151.233 | 2016-01-01 00:00:00 |       59.6646 |       -151.233 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 10 | 2016206001 | profile       | ['temp', 'salt'] |       59.5644 |       -151.393 | 2016-01-01 00:00:00 |       59.5644 |       -151.393 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 11 | 2016221001 | profile       | ['temp', 'salt'] |       59.6698 |       -151.985 | 2016-01-01 00:00:00 |       59.6698 |       -151.985 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 12 | 2016223001 | profile       | ['temp', 'salt'] |       59.5834 |       -151.446 | 2016-01-01 00:00:00 |       59.5834 |       -151.446 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 13 | 2016223002 | profile       | ['temp', 'salt'] |       59.5713 |       -151.716 | 2016-01-01 00:00:00 |       59.5713 |       -151.716 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 14 | 2016224001 | profile       | ['temp', 'salt'] |       59.5006 |       -151.889 | 2016-01-01 00:00:00 |       59.5006 |       -151.889 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 15 | 2016225001 | profile       | ['temp', 'salt'] |       59.4217 |       -152.025 | 2016-01-01 00:00:00 |       59.4217 |       -152.025 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 16 | 2016226001 | profile       | ['temp', 'salt'] |       59.3211 |       -152.102 | 2016-01-01 00:00:00 |       59.3211 |       -152.102 | 2016-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 17 | 2017101001 | profile       | ['temp', 'salt'] |       60.358  |       -152.214 | 2017-01-01 00:00:00 |       60.358  |       -152.214 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 18 | 2017103001 | profile       | ['temp', 'salt'] |       60.1284 |       -152.493 | 2017-01-01 00:00:00 |       60.1284 |       -152.493 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 19 | 2017120001 | profile       | ['temp', 'salt'] |       60.3292 |       -152.177 | 2017-01-01 00:00:00 |       60.3292 |       -152.177 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 20 | 2017122001 | profile       | ['temp', 'salt'] |       60.231  |       -152.285 | 2017-01-01 00:00:00 |       60.231  |       -152.285 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 21 | 2017123001 | profile       | ['temp', 'salt'] |       60.0473 |       -152.52  | 2017-01-01 00:00:00 |       60.0473 |       -152.52  | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 22 | 2017124001 | profile       | ['temp', 'salt'] |       59.9828 |       -152.263 | 2017-01-01 00:00:00 |       59.9828 |       -152.263 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 23 | 2017125001 | profile       | ['temp', 'salt'] |       59.919  |       -152.27  | 2017-01-01 00:00:00 |       59.919  |       -152.27  | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 24 | 2017125002 | profile       | ['temp', 'salt'] |       59.9439 |       -151.941 | 2017-01-01 00:00:00 |       59.9439 |       -151.941 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 25 | 2017201001 | profile       | ['temp', 'salt'] |       59.6637 |       -151.801 | 2017-01-01 00:00:00 |       59.6637 |       -151.801 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 26 | 2017204001 | profile       | ['temp', 'salt'] |       59.6447 |       -151.282 | 2017-01-01 00:00:00 |       59.6447 |       -151.282 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 27 | 2017205001 | profile       | ['temp', 'salt'] |       59.6727 |       -151.197 | 2017-01-01 00:00:00 |       59.6727 |       -151.197 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 28 | 2017206001 | profile       | ['temp', 'salt'] |       59.6599 |       -151.224 | 2017-01-01 00:00:00 |       59.6599 |       -151.224 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 29 | 2017207001 | profile       | ['temp', 'salt'] |       59.5196 |       -151.462 | 2017-01-01 00:00:00 |       59.5196 |       -151.462 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 30 | 2017212001 | profile       | ['temp', 'salt'] |       59.3781 |       -151.891 | 2017-01-01 00:00:00 |       59.3781 |       -151.891 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 31 | 2017214001 | profile       | ['temp', 'salt'] |       59.5773 |       -151.363 | 2017-01-01 00:00:00 |       59.5773 |       -151.363 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 32 | 2017220001 | profile       | ['temp', 'salt'] |       59.7454 |       -151.998 | 2017-01-01 00:00:00 |       59.7454 |       -151.998 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 33 | 2017223001 | profile       | ['temp', 'salt'] |       59.5842 |       -151.512 | 2017-01-01 00:00:00 |       59.5842 |       -151.512 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 34 | 2017224001 | profile       | ['temp', 'salt'] |       59.4971 |       -151.843 | 2017-01-01 00:00:00 |       59.4971 |       -151.843 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 35 | 2017225001 | profile       | ['temp', 'salt'] |       59.3998 |       -152.119 | 2017-01-01 00:00:00 |       59.3998 |       -152.119 | 2017-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 36 | 2018104001 | profile       | ['temp', 'salt'] |       60.0669 |       -152.537 | 2018-01-01 00:00:00 |       60.0669 |       -152.537 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 37 | 2018120001 | profile       | ['temp', 'salt'] |       60.2993 |       -152.223 | 2018-01-01 00:00:00 |       60.2993 |       -152.223 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 38 | 2018121001 | profile       | ['temp', 'salt'] |       60.2658 |       -152.178 | 2018-01-01 00:00:00 |       60.2658 |       -152.178 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 39 | 2018122001 | profile       | ['temp', 'salt'] |       60.166  |       -152.476 | 2018-01-01 00:00:00 |       60.166  |       -152.476 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 40 | 2018123001 | profile       | ['temp', 'salt'] |       60.0947 |       -151.961 | 2018-01-01 00:00:00 |       60.0947 |       -151.961 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 41 | 2018124001 | profile       | ['temp', 'salt'] |       59.9949 |       -152.297 | 2018-01-01 00:00:00 |       59.9949 |       -152.297 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 42 | 2018125001 | profile       | ['temp', 'salt'] |       59.8945 |       -151.986 | 2018-01-01 00:00:00 |       59.8945 |       -151.986 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 43 | 2018126001 | profile       | ['temp', 'salt'] |       59.8347 |       -152.416 | 2018-01-01 00:00:00 |       59.8347 |       -152.416 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 44 | 2018203001 | profile       | ['temp', 'salt'] |       59.5806 |       -151.52  | 2018-01-01 00:00:00 |       59.5806 |       -151.52  | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 45 | 2018203002 | profile       | ['temp', 'salt'] |       59.5905 |       -151.423 | 2018-01-01 00:00:00 |       59.5905 |       -151.423 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 46 | 2018205001 | profile       | ['temp', 'salt'] |       59.6932 |       -151.157 | 2018-01-01 00:00:00 |       59.6932 |       -151.157 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 47 | 2018208001 | profile       | ['temp', 'salt'] |       59.5375 |       -151.518 | 2018-01-01 00:00:00 |       59.5375 |       -151.518 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 48 | 2018214002 | profile       | ['temp', 'salt'] |       59.5746 |       -151.339 | 2018-01-01 00:00:00 |       59.5746 |       -151.339 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 49 | 2018221001 | profile       | ['temp', 'salt'] |       59.6566 |       -151.881 | 2018-01-01 00:00:00 |       59.6566 |       -151.881 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 50 | 2018223001 | profile       | ['temp', 'salt'] |       59.5818 |       -151.473 | 2018-01-01 00:00:00 |       59.5818 |       -151.473 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 51 | 2018223002 | profile       | ['temp', 'salt'] |       59.5737 |       -151.73  | 2018-01-01 00:00:00 |       59.5737 |       -151.73  | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 52 | 2018225001 | profile       | ['temp', 'salt'] |       59.4071 |       -152.014 | 2018-01-01 00:00:00 |       59.4071 |       -152.014 | 2018-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 53 | 2019106001 | profile       | ['temp', 'salt'] |       59.8465 |       -152.807 | 2019-01-01 00:00:00 |       59.8465 |       -152.807 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 54 | 2019121001 | profile       | ['temp', 'salt'] |       60.1817 |       -152.209 | 2019-01-01 00:00:00 |       60.1817 |       -152.209 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 55 | 2019122001 | profile       | ['temp', 'salt'] |       60.1561 |       -152.379 | 2019-01-01 00:00:00 |       60.1561 |       -152.379 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 56 | 2019123001 | profile       | ['temp', 'salt'] |       60.0269 |       -151.982 | 2019-01-01 00:00:00 |       60.0269 |       -151.982 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 57 | 2019125001 | profile       | ['temp', 'salt'] |       59.928  |       -152.179 | 2019-01-01 00:00:00 |       59.928  |       -152.179 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 58 | 2019126001 | profile       | ['temp', 'salt'] |       59.8979 |       -151.898 | 2019-01-01 00:00:00 |       59.8979 |       -151.898 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 59 | 2019205001 | profile       | ['temp', 'salt'] |       59.6756 |       -151.205 | 2019-01-01 00:00:00 |       59.6756 |       -151.205 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 60 | 2019210001 | profile       | ['temp', 'salt'] |       59.4996 |       -151.735 | 2019-01-01 00:00:00 |       59.4996 |       -151.735 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 61 | 2019221001 | profile       | ['temp', 'salt'] |       59.6465 |       -152.216 | 2019-01-01 00:00:00 |       59.6465 |       -152.216 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 62 | 2019223001 | profile       | ['temp', 'salt'] |       59.5795 |       -151.4   | 2019-01-01 00:00:00 |       59.5795 |       -151.4   | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 63 | 2019223002 | profile       | ['temp', 'salt'] |       59.5726 |       -151.765 | 2019-01-01 00:00:00 |       59.5726 |       -151.765 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 64 | 2019226001 | profile       | ['temp', 'salt'] |       59.3545 |       -152.231 | 2019-01-01 00:00:00 |       59.3545 |       -152.231 | 2019-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 65 | 2021105001 | profile       | ['temp', 'salt'] |       60.0328 |       -152.547 | 2021-01-01 00:00:00 |       60.0328 |       -152.547 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 66 | 2021122001 | profile       | ['temp', 'salt'] |       60.1651 |       -152.314 | 2021-01-01 00:00:00 |       60.1651 |       -152.314 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 67 | 2021123001 | profile       | ['temp', 'salt'] |       60.0727 |       -152.062 | 2021-01-01 00:00:00 |       60.0727 |       -152.062 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 68 | 2021124001 | profile       | ['temp', 'salt'] |       60.0058 |       -152.25  | 2021-01-01 00:00:00 |       60.0058 |       -152.25  | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 69 | 2021125001 | profile       | ['temp', 'salt'] |       59.8989 |       -151.97  | 2021-01-01 00:00:00 |       59.8989 |       -151.97  | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 70 | 2021126001 | profile       | ['temp', 'salt'] |       59.8513 |       -152.565 | 2021-01-01 00:00:00 |       59.8513 |       -152.565 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 71 | 2021205001 | profile       | ['temp', 'salt'] |       59.7194 |       -151.104 | 2021-01-01 00:00:00 |       59.7194 |       -151.104 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 72 | 2021210001 | profile       | ['temp', 'salt'] |       59.5051 |       -151.586 | 2021-01-01 00:00:00 |       59.5051 |       -151.586 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 73 | 2021221001 | profile       | ['temp', 'salt'] |       59.667  |       -152.202 | 2021-01-01 00:00:00 |       59.667  |       -152.202 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 74 | 2021223001 | profile       | ['temp', 'salt'] |       59.582  |       -151.579 | 2021-01-01 00:00:00 |       59.582  |       -151.579 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 75 | 2021223002 | profile       | ['temp', 'salt'] |       59.5683 |       -151.419 | 2021-01-01 00:00:00 |       59.5683 |       -151.419 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 76 | 2021224001 | profile       | ['temp', 'salt'] |       59.4972 |       -152.164 | 2021-01-01 00:00:00 |       59.4972 |       -152.164 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |
| 77 | 2021226001 | profile       | ['temp', 'salt'] |       59.3349 |       -152.047 | 2021-01-01 00:00:00 |       59.3349 |       -152.047 | 2021-01-01 00:00:00 | https://researchworkspace.com/files/42202136/Arimitsu_CookInlet_CTD.csv |

```
````

+++




**Map of CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_usgs_boem")("ctd_profiles_usgs_boem")
```


### Towed CTD (OTF KBNERR): central Cook Inlet

* CTD Towed 2003 - OTF KBNERR
* July 2003, 5min sampling frequency
* Slug: ctd_towed_otf_kbnerr
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_towed_otf_kbnerr`

Towed CTD Profiles.

Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths


Notes:

Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                   | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                    |
|---:|:--------------------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:---------------------------------------------------------------------------|
|  0 | mic071303_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8603 |       -152.314 | 2003-07-13 13:30:00 |       59.8288 |       -152.416 | 2003-07-13 06:50:00 | https://researchworkspace.com/files/42202371/mic071303_subsampled.csv      |
|  1 | mic071903_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8799 |       -152.154 | 2003-07-19 11:15:00 |       59.8237 |       -152.403 | 2003-07-19 06:40:00 | https://researchworkspace.com/files/42202372/mic071903_subsampled.csv      |
|  2 | mic072003_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8718 |       -152.181 | 2003-07-20 15:55:00 |       59.8176 |       -152.45  | 2003-07-20 11:00:00 | https://researchworkspace.com/files/42202373/mic072003_subsampled.csv      |
|  3 | mic072103_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8729 |       -152.147 | 2003-07-21 11:30:00 |       59.8246 |       -152.456 | 2003-07-21 06:25:00 | https://researchworkspace.com/files/42202374/mic072103_subsampled.csv      |
|  4 | mic072203_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8739 |       -152.153 | 2003-07-22 15:50:00 |       59.8371 |       -152.441 | 2003-07-22 11:15:00 | https://researchworkspace.com/files/42202375/mic072203_subsampled.csv      |
|  5 | mic072403_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.874  |       -152.164 | 2003-07-24 15:55:00 |       59.8376 |       -152.445 | 2003-07-24 11:30:00 | https://researchworkspace.com/files/42202376/mic072403_subsampled.csv      |
|  6 | mic072503_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8589 |       -152.156 | 2003-07-25 12:10:00 |       59.8267 |       -152.464 | 2003-07-25 06:55:00 | https://researchworkspace.com/files/42202377/mic072503_subsampled.csv      |
|  7 | mic072603_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8736 |       -152.158 | 2003-07-26 16:15:00 |       59.8275 |       -152.434 | 2003-07-26 11:05:00 | https://researchworkspace.com/files/42202378/mic072603_subsampled.csv      |
|  8 | mic072803_65-8_subsampled | trajectoryProfile | ['temp', 'salt'] |       59.8948 |       -152.303 | 2003-07-28 17:05:00 |       59.8644 |       -152.439 | 2003-07-28 14:50:00 | https://researchworkspace.com/files/42202379/mic072803_65-8_subsampled.csv |
|  9 | mic072903_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8801 |       -152.154 | 2003-07-29 10:10:00 |       59.7911 |       -152.419 | 2003-07-29 05:35:00 | https://researchworkspace.com/files/42202380/mic072903_subsampled.csv      |
| 10 | mic073003_subsampled      | trajectoryProfile | ['temp', 'salt'] |       59.8731 |       -152.182 | 2003-07-30 14:10:00 |       59.7915 |       -152.435 | 2003-07-30 10:05:00 | https://researchworkspace.com/files/42202381/mic073003_subsampled.csv      |

```
````

+++




**Map of Towed CTD Profiles**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_towed_otf_kbnerr")("ctd_towed_otf_kbnerr")
```


### Underway CTD (NOAA PMEL): Towed on ferry

* CTD Towed 2004-2008 Ferry in-line - NOAA PMEL
* Continuous 2004 to 2008, 5min sampling frequency
* Slug: ctd_towed_ferry_noaa_pmel
* Included: True
* Feature type: trajectory
* See the full dataset page for more information: {ref}`page:ctd_towed_ferry_noaa_pmel`


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


Notes:

The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   | featuretype   | key_variables   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                                        |
|---:|:----------|:--------------|:----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------------------------------------|
|  0 | 2004-10   | trajectory    | []              |       60.1176 |       -148.512 | 2004-10-12 17:55:00 |       56.5869 |       -156.487 | 2004-10-01 00:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  1 | 2004-11   | trajectory    | []              |       60.1153 |       -148.503 | 2004-11-23 06:55:00 |       57.7869 |       -152.861 | 2004-11-08 04:55:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  2 | 2004-12   | trajectory    | []              |       60.1177 |       -148.51  | 2004-12-30 22:55:00 |       57.7931 |       -152.377 | 2004-12-01 05:25:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  3 | 2004-9    | trajectory    | []              |       60.118  |       -148.51  | 2004-09-30 21:50:00 |       57.787  |       -152.861 | 2004-09-15 07:10:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  4 | 2005-1    | trajectory    | []              |       60.1174 |       -148.507 | 2005-01-31 23:55:00 |       57.7841 |       -152.862 | 2005-01-01 08:35:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  5 | 2005-10   | trajectory    | []              |       59.6025 |       -151.403 | 2005-10-31 20:10:00 |       56.5857 |       -156.49  | 2005-10-01 05:40:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  6 | 2005-11   | trajectory    | []              |       59.6423 |       -148.507 | 2005-11-16 20:40:00 |       57.7401 |       -153.48  | 2005-11-01 03:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  7 | 2005-2    | trajectory    | []              |       60.1183 |       -148.51  | 2005-02-28 23:55:00 |       57.7838 |       -152.862 | 2005-02-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  8 | 2005-3    | trajectory    | []              |       60.1173 |       -148.529 | 2005-03-08 23:10:00 |       57.7868 |       -152.86  | 2005-03-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  9 | 2005-4    | trajectory    | []              |       60.1166 |       -148.521 | 2005-04-28 23:00:00 |       56.5825 |       -156.494 | 2005-04-10 06:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 10 | 2005-5    | trajectory    | []              |       60.1161 |       -148.531 | 2005-05-03 14:45:00 |       57.787  |       -152.861 | 2005-05-02 05:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 11 | 2005-6    | trajectory    | []              |       60.1188 |       -148.5   | 2005-06-30 22:55:00 |       56.5725 |       -156.496 | 2005-06-08 07:30:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 12 | 2005-7    | trajectory    | []              |       60.1184 |       -148.512 | 2005-07-31 21:15:00 |       56.5772 |       -156.494 | 2005-07-01 02:50:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 13 | 2005-8    | trajectory    | []              |       60.1181 |       -148.51  | 2005-08-31 15:50:00 |       56.5715 |       -156.5   | 2005-08-01 02:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 14 | 2005-9    | trajectory    | []              |       60.1178 |       -148.511 | 2005-09-30 21:55:00 |       57.7869 |       -153.645 | 2005-09-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 15 | 2006-10   | trajectory    | []              |       59.6025 |       -151.403 | 2006-10-31 22:25:00 |       56.5905 |       -156.485 | 2006-10-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 16 | 2006-11   | trajectory    | []              |       59.6169 |       -151.317 | 2006-11-30 22:10:00 |       57.7867 |       -153.477 | 2006-11-01 03:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 17 | 2006-12   | trajectory    | []              |       59.6056 |       -151.399 | 2006-12-31 22:20:00 |       57.7868 |       -153.473 | 2006-12-01 03:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 18 | 2006-5    | trajectory    | []              |       59.6025 |       -151.402 | 2006-05-31 19:35:00 |       56.5865 |       -156.479 | 2006-05-10 18:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 19 | 2006-6    | trajectory    | []              |       59.6025 |       -151.402 | 2006-06-29 14:30:00 |       56.58   |       -156.497 | 2006-06-01 01:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 20 | 2006-7    | trajectory    | []              |       59.6024 |       -151.402 | 2006-07-31 23:55:00 |       56.579  |       -156.495 | 2006-07-03 15:45:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 21 | 2006-8    | trajectory    | []              |       59.6026 |       -151.402 | 2006-08-31 15:55:00 |       56.583  |       -156.493 | 2006-08-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 22 | 2006-9    | trajectory    | []              |       59.6025 |       -151.401 | 2006-09-30 23:55:00 |       56.5744 |       -156.497 | 2006-09-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 23 | 2007-1    | trajectory    | []              |       59.6024 |       -151.404 | 2007-01-09 15:55:00 |       57.7828 |       -153.466 | 2007-01-01 03:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 24 | 2007-10   | trajectory    | []              |       58.7269 |       -152.039 | 2007-10-01 11:55:00 |       58.5762 |       -152.118 | 2007-10-01 11:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 25 | 2007-2    | trajectory    | []              |       60.0201 |       -149.372 | 2007-02-28 17:05:00 |       57.7867 |       -153.468 | 2007-02-19 09:45:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 26 | 2007-3    | trajectory    | []              |       59.6731 |       -151.211 | 2007-03-31 23:55:00 |       57.7867 |       -153.476 | 2007-03-01 07:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 27 | 2007-4    | trajectory    | []              |       59.6028 |       -151.388 | 2007-04-30 20:15:00 |       56.5819 |       -156.492 | 2007-04-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 28 | 2007-5    | trajectory    | []              |       59.6025 |       -151.382 | 2007-05-31 14:05:00 |       56.5826 |       -156.494 | 2007-05-01 02:40:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 29 | 2007-6    | trajectory    | []              |       59.6027 |       -151.401 | 2007-06-28 13:55:00 |       56.576  |       -156.498 | 2007-06-04 21:40:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 30 | 2007-7    | trajectory    | []              |       59.6025 |       -151.403 | 2007-07-31 21:50:00 |       56.581  |       -156.494 | 2007-07-02 23:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 31 | 2007-8    | trajectory    | []              |       59.6023 |       -151.402 | 2007-08-31 20:30:00 |       56.5844 |       -156.497 | 2007-08-03 16:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 32 | 2007-9    | trajectory    | []              |       59.6025 |       -151.401 | 2007-09-20 07:55:00 |       56.598  |       -156.453 | 2007-09-01 02:25:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 33 | 2008-10   | trajectory    | []              |       59.6023 |       -151.402 | 2008-10-31 20:20:00 |       56.5825 |       -156.496 | 2008-10-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 34 | 2008-11   | trajectory    | []              |       59.6023 |       -151.404 | 2008-11-05 17:05:00 |       57.7868 |       -152.862 | 2008-11-01 02:30:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 35 | 2008-3    | trajectory    | []              |       60.814  |       -148.501 | 2008-03-31 21:55:00 |       57.7868 |       -152.862 | 2008-03-10 18:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 36 | 2008-4    | trajectory    | []              |       60.8154 |       -148.5   | 2008-04-30 22:05:00 |       57.7868 |       -152.862 | 2008-04-01 19:10:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 37 | 2008-5    | trajectory    | []              |       59.6025 |       -151.402 | 2008-05-29 14:10:00 |       56.5776 |       -156.494 | 2008-05-01 04:50:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 38 | 2008-6    | trajectory    | []              |       59.6025 |       -151.402 | 2008-06-30 23:55:00 |       56.5844 |       -156.496 | 2008-06-03 00:10:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 39 | 2008-7    | trajectory    | []              |       59.6023 |       -151.401 | 2008-07-31 21:20:00 |       56.5831 |       -156.5   | 2008-07-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 40 | 2008-8    | trajectory    | []              |       59.6033 |       -151.403 | 2008-08-31 21:10:00 |       56.5826 |       -156.494 | 2008-08-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 41 | 2008-9    | trajectory    | []              |       59.6025 |       -151.402 | 2008-09-30 21:20:00 |       57.7868 |       -153.462 | 2008-09-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |

```
````

+++




**Map of Towed CTD Paths**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_towed_ferry_noaa_pmel")("ctd_towed_ferry_noaa_pmel")
```


### Underway CTD (GWA): Towed CTD

* CTD Towed 2017-2019 - GWA
* Approximately monthly in summer from 2017 to 2020, 5min sampling frequency
* Slug: ctd_towed_gwa
* Included: True
* Feature type: trajectory
* See the full dataset page for more information: {ref}`page:ctd_towed_gwa`

Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2017-2020. 2017 and 2018 have salinity and temperature, 2019 and 2020 have only temperature.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Notes:

Made all longitudes negative west values, converted some local times, 2019 and 2020 only have temperature, ship track outside domain is not included, resampled from 2min to 5min.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset    | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                           |
|---:|:-----------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------------------------------|
|  0 | 2017-04-30 | trajectory    | ['temp', 'salt'] |       59.355  |       -150.5   | 2017-04-30 11:30:00 |        58.79  |       -152.08  | 2017-04-30 07:30:00 | https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv |
|  1 | 2017-05-30 | trajectory    | ['temp', 'salt'] |       59.3067 |       -150.51  | 2017-05-30 11:40:00 |        58.795 |       -152.08  | 2017-05-30 08:00:00 | https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv |
|  2 | 2017-08-01 | trajectory    | ['temp', 'salt'] |       59.02   |       -150.52  | 2017-08-01 03:20:00 |        58.81  |       -151.38  | 2017-08-01 01:35:00 | https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv |
|  3 | 2017-09-03 | trajectory    | ['temp', 'salt'] |       59.03   |       -150.52  | 2017-09-03 04:35:00 |        58.8   |       -151.55  | 2017-09-03 02:25:00 | https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv |
|  4 | 2017-10-03 | trajectory    | ['temp', 'salt'] |       59.17   |       -150.5   | 2017-10-24 04:10:00 |        58.79  |       -152.08  | 2017-10-03 00:10:00 | https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv |
|  5 | 2018-04-17 | trajectory    | ['temp', 'salt'] |       59.16   |       -150.5   | 2018-04-17 11:35:00 |        58.81  |       -152.11  | 2018-04-17 08:10:00 | https://researchworkspace.com/files/42202337/CPR_physical_data_2018_subsetted.csv |
|  6 | 2018-05-19 | trajectory    | ['temp', 'salt'] |       59.11   |       -150.5   | 2018-05-19 19:00:00 |        58.81  |       -151.7   | 2018-05-19 15:20:00 | https://researchworkspace.com/files/42202337/CPR_physical_data_2018_subsetted.csv |
|  7 | 2018-06-18 | trajectory    | ['temp', 'salt'] |       59.965  |       -150.5   | 2018-06-18 19:20:00 |        58.8   |       -152.13  | 2018-06-18 14:20:00 | https://researchworkspace.com/files/42202337/CPR_physical_data_2018_subsetted.csv |
|  8 | 2018-07-21 | trajectory    | ['temp', 'salt'] |       59.475  |       -150.5   | 2018-07-21 21:00:00 |        58.8   |       -152.08  | 2018-07-21 17:00:00 | https://researchworkspace.com/files/42202337/CPR_physical_data_2018_subsetted.csv |
|  9 | 2019-04-13 | trajectory    | ['temp']         |       59.38   |       -150.52  | 2019-04-13 21:20:00 |        58.81  |       -152.13  | 2019-04-13 18:00:00 | https://researchworkspace.com/files/42202339/CPR_physical_data_2019_subsetted.csv |
| 10 | 2019-05-13 | trajectory    | ['temp']         |       58.94   |       -150.5   | 2019-05-13 19:40:00 |        58.8   |       -151.01  | 2019-05-13 18:40:00 | https://researchworkspace.com/files/42202339/CPR_physical_data_2019_subsetted.csv |
| 11 | 2019-08-17 | trajectory    | ['temp']         |       59.37   |       -150.51  | 2019-08-17 21:25:00 |        58.82  |       -152.17  | 2019-08-17 18:15:00 | https://researchworkspace.com/files/42202339/CPR_physical_data_2019_subsetted.csv |
| 12 | 2019-09-16 | trajectory    | ['temp']         |       59.34   |       -150.51  | 2019-09-16 23:00:00 |        58.57  |       -152.12  | 2019-09-16 19:10:00 | https://researchworkspace.com/files/42202339/CPR_physical_data_2019_subsetted.csv |
| 13 | 2020-07-07 | trajectory    | ['temp']         |       59.42   |       -150.512 | 2020-07-07 05:30:00 |        58.79  |       -152.153 | 2020-07-07 01:25:00 | https://researchworkspace.com/files/42202341/CPR_physical_data_2020_subsetted.csv |
| 14 | 2020-08-09 | trajectory    | ['temp']         |       59.4    |       -150.513 | 2020-08-09 08:00:00 |        58.79  |       -152.133 | 2020-08-09 04:05:00 | https://researchworkspace.com/files/42202341/CPR_physical_data_2020_subsetted.csv |
| 15 | 2020-09-08 | trajectory    | ['temp']         |       60.52   |       -150.516 | 2020-09-08 23:05:00 |        58.77  |       -152.2   | 2020-09-08 15:05:00 | https://researchworkspace.com/files/42202341/CPR_physical_data_2020_subsetted.csv |

```
````

+++




**Map of Flow through on Ship of Opportunity**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_towed_gwa")("ctd_towed_gwa")
```


### Underway CTD (GWA): Towed, temperature only

* Temperature towed 2011-2016 - GWA
* Approximately monthly in summer from 2011 to 2016, 5min sampling frequency
* Slug: ctd_towed_gwa_temp
* Included: True
* Feature type: trajectory
* See the full dataset page for more information: {ref}`page:ctd_towed_gwa_temp`

Temperature only: Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska.

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2011-2016.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Notes:

Converted some local times, ship track outside domain is not included.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset    | featuretype   | key_variables   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                             |
|---:|:-----------|:--------------|:----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------------------------------------|
|  0 | 2011-06-20 | trajectory    | ['temp']        |       59.2073 |       -150.532 | 2011-06-20 17:40:00 |       58.8066 |       -152.133 | 2011-06-20 14:50:00 | https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv |
|  1 | 2011-07-23 | trajectory    | ['temp']        |       59.0286 |       -150.526 | 2011-07-23 18:00:00 |       58.8215 |       -151.448 | 2011-07-23 16:25:00 | https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv |
|  2 | 2011-08-22 | trajectory    | ['temp']        |       59.1542 |       -150.5   | 2011-08-22 18:05:00 |       58.8112 |       -152.048 | 2011-08-22 15:20:00 | https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv |
|  3 | 2012-04-09 | trajectory    | ['temp']        |       60.58   |       -150.52  | 2012-04-10 02:05:00 |       58.82   |       -152.13  | 2012-04-09 19:30:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  4 | 2012-05-13 | trajectory    | ['temp']        |       59.41   |       -150.52  | 2012-05-13 03:30:00 |       58.82   |       -152.14  | 2012-05-13 00:15:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  5 | 2012-06-11 | trajectory    | ['temp']        |       59.34   |       -150.51  | 2012-06-12 03:10:00 |       58.81   |       -152.13  | 2012-06-11 23:55:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  6 | 2012-09-16 | trajectory    | ['temp']        |       59.54   |       -150.52  | 2012-09-16 05:15:00 |       58.82   |       -152.13  | 2012-09-16 00:25:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  7 | 2012-10-16 | trajectory    | ['temp']        |       60.5    |       -150.51  | 2012-10-16 09:45:00 |       58.81   |       -152.13  | 2012-10-16 01:50:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  8 | 2013-04-14 | trajectory    | ['temp']        |       60.51   |       -150.53  | 2013-04-14 11:00:00 |       58.81   |       -152.13  | 2013-04-14 03:05:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
|  9 | 2013-05-13 | trajectory    | ['temp']        |       59.73   |       -150.5   | 2013-05-14 02:15:00 |       58.81   |       -152.13  | 2013-05-13 21:35:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 10 | 2013-06-15 | trajectory    | ['temp']        |       59.47   |       -150.52  | 2013-06-16 02:00:00 |       58.81   |       -152.13  | 2013-06-15 22:15:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 11 | 2013-07-15 | trajectory    | ['temp']        |       59.2    |       -150.51  | 2013-07-16 02:40:00 |       58.82   |       -152.1   | 2013-07-15 23:55:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 12 | 2013-08-17 | trajectory    | ['temp']        |       59.43   |       -150.5   | 2013-08-18 02:30:00 |       58.8    |       -152.13  | 2013-08-17 22:35:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 13 | 2014-04-27 | trajectory    | ['temp']        |       59.22   |       -150.53  | 2014-04-27 04:20:00 |       58.82   |       -152.13  | 2014-04-27 01:00:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 14 | 2014-05-27 | trajectory    | ['temp']        |       59.11   |       -150.51  | 2014-05-27 03:55:00 |       58.8    |       -151.99  | 2014-05-27 01:10:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 15 | 2014-06-29 | trajectory    | ['temp']        |       59.01   |       -150.51  | 2014-06-29 04:45:00 |       58.77   |       -151.66  | 2014-06-29 02:35:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 16 | 2014-07-29 | trajectory    | ['temp']        |       59.52   |       -150.52  | 2014-07-29 05:00:00 |       58.81   |       -152.28  | 2014-07-29 00:35:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 17 | 2014-08-31 | trajectory    | ['temp']        |       59.05   |       -150.51  | 2014-08-31 03:50:00 |       58.82   |       -151.82  | 2014-08-31 01:40:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 18 | 2015-08-23 | trajectory    | ['temp']        |       59.56   |       -150.5   | 2015-08-23 14:35:00 |       58.78   |       -152.13  | 2015-08-23 10:05:00 | https://researchworkspace.com/files/42202624/CPR_TemperatureData_2015_subsetted.csv |
| 19 | 2015-09-01 | trajectory    | ['temp']        |       60.53   |       -150.5   | 2015-09-01 16:10:00 |       58.66   |       -152.13  | 2015-09-01 08:05:00 | https://researchworkspace.com/files/42202624/CPR_TemperatureData_2015_subsetted.csv |
| 20 | 2016-04-17 | trajectory    | ['temp']        |       59.34   |       -150.53  | 2016-04-17 03:35:00 |       58.82   |       -152.16  | 2016-04-17 00:15:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 21 | 2016-05-16 | trajectory    | ['temp']        |       59.39   |       -150.5   | 2016-05-17 03:30:00 |       58.79   |       -152.18  | 2016-05-16 23:15:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 22 | 2016-06-19 | trajectory    | ['temp']        |       59.23   |       -150.5   | 2016-06-19 03:35:00 |       58.78   |       -152.15  | 2016-06-19 00:10:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 23 | 2016-07-19 | trajectory    | ['temp']        |       59.07   |       -150.51  | 2016-07-19 03:50:00 |       58.8    |       -151.9   | 2016-07-19 01:05:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 24 | 2016-08-29 | trajectory    | ['temp']        |       59.22   |       -150.52  | 2016-08-30 03:20:00 |       58.81   |       -152.14  | 2016-08-29 23:45:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 25 | 2016-10-02 | trajectory    | ['temp']        |       59.15   |       -150.5   | 2016-10-02 04:55:00 |       58.81   |       -152.03  | 2016-10-02 01:55:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |

```
````

+++




**Map of Flow through on Ship of Opportunity**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_towed_gwa_temp")("ctd_towed_gwa_temp")
```


### CTD transects: Barabara to Bluff

* Barabara to Bluff 2002-2003
* 2002-2003
* Slug: ctd_transects_barabara_to_bluff_2002_2003
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_barabara_to_bluff_2002_2003`

Repeat CTD transect from Barabara to Bluff Point in Cook Inlet from 2002 tp 2003.


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                   |
|---:|:----------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------|
|  0 | Cruise 1  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-07-23 10:34:00 |       59.49   |       -151.657 | 2002-07-23 08:28:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  1 | Cruise 10 | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-05-19 14:46:00 |       59.49   |       -151.657 | 2003-05-19 13:17:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  2 | Cruise 11 | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-06-21 13:02:00 |       59.49   |       -151.657 | 2003-06-21 11:20:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  3 | Cruise 2  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-09-07 13:16:00 |       59.49   |       -151.657 | 2002-09-07 11:05:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  4 | Cruise 3  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-09-25 13:56:00 |       59.49   |       -151.657 | 2002-09-25 11:55:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  5 | Cruise 4  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-11-11 16:31:00 |       59.49   |       -151.657 | 2002-11-11 14:45:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  6 | Cruise 5  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-12-11 18:55:00 |       59.49   |       -151.657 | 2002-12-11 16:39:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  7 | Cruise 6  | trajectoryProfile | ['temp', 'salt'] |       59.6233 |        -151.65 | 2003-01-31 17:27:00 |       59.49   |       -151.656 | 2003-01-31 15:56:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  8 | Cruise 7  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-02-18 18:19:00 |       59.49   |       -151.657 | 2003-02-18 16:50:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  9 | Cruise 8  | trajectoryProfile | ['temp', 'salt'] |       59.6317 |        -151.65 | 2003-03-31 17:32:00 |       59.4983 |       -151.656 | 2003-03-31 15:27:00 | https://researchworkspace.com/files/42396691/barabara.csv |
| 10 | Cruise 9  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-04-17 14:15:00 |       59.49   |       -151.657 | 2003-04-17 12:35:00 | https://researchworkspace.com/files/42396691/barabara.csv |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_barabara_to_bluff_2002_2003")("ctd_transects_barabara_to_bluff_2002_2003")
```


### CTD Transects, Moored CTD (CMI KBNERR): Six repeat, one single transect, one moored CTD

* CTD profiles 2004-2006 - CMI KBNERR
* From 2004 to 2006
* Slug: ctd_transects_cmi_kbnerr
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_cmi_kbnerr`

Seasonality of Boundary Conditions for Cook Inlet, Alaska

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


Notes:

Used in the NWGOA model/data comparison.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset          | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                          |
|---:|:-----------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------|
|  0 | Cruise_00-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.625  |       -151.65  | 2004-03-13 12:27:00 |       59.5083 |       -151.65  | 2004-03-13 10:40:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  1 | Cruise_01-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-04-20 18:20:00 |       58.65   |       -152.333 | 2004-04-20 08:45:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  2 | Cruise_01-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-04-19 23:10:00 |       58.6133 |       -153.24  | 2004-04-19 15:21:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  3 | Cruise_01-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-04-19 03:19:00 |       59.7717 |       -152.537 | 2004-04-18 21:36:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  4 | Cruise_01-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.625  |       -151.65  | 2004-04-21 09:28:00 |       59.5083 |       -151.65  | 2004-04-21 07:29:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  5 | Cruise_02-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-05-26 21:07:00 |       58.65   |       -152.333 | 2004-05-26 11:50:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  6 | Cruise_02-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-05-26 09:39:00 |       58.6133 |       -153.24  | 2004-05-26 02:17:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  7 | Cruise_02-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-05-25 16:34:00 |       59.7717 |       -152.537 | 2004-05-25 11:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  8 | Cruise_02-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.625  |       -151.65  | 2004-05-27 08:04:00 |       59.5169 |       -151.65  | 2004-05-27 05:59:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  9 | Cruise_03-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-06-13 20:35:00 |       58.65   |       -152.333 | 2004-06-13 11:34:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 10 | Cruise_03-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-06-14 05:21:00 |       58.6133 |       -153.24  | 2004-06-13 22:11:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 11 | Cruise_03-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-06-14 18:27:00 |       59.7717 |       -152.537 | 2004-06-14 13:39:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 12 | Cruise_03-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6417 |       -151.65  | 2004-06-15 02:01:00 |       59.5083 |       -151.65  | 2004-06-14 23:59:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 13 | Cruise_05-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-08-17 20:55:00 |       58.65   |       -152.333 | 2004-08-17 13:00:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 14 | Cruise_05-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-08-17 08:13:00 |       58.6133 |       -153.24  | 2004-08-17 02:15:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 15 | Cruise_05-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-08-16 14:41:00 |       59.7717 |       -152.537 | 2004-08-16 10:22:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 16 | Cruise_05-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6417 |       -151.65  | 2004-08-18 06:08:00 |       59.5083 |       -151.65  | 2004-08-18 04:21:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 17 | Cruise_06-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.19   |       -151.89  | 2004-09-08 09:39:00 |       58.65   |       -152.333 | 2004-09-07 23:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 18 | Cruise_06-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-09-08 21:50:00 |       58.6133 |       -153.24  | 2004-09-08 14:33:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 19 | Cruise_06-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-09-09 14:29:00 |       59.7717 |       -152.537 | 2004-09-09 09:03:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 20 | Cruise_06-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6417 |       -151.65  | 2004-09-09 20:03:00 |       59.5083 |       -151.65  | 2004-09-09 17:54:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 21 | Cruise_07-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-01-09 06:16:00 |       58.65   |       -152.333 | 2005-01-08 19:06:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 22 | Cruise_07-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-01-09 16:37:00 |       58.6133 |       -153.24  | 2005-01-09 08:10:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 23 | Cruise_07-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-01-10 09:01:00 |       59.7717 |       -152.567 | 2005-01-10 03:07:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 24 | Cruise_07-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-01-10 14:03:00 |       59.4917 |       -151.65  | 2005-01-10 11:04:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 25 | Cruise_08-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-04-26 07:23:00 |       58.65   |       -152.333 | 2005-04-25 20:05:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 26 | Cruise_08-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-04-26 19:48:00 |       58.6133 |       -153.24  | 2005-04-26 12:43:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 27 | Cruise_08-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-04-27 10:50:00 |       59.7717 |       -152.567 | 2005-04-27 04:33:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 28 | Cruise_08-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-04-25 17:42:00 |       59.4917 |       -151.65  | 2005-04-25 14:49:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 29 | Cruise_09-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-06-14 18:18:00 |       58.65   |       -152.333 | 2005-06-14 10:26:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 30 | Cruise_09-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-06-15 05:50:00 |       58.6133 |       -153.24  | 2005-06-14 23:37:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 31 | Cruise_09-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-06-15 20:28:00 |       59.7717 |       -152.567 | 2005-06-15 15:55:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 32 | Cruise_09-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-06-16 20:48:00 |       59.4917 |       -151.65  | 2005-06-16 18:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 33 | Cruise_10-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-07-30 06:56:00 |       58.65   |       -152.333 | 2005-07-29 17:13:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 34 | Cruise_10-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-07-29 12:14:00 |       58.6133 |       -153.24  | 2005-07-29 07:13:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 35 | Cruise_10-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-07-28 17:57:00 |       59.7717 |       -152.567 | 2005-07-28 11:09:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 36 | Cruise_10-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-07-30 18:02:00 |       59.4917 |       -151.65  | 2005-07-30 16:08:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 37 | Cruise_11-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-09-05 02:18:00 |       58.65   |       -152.333 | 2005-09-04 18:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 38 | Cruise_11-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-09-05 16:08:00 |       58.6133 |       -153.24  | 2005-09-05 10:42:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 39 | Cruise_11-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-09-06 08:02:00 |       59.7717 |       -152.567 | 2005-09-06 02:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 40 | Cruise_11-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-09-06 11:29:00 |       59.4917 |       -151.65  | 2005-09-06 09:35:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 41 | Cruise_12-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-10-13 22:35:00 |       58.65   |       -152.333 | 2005-10-13 15:26:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 42 | Cruise_12-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-10-14 06:03:00 |       58.6133 |       -153.24  | 2005-10-14 00:06:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 43 | Cruise_12-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-10-14 19:04:00 |       59.7717 |       -152.567 | 2005-10-14 14:47:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 44 | Cruise_12-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-10-14 22:50:00 |       59.4917 |       -151.65  | 2005-10-14 20:44:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 45 | Cruise_13-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-07-27 02:55:00 |       58.65   |       -152.333 | 2006-07-26 19:07:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 46 | Cruise_13-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.987 | 2006-07-26 03:26:00 |       59.81   |       -152.567 | 2006-07-26 00:02:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 47 | Cruise_13-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-07-28 14:32:00 |       59.4917 |       -151.65  | 2006-07-28 12:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 48 | Cruise_13-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-07-28 02:39:00 |       58.865  |       -153.24  | 2006-07-27 16:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 49 | Cruise_13-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152     | 2006-07-26 16:48:00 |       59.3083 |       -153.302 | 2006-07-26 09:08:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 50 | Cruise_14-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-08-06 10:16:00 |       58.65   |       -152.333 | 2006-08-06 03:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 51 | Cruise_14-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2006-08-06 22:48:00 |       58.6133 |       -153.24  | 2006-08-06 17:40:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 52 | Cruise_14-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2006-08-05 14:02:00 |       59.7717 |       -152.567 | 2006-08-05 10:04:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 53 | Cruise_14-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-08-07 14:57:00 |       59.4917 |       -151.65  | 2006-08-07 13:11:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 54 | Cruise_14-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-08-07 08:22:00 |       58.865  |       -153.24  | 2006-08-06 23:14:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 55 | Cruise_14-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.355  |       -152     | 2006-08-06 02:06:00 |       59.3083 |       -153.302 | 2006-08-05 19:22:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 56 | Cruise_15-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-08-13 02:41:00 |       58.65   |       -152.333 | 2006-08-12 19:38:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 57 | Cruise_15-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2006-08-12 04:36:00 |       59.7717 |       -152.567 | 2006-08-12 00:23:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 58 | Cruise_15-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-08-14 13:27:00 |       59.4917 |       -151.65  | 2006-08-14 11:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 59 | Cruise_15-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-08-14 03:21:00 |       58.865  |       -153.24  | 2006-08-13 17:40:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 60 | Cruise_15-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.355  |       -152     | 2006-08-12 17:34:00 |       59.3083 |       -153.302 | 2006-08-12 10:17:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 61 | Cruise_16-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-09-12 13:16:00 |       58.65   |       -152.333 | 2006-09-12 06:48:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 62 | Cruise_16-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2006-09-13 05:36:00 |       58.6133 |       -153.24  | 2006-09-13 00:12:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 63 | Cruise_16-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2006-09-11 16:22:00 |       59.7717 |       -152.567 | 2006-09-11 12:16:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 64 | Cruise_16-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-09-13 19:04:00 |       59.4917 |       -151.65  | 2006-09-13 17:18:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 65 | Cruise_16-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-09-13 15:03:00 |       58.865  |       -153.24  | 2006-09-13 06:13:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 66 | Cruise_16-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.355  |       -152     | 2006-09-12 05:27:00 |       59.3083 |       -153.302 | 2006-09-11 22:06:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 67 | Kbay_timeseries  | trajectoryProfile | ['temp', 'salt'] |       59.5833 |       -151.75  | 2006-04-23 17:33:00 |       59.5833 |       -151.75  | 2006-04-22 17:06:00 | https://researchworkspace.com/files/39886046/Kbay_timeseries.txt |
| 68 | sue_shelikof     | trajectoryProfile | ['temp', 'salt'] |       58.6133 |       -152.633 | 2006-09-12 22:04:00 |       58.3505 |       -152.898 | 2006-09-12 19:41:00 | https://researchworkspace.com/files/39886061/sue_shelikof.txt    |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_cmi_kbnerr")("ctd_transects_cmi_kbnerr")
```


### CTD Transect (CMI UAF): from East Foreland Lighthouse

* CTD profiles 2004-2005 - CMI UAF
* 10 cruises, approximately monthly for summer months, in 2004 and 2005
* Slug: ctd_transects_cmi_uaf
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_cmi_uaf`

Seasonality of Boundary Conditions for Cook Inlet, Alaska: Transect (3) at East Foreland Lighthouse.

9 CTD profiles at stations across 10 cruises in (approximately) the same locations. Approximately monthly for summer months, 2004 and 2005.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf


Notes:

Used in the NWGOA model/data comparison.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                            |
|---:|:----------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------------|
|  0 | Cruise-01 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.418 | 2004-05-21 10:34:00 |        60.716 |       -151.683 | 2004-05-21 09:23:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  1 | Cruise-02 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2004-06-24 09:08:00 |        60.716 |       -151.683 | 2004-06-24 07:07:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  2 | Cruise-03 | trajectoryProfile | ['temp', 'salt'] |        60.718 |       -151.417 | 2004-08-08 09:20:00 |        60.716 |       -151.683 | 2004-08-08 07:55:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  3 | Cruise-04 | trajectoryProfile | ['temp', 'salt'] |        60.718 |       -151.417 | 2004-09-17 08:25:00 |        60.715 |       -151.684 | 2004-09-17 07:00:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  4 | Cruise-05 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2004-10-09 14:37:00 |        60.713 |       -151.683 | 2004-10-09 13:21:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  5 | Cruise-06 | trajectoryProfile | ['temp', 'salt'] |        60.72  |       -151.45  | 2005-03-30 12:49:00 |        60.72  |       -151.65  | 2005-03-30 11:22:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  6 | Cruise-07 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-05-02 12:32:00 |        60.715 |       -151.683 | 2005-05-02 11:13:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  7 | Cruise-08 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-06-01 13:23:00 |        60.715 |       -151.683 | 2005-06-01 12:03:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  8 | Cruise-09 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-08-26 11:08:00 |        60.715 |       -151.683 | 2005-08-26 09:35:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  9 | Cruise-10 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-10-03 18:50:00 |        60.716 |       -151.684 | 2005-10-03 17:39:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_cmi_uaf")("ctd_transects_cmi_uaf")
```


### CTD Transects (GWA): Six repeat transects in Cook Inlet

* CTD profiles 2012-2021 - GWA
* Quarterly repeats from 2012 to 2021
* Slug: ctd_transects_gwa
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_gwa`


The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    

Notes:

Not used in the NWGOA model/data comparison.

````{div} full-width
```{dropdown} Dataset metadata

|     | Dataset                        | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                                  |
|----:|:-------------------------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------------------------------|
|   0 | transect_3-2012-05-02          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2012-05-02 23:56:00 |       59.78   |       -152.567 | 2012-05-02 17:54:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|   1 | transect_3-2012-07-29          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2012-07-29 20:35:00 |       59.78   |       -152.567 | 2012-07-29 15:04:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|   2 | transect_3-2012-10-29          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2012-10-29 13:30:00 |       59.78   |       -152.567 | 2012-10-29 08:55:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|   3 | transect_3-2013-04-20          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2013-04-20 22:41:00 |       59.78   |       -152.567 | 2013-04-20 18:08:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|   4 | transect_3-2013-07-19          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2013-07-19 15:28:00 |       59.78   |       -152.567 | 2013-07-19 09:59:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|   5 | transect_3-2013-11-08          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2013-11-08 16:35:00 |       59.78   |       -152.567 | 2013-11-08 12:08:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|   6 | transect_3-2014-04-11          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2014-04-11 15:03:00 |       59.78   |       -152.567 | 2014-04-11 10:53:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|   7 | transect_3-2014-07-22          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.883 | 2014-07-22 14:23:00 |       59.772  |       -152.567 | 2014-07-22 08:01:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|   8 | transect_3-2014-10-13          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2014-10-13 17:30:00 |       59.78   |       -152.567 | 2014-10-13 13:13:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|   9 | transect_3-2015-02-22          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2015-02-22 16:01:00 |       59.78   |       -152.567 | 2015-02-22 11:47:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  10 | transect_3-2015-04-12          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2015-04-12 19:18:00 |       59.78   |       -152.567 | 2015-04-12 14:34:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  11 | transect_3-2015-11-04          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2015-11-04 13:17:00 |       59.78   |       -152.567 | 2015-11-04 03:32:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  12 | transect_3-2016-02-14          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2016-02-14 18:00:00 |       59.78   |       -152.567 | 2016-02-14 13:25:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  13 | transect_3-2016-04-11          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2016-04-11 11:03:00 |       59.78   |       -152.567 | 2016-04-11 06:52:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  14 | transect_3-2016-08-29          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.883 | 2016-08-29 15:21:00 |       59.772  |       -152.567 | 2016-08-29 08:13:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  15 | transect_3-2017-04-19          | trajectoryProfile | ['temp', 'salt'] |       60.007  |       -151.905 | 2017-04-20 00:12:00 |       59.78   |       -152.567 | 2017-04-19 19:35:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  16 | transect_3-2017-07-25          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2017-07-25 13:17:00 |       59.78   |       -152.04  | 2017-07-25 12:29:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  17 | transect_3-2018-06-25          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2018-06-25 11:17:00 |       59.78   |       -152.04  | 2018-06-25 10:41:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  18 | transect_3-2018-07-26          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2018-07-26 12:41:00 |       59.78   |       -152.04  | 2018-07-26 12:00:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  19 | transect_3-2018-09-13          | trajectoryProfile | ['temp', 'salt'] |       59.863  |       -151.987 | 2018-09-13 11:18:00 |       59.81   |       -152.145 | 2018-09-13 10:48:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  20 | transect_3-2019-02-08          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2019-02-08 15:46:00 |       59.78   |       -152.04  | 2019-02-08 15:05:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  21 | transect_3-2019-05-14          | trajectoryProfile | ['temp', 'salt'] |       59.81   |       -151.905 | 2019-05-14 13:11:00 |       59.78   |       -151.987 | 2019-05-14 12:39:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  22 | transect_3-2019-07-25          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.935 | 2019-07-25 14:05:00 |       59.79   |       -152.04  | 2019-07-25 13:25:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  23 | transect_3-2019-09-16          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2019-09-16 13:53:00 |       59.78   |       -152.04  | 2019-09-16 13:09:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  24 | transect_3-2020-07-29          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2020-07-29 10:45:00 |       59.78   |       -152.04  | 2020-07-29 10:08:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  25 | transect_3-2021-04-16          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.905 | 2021-04-16 11:44:00 |       59.78   |       -152.04  | 2021-04-16 11:02:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  26 | transect_3-2021-07-16          | trajectoryProfile | ['temp', 'salt'] |       59.827  |       -151.935 | 2021-07-16 15:44:00 |       59.79   |       -152.04  | 2021-07-16 15:05:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  27 | transect_4-2012-05-02          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-05-02 15:35:00 |       59.492  |       -151.65  | 2012-05-02 13:15:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  28 | transect_4-2012-05-31          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-05-31 12:42:00 |       59.492  |       -151.65  | 2012-05-31 10:58:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  29 | transect_4-2012-06-05_A        | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-06-05 11:29:00 |       59.492  |       -151.65  | 2012-06-05 09:16:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  30 | transect_4-2012-06-05_B        | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-06-05 17:30:00 |       59.492  |       -151.65  | 2012-06-05 15:24:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  31 | transect_4-2012-07-31          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-07-31 11:02:00 |       59.492  |       -151.65  | 2012-07-31 08:36:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  32 | transect_4-2012-08-15          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-08-15 16:00:00 |       59.492  |       -151.65  | 2012-08-15 14:34:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  33 | transect_4-2012-10-29          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2012-10-29 17:43:00 |       59.492  |       -151.65  | 2012-10-29 15:45:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  34 | transect_4-2013-02-12          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2013-02-12 15:17:00 |       59.492  |       -151.65  | 2013-02-12 12:59:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  35 | transect_4-2013-04-21          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2013-04-21 11:45:00 |       59.492  |       -151.65  | 2013-04-21 09:26:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  36 | transect_4-2013-06-06          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2013-06-06 11:15:00 |       59.492  |       -151.65  | 2013-06-06 09:45:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  37 | transect_4-2013-07-19          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2013-07-19 20:55:00 |       59.492  |       -151.65  | 2013-07-19 17:50:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  38 | transect_4-2013-10-29          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2013-10-29 14:44:00 |       59.492  |       -151.65  | 2013-10-29 12:18:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  39 | transect_4-2014-02-15          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2014-02-15 15:34:00 |       59.492  |       -151.65  | 2014-02-15 13:23:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  40 | transect_4-2014-04-11          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2014-04-11 18:27:00 |       59.492  |       -151.65  | 2014-04-11 16:30:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  41 | transect_4-2014-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2014-07-21 22:13:00 |       59.492  |       -151.65  | 2014-07-21 18:36:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  42 | transect_4-2014-08-13          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2014-08-13 16:04:00 |       59.492  |       -151.65  | 2014-08-13 14:02:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  43 | transect_4-2014-10-13          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2014-10-13 11:23:00 |       59.492  |       -151.65  | 2014-10-13 08:58:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  44 | transect_4-2015-02-12          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2015-02-12 12:40:00 |       59.492  |       -151.65  | 2015-02-12 10:26:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  45 | transect_4-2015-02-24          | trajectoryProfile | ['temp', 'salt'] |       59.542  |       -151.65  | 2015-02-24 18:13:00 |       59.542  |       -151.65  | 2015-02-24 18:13:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  46 | transect_4-2015-04-08          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2015-04-08 11:08:00 |       59.492  |       -151.65  | 2015-04-08 09:08:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  47 | transect_4-2015-08-14          | trajectoryProfile | ['temp', 'salt'] |       59.542  |       -151.65  | 2015-08-14 15:55:00 |       59.492  |       -151.65  | 2015-08-14 15:07:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  48 | transect_4-2015-09-24          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2015-09-24 16:19:00 |       59.492  |       -151.65  | 2015-09-24 15:05:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  49 | transect_4-2015-10-19          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2015-10-19 17:58:00 |       59.492  |       -151.65  | 2015-10-19 16:26:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  50 | transect_4-2015-11-03          | trajectoryProfile | ['temp', 'salt'] |       59.542  |       -151.65  | 2015-11-03 16:29:00 |       59.542  |       -151.65  | 2015-11-03 16:29:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  51 | transect_4-2015-11-04          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2015-11-04 18:51:00 |       59.492  |       -151.65  | 2015-11-04 15:32:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  52 | transect_4-2015-12-10          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2015-12-10 15:13:00 |       59.492  |       -151.65  | 2015-12-10 13:40:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  53 | transect_4-2016-02-09          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2016-02-09 12:34:00 |       59.492  |       -151.65  | 2016-02-09 10:35:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  54 | transect_4-2016-04-11          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2016-04-11 15:13:00 |       59.492  |       -151.65  | 2016-04-11 13:11:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  55 | transect_4-2016-07-27          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2016-07-27 14:30:00 |       59.492  |       -151.65  | 2016-07-27 12:40:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  56 | transect_4-2016-10-13          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2016-10-13 16:34:00 |       59.492  |       -151.65  | 2016-10-13 14:51:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  57 | transect_4-2016-12-13          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2016-12-13 16:01:00 |       59.492  |       -151.65  | 2016-12-13 13:49:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  58 | transect_4-2017-04-20          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2017-04-20 15:56:00 |       59.492  |       -151.65  | 2017-04-20 13:38:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  59 | transect_4-2017-07-25          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2017-07-25 11:53:00 |       59.492  |       -151.65  | 2017-07-25 09:48:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  60 | transect_4-2017-10-17          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2017-10-17 13:33:00 |       59.492  |       -151.65  | 2017-10-17 11:33:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  61 | transect_4-2018-04-23          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2018-04-23 15:11:00 |       59.492  |       -151.65  | 2018-04-23 13:18:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  62 | transect_4-2018-06-25          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2018-06-25 14:32:00 |       59.492  |       -151.65  | 2018-06-25 12:26:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  63 | transect_4-2018-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2018-07-24 12:08:00 |       59.492  |       -151.65  | 2018-07-24 10:24:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  64 | transect_4-2018-09-13          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2018-09-13 13:42:00 |       59.492  |       -151.65  | 2018-09-13 12:04:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  65 | transect_4-2019-02-07          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2019-02-07 12:28:00 |       59.492  |       -151.65  | 2019-02-07 10:34:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  66 | transect_4-2019-05-14          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2019-05-14 11:24:00 |       59.492  |       -151.65  | 2019-05-14 09:36:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  67 | transect_4-2019-07-25          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2019-07-25 17:01:00 |       59.492  |       -151.65  | 2019-07-25 14:37:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  68 | transect_4-2019-09-16          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2019-09-16 16:29:00 |       59.492  |       -151.65  | 2019-09-16 14:27:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  69 | transect_4-2020-02-14          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2020-02-14 14:31:00 |       59.492  |       -151.65  | 2020-02-14 12:52:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  70 | transect_4-2020-07-23          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2020-07-23 11:43:00 |       59.492  |       -151.65  | 2020-07-23 09:39:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  71 | transect_4-2020-09-21          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2020-09-21 13:34:00 |       59.492  |       -151.65  | 2020-09-21 11:51:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  72 | transect_4-2021-02-17          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2021-02-17 13:08:00 |       59.492  |       -151.65  | 2021-02-17 11:39:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  73 | transect_4-2021-04-16          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2021-04-16 13:54:00 |       59.492  |       -151.65  | 2021-04-16 12:16:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  74 | transect_4-2021-07-16          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2021-07-16 14:21:00 |       59.492  |       -151.65  | 2021-07-16 12:30:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  75 | transect_4-2021-09-17          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2021-09-17 12:43:00 |       59.492  |       -151.65  | 2021-09-17 11:00:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  76 | transect_4-2022-03-01          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2022-03-01 12:55:00 |       59.492  |       -151.65  | 2022-03-01 11:50:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
|  77 | transect_4-2022-04-13          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2022-04-13 11:26:00 |       59.492  |       -151.65  | 2022-04-13 10:15:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
|  78 | transect_4-2022-07-23          | trajectoryProfile | ['temp', 'salt'] |       59.633  |       -151.65  | 2022-07-23 12:19:00 |       59.492  |       -151.65  | 2022-07-23 10:46:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
|  79 | transect_6-2012-05-03          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2012-05-04 01:43:00 |       58.872  |       -153.212 | 2012-05-03 17:38:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  80 | transect_6-2012-07-30          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2012-07-31 00:40:00 |       58.869  |       -153.225 | 2012-07-30 15:02:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  81 | transect_6-2012-10-28          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2012-10-28 18:55:00 |       58.869  |       -153.225 | 2012-10-28 07:54:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  82 | transect_6-2013-04-19          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2013-04-19 20:50:00 |       58.869  |       -153.225 | 2013-04-19 09:27:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  83 | transect_6-2013-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2013-07-22 03:45:00 |       58.869  |       -153.225 | 2013-07-21 18:28:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  84 | transect_6-2013-11-06          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2013-11-06 17:31:00 |       58.869  |       -153.225 | 2013-11-06 09:07:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  85 | transect_6-2014-04-06          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2014-04-06 17:31:00 |       58.869  |       -153.225 | 2014-04-06 09:18:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  86 | transect_6-2014-07-23          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2014-07-23 20:04:00 |       58.869  |       -153.225 | 2014-07-23 08:40:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  87 | transect_6-2014-10-18          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2014-10-18 09:13:00 |       58.869  |       -153.225 | 2014-10-18 00:27:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  88 | transect_6-2015-02-23          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2015-02-24 00:32:00 |       58.869  |       -153.225 | 2015-02-23 15:26:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  89 | transect_6-2015-04-08          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2015-04-08 04:32:00 |       59.075  |       -152.445 | 2015-04-08 01:00:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  90 | transect_6-2015-08-14          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2015-08-14 12:00:00 |       59.161  |       -152.117 | 2015-08-14 10:33:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  91 | transect_6-2016-02-15          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2016-02-15 18:53:00 |       58.869  |       -153.225 | 2016-02-15 10:19:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  92 | transect_6-2016-04-10          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2016-04-10 15:59:00 |       58.869  |       -153.225 | 2016-04-10 07:45:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  93 | transect_6-2016-08-31          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2016-08-31 19:05:00 |       58.869  |       -153.225 | 2016-08-31 07:41:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  94 | transect_6-2016-12-12          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2016-12-12 22:07:00 |       59.017  |       -152.665 | 2016-12-12 16:55:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  95 | transect_6-2017-04-18          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2017-04-18 22:13:00 |       58.8689 |       -153.24  | 2017-04-18 12:18:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  96 | transect_6-2017-07-26          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2017-07-26 13:02:00 |       59.175  |       -152.062 | 2017-07-26 12:24:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  97 | transect_6-2017-11-02          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2017-11-02 13:08:00 |       59.19   |       -152.007 | 2017-11-02 12:24:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  98 | transect_6-2018-07-18          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2018-07-18 11:50:00 |       59.161  |       -152.117 | 2018-07-18 10:16:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  99 | transect_6-2018-09-17          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2018-09-17 12:23:00 |       59.161  |       -152.117 | 2018-09-17 11:04:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 100 | transect_6-2019-02-08          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2019-02-08 12:32:00 |       59.161  |       -152.117 | 2019-02-08 11:23:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 101 | transect_6-2019-05-12          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2019-05-12 14:43:00 |       58.869  |       -153.225 | 2019-05-12 05:33:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 102 | transect_6-2019-07-25          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2019-07-25 10:43:00 |       59.161  |       -152.117 | 2019-07-25 09:19:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 103 | transect_6-2020-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2020-07-24 10:25:00 |       59.175  |       -152.062 | 2020-07-24 09:23:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 104 | transect_6-2020-09-20          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2020-09-20 10:43:00 |       59.161  |       -152.117 | 2020-09-20 09:27:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 105 | transect_6-2021-02-16          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2021-02-16 12:10:00 |       59.175  |       -152.062 | 2021-02-16 11:22:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 106 | transect_6-2021-04-14          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2021-04-14 16:53:00 |       58.869  |       -153.225 | 2021-04-14 07:06:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 107 | transect_6-2021-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2021-07-21 11:54:00 |       59.175  |       -152.062 | 2021-07-21 10:50:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 108 | transect_6-2021-10-05          | trajectoryProfile | ['temp', 'salt'] |       59.212  |       -151.925 | 2021-10-05 11:40:00 |       59.197  |       -151.98  | 2021-10-05 11:03:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 109 | transect_6-2022-02-28          | trajectoryProfile | ['temp', 'salt'] |       59.205  |       -151.952 | 2022-02-28 11:26:00 |       59.205  |       -151.952 | 2022-02-28 11:26:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 110 | transect_6-2022-04-12          | trajectoryProfile | ['temp', 'salt'] |       59.205  |       -151.952 | 2022-04-12 10:12:00 |       59.205  |       -151.952 | 2022-04-12 10:12:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 111 | transect_6-2022-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.205  |       -151.952 | 2022-07-21 11:11:00 |       59.205  |       -151.952 | 2022-07-21 11:11:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 112 | transect_7-2012-07-30          | trajectoryProfile | ['temp', 'salt'] |       59.335  |       -152.032 | 2012-07-30 11:04:00 |       59.31   |       -152.847 | 2012-07-30 06:53:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 113 | transect_7-2012-10-28          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2012-10-29 02:53:00 |       59.31   |       -153.302 | 2012-10-28 20:01:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 114 | transect_7-2013-04-20          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152     | 2013-04-20 14:03:00 |       59.308  |       -153.302 | 2013-04-20 06:29:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 115 | transect_7-2013-07-18          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2013-07-18 19:56:00 |       59.31   |       -153.302 | 2013-07-18 12:36:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 116 | transect_7-2014-02-17          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.097 | 2014-02-17 12:00:00 |       59.312  |       -153.302 | 2014-02-17 06:14:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 117 | transect_7-2014-04-07          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2014-04-07 09:52:00 |       59.31   |       -153.302 | 2014-04-07 03:17:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 118 | transect_7-2014-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2014-07-24 16:53:00 |       59.31   |       -153.302 | 2014-07-24 08:00:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 119 | transect_7-2014-10-17          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2014-10-17 17:42:00 |       59.31   |       -152.196 | 2014-10-17 16:12:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 120 | transect_7-2014-10-18          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2014-10-18 19:16:00 |       59.31   |       -153.302 | 2014-10-18 12:49:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 121 | transect_7-2015-02-24          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2015-02-24 12:02:00 |       59.31   |       -153.302 | 2015-02-24 05:35:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 122 | transect_7-2015-04-13          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2015-04-13 07:51:00 |       59.31   |       -153.302 | 2015-04-13 01:35:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 123 | transect_7-2015-08-14          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2015-08-14 13:38:00 |       59.31   |       -152.196 | 2015-08-14 12:30:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 124 | transect_7-2016-02-16          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2016-02-16 06:43:00 |       59.31   |       -153.302 | 2016-02-16 00:02:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 125 | transect_7-2016-08-30          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152     | 2016-08-30 15:26:00 |       59.308  |       -153.302 | 2016-08-30 07:43:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 126 | transect_7-2016-12-13          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2016-12-13 11:20:00 |       59.31   |       -152.196 | 2016-12-13 10:09:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 127 | transect_7-2017-04-19          | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152.032 | 2017-04-19 15:57:00 |       59.31   |       -153.302 | 2017-04-19 08:20:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 128 | transect_7-2017-07-26          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.097 | 2017-07-26 11:52:00 |       59.312  |       -152.196 | 2017-07-26 11:10:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 129 | transect_7-2017-11-02          | trajectoryProfile | ['temp', 'salt'] |       59.312  |       -152.032 | 2017-11-02 14:31:00 |       59.31   |       -152.097 | 2017-11-02 14:00:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 130 | transect_7-2018-03-27          | trajectoryProfile | ['temp', 'salt'] |       59.31   |       -152.065 | 2018-03-27 12:51:00 |       59.31   |       -152.065 | 2018-03-27 12:51:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 131 | transect_7-2018-07-18          | trajectoryProfile | ['temp', 'salt'] |       59.313  |       -152.032 | 2018-07-18 13:03:00 |       59.31   |       -152.13  | 2018-07-18 12:26:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 132 | transect_7-2018-09-17          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2018-09-17 13:47:00 |       59.31   |       -152.196 | 2018-09-17 12:57:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 133 | transect_7-2019-02-08          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.065 | 2019-02-08 13:52:00 |       59.31   |       -152.196 | 2019-02-08 13:06:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 134 | transect_7-2019-05-12          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2019-05-12 16:35:00 |       59.31   |       -152.196 | 2019-05-12 15:30:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 135 | transect_7-2019-07-25          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2019-07-25 12:03:00 |       59.31   |       -152.196 | 2019-07-25 11:02:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 136 | transect_7-2019-09-19          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2019-09-19 15:42:00 |       59.31   |       -152.196 | 2019-09-19 14:48:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 137 | transect_7-2020-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2020-07-24 11:43:00 |       59.31   |       -152.196 | 2020-07-24 10:57:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 138 | transect_7-2020-09-20          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2020-09-20 12:09:00 |       59.31   |       -152.196 | 2020-09-20 11:19:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 139 | transect_7-2021-02-16          | trajectoryProfile | ['temp', 'salt'] |       59.315  |       -152.032 | 2021-02-16 13:35:00 |       59.31   |       -152.196 | 2021-02-16 12:44:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 140 | transect_7-2021-04-14          | trajectoryProfile | ['temp', 'salt'] |       59.313  |       -152.032 | 2021-04-14 18:14:00 |       59.31   |       -152.13  | 2021-04-14 17:32:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 141 | transect_7-2021-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.313  |       -152.032 | 2021-07-21 13:01:00 |       59.31   |       -152.13  | 2021-07-21 12:24:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 142 | transect_7-2021-10-05          | trajectoryProfile | ['temp', 'salt'] |       59.312  |       -152.032 | 2021-10-05 12:35:00 |       59.31   |       -152.097 | 2021-10-05 12:05:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 143 | transect_7-2022-02-28          | trajectoryProfile | ['temp', 'salt'] |       59.31   |       -152.065 | 2022-02-28 12:05:00 |       59.31   |       -152.065 | 2022-02-28 12:05:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 144 | transect_7-2022-04-12          | trajectoryProfile | ['temp', 'salt'] |       59.31   |       -152.065 | 2022-04-12 10:52:00 |       59.31   |       -152.065 | 2022-04-12 10:52:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 145 | transect_7-2022-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.31   |       -152.065 | 2022-07-21 11:55:00 |       59.31   |       -152.065 | 2022-07-21 11:55:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 146 | transect_9-2012-02-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-02-14 13:40:00 |       59.5702 |       -151.404 | 2012-02-14 12:31:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 147 | transect_9-2012-03-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-03-14 15:27:00 |       59.5702 |       -151.404 | 2012-03-14 14:05:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 148 | transect_9-2012-04-10          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-04-10 19:17:00 |       59.5702 |       -151.404 | 2012-04-10 18:02:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 149 | transect_9-2012-04-26          | trajectoryProfile | ['temp', 'salt'] |       59.5794 |       -151.357 | 2012-04-26 18:50:00 |       59.5702 |       -151.379 | 2012-04-26 18:03:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 150 | transect_9-2012-05-31_A        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-05-31 14:08:00 |       59.5702 |       -151.404 | 2012-05-31 12:13:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 151 | transect_9-2012-05-31_B        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-05-31 19:22:00 |       59.5702 |       -151.404 | 2012-05-31 17:53:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 152 | transect_9-2012-06-05_A        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-06-05 12:00:00 |       59.5702 |       -151.404 | 2012-06-05 10:16:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 153 | transect_9-2012-06-05_B        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-06-05 18:35:00 |       59.5702 |       -151.404 | 2012-06-05 16:43:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 154 | transect_9-2012-06-27          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-06-27 09:52:00 |       59.5702 |       -151.404 | 2012-06-27 08:32:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 155 | transect_9-2012-07-02          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-07-02 15:28:00 |       59.5702 |       -151.404 | 2012-07-02 14:08:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 156 | transect_9-2012-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-07-21 18:04:00 |       59.5702 |       -151.404 | 2012-07-21 16:41:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 157 | transect_9-2012-08-03          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-08-03 16:45:00 |       59.5702 |       -151.404 | 2012-08-03 15:25:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 158 | transect_9-2012-08-15          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-08-15 15:46:00 |       59.5702 |       -151.404 | 2012-08-15 14:09:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 159 | transect_9-2012-08-26          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-08-26 12:14:00 |       59.5702 |       -151.404 | 2012-08-26 10:55:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 160 | transect_9-2012-08-31          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.362 | 2012-08-31 16:35:00 |       59.5718 |       -151.404 | 2012-08-31 15:14:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 161 | transect_9-2012-09-21_A        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-09-21 10:49:00 |       59.5702 |       -151.404 | 2012-09-21 09:32:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 162 | transect_9-2012-09-21_B        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-09-21 12:13:00 |       59.5702 |       -151.404 | 2012-09-21 11:06:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 163 | transect_9-2012-09-21_C        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-09-21 13:40:00 |       59.5702 |       -151.404 | 2012-09-21 12:27:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 164 | transect_9-2012-09-21_D        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-09-21 15:49:00 |       59.5702 |       -151.404 | 2012-09-21 14:38:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 165 | transect_9-2012-09-21_E        | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-09-21 19:18:00 |       59.5702 |       -151.404 | 2012-09-21 17:32:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 166 | transect_9-2012-10-12          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-10-12 14:10:00 |       59.5702 |       -151.404 | 2012-10-12 12:45:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 167 | transect_9-2012-10-29          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2012-10-29 20:53:00 |       59.5702 |       -151.404 | 2012-10-29 19:10:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 168 | transect_9-2013-01-04          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-01-04 20:12:00 |       59.5702 |       -151.404 | 2013-01-04 18:04:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 169 | transect_9-2013-02-12          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-02-12 11:22:00 |       59.5702 |       -151.404 | 2013-02-12 09:18:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 170 | transect_9-2013-03-15          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-03-15 20:12:00 |       59.5702 |       -151.404 | 2013-03-15 17:58:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 171 | transect_9-2013-04-21          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-04-21 16:18:00 |       59.5702 |       -151.404 | 2013-04-21 14:30:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 172 | transect_9-2013-05-21          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-05-21 13:59:00 |       59.5702 |       -151.404 | 2013-05-21 12:07:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 173 | transect_9-2013-06-06          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-06-06 11:50:00 |       59.5702 |       -151.404 | 2013-06-06 10:12:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 174 | transect_9-2013-06-19          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-06-19 12:42:00 |       59.5702 |       -151.404 | 2013-06-19 10:48:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 175 | transect_9-2013-06-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-06-28 15:09:00 |       59.5702 |       -151.404 | 2013-06-28 13:18:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 176 | transect_9-2013-07-05          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-07-05 16:02:00 |       59.5702 |       -151.404 | 2013-07-05 14:33:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 177 | transect_9-2013-07-09          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-07-09 19:06:00 |       59.5702 |       -151.404 | 2013-07-09 17:17:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 178 | transect_9-2013-07-22          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-07-22 10:16:00 |       59.5702 |       -151.404 | 2013-07-22 09:01:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 179 | transect_9-2013-08-07          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-08-07 16:38:00 |       59.5702 |       -151.404 | 2013-08-07 15:25:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 180 | transect_9-2013-08-30          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-08-30 12:54:00 |       59.5702 |       -151.404 | 2013-08-30 11:15:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 181 | transect_9-2013-09-25          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-09-25 15:13:00 |       59.5702 |       -151.404 | 2013-09-25 13:36:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 182 | transect_9-2013-10-29          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-10-29 10:52:00 |       59.5702 |       -151.404 | 2013-10-29 09:08:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 183 | transect_9-2013-12-03          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2013-12-03 16:02:00 |       59.5702 |       -151.404 | 2013-12-03 14:16:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 184 | transect_9-2014-01-09          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-01-09 15:39:00 |       59.5702 |       -151.404 | 2014-01-09 13:55:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 185 | transect_9-2014-02-15          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-02-15 11:55:00 |       59.5702 |       -151.404 | 2014-02-15 10:24:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 186 | transect_9-2014-03-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-03-28 15:26:00 |       59.5702 |       -151.404 | 2014-03-28 13:43:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 187 | transect_9-2014-04-11          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-04-11 21:00:00 |       59.5702 |       -151.404 | 2014-04-11 19:49:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 188 | transect_9-2014-05-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-05-28 17:20:00 |       59.5702 |       -151.404 | 2014-05-28 15:22:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 189 | transect_9-2014-06-18          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-06-18 18:53:00 |       59.5702 |       -151.404 | 2014-06-18 16:51:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 190 | transect_9-2014-07-21          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-07-21 16:55:00 |       59.5702 |       -151.404 | 2014-07-21 14:44:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 191 | transect_9-2014-08-13          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-08-13 12:37:00 |       59.5702 |       -151.404 | 2014-08-13 10:20:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 192 | transect_9-2014-10-19          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-10-19 11:31:00 |       59.5702 |       -151.404 | 2014-10-19 10:03:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 193 | transect_9-2014-11-25          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-11-25 17:08:00 |       59.5702 |       -151.404 | 2014-11-25 15:40:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 194 | transect_9-2014-12-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2014-12-17 12:50:00 |       59.5702 |       -151.404 | 2014-12-17 11:11:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 195 | transect_9-2015-01-16          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-01-16 15:25:00 |       59.5702 |       -151.404 | 2015-01-16 14:01:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 196 | transect_9-2015-02-12          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-02-12 17:06:00 |       59.5702 |       -151.404 | 2015-02-12 15:45:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 197 | transect_9-2015-02-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.385 | 2015-02-24 19:26:00 |       59.5824 |       -151.404 | 2015-02-24 19:14:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 198 | transect_9-2015-03-31          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-03-31 14:43:00 |       59.5702 |       -151.404 | 2015-03-31 13:07:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 199 | transect_9-2015-04-08          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-04-08 15:26:00 |       59.5702 |       -151.404 | 2015-04-08 14:07:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 200 | transect_9-2015-05-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-05-28 13:29:00 |       59.5702 |       -151.404 | 2015-05-28 11:38:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 201 | transect_9-2015-06-26          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-06-26 12:43:00 |       59.5702 |       -151.404 | 2015-06-26 10:38:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 202 | transect_9-2015-07-10          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-07-10 11:51:00 |       59.5702 |       -151.404 | 2015-07-10 09:48:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 203 | transect_9-2015-07-29          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-07-29 15:18:00 |       59.5702 |       -151.404 | 2015-07-29 13:21:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 204 | transect_9-2015-08-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-08-14 18:30:00 |       59.5702 |       -151.404 | 2015-08-14 16:45:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 205 | transect_9-2015-09-04          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-09-04 11:20:00 |       59.5702 |       -151.404 | 2015-09-04 09:22:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 206 | transect_9-2015-09-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-09-24 14:29:00 |       59.5702 |       -151.404 | 2015-09-24 13:16:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 207 | transect_9-2015-10-19          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-10-19 15:42:00 |       59.5702 |       -151.404 | 2015-10-19 14:12:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 208 | transect_9-2015-11-04          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-11-04 22:31:00 |       59.5702 |       -151.404 | 2015-11-04 20:35:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 209 | transect_9-2015-12-10          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2015-12-10 13:04:00 |       59.5702 |       -151.404 | 2015-12-10 11:42:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 210 | transect_9-2016-01-07          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-01-07 13:36:00 |       59.5702 |       -151.404 | 2016-01-07 12:07:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 211 | transect_9-2016-02-09          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-02-09 15:03:00 |       59.5702 |       -151.404 | 2016-02-09 13:48:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 212 | transect_9-2016-04-07          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-04-07 15:45:00 |       59.5702 |       -151.404 | 2016-04-07 14:05:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 213 | transect_9-2016-05-12          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-05-12 14:23:00 |       59.5702 |       -151.404 | 2016-05-12 12:59:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 214 | transect_9-2016-06-16          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-06-16 13:30:00 |       59.5702 |       -151.404 | 2016-06-16 11:52:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 215 | transect_9-2016-07-27          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-07-27 11:57:00 |       59.5702 |       -151.404 | 2016-07-27 10:18:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 216 | transect_9-2016-09-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-09-23 12:22:00 |       59.5702 |       -151.404 | 2016-09-23 10:40:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 217 | transect_9-2016-10-13          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-10-13 14:11:00 |       59.5702 |       -151.404 | 2016-10-13 12:40:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 218 | transect_9-2016-11-10          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-11-10 15:04:00 |       59.5702 |       -151.404 | 2016-11-10 13:24:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 219 | transect_9-2016-12-13          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2016-12-13 19:10:00 |       59.5702 |       -151.404 | 2016-12-13 17:30:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 220 | transect_9-2017-01-11          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-01-11 14:19:00 |       59.5702 |       -151.404 | 2017-01-11 12:38:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 221 | transect_9-2017-02-07          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-02-07 12:09:00 |       59.5702 |       -151.404 | 2017-02-07 10:36:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 222 | transect_9-2017-03-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-03-28 15:24:00 |       59.5702 |       -151.404 | 2017-03-28 13:50:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 223 | transect_9-2017-04-20          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-04-20 22:51:00 |       59.5702 |       -151.404 | 2017-04-20 21:10:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 224 | transect_9-2017-05-30          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-05-30 13:49:00 |       59.5702 |       -151.404 | 2017-05-30 12:05:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 225 | transect_9-2017-06-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-06-28 13:09:00 |       59.5702 |       -151.404 | 2017-06-28 11:20:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 226 | transect_9-2017-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-07-24 10:54:00 |       59.5702 |       -151.404 | 2017-07-24 09:03:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 227 | transect_9-2017-08-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-08-24 18:32:00 |       59.5702 |       -151.404 | 2017-08-24 16:59:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 228 | transect_9-2017-09-22          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-09-22 16:15:00 |       59.5702 |       -151.404 | 2017-09-22 14:42:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 229 | transect_9-2017-10-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-10-17 15:31:00 |       59.5702 |       -151.404 | 2017-10-17 14:00:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 230 | transect_9-2017-11-07          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-11-07 17:16:00 |       59.5702 |       -151.404 | 2017-11-07 15:47:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 231 | transect_9-2017-12-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2017-12-14 12:07:00 |       59.5702 |       -151.404 | 2017-12-14 10:38:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 232 | transect_9-2018-01-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-01-17 14:54:00 |       59.5702 |       -151.404 | 2018-01-17 13:26:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 233 | transect_9-2018-03-02          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-03-02 16:11:00 |       59.5702 |       -151.404 | 2018-03-02 14:46:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 234 | transect_9-2018-03-27          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-03-27 11:31:00 |       59.5702 |       -151.404 | 2018-03-27 09:56:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 235 | transect_9-2018-04-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-04-23 12:34:00 |       59.5702 |       -151.404 | 2018-04-23 10:52:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 236 | transect_9-2018-05-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-05-24 15:34:00 |       59.5702 |       -151.404 | 2018-05-24 14:07:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 237 | transect_9-2018-06-22          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-06-22 15:07:00 |       59.5702 |       -151.404 | 2018-06-22 13:40:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 238 | transect_9-2018-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-07-24 14:14:00 |       59.5702 |       -151.404 | 2018-07-24 12:43:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 239 | transect_9-2018-08-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-08-23 15:59:00 |       59.5702 |       -151.404 | 2018-08-23 14:14:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 240 | transect_9-2018-09-13          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-09-13 15:35:00 |       59.5702 |       -151.404 | 2018-09-13 14:10:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 241 | transect_9-2018-10-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-10-17 15:51:00 |       59.5702 |       -151.404 | 2018-10-17 14:28:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 242 | transect_9-2018-11-08          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-11-08 15:08:00 |       59.5702 |       -151.404 | 2018-11-08 13:43:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 243 | transect_9-2018-12-06          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2018-12-06 15:48:00 |       59.5702 |       -151.404 | 2018-12-06 14:28:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 244 | transect_9-2019-02-07          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-02-07 16:38:00 |       59.5702 |       -151.404 | 2019-02-07 15:17:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 245 | transect_9-2019-03-19          | trajectoryProfile | ['temp', 'salt'] |       59.5925 |       -151.357 | 2019-03-19 14:41:00 |       59.5702 |       -151.399 | 2019-03-19 13:16:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 246 | transect_9-2019-04-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-04-24 15:17:00 |       59.5702 |       -151.404 | 2019-04-24 13:37:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 247 | transect_9-2019-05-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-05-14 18:41:00 |       59.5702 |       -151.404 | 2019-05-14 17:25:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 248 | transect_9-2019-06-19          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-06-19 17:57:00 |       59.5702 |       -151.404 | 2019-06-19 15:57:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 249 | transect_9-2019-07-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-07-23 17:18:00 |       59.5702 |       -151.404 | 2019-07-23 15:24:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 250 | transect_9-2019-09-16          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-09-16 11:37:00 |       59.5702 |       -151.404 | 2019-09-16 09:29:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 251 | transect_9-2019-10-30          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-10-30 16:08:00 |       59.5702 |       -151.404 | 2019-10-30 14:21:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 252 | transect_9-2019-11-15          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-11-15 17:29:00 |       59.5702 |       -151.404 | 2019-11-15 15:44:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 253 | transect_9-2019-12-12          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2019-12-12 15:32:00 |       59.5702 |       -151.404 | 2019-12-12 14:00:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 254 | transect_9-2020-02-06          | trajectoryProfile | ['temp', 'salt'] |       59.5794 |       -151.357 | 2020-02-06 14:30:00 |       59.5702 |       -151.379 | 2020-02-06 13:55:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 255 | transect_9-2020-03-18          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2020-03-18 15:46:00 |       59.5702 |       -151.404 | 2020-03-18 14:20:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 256 | transect_9-2020-06-04          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2020-06-04 12:39:00 |       59.5702 |       -151.404 | 2020-06-04 11:24:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 257 | transect_9-2020-07-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2020-07-24 14:45:00 |       59.5702 |       -151.404 | 2020-07-24 13:02:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 258 | transect_9-2020-08-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2020-08-14 15:15:00 |       59.5702 |       -151.404 | 2020-08-14 13:47:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 259 | transect_9-2020-09-21          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2020-09-21 11:12:00 |       59.5702 |       -151.404 | 2020-09-21 09:35:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 260 | transect_9-2020-10-15          | trajectoryProfile | ['temp', 'salt'] |       59.5925 |       -151.357 | 2020-10-15 15:43:00 |       59.5702 |       -151.399 | 2020-10-15 14:32:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 261 | transect_9-2020-12-28          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2020-12-28 11:54:00 |       59.5702 |       -151.404 | 2020-12-28 10:50:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 262 | transect_9-2021-01-13          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-01-13 15:24:00 |       59.5702 |       -151.404 | 2021-01-13 14:11:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 263 | transect_9-2021-02-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-02-17 14:47:00 |       59.5702 |       -151.404 | 2021-02-17 13:36:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 264 | transect_9-2021-03-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-03-23 16:30:00 |       59.5702 |       -151.404 | 2021-03-23 15:08:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 265 | transect_9-2021-04-16          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-04-16 17:52:00 |       59.5702 |       -151.404 | 2021-04-16 16:37:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 266 | transect_9-2021-05-06          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-05-06 16:01:00 |       59.5702 |       -151.404 | 2021-05-06 14:42:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 267 | transect_9-2021-06-21          | trajectoryProfile | ['temp', 'salt'] |       59.5925 |       -151.357 | 2021-06-21 15:21:00 |       59.5702 |       -151.399 | 2021-06-21 14:05:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 268 | transect_9-2021-07-16          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-07-16 11:34:00 |       59.5702 |       -151.404 | 2021-07-16 09:37:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 269 | transect_9-2021-08-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-08-17 16:16:00 |       59.5702 |       -151.404 | 2021-08-17 14:45:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 270 | transect_9-2021-09-17          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-09-17 14:37:00 |       59.5702 |       -151.404 | 2021-09-17 13:13:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 271 | transect_9-2021-10-21          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-10-21 16:39:00 |       59.5702 |       -151.404 | 2021-10-21 15:07:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 272 | transect_9-2021-11-14          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-11-14 16:06:00 |       59.5702 |       -151.404 | 2021-11-14 14:33:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 273 | transect_9-2021-12-18          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2021-12-18 15:11:00 |       59.5702 |       -151.404 | 2021-12-18 13:53:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 274 | transect_9-2022-01-31          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-01-31 15:33:00 |       59.5702 |       -151.404 | 2022-01-31 14:08:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 275 | transect_9-2022-03-01          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-03-01 14:36:00 |       59.5702 |       -151.404 | 2022-03-01 13:22:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 276 | transect_9-2022-03-22          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-03-22 13:19:00 |       59.5702 |       -151.404 | 2022-03-22 12:05:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 277 | transect_9-2022-04-13          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-04-13 13:00:00 |       59.5702 |       -151.404 | 2022-04-13 11:57:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 278 | transect_9-2022-05-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-05-23 15:45:00 |       59.5702 |       -151.404 | 2022-05-23 14:38:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 279 | transect_9-2022-06-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-06-24 15:32:00 |       59.5702 |       -151.404 | 2022-06-24 14:19:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 280 | transect_9-2022-07-23          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-07-23 14:34:00 |       59.5702 |       -151.404 | 2022-07-23 13:23:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 281 | transect_9-2022-08-24          | trajectoryProfile | ['temp', 'salt'] |       59.596  |       -151.357 | 2022-08-24 15:06:00 |       59.5702 |       -151.404 | 2022-08-24 14:08:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 282 | transect_AlongBay-2012-08-15   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2012-08-15 11:26:00 |       59.5    |       -151.888 | 2012-08-15 09:35:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 283 | transect_AlongBay-2013-02-12   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2013-02-12 23:59:00 |       59.5    |       -151.888 | 2013-02-12 16:35:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 284 | transect_AlongBay-2013-02-13_A | trajectoryProfile | ['temp', 'salt'] |       59.7203 |       -151.125 | 2013-02-13 00:27:00 |       59.7203 |       -151.125 | 2013-02-13 00:27:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 285 | transect_AlongBay-2013-02-13_B | trajectoryProfile | ['temp', 'salt'] |       59.7203 |       -151.125 | 2013-02-13 00:30:00 |       59.7203 |       -151.125 | 2013-02-13 00:30:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 286 | transect_AlongBay-2013-06-06   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2013-06-06 13:44:00 |       59.5    |       -151.888 | 2013-06-06 12:06:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 287 | transect_AlongBay-2014-03-28   | trajectoryProfile | ['temp', 'salt'] |       59.6583 |       -151.208 | 2014-03-28 17:31:00 |       59.5    |       -151.888 | 2014-03-28 11:56:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 288 | transect_AlongBay-2014-05-28   | trajectoryProfile | ['temp', 'salt'] |       59.632  |       -151.25  | 2014-05-28 14:38:00 |       59.525  |       -151.65  | 2014-05-28 10:49:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 289 | transect_AlongBay-2014-08-14   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2014-08-14 14:25:00 |       59.5    |       -151.888 | 2014-08-14 09:20:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 290 | transect_AlongBay-2015-07-10   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2015-07-10 17:54:00 |       59.445  |       -152     | 2015-07-10 12:43:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 291 | transect_AlongBay-2015-08-14   | trajectoryProfile | ['temp', 'salt'] |       59.563  |       -151.46  | 2015-08-14 16:26:00 |       59.445  |       -152     | 2015-08-14 14:15:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 292 | transect_AlongBay-2016-01-07   | trajectoryProfile | ['temp', 'salt'] |       59.613  |       -151.295 | 2016-01-07 15:56:00 |       59.552  |       -151.53  | 2016-01-07 14:47:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 293 | transect_AlongBay-2016-05-12   | trajectoryProfile | ['temp', 'salt'] |       59.632  |       -151.25  | 2016-05-12 20:00:00 |       59.383  |       -152.05  | 2016-05-12 16:02:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 294 | transect_AlongBay-2016-06-16   | trajectoryProfile | ['temp', 'salt'] |       59.712  |       -151.116 | 2016-06-16 16:36:00 |       59.525  |       -151.65  | 2016-06-16 14:36:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 295 | transect_AlongBay-2016-07-27   | trajectoryProfile | ['temp', 'salt'] |       59.632  |       -151.25  | 2016-07-27 16:50:00 |       59.5    |       -151.888 | 2016-07-27 14:59:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 296 | transect_AlongBay-2017-01-11   | trajectoryProfile | ['temp', 'salt'] |       59.5824 |       -151.385 | 2017-01-11 15:52:00 |       59.525  |       -151.65  | 2017-01-11 15:04:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 297 | transect_AlongBay-2017-02-07   | trajectoryProfile | ['temp', 'salt'] |       59.592  |       -151.35  | 2017-02-07 16:49:00 |       59.5    |       -151.888 | 2017-02-07 13:02:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 298 | transect_AlongBay-2017-03-28   | trajectoryProfile | ['temp', 'salt'] |       59.6583 |       -151.208 | 2017-03-28 13:14:00 |       59.5    |       -151.888 | 2017-03-28 10:49:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 299 | transect_AlongBay-2017-04-20   | trajectoryProfile | ['temp', 'salt'] |       59.613  |       -151.295 | 2017-04-20 20:20:00 |       59.5    |       -151.888 | 2017-04-20 16:57:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 300 | transect_AlongBay-2017-05-30   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2017-05-30 16:37:00 |       59.525  |       -151.65  | 2017-05-30 14:28:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 301 | transect_AlongBay-2017-06-28   | trajectoryProfile | ['temp', 'salt'] |       59.632  |       -151.25  | 2017-06-28 15:27:00 |       59.525  |       -151.65  | 2017-06-28 13:47:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 302 | transect_AlongBay-2017-07-24   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2017-07-24 14:59:00 |       59.525  |       -151.65  | 2017-07-24 12:13:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 303 | transect_AlongBay-2017-07-26   | trajectoryProfile | ['temp', 'salt'] |       59.552  |       -151.53  | 2017-07-26 10:46:00 |       59.383  |       -152.05  | 2017-07-26 09:18:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 304 | transect_AlongBay-2017-08-24   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2017-08-24 16:22:00 |       59.525  |       -151.65  | 2017-08-24 14:03:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 305 | transect_AlongBay-2017-09-22   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2017-09-22 13:26:00 |       59.5    |       -151.888 | 2017-09-22 10:39:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 306 | transect_AlongBay-2017-10-20   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2017-10-20 14:02:00 |       59.518  |       -151.728 | 2017-10-20 11:01:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 307 | transect_AlongBay-2017-11-02   | trajectoryProfile | ['temp', 'salt'] |       59.5824 |       -151.385 | 2017-11-02 17:10:00 |       59.383  |       -152.05  | 2017-11-02 15:04:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 308 | transect_AlongBay-2017-11-07   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2017-11-07 14:55:00 |       59.5    |       -151.888 | 2017-11-07 11:49:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 309 | transect_AlongBay-2017-12-14   | trajectoryProfile | ['temp', 'salt'] |       59.6583 |       -151.208 | 2017-12-14 14:33:00 |       59.525  |       -151.65  | 2017-12-14 12:53:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 310 | transect_AlongBay-2018-01-17   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2018-01-17 12:41:00 |       59.525  |       -151.65  | 2018-01-17 10:45:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 311 | transect_AlongBay-2018-03-02   | trajectoryProfile | ['temp', 'salt'] |       59.6583 |       -151.208 | 2018-03-02 14:15:00 |       59.5    |       -151.888 | 2018-03-02 11:40:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 312 | transect_AlongBay-2018-03-27   | trajectoryProfile | ['temp', 'salt'] |       59.712  |       -151.116 | 2018-03-27 16:38:00 |       59.383  |       -152.05  | 2018-03-27 13:18:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 313 | transect_AlongBay-2018-04-23   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-04-23 18:30:00 |       59.5    |       -151.888 | 2018-04-23 15:40:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 314 | transect_AlongBay-2018-05-24   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-05-24 13:24:00 |       59.5    |       -151.888 | 2018-05-24 10:31:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 315 | transect_AlongBay-2018-06-22   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-06-22 13:06:00 |       59.5    |       -151.888 | 2018-06-22 10:13:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 316 | transect_AlongBay-2018-07-18   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-07-18 16:42:00 |       59.383  |       -152.05  | 2018-07-18 13:19:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 317 | transect_AlongBay-2018-08-23   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-08-23 13:37:00 |       59.5    |       -151.888 | 2018-08-23 10:28:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 318 | transect_AlongBay-2018-09-17   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-09-17 17:35:00 |       59.383  |       -152.05  | 2018-09-17 14:08:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 319 | transect_AlongBay-2018-10-17   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-10-17 13:39:00 |       59.5    |       -151.888 | 2018-10-17 10:33:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 320 | transect_AlongBay-2018-11-08   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-11-08 12:53:00 |       59.552  |       -151.53  | 2018-11-08 10:47:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 321 | transect_AlongBay-2018-12-06   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2018-12-06 13:54:00 |       59.5    |       -151.888 | 2018-12-06 10:53:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 322 | transect_AlongBay-2019-02-07   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-02-07 14:44:00 |       59.552  |       -151.53  | 2019-02-07 12:45:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 323 | transect_AlongBay-2019-03-19   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-03-19 12:34:00 |       59.5    |       -151.888 | 2019-03-19 09:13:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 324 | transect_AlongBay-2019-04-24   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-04-24 12:58:00 |       59.518  |       -151.728 | 2019-04-24 09:58:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 325 | transect_AlongBay-2019-05-14   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-05-14 16:45:00 |       59.5    |       -151.888 | 2019-05-14 14:00:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 326 | transect_AlongBay-2019-06-19   | trajectoryProfile | ['temp', 'salt'] |       59.712  |       -151.116 | 2019-06-19 14:53:00 |       59.5    |       -151.888 | 2019-06-19 11:21:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 327 | transect_AlongBay-2019-07-23   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-07-23 14:36:00 |       59.5    |       -151.888 | 2019-07-23 11:05:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 328 | transect_AlongBay-2019-10-30   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-10-30 13:46:00 |       59.518  |       -151.728 | 2019-10-30 10:43:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 329 | transect_AlongBay-2019-11-15   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2019-11-15 15:06:00 |       59.518  |       -151.728 | 2019-11-15 11:52:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 330 | transect_AlongBay-2019-12-12   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2019-12-12 13:32:00 |       59.518  |       -151.728 | 2019-12-12 10:38:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 331 | transect_AlongBay-2020-02-06   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-02-06 13:20:00 |       59.518  |       -151.728 | 2020-02-06 10:28:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 332 | transect_AlongBay-2020-03-18   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-03-18 13:42:00 |       59.518  |       -151.728 | 2020-03-18 10:27:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 333 | transect_AlongBay-2020-06-04   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-06-04 14:17:00 |       59.5    |       -151.888 | 2020-06-04 09:48:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 334 | transect_AlongBay-2020-07-08   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-07-08 16:53:00 |       59.5824 |       -151.385 | 2020-07-08 15:22:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 335 | transect_AlongBay-2020-07-23   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-07-23 15:00:00 |       59.5    |       -151.888 | 2020-07-23 12:15:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 336 | transect_AlongBay-2020-08-14   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-08-14 13:10:00 |       59.5    |       -151.888 | 2020-08-14 09:56:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 337 | transect_AlongBay-2020-09-20   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-09-20 15:44:00 |       59.383  |       -152.05  | 2020-09-20 12:24:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 338 | transect_AlongBay-2020-10-15   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-10-15 13:59:00 |       59.5    |       -151.888 | 2020-10-15 11:07:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 339 | transect_AlongBay-2020-12-28   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2020-12-28 14:41:00 |       59.525  |       -151.65  | 2020-12-28 12:42:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 340 | transect_AlongBay-2021-01-13   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2021-01-13 13:46:00 |       59.518  |       -151.728 | 2021-01-13 11:20:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 341 | transect_AlongBay-2021-02-16   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2021-02-16 16:43:00 |       59.383  |       -152.05  | 2021-02-16 13:51:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 342 | transect_AlongBay-2021-03-23   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2021-03-23 14:41:00 |       59.518  |       -151.728 | 2021-03-23 11:57:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 343 | transect_AlongBay-2021-04-14   | trajectoryProfile | ['temp', 'salt'] |       59.5824 |       -151.385 | 2021-04-14 22:00:00 |       59.383  |       -152.05  | 2021-04-14 18:52:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 344 | transect_AlongBay-2021-04-16   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2021-04-16 16:11:00 |       59.518  |       -151.728 | 2021-04-16 14:04:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 345 | transect_AlongBay-2021-05-06   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-05-06 13:41:00 |       59.5    |       -151.888 | 2021-05-06 10:19:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 346 | transect_AlongBay-2021-06-21   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-06-21 13:28:00 |       59.518  |       -151.728 | 2021-06-21 10:23:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 347 | transect_AlongBay-2021-07-21   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-07-21 16:51:00 |       59.383  |       -152.05  | 2021-07-21 13:18:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 348 | transect_AlongBay-2021-08-17   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-08-17 14:06:00 |       59.5    |       -151.888 | 2021-08-17 10:30:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 349 | transect_AlongBay-2021-10-04   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-10-04 14:41:00 |       59.5    |       -151.888 | 2021-10-04 11:30:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 350 | transect_AlongBay-2021-10-05   | trajectoryProfile | ['temp', 'salt'] |       59.445  |       -152     | 2021-10-05 13:04:00 |       59.383  |       -152.05  | 2021-10-05 12:50:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 351 | transect_AlongBay-2021-10-21   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-10-21 14:31:00 |       59.518  |       -151.728 | 2021-10-21 10:46:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 352 | transect_AlongBay-2021-11-14   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2021-11-14 13:53:00 |       59.518  |       -151.728 | 2021-11-14 10:32:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 353 | transect_AlongBay-2021-12-18   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2021-12-18 13:30:00 |       59.518  |       -151.728 | 2021-12-18 10:48:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 354 | transect_AlongBay-2022-01-31   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2022-01-31 13:28:00 |       59.518  |       -151.728 | 2022-01-31 10:35:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 355 | transect_AlongBay-2022-02-28   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2022-02-28 15:23:00 |       59.383  |       -152.05  | 2022-02-28 12:23:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 356 | transect_AlongBay-2022-03-21   | trajectoryProfile | ['temp', 'salt'] |       59.687  |       -151.165 | 2022-03-21 16:06:00 |       59.518  |       -151.728 | 2022-03-21 13:33:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 357 | transect_AlongBay-2022-04-12   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2022-04-12 15:13:00 |       59.383  |       -152.05  | 2022-04-12 11:10:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 358 | transect_AlongBay-2022-05-23   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2022-05-23 13:58:00 |       59.5    |       -151.888 | 2022-05-23 10:34:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 359 | transect_AlongBay-2022-06-24   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2022-06-24 13:41:00 |       59.5    |       -151.888 | 2022-06-24 10:12:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 360 | transect_AlongBay-2022-07-21   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2022-07-21 16:24:00 |       59.383  |       -152.05  | 2022-07-21 12:25:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 361 | transect_AlongBay-2022-08-24   | trajectoryProfile | ['temp', 'salt'] |       59.742  |       -151.057 | 2022-08-24 13:20:00 |       59.5    |       -151.888 | 2022-08-24 09:46:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_gwa")("ctd_transects_gwa")
```


### CTD transects

* CTD transects 2002
* 2002
* Slug: ctd_transects_misc_2002
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_misc_2002`

Miscellaneous CTD transects in Cook Inlet from 2002


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset         | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                          |
|---:|:----------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------|
|  0 | Bear_Jul-02     | trajectoryProfile | ['temp', 'salt'] |       59.7535 |       -151.07  | 2002-07-26 17:45:00 |       59.7302 |       -151.123 | 2002-07-26 17:18:00 | https://researchworkspace.com/files/42186319/Bear_Jul-02.csv     |
|  1 | Cohen           | trajectoryProfile | ['temp', 'salt'] |       59.5959 |       -151.415 | 2002-07-24 18:28:00 |       59.5392 |       -151.481 | 2002-07-24 17:24:00 | https://researchworkspace.com/files/42186397/Cohen.csv           |
|  2 | Glacier         | trajectoryProfile | ['temp', 'salt'] |       59.6954 |       -151.196 | 2002-07-26 19:22:00 |       59.6519 |       -151.258 | 2002-07-26 18:46:00 | https://researchworkspace.com/files/42199559/Glacier.csv         |
|  3 | Peterson_Jul-02 | trajectoryProfile | ['temp', 'salt'] |       59.6012 |       -151.274 | 2002-07-24 17:12:00 |       59.5977 |       -151.407 | 2002-07-24 15:48:00 | https://researchworkspace.com/files/42199566/Peterson_Jul-02.csv |
|  4 | PtAdam_jul-02   | trajectoryProfile | ['temp', 'salt'] |       59.2591 |       -152.001 | 2002-07-28 23:09:00 |       59.2559 |       -152.097 | 2002-07-28 22:27:00 | https://researchworkspace.com/files/42200000/PtAdam_jul-02.csv   |
|  5 | pogibshi_Jul-02 | trajectoryProfile | ['temp', 'salt'] |       59.7455 |       -151.866 | 2002-07-25 19:57:00 |       59.4259 |       -151.892 | 2002-07-25 16:08:00 | https://researchworkspace.com/files/42199989/pogibshi_Jul-02.csv |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_misc_2002")("ctd_transects_misc_2002")
```


### CTD Transect (OTF KBNERR): Repeated from Anchor Point

* CTD profiles 2003-2006 - OTF KBNERR
* Daily in July, 2003 to 2006
* Slug: ctd_transects_otf_kbnerr
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_otf_kbnerr`

CTD Transect Across Anchor Point, for GEM Project 030670.

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf
Project description: https://evostc.state.ak.us/restoration-projects/project-search/monitoring-dynamics-of-the-alaska-coastal-current-and-development-of-applications-for-management-of-cook-inlet-salmon-040670/


Notes:

These data were not included in the NWGOA model/data comparison

````{div} full-width
```{dropdown} Dataset metadata

|     | Dataset    | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                        |
|----:|:-----------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:---------------------------------------------------------------|
|   0 | 2003-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-01 18:35:00 |       59.825  |       -152.438 | 2003-07-01 12:02:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   1 | 2003-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-02 12:03:00 |       59.825  |       -152.438 | 2003-07-02 06:40:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   2 | 2003-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-04 17:02:00 |       59.825  |       -152.438 | 2003-07-04 12:00:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   3 | 2003-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-05 13:05:00 |       59.825  |       -152.438 | 2003-07-05 07:51:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   4 | 2003-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-06 21:59:00 |       59.825  |       -152.438 | 2003-07-06 16:00:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   5 | 2003-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-07 11:27:00 |       59.825  |       -152.438 | 2003-07-07 06:22:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   6 | 2003-07-08 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-08 15:55:00 |       59.825  |       -152.438 | 2003-07-08 10:14:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   7 | 2003-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-09 11:54:00 |       59.825  |       -152.438 | 2003-07-09 05:43:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   8 | 2003-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-10 17:04:00 |       59.825  |       -152.438 | 2003-07-10 10:21:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   9 | 2003-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-11 12:50:00 |       59.825  |       -152.438 | 2003-07-11 06:36:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  10 | 2003-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-12 16:26:00 |       59.825  |       -152.438 | 2003-07-12 10:24:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  11 | 2003-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-13 13:10:00 |       59.825  |       -152.438 | 2003-07-13 06:05:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  12 | 2003-07-14 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-14 20:00:00 |       59.825  |       -152.438 | 2003-07-14 12:43:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  13 | 2003-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.225 | 2003-07-15 13:39:00 |       59.8367 |       -152.438 | 2003-07-15 07:03:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  14 | 2003-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2003-07-16 17:56:00 |       59.825  |       -152.367 | 2003-07-16 12:24:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  15 | 2003-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-17 13:07:00 |       59.825  |       -152.438 | 2003-07-17 06:54:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  16 | 2003-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-18 19:23:00 |       59.825  |       -152.438 | 2003-07-18 13:05:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  17 | 2003-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.438 | 2003-07-19 05:59:00 |       59.8733 |       -152.438 | 2003-07-19 05:59:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  18 | 2003-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-21 10:34:00 |       59.825  |       -152.438 | 2003-07-21 04:48:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  19 | 2003-07-22 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-22 15:54:00 |       59.825  |       -152.438 | 2003-07-22 10:26:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  20 | 2003-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-23 12:57:00 |       59.825  |       -152.438 | 2003-07-23 07:00:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  21 | 2003-07-24 | trajectoryProfile | ['temp', 'salt'] |       59.8567 |       -152.152 | 2003-07-24 14:00:00 |       59.825  |       -152.33  | 2003-07-24 10:45:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  22 | 2003-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-25 12:17:00 |       59.825  |       -152.438 | 2003-07-25 06:17:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  23 | 2003-07-26 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-26 16:19:00 |       59.825  |       -152.438 | 2003-07-26 10:29:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  24 | 2003-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-28 17:06:00 |       59.825  |       -152.438 | 2003-07-28 10:52:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  25 | 2003-07-29 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-29 10:15:00 |       59.825  |       -152.438 | 2003-07-29 04:58:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  26 | 2003-07-30 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-30 14:11:00 |       59.825  |       -152.438 | 2003-07-30 09:32:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  27 | 2004-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.225 | 2004-07-01 13:26:00 |       59.8367 |       -152.438 | 2004-07-01 08:37:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  28 | 2004-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-02 11:18:00 |       59.825  |       -152.438 | 2004-07-02 04:46:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  29 | 2004-07-03 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-03 15:49:00 |       59.825  |       -152.438 | 2004-07-03 10:50:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  30 | 2004-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-04 10:19:00 |       59.825  |       -152.438 | 2004-07-04 05:25:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  31 | 2004-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-05 16:34:00 |       59.825  |       -152.438 | 2004-07-05 10:34:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  32 | 2004-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-06 18:23:00 |       59.825  |       -152.438 | 2004-07-06 13:37:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  33 | 2004-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-07 10:01:00 |       59.825  |       -152.438 | 2004-07-07 04:56:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  34 | 2004-07-08 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-08 17:05:00 |       59.825  |       -152.438 | 2004-07-08 10:41:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  35 | 2004-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-09 10:21:00 |       59.825  |       -152.438 | 2004-07-09 04:53:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  36 | 2004-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-10 15:20:00 |       59.825  |       -152.438 | 2004-07-10 09:16:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  37 | 2004-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-11 11:51:00 |       59.825  |       -152.438 | 2004-07-11 05:41:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  38 | 2004-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-12 15:39:00 |       59.825  |       -152.438 | 2004-07-12 10:23:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  39 | 2004-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-13 12:44:00 |       59.825  |       -152.438 | 2004-07-13 05:48:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  40 | 2004-07-14 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2004-07-14 23:48:00 |       59.825  |       -152.367 | 2004-07-14 11:31:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  41 | 2004-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-15 12:35:00 |       59.825  |       -152.438 | 2004-07-15 00:46:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  42 | 2004-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-16 18:05:00 |       59.825  |       -152.438 | 2004-07-16 10:56:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  43 | 2004-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-17 10:55:00 |       59.825  |       -152.438 | 2004-07-17 05:01:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  44 | 2004-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-18 17:16:00 |       59.825  |       -152.438 | 2004-07-18 10:52:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  45 | 2004-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-19 10:43:00 |       59.825  |       -152.438 | 2004-07-19 05:11:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  46 | 2004-07-20 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2004-07-20 15:36:00 |       59.825  |       -152.367 | 2004-07-20 11:14:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  47 | 2004-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-21 10:26:00 |       59.825  |       -152.438 | 2004-07-21 05:27:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  48 | 2004-07-22 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-22 17:38:00 |       59.825  |       -152.438 | 2004-07-22 11:11:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  49 | 2004-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-23 11:33:00 |       59.825  |       -152.438 | 2004-07-23 06:30:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  50 | 2004-07-24 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-24 16:29:00 |       59.825  |       -152.438 | 2004-07-24 10:19:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  51 | 2004-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-25 11:33:00 |       59.825  |       -152.438 | 2004-07-25 06:09:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  52 | 2004-07-27 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-27 16:42:00 |       59.825  |       -152.438 | 2004-07-27 10:16:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  53 | 2004-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-28 12:50:00 |       59.825  |       -152.438 | 2004-07-28 07:00:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  54 | 2004-07-29 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-29 16:23:00 |       59.825  |       -152.438 | 2004-07-29 10:32:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  55 | 2004-07-30 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-30 11:19:00 |       59.825  |       -152.438 | 2004-07-30 04:39:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  56 | 2005-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-01 21:05:00 |       59.825  |       -152.438 | 2005-07-01 14:15:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  57 | 2005-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-02 14:22:00 |       59.825  |       -152.438 | 2005-07-02 06:52:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  58 | 2005-07-03 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-03 19:16:00 |       59.825  |       -152.438 | 2005-07-03 12:56:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  59 | 2005-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-04 13:45:00 |       59.825  |       -152.438 | 2005-07-04 05:56:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  60 | 2005-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-05 21:15:00 |       59.825  |       -152.438 | 2005-07-05 12:58:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  61 | 2005-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-06 14:45:00 |       59.825  |       -152.438 | 2005-07-06 06:30:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  62 | 2005-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-07 21:07:00 |       59.825  |       -152.438 | 2005-07-07 12:29:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  63 | 2005-07-08 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-08 13:25:00 |       59.825  |       -152.438 | 2005-07-08 05:58:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  64 | 2005-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-09 18:33:00 |       59.825  |       -152.438 | 2005-07-09 11:22:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  65 | 2005-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.293 | 2005-07-10 10:43:00 |       59.85   |       -152.438 | 2005-07-10 06:59:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  66 | 2005-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-11 17:21:00 |       59.825  |       -152.438 | 2005-07-11 10:16:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  67 | 2005-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-12 14:28:00 |       59.825  |       -152.438 | 2005-07-12 07:22:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  68 | 2005-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-13 18:21:00 |       59.825  |       -152.438 | 2005-07-13 12:06:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  69 | 2005-07-14 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-14 12:30:00 |       59.825  |       -152.438 | 2005-07-14 06:42:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  70 | 2005-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-15 19:20:00 |       59.825  |       -152.438 | 2005-07-15 12:05:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  71 | 2005-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-16 13:56:00 |       59.825  |       -152.438 | 2005-07-16 07:54:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  72 | 2005-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-17 15:55:00 |       59.825  |       -152.438 | 2005-07-17 10:46:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  73 | 2005-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-18 11:23:00 |       59.825  |       -152.438 | 2005-07-18 05:38:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  74 | 2005-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-19 18:26:00 |       59.825  |       -152.438 | 2005-07-19 12:25:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  75 | 2005-07-20 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-20 15:54:00 |       59.825  |       -152.438 | 2005-07-20 07:41:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  76 | 2005-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-21 16:22:00 |       59.825  |       -152.438 | 2005-07-21 09:51:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  77 | 2005-07-22 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-22 13:36:00 |       59.825  |       -152.438 | 2005-07-22 05:40:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  78 | 2005-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-23 18:26:00 |       59.825  |       -152.438 | 2005-07-23 11:16:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  79 | 2005-07-24 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-24 14:14:00 |       59.825  |       -152.438 | 2005-07-24 06:23:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  80 | 2005-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-25 18:21:00 |       59.825  |       -152.438 | 2005-07-25 11:11:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  81 | 2005-07-26 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-26 14:00:00 |       59.825  |       -152.438 | 2005-07-26 06:32:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  82 | 2005-07-27 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-27 19:14:00 |       59.825  |       -152.438 | 2005-07-27 13:43:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  83 | 2005-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-28 12:45:00 |       59.825  |       -152.438 | 2005-07-28 06:37:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  84 | 2005-07-29 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-29 17:02:00 |       59.825  |       -152.438 | 2005-07-29 10:13:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  85 | 2005-07-30 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-30 15:37:00 |       59.825  |       -152.438 | 2005-07-30 06:55:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  86 | 2006-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-01 16:37:00 |       59.825  |       -152.438 | 2006-07-01 11:14:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  87 | 2006-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-02 11:40:00 |       59.825  |       -152.438 | 2006-07-02 06:38:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  88 | 2006-07-03 | trajectoryProfile | ['temp', 'salt'] |       59.825  |       -152.152 | 2006-07-03 09:29:00 |       59.825  |       -152.152 | 2006-07-03 09:29:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  89 | 2006-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2006-07-04 11:52:00 |       59.825  |       -152.367 | 2006-07-04 07:48:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  90 | 2006-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2006-07-05 14:21:00 |       59.825  |       -152.367 | 2006-07-05 10:06:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  91 | 2006-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8567 |       -152.152 | 2006-07-06 12:11:00 |       59.825  |       -152.33  | 2006-07-06 08:06:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  92 | 2006-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-07 14:15:00 |       59.825  |       -152.438 | 2006-07-07 08:15:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  93 | 2006-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-09 16:09:00 |       59.825  |       -152.438 | 2006-07-09 09:57:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  94 | 2006-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-10 12:29:00 |       59.825  |       -152.438 | 2006-07-10 06:37:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  95 | 2006-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-11 14:20:00 |       59.825  |       -152.438 | 2006-07-11 08:43:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  96 | 2006-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-12 12:17:00 |       59.825  |       -152.438 | 2006-07-12 05:45:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  97 | 2006-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-13 15:48:00 |       59.825  |       -152.438 | 2006-07-13 10:11:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  98 | 2006-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.825  |       -152.152 | 2006-07-15 09:21:00 |       59.825  |       -152.152 | 2006-07-15 09:21:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  99 | 2006-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-16 16:34:00 |       59.825  |       -152.438 | 2006-07-16 10:40:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 100 | 2006-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-17 13:08:00 |       59.825  |       -152.438 | 2006-07-17 07:27:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 101 | 2006-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-18 13:59:00 |       59.825  |       -152.438 | 2006-07-18 08:14:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 102 | 2006-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.367 | 2006-07-19 08:28:00 |       59.8617 |       -152.438 | 2006-07-19 07:23:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 103 | 2006-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-21 16:14:00 |       59.825  |       -152.438 | 2006-07-21 09:43:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 104 | 2006-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8367 |       -152.152 | 2006-07-23 09:59:00 |       59.825  |       -152.225 | 2006-07-23 08:47:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 105 | 2006-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-25 19:30:00 |       59.825  |       -152.438 | 2006-07-25 12:55:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 106 | 2006-07-26 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-26 12:10:00 |       59.825  |       -152.438 | 2006-07-26 06:09:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 107 | 2006-07-27 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-27 17:29:00 |       59.825  |       -152.438 | 2006-07-27 11:08:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 108 | 2006-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.438 | 2006-07-28 07:24:00 |       59.8733 |       -152.438 | 2006-07-28 07:24:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_otf_kbnerr")("ctd_transects_otf_kbnerr")
```


### CTD Transects (UAF): Repeated in central Cook Inlet

* CTD time series UAF
* 26-hour period on 9-10 August 2003
* Slug: ctd_transects_uaf
* Included: True
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:ctd_transects_uaf`

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles

Surface-to-bottom measurements of temperature, salinity, and transmissivity, as well as measurements of surface currents (vessel drift speeds) were acquired along an east-west section in central Cook Inlet, Alaska during a 26-hour period on 9-10 August 2003. These measurements are used to describe the evolution of frontal features (tide rips) and physical properties along this section during semidiurnal and diurnal tidal cycles. The observation that the amplitude of surface currents is a function of water depth is used to show that strong frontal features occur in association with steep bathymetry. The positions and strengths of these fronts vary with the semidiurnal tide. The presence of freshwater gradients alters the phase and duration of tidal currents across the section. Where mean density-driven flow is northward (along the eastern shore and near Kalgin Island), the onset of northward tidal flow (flood tide) occurs earlier and has longer duration than the onset and duration of northward tidal flow where mean density-driven flow is southward (in the shipping channel). Conversely, where mean density-driven flow is southward (in the shipping channel), the onset of southward tidal flow (ebb tide) occurs earlier and has longer duration than the onset and duration of southward tidal flow along the eastern shore and near Kalgin Island. 

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles
Stephen R. Okkonen
Institute of Marine Science
University of Alaska Fairbanks
Report: https://www.circac.org/wp-content/uploads/Okkonen_2005_hydrography-and-currents-in-Cook-Inlet.pdf


Notes:

Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset     | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                         |
|---:|:------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------------|
|  0 | Transect_01 | trajectoryProfile | ['temp', 'salt'] |       60.4837 |       -151.3   | 2003-08-09 23:03:00 |       60.4815 |       -151.8   | 2003-08-09 20:36:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  1 | Transect_02 | trajectoryProfile | ['temp', 'salt'] |       60.4843 |       -151.301 | 2003-08-10 01:25:00 |       60.4816 |       -151.765 | 2003-08-09 23:12:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  2 | Transect_03 | trajectoryProfile | ['temp', 'salt'] |       60.4842 |       -151.336 | 2003-08-10 04:06:00 |       60.4827 |       -151.8   | 2003-08-10 01:35:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  3 | Transect_04 | trajectoryProfile | ['temp', 'salt'] |       60.4858 |       -151.3   | 2003-08-10 07:06:00 |       60.4823 |       -151.766 | 2003-08-10 04:14:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  4 | Transect_05 | trajectoryProfile | ['temp', 'salt'] |       60.4836 |       -151.334 | 2003-08-10 10:02:00 |       60.4827 |       -151.799 | 2003-08-10 07:16:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  5 | Transect_06 | trajectoryProfile | ['temp', 'salt'] |       60.4833 |       -151.3   | 2003-08-10 12:37:00 |       60.4825 |       -151.766 | 2003-08-10 10:11:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  6 | Transect_07 | trajectoryProfile | ['temp', 'salt'] |       60.4842 |       -151.3   | 2003-08-10 16:58:00 |       60.4823 |       -151.8   | 2003-08-10 14:01:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  7 | Transect_08 | trajectoryProfile | ['temp', 'salt'] |       60.4845 |       -151.3   | 2003-08-10 20:17:00 |       60.482  |       -151.767 | 2003-08-10 17:09:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  8 | Transect_09 | trajectoryProfile | ['temp', 'salt'] |       60.484  |       -151.317 | 2003-08-10 22:59:00 |       60.4827 |       -151.8   | 2003-08-10 20:26:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |

```
````

+++




**Map of CTD Transects**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_uaf")("ctd_transects_uaf")
```


### HF Radar (UAF)

* HF Radar - UAF
* 2002-2009
* Slug: hfradar
* Included: True
* Feature type: grid
* See the full dataset page for more information: {ref}`page:hfradar`

HF Radar from UAF.

Files are:
* Upper Cook Inlet (System A): 2002-2003 and 2009
* Lower Cook Inlet (System B): 2006-2007

Data variables available include tidally filtered and weekly averaged along with tidal constituents calculated from hourly data.
    
Some of the data is written up in reports:
* https://espis.boem.gov/final%20reports/5009.pdf
* https://www.govinfo.gov/app/details/GOVPUB-I-47b721482d69e308aec1cca9b3e51955

Data set up:
![pic](https://researchworkspace.com/files/40338104/UAcoverage.gif)


Notes:

These are accessed from Research Workspace where they have already been processed.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                              | featuretype   | key_variables   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                                          |
|---:|:-------------------------------------|:--------------|:----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------------------------------------------|
|  0 | lower-ci_system-B_2006-2007          | grid          | []              |       60.0411 |       -151.899 | 2007-11-11 00:00:00 |       59.1251 |       -153.23  | 2006-11-12 00:00:00 | https://researchworkspace.com/files/42394327/lower-ci_system-B_2006-2007_subtidal_weekly_mean.nc |
|  1 | lower-ci_system-B_2006-2007_tidecons | grid          | nan             |      nan      |        nan     | nan                 |      nan      |        nan     | nan                 | https://researchworkspace.com/files/42393598/lower-ci_system-B_2006-2007_tidecons.nc             |
|  2 | upper-ci_system-A_2002-2003          | grid          | []              |       60.7497 |       -151.358 | 2003-06-15 00:00:00 |       60.2635 |       -152.126 | 2002-12-08 00:00:00 | https://researchworkspace.com/files/42394322/upper-ci_system-A_2002-2003_subtidal_weekly_mean.nc |
|  3 | upper-ci_system-A_2002-2003_tidecons | grid          | nan             |      nan      |        nan     | nan                 |      nan      |        nan     | nan                 | https://researchworkspace.com/files/42393592/upper-ci_system-A_2002-2003_tidecons.nc             |
|  4 | upper-ci_system-A_2009               | grid          | []              |       60.7716 |       -151.378 | 2009-06-07 00:00:00 |       60.2321 |       -152.378 | 2009-04-19 00:00:00 | https://researchworkspace.com/files/42394329/upper-ci_system-A_2009_subtidal_weekly_mean.nc      |
|  5 | upper-ci_system-A_2009_tidecons      | grid          | nan             |      nan      |        nan     | nan                 |      nan      |        nan     | nan                 | https://researchworkspace.com/files/42393604/upper-ci_system-A_2009_tidecons.nc                  |

```
````

+++




**Map of HF Radar Data Areas**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "hfradar")("hfradar")
```


### Moorings (CDIP): Lower and Central Cook Inlet, Kodiak Island

* Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP)
* From 2011 to 2023, variable
* Slug: moorings_aoos_cdip
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_aoos_cdip`

Moorings from AOOS/CDIP


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                | datasetID              | featuretype   | griddap   | info_url                                                             | institution                          | key_variables   |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                             | tabledap                                                       | title                                                | urlpath                                                        |
|---:|:-----------------------|:-----------------------|:--------------|:----------|:---------------------------------------------------------------------|:-------------------------------------|:----------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:----------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:-----------------------------------------------------|:---------------------------------------------------------------|
|  0 | aoos_204               | aoos_204               | timeSeries    |           | https://erddap.aoos.org/erddap/info/aoos_204/index.csv               | Alaska Ocean Observing System (AOOS) | ['temp']        |       59.5973 |       -151.829 | 2023-09-05 15:45:00+00:00 |       59.5973 |       -151.829 | 2013-07-21 19:22:27+00:00 | Timeseries data from 'Lower Cook Inlet, AK, CDIP Wave and Current Buoy 204' (aoos_204)              | https://erddap.aoos.org/erddap/tabledap/aoos_204               | Lower Cook Inlet, AK, CDIP Wave and Current Buoy 204 | https://erddap.aoos.org/erddap/tabledap/aoos_204               |
|  1 | central-cook-inlet-175 | central-cook-inlet-175 | timeSeries    |           | https://erddap.aoos.org/erddap/info/central-cook-inlet-175/index.csv | Alaska Ocean Observing System (AOOS) | ['temp']        |       59.7335 |       -152.005 | 2013-01-03 06:54:07+00:00 |       59.7335 |       -152.005 | 2011-05-09 23:00:27+00:00 | Timeseries data from 'Central Cook Inlet, AK, Historic CDIP Wave Buoy 175' (central-cook-inlet-175) | https://erddap.aoos.org/erddap/tabledap/central-cook-inlet-175 | Central Cook Inlet, AK, Historic CDIP Wave Buoy 175  | https://erddap.aoos.org/erddap/tabledap/central-cook-inlet-175 |
|  2 | edu_ucsd_cdip_236      | edu_ucsd_cdip_236      | timeSeries    |           | https://erddap.aoos.org/erddap/info/edu_ucsd_cdip_236/index.csv      | Alaska Ocean Observing System (AOOS) | ['temp']        |       57.4795 |       -151.695 | 2021-09-25 17:58:20+00:00 |       57.4795 |       -151.695 | 2017-09-28 22:00:00+00:00 | Timeseries data from 'Kodiak, AK, CDIP Wave Buoy 236' (edu_ucsd_cdip_236)                           | https://erddap.aoos.org/erddap/tabledap/edu_ucsd_cdip_236      | Kodiak, AK, CDIP Wave Buoy 236                       | https://erddap.aoos.org/erddap/tabledap/edu_ucsd_cdip_236      |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_aoos_cdip")("moorings_aoos_cdip")
```


### Moorings (KBNERR): Kachemak Bay: Bear Cove, Seldovia

* Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* From 2004 to present day, variable
* Slug: moorings_kbnerr_bear_cove_seldovia
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_kbnerr_bear_cove_seldovia`

Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
* nerrs_kacsdwq :: kacsdwq
* nerrs_kacsswq :: kacsswq

* cdmo_nerrs_bearcove :: This is a different station than kacbcwq, which was active 2002-2003 while this is in 2015. They are also in different locations.
    
More information: https://accs.uaa.alaska.edu/kbnerr/


Notes:

These are accessed through AOOS portal/ERDDAP server.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset             | datasetID           | featuretype   | griddap   | info_url                                                          | institution                                               | key_variables           |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                    | tabledap                                                    | title                               | urlpath                                                     |
|---:|:--------------------|:--------------------|:--------------|:----------|:------------------------------------------------------------------|:----------------------------------------------------------|:------------------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:---------------------------------------------------------------------------|:------------------------------------------------------------|:------------------------------------|:------------------------------------------------------------|
|  0 | cdmo_nerrs_bearcove | cdmo_nerrs_bearcove | timeSeries    |           | https://erddap.aoos.org/erddap/info/cdmo_nerrs_bearcove/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | ['temp', 'salt']        |       59.7262 |       -151.049 | 2015-11-20 17:15:00+00:00 |       59.7262 |       -151.049 | 2015-05-05 14:00:00+00:00 | Timeseries data from 'Bear Cove Water Quality' (cdmo_nerrs_bearcove)       | https://erddap.aoos.org/erddap/tabledap/cdmo_nerrs_bearcove | Bear Cove Water Quality             | https://erddap.aoos.org/erddap/tabledap/cdmo_nerrs_bearcove |
|  1 | nerrs_kacsdwq       | nerrs_kacsdwq       | timeSeries    |           | https://erddap.aoos.org/erddap/info/nerrs_kacsdwq/index.csv       | Kachemak Bay National Estuarine Research Reserve (KBNERR) | ['ssh', 'temp', 'salt'] |       59.441  |       -151.721 | 2023-09-05 16:45:00+00:00 |       59.441  |       -151.721 | 2004-01-01 09:00:00+00:00 | Timeseries data from 'Seldovia Deep Water Quality (SEQA2)' (nerrs_kacsdwq) | https://erddap.aoos.org/erddap/tabledap/nerrs_kacsdwq       | Seldovia Deep Water Quality (SEQA2) | https://erddap.aoos.org/erddap/tabledap/nerrs_kacsdwq       |
|  2 | nerrs_kacsswq       | nerrs_kacsswq       | timeSeries    |           | https://erddap.aoos.org/erddap/info/nerrs_kacsswq/index.csv       | Kachemak Bay National Estuarine Research Reserve (KBNERR) | ['ssh', 'temp', 'salt'] |       59.441  |       -151.721 | 2023-07-10 19:30:00+00:00 |       59.441  |       -151.721 | 2004-01-01 09:00:00+00:00 | Timeseries data from 'Seldovia Surface Water Quality' (nerrs_kacsswq)      | https://erddap.aoos.org/erddap/tabledap/nerrs_kacsswq       | Seldovia Surface Water Quality      | https://erddap.aoos.org/erddap/tabledap/nerrs_kacsswq       |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_bear_cove_seldovia")("moorings_kbnerr_bear_cove_seldovia")
```


### Moorings (KBNERR): Historical, Kachemak Bay

* Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* From 2001 to 2003, variable
* Slug: moorings_kbnerr_historical
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_kbnerr_historical`

Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
More information: https://accs.uaa.alaska.edu/kbnerr/


Notes:

These are accessed from Research Workspace.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset   | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                            |
|---:|:----------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------------|
|  0 | kacbcwq   | timeSeries    | ['temp', 'salt'] |       59.7057 |       -151.109 | 2003-09-24 17:30:00 |       59.7057 |       -151.109 | 2002-06-18 11:30:00 | https://researchworkspace.com/files/42202441/kacbcwq_subsetted.csv |
|  1 | kacdlwq   | timeSeries    | ['temp', 'salt'] |       59.6023 |       -151.41  | 2002-12-31 23:30:00 |       59.6023 |       -151.41  | 2002-10-24 10:00:00 | https://researchworkspace.com/files/42202443/kacdlwq_subsetted.csv |
|  2 | kachowq   | timeSeries    | ['temp', 'salt'] |       59.6023 |       -151.41  | 2002-11-20 12:30:00 |       59.6023 |       -151.41  | 2001-07-12 07:45:00 | https://researchworkspace.com/files/42202445/kachowq_subsetted.csv |
|  3 | kacpgwq   | timeSeries    | ['temp', 'salt'] |       59.3705 |       -151.896 | 2003-09-24 15:30:00 |       59.3705 |       -151.896 | 2002-06-21 10:00:00 | https://researchworkspace.com/files/42202447/kacpgwq_subsetted.csv |
|  4 | kacsewq   | timeSeries    | ['temp', 'salt'] |       59.441  |       -151.721 | 2003-12-31 23:30:00 |       59.441  |       -151.721 | 2001-08-17 15:15:00 | https://researchworkspace.com/files/42202449/kacsewq_subsetted.csv |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_historical")("moorings_kbnerr_historical")
```


### Moorings (KBNERR): Kachemak Bay, Homer stations

* Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* From 2003 to present day, variable
* Slug: moorings_kbnerr_homer
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_kbnerr_homer`

Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
* nerrs_kachdwq :: kachdwq
* homer-dolphin-surface-water-q :: kachswq
* nerrs_kach3wq :: kach3wq
    
More information: https://accs.uaa.alaska.edu/kbnerr/


Notes:

These are accessed through AOOS portal/ERDDAP server.

````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                       | datasetID                     | featuretype   | griddap   | info_url                                                                    | institution                                               | key_variables           |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                                 | tabledap                                                              | title                                            | urlpath                                                               |
|---:|:------------------------------|:------------------------------|:--------------|:----------|:----------------------------------------------------------------------------|:----------------------------------------------------------|:------------------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:--------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-------------------------------------------------|:----------------------------------------------------------------------|
|  0 | homer-dolphin-surface-water-q | homer-dolphin-surface-water-q | timeSeries    |           | https://erddap.aoos.org/erddap/info/homer-dolphin-surface-water-q/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | ['ssh', 'temp', 'salt'] |        59.602 |       -151.409 | 2011-11-29 01:00:00+00:00 |        59.602 |       -151.409 | 2004-02-13 18:30:00+00:00 | Timeseries data from 'Homer Dolphin Surface Water Quality (Historical)' (homer-dolphin-surface-water-q) | https://erddap.aoos.org/erddap/tabledap/homer-dolphin-surface-water-q | Homer Dolphin Surface Water Quality (Historical) | https://erddap.aoos.org/erddap/tabledap/homer-dolphin-surface-water-q |
|  1 | nerrs_kach3wq                 | nerrs_kach3wq                 | timeSeries    |           | https://erddap.aoos.org/erddap/info/nerrs_kach3wq/index.csv                 | Kachemak Bay National Estuarine Research Reserve (KBNERR) | ['ssh', 'temp', 'salt'] |        59.602 |       -151.409 | 2023-08-07 19:45:00+00:00 |        59.602 |       -151.409 | 2012-05-31 21:15:00+00:00 | Timeseries data from 'Homer Surface 3 Water Quality' (nerrs_kach3wq)                                    | https://erddap.aoos.org/erddap/tabledap/nerrs_kach3wq                 | Homer Surface 3 Water Quality                    | https://erddap.aoos.org/erddap/tabledap/nerrs_kach3wq                 |
|  2 | nerrs_kachdwq                 | nerrs_kachdwq                 | timeSeries    |           | https://erddap.aoos.org/erddap/info/nerrs_kachdwq/index.csv                 | Kachemak Bay National Estuarine Research Reserve (KBNERR) | ['ssh', 'temp', 'salt'] |        59.602 |       -151.409 | 2023-09-05 16:15:00+00:00 |        59.602 |       -151.409 | 2003-01-01 09:00:00+00:00 | Timeseries data from 'Homer Dolphin Deep Water Quality (KCHA2)' (nerrs_kachdwq)                         | https://erddap.aoos.org/erddap/tabledap/nerrs_kachdwq                 | Homer Dolphin Deep Water Quality (KCHA2)         | https://erddap.aoos.org/erddap/tabledap/nerrs_kachdwq                 |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_homer")("moorings_kbnerr_homer")
```


### Moorings (NOAA): across Cook Inlet

* Moorings from NOAA
* From 1999 (and earlier) to 2023, variable
* Slug: moorings_noaa
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_noaa`

Moorings from NOAA

Geese Island, Sitkalidak Island, Bear Cove, Anchorage, Kodiak Island, Alitak, Seldovia, Old Harbor, Boulder Point, Albatross Banks, Shelikof Strait


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                       | datasetID                     | featuretype   | griddap   | info_url                                                                    | institution                                                              | key_variables   |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                    | tabledap                                                              | title                               | urlpath                                                               |
|---:|:------------------------------|:------------------------------|:--------------|:----------|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:-------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:------------------------------------|:----------------------------------------------------------------------|
|  0 | boulder-point                 | boulder-point                 | timeSeries    |           | https://erddap.aoos.org/erddap/info/boulder-point/index.csv                 | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh']         |       60.7767 |       -151.245 | 1999-09-13 20:00:00+00:00 |       60.7767 |       -151.245 | 1999-08-14 00:00:00+00:00 | Timeseries data from 'Boulder Point, AK' (boulder-point)                                   | https://erddap.aoos.org/erddap/tabledap/boulder-point                 | Boulder Point, AK                   | https://erddap.aoos.org/erddap/tabledap/boulder-point                 |
|  1 | geese-island-gps-tide-buoy    | geese-island-gps-tide-buoy    | timeSeries    |           | https://erddap.aoos.org/erddap/info/geese-island-gps-tide-buoy/index.csv    | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh']         |       56.5947 |       -153.996 | 2016-07-30 17:00:00+00:00 |       56.5947 |       -153.996 | 2016-06-25 06:00:00+00:00 | Timeseries data from 'Geese Island Gps Tide Buoy, AK' (geese-island-gps-tide-buoy)         | https://erddap.aoos.org/erddap/tabledap/geese-island-gps-tide-buoy    | Geese Island Gps Tide Buoy, AK      | https://erddap.aoos.org/erddap/tabledap/geese-island-gps-tide-buoy    |
|  2 | noaa_nos_co_ops_9455500       | noaa_nos_co_ops_9455500       | timeSeries    |           | https://erddap.aoos.org/erddap/info/noaa_nos_co_ops_9455500/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh', 'temp'] |       59.4405 |       -151.72  | 2023-09-12 18:00:00+00:00 |       59.4405 |       -151.72  | 1975-07-12 10:00:00+00:00 | Timeseries data from 'Seldovia, AK (OVIA2)' (noaa_nos_co_ops_9455500)                      | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9455500       | Seldovia, AK (OVIA2)                | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9455500       |
|  3 | noaa_nos_co_ops_9455595       | noaa_nos_co_ops_9455595       | timeSeries    |           | https://erddap.aoos.org/erddap/info/noaa_nos_co_ops_9455595/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh']         |       59.725  |       -151.023 | 2023-09-12 18:00:00+00:00 |       59.725  |       -151.023 | 2008-07-03 23:00:00+00:00 | Timeseries data from 'Bear Cove, Kachemak Bay, AK' (noaa_nos_co_ops_9455595)               | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9455595       | Bear Cove, Kachemak Bay, AK         | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9455595       |
|  4 | noaa_nos_co_ops_9455920       | noaa_nos_co_ops_9455920       | timeSeries    |           | https://erddap.aoos.org/erddap/info/noaa_nos_co_ops_9455920/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh', 'temp'] |       61.2375 |       -149.89  | 2023-09-12 18:00:00+00:00 |       61.2375 |       -149.89  | 1978-10-02 05:00:00+00:00 | Timeseries data from 'Anchorage, AK (ANTA2)' (noaa_nos_co_ops_9455920)                     | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9455920       | Anchorage, AK (ANTA2)               | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9455920       |
|  5 | noaa_nos_co_ops_9457804       | noaa_nos_co_ops_9457804       | timeSeries    |           | https://erddap.aoos.org/erddap/info/noaa_nos_co_ops_9457804/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh', 'temp'] |       56.8974 |       -154.248 | 2023-09-12 18:00:00+00:00 |       56.8974 |       -154.248 | 2006-05-18 22:00:00+00:00 | Timeseries data from 'Alitak, AK (ALIA2)' (noaa_nos_co_ops_9457804)                        | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9457804       | Alitak, AK (ALIA2)                  | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_9457804       |
|  6 | noaa_nos_co_ops_kdaa2         | noaa_nos_co_ops_kdaa2         | timeSeries    |           | https://erddap.aoos.org/erddap/info/noaa_nos_co_ops_kdaa2/index.csv         | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['temp']        |       57.73   |       -152.514 | 2023-09-05 17:00:00+00:00 |       57.73   |       -152.514 | 2018-03-03 23:06:00+00:00 | Timeseries data from 'KDAA2 - 9457292- Kodiak Island, AK' (noaa_nos_co_ops_kdaa2)          | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_kdaa2         | KDAA2 - 9457292- Kodiak Island, AK  | https://erddap.aoos.org/erddap/tabledap/noaa_nos_co_ops_kdaa2         |
|  7 | old-harbor-1                  | old-harbor-1                  | timeSeries    |           | https://erddap.aoos.org/erddap/info/old-harbor-1/index.csv                  | NOAA National Tsunami Warning Center (NTWC)                              | ['ssh']         |       57.1998 |       -153.307 | 2018-08-27 15:00:00+00:00 |       57.1998 |       -153.307 | 2014-09-20 13:00:00+00:00 | Timeseries data from 'Old Harbor' (old-harbor-1)                                           | https://erddap.aoos.org/erddap/tabledap/old-harbor-1                  | Old Harbor                          | https://erddap.aoos.org/erddap/tabledap/old-harbor-1                  |
|  8 | sitkalidak-island-gps-tide-bu | sitkalidak-island-gps-tide-bu | timeSeries    |           | https://erddap.aoos.org/erddap/info/sitkalidak-island-gps-tide-bu/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | ['ssh']         |       56.9657 |       -153.252 | 2016-07-27 16:00:00+00:00 |       56.9657 |       -153.252 | 2016-06-25 06:00:00+00:00 | Timeseries data from 'Sitkalidak Island Gps Tide Buoy, AK' (sitkalidak-island-gps-tide-bu) | https://erddap.aoos.org/erddap/tabledap/sitkalidak-island-gps-tide-bu | Sitkalidak Island Gps Tide Buoy, AK | https://erddap.aoos.org/erddap/tabledap/sitkalidak-island-gps-tide-bu |
|  9 | wmo_46077                     | wmo_46077                     | timeSeries    |           | https://erddap.aoos.org/erddap/info/wmo_46077/index.csv                     | NOAA National Data Buoy Center (NDBC)                                    | ['temp']        |       57.892  |       -154.291 | 2023-09-05 17:00:00+00:00 |       57.892  |       -154.291 | 2017-06-14 10:50:00+00:00 | Timeseries data from '46077 - Shelikof Strait, AK' (urn:ioos:station:wmo:46077)            | https://erddap.aoos.org/erddap/tabledap/wmo_46077                     | 46077 - Shelikof Strait, AK         | https://erddap.aoos.org/erddap/tabledap/wmo_46077                     |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_noaa")("moorings_noaa")
```


### Moorings (NPS): Chinitna Bay, Aguchik Island

* Moorings from National Parks Service (NPS)
* From 2018 to 2019, variable
* Slug: moorings_nps
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_nps`

Moorings from NPS


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                          | datasetID                        | featuretype   | griddap   | info_url                                                                       | institution                 | key_variables   |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                              | tabledap                                                                 | title                                      | urlpath                                                                  |
|---:|:---------------------------------|:---------------------------------|:--------------|:----------|:-------------------------------------------------------------------------------|:----------------------------|:----------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:-----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------|:-------------------------------------------------------------------------|
|  0 | aguchik-island-ak-tide-station-9 | aguchik-island-ak-tide-station-9 | timeSeries    |           | https://erddap.aoos.org/erddap/info/aguchik-island-ak-tide-station-9/index.csv | National Park Service (NPS) | ['ssh']         |       58.2946 |       -154.266 | 2019-09-28 17:30:00+00:00 |       58.2946 |       -154.266 | 2018-09-11 18:36:00+00:00 | Timeseries data from 'Aguchik Island, AK, Tide Station (9456901)' (aguchik-island-ak-tide-station-9) | https://erddap.aoos.org/erddap/tabledap/aguchik-island-ak-tide-station-9 | Aguchik Island, AK, Tide Station (9456901) | https://erddap.aoos.org/erddap/tabledap/aguchik-island-ak-tide-station-9 |
|  1 | chinitna-bay-ak-tide-station-945 | chinitna-bay-ak-tide-station-945 | timeSeries    |           | https://erddap.aoos.org/erddap/info/chinitna-bay-ak-tide-station-945/index.csv | National Park Service (NPS) | ['ssh']         |       59.8421 |       -152.993 | 2018-10-26 08:24:00+00:00 |       59.8421 |       -152.993 | 2018-06-14 20:00:00+00:00 | Timeseries data from 'Chinitna Bay, AK, Tide Station (9456357)' (chinitna-bay-ak-tide-station-945)   | https://erddap.aoos.org/erddap/tabledap/chinitna-bay-ak-tide-station-945 | Chinitna Bay, AK, Tide Station (9456357)   | https://erddap.aoos.org/erddap/tabledap/chinitna-bay-ak-tide-station-945 |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_nps")("moorings_nps")
```


### Moorings (UAF): Kodiak Island, Peterson Bay

* Moorings from University of Alaska Fairbanks (UAF)
* From 2013 to present, variable
* Slug: moorings_uaf
* Included: True
* Feature type: timeSeries
* See the full dataset page for more information: {ref}`page:moorings_uaf`

Moorings from UAF


Notes:



````{div} full-width
```{dropdown} Dataset metadata

|    | Dataset                          | datasetID                        | featuretype   | griddap   | info_url                                                                       | institution                                    | key_variables    |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                                 | tabledap                                                                 | title                                         | urlpath                                                                  |
|---:|:---------------------------------|:---------------------------------|:--------------|:----------|:-------------------------------------------------------------------------------|:-----------------------------------------------|:-----------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:--------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------------------------------------------|:-------------------------------------------------------------------------|
|  0 | peterson-bay-ak-gnss-r           | peterson-bay-ak-gnss-r           | timeSeries    |           | https://erddap.aoos.org/erddap/info/peterson-bay-ak-gnss-r/index.csv           | UAF Geophysical Institute (GI)                 | ['ssh']          |       59.5727 |       -151.272 | 2023-09-03 23:45:00+00:00 |       59.5727 |       -151.272 | 2017-01-01 00:22:00+00:00 | Timeseries data from 'Peterson Bay, AK (GNSS-R)' (peterson-bay-ak-gnss-r)                               | https://erddap.aoos.org/erddap/tabledap/peterson-bay-ak-gnss-r           | Peterson Bay, AK (GNSS-R)                     | https://erddap.aoos.org/erddap/tabledap/peterson-bay-ak-gnss-r           |
|  1 | uaf_ocean_acidification_resea_ko | uaf_ocean_acidification_resea_ko | timeSeries    |           | https://erddap.aoos.org/erddap/info/uaf_ocean_acidification_resea_ko/index.csv | UAF Ocean Acidification Research Center (OARC) | ['temp', 'salt'] |       57.7    |       -152.31  | 2016-04-18 15:17:00+00:00 |       57.7    |       -152.31  | 2013-03-30 00:17:00+00:00 | Timeseries data from 'Kodiak Ocean Acidification Mooring (Historic)' (uaf_ocean_acidification_resea_ko) | https://erddap.aoos.org/erddap/tabledap/uaf_ocean_acidification_resea_ko | Kodiak Ocean Acidification Mooring (Historic) | https://erddap.aoos.org/erddap/tabledap/uaf_ocean_acidification_resea_ko |

```
````

+++




**Map of Moorings**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_uaf")("moorings_uaf")
```


### Station Sampling (OTF ADF&G): Long term station sampling

* surface Temp Sal - OTF ADF&G
* Daily sampling mostly in July 1979 to 2021
* Slug: surface_otf_adfg
* Included: False
* Feature type: trajectoryProfile
* See the full dataset page for more information: {ref}`page:surface_otf_adfg`

Long term surface sampling

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf


Notes:

Not used because no times associated with data.

````{div} full-width
```{dropdown} Dataset metadata



```
````

+++




**Map of Stations**

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "surface_otf_adfg")("surface_otf_adfg")
```
