---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
---

```{code-cell}
import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
```

# NOAA ADCP survey Cook Inlet: 2005

* Cook Inlet 2005 Current Survey
* adcp_moored_noaa_coi_2005
* 2005, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet




Dataset metadata:
|    | Dataset   |   depth | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude |   measured_depth |   minLatitude |   minLongitude | name                       | observe_dst   | orientation   | ping_int   | project                        | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   |
|---:|:----------|--------:|:------------------|:--------------------|--------------------------:|---------------------:|:--------------------|--------:|---------:|--------------:|---------------:|-----------------:|--------------:|---------------:|:---------------------------|:--------------|:--------------|:-----------|:-------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|
|  0 | COI0501   |    33.5 | timeSeriesProfile | 2005-05-19 00:24:00 |                       349 |                  6.1 | 2005-06-28 20:06:00 | 60.722  | -151.647 |       60.722  |       -151.647 |            29.53 |       60.722  |       -151.647 | West Foreland              | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0501/deployments.json |                |                -9 | metric  |
|  1 | COI0502   |    33.8 | timeSeriesProfile | 2005-05-18 23:23:00 |                         3 |                  6.1 | 2005-07-18 16:11:00 | 60.7207 | -151.557 |       60.7207 |       -151.557 |            31.27 |       60.7207 |       -151.557 | The Forelands              | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0502/deployments.json |                |                -9 | metric  |
|  2 | COI0503   |    44.2 | timeSeriesProfile | 2005-05-18 22:36:00 |                         6 |                  7.4 | 2005-06-29 22:54:00 | 60.7173 | -151.433 |       60.7173 |       -151.433 |            48.61 |       60.7173 |       -151.433 | East Foreland              | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0503/deployments.json |                |                -9 | metric  |
|  3 | COI0504   |    33.5 | timeSeriesProfile | 2005-05-18 21:24:00 |                       345 |                  7.4 | 2005-06-29 23:30:00 | 60.6834 | -151.418 |       60.6834 |       -151.418 |            39.42 |       60.6834 |       -151.418 | Nikiski, .8 nm west of     | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0504/deployments.json |                |                -9 | metric  |
|  4 | COI0505   |    22.6 | timeSeriesProfile | 2005-05-19 01:23:00 |                        58 |                  6.1 | 2005-07-22 18:41:00 | 60.5967 | -151.74  |       60.5967 |       -151.74  |            21.61 |       60.5967 |       -151.74  | West Foreland, south of    | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0505/deployments.json |                |                -9 | metric  |
|  5 | COI0506   |    27.1 | timeSeriesProfile | 2005-05-18 20:06:00 |                        21 |                  6.1 | 2005-06-30 01:54:00 | 60.5808 | -151.445 |       60.5808 |       -151.445 |            23.88 |       60.5808 |       -151.445 | Kenai River, north of      | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0506/deployments.json |                |                -9 | metric  |
|  6 | COI0507   |    27.4 | timeSeriesProfile | 2005-05-19 03:00:00 |                        51 |                  6.1 | 2005-06-30 20:36:00 | 60.5517 | -152.128 |       60.5517 |       -152.128 |            26.78 |       60.5517 |       -152.128 | Drift River Terminal       | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0507/deployments.json |                |                -9 | metric  |
|  7 | COI0508   |    51.5 | timeSeriesProfile | 2005-05-18 18:54:00 |                        33 |                  7.4 | 2005-06-30 14:24:00 | 60.483  | -151.673 |       60.483  |       -151.673 |            48    |       60.483  |       -151.673 | Kalgin Island, east of     | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0508/deployments.json |                |                -9 | metric  |
|  8 | COI0509   |    96.3 | timeSeriesProfile | 2005-05-19 04:53:00 |                        15 |                 10.7 | 2005-06-29 14:35:00 | 60.3792 | -152.182 |       60.3792 |       -152.182 |            94.67 |       60.3792 |       -152.182 | Harriot Pt., west of       | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0509/deployments.json |                |                -9 | metric  |
|  9 | COI0510   |    34.5 | timeSeriesProfile | 2005-05-18 16:42:00 |                        33 |                  7.4 | 2005-06-29 04:48:00 | 60.248  | -151.755 |       60.248  |       -151.755 |            29.04 |       60.248  |       -151.755 | Kalgin Island, SE of       | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0510/deployments.json |                |                -9 | metric  |
| 10 | COI0511   |    68.6 | timeSeriesProfile | 2005-06-29 02:54:00 |                        31 |                  6.1 | 2005-08-15 15:42:00 | 60.0233 | -152.12  |       60.0233 |       -152.12  |            67.08 |       60.0233 |       -152.12  | Cape Ninilchik, west of    | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0511/deployments.json |                |                -9 | metric  |
| 11 | COI0512   |    17.4 | timeSeriesProfile | 2005-07-05 07:06:00 |                       320 |                  6.1 | 2005-08-15 05:48:00 | 59.5666 | -153.422 |       59.5666 |       -153.422 |            17.19 |       59.5666 |       -153.422 | Iliamna Bay                | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0512/deployments.json |                |                -9 | metric  |
| 12 | COI0513   |    31.2 | timeSeriesProfile | 2005-07-04 01:30:00 |                        40 |                  6.1 | 2005-08-13 19:18:00 | 59.4828 | -151.755 |       59.4828 |       -151.755 |            28.06 |       59.4828 |       -151.755 | Seldovia                   | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0513/deployments.json |                |                -9 | metric  |
| 13 | COI0514   |    80.2 | timeSeriesProfile | 2005-07-05 11:12:00 |                         5 |                  6.1 | 2005-08-15 02:12:00 | 59.3018 | -152.93  |       59.3018 |       -152.93  |            74.3  |       59.3018 |       -152.93  | Augustine Island           | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0514/deployments.json |                |                -9 | metric  |
| 14 | COI0515   |    87.7 | timeSeriesProfile | 2005-07-05 14:06:00 |                        10 |                  6.1 | 2005-08-13 23:24:00 | 59.3149 | -152.365 |       59.3149 |       -152.365 |            85.36 |       59.3149 |       -152.365 | Kachemak Bay, southwest of | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0515/deployments.json |                |                -9 | metric  |
| 15 | COI0516   |    47.1 | timeSeriesProfile | 2005-07-04 03:00:00 |                        30 |                  6.1 | 2005-08-13 21:00:00 | 59.4    | -151.966 |       59.4    |       -151.966 |            45.79 |       59.4    |       -151.966 | Port Graham                | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0516/deployments.json |                |                -9 | metric  |
| 16 | COI0517   |   177.9 | timeSeriesProfile | 2005-07-05 00:36:00 |                       340 |                 20   | 2005-08-14 22:00:00 | 58.8901 | -153.184 |       58.8901 |       -153.184 |           166.82 |       58.8901 |       -153.184 | Cape Douglas               | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0517/deployments.json |                |                -9 | metric  |
| 17 | COI0518   |   170.8 | timeSeriesProfile | 2005-07-04 22:18:00 |                       312 |                 20   | 2005-08-14 19:30:00 | 58.9805 | -152.728 |       58.9805 |       -152.728 |           165.68 |       58.9805 |       -152.728 | Cape Douglas, NE           | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0518/deployments.json |                |                -9 | metric  |
| 18 | COI0519   |   146.6 | timeSeriesProfile | 2005-07-04 20:24:00 |                       300 |                  8   | 2005-08-14 17:36:00 | 58.808  | -152.408 |       58.808  |       -152.408 |           143.26 |       58.808  |       -152.408 | Stevenson Passage          | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0519/deployments.json |                |                -9 | metric  |
| 19 | COI0520   |   162.4 | timeSeriesProfile | 2005-07-04 17:18:00 |                       300 |                  6.1 | 2005-08-14 13:54:00 | 59.0492 | -152.152 |       59.0492 |       -152.152 |           160.72 |       59.0492 |       -152.152 | West Amatuli Island, North | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0520/deployments.json |                |                -9 | metric  |
| 20 | COI0521   |    87   | timeSeriesProfile | 2005-07-04 06:12:00 |                       306 |                  6.1 | 2005-08-14 02:54:00 | 59.1207 | -151.895 |       59.1207 |       -151.895 |            81.83 |       59.1207 |       -151.895 | Cape Elizabeth             | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0521/deployments.json |                |                -9 | metric  |
| 21 | COI0522   |    37.8 | timeSeriesProfile | 2005-07-04 08:54:00 |                        45 |                  6.1 | 2005-08-14 04:36:00 | 59.2112 | -151.787 |       59.2112 |       -151.787 |            32.37 |       59.2112 |       -151.787 | Port Chatham               | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0522/deployments.json |                |                -9 | metric  |
| 22 | COI0523   |    82.1 | timeSeriesProfile | 2005-07-04 08:12:00 |                       350 |                  6.1 | 2005-08-14 05:17:00 | 59.1666 | -151.775 |       59.1666 |       -151.775 |            79.44 |       59.1666 |       -151.775 | Chugach Passage            | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0523/deployments.json |                |                -9 | metric  |
| 23 | COI0524   |    30.9 | timeSeriesProfile | 2005-07-04 07:42:00 |                       270 |                  6.1 | 2005-08-14 06:06:00 | 59.1339 | -151.706 |       59.1339 |       -151.706 |            26.83 |       59.1339 |       -151.706 | Chugach Passage, east of   | True          | up            |            | Cook Inlet 2005 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0524/deployments.json |                |                -9 | metric  |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_coi_2005"))
```

## Map of Moored ADCPs
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_coi_2005")("adcp_moored_noaa_coi_2005")
    
```

## COI0501
        

```{code-cell}
cat['COI0501'].plot.ualong() + cat['COI0501'].plot.vacross()
```

## COI0502
        

```{code-cell}
cat['COI0502'].plot.ualong() + cat['COI0502'].plot.vacross()
```

## COI0503
        

```{code-cell}
cat['COI0503'].plot.ualong() + cat['COI0503'].plot.vacross()
```

## COI0504
        

```{code-cell}
cat['COI0504'].plot.ualong() + cat['COI0504'].plot.vacross()
```

## COI0505
        

```{code-cell}
cat['COI0505'].plot.ualong() + cat['COI0505'].plot.vacross()
```

## COI0506
        

```{code-cell}
cat['COI0506'].plot.ualong() + cat['COI0506'].plot.vacross()
```

## COI0507
        

```{code-cell}
cat['COI0507'].plot.ualong() + cat['COI0507'].plot.vacross()
```

## COI0508
        

```{code-cell}
cat['COI0508'].plot.ualong() + cat['COI0508'].plot.vacross()
```

## COI0509
        

```{code-cell}
cat['COI0509'].plot.ualong() + cat['COI0509'].plot.vacross()
```

## COI0510
        

```{code-cell}
cat['COI0510'].plot.ualong() + cat['COI0510'].plot.vacross()
```

## COI0511
        

```{code-cell}
cat['COI0511'].plot.ualong() + cat['COI0511'].plot.vacross()
```

## COI0512
        

```{code-cell}
cat['COI0512'].plot.ualong() + cat['COI0512'].plot.vacross()
```

## COI0513
        

```{code-cell}
cat['COI0513'].plot.ualong() + cat['COI0513'].plot.vacross()
```

## COI0514
        

```{code-cell}
cat['COI0514'].plot.ualong() + cat['COI0514'].plot.vacross()
```

## COI0515
        

```{code-cell}
cat['COI0515'].plot.ualong() + cat['COI0515'].plot.vacross()
```

## COI0516
        

```{code-cell}
cat['COI0516'].plot.ualong() + cat['COI0516'].plot.vacross()
```

## COI0517
        

```{code-cell}
cat['COI0517'].plot.ualong() + cat['COI0517'].plot.vacross()
```

## COI0518
        

```{code-cell}
cat['COI0518'].plot.ualong() + cat['COI0518'].plot.vacross()
```

## COI0519
        

```{code-cell}
cat['COI0519'].plot.ualong() + cat['COI0519'].plot.vacross()
```

## COI0520
        

```{code-cell}
cat['COI0520'].plot.ualong() + cat['COI0520'].plot.vacross()
```

## COI0521
        

```{code-cell}
cat['COI0521'].plot.ualong() + cat['COI0521'].plot.vacross()
```

## COI0522
        

```{code-cell}
cat['COI0522'].plot.ualong() + cat['COI0522'].plot.vacross()
```

## COI0523
        

```{code-cell}
cat['COI0523'].plot.ualong() + cat['COI0523'].plot.vacross()
```

## COI0524
        

```{code-cell}
cat['COI0524'].plot.ualong() + cat['COI0524'].plot.vacross()
```
