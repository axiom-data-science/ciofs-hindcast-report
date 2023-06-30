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

(page:moorings_nps)=
# Moorings (NPS): Chinitna Bay, Aguchik Island

* Moorings from National Parks Service (NPS)
* moorings_nps
* From 2018 to 2019, variable

Moorings from NPS




```{dropdown} Dataset metadata

|    | Dataset                          | datasetID                        | featuretype   | griddap   | info_url                                                                              | institution                 | key_variables   |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                              | tabledap                                                                        | title                                      | urlpath                                                                         |
|---:|:---------------------------------|:---------------------------------|:--------------|:----------|:--------------------------------------------------------------------------------------|:----------------------------|:----------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:-----------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:-------------------------------------------|:--------------------------------------------------------------------------------|
|  0 | aguchik-island-ak-tide-station-9 | aguchik-island-ak-tide-station-9 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/aguchik-island-ak-tide-station-9/index.csv | National Park Service (NPS) | ['ssh']         |       58.2946 |       -154.266 | 2019-09-28 17:30:00+00:00 |       58.2946 |       -154.266 | 2018-09-11 18:36:00+00:00 | Timeseries data from 'Aguchik Island, AK, Tide Station (9456901)' (aguchik-island-ak-tide-station-9) | https://erddap.sensors.ioos.us/erddap/tabledap/aguchik-island-ak-tide-station-9 | Aguchik Island, AK, Tide Station (9456901) | https://erddap.sensors.ioos.us/erddap/tabledap/aguchik-island-ak-tide-station-9 |
|  1 | chinitna-bay-ak-tide-station-945 | chinitna-bay-ak-tide-station-945 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/chinitna-bay-ak-tide-station-945/index.csv | National Park Service (NPS) | ['ssh']         |       59.8421 |       -152.993 | 2018-10-26 08:24:00+00:00 |       59.8421 |       -152.993 | 2018-06-14 20:00:00+00:00 | Timeseries data from 'Chinitna Bay, AK, Tide Station (9456357)' (chinitna-bay-ak-tide-station-945)   | https://erddap.sensors.ioos.us/erddap/tabledap/chinitna-bay-ak-tide-station-945 | Chinitna Bay, AK, Tide Station (9456357)   | https://erddap.sensors.ioos.us/erddap/tabledap/chinitna-bay-ak-tide-station-945 |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("moorings_nps"))
```

## Map of Moorings
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_nps")("moorings_nps")
```

## aguchik-island-ak-tide-station-9
        

```{code-cell}
:tags: [remove-input]

cat['aguchik-island-ak-tide-station-9'].plot.data()
```

## chinitna-bay-ak-tide-station-945
        

```{code-cell}
:tags: [remove-input]

cat['chinitna-bay-ak-tide-station-945'].plot.data()
```
