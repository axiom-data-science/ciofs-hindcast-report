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

# Historical KBNERR Moorings: Kachemak Bay

* Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* moorings_kbnerr_historical
* From 2001 to 2003, variable

Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
More information: https://accs.uaa.alaska.edu/kbnerr/


These are accessed from Research Workspace.

Dataset metadata:
|    | Dataset     | featuretype   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             |
|---:|:------------|:--------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|
|  0 | kacbcwq2002 | timeSeries    |       59.7057 |       -151.109 | 2002-09-11 11:00:00 |       59.7057 |       -151.109 | 2002-06-18 11:30:00 |
|  1 | kacbcwq2003 | timeSeries    |       59.7057 |       -151.109 | 2003-09-24 17:30:00 |       59.7057 |       -151.109 | 2003-04-15 18:00:00 |
|  2 | kacdlwq2002 | timeSeries    |       59.6023 |       -151.41  | 2002-12-31 23:30:00 |       59.6023 |       -151.41  | 2002-10-24 10:00:00 |
|  3 | kachowq2001 | timeSeries    |       59.6023 |       -151.41  | 2001-12-31 23:45:00 |       59.6023 |       -151.41  | 2001-07-12 07:45:00 |
|  4 | kachowq2002 | timeSeries    |       59.6023 |       -151.41  | 2002-11-20 12:30:00 |       59.6023 |       -151.41  | 2002-01-01 00:00:00 |
|  5 | kacpgwq2002 | timeSeries    |       59.3705 |       -151.896 | 2002-10-02 12:30:00 |       59.3705 |       -151.896 | 2002-06-21 10:00:00 |
|  6 | kacpgwq2003 | timeSeries    |       59.3705 |       -151.896 | 2003-09-24 15:30:00 |       59.3705 |       -151.896 | 2003-04-29 12:00:00 |
|  7 | kacsewq2001 | timeSeries    |       59.441  |       -151.721 | 2001-12-04 11:00:00 |       59.441  |       -151.721 | 2001-08-17 15:15:00 |
|  8 | kacsewq2002 | timeSeries    |       59.441  |       -151.721 | 2002-12-31 23:30:00 |       59.441  |       -151.721 | 2002-01-11 17:00:00 |
|  9 | kacsewq2003 | timeSeries    |       59.441  |       -151.721 | 2003-12-31 23:30:00 |       59.441  |       -151.721 | 2003-01-01 00:00:00 |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_kbnerr_historical"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_historical")("moorings_kbnerr_historical")
    
```

## kacbcwq2002
        

```{code-cell}
cat['kacbcwq2002'].plot.data()
```

## kacbcwq2003
        

```{code-cell}
cat['kacbcwq2003'].plot.data()
```

## kacdlwq2002
        

```{code-cell}
cat['kacdlwq2002'].plot.data()
```

## kachowq2001
        

```{code-cell}
cat['kachowq2001'].plot.data()
```

## kachowq2002
        

```{code-cell}
cat['kachowq2002'].plot.data()
```

## kacpgwq2002
        

```{code-cell}
cat['kacpgwq2002'].plot.data()
```

## kacpgwq2003
        

```{code-cell}
cat['kacpgwq2003'].plot.data()
```

## kacsewq2001
        

```{code-cell}
cat['kacsewq2001'].plot.data()
```

## kacsewq2002
        

```{code-cell}
cat['kacsewq2002'].plot.data()
```

## kacsewq2003
        

```{code-cell}
cat['kacsewq2003'].plot.data()
```
