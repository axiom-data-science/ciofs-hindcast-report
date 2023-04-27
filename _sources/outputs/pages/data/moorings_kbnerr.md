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

# KBNERR Moorings: Kachemak Bay

* Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* moorings_kbnerr
* From 2003 to present day, variable

Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
nerrs_kacsdwq :: kacsdwq
nerrs_kachdwq :: kachdwq
homer-dolphin-surface-water-q :: kachswq
nerrs_kach3wq :: kach3wq
nerrs_kacsswq :: kacsswq

cdmo_nerrs_bearcove :: This is a different station than kacbcwq, which was active 2002-2003 while this is in 2015. They are also in different locations.
    
More information: https://accs.uaa.alaska.edu/kbnerr/


These are accessed through AOOS portal/ERDDAP server.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_kbnerr"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr")("moorings_kbnerr")
    
```

## cdmo_nerrs_bearcove
        

+++

            
|    | datasetID           | featuretype   | griddap   | info_url                                                                 | institution                                               | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                              | tabledap                                                           | title                   |
|---:|:--------------------|:--------------|:----------|:-------------------------------------------------------------------------|:----------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:---------------------------------------------------------------------|:-------------------------------------------------------------------|:------------------------|
|  0 | cdmo_nerrs_bearcove | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/cdmo_nerrs_bearcove/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | point     |       59.7262 |       -151.049 | 2015-11-20T17:15:00Z |       59.7262 |       -151.049 | 2015-05-05T14:00:00Z | Timeseries data from 'Bear Cove Water Quality' (cdmo_nerrs_bearcove) | https://erddap.sensors.ioos.us/erddap/tabledap/cdmo_nerrs_bearcove | Bear Cove Water Quality |


```{code-cell}
cat['cdmo_nerrs_bearcove'].plot.data()
```

## homer-dolphin-surface-water-q
        

+++

            
|    | datasetID                     | featuretype   | griddap   | info_url                                                                           | institution                                               | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                                                 | tabledap                                                                     | title                                            |
|---:|:------------------------------|:--------------|:----------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|:-------------------------------------------------|
|  0 | homer-dolphin-surface-water-q | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/homer-dolphin-surface-water-q/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | point     |        59.602 |       -151.409 | 2011-11-29T01:00:00Z |        59.602 |       -151.409 | 2004-02-13T18:30:00Z | Timeseries data from 'Homer Dolphin Surface Water Quality (Historical)' (homer-dolphin-surface-water-q) | https://erddap.sensors.ioos.us/erddap/tabledap/homer-dolphin-surface-water-q | Homer Dolphin Surface Water Quality (Historical) |


```{code-cell}
cat['homer-dolphin-surface-water-q'].plot.data()
```

## nerrs_kach3wq
        

+++

            
|    | datasetID     | featuretype   | griddap   | info_url                                                           | institution                                               | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                              | tabledap                                                     | title                         |
|---:|:--------------|:--------------|:----------|:-------------------------------------------------------------------|:----------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:---------------------------------------------------------------------|:-------------------------------------------------------------|:------------------------------|
|  0 | nerrs_kach3wq | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kach3wq/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | point     |        59.602 |       -151.409 | 2023-04-05T18:30:00Z |        59.602 |       -151.409 | 2012-05-31T21:15:00Z | Timeseries data from 'Homer Surface 3 Water Quality' (nerrs_kach3wq) | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kach3wq | Homer Surface 3 Water Quality |


```{code-cell}
cat['nerrs_kach3wq'].plot.data()
```

## nerrs_kachdwq
        

+++

            
|    | datasetID     | featuretype   | griddap   | info_url                                                           | institution                                               | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                         | tabledap                                                     | title                                    |
|---:|:--------------|:--------------|:----------|:-------------------------------------------------------------------|:----------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------|
|  0 | nerrs_kachdwq | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kachdwq/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | point     |        59.602 |       -151.409 | 2023-04-26T23:15:00Z |        59.602 |       -151.409 | 2003-01-01T09:00:00Z | Timeseries data from 'Homer Dolphin Deep Water Quality (KCHA2)' (nerrs_kachdwq) | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kachdwq | Homer Dolphin Deep Water Quality (KCHA2) |


```{code-cell}
cat['nerrs_kachdwq'].plot.data()
```

## nerrs_kacsdwq
        

+++

            
|    | datasetID     | featuretype   | griddap   | info_url                                                           | institution                                               | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                    | tabledap                                                     | title                               |
|---:|:--------------|:--------------|:----------|:-------------------------------------------------------------------|:----------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:---------------------------------------------------------------------------|:-------------------------------------------------------------|:------------------------------------|
|  0 | nerrs_kacsdwq | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kacsdwq/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | point     |        59.441 |       -151.721 | 2023-04-04T17:45:00Z |        59.441 |       -151.721 | 2004-01-01T09:00:00Z | Timeseries data from 'Seldovia Deep Water Quality (SEQA2)' (nerrs_kacsdwq) | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kacsdwq | Seldovia Deep Water Quality (SEQA2) |


```{code-cell}
cat['nerrs_kacsdwq'].plot.data()
```

## nerrs_kacsswq
        

+++

            
|    | datasetID     | featuretype   | griddap   | info_url                                                           | institution                                               | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                               | tabledap                                                     | title                          |
|---:|:--------------|:--------------|:----------|:-------------------------------------------------------------------|:----------------------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:----------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------|
|  0 | nerrs_kacsswq | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kacsswq/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) | point     |        59.441 |       -151.721 | 2023-04-04T18:30:00Z |        59.441 |       -151.721 | 2004-01-01T09:00:00Z | Timeseries data from 'Seldovia Surface Water Quality' (nerrs_kacsswq) | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kacsswq | Seldovia Surface Water Quality |


```{code-cell}
cat['nerrs_kacsswq'].plot.data()
```
