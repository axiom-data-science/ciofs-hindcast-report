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

# CDIP Buoys: Lower Cook Inlet, Kodiak, Central Cook Inlet

* Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP)
* moorings_aoos_cdip
* From , variable

Moorings from AOOS/CDIP




    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_aoos_cdip"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_aoos_cdip")("moorings_aoos_cdip")
    
```

## aoos_204
        

+++

            
|    | datasetID   | featuretype   | griddap   | info_url                                                      | institution                          | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                                | tabledap                                                | title                                                |
|---:|:------------|:--------------|:----------|:--------------------------------------------------------------|:-------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:---------------------------------------------------------------------------------------|:--------------------------------------------------------|:-----------------------------------------------------|
|  0 | aoos_204    | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/aoos_204/index.csv | Alaska Ocean Observing System (AOOS) | point     |       59.5973 |       -151.829 | 2023-04-27T00:45:00Z |       59.5973 |       -151.829 | 2013-07-21T19:22:27Z | Timeseries data from 'Lower Cook Inlet, AK, CDIP Wave and Current Buoy 204' (aoos_204) | https://erddap.sensors.ioos.us/erddap/tabledap/aoos_204 | Lower Cook Inlet, AK, CDIP Wave and Current Buoy 204 |


```{code-cell}
cat['aoos_204'].plot.data()
```

## central-cook-inlet-175
        

+++

            
|    | datasetID              | featuretype   | griddap   | info_url                                                                    | institution                          | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                                             | tabledap                                                              | title                                               |
|---:|:-----------------------|:--------------|:----------|:----------------------------------------------------------------------------|:-------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:----------------------------------------------------|
|  0 | central-cook-inlet-175 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/central-cook-inlet-175/index.csv | Alaska Ocean Observing System (AOOS) | point     |       59.7335 |       -152.005 | 2013-01-03T06:54:07Z |       59.7335 |       -152.005 | 2011-05-09T23:00:27Z | Timeseries data from 'Central Cook Inlet, AK, Historic CDIP Wave Buoy 175' (central-cook-inlet-175) | https://erddap.sensors.ioos.us/erddap/tabledap/central-cook-inlet-175 | Central Cook Inlet, AK, Historic CDIP Wave Buoy 175 |


```{code-cell}
cat['central-cook-inlet-175'].plot.data()
```

## edu_ucsd_cdip_236
        

+++

            
|    | datasetID         | featuretype   | griddap   | info_url                                                               | institution                          | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                   | tabledap                                                         | title                          |
|---:|:------------------|:--------------|:----------|:-----------------------------------------------------------------------|:-------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------------|:-----------------------------------------------------------------|:-------------------------------|
|  0 | edu_ucsd_cdip_236 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/edu_ucsd_cdip_236/index.csv | Alaska Ocean Observing System (AOOS) | point     |       57.4795 |       -151.695 | 2021-09-25T17:58:20Z |       57.4795 |       -151.695 | 2017-09-28T22:00:00Z | Timeseries data from 'Kodiak, AK, CDIP Wave Buoy 236' (edu_ucsd_cdip_236) | https://erddap.sensors.ioos.us/erddap/tabledap/edu_ucsd_cdip_236 | Kodiak, AK, CDIP Wave Buoy 236 |


```{code-cell}
cat['edu_ucsd_cdip_236'].plot.data()
```
