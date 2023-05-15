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

# Towed CTD (OTF KBNERR): central Cook Inlet

* CTD Towed 2003 - OTF KBNERR
* ctd_towed_otf_kbnerr
* July 2003, 5min sampling frequency

Towed CTD Profiles.

Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths


Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency.

<details><summary>Dataset metadata:</summary>

|    | Dataset                   | featuretype       |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                    |
|---:|:--------------------------|:------------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:---------------------------------------------------------------------------|
|  0 | mic071303_subsampled      | trajectoryProfile |       59.8603 |       -152.314 | 2003-07-13 13:30:00 |       59.8288 |       -152.416 | 2003-07-13 06:50:00 | https://researchworkspace.com/files/42202371/mic071303_subsampled.csv      |
|  1 | mic071903_subsampled      | trajectoryProfile |       59.8799 |       -152.154 | 2003-07-19 11:15:00 |       59.8237 |       -152.403 | 2003-07-19 06:40:00 | https://researchworkspace.com/files/42202372/mic071903_subsampled.csv      |
|  2 | mic072003_subsampled      | trajectoryProfile |       59.8718 |       -152.181 | 2003-07-20 15:55:00 |       59.8176 |       -152.45  | 2003-07-20 11:00:00 | https://researchworkspace.com/files/42202373/mic072003_subsampled.csv      |
|  3 | mic072103_subsampled      | trajectoryProfile |       59.8729 |       -152.147 | 2003-07-21 11:30:00 |       59.8246 |       -152.456 | 2003-07-21 06:25:00 | https://researchworkspace.com/files/42202374/mic072103_subsampled.csv      |
|  4 | mic072203_subsampled      | trajectoryProfile |       59.8739 |       -152.153 | 2003-07-22 15:50:00 |       59.8371 |       -152.441 | 2003-07-22 11:15:00 | https://researchworkspace.com/files/42202375/mic072203_subsampled.csv      |
|  5 | mic072403_subsampled      | trajectoryProfile |       59.874  |       -152.164 | 2003-07-24 15:55:00 |       59.8376 |       -152.445 | 2003-07-24 11:30:00 | https://researchworkspace.com/files/42202376/mic072403_subsampled.csv      |
|  6 | mic072503_subsampled      | trajectoryProfile |       59.8589 |       -152.156 | 2003-07-25 12:10:00 |       59.8267 |       -152.464 | 2003-07-25 06:55:00 | https://researchworkspace.com/files/42202377/mic072503_subsampled.csv      |
|  7 | mic072603_subsampled      | trajectoryProfile |       59.8736 |       -152.158 | 2003-07-26 16:15:00 |       59.8275 |       -152.434 | 2003-07-26 11:05:00 | https://researchworkspace.com/files/42202378/mic072603_subsampled.csv      |
|  8 | mic072803_65-8_subsampled | trajectoryProfile |       59.8948 |       -152.303 | 2003-07-28 17:05:00 |       59.8644 |       -152.439 | 2003-07-28 14:50:00 | https://researchworkspace.com/files/42202379/mic072803_65-8_subsampled.csv |
|  9 | mic072903_subsampled      | trajectoryProfile |       59.8801 |       -152.154 | 2003-07-29 10:10:00 |       59.7911 |       -152.419 | 2003-07-29 05:35:00 | https://researchworkspace.com/files/42202380/mic072903_subsampled.csv      |
| 10 | mic073003_subsampled      | trajectoryProfile |       59.8731 |       -152.182 | 2003-07-30 14:10:00 |       59.7915 |       -152.435 | 2003-07-30 10:05:00 | https://researchworkspace.com/files/42202381/mic073003_subsampled.csv      |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_otf_kbnerr"))
```

## Map of Towed CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_otf_kbnerr")("ctd_towed_otf_kbnerr")
    
```

## mic071303

+++

mic071303_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic071303_subsampled'].plot.map() + cat['mic071303_subsampled'].plot.salt() + cat['mic071303_subsampled'].plot.temp()
```

## mic071903

+++

mic071903_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic071903_subsampled'].plot.map() + cat['mic071903_subsampled'].plot.salt() + cat['mic071903_subsampled'].plot.temp()
```

## mic072003

+++

mic072003_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072003_subsampled'].plot.map() + cat['mic072003_subsampled'].plot.salt() + cat['mic072003_subsampled'].plot.temp()
```

## mic072103

+++

mic072103_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072103_subsampled'].plot.map() + cat['mic072103_subsampled'].plot.salt() + cat['mic072103_subsampled'].plot.temp()
```

## mic072203

+++

mic072203_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072203_subsampled'].plot.map() + cat['mic072203_subsampled'].plot.salt() + cat['mic072203_subsampled'].plot.temp()
```

## mic072403

+++

mic072403_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072403_subsampled'].plot.map() + cat['mic072403_subsampled'].plot.salt() + cat['mic072403_subsampled'].plot.temp()
```

## mic072503

+++

mic072503_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072503_subsampled'].plot.map() + cat['mic072503_subsampled'].plot.salt() + cat['mic072503_subsampled'].plot.temp()
```

## mic072603

+++

mic072603_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072603_subsampled'].plot.map() + cat['mic072603_subsampled'].plot.salt() + cat['mic072603_subsampled'].plot.temp()
```

## mic072803_65-8

+++

mic072803_65-8_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072803_65-8_subsampled'].plot.map() + cat['mic072803_65-8_subsampled'].plot.salt() + cat['mic072803_65-8_subsampled'].plot.temp()
```

## mic072903

+++

mic072903_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic072903_subsampled'].plot.map() + cat['mic072903_subsampled'].plot.salt() + cat['mic072903_subsampled'].plot.temp()
```

## mic073003

+++

mic073003_subsampled
        

```{code-cell}
:tags: [full-width]

cat['mic073003_subsampled'].plot.map() + cat['mic073003_subsampled'].plot.salt() + cat['mic073003_subsampled'].plot.temp()
```
