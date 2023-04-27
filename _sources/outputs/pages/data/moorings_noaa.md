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
```

# NOAA Moorings: Geese Island, Sitkalidak Island, Bear Cove, Anchorage, Kodiak Island, Alitak, Seldovia, Old Harbor, Boulder Point, Albatross Banks, Shelikof Strait

* Moorings from NOAA
* moorings_noaa
* From 1999 (and earlier) to 2023, variable

Moorings from NOAA




    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_noaa"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_noaa")("moorings_noaa")
    
```

## boulder-point
        

+++

            
|    | datasetID     | featuretype   | griddap   | info_url                                                           | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                  | tabledap                                                     | title             |
|---:|:--------------|:--------------|:----------|:-------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:---------------------------------------------------------|:-------------------------------------------------------------|:------------------|
|  0 | boulder-point | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/boulder-point/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |       60.7767 |       -151.245 | 1999-09-13T20:00:00Z |       60.7767 |       -151.245 | 1999-08-14T00:00:00Z | Timeseries data from 'Boulder Point, AK' (boulder-point) | https://erddap.sensors.ioos.us/erddap/tabledap/boulder-point | Boulder Point, AK |


```{code-cell}
cat['boulder-point'].plot.data()
```

## geese-island-gps-tide-buoy
        

+++

            
|    | datasetID                  | featuretype   | griddap   | info_url                                                                        | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                            | tabledap                                                                  | title                          |
|---:|:---------------------------|:--------------|:----------|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------|:-------------------------------|
|  0 | geese-island-gps-tide-buoy | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/geese-island-gps-tide-buoy/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |       56.5947 |       -153.996 | 2016-07-30T17:00:00Z |       56.5947 |       -153.996 | 2016-06-25T06:00:00Z | Timeseries data from 'Geese Island Gps Tide Buoy, AK' (geese-island-gps-tide-buoy) | https://erddap.sensors.ioos.us/erddap/tabledap/geese-island-gps-tide-buoy | Geese Island Gps Tide Buoy, AK |


```{code-cell}
cat['geese-island-gps-tide-buoy'].plot.data()
```

## noaa_nos_co_ops_9455500
        

+++

            
|    | datasetID               | featuretype   | griddap   | info_url                                                                     | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                               | tabledap                                                               | title                |
|---:|:------------------------|:--------------|:----------|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------|:---------------------|
|  0 | noaa_nos_co_ops_9455500 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9455500/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |       59.4405 |        -151.72 | 2023-05-04T01:00:00Z |       59.4405 |        -151.72 | 1975-07-12T10:00:00Z | Timeseries data from 'Seldovia, AK (OVIA2)' (noaa_nos_co_ops_9455500) | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9455500 | Seldovia, AK (OVIA2) |


```{code-cell}
cat['noaa_nos_co_ops_9455500'].plot.data()
```

## noaa_nos_co_ops_9455595
        

+++

            
|    | datasetID               | featuretype   | griddap   | info_url                                                                     | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                      | tabledap                                                               | title                       |
|---:|:------------------------|:--------------|:----------|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------|:----------------------------|
|  0 | noaa_nos_co_ops_9455595 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9455595/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |        59.725 |       -151.023 | 2023-05-04T01:00:00Z |        59.725 |       -151.023 | 2008-07-03T23:00:00Z | Timeseries data from 'Bear Cove, Kachemak Bay, AK' (noaa_nos_co_ops_9455595) | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9455595 | Bear Cove, Kachemak Bay, AK |


```{code-cell}
cat['noaa_nos_co_ops_9455595'].plot.data()
```

## noaa_nos_co_ops_9455920
        

+++

            
|    | datasetID               | featuretype   | griddap   | info_url                                                                     | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                | tabledap                                                               | title                 |
|---:|:------------------------|:--------------|:----------|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------|:----------------------|
|  0 | noaa_nos_co_ops_9455920 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9455920/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |       61.2375 |        -149.89 | 2023-05-04T01:00:00Z |       61.2375 |        -149.89 | 1978-10-02T05:00:00Z | Timeseries data from 'Anchorage, AK (ANTA2)' (noaa_nos_co_ops_9455920) | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9455920 | Anchorage, AK (ANTA2) |


```{code-cell}
cat['noaa_nos_co_ops_9455920'].plot.data()
```

## noaa_nos_co_ops_9457804
        

+++

            
|    | datasetID               | featuretype   | griddap   | info_url                                                                     | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                             | tabledap                                                               | title              |
|---:|:------------------------|:--------------|:----------|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------|:-----------------------------------------------------------------------|:-------------------|
|  0 | noaa_nos_co_ops_9457804 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9457804/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |       56.8974 |       -154.248 | 2023-05-04T01:00:00Z |       56.8974 |       -154.248 | 2006-05-18T22:00:00Z | Timeseries data from 'Alitak, AK (ALIA2)' (noaa_nos_co_ops_9457804) | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9457804 | Alitak, AK (ALIA2) |


```{code-cell}
cat['noaa_nos_co_ops_9457804'].plot.data()
```

## noaa_nos_co_ops_kdaa2
        

+++

            
|    | datasetID             | featuretype   | griddap   | info_url                                                                   | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                           | tabledap                                                             | title                              |
|---:|:----------------------|:--------------|:----------|:---------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------|:-----------------------------------|
|  0 | noaa_nos_co_ops_kdaa2 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_kdaa2/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |         57.73 |       -152.514 | 2023-04-26T23:42:00Z |         57.73 |       -152.514 | 2018-03-03T23:06:00Z | Timeseries data from 'KDAA2 - 9457292- Kodiak Island, AK' (noaa_nos_co_ops_kdaa2) | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_kdaa2 | KDAA2 - 9457292- Kodiak Island, AK |


```{code-cell}
cat['noaa_nos_co_ops_kdaa2'].plot.data()
```

## old-harbor-1
        

+++

            
|    | datasetID    | featuretype   | griddap   | info_url                                                          | institution                                 | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                          | tabledap                                                    | title      |
|---:|:-------------|:--------------|:----------|:------------------------------------------------------------------|:--------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:-------------------------------------------------|:------------------------------------------------------------|:-----------|
|  0 | old-harbor-1 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/old-harbor-1/index.csv | NOAA National Tsunami Warning Center (NTWC) | point     |       57.1998 |       -153.307 | 2018-08-27T15:00:00Z |       57.1998 |       -153.307 | 2014-09-20T13:00:00Z | Timeseries data from 'Old Harbor' (old-harbor-1) | https://erddap.sensors.ioos.us/erddap/tabledap/old-harbor-1 | Old Harbor |


```{code-cell}
cat['old-harbor-1'].plot.data()
```

## sitkalidak-island-gps-tide-bu
        

+++

            
|    | datasetID                     | featuretype   | griddap   | info_url                                                                           | institution                                                              | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                                    | tabledap                                                                     | title                               |
|---:|:------------------------------|:--------------|:----------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|:------------------------------------|
|  0 | sitkalidak-island-gps-tide-bu | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/sitkalidak-island-gps-tide-bu/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) | point     |       56.9657 |       -153.252 | 2016-07-27T16:00:00Z |       56.9657 |       -153.252 | 2016-06-25T06:00:00Z | Timeseries data from 'Sitkalidak Island Gps Tide Buoy, AK' (sitkalidak-island-gps-tide-bu) | https://erddap.sensors.ioos.us/erddap/tabledap/sitkalidak-island-gps-tide-bu | Sitkalidak Island Gps Tide Buoy, AK |


```{code-cell}
cat['sitkalidak-island-gps-tide-bu'].plot.data()
```

## wmo_46077
        

+++

            
|    | datasetID   | featuretype   | griddap   | info_url                                                       | institution                           | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                         | tabledap                                                 | title                       |
|---:|:------------|:--------------|:----------|:---------------------------------------------------------------|:--------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------------------|:---------------------------------------------------------|:----------------------------|
|  0 | wmo_46077   | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/wmo_46077/index.csv | NOAA National Data Buoy Center (NDBC) | point     |        57.892 |       -154.291 | 2023-04-26T17:00:00Z |        57.892 |       -154.291 | 2017-06-14T10:50:00Z | Timeseries data from '46077 - Shelikof Strait, AK' (urn:ioos:station:wmo:46077) | https://erddap.sensors.ioos.us/erddap/tabledap/wmo_46077 | 46077 - Shelikof Strait, AK |


```{code-cell}
cat['wmo_46077'].plot.data()
```
