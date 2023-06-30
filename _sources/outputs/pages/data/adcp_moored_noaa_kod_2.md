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

(page:adcp_moored_noaa_kod_2)=
# Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 2

* Kodiak Island 2009 Current Survey (2)
* adcp_moored_noaa_kod_2
* 2009, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.




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



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_kod_2"))
```

## Map of Moored ADCPs
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_kod_2")("adcp_moored_noaa_kod_2")
```

## KOD0926
        

```{code-cell}
:tags: [remove-input]

cat['KOD0926'].plot.ualong() + cat['KOD0926'].plot.vacross()
```

## KOD0927
        

```{code-cell}
:tags: [remove-input]

cat['KOD0927'].plot.ualong() + cat['KOD0927'].plot.vacross()
```

## KOD0928
        

```{code-cell}
:tags: [remove-input]

cat['KOD0928'].plot.ualong() + cat['KOD0928'].plot.vacross()
```

## KOD0929
        

```{code-cell}
:tags: [remove-input]

cat['KOD0929'].plot.ualong() + cat['KOD0929'].plot.vacross()
```

## KOD0930
        

```{code-cell}
:tags: [remove-input]

cat['KOD0930'].plot.ualong() + cat['KOD0930'].plot.vacross()
```

## KOD0931
        

```{code-cell}
:tags: [remove-input]

cat['KOD0931'].plot.ualong() + cat['KOD0931'].plot.vacross()
```

## KOD0932
        

```{code-cell}
:tags: [remove-input]

cat['KOD0932'].plot.ualong() + cat['KOD0932'].plot.vacross()
```

## KOD0933
        

```{code-cell}
:tags: [remove-input]

cat['KOD0933'].plot.ualong() + cat['KOD0933'].plot.vacross()
```

## KOD0934
        

```{code-cell}
:tags: [remove-input]

cat['KOD0934'].plot.ualong() + cat['KOD0934'].plot.vacross()
```

## KOD0935
        

```{code-cell}
:tags: [remove-input]

cat['KOD0935'].plot.ualong() + cat['KOD0935'].plot.vacross()
```

## KOD0936
        

```{code-cell}
:tags: [remove-input]

cat['KOD0936'].plot.ualong() + cat['KOD0936'].plot.vacross()
```

## KOD0937
        

```{code-cell}
:tags: [remove-input]

cat['KOD0937'].plot.ualong() + cat['KOD0937'].plot.vacross()
```

## KOD0938
        

```{code-cell}
:tags: [remove-input]

cat['KOD0938'].plot.ualong() + cat['KOD0938'].plot.vacross()
```

## KOD0939
        

```{code-cell}
:tags: [remove-input]

cat['KOD0939'].plot.ualong() + cat['KOD0939'].plot.vacross()
```

## KOD0940
        

```{code-cell}
:tags: [remove-input]

cat['KOD0940'].plot.ualong() + cat['KOD0940'].plot.vacross()
```

## KOD0941
        

```{code-cell}
:tags: [remove-input]

cat['KOD0941'].plot.ualong() + cat['KOD0941'].plot.vacross()
```

## KOD0942
        

```{code-cell}
:tags: [remove-input]

cat['KOD0942'].plot.ualong() + cat['KOD0942'].plot.vacross()
```

## KOD0943
        

```{code-cell}
:tags: [remove-input]

cat['KOD0943'].plot.ualong() + cat['KOD0943'].plot.vacross()
```

## KOD0944
        

```{code-cell}
:tags: [remove-input]

cat['KOD0944'].plot.ualong() + cat['KOD0944'].plot.vacross()
```
