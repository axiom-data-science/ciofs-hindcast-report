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

# NOAA ADCP survey Kodiak Island: Set 2

* Kodiak Island 2009 Current Survey (2)
* adcp_moored_noaa_kod_2
* 2009, each for one or a few months

Moored NOAA ADCP surveys in Cook Inlet




Dataset metadata:
|    | Dataset   |   depth | featuretype       | first_good_data     |   flood_direction_degrees |   height_from_bottom | last_good_data      |     lat |      lon |   maxLatitude |   maxLongitude |   measured_depth |   minLatitude |   minLongitude | name                                      | observe_dst   | orientation   | ping_int   | project                           | project_type   |   sample_interval | self                                                                                      | sensor_depth   |   timezone_offset | units   |
|---:|:----------|--------:|:------------------|:--------------------|--------------------------:|---------------------:|:--------------------|--------:|---------:|--------------:|---------------:|-----------------:|--------------:|---------------:|:------------------------------------------|:--------------|:--------------|:-----------|:----------------------------------|:---------------|------------------:|:------------------------------------------------------------------------------------------|:---------------|------------------:|:--------|
|  0 | KOD0926   |    59   | timeSeriesProfile | 2009-06-03 23:36:00 |                        50 |                 5.5  | 2009-08-30 01:06:00 | 58.2145 | -153.22  |       58.2145 |       -153.22  |            56.58 |       58.2145 |       -153.22  | Steep Cape                                | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0926/deployments.json |                |                -9 | metric  |
|  1 | KOD0927   |    86.2 | timeSeriesProfile | 2009-07-17 02:00:00 |                       270 |                 5.6  | 2009-08-29 20:18:00 | 58.019  | -153.43  |       58.019  |       -153.43  |            85.28 |       58.019  |       -153.43  | Raspberry Cape, S of                      | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0927/deployments.json |                |                -9 | metric  |
|  2 | KOD0928   |    61.8 | timeSeriesProfile | 2009-07-17 03:30:00 |                       285 |                 5.6  | 2009-09-01 18:06:00 | 57.9976 | -153.156 |       57.9976 |       -153.156 |            57.46 |       57.9976 |       -153.156 | Kupreanof Strait                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0928/deployments.json |                |                -9 | metric  |
|  3 | KOD0929   |    28.9 | timeSeriesProfile | 2009-07-22 04:48:00 |                       280 |                 4.52 | 2009-09-01 20:54:00 | 57.9604 | -152.901 |       57.9604 |       -152.901 |            28.24 |       57.9604 |       -152.901 | Kupreanof Strait, 0.8 mi. off Chernof Pt. | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0929/deployments.json |                |                -9 | metric  |
|  4 | KOD0930   |    32.9 | timeSeriesProfile | 2009-07-22 15:48:00 |                       280 |                 5.6  | 2009-09-01 20:54:00 | 57.9396 | -152.863 |       57.9396 |       -152.863 |            34.04 |       57.9396 |       -152.863 | Whale Passage, Northwest Entrance         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0930/deployments.json |                |                -9 | metric  |
|  5 | KOD0931   |    31.3 | timeSeriesProfile | 2009-07-17 17:24:00 |                       285 |                 5.6  | 2009-09-02 02:24:00 | 57.9188 | -152.795 |       57.9188 |       -152.795 |            29.83 |       57.9188 |       -152.795 | Whale Passage, off Bird Point             | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0931/deployments.json |                |                -9 | metric  |
|  6 | KOD0932   |    59.1 | timeSeriesProfile | 2009-07-17 17:54:00 |                       330 |                 5.6  | 2009-09-02 01:00:00 | 57.9075 | -152.777 |       57.9075 |       -152.777 |            61.22 |       57.9075 |       -152.777 | Shag Rocks                                | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0932/deployments.json |                |                -9 | metric  |
|  7 | KOD0933   |    34.1 | timeSeriesProfile | 2009-07-17 20:12:00 |                       290 |                 5.6  | 2009-09-01 23:30:00 | 57.9121 | -152.524 |       57.9121 |       -152.524 |            34.32 |       57.9121 |       -152.524 | Narrow Strait, off Ouzinkie Point         | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0933/deployments.json |                |                -9 | metric  |
|  8 | KOD0934   |    41.1 | timeSeriesProfile | 2009-07-17 18:54:00 |                       260 |                 5.6  | 2009-09-01 01:30:00 | 57.9947 | -152.684 |       57.9947 |       -152.684 |            39.22 |       57.9947 |       -152.684 | Afognak Strait, East Entrance             | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0934/deployments.json |                |                -9 | metric  |
|  9 | KOD0935   |    64.3 | timeSeriesProfile | 2009-07-21 21:06:00 |                       160 |                 5.6  | 2009-08-29 23:06:00 | 58.0718 | -153.065 |       58.0718 |       -153.065 |            61.43 |       58.0718 |       -153.065 | Raspberry Strait                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0935/deployments.json |                |                -9 | metric  |
| 10 | KOD0936   |    42.2 | timeSeriesProfile | 2009-07-20 23:24:00 |                       180 |                 5.6  | 2009-08-30 17:42:00 | 58.4057 | -152.907 |       58.4057 |       -152.907 |            38.67 |       58.4057 |       -152.907 | Black Cape                                | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0936/deployments.json |                |                -9 | metric  |
| 11 | KOD0937   |    43.8 | timeSeriesProfile | 2009-07-20 22:30:00 |                       235 |                 5.6  | 2009-08-30 18:30:00 | 58.4611 | -152.826 |       58.4611 |       -152.826 |            40.49 |       58.4611 |       -152.826 | Alligator Island                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0937/deployments.json |                |                -9 | metric  |
| 12 | KOD0938   |   109   | timeSeriesProfile | 2009-07-20 21:30:00 |                       250 |                25.17 | 2009-08-31 00:29:00 | 58.4852 | -152.67  |       58.4852 |       -152.67  |           120.59 |       58.4852 |       -152.67  | Lighthouse Point                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0938/deployments.json |                |                -9 | metric  |
| 13 | KOD0939   |    36   | timeSeriesProfile | 2009-07-20 20:12:00 |                       275 |                 5.6  | 2009-08-31 02:23:00 | 58.4669 | -152.495 |       58.4669 |       -152.495 |            37.99 |       58.4669 |       -152.495 | Cape Current Narrows, Shuyak Strait       | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0939/deployments.json |                |                -9 | metric  |
| 14 | KOD0940   |   108   | timeSeriesProfile | 2009-07-20 00:00:00 |                       215 |                29.67 | 2009-08-31 02:17:00 | 58.4579 | -152.428 |       58.4579 |       -152.428 |           105.6  |       58.4579 |       -152.428 | East Shuyak Strait                        | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0940/deployments.json |                |                -9 | metric  |
| 15 | KOD0941   |    50.5 | timeSeriesProfile | 2009-07-19 00:24:00 |                       350 |                 5.6  | 2009-08-31 19:12:00 | 58.346  | -151.915 |       58.346  |       -151.915 |            51.8  |       58.346  |       -151.915 | Tonki Cape, E of                          | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0941/deployments.json |                |                -9 | metric  |
| 16 | KOD0942   |    63.2 | timeSeriesProfile | 2009-07-18 23:12:00 |                         0 |                 5.6  | 2009-08-31 20:36:00 | 58.2444 | -151.932 |       58.2444 |       -151.932 |            61.21 |       58.2444 |       -151.932 | Marmot Island, W of                       | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0942/deployments.json |                |                -9 | metric  |
| 17 | KOD0943   |    66.2 | timeSeriesProfile | 2009-07-18 22:06:00 |                         5 |                 5.6  | 2009-08-31 21:47:00 | 58.1709 | -151.969 |       58.1709 |       -151.969 |            64.52 |       58.1709 |       -151.969 | Marmot Island, SW of                      | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0943/deployments.json |                |                -9 | metric  |
| 18 | KOD0944   |    63.1 | timeSeriesProfile | 2009-07-19 19:42:00 |                       270 |                11.52 | 2009-08-30 21:24:00 | 58.6511 | -152.397 |       58.6511 |       -152.397 |            59.74 |       58.6511 |       -152.397 | Perevalnie Island, N of                   | True          | up            |            | Kodiak Island 2009 Current Survey | Survey         |               360 | https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/KOD0944/deployments.json |                |                -9 | metric  |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("adcp_moored_noaa_kod_2"))
```

## Map of Moored ADCPs
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "adcp_moored_noaa_kod_2")("adcp_moored_noaa_kod_2")
    
```

## KOD0926
        

```{code-cell}
cat['KOD0926'].plot.ualong() + cat['KOD0926'].plot.vacross()
```

## KOD0927
        

```{code-cell}
cat['KOD0927'].plot.ualong() + cat['KOD0927'].plot.vacross()
```

## KOD0928
        

```{code-cell}
cat['KOD0928'].plot.ualong() + cat['KOD0928'].plot.vacross()
```

## KOD0929
        

```{code-cell}
cat['KOD0929'].plot.ualong() + cat['KOD0929'].plot.vacross()
```

## KOD0930
        

```{code-cell}
cat['KOD0930'].plot.ualong() + cat['KOD0930'].plot.vacross()
```

## KOD0931
        

```{code-cell}
cat['KOD0931'].plot.ualong() + cat['KOD0931'].plot.vacross()
```

## KOD0932
        

```{code-cell}
cat['KOD0932'].plot.ualong() + cat['KOD0932'].plot.vacross()
```

## KOD0933
        

```{code-cell}
cat['KOD0933'].plot.ualong() + cat['KOD0933'].plot.vacross()
```

## KOD0934
        

```{code-cell}
cat['KOD0934'].plot.ualong() + cat['KOD0934'].plot.vacross()
```

## KOD0935
        

```{code-cell}
cat['KOD0935'].plot.ualong() + cat['KOD0935'].plot.vacross()
```

## KOD0936
        

```{code-cell}
cat['KOD0936'].plot.ualong() + cat['KOD0936'].plot.vacross()
```

## KOD0937
        

```{code-cell}
cat['KOD0937'].plot.ualong() + cat['KOD0937'].plot.vacross()
```

## KOD0938
        

```{code-cell}
cat['KOD0938'].plot.ualong() + cat['KOD0938'].plot.vacross()
```

## KOD0939
        

```{code-cell}
cat['KOD0939'].plot.ualong() + cat['KOD0939'].plot.vacross()
```

## KOD0940
        

```{code-cell}
cat['KOD0940'].plot.ualong() + cat['KOD0940'].plot.vacross()
```

## KOD0941
        

```{code-cell}
cat['KOD0941'].plot.ualong() + cat['KOD0941'].plot.vacross()
```

## KOD0942
        

```{code-cell}
cat['KOD0942'].plot.ualong() + cat['KOD0942'].plot.vacross()
```

## KOD0943
        

```{code-cell}
cat['KOD0943'].plot.ualong() + cat['KOD0943'].plot.vacross()
```

## KOD0944
        

```{code-cell}
cat['KOD0944'].plot.ualong() + cat['KOD0944'].plot.vacross()
```
