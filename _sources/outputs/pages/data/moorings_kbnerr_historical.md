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

# Moorings (KBNERR): Historical, Kachemak Bay

* Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* moorings_kbnerr_historical
* From 2001 to 2003, variable

Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
More information: https://accs.uaa.alaska.edu/kbnerr/


These are accessed from Research Workspace.

<details><summary>Dataset metadata:</summary>

|    | Dataset   | featuretype   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                            |
|---:|:----------|:--------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------------|
|  0 | kacbcwq   | timeSeries    |       59.7057 |       -151.109 | 2003-09-24 17:30:00 |       59.7057 |       -151.109 | 2002-06-18 11:30:00 | https://researchworkspace.com/files/42202441/kacbcwq_subsetted.csv |
|  1 | kacdlwq   | timeSeries    |       59.6023 |       -151.41  | 2002-12-31 23:30:00 |       59.6023 |       -151.41  | 2002-10-24 10:00:00 | https://researchworkspace.com/files/42202443/kacdlwq_subsetted.csv |
|  2 | kachowq   | timeSeries    |       59.6023 |       -151.41  | 2002-11-20 12:30:00 |       59.6023 |       -151.41  | 2001-07-12 07:45:00 | https://researchworkspace.com/files/42202445/kachowq_subsetted.csv |
|  3 | kacpgwq   | timeSeries    |       59.3705 |       -151.896 | 2003-09-24 15:30:00 |       59.3705 |       -151.896 | 2002-06-21 10:00:00 | https://researchworkspace.com/files/42202447/kacpgwq_subsetted.csv |
|  4 | kacsewq   | timeSeries    |       59.441  |       -151.721 | 2003-12-31 23:30:00 |       59.441  |       -151.721 | 2001-08-17 15:15:00 | https://researchworkspace.com/files/42202449/kacsewq_subsetted.csv |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_kbnerr_historical"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_historical")("moorings_kbnerr_historical")
    
```

## kacbcwq
        

```{code-cell}
:tags: [full-width]

(cat['kacbcwq'].plot.data()).cols(1)
```

## kacdlwq
        

```{code-cell}
:tags: [full-width]

(cat['kacdlwq'].plot.data()).cols(1)
```

## kachowq
        

```{code-cell}
:tags: [full-width]

(cat['kachowq'].plot.data()).cols(1)
```

## kacpgwq
        

```{code-cell}
:tags: [full-width]

(cat['kacpgwq'].plot.data()).cols(1)
```

## kacsewq
        

```{code-cell}
:tags: [full-width]

(cat['kacsewq'].plot.data()).cols(1)
```
