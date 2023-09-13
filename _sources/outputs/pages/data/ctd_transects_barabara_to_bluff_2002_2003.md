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
import holoviews as hv
from holoviews import opts
```

(page:ctd_transects_barabara_to_bluff_2002_2003)=
# CTD transects: Barabara to Bluff

* Barabara to Bluff 2002-2003
* ctd_transects_barabara_to_bluff_2002_2003
* 2002-2003

Repeat CTD transect from Barabara to Bluff Point in Cook Inlet from 2002 tp 2003.




```{dropdown} Dataset metadata

|    | Dataset   | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                   |
|---:|:----------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------|
|  0 | Cruise 1  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-07-23 10:34:00 |       59.49   |       -151.657 | 2002-07-23 08:28:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  1 | Cruise 10 | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-05-19 14:46:00 |       59.49   |       -151.657 | 2003-05-19 13:17:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  2 | Cruise 11 | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-06-21 13:02:00 |       59.49   |       -151.657 | 2003-06-21 11:20:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  3 | Cruise 2  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-09-07 13:16:00 |       59.49   |       -151.657 | 2002-09-07 11:05:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  4 | Cruise 3  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-09-25 13:56:00 |       59.49   |       -151.657 | 2002-09-25 11:55:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  5 | Cruise 4  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-11-11 16:31:00 |       59.49   |       -151.657 | 2002-11-11 14:45:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  6 | Cruise 5  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2002-12-11 18:55:00 |       59.49   |       -151.657 | 2002-12-11 16:39:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  7 | Cruise 6  | trajectoryProfile | ['temp', 'salt'] |       59.6233 |        -151.65 | 2003-01-31 17:27:00 |       59.49   |       -151.656 | 2003-01-31 15:56:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  8 | Cruise 7  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-02-18 18:19:00 |       59.49   |       -151.657 | 2003-02-18 16:50:00 | https://researchworkspace.com/files/42396691/barabara.csv |
|  9 | Cruise 8  | trajectoryProfile | ['temp', 'salt'] |       59.6317 |        -151.65 | 2003-03-31 17:32:00 |       59.4983 |       -151.656 | 2003-03-31 15:27:00 | https://researchworkspace.com/files/42396691/barabara.csv |
| 10 | Cruise 9  | trajectoryProfile | ['temp', 'salt'] |       59.64   |        -151.65 | 2003-04-17 14:15:00 |       59.49   |       -151.657 | 2003-04-17 12:35:00 | https://researchworkspace.com/files/42396691/barabara.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_transects_barabara_to_bluff_2002_2003"))
```

## Map of CTD Transects
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_barabara_to_bluff_2002_2003")("ctd_transects_barabara_to_bluff_2002_2003")
```

## Cruise 1
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 1'].plot.salt() + cat['Cruise 1'].plot.temp()
```

## Cruise 10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 10'].plot.salt() + cat['Cruise 10'].plot.temp()
```

## Cruise 11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 11'].plot.salt() + cat['Cruise 11'].plot.temp()
```

## Cruise 2
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 2'].plot.salt() + cat['Cruise 2'].plot.temp()
```

## Cruise 3
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 3'].plot.salt() + cat['Cruise 3'].plot.temp()
```

## Cruise 4
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 4'].plot.salt() + cat['Cruise 4'].plot.temp()
```

## Cruise 5
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 5'].plot.salt() + cat['Cruise 5'].plot.temp()
```

## Cruise 6
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 6'].plot.salt() + cat['Cruise 6'].plot.temp()
```

## Cruise 7
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 7'].plot.salt() + cat['Cruise 7'].plot.temp()
```

## Cruise 8
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 8'].plot.salt() + cat['Cruise 8'].plot.temp()
```

## Cruise 9
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise 9'].plot.salt() + cat['Cruise 9'].plot.temp()
```
