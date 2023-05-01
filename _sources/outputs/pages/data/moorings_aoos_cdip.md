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

# CDIP Buoys: Lower Cook Inlet, Kodiak, Central Cook Inlet

* Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP)
* moorings_aoos_cdip
* From , variable

Moorings from AOOS/CDIP




Dataset metadata:
|    | Dataset                | datasetID              | featuretype   | griddap   | info_url                                                                    | institution                          |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                             | tabledap                                                              | title                                                |
|---:|:-----------------------|:-----------------------|:--------------|:----------|:----------------------------------------------------------------------------|:-------------------------------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------------------------------|
|  0 | aoos_204               | aoos_204               | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/aoos_204/index.csv               | Alaska Ocean Observing System (AOOS) |       59.5973 |       -151.829 | 2023-05-01 13:45:00+00:00 |       59.5973 |       -151.829 | 2013-07-21 19:22:27+00:00 | Timeseries data from 'Lower Cook Inlet, AK, CDIP Wave and Current Buoy 204' (aoos_204)              | https://erddap.sensors.ioos.us/erddap/tabledap/aoos_204               | Lower Cook Inlet, AK, CDIP Wave and Current Buoy 204 |
|  1 | central-cook-inlet-175 | central-cook-inlet-175 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/central-cook-inlet-175/index.csv | Alaska Ocean Observing System (AOOS) |       59.7335 |       -152.005 | 2013-01-03 06:54:07+00:00 |       59.7335 |       -152.005 | 2011-05-09 23:00:27+00:00 | Timeseries data from 'Central Cook Inlet, AK, Historic CDIP Wave Buoy 175' (central-cook-inlet-175) | https://erddap.sensors.ioos.us/erddap/tabledap/central-cook-inlet-175 | Central Cook Inlet, AK, Historic CDIP Wave Buoy 175  |
|  2 | edu_ucsd_cdip_236      | edu_ucsd_cdip_236      | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/edu_ucsd_cdip_236/index.csv      | Alaska Ocean Observing System (AOOS) |       57.4795 |       -151.695 | 2021-09-25 17:58:20+00:00 |       57.4795 |       -151.695 | 2017-09-28 22:00:00+00:00 | Timeseries data from 'Kodiak, AK, CDIP Wave Buoy 236' (edu_ucsd_cdip_236)                           | https://erddap.sensors.ioos.us/erddap/tabledap/edu_ucsd_cdip_236      | Kodiak, AK, CDIP Wave Buoy 236                       |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_aoos_cdip"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_aoos_cdip")("moorings_aoos_cdip")
    
```

## aoos_204
        

```{code-cell}
cat['aoos_204'].plot.data()
```

## central-cook-inlet-175
        

```{code-cell}
cat['central-cook-inlet-175'].plot.data()
```

## edu_ucsd_cdip_236
        

```{code-cell}
cat['edu_ucsd_cdip_236'].plot.data()
```
