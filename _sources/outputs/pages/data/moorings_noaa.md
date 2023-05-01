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

# NOAA Moorings: Miscellaneous locations

* Moorings from NOAA
* moorings_noaa
* From 1999 (and earlier) to 2023, variable

Moorings from NOAA

Geese Island, Sitkalidak Island, Bear Cove, Anchorage, Kodiak Island, Alitak, Seldovia, Old Harbor, Boulder Point, Albatross Banks, Shelikof Strait




Dataset metadata:
|    | Dataset                       | datasetID                     | featuretype   | griddap   | info_url                                                                           | institution                                                              |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                    | tabledap                                                                     | title                               |
|---:|:------------------------------|:------------------------------|:--------------|:----------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|:------------------------------------|
|  0 | boulder-point                 | boulder-point                 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/boulder-point/index.csv                 | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       60.7767 |       -151.245 | 1999-09-13 20:00:00+00:00 |       60.7767 |       -151.245 | 1999-08-14 00:00:00+00:00 | Timeseries data from 'Boulder Point, AK' (boulder-point)                                   | https://erddap.sensors.ioos.us/erddap/tabledap/boulder-point                 | Boulder Point, AK                   |
|  1 | geese-island-gps-tide-buoy    | geese-island-gps-tide-buoy    | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/geese-island-gps-tide-buoy/index.csv    | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       56.5947 |       -153.996 | 2016-07-30 17:00:00+00:00 |       56.5947 |       -153.996 | 2016-06-25 06:00:00+00:00 | Timeseries data from 'Geese Island Gps Tide Buoy, AK' (geese-island-gps-tide-buoy)         | https://erddap.sensors.ioos.us/erddap/tabledap/geese-island-gps-tide-buoy    | Geese Island Gps Tide Buoy, AK      |
|  2 | noaa_nos_co_ops_9455500       | noaa_nos_co_ops_9455500       | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9455500/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       59.4405 |       -151.72  | 2023-05-08 14:00:00+00:00 |       59.4405 |       -151.72  | 1975-07-12 10:00:00+00:00 | Timeseries data from 'Seldovia, AK (OVIA2)' (noaa_nos_co_ops_9455500)                      | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9455500       | Seldovia, AK (OVIA2)                |
|  3 | noaa_nos_co_ops_9455595       | noaa_nos_co_ops_9455595       | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9455595/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       59.725  |       -151.023 | 2023-05-08 14:00:00+00:00 |       59.725  |       -151.023 | 2008-07-03 23:00:00+00:00 | Timeseries data from 'Bear Cove, Kachemak Bay, AK' (noaa_nos_co_ops_9455595)               | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9455595       | Bear Cove, Kachemak Bay, AK         |
|  4 | noaa_nos_co_ops_9455920       | noaa_nos_co_ops_9455920       | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9455920/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       61.2375 |       -149.89  | 2023-05-08 14:00:00+00:00 |       61.2375 |       -149.89  | 1978-10-02 05:00:00+00:00 | Timeseries data from 'Anchorage, AK (ANTA2)' (noaa_nos_co_ops_9455920)                     | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9455920       | Anchorage, AK (ANTA2)               |
|  5 | noaa_nos_co_ops_9457804       | noaa_nos_co_ops_9457804       | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_9457804/index.csv       | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       56.8974 |       -154.248 | 2023-05-08 14:00:00+00:00 |       56.8974 |       -154.248 | 2006-05-18 22:00:00+00:00 | Timeseries data from 'Alitak, AK (ALIA2)' (noaa_nos_co_ops_9457804)                        | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_9457804       | Alitak, AK (ALIA2)                  |
|  6 | noaa_nos_co_ops_kdaa2         | noaa_nos_co_ops_kdaa2         | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/noaa_nos_co_ops_kdaa2/index.csv         | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       57.73   |       -152.514 | 2023-05-01 13:00:00+00:00 |       57.73   |       -152.514 | 2018-03-03 23:06:00+00:00 | Timeseries data from 'KDAA2 - 9457292- Kodiak Island, AK' (noaa_nos_co_ops_kdaa2)          | https://erddap.sensors.ioos.us/erddap/tabledap/noaa_nos_co_ops_kdaa2         | KDAA2 - 9457292- Kodiak Island, AK  |
|  7 | old-harbor-1                  | old-harbor-1                  | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/old-harbor-1/index.csv                  | NOAA National Tsunami Warning Center (NTWC)                              |       57.1998 |       -153.307 | 2018-08-27 15:00:00+00:00 |       57.1998 |       -153.307 | 2014-09-20 13:00:00+00:00 | Timeseries data from 'Old Harbor' (old-harbor-1)                                           | https://erddap.sensors.ioos.us/erddap/tabledap/old-harbor-1                  | Old Harbor                          |
|  8 | sitkalidak-island-gps-tide-bu | sitkalidak-island-gps-tide-bu | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/sitkalidak-island-gps-tide-bu/index.csv | NOAA Center for Operational Oceanographic Products and Services (CO-OPS) |       56.9657 |       -153.252 | 2016-07-27 16:00:00+00:00 |       56.9657 |       -153.252 | 2016-06-25 06:00:00+00:00 | Timeseries data from 'Sitkalidak Island Gps Tide Buoy, AK' (sitkalidak-island-gps-tide-bu) | https://erddap.sensors.ioos.us/erddap/tabledap/sitkalidak-island-gps-tide-bu | Sitkalidak Island Gps Tide Buoy, AK |
|  9 | wmo_46077                     | wmo_46077                     | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/wmo_46077/index.csv                     | NOAA National Data Buoy Center (NDBC)                                    |       57.892  |       -154.291 | 2023-05-01 09:00:00+00:00 |       57.892  |       -154.291 | 2017-06-14 10:50:00+00:00 | Timeseries data from '46077 - Shelikof Strait, AK' (urn:ioos:station:wmo:46077)            | https://erddap.sensors.ioos.us/erddap/tabledap/wmo_46077                     | 46077 - Shelikof Strait, AK         |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_noaa"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_noaa")("moorings_noaa")
    
```

## boulder-point
        

```{code-cell}
cat['boulder-point'].plot.data()
```

## geese-island-gps-tide-buoy
        

```{code-cell}
cat['geese-island-gps-tide-buoy'].plot.data()
```

## noaa_nos_co_ops_9455500
        

```{code-cell}
cat['noaa_nos_co_ops_9455500'].plot.data()
```

## noaa_nos_co_ops_9455595
        

```{code-cell}
cat['noaa_nos_co_ops_9455595'].plot.data()
```

## noaa_nos_co_ops_9455920
        

```{code-cell}
cat['noaa_nos_co_ops_9455920'].plot.data()
```

## noaa_nos_co_ops_9457804
        

```{code-cell}
cat['noaa_nos_co_ops_9457804'].plot.data()
```

## noaa_nos_co_ops_kdaa2
        

```{code-cell}
cat['noaa_nos_co_ops_kdaa2'].plot.data()
```

## old-harbor-1
        

```{code-cell}
cat['old-harbor-1'].plot.data()
```

## sitkalidak-island-gps-tide-bu
        

```{code-cell}
cat['sitkalidak-island-gps-tide-bu'].plot.data()
```

## wmo_46077
        

```{code-cell}
cat['wmo_46077'].plot.data()
```
