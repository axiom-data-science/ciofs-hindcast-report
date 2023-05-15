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

import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
```

# CTD Transects (GWA): Six repeat transects in Cook Inlet

* CTD profiles 2012-2021 - GWA
* ctd_profiles_gwa
* Quarterly repeats from 2012 to 2021


The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    

Not used in the NWGOA model/data comparison.

<details><summary>Dataset metadata:</summary>

|     | Dataset                        | featuretype       |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                                  |
|----:|:-------------------------------|:------------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------------------------------|
|   0 | transect_3-2012-05-02          | trajectoryProfile |       60.007  |       -151.905 | 2012-05-02 23:56:00 |       59.78   |       -152.567 | 2012-05-02 17:54:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|   1 | transect_3-2012-07-29          | trajectoryProfile |       60.007  |       -151.905 | 2012-07-29 20:35:00 |       59.78   |       -152.567 | 2012-07-29 15:04:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|   2 | transect_3-2012-10-29          | trajectoryProfile |       60.007  |       -151.905 | 2012-10-29 13:30:00 |       59.78   |       -152.567 | 2012-10-29 08:55:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|   3 | transect_3-2013-04-20          | trajectoryProfile |       60.007  |       -151.905 | 2013-04-20 22:41:00 |       59.78   |       -152.567 | 2013-04-20 18:08:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|   4 | transect_3-2013-07-19          | trajectoryProfile |       60.007  |       -151.905 | 2013-07-19 15:28:00 |       59.78   |       -152.567 | 2013-07-19 09:59:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|   5 | transect_3-2013-11-08          | trajectoryProfile |       60.007  |       -151.905 | 2013-11-08 16:35:00 |       59.78   |       -152.567 | 2013-11-08 12:08:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|   6 | transect_3-2014-04-11          | trajectoryProfile |       60.007  |       -151.905 | 2014-04-11 15:03:00 |       59.78   |       -152.567 | 2014-04-11 10:53:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|   7 | transect_3-2014-07-22          | trajectoryProfile |       60.007  |       -151.883 | 2014-07-22 14:23:00 |       59.772  |       -152.567 | 2014-07-22 08:01:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|   8 | transect_3-2014-10-13          | trajectoryProfile |       60.007  |       -151.905 | 2014-10-13 17:30:00 |       59.78   |       -152.567 | 2014-10-13 13:13:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|   9 | transect_3-2015-02-22          | trajectoryProfile |       60.007  |       -151.905 | 2015-02-22 16:01:00 |       59.78   |       -152.567 | 2015-02-22 11:47:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  10 | transect_3-2015-04-12          | trajectoryProfile |       60.007  |       -151.905 | 2015-04-12 19:18:00 |       59.78   |       -152.567 | 2015-04-12 14:34:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  11 | transect_3-2015-11-04          | trajectoryProfile |       60.007  |       -151.905 | 2015-11-04 13:17:00 |       59.78   |       -152.567 | 2015-11-04 03:32:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  12 | transect_3-2016-02-14          | trajectoryProfile |       60.007  |       -151.905 | 2016-02-14 18:00:00 |       59.78   |       -152.567 | 2016-02-14 13:25:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  13 | transect_3-2016-04-11          | trajectoryProfile |       60.007  |       -151.905 | 2016-04-11 11:03:00 |       59.78   |       -152.567 | 2016-04-11 06:52:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  14 | transect_3-2016-08-29          | trajectoryProfile |       60.007  |       -151.883 | 2016-08-29 15:21:00 |       59.772  |       -152.567 | 2016-08-29 08:13:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  15 | transect_3-2017-04-19          | trajectoryProfile |       60.007  |       -151.905 | 2017-04-20 00:12:00 |       59.78   |       -152.567 | 2017-04-19 19:35:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  16 | transect_3-2017-07-25          | trajectoryProfile |       59.827  |       -151.905 | 2017-07-25 13:17:00 |       59.78   |       -152.04  | 2017-07-25 12:29:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  17 | transect_3-2018-06-25          | trajectoryProfile |       59.827  |       -151.905 | 2018-06-25 11:17:00 |       59.78   |       -152.04  | 2018-06-25 10:41:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  18 | transect_3-2018-07-26          | trajectoryProfile |       59.827  |       -151.905 | 2018-07-26 12:41:00 |       59.78   |       -152.04  | 2018-07-26 12:00:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  19 | transect_3-2018-09-13          | trajectoryProfile |       59.863  |       -151.987 | 2018-09-13 11:18:00 |       59.81   |       -152.145 | 2018-09-13 10:48:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  20 | transect_3-2019-02-08          | trajectoryProfile |       59.827  |       -151.905 | 2019-02-08 15:46:00 |       59.78   |       -152.04  | 2019-02-08 15:05:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  21 | transect_3-2019-05-14          | trajectoryProfile |       59.81   |       -151.905 | 2019-05-14 13:11:00 |       59.78   |       -151.987 | 2019-05-14 12:39:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  22 | transect_3-2019-07-25          | trajectoryProfile |       59.827  |       -151.935 | 2019-07-25 14:05:00 |       59.79   |       -152.04  | 2019-07-25 13:25:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  23 | transect_3-2019-09-16          | trajectoryProfile |       59.827  |       -151.905 | 2019-09-16 13:53:00 |       59.78   |       -152.04  | 2019-09-16 13:09:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  24 | transect_3-2020-07-29          | trajectoryProfile |       59.827  |       -151.905 | 2020-07-29 10:45:00 |       59.78   |       -152.04  | 2020-07-29 10:08:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  25 | transect_3-2021-04-16          | trajectoryProfile |       59.827  |       -151.905 | 2021-04-16 11:44:00 |       59.78   |       -152.04  | 2021-04-16 11:02:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  26 | transect_3-2021-07-16          | trajectoryProfile |       59.827  |       -151.935 | 2021-07-16 15:44:00 |       59.79   |       -152.04  | 2021-07-16 15:05:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  27 | transect_4-2012-05-02          | trajectoryProfile |       59.633  |       -151.65  | 2012-05-02 15:35:00 |       59.492  |       -151.65  | 2012-05-02 13:15:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  28 | transect_4-2012-05-31          | trajectoryProfile |       59.633  |       -151.65  | 2012-05-31 12:42:00 |       59.492  |       -151.65  | 2012-05-31 10:58:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  29 | transect_4-2012-06-05_A        | trajectoryProfile |       59.633  |       -151.65  | 2012-06-05 11:29:00 |       59.492  |       -151.65  | 2012-06-05 09:16:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  30 | transect_4-2012-06-05_B        | trajectoryProfile |       59.633  |       -151.65  | 2012-06-05 17:30:00 |       59.492  |       -151.65  | 2012-06-05 15:24:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  31 | transect_4-2012-07-31          | trajectoryProfile |       59.633  |       -151.65  | 2012-07-31 11:02:00 |       59.492  |       -151.65  | 2012-07-31 08:36:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  32 | transect_4-2012-08-15          | trajectoryProfile |       59.633  |       -151.65  | 2012-08-15 16:00:00 |       59.492  |       -151.65  | 2012-08-15 14:34:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  33 | transect_4-2012-10-29          | trajectoryProfile |       59.633  |       -151.65  | 2012-10-29 17:43:00 |       59.492  |       -151.65  | 2012-10-29 15:45:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  34 | transect_4-2013-02-12          | trajectoryProfile |       59.633  |       -151.65  | 2013-02-12 15:17:00 |       59.492  |       -151.65  | 2013-02-12 12:59:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  35 | transect_4-2013-04-21          | trajectoryProfile |       59.633  |       -151.65  | 2013-04-21 11:45:00 |       59.492  |       -151.65  | 2013-04-21 09:26:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  36 | transect_4-2013-06-06          | trajectoryProfile |       59.633  |       -151.65  | 2013-06-06 11:15:00 |       59.492  |       -151.65  | 2013-06-06 09:45:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  37 | transect_4-2013-07-19          | trajectoryProfile |       59.633  |       -151.65  | 2013-07-19 20:55:00 |       59.492  |       -151.65  | 2013-07-19 17:50:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  38 | transect_4-2013-10-29          | trajectoryProfile |       59.633  |       -151.65  | 2013-10-29 14:44:00 |       59.492  |       -151.65  | 2013-10-29 12:18:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  39 | transect_4-2014-02-15          | trajectoryProfile |       59.633  |       -151.65  | 2014-02-15 15:34:00 |       59.492  |       -151.65  | 2014-02-15 13:23:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  40 | transect_4-2014-04-11          | trajectoryProfile |       59.633  |       -151.65  | 2014-04-11 18:27:00 |       59.492  |       -151.65  | 2014-04-11 16:30:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  41 | transect_4-2014-07-21          | trajectoryProfile |       59.633  |       -151.65  | 2014-07-21 22:13:00 |       59.492  |       -151.65  | 2014-07-21 18:36:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  42 | transect_4-2014-08-13          | trajectoryProfile |       59.633  |       -151.65  | 2014-08-13 16:04:00 |       59.492  |       -151.65  | 2014-08-13 14:02:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  43 | transect_4-2014-10-13          | trajectoryProfile |       59.633  |       -151.65  | 2014-10-13 11:23:00 |       59.492  |       -151.65  | 2014-10-13 08:58:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  44 | transect_4-2015-02-12          | trajectoryProfile |       59.633  |       -151.65  | 2015-02-12 12:40:00 |       59.492  |       -151.65  | 2015-02-12 10:26:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  45 | transect_4-2015-02-24          | trajectoryProfile |       59.542  |       -151.65  | 2015-02-24 18:13:00 |       59.542  |       -151.65  | 2015-02-24 18:13:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  46 | transect_4-2015-04-08          | trajectoryProfile |       59.633  |       -151.65  | 2015-04-08 11:08:00 |       59.492  |       -151.65  | 2015-04-08 09:08:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  47 | transect_4-2015-08-14          | trajectoryProfile |       59.542  |       -151.65  | 2015-08-14 15:55:00 |       59.492  |       -151.65  | 2015-08-14 15:07:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  48 | transect_4-2015-09-24          | trajectoryProfile |       59.633  |       -151.65  | 2015-09-24 16:19:00 |       59.492  |       -151.65  | 2015-09-24 15:05:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  49 | transect_4-2015-10-19          | trajectoryProfile |       59.633  |       -151.65  | 2015-10-19 17:58:00 |       59.492  |       -151.65  | 2015-10-19 16:26:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  50 | transect_4-2015-11-03          | trajectoryProfile |       59.542  |       -151.65  | 2015-11-03 16:29:00 |       59.542  |       -151.65  | 2015-11-03 16:29:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  51 | transect_4-2015-11-04          | trajectoryProfile |       59.633  |       -151.65  | 2015-11-04 18:51:00 |       59.492  |       -151.65  | 2015-11-04 15:32:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  52 | transect_4-2015-12-10          | trajectoryProfile |       59.633  |       -151.65  | 2015-12-10 15:13:00 |       59.492  |       -151.65  | 2015-12-10 13:40:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  53 | transect_4-2016-02-09          | trajectoryProfile |       59.633  |       -151.65  | 2016-02-09 12:34:00 |       59.492  |       -151.65  | 2016-02-09 10:35:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  54 | transect_4-2016-04-11          | trajectoryProfile |       59.633  |       -151.65  | 2016-04-11 15:13:00 |       59.492  |       -151.65  | 2016-04-11 13:11:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  55 | transect_4-2016-07-27          | trajectoryProfile |       59.633  |       -151.65  | 2016-07-27 14:30:00 |       59.492  |       -151.65  | 2016-07-27 12:40:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  56 | transect_4-2016-10-13          | trajectoryProfile |       59.633  |       -151.65  | 2016-10-13 16:34:00 |       59.492  |       -151.65  | 2016-10-13 14:51:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  57 | transect_4-2016-12-13          | trajectoryProfile |       59.633  |       -151.65  | 2016-12-13 16:01:00 |       59.492  |       -151.65  | 2016-12-13 13:49:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  58 | transect_4-2017-04-20          | trajectoryProfile |       59.633  |       -151.65  | 2017-04-20 15:56:00 |       59.492  |       -151.65  | 2017-04-20 13:38:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  59 | transect_4-2017-07-25          | trajectoryProfile |       59.633  |       -151.65  | 2017-07-25 11:53:00 |       59.492  |       -151.65  | 2017-07-25 09:48:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  60 | transect_4-2017-10-17          | trajectoryProfile |       59.633  |       -151.65  | 2017-10-17 13:33:00 |       59.492  |       -151.65  | 2017-10-17 11:33:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  61 | transect_4-2018-04-23          | trajectoryProfile |       59.633  |       -151.65  | 2018-04-23 15:11:00 |       59.492  |       -151.65  | 2018-04-23 13:18:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  62 | transect_4-2018-06-25          | trajectoryProfile |       59.633  |       -151.65  | 2018-06-25 14:32:00 |       59.492  |       -151.65  | 2018-06-25 12:26:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  63 | transect_4-2018-07-24          | trajectoryProfile |       59.633  |       -151.65  | 2018-07-24 12:08:00 |       59.492  |       -151.65  | 2018-07-24 10:24:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  64 | transect_4-2018-09-13          | trajectoryProfile |       59.633  |       -151.65  | 2018-09-13 13:42:00 |       59.492  |       -151.65  | 2018-09-13 12:04:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  65 | transect_4-2019-02-07          | trajectoryProfile |       59.633  |       -151.65  | 2019-02-07 12:28:00 |       59.492  |       -151.65  | 2019-02-07 10:34:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  66 | transect_4-2019-05-14          | trajectoryProfile |       59.633  |       -151.65  | 2019-05-14 11:24:00 |       59.492  |       -151.65  | 2019-05-14 09:36:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  67 | transect_4-2019-07-25          | trajectoryProfile |       59.633  |       -151.65  | 2019-07-25 17:01:00 |       59.492  |       -151.65  | 2019-07-25 14:37:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  68 | transect_4-2019-09-16          | trajectoryProfile |       59.633  |       -151.65  | 2019-09-16 16:29:00 |       59.492  |       -151.65  | 2019-09-16 14:27:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
|  69 | transect_4-2020-02-14          | trajectoryProfile |       59.633  |       -151.65  | 2020-02-14 14:31:00 |       59.492  |       -151.65  | 2020-02-14 12:52:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  70 | transect_4-2020-07-23          | trajectoryProfile |       59.633  |       -151.65  | 2020-07-23 11:43:00 |       59.492  |       -151.65  | 2020-07-23 09:39:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  71 | transect_4-2020-09-21          | trajectoryProfile |       59.633  |       -151.65  | 2020-09-21 13:34:00 |       59.492  |       -151.65  | 2020-09-21 11:51:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
|  72 | transect_4-2021-02-17          | trajectoryProfile |       59.633  |       -151.65  | 2021-02-17 13:08:00 |       59.492  |       -151.65  | 2021-02-17 11:39:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  73 | transect_4-2021-04-16          | trajectoryProfile |       59.633  |       -151.65  | 2021-04-16 13:54:00 |       59.492  |       -151.65  | 2021-04-16 12:16:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  74 | transect_4-2021-07-16          | trajectoryProfile |       59.633  |       -151.65  | 2021-07-16 14:21:00 |       59.492  |       -151.65  | 2021-07-16 12:30:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  75 | transect_4-2021-09-17          | trajectoryProfile |       59.633  |       -151.65  | 2021-09-17 12:43:00 |       59.492  |       -151.65  | 2021-09-17 11:00:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
|  76 | transect_4-2022-03-01          | trajectoryProfile |       59.633  |       -151.65  | 2022-03-01 12:55:00 |       59.492  |       -151.65  | 2022-03-01 11:50:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
|  77 | transect_4-2022-04-13          | trajectoryProfile |       59.633  |       -151.65  | 2022-04-13 11:26:00 |       59.492  |       -151.65  | 2022-04-13 10:15:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
|  78 | transect_4-2022-07-23          | trajectoryProfile |       59.633  |       -151.65  | 2022-07-23 12:19:00 |       59.492  |       -151.65  | 2022-07-23 10:46:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
|  79 | transect_6-2012-05-03          | trajectoryProfile |       59.212  |       -151.925 | 2012-05-04 01:43:00 |       58.872  |       -153.212 | 2012-05-03 17:38:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  80 | transect_6-2012-07-30          | trajectoryProfile |       59.212  |       -151.925 | 2012-07-31 00:40:00 |       58.869  |       -153.225 | 2012-07-30 15:02:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  81 | transect_6-2012-10-28          | trajectoryProfile |       59.212  |       -151.925 | 2012-10-28 18:55:00 |       58.869  |       -153.225 | 2012-10-28 07:54:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
|  82 | transect_6-2013-04-19          | trajectoryProfile |       59.212  |       -151.925 | 2013-04-19 20:50:00 |       58.869  |       -153.225 | 2013-04-19 09:27:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  83 | transect_6-2013-07-21          | trajectoryProfile |       59.212  |       -151.925 | 2013-07-22 03:45:00 |       58.869  |       -153.225 | 2013-07-21 18:28:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  84 | transect_6-2013-11-06          | trajectoryProfile |       59.212  |       -151.925 | 2013-11-06 17:31:00 |       58.869  |       -153.225 | 2013-11-06 09:07:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
|  85 | transect_6-2014-04-06          | trajectoryProfile |       59.212  |       -151.925 | 2014-04-06 17:31:00 |       58.869  |       -153.225 | 2014-04-06 09:18:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  86 | transect_6-2014-07-23          | trajectoryProfile |       59.212  |       -151.925 | 2014-07-23 20:04:00 |       58.869  |       -153.225 | 2014-07-23 08:40:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  87 | transect_6-2014-10-18          | trajectoryProfile |       59.212  |       -151.925 | 2014-10-18 09:13:00 |       58.869  |       -153.225 | 2014-10-18 00:27:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
|  88 | transect_6-2015-02-23          | trajectoryProfile |       59.212  |       -151.925 | 2015-02-24 00:32:00 |       58.869  |       -153.225 | 2015-02-23 15:26:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  89 | transect_6-2015-04-08          | trajectoryProfile |       59.212  |       -151.925 | 2015-04-08 04:32:00 |       59.075  |       -152.445 | 2015-04-08 01:00:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  90 | transect_6-2015-08-14          | trajectoryProfile |       59.212  |       -151.925 | 2015-08-14 12:00:00 |       59.161  |       -152.117 | 2015-08-14 10:33:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
|  91 | transect_6-2016-02-15          | trajectoryProfile |       59.212  |       -151.925 | 2016-02-15 18:53:00 |       58.869  |       -153.225 | 2016-02-15 10:19:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  92 | transect_6-2016-04-10          | trajectoryProfile |       59.212  |       -151.925 | 2016-04-10 15:59:00 |       58.869  |       -153.225 | 2016-04-10 07:45:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  93 | transect_6-2016-08-31          | trajectoryProfile |       59.212  |       -151.925 | 2016-08-31 19:05:00 |       58.869  |       -153.225 | 2016-08-31 07:41:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  94 | transect_6-2016-12-12          | trajectoryProfile |       59.212  |       -151.925 | 2016-12-12 22:07:00 |       59.017  |       -152.665 | 2016-12-12 16:55:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
|  95 | transect_6-2017-04-18          | trajectoryProfile |       59.212  |       -151.925 | 2017-04-18 22:13:00 |       58.8689 |       -153.24  | 2017-04-18 12:18:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  96 | transect_6-2017-07-26          | trajectoryProfile |       59.212  |       -151.925 | 2017-07-26 13:02:00 |       59.175  |       -152.062 | 2017-07-26 12:24:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  97 | transect_6-2017-11-02          | trajectoryProfile |       59.212  |       -151.925 | 2017-11-02 13:08:00 |       59.19   |       -152.007 | 2017-11-02 12:24:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
|  98 | transect_6-2018-07-18          | trajectoryProfile |       59.212  |       -151.925 | 2018-07-18 11:50:00 |       59.161  |       -152.117 | 2018-07-18 10:16:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
|  99 | transect_6-2018-09-17          | trajectoryProfile |       59.212  |       -151.925 | 2018-09-17 12:23:00 |       59.161  |       -152.117 | 2018-09-17 11:04:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 100 | transect_6-2019-02-08          | trajectoryProfile |       59.212  |       -151.925 | 2019-02-08 12:32:00 |       59.161  |       -152.117 | 2019-02-08 11:23:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 101 | transect_6-2019-05-12          | trajectoryProfile |       59.212  |       -151.925 | 2019-05-12 14:43:00 |       58.869  |       -153.225 | 2019-05-12 05:33:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 102 | transect_6-2019-07-25          | trajectoryProfile |       59.212  |       -151.925 | 2019-07-25 10:43:00 |       59.161  |       -152.117 | 2019-07-25 09:19:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 103 | transect_6-2020-07-24          | trajectoryProfile |       59.212  |       -151.925 | 2020-07-24 10:25:00 |       59.175  |       -152.062 | 2020-07-24 09:23:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 104 | transect_6-2020-09-20          | trajectoryProfile |       59.212  |       -151.925 | 2020-09-20 10:43:00 |       59.161  |       -152.117 | 2020-09-20 09:27:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 105 | transect_6-2021-02-16          | trajectoryProfile |       59.212  |       -151.925 | 2021-02-16 12:10:00 |       59.175  |       -152.062 | 2021-02-16 11:22:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 106 | transect_6-2021-04-14          | trajectoryProfile |       59.212  |       -151.925 | 2021-04-14 16:53:00 |       58.869  |       -153.225 | 2021-04-14 07:06:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 107 | transect_6-2021-07-21          | trajectoryProfile |       59.212  |       -151.925 | 2021-07-21 11:54:00 |       59.175  |       -152.062 | 2021-07-21 10:50:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 108 | transect_6-2021-10-05          | trajectoryProfile |       59.212  |       -151.925 | 2021-10-05 11:40:00 |       59.197  |       -151.98  | 2021-10-05 11:03:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 109 | transect_6-2022-02-28          | trajectoryProfile |       59.205  |       -151.952 | 2022-02-28 11:26:00 |       59.205  |       -151.952 | 2022-02-28 11:26:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 110 | transect_6-2022-04-12          | trajectoryProfile |       59.205  |       -151.952 | 2022-04-12 10:12:00 |       59.205  |       -151.952 | 2022-04-12 10:12:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 111 | transect_6-2022-07-21          | trajectoryProfile |       59.205  |       -151.952 | 2022-07-21 11:11:00 |       59.205  |       -151.952 | 2022-07-21 11:11:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 112 | transect_7-2012-07-30          | trajectoryProfile |       59.335  |       -152.032 | 2012-07-30 11:04:00 |       59.31   |       -152.847 | 2012-07-30 06:53:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 113 | transect_7-2012-10-28          | trajectoryProfile |       59.35   |       -152.032 | 2012-10-29 02:53:00 |       59.31   |       -153.302 | 2012-10-28 20:01:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 114 | transect_7-2013-04-20          | trajectoryProfile |       59.35   |       -152     | 2013-04-20 14:03:00 |       59.308  |       -153.302 | 2013-04-20 06:29:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 115 | transect_7-2013-07-18          | trajectoryProfile |       59.35   |       -152.032 | 2013-07-18 19:56:00 |       59.31   |       -153.302 | 2013-07-18 12:36:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 116 | transect_7-2014-02-17          | trajectoryProfile |       59.35   |       -152.097 | 2014-02-17 12:00:00 |       59.312  |       -153.302 | 2014-02-17 06:14:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 117 | transect_7-2014-04-07          | trajectoryProfile |       59.35   |       -152.032 | 2014-04-07 09:52:00 |       59.31   |       -153.302 | 2014-04-07 03:17:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 118 | transect_7-2014-07-24          | trajectoryProfile |       59.35   |       -152.032 | 2014-07-24 16:53:00 |       59.31   |       -153.302 | 2014-07-24 08:00:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 119 | transect_7-2014-10-17          | trajectoryProfile |       59.315  |       -152.032 | 2014-10-17 17:42:00 |       59.31   |       -152.196 | 2014-10-17 16:12:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 120 | transect_7-2014-10-18          | trajectoryProfile |       59.35   |       -152.032 | 2014-10-18 19:16:00 |       59.31   |       -153.302 | 2014-10-18 12:49:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 121 | transect_7-2015-02-24          | trajectoryProfile |       59.35   |       -152.032 | 2015-02-24 12:02:00 |       59.31   |       -153.302 | 2015-02-24 05:35:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 122 | transect_7-2015-04-13          | trajectoryProfile |       59.35   |       -152.032 | 2015-04-13 07:51:00 |       59.31   |       -153.302 | 2015-04-13 01:35:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 123 | transect_7-2015-08-14          | trajectoryProfile |       59.315  |       -152.032 | 2015-08-14 13:38:00 |       59.31   |       -152.196 | 2015-08-14 12:30:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 124 | transect_7-2016-02-16          | trajectoryProfile |       59.35   |       -152.032 | 2016-02-16 06:43:00 |       59.31   |       -153.302 | 2016-02-16 00:02:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 125 | transect_7-2016-08-30          | trajectoryProfile |       59.35   |       -152     | 2016-08-30 15:26:00 |       59.308  |       -153.302 | 2016-08-30 07:43:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 126 | transect_7-2016-12-13          | trajectoryProfile |       59.315  |       -152.032 | 2016-12-13 11:20:00 |       59.31   |       -152.196 | 2016-12-13 10:09:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 127 | transect_7-2017-04-19          | trajectoryProfile |       59.35   |       -152.032 | 2017-04-19 15:57:00 |       59.31   |       -153.302 | 2017-04-19 08:20:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 128 | transect_7-2017-07-26          | trajectoryProfile |       59.315  |       -152.097 | 2017-07-26 11:52:00 |       59.312  |       -152.196 | 2017-07-26 11:10:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 129 | transect_7-2017-11-02          | trajectoryProfile |       59.312  |       -152.032 | 2017-11-02 14:31:00 |       59.31   |       -152.097 | 2017-11-02 14:00:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 130 | transect_7-2018-03-27          | trajectoryProfile |       59.31   |       -152.065 | 2018-03-27 12:51:00 |       59.31   |       -152.065 | 2018-03-27 12:51:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 131 | transect_7-2018-07-18          | trajectoryProfile |       59.313  |       -152.032 | 2018-07-18 13:03:00 |       59.31   |       -152.13  | 2018-07-18 12:26:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 132 | transect_7-2018-09-17          | trajectoryProfile |       59.315  |       -152.032 | 2018-09-17 13:47:00 |       59.31   |       -152.196 | 2018-09-17 12:57:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 133 | transect_7-2019-02-08          | trajectoryProfile |       59.315  |       -152.065 | 2019-02-08 13:52:00 |       59.31   |       -152.196 | 2019-02-08 13:06:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 134 | transect_7-2019-05-12          | trajectoryProfile |       59.315  |       -152.032 | 2019-05-12 16:35:00 |       59.31   |       -152.196 | 2019-05-12 15:30:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 135 | transect_7-2019-07-25          | trajectoryProfile |       59.315  |       -152.032 | 2019-07-25 12:03:00 |       59.31   |       -152.196 | 2019-07-25 11:02:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 136 | transect_7-2019-09-19          | trajectoryProfile |       59.315  |       -152.032 | 2019-09-19 15:42:00 |       59.31   |       -152.196 | 2019-09-19 14:48:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 137 | transect_7-2020-07-24          | trajectoryProfile |       59.315  |       -152.032 | 2020-07-24 11:43:00 |       59.31   |       -152.196 | 2020-07-24 10:57:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 138 | transect_7-2020-09-20          | trajectoryProfile |       59.315  |       -152.032 | 2020-09-20 12:09:00 |       59.31   |       -152.196 | 2020-09-20 11:19:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 139 | transect_7-2021-02-16          | trajectoryProfile |       59.315  |       -152.032 | 2021-02-16 13:35:00 |       59.31   |       -152.196 | 2021-02-16 12:44:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 140 | transect_7-2021-04-14          | trajectoryProfile |       59.313  |       -152.032 | 2021-04-14 18:14:00 |       59.31   |       -152.13  | 2021-04-14 17:32:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 141 | transect_7-2021-07-21          | trajectoryProfile |       59.313  |       -152.032 | 2021-07-21 13:01:00 |       59.31   |       -152.13  | 2021-07-21 12:24:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 142 | transect_7-2021-10-05          | trajectoryProfile |       59.312  |       -152.032 | 2021-10-05 12:35:00 |       59.31   |       -152.097 | 2021-10-05 12:05:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 143 | transect_7-2022-02-28          | trajectoryProfile |       59.31   |       -152.065 | 2022-02-28 12:05:00 |       59.31   |       -152.065 | 2022-02-28 12:05:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 144 | transect_7-2022-04-12          | trajectoryProfile |       59.31   |       -152.065 | 2022-04-12 10:52:00 |       59.31   |       -152.065 | 2022-04-12 10:52:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 145 | transect_7-2022-07-21          | trajectoryProfile |       59.31   |       -152.065 | 2022-07-21 11:55:00 |       59.31   |       -152.065 | 2022-07-21 11:55:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 146 | transect_9-2012-02-14          | trajectoryProfile |       59.596  |       -151.357 | 2012-02-14 13:40:00 |       59.5702 |       -151.404 | 2012-02-14 12:31:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 147 | transect_9-2012-03-14          | trajectoryProfile |       59.596  |       -151.357 | 2012-03-14 15:27:00 |       59.5702 |       -151.404 | 2012-03-14 14:05:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 148 | transect_9-2012-04-10          | trajectoryProfile |       59.596  |       -151.357 | 2012-04-10 19:17:00 |       59.5702 |       -151.404 | 2012-04-10 18:02:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 149 | transect_9-2012-04-26          | trajectoryProfile |       59.5794 |       -151.357 | 2012-04-26 18:50:00 |       59.5702 |       -151.379 | 2012-04-26 18:03:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 150 | transect_9-2012-05-31_A        | trajectoryProfile |       59.596  |       -151.357 | 2012-05-31 14:08:00 |       59.5702 |       -151.404 | 2012-05-31 12:13:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 151 | transect_9-2012-05-31_B        | trajectoryProfile |       59.596  |       -151.357 | 2012-05-31 19:22:00 |       59.5702 |       -151.404 | 2012-05-31 17:53:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 152 | transect_9-2012-06-05_A        | trajectoryProfile |       59.596  |       -151.357 | 2012-06-05 12:00:00 |       59.5702 |       -151.404 | 2012-06-05 10:16:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 153 | transect_9-2012-06-05_B        | trajectoryProfile |       59.596  |       -151.357 | 2012-06-05 18:35:00 |       59.5702 |       -151.404 | 2012-06-05 16:43:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 154 | transect_9-2012-06-27          | trajectoryProfile |       59.596  |       -151.357 | 2012-06-27 09:52:00 |       59.5702 |       -151.404 | 2012-06-27 08:32:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 155 | transect_9-2012-07-02          | trajectoryProfile |       59.596  |       -151.357 | 2012-07-02 15:28:00 |       59.5702 |       -151.404 | 2012-07-02 14:08:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 156 | transect_9-2012-07-21          | trajectoryProfile |       59.596  |       -151.357 | 2012-07-21 18:04:00 |       59.5702 |       -151.404 | 2012-07-21 16:41:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 157 | transect_9-2012-08-03          | trajectoryProfile |       59.596  |       -151.357 | 2012-08-03 16:45:00 |       59.5702 |       -151.404 | 2012-08-03 15:25:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 158 | transect_9-2012-08-15          | trajectoryProfile |       59.596  |       -151.357 | 2012-08-15 15:46:00 |       59.5702 |       -151.404 | 2012-08-15 14:09:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 159 | transect_9-2012-08-26          | trajectoryProfile |       59.596  |       -151.357 | 2012-08-26 12:14:00 |       59.5702 |       -151.404 | 2012-08-26 10:55:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 160 | transect_9-2012-08-31          | trajectoryProfile |       59.596  |       -151.362 | 2012-08-31 16:35:00 |       59.5718 |       -151.404 | 2012-08-31 15:14:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 161 | transect_9-2012-09-21_A        | trajectoryProfile |       59.596  |       -151.357 | 2012-09-21 10:49:00 |       59.5702 |       -151.404 | 2012-09-21 09:32:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 162 | transect_9-2012-09-21_B        | trajectoryProfile |       59.596  |       -151.357 | 2012-09-21 12:13:00 |       59.5702 |       -151.404 | 2012-09-21 11:06:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 163 | transect_9-2012-09-21_C        | trajectoryProfile |       59.596  |       -151.357 | 2012-09-21 13:40:00 |       59.5702 |       -151.404 | 2012-09-21 12:27:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 164 | transect_9-2012-09-21_D        | trajectoryProfile |       59.596  |       -151.357 | 2012-09-21 15:49:00 |       59.5702 |       -151.404 | 2012-09-21 14:38:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 165 | transect_9-2012-09-21_E        | trajectoryProfile |       59.596  |       -151.357 | 2012-09-21 19:18:00 |       59.5702 |       -151.404 | 2012-09-21 17:32:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 166 | transect_9-2012-10-12          | trajectoryProfile |       59.596  |       -151.357 | 2012-10-12 14:10:00 |       59.5702 |       -151.404 | 2012-10-12 12:45:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 167 | transect_9-2012-10-29          | trajectoryProfile |       59.596  |       -151.357 | 2012-10-29 20:53:00 |       59.5702 |       -151.404 | 2012-10-29 19:10:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 168 | transect_9-2013-01-04          | trajectoryProfile |       59.596  |       -151.357 | 2013-01-04 20:12:00 |       59.5702 |       -151.404 | 2013-01-04 18:04:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 169 | transect_9-2013-02-12          | trajectoryProfile |       59.596  |       -151.357 | 2013-02-12 11:22:00 |       59.5702 |       -151.404 | 2013-02-12 09:18:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 170 | transect_9-2013-03-15          | trajectoryProfile |       59.596  |       -151.357 | 2013-03-15 20:12:00 |       59.5702 |       -151.404 | 2013-03-15 17:58:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 171 | transect_9-2013-04-21          | trajectoryProfile |       59.596  |       -151.357 | 2013-04-21 16:18:00 |       59.5702 |       -151.404 | 2013-04-21 14:30:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 172 | transect_9-2013-05-21          | trajectoryProfile |       59.596  |       -151.357 | 2013-05-21 13:59:00 |       59.5702 |       -151.404 | 2013-05-21 12:07:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 173 | transect_9-2013-06-06          | trajectoryProfile |       59.596  |       -151.357 | 2013-06-06 11:50:00 |       59.5702 |       -151.404 | 2013-06-06 10:12:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 174 | transect_9-2013-06-19          | trajectoryProfile |       59.596  |       -151.357 | 2013-06-19 12:42:00 |       59.5702 |       -151.404 | 2013-06-19 10:48:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 175 | transect_9-2013-06-28          | trajectoryProfile |       59.596  |       -151.357 | 2013-06-28 15:09:00 |       59.5702 |       -151.404 | 2013-06-28 13:18:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 176 | transect_9-2013-07-05          | trajectoryProfile |       59.596  |       -151.357 | 2013-07-05 16:02:00 |       59.5702 |       -151.404 | 2013-07-05 14:33:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 177 | transect_9-2013-07-09          | trajectoryProfile |       59.596  |       -151.357 | 2013-07-09 19:06:00 |       59.5702 |       -151.404 | 2013-07-09 17:17:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 178 | transect_9-2013-07-22          | trajectoryProfile |       59.596  |       -151.357 | 2013-07-22 10:16:00 |       59.5702 |       -151.404 | 2013-07-22 09:01:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 179 | transect_9-2013-08-07          | trajectoryProfile |       59.596  |       -151.357 | 2013-08-07 16:38:00 |       59.5702 |       -151.404 | 2013-08-07 15:25:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 180 | transect_9-2013-08-30          | trajectoryProfile |       59.596  |       -151.357 | 2013-08-30 12:54:00 |       59.5702 |       -151.404 | 2013-08-30 11:15:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 181 | transect_9-2013-09-25          | trajectoryProfile |       59.596  |       -151.357 | 2013-09-25 15:13:00 |       59.5702 |       -151.404 | 2013-09-25 13:36:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 182 | transect_9-2013-10-29          | trajectoryProfile |       59.596  |       -151.357 | 2013-10-29 10:52:00 |       59.5702 |       -151.404 | 2013-10-29 09:08:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 183 | transect_9-2013-12-03          | trajectoryProfile |       59.596  |       -151.357 | 2013-12-03 16:02:00 |       59.5702 |       -151.404 | 2013-12-03 14:16:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 184 | transect_9-2014-01-09          | trajectoryProfile |       59.596  |       -151.357 | 2014-01-09 15:39:00 |       59.5702 |       -151.404 | 2014-01-09 13:55:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 185 | transect_9-2014-02-15          | trajectoryProfile |       59.596  |       -151.357 | 2014-02-15 11:55:00 |       59.5702 |       -151.404 | 2014-02-15 10:24:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 186 | transect_9-2014-03-28          | trajectoryProfile |       59.596  |       -151.357 | 2014-03-28 15:26:00 |       59.5702 |       -151.404 | 2014-03-28 13:43:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 187 | transect_9-2014-04-11          | trajectoryProfile |       59.596  |       -151.357 | 2014-04-11 21:00:00 |       59.5702 |       -151.404 | 2014-04-11 19:49:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 188 | transect_9-2014-05-28          | trajectoryProfile |       59.596  |       -151.357 | 2014-05-28 17:20:00 |       59.5702 |       -151.404 | 2014-05-28 15:22:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 189 | transect_9-2014-06-18          | trajectoryProfile |       59.596  |       -151.357 | 2014-06-18 18:53:00 |       59.5702 |       -151.404 | 2014-06-18 16:51:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 190 | transect_9-2014-07-21          | trajectoryProfile |       59.596  |       -151.357 | 2014-07-21 16:55:00 |       59.5702 |       -151.404 | 2014-07-21 14:44:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 191 | transect_9-2014-08-13          | trajectoryProfile |       59.596  |       -151.357 | 2014-08-13 12:37:00 |       59.5702 |       -151.404 | 2014-08-13 10:20:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 192 | transect_9-2014-10-19          | trajectoryProfile |       59.596  |       -151.357 | 2014-10-19 11:31:00 |       59.5702 |       -151.404 | 2014-10-19 10:03:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 193 | transect_9-2014-11-25          | trajectoryProfile |       59.596  |       -151.357 | 2014-11-25 17:08:00 |       59.5702 |       -151.404 | 2014-11-25 15:40:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 194 | transect_9-2014-12-17          | trajectoryProfile |       59.596  |       -151.357 | 2014-12-17 12:50:00 |       59.5702 |       -151.404 | 2014-12-17 11:11:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 195 | transect_9-2015-01-16          | trajectoryProfile |       59.596  |       -151.357 | 2015-01-16 15:25:00 |       59.5702 |       -151.404 | 2015-01-16 14:01:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 196 | transect_9-2015-02-12          | trajectoryProfile |       59.596  |       -151.357 | 2015-02-12 17:06:00 |       59.5702 |       -151.404 | 2015-02-12 15:45:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 197 | transect_9-2015-02-24          | trajectoryProfile |       59.596  |       -151.385 | 2015-02-24 19:26:00 |       59.5824 |       -151.404 | 2015-02-24 19:14:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 198 | transect_9-2015-03-31          | trajectoryProfile |       59.596  |       -151.357 | 2015-03-31 14:43:00 |       59.5702 |       -151.404 | 2015-03-31 13:07:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 199 | transect_9-2015-04-08          | trajectoryProfile |       59.596  |       -151.357 | 2015-04-08 15:26:00 |       59.5702 |       -151.404 | 2015-04-08 14:07:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 200 | transect_9-2015-05-28          | trajectoryProfile |       59.596  |       -151.357 | 2015-05-28 13:29:00 |       59.5702 |       -151.404 | 2015-05-28 11:38:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 201 | transect_9-2015-06-26          | trajectoryProfile |       59.596  |       -151.357 | 2015-06-26 12:43:00 |       59.5702 |       -151.404 | 2015-06-26 10:38:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 202 | transect_9-2015-07-10          | trajectoryProfile |       59.596  |       -151.357 | 2015-07-10 11:51:00 |       59.5702 |       -151.404 | 2015-07-10 09:48:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 203 | transect_9-2015-07-29          | trajectoryProfile |       59.596  |       -151.357 | 2015-07-29 15:18:00 |       59.5702 |       -151.404 | 2015-07-29 13:21:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 204 | transect_9-2015-08-14          | trajectoryProfile |       59.596  |       -151.357 | 2015-08-14 18:30:00 |       59.5702 |       -151.404 | 2015-08-14 16:45:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 205 | transect_9-2015-09-04          | trajectoryProfile |       59.596  |       -151.357 | 2015-09-04 11:20:00 |       59.5702 |       -151.404 | 2015-09-04 09:22:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 206 | transect_9-2015-09-24          | trajectoryProfile |       59.596  |       -151.357 | 2015-09-24 14:29:00 |       59.5702 |       -151.404 | 2015-09-24 13:16:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 207 | transect_9-2015-10-19          | trajectoryProfile |       59.596  |       -151.357 | 2015-10-19 15:42:00 |       59.5702 |       -151.404 | 2015-10-19 14:12:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 208 | transect_9-2015-11-04          | trajectoryProfile |       59.596  |       -151.357 | 2015-11-04 22:31:00 |       59.5702 |       -151.404 | 2015-11-04 20:35:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 209 | transect_9-2015-12-10          | trajectoryProfile |       59.596  |       -151.357 | 2015-12-10 13:04:00 |       59.5702 |       -151.404 | 2015-12-10 11:42:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 210 | transect_9-2016-01-07          | trajectoryProfile |       59.596  |       -151.357 | 2016-01-07 13:36:00 |       59.5702 |       -151.404 | 2016-01-07 12:07:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 211 | transect_9-2016-02-09          | trajectoryProfile |       59.596  |       -151.357 | 2016-02-09 15:03:00 |       59.5702 |       -151.404 | 2016-02-09 13:48:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 212 | transect_9-2016-04-07          | trajectoryProfile |       59.596  |       -151.357 | 2016-04-07 15:45:00 |       59.5702 |       -151.404 | 2016-04-07 14:05:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 213 | transect_9-2016-05-12          | trajectoryProfile |       59.596  |       -151.357 | 2016-05-12 14:23:00 |       59.5702 |       -151.404 | 2016-05-12 12:59:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 214 | transect_9-2016-06-16          | trajectoryProfile |       59.596  |       -151.357 | 2016-06-16 13:30:00 |       59.5702 |       -151.404 | 2016-06-16 11:52:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 215 | transect_9-2016-07-27          | trajectoryProfile |       59.596  |       -151.357 | 2016-07-27 11:57:00 |       59.5702 |       -151.404 | 2016-07-27 10:18:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 216 | transect_9-2016-09-23          | trajectoryProfile |       59.596  |       -151.357 | 2016-09-23 12:22:00 |       59.5702 |       -151.404 | 2016-09-23 10:40:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 217 | transect_9-2016-10-13          | trajectoryProfile |       59.596  |       -151.357 | 2016-10-13 14:11:00 |       59.5702 |       -151.404 | 2016-10-13 12:40:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 218 | transect_9-2016-11-10          | trajectoryProfile |       59.596  |       -151.357 | 2016-11-10 15:04:00 |       59.5702 |       -151.404 | 2016-11-10 13:24:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 219 | transect_9-2016-12-13          | trajectoryProfile |       59.596  |       -151.357 | 2016-12-13 19:10:00 |       59.5702 |       -151.404 | 2016-12-13 17:30:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 220 | transect_9-2017-01-11          | trajectoryProfile |       59.596  |       -151.357 | 2017-01-11 14:19:00 |       59.5702 |       -151.404 | 2017-01-11 12:38:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 221 | transect_9-2017-02-07          | trajectoryProfile |       59.596  |       -151.357 | 2017-02-07 12:09:00 |       59.5702 |       -151.404 | 2017-02-07 10:36:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 222 | transect_9-2017-03-28          | trajectoryProfile |       59.596  |       -151.357 | 2017-03-28 15:24:00 |       59.5702 |       -151.404 | 2017-03-28 13:50:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 223 | transect_9-2017-04-20          | trajectoryProfile |       59.596  |       -151.357 | 2017-04-20 22:51:00 |       59.5702 |       -151.404 | 2017-04-20 21:10:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 224 | transect_9-2017-05-30          | trajectoryProfile |       59.596  |       -151.357 | 2017-05-30 13:49:00 |       59.5702 |       -151.404 | 2017-05-30 12:05:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 225 | transect_9-2017-06-28          | trajectoryProfile |       59.596  |       -151.357 | 2017-06-28 13:09:00 |       59.5702 |       -151.404 | 2017-06-28 11:20:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 226 | transect_9-2017-07-24          | trajectoryProfile |       59.596  |       -151.357 | 2017-07-24 10:54:00 |       59.5702 |       -151.404 | 2017-07-24 09:03:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 227 | transect_9-2017-08-24          | trajectoryProfile |       59.596  |       -151.357 | 2017-08-24 18:32:00 |       59.5702 |       -151.404 | 2017-08-24 16:59:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 228 | transect_9-2017-09-22          | trajectoryProfile |       59.596  |       -151.357 | 2017-09-22 16:15:00 |       59.5702 |       -151.404 | 2017-09-22 14:42:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 229 | transect_9-2017-10-17          | trajectoryProfile |       59.596  |       -151.357 | 2017-10-17 15:31:00 |       59.5702 |       -151.404 | 2017-10-17 14:00:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 230 | transect_9-2017-11-07          | trajectoryProfile |       59.596  |       -151.357 | 2017-11-07 17:16:00 |       59.5702 |       -151.404 | 2017-11-07 15:47:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 231 | transect_9-2017-12-14          | trajectoryProfile |       59.596  |       -151.357 | 2017-12-14 12:07:00 |       59.5702 |       -151.404 | 2017-12-14 10:38:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 232 | transect_9-2018-01-17          | trajectoryProfile |       59.596  |       -151.357 | 2018-01-17 14:54:00 |       59.5702 |       -151.404 | 2018-01-17 13:26:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 233 | transect_9-2018-03-02          | trajectoryProfile |       59.596  |       -151.357 | 2018-03-02 16:11:00 |       59.5702 |       -151.404 | 2018-03-02 14:46:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 234 | transect_9-2018-03-27          | trajectoryProfile |       59.596  |       -151.357 | 2018-03-27 11:31:00 |       59.5702 |       -151.404 | 2018-03-27 09:56:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 235 | transect_9-2018-04-23          | trajectoryProfile |       59.596  |       -151.357 | 2018-04-23 12:34:00 |       59.5702 |       -151.404 | 2018-04-23 10:52:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 236 | transect_9-2018-05-24          | trajectoryProfile |       59.596  |       -151.357 | 2018-05-24 15:34:00 |       59.5702 |       -151.404 | 2018-05-24 14:07:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 237 | transect_9-2018-06-22          | trajectoryProfile |       59.596  |       -151.357 | 2018-06-22 15:07:00 |       59.5702 |       -151.404 | 2018-06-22 13:40:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 238 | transect_9-2018-07-24          | trajectoryProfile |       59.596  |       -151.357 | 2018-07-24 14:14:00 |       59.5702 |       -151.404 | 2018-07-24 12:43:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 239 | transect_9-2018-08-23          | trajectoryProfile |       59.596  |       -151.357 | 2018-08-23 15:59:00 |       59.5702 |       -151.404 | 2018-08-23 14:14:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 240 | transect_9-2018-09-13          | trajectoryProfile |       59.596  |       -151.357 | 2018-09-13 15:35:00 |       59.5702 |       -151.404 | 2018-09-13 14:10:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 241 | transect_9-2018-10-17          | trajectoryProfile |       59.596  |       -151.357 | 2018-10-17 15:51:00 |       59.5702 |       -151.404 | 2018-10-17 14:28:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 242 | transect_9-2018-11-08          | trajectoryProfile |       59.596  |       -151.357 | 2018-11-08 15:08:00 |       59.5702 |       -151.404 | 2018-11-08 13:43:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 243 | transect_9-2018-12-06          | trajectoryProfile |       59.596  |       -151.357 | 2018-12-06 15:48:00 |       59.5702 |       -151.404 | 2018-12-06 14:28:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 244 | transect_9-2019-02-07          | trajectoryProfile |       59.596  |       -151.357 | 2019-02-07 16:38:00 |       59.5702 |       -151.404 | 2019-02-07 15:17:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 245 | transect_9-2019-03-19          | trajectoryProfile |       59.5925 |       -151.357 | 2019-03-19 14:41:00 |       59.5702 |       -151.399 | 2019-03-19 13:16:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 246 | transect_9-2019-04-24          | trajectoryProfile |       59.596  |       -151.357 | 2019-04-24 15:17:00 |       59.5702 |       -151.404 | 2019-04-24 13:37:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 247 | transect_9-2019-05-14          | trajectoryProfile |       59.596  |       -151.357 | 2019-05-14 18:41:00 |       59.5702 |       -151.404 | 2019-05-14 17:25:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 248 | transect_9-2019-06-19          | trajectoryProfile |       59.596  |       -151.357 | 2019-06-19 17:57:00 |       59.5702 |       -151.404 | 2019-06-19 15:57:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 249 | transect_9-2019-07-23          | trajectoryProfile |       59.596  |       -151.357 | 2019-07-23 17:18:00 |       59.5702 |       -151.404 | 2019-07-23 15:24:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 250 | transect_9-2019-09-16          | trajectoryProfile |       59.596  |       -151.357 | 2019-09-16 11:37:00 |       59.5702 |       -151.404 | 2019-09-16 09:29:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 251 | transect_9-2019-10-30          | trajectoryProfile |       59.596  |       -151.357 | 2019-10-30 16:08:00 |       59.5702 |       -151.404 | 2019-10-30 14:21:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 252 | transect_9-2019-11-15          | trajectoryProfile |       59.596  |       -151.357 | 2019-11-15 17:29:00 |       59.5702 |       -151.404 | 2019-11-15 15:44:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 253 | transect_9-2019-12-12          | trajectoryProfile |       59.596  |       -151.357 | 2019-12-12 15:32:00 |       59.5702 |       -151.404 | 2019-12-12 14:00:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 254 | transect_9-2020-02-06          | trajectoryProfile |       59.5794 |       -151.357 | 2020-02-06 14:30:00 |       59.5702 |       -151.379 | 2020-02-06 13:55:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 255 | transect_9-2020-03-18          | trajectoryProfile |       59.596  |       -151.357 | 2020-03-18 15:46:00 |       59.5702 |       -151.404 | 2020-03-18 14:20:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 256 | transect_9-2020-06-04          | trajectoryProfile |       59.596  |       -151.357 | 2020-06-04 12:39:00 |       59.5702 |       -151.404 | 2020-06-04 11:24:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 257 | transect_9-2020-07-24          | trajectoryProfile |       59.596  |       -151.357 | 2020-07-24 14:45:00 |       59.5702 |       -151.404 | 2020-07-24 13:02:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 258 | transect_9-2020-08-14          | trajectoryProfile |       59.596  |       -151.357 | 2020-08-14 15:15:00 |       59.5702 |       -151.404 | 2020-08-14 13:47:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 259 | transect_9-2020-09-21          | trajectoryProfile |       59.596  |       -151.357 | 2020-09-21 11:12:00 |       59.5702 |       -151.404 | 2020-09-21 09:35:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 260 | transect_9-2020-10-15          | trajectoryProfile |       59.5925 |       -151.357 | 2020-10-15 15:43:00 |       59.5702 |       -151.399 | 2020-10-15 14:32:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 261 | transect_9-2020-12-28          | trajectoryProfile |       59.596  |       -151.357 | 2020-12-28 11:54:00 |       59.5702 |       -151.404 | 2020-12-28 10:50:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 262 | transect_9-2021-01-13          | trajectoryProfile |       59.596  |       -151.357 | 2021-01-13 15:24:00 |       59.5702 |       -151.404 | 2021-01-13 14:11:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 263 | transect_9-2021-02-17          | trajectoryProfile |       59.596  |       -151.357 | 2021-02-17 14:47:00 |       59.5702 |       -151.404 | 2021-02-17 13:36:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 264 | transect_9-2021-03-23          | trajectoryProfile |       59.596  |       -151.357 | 2021-03-23 16:30:00 |       59.5702 |       -151.404 | 2021-03-23 15:08:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 265 | transect_9-2021-04-16          | trajectoryProfile |       59.596  |       -151.357 | 2021-04-16 17:52:00 |       59.5702 |       -151.404 | 2021-04-16 16:37:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 266 | transect_9-2021-05-06          | trajectoryProfile |       59.596  |       -151.357 | 2021-05-06 16:01:00 |       59.5702 |       -151.404 | 2021-05-06 14:42:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 267 | transect_9-2021-06-21          | trajectoryProfile |       59.5925 |       -151.357 | 2021-06-21 15:21:00 |       59.5702 |       -151.399 | 2021-06-21 14:05:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 268 | transect_9-2021-07-16          | trajectoryProfile |       59.596  |       -151.357 | 2021-07-16 11:34:00 |       59.5702 |       -151.404 | 2021-07-16 09:37:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 269 | transect_9-2021-08-17          | trajectoryProfile |       59.596  |       -151.357 | 2021-08-17 16:16:00 |       59.5702 |       -151.404 | 2021-08-17 14:45:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 270 | transect_9-2021-09-17          | trajectoryProfile |       59.596  |       -151.357 | 2021-09-17 14:37:00 |       59.5702 |       -151.404 | 2021-09-17 13:13:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 271 | transect_9-2021-10-21          | trajectoryProfile |       59.596  |       -151.357 | 2021-10-21 16:39:00 |       59.5702 |       -151.404 | 2021-10-21 15:07:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 272 | transect_9-2021-11-14          | trajectoryProfile |       59.596  |       -151.357 | 2021-11-14 16:06:00 |       59.5702 |       -151.404 | 2021-11-14 14:33:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 273 | transect_9-2021-12-18          | trajectoryProfile |       59.596  |       -151.357 | 2021-12-18 15:11:00 |       59.5702 |       -151.404 | 2021-12-18 13:53:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 274 | transect_9-2022-01-31          | trajectoryProfile |       59.596  |       -151.357 | 2022-01-31 15:33:00 |       59.5702 |       -151.404 | 2022-01-31 14:08:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 275 | transect_9-2022-03-01          | trajectoryProfile |       59.596  |       -151.357 | 2022-03-01 14:36:00 |       59.5702 |       -151.404 | 2022-03-01 13:22:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 276 | transect_9-2022-03-22          | trajectoryProfile |       59.596  |       -151.357 | 2022-03-22 13:19:00 |       59.5702 |       -151.404 | 2022-03-22 12:05:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 277 | transect_9-2022-04-13          | trajectoryProfile |       59.596  |       -151.357 | 2022-04-13 13:00:00 |       59.5702 |       -151.404 | 2022-04-13 11:57:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 278 | transect_9-2022-05-23          | trajectoryProfile |       59.596  |       -151.357 | 2022-05-23 15:45:00 |       59.5702 |       -151.404 | 2022-05-23 14:38:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 279 | transect_9-2022-06-24          | trajectoryProfile |       59.596  |       -151.357 | 2022-06-24 15:32:00 |       59.5702 |       -151.404 | 2022-06-24 14:19:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 280 | transect_9-2022-07-23          | trajectoryProfile |       59.596  |       -151.357 | 2022-07-23 14:34:00 |       59.5702 |       -151.404 | 2022-07-23 13:23:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 281 | transect_9-2022-08-24          | trajectoryProfile |       59.596  |       -151.357 | 2022-08-24 15:06:00 |       59.5702 |       -151.404 | 2022-08-24 14:08:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 282 | transect_AlongBay-2012-08-15   | trajectoryProfile |       59.742  |       -151.057 | 2012-08-15 11:26:00 |       59.5    |       -151.888 | 2012-08-15 09:35:00 | https://researchworkspace.com/files/42203150/CookInletKachemakBay_CTD_2012_subsetted.csv |
| 283 | transect_AlongBay-2013-02-12   | trajectoryProfile |       59.742  |       -151.057 | 2013-02-12 23:59:00 |       59.5    |       -151.888 | 2013-02-12 16:35:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 284 | transect_AlongBay-2013-02-13_A | trajectoryProfile |       59.7203 |       -151.125 | 2013-02-13 00:27:00 |       59.7203 |       -151.125 | 2013-02-13 00:27:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 285 | transect_AlongBay-2013-02-13_B | trajectoryProfile |       59.7203 |       -151.125 | 2013-02-13 00:30:00 |       59.7203 |       -151.125 | 2013-02-13 00:30:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 286 | transect_AlongBay-2013-06-06   | trajectoryProfile |       59.742  |       -151.057 | 2013-06-06 13:44:00 |       59.5    |       -151.888 | 2013-06-06 12:06:00 | https://researchworkspace.com/files/42203152/CookInletKachemakBay_CTD_2013_subsetted.csv |
| 287 | transect_AlongBay-2014-03-28   | trajectoryProfile |       59.6583 |       -151.208 | 2014-03-28 17:31:00 |       59.5    |       -151.888 | 2014-03-28 11:56:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 288 | transect_AlongBay-2014-05-28   | trajectoryProfile |       59.632  |       -151.25  | 2014-05-28 14:38:00 |       59.525  |       -151.65  | 2014-05-28 10:49:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 289 | transect_AlongBay-2014-08-14   | trajectoryProfile |       59.742  |       -151.057 | 2014-08-14 14:25:00 |       59.5    |       -151.888 | 2014-08-14 09:20:00 | https://researchworkspace.com/files/42203153/CookInletKachemakBay_CTD_2014_subsetted.csv |
| 290 | transect_AlongBay-2015-07-10   | trajectoryProfile |       59.742  |       -151.057 | 2015-07-10 17:54:00 |       59.445  |       -152     | 2015-07-10 12:43:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 291 | transect_AlongBay-2015-08-14   | trajectoryProfile |       59.563  |       -151.46  | 2015-08-14 16:26:00 |       59.445  |       -152     | 2015-08-14 14:15:00 | https://researchworkspace.com/files/42203154/CookInletKachemakBay_CTD_2015_subsetted.csv |
| 292 | transect_AlongBay-2016-01-07   | trajectoryProfile |       59.613  |       -151.295 | 2016-01-07 15:56:00 |       59.552  |       -151.53  | 2016-01-07 14:47:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 293 | transect_AlongBay-2016-05-12   | trajectoryProfile |       59.632  |       -151.25  | 2016-05-12 20:00:00 |       59.383  |       -152.05  | 2016-05-12 16:02:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 294 | transect_AlongBay-2016-06-16   | trajectoryProfile |       59.712  |       -151.116 | 2016-06-16 16:36:00 |       59.525  |       -151.65  | 2016-06-16 14:36:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 295 | transect_AlongBay-2016-07-27   | trajectoryProfile |       59.632  |       -151.25  | 2016-07-27 16:50:00 |       59.5    |       -151.888 | 2016-07-27 14:59:00 | https://researchworkspace.com/files/42203155/CookInletKachemakBay_CTD_2016_subsetted.csv |
| 296 | transect_AlongBay-2017-01-11   | trajectoryProfile |       59.5824 |       -151.385 | 2017-01-11 15:52:00 |       59.525  |       -151.65  | 2017-01-11 15:04:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 297 | transect_AlongBay-2017-02-07   | trajectoryProfile |       59.592  |       -151.35  | 2017-02-07 16:49:00 |       59.5    |       -151.888 | 2017-02-07 13:02:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 298 | transect_AlongBay-2017-03-28   | trajectoryProfile |       59.6583 |       -151.208 | 2017-03-28 13:14:00 |       59.5    |       -151.888 | 2017-03-28 10:49:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 299 | transect_AlongBay-2017-04-20   | trajectoryProfile |       59.613  |       -151.295 | 2017-04-20 20:20:00 |       59.5    |       -151.888 | 2017-04-20 16:57:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 300 | transect_AlongBay-2017-05-30   | trajectoryProfile |       59.687  |       -151.165 | 2017-05-30 16:37:00 |       59.525  |       -151.65  | 2017-05-30 14:28:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 301 | transect_AlongBay-2017-06-28   | trajectoryProfile |       59.632  |       -151.25  | 2017-06-28 15:27:00 |       59.525  |       -151.65  | 2017-06-28 13:47:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 302 | transect_AlongBay-2017-07-24   | trajectoryProfile |       59.742  |       -151.057 | 2017-07-24 14:59:00 |       59.525  |       -151.65  | 2017-07-24 12:13:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 303 | transect_AlongBay-2017-07-26   | trajectoryProfile |       59.552  |       -151.53  | 2017-07-26 10:46:00 |       59.383  |       -152.05  | 2017-07-26 09:18:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 304 | transect_AlongBay-2017-08-24   | trajectoryProfile |       59.742  |       -151.057 | 2017-08-24 16:22:00 |       59.525  |       -151.65  | 2017-08-24 14:03:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 305 | transect_AlongBay-2017-09-22   | trajectoryProfile |       59.742  |       -151.057 | 2017-09-22 13:26:00 |       59.5    |       -151.888 | 2017-09-22 10:39:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 306 | transect_AlongBay-2017-10-20   | trajectoryProfile |       59.742  |       -151.057 | 2017-10-20 14:02:00 |       59.518  |       -151.728 | 2017-10-20 11:01:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 307 | transect_AlongBay-2017-11-02   | trajectoryProfile |       59.5824 |       -151.385 | 2017-11-02 17:10:00 |       59.383  |       -152.05  | 2017-11-02 15:04:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 308 | transect_AlongBay-2017-11-07   | trajectoryProfile |       59.742  |       -151.057 | 2017-11-07 14:55:00 |       59.5    |       -151.888 | 2017-11-07 11:49:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 309 | transect_AlongBay-2017-12-14   | trajectoryProfile |       59.6583 |       -151.208 | 2017-12-14 14:33:00 |       59.525  |       -151.65  | 2017-12-14 12:53:00 | https://researchworkspace.com/files/42203156/CookInletKachemakBay_CTD_2017_subsetted.csv |
| 310 | transect_AlongBay-2018-01-17   | trajectoryProfile |       59.687  |       -151.165 | 2018-01-17 12:41:00 |       59.525  |       -151.65  | 2018-01-17 10:45:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 311 | transect_AlongBay-2018-03-02   | trajectoryProfile |       59.6583 |       -151.208 | 2018-03-02 14:15:00 |       59.5    |       -151.888 | 2018-03-02 11:40:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 312 | transect_AlongBay-2018-03-27   | trajectoryProfile |       59.712  |       -151.116 | 2018-03-27 16:38:00 |       59.383  |       -152.05  | 2018-03-27 13:18:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 313 | transect_AlongBay-2018-04-23   | trajectoryProfile |       59.742  |       -151.057 | 2018-04-23 18:30:00 |       59.5    |       -151.888 | 2018-04-23 15:40:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 314 | transect_AlongBay-2018-05-24   | trajectoryProfile |       59.742  |       -151.057 | 2018-05-24 13:24:00 |       59.5    |       -151.888 | 2018-05-24 10:31:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 315 | transect_AlongBay-2018-06-22   | trajectoryProfile |       59.742  |       -151.057 | 2018-06-22 13:06:00 |       59.5    |       -151.888 | 2018-06-22 10:13:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 316 | transect_AlongBay-2018-07-18   | trajectoryProfile |       59.742  |       -151.057 | 2018-07-18 16:42:00 |       59.383  |       -152.05  | 2018-07-18 13:19:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 317 | transect_AlongBay-2018-08-23   | trajectoryProfile |       59.742  |       -151.057 | 2018-08-23 13:37:00 |       59.5    |       -151.888 | 2018-08-23 10:28:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 318 | transect_AlongBay-2018-09-17   | trajectoryProfile |       59.742  |       -151.057 | 2018-09-17 17:35:00 |       59.383  |       -152.05  | 2018-09-17 14:08:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 319 | transect_AlongBay-2018-10-17   | trajectoryProfile |       59.742  |       -151.057 | 2018-10-17 13:39:00 |       59.5    |       -151.888 | 2018-10-17 10:33:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 320 | transect_AlongBay-2018-11-08   | trajectoryProfile |       59.742  |       -151.057 | 2018-11-08 12:53:00 |       59.552  |       -151.53  | 2018-11-08 10:47:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 321 | transect_AlongBay-2018-12-06   | trajectoryProfile |       59.742  |       -151.057 | 2018-12-06 13:54:00 |       59.5    |       -151.888 | 2018-12-06 10:53:00 | https://researchworkspace.com/files/42203157/CookInletKachemakBay_CTD_2018_subsetted.csv |
| 322 | transect_AlongBay-2019-02-07   | trajectoryProfile |       59.742  |       -151.057 | 2019-02-07 14:44:00 |       59.552  |       -151.53  | 2019-02-07 12:45:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 323 | transect_AlongBay-2019-03-19   | trajectoryProfile |       59.742  |       -151.057 | 2019-03-19 12:34:00 |       59.5    |       -151.888 | 2019-03-19 09:13:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 324 | transect_AlongBay-2019-04-24   | trajectoryProfile |       59.742  |       -151.057 | 2019-04-24 12:58:00 |       59.518  |       -151.728 | 2019-04-24 09:58:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 325 | transect_AlongBay-2019-05-14   | trajectoryProfile |       59.742  |       -151.057 | 2019-05-14 16:45:00 |       59.5    |       -151.888 | 2019-05-14 14:00:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 326 | transect_AlongBay-2019-06-19   | trajectoryProfile |       59.712  |       -151.116 | 2019-06-19 14:53:00 |       59.5    |       -151.888 | 2019-06-19 11:21:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 327 | transect_AlongBay-2019-07-23   | trajectoryProfile |       59.742  |       -151.057 | 2019-07-23 14:36:00 |       59.5    |       -151.888 | 2019-07-23 11:05:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 328 | transect_AlongBay-2019-10-30   | trajectoryProfile |       59.742  |       -151.057 | 2019-10-30 13:46:00 |       59.518  |       -151.728 | 2019-10-30 10:43:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 329 | transect_AlongBay-2019-11-15   | trajectoryProfile |       59.742  |       -151.057 | 2019-11-15 15:06:00 |       59.518  |       -151.728 | 2019-11-15 11:52:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 330 | transect_AlongBay-2019-12-12   | trajectoryProfile |       59.687  |       -151.165 | 2019-12-12 13:32:00 |       59.518  |       -151.728 | 2019-12-12 10:38:00 | https://researchworkspace.com/files/42203158/CookInletKachemakBay_CTD_2019_subsetted.csv |
| 331 | transect_AlongBay-2020-02-06   | trajectoryProfile |       59.742  |       -151.057 | 2020-02-06 13:20:00 |       59.518  |       -151.728 | 2020-02-06 10:28:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 332 | transect_AlongBay-2020-03-18   | trajectoryProfile |       59.742  |       -151.057 | 2020-03-18 13:42:00 |       59.518  |       -151.728 | 2020-03-18 10:27:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 333 | transect_AlongBay-2020-06-04   | trajectoryProfile |       59.742  |       -151.057 | 2020-06-04 14:17:00 |       59.5    |       -151.888 | 2020-06-04 09:48:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 334 | transect_AlongBay-2020-07-08   | trajectoryProfile |       59.742  |       -151.057 | 2020-07-08 16:53:00 |       59.5824 |       -151.385 | 2020-07-08 15:22:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 335 | transect_AlongBay-2020-07-23   | trajectoryProfile |       59.742  |       -151.057 | 2020-07-23 15:00:00 |       59.5    |       -151.888 | 2020-07-23 12:15:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 336 | transect_AlongBay-2020-08-14   | trajectoryProfile |       59.742  |       -151.057 | 2020-08-14 13:10:00 |       59.5    |       -151.888 | 2020-08-14 09:56:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 337 | transect_AlongBay-2020-09-20   | trajectoryProfile |       59.742  |       -151.057 | 2020-09-20 15:44:00 |       59.383  |       -152.05  | 2020-09-20 12:24:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 338 | transect_AlongBay-2020-10-15   | trajectoryProfile |       59.742  |       -151.057 | 2020-10-15 13:59:00 |       59.5    |       -151.888 | 2020-10-15 11:07:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 339 | transect_AlongBay-2020-12-28   | trajectoryProfile |       59.742  |       -151.057 | 2020-12-28 14:41:00 |       59.525  |       -151.65  | 2020-12-28 12:42:00 | https://researchworkspace.com/files/42203159/CookInletKachemakBay_CTD_2020_subsetted.csv |
| 340 | transect_AlongBay-2021-01-13   | trajectoryProfile |       59.687  |       -151.165 | 2021-01-13 13:46:00 |       59.518  |       -151.728 | 2021-01-13 11:20:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 341 | transect_AlongBay-2021-02-16   | trajectoryProfile |       59.687  |       -151.165 | 2021-02-16 16:43:00 |       59.383  |       -152.05  | 2021-02-16 13:51:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 342 | transect_AlongBay-2021-03-23   | trajectoryProfile |       59.687  |       -151.165 | 2021-03-23 14:41:00 |       59.518  |       -151.728 | 2021-03-23 11:57:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 343 | transect_AlongBay-2021-04-14   | trajectoryProfile |       59.5824 |       -151.385 | 2021-04-14 22:00:00 |       59.383  |       -152.05  | 2021-04-14 18:52:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 344 | transect_AlongBay-2021-04-16   | trajectoryProfile |       59.687  |       -151.165 | 2021-04-16 16:11:00 |       59.518  |       -151.728 | 2021-04-16 14:04:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 345 | transect_AlongBay-2021-05-06   | trajectoryProfile |       59.742  |       -151.057 | 2021-05-06 13:41:00 |       59.5    |       -151.888 | 2021-05-06 10:19:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 346 | transect_AlongBay-2021-06-21   | trajectoryProfile |       59.742  |       -151.057 | 2021-06-21 13:28:00 |       59.518  |       -151.728 | 2021-06-21 10:23:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 347 | transect_AlongBay-2021-07-21   | trajectoryProfile |       59.742  |       -151.057 | 2021-07-21 16:51:00 |       59.383  |       -152.05  | 2021-07-21 13:18:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 348 | transect_AlongBay-2021-08-17   | trajectoryProfile |       59.742  |       -151.057 | 2021-08-17 14:06:00 |       59.5    |       -151.888 | 2021-08-17 10:30:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 349 | transect_AlongBay-2021-10-04   | trajectoryProfile |       59.742  |       -151.057 | 2021-10-04 14:41:00 |       59.5    |       -151.888 | 2021-10-04 11:30:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 350 | transect_AlongBay-2021-10-05   | trajectoryProfile |       59.445  |       -152     | 2021-10-05 13:04:00 |       59.383  |       -152.05  | 2021-10-05 12:50:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 351 | transect_AlongBay-2021-10-21   | trajectoryProfile |       59.742  |       -151.057 | 2021-10-21 14:31:00 |       59.518  |       -151.728 | 2021-10-21 10:46:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 352 | transect_AlongBay-2021-11-14   | trajectoryProfile |       59.742  |       -151.057 | 2021-11-14 13:53:00 |       59.518  |       -151.728 | 2021-11-14 10:32:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 353 | transect_AlongBay-2021-12-18   | trajectoryProfile |       59.687  |       -151.165 | 2021-12-18 13:30:00 |       59.518  |       -151.728 | 2021-12-18 10:48:00 | https://researchworkspace.com/files/42203160/CookInletKachemakBay_CTD_2021_subsetted.csv |
| 354 | transect_AlongBay-2022-01-31   | trajectoryProfile |       59.687  |       -151.165 | 2022-01-31 13:28:00 |       59.518  |       -151.728 | 2022-01-31 10:35:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 355 | transect_AlongBay-2022-02-28   | trajectoryProfile |       59.687  |       -151.165 | 2022-02-28 15:23:00 |       59.383  |       -152.05  | 2022-02-28 12:23:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 356 | transect_AlongBay-2022-03-21   | trajectoryProfile |       59.687  |       -151.165 | 2022-03-21 16:06:00 |       59.518  |       -151.728 | 2022-03-21 13:33:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 357 | transect_AlongBay-2022-04-12   | trajectoryProfile |       59.742  |       -151.057 | 2022-04-12 15:13:00 |       59.383  |       -152.05  | 2022-04-12 11:10:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 358 | transect_AlongBay-2022-05-23   | trajectoryProfile |       59.742  |       -151.057 | 2022-05-23 13:58:00 |       59.5    |       -151.888 | 2022-05-23 10:34:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 359 | transect_AlongBay-2022-06-24   | trajectoryProfile |       59.742  |       -151.057 | 2022-06-24 13:41:00 |       59.5    |       -151.888 | 2022-06-24 10:12:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 360 | transect_AlongBay-2022-07-21   | trajectoryProfile |       59.742  |       -151.057 | 2022-07-21 16:24:00 |       59.383  |       -152.05  | 2022-07-21 12:25:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |
| 361 | transect_AlongBay-2022-08-24   | trajectoryProfile |       59.742  |       -151.057 | 2022-08-24 13:20:00 |       59.5    |       -151.888 | 2022-08-24 09:46:00 | https://researchworkspace.com/files/42203161/CookInletKachemakBay_CTD_2022_subsetted.csv |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_gwa"))
```

## Map of Transects
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_gwa")("ctd_profiles_gwa")
    
```

## transect_3

+++

transect_3-2012-05-02
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2012-05-02'].plot.salt() + cat['transect_3-2012-05-02'].plot.temp()
```

transect_3-2012-07-29
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2012-07-29'].plot.salt() + cat['transect_3-2012-07-29'].plot.temp()
```

transect_3-2012-10-29
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2012-10-29'].plot.salt() + cat['transect_3-2012-10-29'].plot.temp()
```

transect_3-2013-04-20
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2013-04-20'].plot.salt() + cat['transect_3-2013-04-20'].plot.temp()
```

transect_3-2013-07-19
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2013-07-19'].plot.salt() + cat['transect_3-2013-07-19'].plot.temp()
```

transect_3-2013-11-08
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2013-11-08'].plot.salt() + cat['transect_3-2013-11-08'].plot.temp()
```

transect_3-2014-04-11
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2014-04-11'].plot.salt() + cat['transect_3-2014-04-11'].plot.temp()
```

transect_3-2014-07-22
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2014-07-22'].plot.salt() + cat['transect_3-2014-07-22'].plot.temp()
```

transect_3-2014-10-13
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2014-10-13'].plot.salt() + cat['transect_3-2014-10-13'].plot.temp()
```

transect_3-2015-02-22
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2015-02-22'].plot.salt() + cat['transect_3-2015-02-22'].plot.temp()
```

transect_3-2015-04-12
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2015-04-12'].plot.salt() + cat['transect_3-2015-04-12'].plot.temp()
```

transect_3-2015-11-04
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2015-11-04'].plot.salt() + cat['transect_3-2015-11-04'].plot.temp()
```

transect_3-2016-02-14
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2016-02-14'].plot.salt() + cat['transect_3-2016-02-14'].plot.temp()
```

transect_3-2016-04-11
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2016-04-11'].plot.salt() + cat['transect_3-2016-04-11'].plot.temp()
```

transect_3-2016-08-29
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2016-08-29'].plot.salt() + cat['transect_3-2016-08-29'].plot.temp()
```

transect_3-2017-04-19
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2017-04-19'].plot.salt() + cat['transect_3-2017-04-19'].plot.temp()
```

transect_3-2017-07-25
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2017-07-25'].plot.salt() + cat['transect_3-2017-07-25'].plot.temp()
```

transect_3-2018-06-25
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2018-06-25'].plot.salt() + cat['transect_3-2018-06-25'].plot.temp()
```

transect_3-2018-07-26
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2018-07-26'].plot.salt() + cat['transect_3-2018-07-26'].plot.temp()
```

transect_3-2018-09-13
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2018-09-13'].plot.salt() + cat['transect_3-2018-09-13'].plot.temp()
```

transect_3-2019-02-08
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2019-02-08'].plot.salt() + cat['transect_3-2019-02-08'].plot.temp()
```

transect_3-2019-05-14
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2019-05-14'].plot.salt() + cat['transect_3-2019-05-14'].plot.temp()
```

transect_3-2019-07-25
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2019-07-25'].plot.salt() + cat['transect_3-2019-07-25'].plot.temp()
```

transect_3-2019-09-16
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2019-09-16'].plot.salt() + cat['transect_3-2019-09-16'].plot.temp()
```

transect_3-2020-07-29
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2020-07-29'].plot.salt() + cat['transect_3-2020-07-29'].plot.temp()
```

transect_3-2021-04-16
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2021-04-16'].plot.salt() + cat['transect_3-2021-04-16'].plot.temp()
```

transect_3-2021-07-16
        

```{code-cell}
:tags: [full-width]

cat['transect_3-2021-07-16'].plot.salt() + cat['transect_3-2021-07-16'].plot.temp()
```

## transect_4

+++

transect_4-2012-05-02
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-05-02'].plot.salt() + cat['transect_4-2012-05-02'].plot.temp()
```

transect_4-2012-05-31
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-05-31'].plot.salt() + cat['transect_4-2012-05-31'].plot.temp()
```

transect_4-2012-06-05_A
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-06-05_A'].plot.salt() + cat['transect_4-2012-06-05_A'].plot.temp()
```

transect_4-2012-06-05_B
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-06-05_B'].plot.salt() + cat['transect_4-2012-06-05_B'].plot.temp()
```

transect_4-2012-07-31
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-07-31'].plot.salt() + cat['transect_4-2012-07-31'].plot.temp()
```

transect_4-2012-08-15
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-08-15'].plot.salt() + cat['transect_4-2012-08-15'].plot.temp()
```

transect_4-2012-10-29
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2012-10-29'].plot.salt() + cat['transect_4-2012-10-29'].plot.temp()
```

transect_4-2013-02-12
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2013-02-12'].plot.salt() + cat['transect_4-2013-02-12'].plot.temp()
```

transect_4-2013-04-21
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2013-04-21'].plot.salt() + cat['transect_4-2013-04-21'].plot.temp()
```

transect_4-2013-06-06
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2013-06-06'].plot.salt() + cat['transect_4-2013-06-06'].plot.temp()
```

transect_4-2013-07-19
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2013-07-19'].plot.salt() + cat['transect_4-2013-07-19'].plot.temp()
```

transect_4-2013-10-29
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2013-10-29'].plot.salt() + cat['transect_4-2013-10-29'].plot.temp()
```

transect_4-2014-02-15
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2014-02-15'].plot.salt() + cat['transect_4-2014-02-15'].plot.temp()
```

transect_4-2014-04-11
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2014-04-11'].plot.salt() + cat['transect_4-2014-04-11'].plot.temp()
```

transect_4-2014-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2014-07-21'].plot.salt() + cat['transect_4-2014-07-21'].plot.temp()
```

transect_4-2014-08-13
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2014-08-13'].plot.salt() + cat['transect_4-2014-08-13'].plot.temp()
```

transect_4-2014-10-13
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2014-10-13'].plot.salt() + cat['transect_4-2014-10-13'].plot.temp()
```

transect_4-2015-02-12
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-02-12'].plot.salt() + cat['transect_4-2015-02-12'].plot.temp()
```

transect_4-2015-02-24
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-02-24'].plot.salt() + cat['transect_4-2015-02-24'].plot.temp()
```

transect_4-2015-04-08
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-04-08'].plot.salt() + cat['transect_4-2015-04-08'].plot.temp()
```

transect_4-2015-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-08-14'].plot.salt() + cat['transect_4-2015-08-14'].plot.temp()
```

transect_4-2015-09-24
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-09-24'].plot.salt() + cat['transect_4-2015-09-24'].plot.temp()
```

transect_4-2015-10-19
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-10-19'].plot.salt() + cat['transect_4-2015-10-19'].plot.temp()
```

transect_4-2015-11-03
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-11-03'].plot.salt() + cat['transect_4-2015-11-03'].plot.temp()
```

transect_4-2015-11-04
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-11-04'].plot.salt() + cat['transect_4-2015-11-04'].plot.temp()
```

transect_4-2015-12-10
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2015-12-10'].plot.salt() + cat['transect_4-2015-12-10'].plot.temp()
```

transect_4-2016-02-09
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2016-02-09'].plot.salt() + cat['transect_4-2016-02-09'].plot.temp()
```

transect_4-2016-04-11
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2016-04-11'].plot.salt() + cat['transect_4-2016-04-11'].plot.temp()
```

transect_4-2016-07-27
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2016-07-27'].plot.salt() + cat['transect_4-2016-07-27'].plot.temp()
```

transect_4-2016-10-13
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2016-10-13'].plot.salt() + cat['transect_4-2016-10-13'].plot.temp()
```

transect_4-2016-12-13
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2016-12-13'].plot.salt() + cat['transect_4-2016-12-13'].plot.temp()
```

transect_4-2017-04-20
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2017-04-20'].plot.salt() + cat['transect_4-2017-04-20'].plot.temp()
```

transect_4-2017-07-25
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2017-07-25'].plot.salt() + cat['transect_4-2017-07-25'].plot.temp()
```

transect_4-2017-10-17
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2017-10-17'].plot.salt() + cat['transect_4-2017-10-17'].plot.temp()
```

transect_4-2018-04-23
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2018-04-23'].plot.salt() + cat['transect_4-2018-04-23'].plot.temp()
```

transect_4-2018-06-25
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2018-06-25'].plot.salt() + cat['transect_4-2018-06-25'].plot.temp()
```

transect_4-2018-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2018-07-24'].plot.salt() + cat['transect_4-2018-07-24'].plot.temp()
```

transect_4-2018-09-13
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2018-09-13'].plot.salt() + cat['transect_4-2018-09-13'].plot.temp()
```

transect_4-2019-02-07
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2019-02-07'].plot.salt() + cat['transect_4-2019-02-07'].plot.temp()
```

transect_4-2019-05-14
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2019-05-14'].plot.salt() + cat['transect_4-2019-05-14'].plot.temp()
```

transect_4-2019-07-25
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2019-07-25'].plot.salt() + cat['transect_4-2019-07-25'].plot.temp()
```

transect_4-2019-09-16
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2019-09-16'].plot.salt() + cat['transect_4-2019-09-16'].plot.temp()
```

transect_4-2020-02-14
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2020-02-14'].plot.salt() + cat['transect_4-2020-02-14'].plot.temp()
```

transect_4-2020-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2020-07-23'].plot.salt() + cat['transect_4-2020-07-23'].plot.temp()
```

transect_4-2020-09-21
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2020-09-21'].plot.salt() + cat['transect_4-2020-09-21'].plot.temp()
```

transect_4-2021-02-17
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2021-02-17'].plot.salt() + cat['transect_4-2021-02-17'].plot.temp()
```

transect_4-2021-04-16
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2021-04-16'].plot.salt() + cat['transect_4-2021-04-16'].plot.temp()
```

transect_4-2021-07-16
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2021-07-16'].plot.salt() + cat['transect_4-2021-07-16'].plot.temp()
```

transect_4-2021-09-17
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2021-09-17'].plot.salt() + cat['transect_4-2021-09-17'].plot.temp()
```

transect_4-2022-03-01
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2022-03-01'].plot.salt() + cat['transect_4-2022-03-01'].plot.temp()
```

transect_4-2022-04-13
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2022-04-13'].plot.salt() + cat['transect_4-2022-04-13'].plot.temp()
```

transect_4-2022-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_4-2022-07-23'].plot.salt() + cat['transect_4-2022-07-23'].plot.temp()
```

## transect_6

+++

transect_6-2012-05-03
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2012-05-03'].plot.salt() + cat['transect_6-2012-05-03'].plot.temp()
```

transect_6-2012-07-30
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2012-07-30'].plot.salt() + cat['transect_6-2012-07-30'].plot.temp()
```

transect_6-2012-10-28
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2012-10-28'].plot.salt() + cat['transect_6-2012-10-28'].plot.temp()
```

transect_6-2013-04-19
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2013-04-19'].plot.salt() + cat['transect_6-2013-04-19'].plot.temp()
```

transect_6-2013-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2013-07-21'].plot.salt() + cat['transect_6-2013-07-21'].plot.temp()
```

transect_6-2013-11-06
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2013-11-06'].plot.salt() + cat['transect_6-2013-11-06'].plot.temp()
```

transect_6-2014-04-06
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2014-04-06'].plot.salt() + cat['transect_6-2014-04-06'].plot.temp()
```

transect_6-2014-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2014-07-23'].plot.salt() + cat['transect_6-2014-07-23'].plot.temp()
```

transect_6-2014-10-18
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2014-10-18'].plot.salt() + cat['transect_6-2014-10-18'].plot.temp()
```

transect_6-2015-02-23
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2015-02-23'].plot.salt() + cat['transect_6-2015-02-23'].plot.temp()
```

transect_6-2015-04-08
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2015-04-08'].plot.salt() + cat['transect_6-2015-04-08'].plot.temp()
```

transect_6-2015-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2015-08-14'].plot.salt() + cat['transect_6-2015-08-14'].plot.temp()
```

transect_6-2016-02-15
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2016-02-15'].plot.salt() + cat['transect_6-2016-02-15'].plot.temp()
```

transect_6-2016-04-10
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2016-04-10'].plot.salt() + cat['transect_6-2016-04-10'].plot.temp()
```

transect_6-2016-08-31
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2016-08-31'].plot.salt() + cat['transect_6-2016-08-31'].plot.temp()
```

transect_6-2016-12-12
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2016-12-12'].plot.salt() + cat['transect_6-2016-12-12'].plot.temp()
```

transect_6-2017-04-18
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2017-04-18'].plot.salt() + cat['transect_6-2017-04-18'].plot.temp()
```

transect_6-2017-07-26
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2017-07-26'].plot.salt() + cat['transect_6-2017-07-26'].plot.temp()
```

transect_6-2017-11-02
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2017-11-02'].plot.salt() + cat['transect_6-2017-11-02'].plot.temp()
```

transect_6-2018-07-18
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2018-07-18'].plot.salt() + cat['transect_6-2018-07-18'].plot.temp()
```

transect_6-2018-09-17
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2018-09-17'].plot.salt() + cat['transect_6-2018-09-17'].plot.temp()
```

transect_6-2019-02-08
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2019-02-08'].plot.salt() + cat['transect_6-2019-02-08'].plot.temp()
```

transect_6-2019-05-12
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2019-05-12'].plot.salt() + cat['transect_6-2019-05-12'].plot.temp()
```

transect_6-2019-07-25
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2019-07-25'].plot.salt() + cat['transect_6-2019-07-25'].plot.temp()
```

transect_6-2020-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2020-07-24'].plot.salt() + cat['transect_6-2020-07-24'].plot.temp()
```

transect_6-2020-09-20
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2020-09-20'].plot.salt() + cat['transect_6-2020-09-20'].plot.temp()
```

transect_6-2021-02-16
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2021-02-16'].plot.salt() + cat['transect_6-2021-02-16'].plot.temp()
```

transect_6-2021-04-14
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2021-04-14'].plot.salt() + cat['transect_6-2021-04-14'].plot.temp()
```

transect_6-2021-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2021-07-21'].plot.salt() + cat['transect_6-2021-07-21'].plot.temp()
```

transect_6-2021-10-05
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2021-10-05'].plot.salt() + cat['transect_6-2021-10-05'].plot.temp()
```

transect_6-2022-02-28
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2022-02-28'].plot.salt() + cat['transect_6-2022-02-28'].plot.temp()
```

transect_6-2022-04-12
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2022-04-12'].plot.salt() + cat['transect_6-2022-04-12'].plot.temp()
```

transect_6-2022-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_6-2022-07-21'].plot.salt() + cat['transect_6-2022-07-21'].plot.temp()
```

## transect_7

+++

transect_7-2012-07-30
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2012-07-30'].plot.salt() + cat['transect_7-2012-07-30'].plot.temp()
```

transect_7-2012-10-28
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2012-10-28'].plot.salt() + cat['transect_7-2012-10-28'].plot.temp()
```

transect_7-2013-04-20
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2013-04-20'].plot.salt() + cat['transect_7-2013-04-20'].plot.temp()
```

transect_7-2013-07-18
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2013-07-18'].plot.salt() + cat['transect_7-2013-07-18'].plot.temp()
```

transect_7-2014-02-17
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2014-02-17'].plot.salt() + cat['transect_7-2014-02-17'].plot.temp()
```

transect_7-2014-04-07
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2014-04-07'].plot.salt() + cat['transect_7-2014-04-07'].plot.temp()
```

transect_7-2014-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2014-07-24'].plot.salt() + cat['transect_7-2014-07-24'].plot.temp()
```

transect_7-2014-10-17
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2014-10-17'].plot.salt() + cat['transect_7-2014-10-17'].plot.temp()
```

transect_7-2014-10-18
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2014-10-18'].plot.salt() + cat['transect_7-2014-10-18'].plot.temp()
```

transect_7-2015-02-24
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2015-02-24'].plot.salt() + cat['transect_7-2015-02-24'].plot.temp()
```

transect_7-2015-04-13
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2015-04-13'].plot.salt() + cat['transect_7-2015-04-13'].plot.temp()
```

transect_7-2015-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2015-08-14'].plot.salt() + cat['transect_7-2015-08-14'].plot.temp()
```

transect_7-2016-02-16
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2016-02-16'].plot.salt() + cat['transect_7-2016-02-16'].plot.temp()
```

transect_7-2016-08-30
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2016-08-30'].plot.salt() + cat['transect_7-2016-08-30'].plot.temp()
```

transect_7-2016-12-13
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2016-12-13'].plot.salt() + cat['transect_7-2016-12-13'].plot.temp()
```

transect_7-2017-04-19
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2017-04-19'].plot.salt() + cat['transect_7-2017-04-19'].plot.temp()
```

transect_7-2017-07-26
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2017-07-26'].plot.salt() + cat['transect_7-2017-07-26'].plot.temp()
```

transect_7-2017-11-02
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2017-11-02'].plot.salt() + cat['transect_7-2017-11-02'].plot.temp()
```

transect_7-2018-03-27
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2018-03-27'].plot.salt() + cat['transect_7-2018-03-27'].plot.temp()
```

transect_7-2018-07-18
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2018-07-18'].plot.salt() + cat['transect_7-2018-07-18'].plot.temp()
```

transect_7-2018-09-17
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2018-09-17'].plot.salt() + cat['transect_7-2018-09-17'].plot.temp()
```

transect_7-2019-02-08
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2019-02-08'].plot.salt() + cat['transect_7-2019-02-08'].plot.temp()
```

transect_7-2019-05-12
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2019-05-12'].plot.salt() + cat['transect_7-2019-05-12'].plot.temp()
```

transect_7-2019-07-25
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2019-07-25'].plot.salt() + cat['transect_7-2019-07-25'].plot.temp()
```

transect_7-2019-09-19
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2019-09-19'].plot.salt() + cat['transect_7-2019-09-19'].plot.temp()
```

transect_7-2020-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2020-07-24'].plot.salt() + cat['transect_7-2020-07-24'].plot.temp()
```

transect_7-2020-09-20
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2020-09-20'].plot.salt() + cat['transect_7-2020-09-20'].plot.temp()
```

transect_7-2021-02-16
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2021-02-16'].plot.salt() + cat['transect_7-2021-02-16'].plot.temp()
```

transect_7-2021-04-14
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2021-04-14'].plot.salt() + cat['transect_7-2021-04-14'].plot.temp()
```

transect_7-2021-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2021-07-21'].plot.salt() + cat['transect_7-2021-07-21'].plot.temp()
```

transect_7-2021-10-05
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2021-10-05'].plot.salt() + cat['transect_7-2021-10-05'].plot.temp()
```

transect_7-2022-02-28
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2022-02-28'].plot.salt() + cat['transect_7-2022-02-28'].plot.temp()
```

transect_7-2022-04-12
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2022-04-12'].plot.salt() + cat['transect_7-2022-04-12'].plot.temp()
```

transect_7-2022-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_7-2022-07-21'].plot.salt() + cat['transect_7-2022-07-21'].plot.temp()
```

## transect_9

+++

transect_9-2012-02-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-02-14'].plot.salt() + cat['transect_9-2012-02-14'].plot.temp()
```

transect_9-2012-03-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-03-14'].plot.salt() + cat['transect_9-2012-03-14'].plot.temp()
```

transect_9-2012-04-10
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-04-10'].plot.salt() + cat['transect_9-2012-04-10'].plot.temp()
```

transect_9-2012-04-26
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-04-26'].plot.salt() + cat['transect_9-2012-04-26'].plot.temp()
```

transect_9-2012-05-31_A
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-05-31_A'].plot.salt() + cat['transect_9-2012-05-31_A'].plot.temp()
```

transect_9-2012-05-31_B
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-05-31_B'].plot.salt() + cat['transect_9-2012-05-31_B'].plot.temp()
```

transect_9-2012-06-05_A
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-06-05_A'].plot.salt() + cat['transect_9-2012-06-05_A'].plot.temp()
```

transect_9-2012-06-05_B
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-06-05_B'].plot.salt() + cat['transect_9-2012-06-05_B'].plot.temp()
```

transect_9-2012-06-27
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-06-27'].plot.salt() + cat['transect_9-2012-06-27'].plot.temp()
```

transect_9-2012-07-02
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-07-02'].plot.salt() + cat['transect_9-2012-07-02'].plot.temp()
```

transect_9-2012-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-07-21'].plot.salt() + cat['transect_9-2012-07-21'].plot.temp()
```

transect_9-2012-08-03
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-08-03'].plot.salt() + cat['transect_9-2012-08-03'].plot.temp()
```

transect_9-2012-08-15
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-08-15'].plot.salt() + cat['transect_9-2012-08-15'].plot.temp()
```

transect_9-2012-08-26
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-08-26'].plot.salt() + cat['transect_9-2012-08-26'].plot.temp()
```

transect_9-2012-08-31
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-08-31'].plot.salt() + cat['transect_9-2012-08-31'].plot.temp()
```

transect_9-2012-09-21_A
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-09-21_A'].plot.salt() + cat['transect_9-2012-09-21_A'].plot.temp()
```

transect_9-2012-09-21_B
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-09-21_B'].plot.salt() + cat['transect_9-2012-09-21_B'].plot.temp()
```

transect_9-2012-09-21_C
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-09-21_C'].plot.salt() + cat['transect_9-2012-09-21_C'].plot.temp()
```

transect_9-2012-09-21_D
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-09-21_D'].plot.salt() + cat['transect_9-2012-09-21_D'].plot.temp()
```

transect_9-2012-09-21_E
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-09-21_E'].plot.salt() + cat['transect_9-2012-09-21_E'].plot.temp()
```

transect_9-2012-10-12
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-10-12'].plot.salt() + cat['transect_9-2012-10-12'].plot.temp()
```

transect_9-2012-10-29
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2012-10-29'].plot.salt() + cat['transect_9-2012-10-29'].plot.temp()
```

transect_9-2013-01-04
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-01-04'].plot.salt() + cat['transect_9-2013-01-04'].plot.temp()
```

transect_9-2013-02-12
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-02-12'].plot.salt() + cat['transect_9-2013-02-12'].plot.temp()
```

transect_9-2013-03-15
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-03-15'].plot.salt() + cat['transect_9-2013-03-15'].plot.temp()
```

transect_9-2013-04-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-04-21'].plot.salt() + cat['transect_9-2013-04-21'].plot.temp()
```

transect_9-2013-05-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-05-21'].plot.salt() + cat['transect_9-2013-05-21'].plot.temp()
```

transect_9-2013-06-06
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-06-06'].plot.salt() + cat['transect_9-2013-06-06'].plot.temp()
```

transect_9-2013-06-19
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-06-19'].plot.salt() + cat['transect_9-2013-06-19'].plot.temp()
```

transect_9-2013-06-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-06-28'].plot.salt() + cat['transect_9-2013-06-28'].plot.temp()
```

transect_9-2013-07-05
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-07-05'].plot.salt() + cat['transect_9-2013-07-05'].plot.temp()
```

transect_9-2013-07-09
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-07-09'].plot.salt() + cat['transect_9-2013-07-09'].plot.temp()
```

transect_9-2013-07-22
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-07-22'].plot.salt() + cat['transect_9-2013-07-22'].plot.temp()
```

transect_9-2013-08-07
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-08-07'].plot.salt() + cat['transect_9-2013-08-07'].plot.temp()
```

transect_9-2013-08-30
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-08-30'].plot.salt() + cat['transect_9-2013-08-30'].plot.temp()
```

transect_9-2013-09-25
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-09-25'].plot.salt() + cat['transect_9-2013-09-25'].plot.temp()
```

transect_9-2013-10-29
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-10-29'].plot.salt() + cat['transect_9-2013-10-29'].plot.temp()
```

transect_9-2013-12-03
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2013-12-03'].plot.salt() + cat['transect_9-2013-12-03'].plot.temp()
```

transect_9-2014-01-09
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-01-09'].plot.salt() + cat['transect_9-2014-01-09'].plot.temp()
```

transect_9-2014-02-15
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-02-15'].plot.salt() + cat['transect_9-2014-02-15'].plot.temp()
```

transect_9-2014-03-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-03-28'].plot.salt() + cat['transect_9-2014-03-28'].plot.temp()
```

transect_9-2014-04-11
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-04-11'].plot.salt() + cat['transect_9-2014-04-11'].plot.temp()
```

transect_9-2014-05-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-05-28'].plot.salt() + cat['transect_9-2014-05-28'].plot.temp()
```

transect_9-2014-06-18
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-06-18'].plot.salt() + cat['transect_9-2014-06-18'].plot.temp()
```

transect_9-2014-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-07-21'].plot.salt() + cat['transect_9-2014-07-21'].plot.temp()
```

transect_9-2014-08-13
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-08-13'].plot.salt() + cat['transect_9-2014-08-13'].plot.temp()
```

transect_9-2014-10-19
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-10-19'].plot.salt() + cat['transect_9-2014-10-19'].plot.temp()
```

transect_9-2014-11-25
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-11-25'].plot.salt() + cat['transect_9-2014-11-25'].plot.temp()
```

transect_9-2014-12-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2014-12-17'].plot.salt() + cat['transect_9-2014-12-17'].plot.temp()
```

transect_9-2015-01-16
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-01-16'].plot.salt() + cat['transect_9-2015-01-16'].plot.temp()
```

transect_9-2015-02-12
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-02-12'].plot.salt() + cat['transect_9-2015-02-12'].plot.temp()
```

transect_9-2015-02-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-02-24'].plot.salt() + cat['transect_9-2015-02-24'].plot.temp()
```

transect_9-2015-03-31
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-03-31'].plot.salt() + cat['transect_9-2015-03-31'].plot.temp()
```

transect_9-2015-04-08
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-04-08'].plot.salt() + cat['transect_9-2015-04-08'].plot.temp()
```

transect_9-2015-05-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-05-28'].plot.salt() + cat['transect_9-2015-05-28'].plot.temp()
```

transect_9-2015-06-26
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-06-26'].plot.salt() + cat['transect_9-2015-06-26'].plot.temp()
```

transect_9-2015-07-10
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-07-10'].plot.salt() + cat['transect_9-2015-07-10'].plot.temp()
```

transect_9-2015-07-29
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-07-29'].plot.salt() + cat['transect_9-2015-07-29'].plot.temp()
```

transect_9-2015-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-08-14'].plot.salt() + cat['transect_9-2015-08-14'].plot.temp()
```

transect_9-2015-09-04
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-09-04'].plot.salt() + cat['transect_9-2015-09-04'].plot.temp()
```

transect_9-2015-09-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-09-24'].plot.salt() + cat['transect_9-2015-09-24'].plot.temp()
```

transect_9-2015-10-19
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-10-19'].plot.salt() + cat['transect_9-2015-10-19'].plot.temp()
```

transect_9-2015-11-04
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-11-04'].plot.salt() + cat['transect_9-2015-11-04'].plot.temp()
```

transect_9-2015-12-10
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2015-12-10'].plot.salt() + cat['transect_9-2015-12-10'].plot.temp()
```

transect_9-2016-01-07
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-01-07'].plot.salt() + cat['transect_9-2016-01-07'].plot.temp()
```

transect_9-2016-02-09
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-02-09'].plot.salt() + cat['transect_9-2016-02-09'].plot.temp()
```

transect_9-2016-04-07
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-04-07'].plot.salt() + cat['transect_9-2016-04-07'].plot.temp()
```

transect_9-2016-05-12
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-05-12'].plot.salt() + cat['transect_9-2016-05-12'].plot.temp()
```

transect_9-2016-06-16
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-06-16'].plot.salt() + cat['transect_9-2016-06-16'].plot.temp()
```

transect_9-2016-07-27
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-07-27'].plot.salt() + cat['transect_9-2016-07-27'].plot.temp()
```

transect_9-2016-09-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-09-23'].plot.salt() + cat['transect_9-2016-09-23'].plot.temp()
```

transect_9-2016-10-13
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-10-13'].plot.salt() + cat['transect_9-2016-10-13'].plot.temp()
```

transect_9-2016-11-10
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-11-10'].plot.salt() + cat['transect_9-2016-11-10'].plot.temp()
```

transect_9-2016-12-13
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2016-12-13'].plot.salt() + cat['transect_9-2016-12-13'].plot.temp()
```

transect_9-2017-01-11
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-01-11'].plot.salt() + cat['transect_9-2017-01-11'].plot.temp()
```

transect_9-2017-02-07
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-02-07'].plot.salt() + cat['transect_9-2017-02-07'].plot.temp()
```

transect_9-2017-03-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-03-28'].plot.salt() + cat['transect_9-2017-03-28'].plot.temp()
```

transect_9-2017-04-20
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-04-20'].plot.salt() + cat['transect_9-2017-04-20'].plot.temp()
```

transect_9-2017-05-30
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-05-30'].plot.salt() + cat['transect_9-2017-05-30'].plot.temp()
```

transect_9-2017-06-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-06-28'].plot.salt() + cat['transect_9-2017-06-28'].plot.temp()
```

transect_9-2017-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-07-24'].plot.salt() + cat['transect_9-2017-07-24'].plot.temp()
```

transect_9-2017-08-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-08-24'].plot.salt() + cat['transect_9-2017-08-24'].plot.temp()
```

transect_9-2017-09-22
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-09-22'].plot.salt() + cat['transect_9-2017-09-22'].plot.temp()
```

transect_9-2017-10-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-10-17'].plot.salt() + cat['transect_9-2017-10-17'].plot.temp()
```

transect_9-2017-11-07
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-11-07'].plot.salt() + cat['transect_9-2017-11-07'].plot.temp()
```

transect_9-2017-12-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2017-12-14'].plot.salt() + cat['transect_9-2017-12-14'].plot.temp()
```

transect_9-2018-01-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-01-17'].plot.salt() + cat['transect_9-2018-01-17'].plot.temp()
```

transect_9-2018-03-02
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-03-02'].plot.salt() + cat['transect_9-2018-03-02'].plot.temp()
```

transect_9-2018-03-27
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-03-27'].plot.salt() + cat['transect_9-2018-03-27'].plot.temp()
```

transect_9-2018-04-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-04-23'].plot.salt() + cat['transect_9-2018-04-23'].plot.temp()
```

transect_9-2018-05-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-05-24'].plot.salt() + cat['transect_9-2018-05-24'].plot.temp()
```

transect_9-2018-06-22
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-06-22'].plot.salt() + cat['transect_9-2018-06-22'].plot.temp()
```

transect_9-2018-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-07-24'].plot.salt() + cat['transect_9-2018-07-24'].plot.temp()
```

transect_9-2018-08-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-08-23'].plot.salt() + cat['transect_9-2018-08-23'].plot.temp()
```

transect_9-2018-09-13
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-09-13'].plot.salt() + cat['transect_9-2018-09-13'].plot.temp()
```

transect_9-2018-10-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-10-17'].plot.salt() + cat['transect_9-2018-10-17'].plot.temp()
```

transect_9-2018-11-08
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-11-08'].plot.salt() + cat['transect_9-2018-11-08'].plot.temp()
```

transect_9-2018-12-06
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2018-12-06'].plot.salt() + cat['transect_9-2018-12-06'].plot.temp()
```

transect_9-2019-02-07
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-02-07'].plot.salt() + cat['transect_9-2019-02-07'].plot.temp()
```

transect_9-2019-03-19
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-03-19'].plot.salt() + cat['transect_9-2019-03-19'].plot.temp()
```

transect_9-2019-04-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-04-24'].plot.salt() + cat['transect_9-2019-04-24'].plot.temp()
```

transect_9-2019-05-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-05-14'].plot.salt() + cat['transect_9-2019-05-14'].plot.temp()
```

transect_9-2019-06-19
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-06-19'].plot.salt() + cat['transect_9-2019-06-19'].plot.temp()
```

transect_9-2019-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-07-23'].plot.salt() + cat['transect_9-2019-07-23'].plot.temp()
```

transect_9-2019-09-16
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-09-16'].plot.salt() + cat['transect_9-2019-09-16'].plot.temp()
```

transect_9-2019-10-30
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-10-30'].plot.salt() + cat['transect_9-2019-10-30'].plot.temp()
```

transect_9-2019-11-15
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-11-15'].plot.salt() + cat['transect_9-2019-11-15'].plot.temp()
```

transect_9-2019-12-12
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2019-12-12'].plot.salt() + cat['transect_9-2019-12-12'].plot.temp()
```

transect_9-2020-02-06
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-02-06'].plot.salt() + cat['transect_9-2020-02-06'].plot.temp()
```

transect_9-2020-03-18
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-03-18'].plot.salt() + cat['transect_9-2020-03-18'].plot.temp()
```

transect_9-2020-06-04
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-06-04'].plot.salt() + cat['transect_9-2020-06-04'].plot.temp()
```

transect_9-2020-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-07-24'].plot.salt() + cat['transect_9-2020-07-24'].plot.temp()
```

transect_9-2020-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-08-14'].plot.salt() + cat['transect_9-2020-08-14'].plot.temp()
```

transect_9-2020-09-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-09-21'].plot.salt() + cat['transect_9-2020-09-21'].plot.temp()
```

transect_9-2020-10-15
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-10-15'].plot.salt() + cat['transect_9-2020-10-15'].plot.temp()
```

transect_9-2020-12-28
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2020-12-28'].plot.salt() + cat['transect_9-2020-12-28'].plot.temp()
```

transect_9-2021-01-13
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-01-13'].plot.salt() + cat['transect_9-2021-01-13'].plot.temp()
```

transect_9-2021-02-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-02-17'].plot.salt() + cat['transect_9-2021-02-17'].plot.temp()
```

transect_9-2021-03-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-03-23'].plot.salt() + cat['transect_9-2021-03-23'].plot.temp()
```

transect_9-2021-04-16
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-04-16'].plot.salt() + cat['transect_9-2021-04-16'].plot.temp()
```

transect_9-2021-05-06
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-05-06'].plot.salt() + cat['transect_9-2021-05-06'].plot.temp()
```

transect_9-2021-06-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-06-21'].plot.salt() + cat['transect_9-2021-06-21'].plot.temp()
```

transect_9-2021-07-16
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-07-16'].plot.salt() + cat['transect_9-2021-07-16'].plot.temp()
```

transect_9-2021-08-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-08-17'].plot.salt() + cat['transect_9-2021-08-17'].plot.temp()
```

transect_9-2021-09-17
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-09-17'].plot.salt() + cat['transect_9-2021-09-17'].plot.temp()
```

transect_9-2021-10-21
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-10-21'].plot.salt() + cat['transect_9-2021-10-21'].plot.temp()
```

transect_9-2021-11-14
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-11-14'].plot.salt() + cat['transect_9-2021-11-14'].plot.temp()
```

transect_9-2021-12-18
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2021-12-18'].plot.salt() + cat['transect_9-2021-12-18'].plot.temp()
```

transect_9-2022-01-31
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-01-31'].plot.salt() + cat['transect_9-2022-01-31'].plot.temp()
```

transect_9-2022-03-01
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-03-01'].plot.salt() + cat['transect_9-2022-03-01'].plot.temp()
```

transect_9-2022-03-22
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-03-22'].plot.salt() + cat['transect_9-2022-03-22'].plot.temp()
```

transect_9-2022-04-13
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-04-13'].plot.salt() + cat['transect_9-2022-04-13'].plot.temp()
```

transect_9-2022-05-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-05-23'].plot.salt() + cat['transect_9-2022-05-23'].plot.temp()
```

transect_9-2022-06-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-06-24'].plot.salt() + cat['transect_9-2022-06-24'].plot.temp()
```

transect_9-2022-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-07-23'].plot.salt() + cat['transect_9-2022-07-23'].plot.temp()
```

transect_9-2022-08-24
        

```{code-cell}
:tags: [full-width]

cat['transect_9-2022-08-24'].plot.salt() + cat['transect_9-2022-08-24'].plot.temp()
```

## transect_AlongBay

+++

transect_AlongBay-2012-08-15
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2012-08-15'].plot.salt() + cat['transect_AlongBay-2012-08-15'].plot.temp()
```

transect_AlongBay-2013-02-12
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2013-02-12'].plot.salt() + cat['transect_AlongBay-2013-02-12'].plot.temp()
```

transect_AlongBay-2013-02-13_A
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2013-02-13_A'].plot.salt() + cat['transect_AlongBay-2013-02-13_A'].plot.temp()
```

transect_AlongBay-2013-02-13_B
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2013-02-13_B'].plot.salt() + cat['transect_AlongBay-2013-02-13_B'].plot.temp()
```

transect_AlongBay-2013-06-06
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2013-06-06'].plot.salt() + cat['transect_AlongBay-2013-06-06'].plot.temp()
```

transect_AlongBay-2014-03-28
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2014-03-28'].plot.salt() + cat['transect_AlongBay-2014-03-28'].plot.temp()
```

transect_AlongBay-2014-05-28
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2014-05-28'].plot.salt() + cat['transect_AlongBay-2014-05-28'].plot.temp()
```

transect_AlongBay-2014-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2014-08-14'].plot.salt() + cat['transect_AlongBay-2014-08-14'].plot.temp()
```

transect_AlongBay-2015-07-10
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2015-07-10'].plot.salt() + cat['transect_AlongBay-2015-07-10'].plot.temp()
```

transect_AlongBay-2015-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2015-08-14'].plot.salt() + cat['transect_AlongBay-2015-08-14'].plot.temp()
```

transect_AlongBay-2016-01-07
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2016-01-07'].plot.salt() + cat['transect_AlongBay-2016-01-07'].plot.temp()
```

transect_AlongBay-2016-05-12
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2016-05-12'].plot.salt() + cat['transect_AlongBay-2016-05-12'].plot.temp()
```

transect_AlongBay-2016-06-16
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2016-06-16'].plot.salt() + cat['transect_AlongBay-2016-06-16'].plot.temp()
```

transect_AlongBay-2016-07-27
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2016-07-27'].plot.salt() + cat['transect_AlongBay-2016-07-27'].plot.temp()
```

transect_AlongBay-2017-01-11
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-01-11'].plot.salt() + cat['transect_AlongBay-2017-01-11'].plot.temp()
```

transect_AlongBay-2017-02-07
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-02-07'].plot.salt() + cat['transect_AlongBay-2017-02-07'].plot.temp()
```

transect_AlongBay-2017-03-28
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-03-28'].plot.salt() + cat['transect_AlongBay-2017-03-28'].plot.temp()
```

transect_AlongBay-2017-04-20
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-04-20'].plot.salt() + cat['transect_AlongBay-2017-04-20'].plot.temp()
```

transect_AlongBay-2017-05-30
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-05-30'].plot.salt() + cat['transect_AlongBay-2017-05-30'].plot.temp()
```

transect_AlongBay-2017-06-28
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-06-28'].plot.salt() + cat['transect_AlongBay-2017-06-28'].plot.temp()
```

transect_AlongBay-2017-07-24
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-07-24'].plot.salt() + cat['transect_AlongBay-2017-07-24'].plot.temp()
```

transect_AlongBay-2017-07-26
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-07-26'].plot.salt() + cat['transect_AlongBay-2017-07-26'].plot.temp()
```

transect_AlongBay-2017-08-24
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-08-24'].plot.salt() + cat['transect_AlongBay-2017-08-24'].plot.temp()
```

transect_AlongBay-2017-09-22
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-09-22'].plot.salt() + cat['transect_AlongBay-2017-09-22'].plot.temp()
```

transect_AlongBay-2017-10-20
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-10-20'].plot.salt() + cat['transect_AlongBay-2017-10-20'].plot.temp()
```

transect_AlongBay-2017-11-02
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-11-02'].plot.salt() + cat['transect_AlongBay-2017-11-02'].plot.temp()
```

transect_AlongBay-2017-11-07
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-11-07'].plot.salt() + cat['transect_AlongBay-2017-11-07'].plot.temp()
```

transect_AlongBay-2017-12-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2017-12-14'].plot.salt() + cat['transect_AlongBay-2017-12-14'].plot.temp()
```

transect_AlongBay-2018-01-17
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-01-17'].plot.salt() + cat['transect_AlongBay-2018-01-17'].plot.temp()
```

transect_AlongBay-2018-03-02
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-03-02'].plot.salt() + cat['transect_AlongBay-2018-03-02'].plot.temp()
```

transect_AlongBay-2018-03-27
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-03-27'].plot.salt() + cat['transect_AlongBay-2018-03-27'].plot.temp()
```

transect_AlongBay-2018-04-23
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-04-23'].plot.salt() + cat['transect_AlongBay-2018-04-23'].plot.temp()
```

transect_AlongBay-2018-05-24
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-05-24'].plot.salt() + cat['transect_AlongBay-2018-05-24'].plot.temp()
```

transect_AlongBay-2018-06-22
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-06-22'].plot.salt() + cat['transect_AlongBay-2018-06-22'].plot.temp()
```

transect_AlongBay-2018-07-18
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-07-18'].plot.salt() + cat['transect_AlongBay-2018-07-18'].plot.temp()
```

transect_AlongBay-2018-08-23
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-08-23'].plot.salt() + cat['transect_AlongBay-2018-08-23'].plot.temp()
```

transect_AlongBay-2018-09-17
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-09-17'].plot.salt() + cat['transect_AlongBay-2018-09-17'].plot.temp()
```

transect_AlongBay-2018-10-17
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-10-17'].plot.salt() + cat['transect_AlongBay-2018-10-17'].plot.temp()
```

transect_AlongBay-2018-11-08
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-11-08'].plot.salt() + cat['transect_AlongBay-2018-11-08'].plot.temp()
```

transect_AlongBay-2018-12-06
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2018-12-06'].plot.salt() + cat['transect_AlongBay-2018-12-06'].plot.temp()
```

transect_AlongBay-2019-02-07
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-02-07'].plot.salt() + cat['transect_AlongBay-2019-02-07'].plot.temp()
```

transect_AlongBay-2019-03-19
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-03-19'].plot.salt() + cat['transect_AlongBay-2019-03-19'].plot.temp()
```

transect_AlongBay-2019-04-24
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-04-24'].plot.salt() + cat['transect_AlongBay-2019-04-24'].plot.temp()
```

transect_AlongBay-2019-05-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-05-14'].plot.salt() + cat['transect_AlongBay-2019-05-14'].plot.temp()
```

transect_AlongBay-2019-06-19
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-06-19'].plot.salt() + cat['transect_AlongBay-2019-06-19'].plot.temp()
```

transect_AlongBay-2019-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-07-23'].plot.salt() + cat['transect_AlongBay-2019-07-23'].plot.temp()
```

transect_AlongBay-2019-10-30
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-10-30'].plot.salt() + cat['transect_AlongBay-2019-10-30'].plot.temp()
```

transect_AlongBay-2019-11-15
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-11-15'].plot.salt() + cat['transect_AlongBay-2019-11-15'].plot.temp()
```

transect_AlongBay-2019-12-12
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2019-12-12'].plot.salt() + cat['transect_AlongBay-2019-12-12'].plot.temp()
```

transect_AlongBay-2020-02-06
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-02-06'].plot.salt() + cat['transect_AlongBay-2020-02-06'].plot.temp()
```

transect_AlongBay-2020-03-18
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-03-18'].plot.salt() + cat['transect_AlongBay-2020-03-18'].plot.temp()
```

transect_AlongBay-2020-06-04
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-06-04'].plot.salt() + cat['transect_AlongBay-2020-06-04'].plot.temp()
```

transect_AlongBay-2020-07-08
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-07-08'].plot.salt() + cat['transect_AlongBay-2020-07-08'].plot.temp()
```

transect_AlongBay-2020-07-23
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-07-23'].plot.salt() + cat['transect_AlongBay-2020-07-23'].plot.temp()
```

transect_AlongBay-2020-08-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-08-14'].plot.salt() + cat['transect_AlongBay-2020-08-14'].plot.temp()
```

transect_AlongBay-2020-09-20
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-09-20'].plot.salt() + cat['transect_AlongBay-2020-09-20'].plot.temp()
```

transect_AlongBay-2020-10-15
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-10-15'].plot.salt() + cat['transect_AlongBay-2020-10-15'].plot.temp()
```

transect_AlongBay-2020-12-28
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2020-12-28'].plot.salt() + cat['transect_AlongBay-2020-12-28'].plot.temp()
```

transect_AlongBay-2021-01-13
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-01-13'].plot.salt() + cat['transect_AlongBay-2021-01-13'].plot.temp()
```

transect_AlongBay-2021-02-16
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-02-16'].plot.salt() + cat['transect_AlongBay-2021-02-16'].plot.temp()
```

transect_AlongBay-2021-03-23
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-03-23'].plot.salt() + cat['transect_AlongBay-2021-03-23'].plot.temp()
```

transect_AlongBay-2021-04-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-04-14'].plot.salt() + cat['transect_AlongBay-2021-04-14'].plot.temp()
```

transect_AlongBay-2021-04-16
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-04-16'].plot.salt() + cat['transect_AlongBay-2021-04-16'].plot.temp()
```

transect_AlongBay-2021-05-06
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-05-06'].plot.salt() + cat['transect_AlongBay-2021-05-06'].plot.temp()
```

transect_AlongBay-2021-06-21
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-06-21'].plot.salt() + cat['transect_AlongBay-2021-06-21'].plot.temp()
```

transect_AlongBay-2021-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-07-21'].plot.salt() + cat['transect_AlongBay-2021-07-21'].plot.temp()
```

transect_AlongBay-2021-08-17
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-08-17'].plot.salt() + cat['transect_AlongBay-2021-08-17'].plot.temp()
```

transect_AlongBay-2021-10-04
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-10-04'].plot.salt() + cat['transect_AlongBay-2021-10-04'].plot.temp()
```

transect_AlongBay-2021-10-05
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-10-05'].plot.salt() + cat['transect_AlongBay-2021-10-05'].plot.temp()
```

transect_AlongBay-2021-10-21
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-10-21'].plot.salt() + cat['transect_AlongBay-2021-10-21'].plot.temp()
```

transect_AlongBay-2021-11-14
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-11-14'].plot.salt() + cat['transect_AlongBay-2021-11-14'].plot.temp()
```

transect_AlongBay-2021-12-18
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2021-12-18'].plot.salt() + cat['transect_AlongBay-2021-12-18'].plot.temp()
```

transect_AlongBay-2022-01-31
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-01-31'].plot.salt() + cat['transect_AlongBay-2022-01-31'].plot.temp()
```

transect_AlongBay-2022-02-28
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-02-28'].plot.salt() + cat['transect_AlongBay-2022-02-28'].plot.temp()
```

transect_AlongBay-2022-03-21
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-03-21'].plot.salt() + cat['transect_AlongBay-2022-03-21'].plot.temp()
```

transect_AlongBay-2022-04-12
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-04-12'].plot.salt() + cat['transect_AlongBay-2022-04-12'].plot.temp()
```

transect_AlongBay-2022-05-23
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-05-23'].plot.salt() + cat['transect_AlongBay-2022-05-23'].plot.temp()
```

transect_AlongBay-2022-06-24
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-06-24'].plot.salt() + cat['transect_AlongBay-2022-06-24'].plot.temp()
```

transect_AlongBay-2022-07-21
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-07-21'].plot.salt() + cat['transect_AlongBay-2022-07-21'].plot.temp()
```

transect_AlongBay-2022-08-24
        

```{code-cell}
:tags: [full-width]

cat['transect_AlongBay-2022-08-24'].plot.salt() + cat['transect_AlongBay-2022-08-24'].plot.temp()
```
