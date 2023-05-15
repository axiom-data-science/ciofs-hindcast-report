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

# Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 1

* Kodiak Island 2009 Current Survey (1)
* adcp_moored_noaa_kod_1
* 2009, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet

ADCP data has been converted to eastward, northward velocities as well as along- and across-channel velocities, in the latter case using the NOAA-provided rotation angle for the rotation. The along- and across-channel velocities are additionally filtered to show the subtidal signal, which is what is plotted in the dataset page.

Stations "KOD0914", "KOD0915", "KOD0916", "KOD0917", "KOD0918", "KOD0919", "KOD0920" are not included because they are just outside or along the model domain boundary.




<details><summary>Dataset metadata:</summary>

|    | Dataset   |   depth | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude |   measured_depth |   minLatitude |   minLongitude | name                               | observe_dst   | orientation   | ping_int   | project                           | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   | urlpath                                                       |
|---:|:----------|--------:|:------------------|:--------------------|--------------------------:|---------------------:|:--------------------|--------:|---------:|--------------:|---------------:|-----------------:|--------------:|---------------:|:-----------------------------------|:--------------|:--------------|:-----------|:----------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|:--------------------------------------------------------------|
|  0 | KOD0901   |    81.3 | timeSeriesProfile | 2009-05-29 18:06:00 |                       250 |                11.52 | 2009-07-10 22:30:00 | 57.7356 | -152.385 |       57.7356 |       -152.385 |            79.22 |       57.7356 |       -152.385 | Chiniak Bay                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0901/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0901 |
|  1 | KOD0902   |    18.4 | timeSeriesProfile | 2009-05-29 00:54:00 |                        20 |                 3    | 2009-07-10 21:30:00 | 57.7746 | -152.435 |       57.7746 |       -152.435 |            17.24 |       57.7746 |       -152.435 | St. Paul Harbor                    | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0902/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0902 |
|  2 | KOD0903   |    13.3 | timeSeriesProfile | 2009-05-29 03:42:00 |                        56 |                 0.6  | 2009-08-20 01:11:00 | 57.7892 | -152.394 |       57.7892 |       -152.394 |            12.64 |       57.7892 |       -152.394 | Kodiak Harbor Narrows, Chiniak Bay | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0903/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0903 |
|  3 | KOD0904   |    47.3 | timeSeriesProfile | 2009-05-29 03:00:00 |                        60 |                11.52 | 2009-07-10 23:54:00 | 57.8058 | -152.334 |       57.8058 |       -152.334 |            45.82 |       57.8058 |       -152.334 | Woody Island, N of                 | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0904/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0904 |
|  4 | KOD0905   |    31.2 | timeSeriesProfile | 2009-05-29 17:30:00 |                        20 |                 4.5  | 2009-07-10 23:24:00 | 57.7804 | -152.366 |       57.7804 |       -152.366 |            32.58 |       57.7804 |       -152.366 | Woody Channel                      | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0905/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0905 |
|  5 | KOD0906   |    77.7 | timeSeriesProfile | 2009-05-29 20:24:00 |                        20 |                 5.5  | 2009-07-11 19:17:00 | 57.6078 | -152.09  |       57.6078 |       -152.09  |            77.74 |       57.6078 |       -152.09  | Cape Chiniak                       | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0906/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0906 |
|  6 | KOD0907   |    73.9 | timeSeriesProfile | 2009-05-30 00:18:00 |                       220 |                 5.5  | 2009-07-12 01:06:00 | 57.3995 | -152.535 |       57.3995 |       -152.535 |            71.92 |       57.3995 |       -152.535 | Ugak Bay Entrance                  | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0907/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0907 |
|  7 | KOD0910   |   119   | timeSeriesProfile | 2009-05-30 19:00:00 |                       260 |                29.44 | 2009-07-12 19:12:00 | 57.2309 | -152.884 |       57.2309 |       -152.884 |           116.24 |       57.2309 |       -152.884 | Left Cape, E of                    | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0910/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0910 |
|  8 | KOD0911   |   123   | timeSeriesProfile | 2009-05-30 17:36:00 |                       250 |                29.44 | 2009-07-12 17:41:00 | 57.1978 | -153.105 |       57.1978 |       -153.105 |           119.83 |       57.1978 |       -153.105 | Cathedral Island, E of             | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0911/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0911 |
|  9 | KOD0912   |    74.2 | timeSeriesProfile | 2009-05-31 01:30:00 |                       330 |                11.52 | 2009-07-13 02:05:00 | 57.1787 | -153.325 |       57.1787 |       -153.325 |            71.36 |       57.1787 |       -153.325 | Old Harbor                         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0912/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0912 |
| 10 | KOD0913   |   120   | timeSeriesProfile | 2009-05-31 00:06:00 |                        30 |                29.44 | 2009-07-13 00:36:00 | 57.0732 | -153.451 |       57.0732 |       -153.451 |           114.81 |       57.0732 |       -153.451 | Natalia Peninsula, W of            | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0913/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0913 |
| 11 | KOD0921   |    71.9 | timeSeriesProfile | 2009-06-02 02:48:00 |                       350 |                 5.5  | 2009-07-15 01:24:00 | 57.2861 | -154.828 |       57.2861 |       -154.828 |            69.79 |       57.2861 |       -154.828 | Cape Ikolik                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0921/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0921 |
| 12 | KOD0922   |    62.6 | timeSeriesProfile | 2009-06-02 17:36:00 |                        10 |                 5.5  | 2009-07-15 02:54:00 | 57.4172 | -154.766 |       57.4172 |       -154.766 |            59.52 |       57.4172 |       -154.766 | Cape Grant                         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0922/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0922 |
| 13 | KOD0923   |    25   | timeSeriesProfile | 2009-06-03 01:18:00 |                       315 |                 4.42 | 2009-07-15 21:36:00 | 57.6373 | -153.995 |       57.6373 |       -153.995 |            23.71 |       57.6373 |       -153.995 | Uyak Anchorage                     | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0923/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0923 |
| 14 | KOD0924   |    16.8 | timeSeriesProfile | 2009-06-03 02:42:00 |                       290 |                 2.95 | 2009-07-15 23:00:00 | 57.5422 | -153.988 |       57.5422 |       -153.988 |            15.16 |       57.5422 |       -153.988 | Larsen Bay                         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0924/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0924 |
| 15 | KOD0925   |    63   | timeSeriesProfile | 2009-06-02 23:36:00 |                        45 |                 5.5  | 2009-07-16 21:48:00 | 57.7935 | -154.032 |       57.7935 |       -154.032 |            61.33 |       57.7935 |       -154.032 | Cape Kuliuk                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0925/deployments.json |                |                -9 | metric  | https://tidesandcurrents.noaa.gov/stationhome.html?id=KOD0925 |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_kod_1"))
```

## Map of Moored ADCPs
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_kod_1")("adcp_moored_noaa_kod_1")
    
```

## KOD0901
        

```{code-cell}
:tags: [full-width]

cat['KOD0901'].plot.ualong() + cat['KOD0901'].plot.vacross()
```

## KOD0902
        

```{code-cell}
:tags: [full-width]

cat['KOD0902'].plot.ualong() + cat['KOD0902'].plot.vacross()
```

## KOD0903
        

```{code-cell}
:tags: [full-width]

cat['KOD0903'].plot.ualong() + cat['KOD0903'].plot.vacross()
```

## KOD0904
        

```{code-cell}
:tags: [full-width]

cat['KOD0904'].plot.ualong() + cat['KOD0904'].plot.vacross()
```

## KOD0905
        

```{code-cell}
:tags: [full-width]

cat['KOD0905'].plot.ualong() + cat['KOD0905'].plot.vacross()
```

## KOD0906
        

```{code-cell}
:tags: [full-width]

cat['KOD0906'].plot.ualong() + cat['KOD0906'].plot.vacross()
```

## KOD0907
        

```{code-cell}
:tags: [full-width]

cat['KOD0907'].plot.ualong() + cat['KOD0907'].plot.vacross()
```

## KOD0910
        

```{code-cell}
:tags: [full-width]

cat['KOD0910'].plot.ualong() + cat['KOD0910'].plot.vacross()
```

## KOD0911
        

```{code-cell}
:tags: [full-width]

cat['KOD0911'].plot.ualong() + cat['KOD0911'].plot.vacross()
```

## KOD0912
        

```{code-cell}
:tags: [full-width]

cat['KOD0912'].plot.ualong() + cat['KOD0912'].plot.vacross()
```

## KOD0913
        

```{code-cell}
:tags: [full-width]

cat['KOD0913'].plot.ualong() + cat['KOD0913'].plot.vacross()
```

## KOD0921
        

```{code-cell}
:tags: [full-width]

cat['KOD0921'].plot.ualong() + cat['KOD0921'].plot.vacross()
```

## KOD0922
        

```{code-cell}
:tags: [full-width]

cat['KOD0922'].plot.ualong() + cat['KOD0922'].plot.vacross()
```

## KOD0923
        

```{code-cell}
:tags: [full-width]

cat['KOD0923'].plot.ualong() + cat['KOD0923'].plot.vacross()
```

## KOD0924
        

```{code-cell}
:tags: [full-width]

cat['KOD0924'].plot.ualong() + cat['KOD0924'].plot.vacross()
```

## KOD0925
        

```{code-cell}
:tags: [full-width]

cat['KOD0925'].plot.ualong() + cat['KOD0925'].plot.vacross()
```
