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

# Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years

* Cook Inlet 2002/2003/2004/2008/2012 Current Survey
* adcp_moored_noaa_coi_other
* From 2002 to 2012, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.




<details><summary>Dataset metadata:</summary>

|    | Dataset   |   depth | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude |   measured_depth |   minLatitude |   minLongitude | name                       | observe_dst   | orientation   | ping_int   | project                        | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   | urlpath                                                       |
|---:|:----------|--------:|:------------------|:--------------------|--------------------------:|---------------------:|:--------------------|--------:|---------:|--------------:|---------------:|-----------------:|--------------:|---------------:|:---------------------------|:--------------|:--------------|:-----------|:-------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|:--------------------------------------------------------------|
|  0 | COI0206   |   35.05 | timeSeriesProfile | 2002-07-13 01:18:00 |                        90 |                 0.5  | 2002-08-13 17:48:00 | 61.2169 | -149.984 |       61.2169 |       -149.984 |            35.14 |       61.2169 |       -149.984 | Point Woronzof             | True          | up            |            | Cook Inlet 2002 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0206/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0206 |
|  1 | COI0207   |   11.4  | timeSeriesProfile | 2002-07-13 00:32:00 |                        90 |                 0.5  | 2002-10-05 22:08:00 | 61.1792 | -150.126 |       61.1792 |       -150.126 |            11.4  |       61.1792 |       -150.126 | Fire Island, 1 nm E        | True          | up            |            | Cook Inlet 2002 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0207/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0207 |
|  2 | COI0213   |   23.8  | timeSeriesProfile | 2002-07-13 00:00:00 |                        90 |                 9.4  | 2002-08-14 15:12:00 | 61.1922 | -150.176 |       61.1922 |       -150.176 |            26.02 |       61.1922 |       -150.176 | Fire Island                | True          | up            |            | Cook Inlet 2002 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0213/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0213 |
|  3 | COI0301   |   18.9  | timeSeriesProfile | 2003-07-16 00:22:00 |                        17 |                 7.5  | 2003-08-20 16:16:00 | 61.2782 | -149.895 |       61.2782 |       -149.895 |            21.42 |       61.2782 |       -149.895 | Knik Arm, NW of POA        | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0301/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0301 |
|  4 | COI0302   |   21.1  | timeSeriesProfile | 2003-07-16 00:14:00 |                        20 |                 7.5  | 2003-08-20 04:26:00 | 61.2746 | -149.882 |       61.2746 |       -149.882 |            22.49 |       61.2746 |       -149.882 | Knik Arm, East Side        | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0302/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0302 |
|  5 | COI0303   |   31.1  | timeSeriesProfile | 2003-07-16 00:52:00 |                        30 |                 7.5  | 2003-08-21 05:52:00 | 61.2522 | -149.921 |       61.2522 |       -149.921 |            32.04 |       61.2522 |       -149.921 | Port Mackenzie, South of   | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0303/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0303 |
|  6 | COI0306   |   23.8  | timeSeriesProfile | 2003-07-14 20:18:00 |                        80 |                 7.2  | 2003-08-23 02:24:00 | 61.1609 | -150.565 |       61.1609 |       -150.565 |            22.01 |       61.1609 |       -150.565 | Fire Island Shoal, NW of   | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0306/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0306 |
|  7 | COI0307   |   22.3  | timeSeriesProfile | 2003-07-14 21:54:00 |                        45 |                 7.2  | 2003-08-23 01:06:00 | 61.1014 | -150.562 |       61.1014 |       -150.562 |            23.57 |       61.1014 |       -150.562 | Beluga Shoal, S. of        | True          | up            |            | Cook Inlet 2003 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0307/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0307 |
|  8 | COI0418   |  203    | timeSeriesProfile | 2004-06-22 01:31:00 |                       295 |               100    | 2004-08-03 17:25:00 | 59.0658 | -151.982 |       59.0658 |       -151.982 |           192.5  |       59.0658 |       -151.982 | Kennedy Entrance           | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0418/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0418 |
|  9 | COI0419   |   51.5  | timeSeriesProfile | 2004-08-05 21:36:00 |                         0 |                 8.53 | 2004-09-15 14:54:00 | 59.8393 | -152.368 |       59.8393 |       -152.368 |            51.77 |       59.8393 |       -152.368 | Anchor Point West          | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0419/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0419 |
| 10 | COI0420   |   41.4  | timeSeriesProfile | 2004-08-05 20:06:00 |                         0 |                 8.54 | 2004-09-15 14:42:00 | 59.8187 | -152.156 |       59.8187 |       -152.156 |            42.62 |       59.8187 |       -152.156 | Anchor Point East          | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0420/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0420 |
| 11 | COI0421   |   61.6  | timeSeriesProfile | 2004-08-05 16:59:00 |                        80 |                 8.5  | 2004-09-15 19:23:00 | 59.5754 | -151.652 |       59.5754 |       -151.652 |            57.63 |       59.5754 |       -151.652 | Barabara Point             | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0421/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0421 |
| 12 | COI0422   |   56.7  | timeSeriesProfile | 2004-08-06 21:05:00 |                        50 |                 8.5  | 2004-09-15 21:29:00 | 59.6667 | -151.192 |       59.6667 |       -151.192 |            57.13 |       59.6667 |       -151.192 | Glacier Split              | True          | up            |            | Cook Inlet 2004 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0422/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0422 |
| 13 | COI0801   |   22    | timeSeriesProfile | 2008-07-15 22:36:00 |                       345 |                 3.9  | 2008-09-17 22:30:00 | 60.6869 | -151.404 |       60.6869 |       -151.404 |            23.64 |       60.6869 |       -151.404 | Tesoro Pier, N of          | True          | up            |            | Cook Inlet 2008 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0801/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0801 |
| 14 | COI0802   |   22    | timeSeriesProfile | 2008-07-15 23:24:00 |                       345 |                 3.9  | 2008-09-17 22:30:00 | 60.6678 | -151.392 |       60.6678 |       -151.392 |            22.62 |       60.6678 |       -151.392 | Unocal Pier, S of          | True          | up            |            | Cook Inlet 2008 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI0802/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI0802 |
| 15 | COI1201   |   77.3  | timeSeriesProfile | 2012-06-14 00:54:00 |                        35 |                10.35 | 2012-08-14 18:29:00 | 59.5925 | -151.4   |       59.5925 |       -151.4   |            74.93 |       59.5925 |       -151.4   | Homer Spit                 | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1201/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1201 |
| 16 | COI1202   |   43.3  | timeSeriesProfile | 2012-06-13 20:12:00 |                        45 |                 6    | 2012-08-14 20:30:00 | 59.4225 | -151.917 |       59.4225 |       -151.917 |            40.82 |       59.4225 |       -151.917 | Pt. Pogishi, SW of         | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1202/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1202 |
| 17 | COI1203   |   44.7  | timeSeriesProfile | 2012-06-14 18:42:00 |                        10 |                 6    | 2012-08-14 22:06:00 | 59.7438 | -152.034 |       59.7438 |       -152.034 |            40.87 |       59.7438 |       -152.034 | Anchor Point, W of         | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1203/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1203 |
| 18 | COI1204   |   31.7  | timeSeriesProfile | 2012-06-16 01:06:00 |                        55 |                 6    | 2012-08-17 01:06:00 | 61.0598 | -151.081 |       61.0598 |       -151.081 |            28.13 |       61.0598 |       -151.081 | North Forelands            | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1204/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1204 |
| 19 | COI1205   |   69.5  | timeSeriesProfile | 2012-06-15 01:48:00 |                        10 |                 6    | 2012-08-15 23:00:00 | 60.4718 | -151.706 |       60.4718 |       -151.706 |            61.74 |       60.4718 |       -151.706 | Kalgin Island, 4nm E of    | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1205/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1205 |
| 20 | COI1207   |   53.3  | timeSeriesProfile | 2012-06-16 20:12:00 |                        50 |                 6    | 2012-08-17 17:24:00 | 61.0566 | -150.36  |       61.0566 |       -150.36  |            51.95 |       61.0566 |       -150.36  | Point Possession           | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1207/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1207 |
| 21 | COI1208   |   31.6  | timeSeriesProfile | 2012-06-16 21:18:00 |                        90 |                 6    | 2012-08-17 18:30:00 | 61.1036 | -150.265 |       61.1036 |       -150.265 |            32.37 |       61.1036 |       -150.265 | Fire Island, South of      | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1208/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1208 |
| 22 | COI1209   |   29.4  | timeSeriesProfile | 2012-06-17 02:54:00 |                        65 |                 6    | 2012-08-17 05:30:00 | 61.1848 | -150.202 |       61.1848 |       -150.202 |            24.05 |       61.1848 |       -150.202 | Fire Island, North of      | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1209/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1209 |
| 23 | COI1210   |   43.3  | timeSeriesProfile | 2012-06-15 22:12:00 |                        45 |                 6    | 2012-08-16 23:35:00 | 60.887  | -151.233 |       60.887  |       -151.233 |            41.34 |       60.887  |       -151.233 | Middle Ground Shoal, E of. | True          | up            |            | Cook Inlet 2012 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/COI1210/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=COI1210 |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_coi_other"))
```

## Map of Moored ADCPs
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_coi_other")("adcp_moored_noaa_coi_other")
    
```

## COI0206
        

```{code-cell}
:tags: [full-width]

cat['COI0206'].plot.ualong() + cat['COI0206'].plot.vacross()
```

## COI0207
        

```{code-cell}
:tags: [full-width]

cat['COI0207'].plot.ualong() + cat['COI0207'].plot.vacross()
```

## COI0213
        

```{code-cell}
:tags: [full-width]

cat['COI0213'].plot.ualong() + cat['COI0213'].plot.vacross()
```

## COI0301
        

```{code-cell}
:tags: [full-width]

cat['COI0301'].plot.ualong() + cat['COI0301'].plot.vacross()
```

## COI0302
        

```{code-cell}
:tags: [full-width]

cat['COI0302'].plot.ualong() + cat['COI0302'].plot.vacross()
```

## COI0303
        

```{code-cell}
:tags: [full-width]

cat['COI0303'].plot.ualong() + cat['COI0303'].plot.vacross()
```

## COI0306
        

```{code-cell}
:tags: [full-width]

cat['COI0306'].plot.ualong() + cat['COI0306'].plot.vacross()
```

## COI0307
        

```{code-cell}
:tags: [full-width]

cat['COI0307'].plot.ualong() + cat['COI0307'].plot.vacross()
```

## COI0418
        

```{code-cell}
:tags: [full-width]

cat['COI0418'].plot.ualong() + cat['COI0418'].plot.vacross()
```

## COI0419
        

```{code-cell}
:tags: [full-width]

cat['COI0419'].plot.ualong() + cat['COI0419'].plot.vacross()
```

## COI0420
        

```{code-cell}
:tags: [full-width]

cat['COI0420'].plot.ualong() + cat['COI0420'].plot.vacross()
```

## COI0421
        

```{code-cell}
:tags: [full-width]

cat['COI0421'].plot.ualong() + cat['COI0421'].plot.vacross()
```

## COI0422
        

```{code-cell}
:tags: [full-width]

cat['COI0422'].plot.ualong() + cat['COI0422'].plot.vacross()
```

## COI0801
        

```{code-cell}
:tags: [full-width]

cat['COI0801'].plot.ualong() + cat['COI0801'].plot.vacross()
```

## COI0802
        

```{code-cell}
:tags: [full-width]

cat['COI0802'].plot.ualong() + cat['COI0802'].plot.vacross()
```

## COI1201
        

```{code-cell}
:tags: [full-width]

cat['COI1201'].plot.ualong() + cat['COI1201'].plot.vacross()
```

## COI1202
        

```{code-cell}
:tags: [full-width]

cat['COI1202'].plot.ualong() + cat['COI1202'].plot.vacross()
```

## COI1203
        

```{code-cell}
:tags: [full-width]

cat['COI1203'].plot.ualong() + cat['COI1203'].plot.vacross()
```

## COI1204
        

```{code-cell}
:tags: [full-width]

cat['COI1204'].plot.ualong() + cat['COI1204'].plot.vacross()
```

## COI1205
        

```{code-cell}
:tags: [full-width]

cat['COI1205'].plot.ualong() + cat['COI1205'].plot.vacross()
```

## COI1207
        

```{code-cell}
:tags: [full-width]

cat['COI1207'].plot.ualong() + cat['COI1207'].plot.vacross()
```

## COI1208
        

```{code-cell}
:tags: [full-width]

cat['COI1208'].plot.ualong() + cat['COI1208'].plot.vacross()
```

## COI1209
        

```{code-cell}
:tags: [full-width]

cat['COI1209'].plot.ualong() + cat['COI1209'].plot.vacross()
```

## COI1210
        

```{code-cell}
:tags: [full-width]

cat['COI1210'].plot.ualong() + cat['COI1210'].plot.vacross()
```
