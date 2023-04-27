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

# Historical KBNERR Moorings: Kachemak Bay

* Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
* moorings_kbnerr_historical
* From 2001 to 2003, variable

Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
More information: https://accs.uaa.alaska.edu/kbnerr/


These are accessed from Research Workspace.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("moorings_kbnerr_historical"))
```

## Map of Moorings
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_historical")("moorings_kbnerr_historical")
    
```

## kacbcwq2002
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.7057 |       -151.109 | 2002-09-11T11:00:00.000000000 |       59.7057 |       -151.109 | 2002-06-18T11:30:00.000000000 |


```{code-cell}
cat['kacbcwq2002'].plot.data()
```

## kacbcwq2003
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.7057 |       -151.109 | 2003-09-24T17:30:00.000000000 |       59.7057 |       -151.109 | 2003-04-15T18:00:00.000000000 |


```{code-cell}
cat['kacbcwq2003'].plot.data()
```

## kacdlwq2002
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.6023 |        -151.41 | 2002-12-31T23:30:00.000000000 |       59.6023 |        -151.41 | 2002-10-24T10:00:00.000000000 |


```{code-cell}
cat['kacdlwq2002'].plot.data()
```

## kachowq2001
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.6023 |        -151.41 | 2001-12-31T23:45:00.000000000 |       59.6023 |        -151.41 | 2001-07-12T07:45:00.000000000 |


```{code-cell}
cat['kachowq2001'].plot.data()
```

## kachowq2002
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.6023 |        -151.41 | 2002-11-20T12:30:00.000000000 |       59.6023 |        -151.41 | 2002-01-01T00:00:00.000000000 |


```{code-cell}
cat['kachowq2002'].plot.data()
```

## kacpgwq2002
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.3705 |       -151.896 | 2002-10-02T12:30:00.000000000 |       59.3705 |       -151.896 | 2002-06-21T10:00:00.000000000 |


```{code-cell}
cat['kacpgwq2002'].plot.data()
```

## kacpgwq2003
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |       59.3705 |       -151.896 | 2003-09-24T15:30:00.000000000 |       59.3705 |       -151.896 | 2003-04-29T12:00:00.000000000 |


```{code-cell}
cat['kacpgwq2003'].plot.data()
```

## kacsewq2001
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |        59.441 |       -151.721 | 2001-12-04T11:00:00.000000000 |        59.441 |       -151.721 | 2001-08-17T15:15:00.000000000 |


```{code-cell}
cat['kacsewq2001'].plot.data()
```

## kacsewq2002
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |        59.441 |       -151.721 | 2002-12-31T23:30:00.000000000 |        59.441 |       -151.721 | 2002-01-11T17:00:00.000000000 |


```{code-cell}
cat['kacsewq2002'].plot.data()
```

## kacsewq2003
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | timeSeries    | point     |        59.441 |       -151.721 | 2003-12-31T23:30:00.000000000 |        59.441 |       -151.721 | 2003-01-01T00:00:00.000000000 |


```{code-cell}
cat['kacsewq2003'].plot.data()
```
