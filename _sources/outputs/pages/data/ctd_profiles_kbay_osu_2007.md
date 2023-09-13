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

(page:ctd_profiles_kbay_osu_2007)=
# CTD Profiles (Kbay OSU 2007)

* Kbay OSU 2007
* ctd_profiles_kbay_osu_2007
* One-off CTD profiles September 2007

CTD Profiles in Cook Inlet



```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                   |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------|
|  0 |         1 | profile       | ['temp', 'salt'] |       59.3482 |       -151.973 | 2007-09-06 09:05:00 |       59.3482 |       -151.973 | 2007-09-06 09:05:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  1 |        10 | profile       | ['temp', 'salt'] |       59.3587 |       -152     | 2007-09-06 13:03:00 |       59.3587 |       -152     | 2007-09-06 13:03:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  2 |        11 | profile       | ['temp', 'salt'] |       59.358  |       -152.002 | 2007-09-06 13:52:00 |       59.358  |       -152.002 | 2007-09-06 13:52:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  3 |        12 | profile       | ['temp', 'salt'] |       59.3567 |       -152.004 | 2007-09-06 14:00:00 |       59.3567 |       -152.004 | 2007-09-06 14:00:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  4 |        13 | profile       | ['temp', 'salt'] |       59.3557 |       -152.005 | 2007-09-06 14:10:00 |       59.3557 |       -152.005 | 2007-09-06 14:10:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  5 |        14 | profile       | ['temp', 'salt'] |       59.3557 |       -152.005 | 2007-09-07 14:12:00 |       59.3557 |       -152.005 | 2007-09-07 14:12:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  6 |        15 | profile       | ['temp', 'salt'] |       59.4377 |       -151.879 | 2007-09-07 09:12:00 |       59.4377 |       -151.879 | 2007-09-07 09:12:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  7 |        16 | profile       | ['temp', 'salt'] |       59.4407 |       -151.87  | 2007-09-07 09:23:00 |       59.4407 |       -151.87  | 2007-09-07 09:23:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  8 |        17 | profile       | ['temp', 'salt'] |       59.4407 |       -151.87  | 2007-09-07 09:23:00 |       59.4407 |       -151.87  | 2007-09-07 09:23:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
|  9 |        18 | profile       | ['temp', 'salt'] |       59.4385 |       -151.955 | 2007-09-07 10:00:00 |       59.4385 |       -151.955 | 2007-09-07 10:00:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 10 |        19 | profile       | ['temp', 'salt'] |       59.4343 |       -151.95  | 2007-09-07 10:13:00 |       59.4343 |       -151.95  | 2007-09-07 10:13:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 11 |         2 | profile       | ['temp', 'salt'] |       59.3563 |       -151.998 | 2007-09-06 10:30:00 |       59.3563 |       -151.998 | 2007-09-06 10:30:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 12 |        20 | profile       | ['temp', 'salt'] |       59.4402 |       -151.945 | 2007-09-07 10:25:00 |       59.4402 |       -151.945 | 2007-09-07 10:25:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 13 |        21 | profile       | ['temp', 'salt'] |       59.4355 |       -151.933 | 2007-09-07 11:10:00 |       59.4355 |       -151.933 | 2007-09-07 11:10:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 14 |        22 | profile       | ['temp', 'salt'] |       59.4402 |       -151.926 | 2007-09-07 11:18:00 |       59.4402 |       -151.926 | 2007-09-07 11:18:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 15 |        23 | profile       | ['temp', 'salt'] |       59.4457 |       -151.918 | 2007-09-07 11:29:00 |       59.4457 |       -151.918 | 2007-09-07 11:29:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 16 |        24 | profile       | ['temp', 'salt'] |       59.436  |       -151.883 | 2007-09-07 12:14:00 |       59.436  |       -151.883 | 2007-09-07 12:14:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 17 |        25 | profile       | ['temp', 'salt'] |       59.4383 |       -151.883 | 2007-09-07 12:23:00 |       59.4383 |       -151.883 | 2007-09-07 12:23:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 18 |        26 | profile       | ['temp', 'salt'] |       59.4398 |       -151.883 | 2007-09-07 12:29:00 |       59.4398 |       -151.883 | 2007-09-07 12:29:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 19 |        27 | profile       | ['temp', 'salt'] |       59.4415 |       -151.881 | 2007-09-07 12:34:00 |       59.4415 |       -151.881 | 2007-09-07 12:34:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 20 |        28 | profile       | ['temp', 'salt'] |       59.4433 |       -151.879 | 2007-09-07 12:41:00 |       59.4433 |       -151.879 | 2007-09-07 12:41:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 21 |        29 | profile       | ['temp', 'salt'] |       59.4458 |       -151.875 | 2007-09-07 12:49:00 |       59.4458 |       -151.875 | 2007-09-07 12:49:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 22 |         3 | profile       | ['temp', 'salt'] |       59.3607 |       -151.993 | 2007-09-06 10:38:00 |       59.3607 |       -151.993 | 2007-09-06 10:38:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 23 |        30 | profile       | ['temp', 'salt'] |       59.4483 |       -151.869 | 2007-09-08 12:58:00 |       59.4483 |       -151.869 | 2007-09-08 12:58:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 24 |        31 | profile       | ['temp', 'salt'] |       59.4522 |       -151.85  | 2007-09-08 09:26:00 |       59.4522 |       -151.85  | 2007-09-08 09:26:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 25 |        32 | profile       | ['temp', 'salt'] |       59.4538 |       -151.846 | 2007-09-08 09:35:00 |       59.4538 |       -151.846 | 2007-09-08 09:35:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 26 |        33 | profile       | ['temp', 'salt'] |       59.4553 |       -151.841 | 2007-09-08 09:46:00 |       59.4553 |       -151.841 | 2007-09-08 09:46:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 27 |        34 | profile       | ['temp', 'salt'] |       59.441  |       -151.875 | 2007-09-08 10:08:00 |       59.441  |       -151.875 | 2007-09-08 10:08:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 28 |        35 | profile       | ['temp', 'salt'] |       59.4437 |       -151.865 | 2007-09-08 10:17:00 |       59.4437 |       -151.865 | 2007-09-08 10:17:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 29 |        36 | profile       | ['temp', 'salt'] |       59.4455 |       -151.855 | 2007-09-08 10:26:00 |       59.4455 |       -151.855 | 2007-09-08 10:26:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 30 |        37 | profile       | ['temp', 'salt'] |       59.449  |       -151.854 | 2007-09-08 11:37:00 |       59.449  |       -151.854 | 2007-09-08 11:37:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 31 |        38 | profile       | ['temp', 'salt'] |       59.4512 |       -151.845 | 2007-09-08 11:49:00 |       59.4512 |       -151.845 | 2007-09-08 11:49:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 32 |        39 | profile       | ['temp', 'salt'] |       59.4525 |       -151.839 | 2007-09-08 11:59:00 |       59.4525 |       -151.839 | 2007-09-08 11:59:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 33 |         4 | profile       | ['temp', 'salt'] |       59.3637 |       -151.992 | 2007-09-06 10:46:00 |       59.3637 |       -151.992 | 2007-09-06 10:46:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 34 |        40 | profile       | ['temp', 'salt'] |       59.4482 |       -151.875 | 2007-09-08 12:18:00 |       59.4482 |       -151.875 | 2007-09-08 12:18:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 35 |        41 | profile       | ['temp', 'salt'] |       59.4545 |       -151.86  | 2007-09-08 12:31:00 |       59.4545 |       -151.86  | 2007-09-08 12:31:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 36 |        42 | profile       | ['temp', 'salt'] |       59.4512 |       -151.849 | 2007-09-08 12:44:00 |       59.4512 |       -151.849 | 2007-09-08 12:44:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 37 |        43 | profile       | ['temp', 'salt'] |       59.4327 |       -151.891 | 2007-09-08 13:05:00 |       59.4327 |       -151.891 | 2007-09-08 13:05:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 38 |        44 | profile       | ['temp', 'salt'] |       59.4352 |       -151.891 | 2007-09-08 13:18:00 |       59.4352 |       -151.891 | 2007-09-08 13:18:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 39 |        45 | profile       | ['temp', 'salt'] |       59.4393 |       -151.889 | 2007-09-08 13:29:00 |       59.4393 |       -151.889 | 2007-09-08 13:29:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 40 |         5 | profile       | ['temp', 'salt'] |       59.3577 |       -151.999 | 2007-09-06 11:38:00 |       59.3577 |       -151.999 | 2007-09-06 11:38:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 41 |         6 | profile       | ['temp', 'salt'] |       59.3608 |       -151.995 | 2007-09-06 11:49:00 |       59.3608 |       -151.995 | 2007-09-06 11:49:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 42 |         7 | profile       | ['temp', 'salt'] |       59.3642 |       -151.994 | 2007-09-06 12:01:00 |       59.3642 |       -151.994 | 2007-09-06 12:01:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 43 |         8 | profile       | ['temp', 'salt'] |       59.3577 |       -152.001 | 2007-09-06 12:45:00 |       59.3577 |       -152.001 | 2007-09-06 12:45:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |
| 44 |         9 | profile       | ['temp', 'salt'] |       59.3582 |       -152.001 | 2007-09-06 12:53:00 |       59.3582 |       -152.001 | 2007-09-06 12:53:00 | https://researchworkspace.com/files/39888023/kbay_odv.txt |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_kbay_osu_2007"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_kbay_osu_2007")("ctd_profiles_kbay_osu_2007")
```

## 1
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1'].plot.data()
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

## 13
        

```{code-cell}
:tags: [full-width, remove-input]

cat['13'].plot.data()
```

## 14
        

```{code-cell}
:tags: [full-width, remove-input]

cat['14'].plot.data()
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

## 18
        

```{code-cell}
:tags: [full-width, remove-input]

cat['18'].plot.data()
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

## 22
        

```{code-cell}
:tags: [full-width, remove-input]

cat['22'].plot.data()
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

## 25
        

```{code-cell}
:tags: [full-width, remove-input]

cat['25'].plot.data()
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

## 31
        

```{code-cell}
:tags: [full-width, remove-input]

cat['31'].plot.data()
```

## 32
        

```{code-cell}
:tags: [full-width, remove-input]

cat['32'].plot.data()
```

## 33
        

```{code-cell}
:tags: [full-width, remove-input]

cat['33'].plot.data()
```

## 34
        

```{code-cell}
:tags: [full-width, remove-input]

cat['34'].plot.data()
```

## 35
        

```{code-cell}
:tags: [full-width, remove-input]

cat['35'].plot.data()
```

## 36
        

```{code-cell}
:tags: [full-width, remove-input]

cat['36'].plot.data()
```

## 37
        

```{code-cell}
:tags: [full-width, remove-input]

cat['37'].plot.data()
```

## 38
        

```{code-cell}
:tags: [full-width, remove-input]

cat['38'].plot.data()
```

## 39
        

```{code-cell}
:tags: [full-width, remove-input]

cat['39'].plot.data()
```

## 4
        

```{code-cell}
:tags: [full-width, remove-input]

cat['4'].plot.data()
```

## 40
        

```{code-cell}
:tags: [full-width, remove-input]

cat['40'].plot.data()
```

## 41
        

```{code-cell}
:tags: [full-width, remove-input]

cat['41'].plot.data()
```

## 42
        

```{code-cell}
:tags: [full-width, remove-input]

cat['42'].plot.data()
```

## 43
        

```{code-cell}
:tags: [full-width, remove-input]

cat['43'].plot.data()
```

## 44
        

```{code-cell}
:tags: [full-width, remove-input]

cat['44'].plot.data()
```

## 45
        

```{code-cell}
:tags: [full-width, remove-input]

cat['45'].plot.data()
```

## 5
        

```{code-cell}
:tags: [full-width, remove-input]

cat['5'].plot.data()
```

## 6
        

```{code-cell}
:tags: [full-width, remove-input]

cat['6'].plot.data()
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
