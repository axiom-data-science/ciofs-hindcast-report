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

(page:adcp_moored_noaa_coi_2005)=
# Moored ADCP (NOAA): ADCP survey Cook Inlet 2005

* Cook Inlet 2005 Current Survey
* adcp_moored_noaa_coi_2005
* 2005, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.




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



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_coi_2005"))
```

## Map of Moored ADCPs
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_coi_2005")("adcp_moored_noaa_coi_2005")
```

## COI0501
        

```{code-cell}
:tags: [remove-input]

cat['COI0501'].plot.ualong() + cat['COI0501'].plot.vacross()
```

## COI0502
        

```{code-cell}
:tags: [remove-input]

cat['COI0502'].plot.ualong() + cat['COI0502'].plot.vacross()
```

## COI0503
        

```{code-cell}
:tags: [remove-input]

cat['COI0503'].plot.ualong() + cat['COI0503'].plot.vacross()
```

## COI0504
        

```{code-cell}
:tags: [remove-input]

cat['COI0504'].plot.ualong() + cat['COI0504'].plot.vacross()
```

## COI0505
        

```{code-cell}
:tags: [remove-input]

cat['COI0505'].plot.ualong() + cat['COI0505'].plot.vacross()
```

## COI0506
        

```{code-cell}
:tags: [remove-input]

cat['COI0506'].plot.ualong() + cat['COI0506'].plot.vacross()
```

## COI0507
        

```{code-cell}
:tags: [remove-input]

cat['COI0507'].plot.ualong() + cat['COI0507'].plot.vacross()
```

## COI0508
        

```{code-cell}
:tags: [remove-input]

cat['COI0508'].plot.ualong() + cat['COI0508'].plot.vacross()
```

## COI0509
        

```{code-cell}
:tags: [remove-input]

cat['COI0509'].plot.ualong() + cat['COI0509'].plot.vacross()
```

## COI0510
        

```{code-cell}
:tags: [remove-input]

cat['COI0510'].plot.ualong() + cat['COI0510'].plot.vacross()
```

## COI0511
        

```{code-cell}
:tags: [remove-input]

cat['COI0511'].plot.ualong() + cat['COI0511'].plot.vacross()
```

## COI0512
        

```{code-cell}
:tags: [remove-input]

cat['COI0512'].plot.ualong() + cat['COI0512'].plot.vacross()
```

## COI0513
        

```{code-cell}
:tags: [remove-input]

cat['COI0513'].plot.ualong() + cat['COI0513'].plot.vacross()
```

## COI0514
        

```{code-cell}
:tags: [remove-input]

cat['COI0514'].plot.ualong() + cat['COI0514'].plot.vacross()
```

## COI0515
        

```{code-cell}
:tags: [remove-input]

cat['COI0515'].plot.ualong() + cat['COI0515'].plot.vacross()
```

## COI0516
        

```{code-cell}
:tags: [remove-input]

cat['COI0516'].plot.ualong() + cat['COI0516'].plot.vacross()
```

## COI0517
        

```{code-cell}
:tags: [remove-input]

cat['COI0517'].plot.ualong() + cat['COI0517'].plot.vacross()
```

## COI0518
        

```{code-cell}
:tags: [remove-input]

cat['COI0518'].plot.ualong() + cat['COI0518'].plot.vacross()
```

## COI0519
        

```{code-cell}
:tags: [remove-input]

cat['COI0519'].plot.ualong() + cat['COI0519'].plot.vacross()
```

## COI0520
        

```{code-cell}
:tags: [remove-input]

cat['COI0520'].plot.ualong() + cat['COI0520'].plot.vacross()
```

## COI0521
        

```{code-cell}
:tags: [remove-input]

cat['COI0521'].plot.ualong() + cat['COI0521'].plot.vacross()
```

## COI0522
        

```{code-cell}
:tags: [remove-input]

cat['COI0522'].plot.ualong() + cat['COI0522'].plot.vacross()
```

## COI0523
        

```{code-cell}
:tags: [remove-input]

cat['COI0523'].plot.ualong() + cat['COI0523'].plot.vacross()
```

## COI0524
        

```{code-cell}
:tags: [remove-input]

cat['COI0524'].plot.ualong() + cat['COI0524'].plot.vacross()
```
