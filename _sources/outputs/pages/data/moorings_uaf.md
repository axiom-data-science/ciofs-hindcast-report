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

# UAF Moorings: Kodiak Island and Peterson Bay, Cook Inlet

* Moorings from University of Alaska Fairbanks (UAF)
* moorings_uaf
* From 2013 to present, variable

Moorings from UAF




    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_uaf"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_uaf")("moorings_uaf")
    
```

## kodiak-burke-o-lator-kodiak-ak
        

+++

            
|    | datasetID                      | featuretype   | griddap   | info_url                                                                            | institution                                    | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                                  | tabledap                                                                      | title                            |
|---:|:-------------------------------|:--------------|:----------|:------------------------------------------------------------------------------------|:-----------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:-----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|:---------------------------------|
|  0 | kodiak-burke-o-lator-kodiak-ak | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/kodiak-burke-o-lator-kodiak-ak/index.csv | UAF Ocean Acidification Research Center (OARC) | point     |         57.79 |        -152.41 | 2023-04-26T23:15:00Z |         57.79 |        -152.41 | 2022-10-02T04:35:00Z | Timeseries data from 'Kodiak Burke-o-Lator, Kodiak, AK' (kodiak-burke-o-lator-kodiak-ak) | https://erddap.sensors.ioos.us/erddap/tabledap/kodiak-burke-o-lator-kodiak-ak | Kodiak Burke-o-Lator, Kodiak, AK |


```{code-cell}
cat['kodiak-burke-o-lator-kodiak-ak'].plot.data()
```

## peterson-bay-ak-gnss-r
        

+++

            
|    | datasetID              | featuretype   | griddap   | info_url                                                                    | institution                    | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                   | tabledap                                                              | title                     |
|---:|:-----------------------|:--------------|:----------|:----------------------------------------------------------------------------|:-------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------|
|  0 | peterson-bay-ak-gnss-r | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/peterson-bay-ak-gnss-r/index.csv | UAF Geophysical Institute (GI) | point     |       59.5727 |       -151.272 | 2023-03-28T23:33:00Z |       59.5727 |       -151.272 | 2017-01-01T00:22:00Z | Timeseries data from 'Peterson Bay, AK (GNSS-R)' (peterson-bay-ak-gnss-r) | https://erddap.sensors.ioos.us/erddap/tabledap/peterson-bay-ak-gnss-r | Peterson Bay, AK (GNSS-R) |


```{code-cell}
cat['peterson-bay-ak-gnss-r'].plot.data()
```

## uaf_ocean_acidification_resea_ko
        

+++

            
|    | datasetID                        | featuretype   | griddap   | info_url                                                                              | institution                                    | maptype   |   maxLatitude |   maxLongitude | maxTime              |   minLatitude |   minLongitude | minTime              | summary                                                                                                 | tabledap                                                                        | title                                         |
|---:|:---------------------------------|:--------------|:----------|:--------------------------------------------------------------------------------------|:-----------------------------------------------|:----------|--------------:|---------------:|:---------------------|--------------:|---------------:|:---------------------|:--------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:----------------------------------------------|
|  0 | uaf_ocean_acidification_resea_ko | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/uaf_ocean_acidification_resea_ko/index.csv | UAF Ocean Acidification Research Center (OARC) | point     |          57.7 |        -152.31 | 2016-04-18T15:17:00Z |          57.7 |        -152.31 | 2013-03-30T00:17:00Z | Timeseries data from 'Kodiak Ocean Acidification Mooring (Historic)' (uaf_ocean_acidification_resea_ko) | https://erddap.sensors.ioos.us/erddap/tabledap/uaf_ocean_acidification_resea_ko | Kodiak Ocean Acidification Mooring (Historic) |


```{code-cell}
cat['uaf_ocean_acidification_resea_ko'].plot.data()
```