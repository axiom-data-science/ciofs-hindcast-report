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

# Moorings (KBNERR): Kachemak Bay, Homer stations

* Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* moorings_kbnerr_homer
* From 2003 to present day, variable

Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
* nerrs_kachdwq :: kachdwq
* homer-dolphin-surface-water-q :: kachswq
* nerrs_kach3wq :: kach3wq
    
More information: https://accs.uaa.alaska.edu/kbnerr/


These are accessed through AOOS portal/ERDDAP server.

<details><summary>Dataset metadata:</summary>

|    | Dataset                       | datasetID                     | featuretype   | griddap   | info_url                                                                           | institution                                               |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                                                 | tabledap                                                                     | title                                            | urlpath                                                                      |
|---:|:------------------------------|:------------------------------|:--------------|:----------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:--------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|:-------------------------------------------------|:-----------------------------------------------------------------------------|
|  0 | homer-dolphin-surface-water-q | homer-dolphin-surface-water-q | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/homer-dolphin-surface-water-q/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) |        59.602 |       -151.409 | 2011-11-29 01:00:00+00:00 |        59.602 |       -151.409 | 2004-02-13 18:30:00+00:00 | Timeseries data from 'Homer Dolphin Surface Water Quality (Historical)' (homer-dolphin-surface-water-q) | https://erddap.sensors.ioos.us/erddap/tabledap/homer-dolphin-surface-water-q | Homer Dolphin Surface Water Quality (Historical) | https://erddap.sensors.ioos.us/erddap/tabledap/homer-dolphin-surface-water-q |
|  1 | nerrs_kach3wq                 | nerrs_kach3wq                 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kach3wq/index.csv                 | Kachemak Bay National Estuarine Research Reserve (KBNERR) |        59.602 |       -151.409 | 2023-04-05 18:30:00+00:00 |        59.602 |       -151.409 | 2012-05-31 21:15:00+00:00 | Timeseries data from 'Homer Surface 3 Water Quality' (nerrs_kach3wq)                                    | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kach3wq                 | Homer Surface 3 Water Quality                    | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kach3wq                 |
|  2 | nerrs_kachdwq                 | nerrs_kachdwq                 | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kachdwq/index.csv                 | Kachemak Bay National Estuarine Research Reserve (KBNERR) |        59.602 |       -151.409 | 2023-05-14 20:15:00+00:00 |        59.602 |       -151.409 | 2003-01-01 09:00:00+00:00 | Timeseries data from 'Homer Dolphin Deep Water Quality (KCHA2)' (nerrs_kachdwq)                         | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kachdwq                 | Homer Dolphin Deep Water Quality (KCHA2)         | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kachdwq                 |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_kbnerr_homer"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_homer")("moorings_kbnerr_homer")
    
```

## homer-dolphin-surface-water-q
        

```{code-cell}
:tags: [full-width]

(cat['homer-dolphin-surface-water-q'].plot.data()).cols(1)
```

## nerrs_kach3wq
        

```{code-cell}
:tags: [full-width]

(cat['nerrs_kach3wq'].plot.data()).cols(1)
```

## nerrs_kachdwq
        

```{code-cell}
:tags: [full-width]

(cat['nerrs_kachdwq'].plot.data()).cols(1)
```
