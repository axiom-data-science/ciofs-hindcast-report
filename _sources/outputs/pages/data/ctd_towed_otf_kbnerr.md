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

# OTF KBNERR: Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths

* CTD Towed 2003 - OTF KBNERR
* ctd_towed_otf_kbnerr
* July 2003, 5min sampling frequency

Towed CTD Profiles.


Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_otf_kbnerr"))
```

## Map of Towed CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_otf_kbnerr")("ctd_towed_otf_kbnerr")
    
```

## mic071303
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8603 |       -152.314 | 2003-07-13T13:30:00.000000000 |       59.8288 |       -152.416 | 2003-07-13T06:50:00.000000000 |


```{code-cell}
cat['mic071303'].plot.map() + cat['mic071303'].plot.salt() + cat['mic071303'].plot.temp()
```

## mic071903
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8799 |       -152.154 | 2003-07-19T11:15:00.000000000 |       59.8237 |       -152.403 | 2003-07-19T06:40:00.000000000 |


```{code-cell}
cat['mic071903'].plot.map() + cat['mic071903'].plot.salt() + cat['mic071903'].plot.temp()
```

## mic072003
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8718 |       -152.181 | 2003-07-20T15:55:00.000000000 |       59.8176 |        -152.45 | 2003-07-20T11:00:00.000000000 |


```{code-cell}
cat['mic072003'].plot.map() + cat['mic072003'].plot.salt() + cat['mic072003'].plot.temp()
```

## mic072103
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8729 |       -152.147 | 2003-07-21T11:30:00.000000000 |       59.8246 |       -152.456 | 2003-07-21T06:25:00.000000000 |


```{code-cell}
cat['mic072103'].plot.map() + cat['mic072103'].plot.salt() + cat['mic072103'].plot.temp()
```

## mic072203
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8739 |       -152.153 | 2003-07-22T15:50:00.000000000 |       59.8371 |       -152.441 | 2003-07-22T11:15:00.000000000 |


```{code-cell}
cat['mic072203'].plot.map() + cat['mic072203'].plot.salt() + cat['mic072203'].plot.temp()
```

## mic072403
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8741 |       -152.164 | 2003-07-24T15:55:00.000000000 |       59.8376 |       -152.445 | 2003-07-24T11:30:00.000000000 |


```{code-cell}
cat['mic072403'].plot.map() + cat['mic072403'].plot.salt() + cat['mic072403'].plot.temp()
```

## mic072503
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8589 |       -152.156 | 2003-07-25T12:10:00.000000000 |       59.8267 |       -152.464 | 2003-07-25T06:55:00.000000000 |


```{code-cell}
cat['mic072503'].plot.map() + cat['mic072503'].plot.salt() + cat['mic072503'].plot.temp()
```

## mic072603
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8736 |       -152.158 | 2003-07-26T16:15:00.000000000 |       59.8275 |       -152.434 | 2003-07-26T11:05:00.000000000 |


```{code-cell}
cat['mic072603'].plot.map() + cat['mic072603'].plot.salt() + cat['mic072603'].plot.temp()
```

## mic072803_65-8
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8948 |       -152.303 | 2003-07-28T17:05:00.000000000 |       59.8644 |       -152.439 | 2003-07-28T14:50:00.000000000 |


```{code-cell}
cat['mic072803_65-8'].plot.map() + cat['mic072803_65-8'].plot.salt() + cat['mic072803_65-8'].plot.temp()
```

## mic072903
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8801 |       -152.154 | 2003-07-29T10:10:00.000000000 |       59.7911 |       -152.419 | 2003-07-29T05:35:00.000000000 |


```{code-cell}
cat['mic072903'].plot.map() + cat['mic072903'].plot.salt() + cat['mic072903'].plot.temp()
```

## mic073003
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8731 |       -152.182 | 2003-07-30T14:10:00.000000000 |       59.7915 |       -152.435 | 2003-07-30T10:05:00.000000000 |


```{code-cell}
cat['mic073003'].plot.map() + cat['mic073003'].plot.salt() + cat['mic073003'].plot.temp()
```
