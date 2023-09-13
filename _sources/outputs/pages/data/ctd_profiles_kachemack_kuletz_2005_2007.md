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

(page:ctd_profiles_kachemack_kuletz_2005_2007)=
# CTD Profiles (Kachemak Kuletz 2005–2007)

* Kachemak Kuletz 2005–2007
* ctd_profiles_kachemack_kuletz_2005_2007
* One-off CTD profiles June-July 2005 and July 2006 and 2007

CTD Profiles in Cook Inlet



```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                 |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:--------------------------------------------------------|
|  0 |      1    | profile       | ['temp', 'salt'] |       59.7383 |       -151.095 | 2005-06-20 18:44:00 |       59.7383 |       -151.095 | 2005-06-20 18:44:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  1 |      1.1  | profile       | ['temp', 'salt'] |       59.7367 |       -151.067 | 2006-07-23 21:40:00 |       59.7367 |       -151.067 | 2006-07-23 21:40:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  2 |     10    | profile       | ['temp', 'salt'] |       59.555  |       -151.67  | 2005-06-21 15:38:00 |       59.555  |       -151.67  | 2005-06-21 15:38:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  3 |  10000    | profile       | ['temp', 'salt'] |       59.4917 |       -151.65  | 2007-07-24 21:31:00 |       59.4917 |       -151.65  | 2007-07-24 21:31:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  4 |  10001    | profile       | ['temp', 'salt'] |       59.4967 |       -151.65  | 2007-07-24 21:37:00 |       59.4967 |       -151.65  | 2007-07-24 21:37:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  5 |  10002    | profile       | ['temp', 'salt'] |       59.5083 |       -151.65  | 2007-07-24 21:46:00 |       59.5083 |       -151.65  | 2007-07-24 21:46:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  6 |  10003    | profile       | ['temp', 'salt'] |       59.525  |       -151.65  | 2007-07-24 22:01:00 |       59.525  |       -151.65  | 2007-07-24 22:01:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  7 |  10004    | profile       | ['temp', 'salt'] |       59.5417 |       -151.65  | 2007-07-24 22:14:00 |       59.5417 |       -151.65  | 2007-07-24 22:14:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  8 |  10005    | profile       | ['temp', 'salt'] |       59.5583 |       -151.65  | 2007-07-24 22:26:00 |       59.5583 |       -151.65  | 2007-07-24 22:26:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
|  9 |  10006    | profile       | ['temp', 'salt'] |       59.575  |       -151.65  | 2007-07-24 22:38:00 |       59.575  |       -151.65  | 2007-07-24 22:38:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 10 |  10007    | profile       | ['temp', 'salt'] |       59.5917 |       -151.65  | 2007-07-24 22:47:00 |       59.5917 |       -151.65  | 2007-07-24 22:47:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 11 |  10008    | profile       | ['temp', 'salt'] |       59.6083 |       -151.65  | 2007-07-24 22:56:00 |       59.6083 |       -151.65  | 2007-07-24 22:56:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 12 |  10009    | profile       | ['temp', 'salt'] |       59.625  |       -151.65  | 2007-07-24 23:08:00 |       59.625  |       -151.65  | 2007-07-24 23:08:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 13 |  10010    | profile       | ['temp', 'salt'] |       59.7317 |       -151.133 | 2007-07-25 17:42:00 |       59.7317 |       -151.133 | 2007-07-25 17:42:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 14 |  10011    | profile       | ['temp', 'salt'] |       59.7167 |       -151.133 | 2007-07-25 17:50:00 |       59.7167 |       -151.133 | 2007-07-25 17:50:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 15 |  10012    | profile       | ['temp', 'salt'] |       59.7    |       -151.133 | 2007-07-25 18:00:00 |       59.7    |       -151.133 | 2007-07-25 18:00:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 16 |  10013    | profile       | ['temp', 'salt'] |       59.6833 |       -151.133 | 2007-07-25 18:11:00 |       59.6833 |       -151.133 | 2007-07-25 18:11:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 17 |  10014    | profile       | ['temp', 'salt'] |       59.65   |       -151.2   | 2007-07-25 18:35:00 |       59.65   |       -151.2   | 2007-07-25 18:35:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 18 |  10015    | profile       | ['temp', 'salt'] |       59.6667 |       -151.2   | 2007-07-25 18:44:00 |       59.6667 |       -151.2   | 2007-07-25 18:44:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 19 |  10016    | profile       | ['temp', 'salt'] |       59.6833 |       -151.2   | 2007-07-25 18:54:00 |       59.6833 |       -151.2   | 2007-07-25 18:54:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 20 |  10017    | profile       | ['temp', 'salt'] |       59.7    |       -151.2   | 2007-07-25 19:08:00 |       59.7    |       -151.2   | 2007-07-25 19:08:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 21 |    101    | profile       | ['temp', 'salt'] |       59.7367 |       -151.067 | 2005-07-23 22:28:00 |       59.7367 |       -151.068 | 2005-07-23 22:28:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 22 |    103    | profile       | ['temp', 'salt'] |       59.7    |       -151.2   | 2005-07-23 20:57:00 |       59.7    |       -151.2   | 2005-07-23 20:57:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 23 |    104    | profile       | ['temp', 'salt'] |       59.6733 |       -151.267 | 2005-07-23 23:20:00 |       59.6733 |       -151.267 | 2005-07-23 23:20:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 24 |    105    | profile       | ['temp', 'salt'] |       59.6533 |       -151.333 | 2005-07-23 19:12:00 |       59.6533 |       -151.333 | 2005-07-23 19:12:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 25 |    107    | profile       | ['temp', 'salt'] |       59.6    |       -151.467 | 2005-07-23 01:01:00 |       59.6    |       -151.467 | 2005-07-23 01:01:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 26 |    109    | profile       | ['temp', 'salt'] |       59.6167 |       -151.6   | 2005-07-22 23:26:00 |       59.6167 |       -151.6   | 2005-07-22 23:26:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 27 |     11    | profile       | ['temp', 'salt'] |       59.535  |       -151.732 | 2005-06-16 16:47:00 |       59.535  |       -151.732 | 2005-06-16 16:47:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 28 |    111    | profile       | ['temp', 'salt'] |       59.6333 |       -151.733 | 2005-07-22 23:06:00 |       59.6333 |       -151.733 | 2005-07-22 23:06:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 29 |     12.1  | profile       | ['temp', 'salt'] |       59.6667 |       -151.8   | 2006-07-22 18:32:00 |       59.6667 |       -151.8   | 2006-07-22 18:32:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 30 |     12.2  | profile       | ['temp', 'salt'] |       59.6167 |       -151.8   | 2006-07-22 18:48:00 |       59.6167 |       -151.8   | 2006-07-22 18:48:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 31 |     12.3  | profile       | ['temp', 'salt'] |       59.5667 |       -151.8   | 2006-07-22 19:06:00 |       59.5667 |       -151.8   | 2006-07-22 19:06:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 32 |     12.4  | profile       | ['temp', 'salt'] |       59.5    |       -151.8   | 2006-07-22 19:30:00 |       59.5    |       -151.8   | 2006-07-22 19:30:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 33 |     12.5  | profile       | ['temp', 'salt'] |       59.4567 |       -151.8   | 2006-07-22 19:51:00 |       59.4567 |       -151.8   | 2006-07-22 19:51:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 34 |      2    | profile       | ['temp', 'salt'] |       59.7183 |       -151.133 | 2005-06-20 18:33:00 |       59.7183 |       -151.133 | 2005-06-20 18:33:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 35 |      2.02 | profile       | ['temp', 'salt'] |       59.7    |       -151.133 | 2006-07-23 20:19:00 |       59.7    |       -151.133 | 2006-07-23 20:19:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 36 |      2.03 | profile       | ['temp', 'salt'] |       59.7317 |       -151.133 | 2006-07-23 21:26:00 |       59.7317 |       -151.133 | 2006-07-23 21:26:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 37 |      2.2  | profile       | ['temp', 'salt'] |       59.7167 |       -151.133 | 2006-07-23 21:11:00 |       59.7167 |       -151.133 | 2006-07-23 21:11:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 38 |      2.3  | profile       | ['temp', 'salt'] |       59.6833 |       -151.133 | 2006-07-23 20:36:00 |       59.6833 |       -151.133 | 2006-07-23 20:36:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 39 |    202    | profile       | ['temp', 'salt'] |       59.7167 |       -151.133 | 2005-07-23 21:21:00 |       59.7167 |       -151.133 | 2005-07-23 21:21:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 40 |    203    | profile       | ['temp', 'salt'] |       59.65   |       -151.2   | 2005-07-23 20:07:00 |       59.65   |       -151.2   | 2005-07-23 20:07:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 41 |    204    | profile       | ['temp', 'salt'] |       59.65   |       -151.267 | 2005-07-23 19:27:00 |       59.65   |       -151.267 | 2005-07-23 19:27:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 42 |    205    | profile       | ['temp', 'salt'] |       59.6169 |       -151.333 | 2005-07-23 18:22:00 |       59.6167 |       -151.333 | 2005-07-23 18:22:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 43 |    206    | profile       | ['temp', 'salt'] |       59.6167 |       -151.4   | 2005-07-23 17:11:00 |       59.6167 |       -151.4   | 2005-07-23 17:11:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 44 |    207    | profile       | ['temp', 'salt'] |       59.5333 |       -151.467 | 2005-07-23 00:40:00 |       59.5333 |       -151.467 | 2005-07-23 00:40:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 45 |    209    | profile       | ['temp', 'salt'] |       59.5667 |       -151.6   | 2005-07-22 23:42:00 |       59.5667 |       -151.6   | 2005-07-22 23:42:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 46 |    211    | profile       | ['temp', 'salt'] |       59.5667 |       -151.733 | 2005-07-22 22:42:00 |       59.5667 |       -151.733 | 2005-07-22 22:42:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 47 |      3    | profile       | ['temp', 'salt'] |       59.6867 |       -151.2   | 2005-06-20 18:18:00 |       59.6867 |       -151.2   | 2005-06-20 18:18:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 48 |      3.01 | profile       | ['temp', 'salt'] |       59.6667 |       -151.2   | 2006-07-23 19:27:00 |       59.6667 |       -151.2   | 2006-07-23 19:27:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 49 |      3.02 | profile       | ['temp', 'salt'] |       59.6833 |       -151.2   | 2006-07-23 19:39:00 |       59.6833 |       -151.2   | 2006-07-23 19:39:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 50 |      3.1  | profile       | ['temp', 'salt'] |       59.7    |       -151.2   | 2006-07-23 20:04:00 |       59.7    |       -151.2   | 2006-07-23 20:04:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 51 |      3.2  | profile       | ['temp', 'salt'] |       59.65   |       -151.2   | 2006-07-23 23:31:00 |       59.65   |       -151.2   | 2006-07-23 23:31:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 52 |    302    | profile       | ['temp', 'salt'] |       59.6833 |       -151.133 | 2005-07-23 21:09:00 |       59.6816 |       -151.133 | 2005-07-23 21:09:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 53 |    304    | profile       | ['temp', 'salt'] |       59.6    |       -151.267 | 2005-07-23 19:46:00 |       59.6    |       -151.267 | 2005-07-23 19:46:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 54 |    305    | profile       | ['temp', 'salt'] |       59.5833 |       -151.337 | 2005-07-23 18:01:00 |       59.5833 |       -151.337 | 2005-07-23 18:01:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 55 |    306    | profile       | ['temp', 'salt'] |       59.56   |       -151.4   | 2005-07-23 17:42:00 |       59.56   |       -151.4   | 2005-07-23 17:42:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 56 |    309    | profile       | ['temp', 'salt'] |       59.5    |       -151.6   | 2005-07-23 00:03:00 |       59.5    |       -151.6   | 2005-07-23 00:03:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 57 |    311    | profile       | ['temp', 'salt'] |       59.485  |       -151.732 | 2005-07-22 22:09:00 |       59.485  |       -151.732 | 2005-07-22 22:09:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 58 |      4    | profile       | ['temp', 'salt'] |       59.6583 |       -151.267 | 2005-06-20 18:05:00 |       59.6583 |       -151.267 | 2005-06-20 18:05:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 59 |      4.1  | profile       | ['temp', 'salt'] |       59.6733 |       -151.267 | 2006-07-23 17:41:00 |       59.6733 |       -151.267 | 2006-07-23 17:41:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 60 |      5    | profile       | ['temp', 'salt'] |       59.6317 |       -151.335 | 2005-06-20 17:46:00 |       59.6317 |       -151.335 | 2005-06-20 17:46:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 61 |      6    | profile       | ['temp', 'salt'] |       59.5983 |       -151.4   | 2005-06-21 16:41:00 |       59.5983 |       -151.4   | 2005-06-21 16:41:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 62 |      7    | profile       | ['temp', 'salt'] |       59.5817 |       -151.467 | 2005-06-21 16:27:00 |       59.5817 |       -151.467 | 2005-06-21 16:27:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 63 |      8    | profile       | ['temp', 'salt'] |       59.5667 |       -151.533 | 2005-06-21 16:10:00 |       59.5667 |       -151.533 | 2005-06-21 16:10:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |
| 64 |      9    | profile       | ['temp', 'salt'] |       59.5617 |       -151.6   | 2005-06-21 15:54:00 |       59.5617 |       -151.6   | 2005-06-21 15:54:00 | https://researchworkspace.com/files/42400517/Kuletz.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_kachemack_kuletz_2005_2007"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_kachemack_kuletz_2005_2007")("ctd_profiles_kachemack_kuletz_2005_2007")
```

## 1.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1.0'].plot.data()
```

## 1.1
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1.1'].plot.data()
```

## 10.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10.0'].plot.data()
```

## 10000.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10000.0'].plot.data()
```

## 10001.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10001.0'].plot.data()
```

## 10002.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10002.0'].plot.data()
```

## 10003.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10003.0'].plot.data()
```

## 10004.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10004.0'].plot.data()
```

## 10005.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10005.0'].plot.data()
```

## 10006.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10006.0'].plot.data()
```

## 10007.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10007.0'].plot.data()
```

## 10008.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10008.0'].plot.data()
```

## 10009.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10009.0'].plot.data()
```

## 10010.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10010.0'].plot.data()
```

## 10011.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10011.0'].plot.data()
```

## 10012.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10012.0'].plot.data()
```

## 10013.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10013.0'].plot.data()
```

## 10014.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10014.0'].plot.data()
```

## 10015.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10015.0'].plot.data()
```

## 10016.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10016.0'].plot.data()
```

## 10017.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10017.0'].plot.data()
```

## 101.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['101.0'].plot.data()
```

## 103.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['103.0'].plot.data()
```

## 104.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['104.0'].plot.data()
```

## 105.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['105.0'].plot.data()
```

## 107.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['107.0'].plot.data()
```

## 109.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['109.0'].plot.data()
```

## 11.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['11.0'].plot.data()
```

## 111.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['111.0'].plot.data()
```

## 12.1
        

```{code-cell}
:tags: [full-width, remove-input]

cat['12.1'].plot.data()
```

## 12.2
        

```{code-cell}
:tags: [full-width, remove-input]

cat['12.2'].plot.data()
```

## 12.3
        

```{code-cell}
:tags: [full-width, remove-input]

cat['12.3'].plot.data()
```

## 12.4
        

```{code-cell}
:tags: [full-width, remove-input]

cat['12.4'].plot.data()
```

## 12.5
        

```{code-cell}
:tags: [full-width, remove-input]

cat['12.5'].plot.data()
```

## 2.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2.0'].plot.data()
```

## 2.02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2.02'].plot.data()
```

## 2.03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2.03'].plot.data()
```

## 2.2
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2.2'].plot.data()
```

## 2.3
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2.3'].plot.data()
```

## 202.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['202.0'].plot.data()
```

## 203.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['203.0'].plot.data()
```

## 204.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['204.0'].plot.data()
```

## 205.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['205.0'].plot.data()
```

## 206.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['206.0'].plot.data()
```

## 207.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['207.0'].plot.data()
```

## 209.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['209.0'].plot.data()
```

## 211.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['211.0'].plot.data()
```

## 3.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['3.0'].plot.data()
```

## 3.01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['3.01'].plot.data()
```

## 3.02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['3.02'].plot.data()
```

## 3.1
        

```{code-cell}
:tags: [full-width, remove-input]

cat['3.1'].plot.data()
```

## 3.2
        

```{code-cell}
:tags: [full-width, remove-input]

cat['3.2'].plot.data()
```

## 302.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['302.0'].plot.data()
```

## 304.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['304.0'].plot.data()
```

## 305.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['305.0'].plot.data()
```

## 306.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['306.0'].plot.data()
```

## 309.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['309.0'].plot.data()
```

## 311.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['311.0'].plot.data()
```

## 4.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['4.0'].plot.data()
```

## 4.1
        

```{code-cell}
:tags: [full-width, remove-input]

cat['4.1'].plot.data()
```

## 5.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['5.0'].plot.data()
```

## 6.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['6.0'].plot.data()
```

## 7.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['7.0'].plot.data()
```

## 8.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['8.0'].plot.data()
```

## 9.0
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9.0'].plot.data()
```
