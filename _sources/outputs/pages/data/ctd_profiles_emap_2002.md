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

(page:ctd_profiles_emap_2002)=
# CTD Profiles (emap 2002)

* emap 2002
* ctd_profiles_emap_2002
* One-off CTD profiles June to August 2002

CTD Profiles in Cook Inlet



```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                               |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------|
|  0 |        10 | profile       | ['temp', 'salt'] |       57.7088 |       -155.568 | 2002-08-18 22:21:00 |       57.7088 |       -155.568 | 2002-08-18 22:21:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  1 |        11 | profile       | ['temp', 'salt'] |       61.0326 |       -151.235 | 2002-08-01 22:50:00 |       61.0326 |       -151.235 | 2002-08-01 22:50:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  2 |        12 | profile       | ['temp', 'salt'] |       60.7028 |       -151.86  | 2002-08-01 03:50:00 |       60.7028 |       -151.86  | 2002-08-01 03:50:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  3 |        15 | profile       | ['temp', 'salt'] |       60.4996 |       -151.964 | 2002-08-01 17:00:00 |       60.4996 |       -151.964 | 2002-08-01 17:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  4 |        16 | profile       | ['temp', 'salt'] |       60.2494 |       -151.528 | 2002-07-31 16:08:00 |       60.2494 |       -151.528 | 2002-07-31 16:08:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  5 |        17 | profile       | ['temp', 'salt'] |       59.9748 |       -152.344 | 2002-07-10 18:00:00 |       59.9748 |       -152.344 | 2002-07-10 18:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  6 |        19 | profile       | ['temp', 'salt'] |       59.2895 |       -152.841 | 2002-06-17 05:20:00 |       59.2895 |       -152.841 | 2002-06-17 05:20:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  7 |         2 | profile       | ['temp', 'salt'] |       60.2097 |       -152.738 | 2002-07-10 23:00:00 |       60.2097 |       -152.738 | 2002-07-10 23:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  8 |        20 | profile       | ['temp', 'salt'] |       59.1081 |       -153.552 | 2002-07-07 16:43:00 |       59.1081 |       -153.552 | 2002-07-07 16:43:00 | https://researchworkspace.com/files/42199527/emap.csv |
|  9 |        21 | profile       | ['temp', 'salt'] |       59.1419 |       -152.331 | 2002-06-14 22:30:00 |       59.1419 |       -152.331 | 2002-06-14 22:30:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 10 |        23 | profile       | ['temp', 'salt'] |       59.0887 |       -153.089 | 2002-06-15 01:45:00 |       59.0887 |       -153.089 | 2002-06-15 01:45:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 11 |        24 | profile       | ['temp', 'salt'] |       58.7848 |       -152.817 | 2002-06-15 16:23:00 |       58.7848 |       -152.817 | 2002-06-15 16:23:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 12 |        26 | profile       | ['temp', 'salt'] |       58.5051 |       -152.833 | 2002-07-06 22:15:00 |       58.5051 |       -152.833 | 2002-07-06 22:15:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 13 |        27 | profile       | ['temp', 'salt'] |       58.0897 |       -153.502 | 2002-08-18 15:14:00 |       58.0897 |       -153.502 | 2002-08-18 15:14:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 14 |        28 | profile       | ['temp', 'salt'] |       57.9256 |       -154.29  | 2002-08-17 19:37:00 |       57.9256 |       -154.29  | 2002-08-17 19:37:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 15 |        29 | profile       | ['temp', 'salt'] |       57.8523 |       -154.552 | 2002-08-18 00:06:00 |       57.8523 |       -154.552 | 2002-08-18 00:06:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 16 |         3 | profile       | ['temp', 'salt'] |       59.8293 |       -153.128 | 2002-07-09 00:30:00 |       59.8293 |       -153.128 | 2002-07-09 00:30:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 17 |        30 | profile       | ['temp', 'salt'] |       57.6196 |       -155.186 | 2002-08-19 02:00:00 |       57.6196 |       -155.186 | 2002-08-19 02:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 18 |         4 | profile       | ['temp', 'salt'] |       59.6204 |       -151.248 | 2002-07-30 16:28:00 |       59.6204 |       -151.248 | 2002-07-30 16:28:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 19 |         5 | profile       | ['temp', 'salt'] |       59.2097 |       -151.822 | 2002-07-14 14:31:00 |       59.2097 |       -151.822 | 2002-07-14 14:31:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 20 |        65 | profile       | ['temp', 'salt'] |       58.4439 |       -152.349 | 2002-07-02 19:00:00 |       58.4439 |       -152.349 | 2002-07-02 19:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 21 |        67 | profile       | ['temp', 'salt'] |       57.1963 |       -153.207 | 2002-06-30 01:00:00 |       57.1963 |       -153.207 | 2002-06-30 01:00:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 22 |        68 | profile       | ['temp', 'salt'] |       57.0624 |       -153.576 | 2002-06-29 16:30:00 |       57.0624 |       -153.576 | 2002-06-29 16:30:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 23 |         7 | profile       | ['temp', 'salt'] |       58.3883 |       -152.981 | 2002-07-06 18:06:00 |       58.3883 |       -152.981 | 2002-07-06 18:06:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 24 |         8 | profile       | ['temp', 'salt'] |       57.9768 |       -154.956 | 2002-08-17 16:34:00 |       57.9768 |       -154.956 | 2002-08-17 16:34:00 | https://researchworkspace.com/files/42199527/emap.csv |
| 25 |         9 | profile       | ['temp', 'salt'] |       57.9808 |       -153.071 | 2002-07-06 02:05:00 |       57.9808 |       -153.071 | 2002-07-06 02:05:00 | https://researchworkspace.com/files/42199527/emap.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_emap_2002"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_emap_2002")("ctd_profiles_emap_2002")
```

## 10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10'].plot.data()
```

## 11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['11'].plot.data()
```

## 12
        

```{code-cell}
:tags: [full-width, remove-input]

cat['12'].plot.data()
```

## 15
        

```{code-cell}
:tags: [full-width, remove-input]

cat['15'].plot.data()
```

## 16
        

```{code-cell}
:tags: [full-width, remove-input]

cat['16'].plot.data()
```

## 17
        

```{code-cell}
:tags: [full-width, remove-input]

cat['17'].plot.data()
```

## 19
        

```{code-cell}
:tags: [full-width, remove-input]

cat['19'].plot.data()
```

## 2
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2'].plot.data()
```

## 20
        

```{code-cell}
:tags: [full-width, remove-input]

cat['20'].plot.data()
```

## 21
        

```{code-cell}
:tags: [full-width, remove-input]

cat['21'].plot.data()
```

## 23
        

```{code-cell}
:tags: [full-width, remove-input]

cat['23'].plot.data()
```

## 24
        

```{code-cell}
:tags: [full-width, remove-input]

cat['24'].plot.data()
```

## 26
        

```{code-cell}
:tags: [full-width, remove-input]

cat['26'].plot.data()
```

## 27
        

```{code-cell}
:tags: [full-width, remove-input]

cat['27'].plot.data()
```

## 28
        

```{code-cell}
:tags: [full-width, remove-input]

cat['28'].plot.data()
```

## 29
        

```{code-cell}
:tags: [full-width, remove-input]

cat['29'].plot.data()
```

## 3
        

```{code-cell}
:tags: [full-width, remove-input]

cat['3'].plot.data()
```

## 30
        

```{code-cell}
:tags: [full-width, remove-input]

cat['30'].plot.data()
```

## 4
        

```{code-cell}
:tags: [full-width, remove-input]

cat['4'].plot.data()
```

## 5
        

```{code-cell}
:tags: [full-width, remove-input]

cat['5'].plot.data()
```

## 65
        

```{code-cell}
:tags: [full-width, remove-input]

cat['65'].plot.data()
```

## 67
        

```{code-cell}
:tags: [full-width, remove-input]

cat['67'].plot.data()
```

## 68
        

```{code-cell}
:tags: [full-width, remove-input]

cat['68'].plot.data()
```

## 7
        

```{code-cell}
:tags: [full-width, remove-input]

cat['7'].plot.data()
```

## 8
        

```{code-cell}
:tags: [full-width, remove-input]

cat['8'].plot.data()
```

## 9
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9'].plot.data()
```
