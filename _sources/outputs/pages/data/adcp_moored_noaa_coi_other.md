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

(page:adcp_moored_noaa_coi_other)=
# Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years

* Cook Inlet 2002/2003/2004/2008/2012 Current Survey
* adcp_moored_noaa_coi_other
* From 2002 to 2012, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.




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



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_coi_other"))
```

## Map of Moored ADCPs
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_coi_other")("adcp_moored_noaa_coi_other")
```

## COI0206
        

```{code-cell}
:tags: [remove-input]

cat['COI0206'].plot.ualong() + cat['COI0206'].plot.vacross()
```

## COI0207
        

```{code-cell}
:tags: [remove-input]

cat['COI0207'].plot.ualong() + cat['COI0207'].plot.vacross()
```

## COI0213
        

```{code-cell}
:tags: [remove-input]

cat['COI0213'].plot.ualong() + cat['COI0213'].plot.vacross()
```

## COI0301
        

```{code-cell}
:tags: [remove-input]

cat['COI0301'].plot.ualong() + cat['COI0301'].plot.vacross()
```

## COI0302
        

```{code-cell}
:tags: [remove-input]

cat['COI0302'].plot.ualong() + cat['COI0302'].plot.vacross()
```

## COI0303
        

```{code-cell}
:tags: [remove-input]

cat['COI0303'].plot.ualong() + cat['COI0303'].plot.vacross()
```

## COI0306
        

```{code-cell}
:tags: [remove-input]

cat['COI0306'].plot.ualong() + cat['COI0306'].plot.vacross()
```

## COI0307
        

```{code-cell}
:tags: [remove-input]

cat['COI0307'].plot.ualong() + cat['COI0307'].plot.vacross()
```

## COI0418
        

```{code-cell}
:tags: [remove-input]

cat['COI0418'].plot.ualong() + cat['COI0418'].plot.vacross()
```

## COI0419
        

```{code-cell}
:tags: [remove-input]

cat['COI0419'].plot.ualong() + cat['COI0419'].plot.vacross()
```

## COI0420
        

```{code-cell}
:tags: [remove-input]

cat['COI0420'].plot.ualong() + cat['COI0420'].plot.vacross()
```

## COI0421
        

```{code-cell}
:tags: [remove-input]

cat['COI0421'].plot.ualong() + cat['COI0421'].plot.vacross()
```

## COI0422
        

```{code-cell}
:tags: [remove-input]

cat['COI0422'].plot.ualong() + cat['COI0422'].plot.vacross()
```

## COI0801
        

```{code-cell}
:tags: [remove-input]

cat['COI0801'].plot.ualong() + cat['COI0801'].plot.vacross()
```

## COI0802
        

```{code-cell}
:tags: [remove-input]

cat['COI0802'].plot.ualong() + cat['COI0802'].plot.vacross()
```

## COI1201
        

```{code-cell}
:tags: [remove-input]

cat['COI1201'].plot.ualong() + cat['COI1201'].plot.vacross()
```

## COI1202
        

```{code-cell}
:tags: [remove-input]

cat['COI1202'].plot.ualong() + cat['COI1202'].plot.vacross()
```

## COI1203
        

```{code-cell}
:tags: [remove-input]

cat['COI1203'].plot.ualong() + cat['COI1203'].plot.vacross()
```

## COI1204
        

```{code-cell}
:tags: [remove-input]

cat['COI1204'].plot.ualong() + cat['COI1204'].plot.vacross()
```

## COI1205
        

```{code-cell}
:tags: [remove-input]

cat['COI1205'].plot.ualong() + cat['COI1205'].plot.vacross()
```

## COI1207
        

```{code-cell}
:tags: [remove-input]

cat['COI1207'].plot.ualong() + cat['COI1207'].plot.vacross()
```

## COI1208
        

```{code-cell}
:tags: [remove-input]

cat['COI1208'].plot.ualong() + cat['COI1208'].plot.vacross()
```

## COI1209
        

```{code-cell}
:tags: [remove-input]

cat['COI1209'].plot.ualong() + cat['COI1209'].plot.vacross()
```

## COI1210
        

```{code-cell}
:tags: [remove-input]

cat['COI1210'].plot.ualong() + cat['COI1210'].plot.vacross()
```
