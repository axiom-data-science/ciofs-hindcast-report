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
import holoviews as hv
from holoviews import opts
```

(page:adcp_moored_noaa_kod_1)=
# Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 1

* Kodiak Island 2009 Current Survey (1)
* adcp_moored_noaa_kod_1
* 2009, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.

Stations "KOD0914", "KOD0915", "KOD0916", "KOD0917", "KOD0918", "KOD0919", "KOD0920" are not included because they are just outside or along the model domain boundary.




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



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_kod_1"))
```

## Map of Moored ADCPs
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_kod_1")("adcp_moored_noaa_kod_1")
```

## KOD0901
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0901'].plot.ualong() + cat['KOD0901'].plot.vacross()
```

## KOD0902
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0902'].plot.ualong() + cat['KOD0902'].plot.vacross()
```

## KOD0903
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0903'].plot.ualong() + cat['KOD0903'].plot.vacross()
```

## KOD0904
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0904'].plot.ualong() + cat['KOD0904'].plot.vacross()
```

## KOD0905
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0905'].plot.ualong() + cat['KOD0905'].plot.vacross()
```

## KOD0906
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0906'].plot.ualong() + cat['KOD0906'].plot.vacross()
```

## KOD0907
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0907'].plot.ualong() + cat['KOD0907'].plot.vacross()
```

## KOD0910
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0910'].plot.ualong() + cat['KOD0910'].plot.vacross()
```

## KOD0911
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0911'].plot.ualong() + cat['KOD0911'].plot.vacross()
```

## KOD0912
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0912'].plot.ualong() + cat['KOD0912'].plot.vacross()
```

## KOD0913
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0913'].plot.ualong() + cat['KOD0913'].plot.vacross()
```

## KOD0921
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0921'].plot.ualong() + cat['KOD0921'].plot.vacross()
```

## KOD0922
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0922'].plot.ualong() + cat['KOD0922'].plot.vacross()
```

## KOD0923
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0923'].plot.ualong() + cat['KOD0923'].plot.vacross()
```

## KOD0924
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0924'].plot.ualong() + cat['KOD0924'].plot.vacross()
```

## KOD0925
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KOD0925'].plot.ualong() + cat['KOD0925'].plot.vacross()
```
