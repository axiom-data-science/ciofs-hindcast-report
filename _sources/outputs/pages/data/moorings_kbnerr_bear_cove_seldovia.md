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

# Moorings (KBNERR): Kachemak Bay: Bear Cove, Seldovia

* Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* moorings_kbnerr_bear_cove_seldovia
* From 2004 to present day, variable

Moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
Station mappings from AOOS/ERDDAP to KBNERR station list:
* nerrs_kacsdwq :: kacsdwq
* nerrs_kacsswq :: kacsswq

* cdmo_nerrs_bearcove :: This is a different station than kacbcwq, which was active 2002-2003 while this is in 2015. They are also in different locations.
    
More information: https://accs.uaa.alaska.edu/kbnerr/


These are accessed through AOOS portal/ERDDAP server.

<details><summary>Dataset metadata:</summary>

|    | Dataset             | datasetID           | featuretype   | griddap   | info_url                                                                 | institution                                               |   maxLatitude |   maxLongitude | maxTime                   |   minLatitude |   minLongitude | minTime                   | summary                                                                    | tabledap                                                           | title                               | urlpath                                                            |
|---:|:--------------------|:--------------------|:--------------|:----------|:-------------------------------------------------------------------------|:----------------------------------------------------------|--------------:|---------------:|:--------------------------|--------------:|---------------:|:--------------------------|:---------------------------------------------------------------------------|:-------------------------------------------------------------------|:------------------------------------|:-------------------------------------------------------------------|
|  0 | cdmo_nerrs_bearcove | cdmo_nerrs_bearcove | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/cdmo_nerrs_bearcove/index.csv | Kachemak Bay National Estuarine Research Reserve (KBNERR) |       59.7262 |       -151.049 | 2015-11-20 17:15:00+00:00 |       59.7262 |       -151.049 | 2015-05-05 14:00:00+00:00 | Timeseries data from 'Bear Cove Water Quality' (cdmo_nerrs_bearcove)       | https://erddap.sensors.ioos.us/erddap/tabledap/cdmo_nerrs_bearcove | Bear Cove Water Quality             | https://erddap.sensors.ioos.us/erddap/tabledap/cdmo_nerrs_bearcove |
|  1 | nerrs_kacsdwq       | nerrs_kacsdwq       | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kacsdwq/index.csv       | Kachemak Bay National Estuarine Research Reserve (KBNERR) |       59.441  |       -151.721 | 2023-05-12 19:00:00+00:00 |       59.441  |       -151.721 | 2004-01-01 09:00:00+00:00 | Timeseries data from 'Seldovia Deep Water Quality (SEQA2)' (nerrs_kacsdwq) | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kacsdwq       | Seldovia Deep Water Quality (SEQA2) | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kacsdwq       |
|  2 | nerrs_kacsswq       | nerrs_kacsswq       | timeSeries    |           | https://erddap.sensors.ioos.us/erddap/info/nerrs_kacsswq/index.csv       | Kachemak Bay National Estuarine Research Reserve (KBNERR) |       59.441  |       -151.721 | 2023-05-12 19:00:00+00:00 |       59.441  |       -151.721 | 2004-01-01 09:00:00+00:00 | Timeseries data from 'Seldovia Surface Water Quality' (nerrs_kacsswq)      | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kacsswq       | Seldovia Surface Water Quality      | https://erddap.sensors.ioos.us/erddap/tabledap/nerrs_kacsswq       |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_kbnerr_bear_cove_seldovia"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_bear_cove_seldovia")("moorings_kbnerr_bear_cove_seldovia")
    
```

## cdmo_nerrs_bearcove
        

```{code-cell}
:tags: [full-width]

(cat['cdmo_nerrs_bearcove'].plot.data()).cols(1)
```

## nerrs_kacsdwq
        

```{code-cell}
:tags: [full-width]

(cat['nerrs_kacsdwq'].plot.data()).cols(1)
```

## nerrs_kacsswq
        

```{code-cell}
:tags: [full-width]

(cat['nerrs_kacsswq'].plot.data()).cols(1)
```
