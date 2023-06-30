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

(page:moorings_uaf)=
# Moorings (UAF): Kodiak Island, Peterson Bay

* Moorings from University of Alaska Fairbanks (UAF)
* moorings_uaf
* From 2013 to present, variable

Moorings from UAF




```{dropdown} Dataset metadata

|    | Dataset                          | datasetID                        | featuretype   | griddap   | info_url                                                                              | institution                                    | key_variables    |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                                 | tabledap                                                                        | title                                         | urlpath                                                                         |
|---:|:---------------------------------|:---------------------------------|:--------------|:----------|:--------------------------------------------------------------------------------------|:-----------------------------------------------|:-----------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:--------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:----------------------------------------------|:--------------------------------------------------------------------------------|
|  0 | kodiak-burke-o-lator-kodiak-ak   | kodiak-burke-o-lator-kodiak-ak   | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/kodiak-burke-o-lator-kodiak-ak/index.csv   | UAF Ocean Acidification Research Center (OARC) | ['temp', 'salt'] |       57.79   |       -152.41  | 2023-06-07 13:15:00+00:00 |       57.79   |       -152.41  | 2022-10-02 04:35:00+00:00 | Timeseries data from 'Kodiak Burke-o-Lator, Kodiak, AK' (kodiak-burke-o-lator-kodiak-ak)                | https://erddap.sensors.ioos.us/erddap/tabledap/kodiak-burke-o-lator-kodiak-ak   | Kodiak Burke-o-Lator, Kodiak, AK              | https://erddap.sensors.ioos.us/erddap/tabledap/kodiak-burke-o-lator-kodiak-ak   |
|  1 | peterson-bay-ak-gnss-r           | peterson-bay-ak-gnss-r           | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/peterson-bay-ak-gnss-r/index.csv           | UAF Geophysical Institute (GI)                 | ['ssh']          |       59.5727 |       -151.272 | 2023-06-05 23:45:00+00:00 |       59.5727 |       -151.272 | 2017-01-01 00:22:00+00:00 | Timeseries data from 'Peterson Bay, AK (GNSS-R)' (peterson-bay-ak-gnss-r)                               | https://erddap.sensors.ioos.us/erddap/tabledap/peterson-bay-ak-gnss-r           | Peterson Bay, AK (GNSS-R)                     | https://erddap.sensors.ioos.us/erddap/tabledap/peterson-bay-ak-gnss-r           |
|  2 | uaf_ocean_acidification_resea_ko | uaf_ocean_acidification_resea_ko | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/uaf_ocean_acidification_resea_ko/index.csv | UAF Ocean Acidification Research Center (OARC) | ['temp', 'salt'] |       57.7    |       -152.31  | 2016-04-18 15:17:00+00:00 |       57.7    |       -152.31  | 2013-03-30 00:17:00+00:00 | Timeseries data from 'Kodiak Ocean Acidification Mooring (Historic)' (uaf_ocean_acidification_resea_ko) | https://erddap.sensors.ioos.us/erddap/tabledap/uaf_ocean_acidification_resea_ko | Kodiak Ocean Acidification Mooring (Historic) | https://erddap.sensors.ioos.us/erddap/tabledap/uaf_ocean_acidification_resea_ko |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("moorings_uaf"))
```

## Map of Moorings
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_uaf")("moorings_uaf")
```

## kodiak-burke-o-lator-kodiak-ak
        

```{code-cell}
:tags: [remove-input]

(cat['kodiak-burke-o-lator-kodiak-ak'].plot.data()).cols(1)
```

## peterson-bay-ak-gnss-r
        

```{code-cell}
:tags: [remove-input]

cat['peterson-bay-ak-gnss-r'].plot.data()
```

## uaf_ocean_acidification_resea_ko
        

```{code-cell}
:tags: [remove-input]

(cat['uaf_ocean_acidification_resea_ko'].plot.data()).cols(1)
```
