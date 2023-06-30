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

(page:ctd_profiles_2005_noaa)=
# CTD Profiles (NOAA): across Cook Inlet

* CTD profiles 2005 - NOAA
* ctd_profiles_2005_noaa
* One-off CTD profiles in June and July 2005

CTD Profiles from NOAA.




```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                     |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------------|
|  0 |       501 | profile       | ['temp', 'salt'] |       60.722  |       -151.647 | 2005-06-16 15:34:00 |       60.722  |       -151.647 | 2005-06-16 15:34:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  1 |       502 | profile       | ['temp', 'salt'] |       60.7207 |       -151.557 | 2005-06-16 15:08:00 |       60.7207 |       -151.557 | 2005-06-16 15:08:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  2 |       503 | profile       | ['temp', 'salt'] |       60.7173 |       -151.433 | 2005-06-16 14:34:00 |       60.7173 |       -151.433 | 2005-06-16 14:34:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  3 |       504 | profile       | ['temp', 'salt'] |       60.6834 |       -151.418 | 2005-06-16 14:01:00 |       60.6834 |       -151.418 | 2005-06-16 14:01:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  4 |       505 | profile       | ['temp', 'salt'] |       60.5967 |       -151.739 | 2005-06-16 16:33:00 |       60.5967 |       -151.739 | 2005-06-16 16:33:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  5 |       506 | profile       | ['temp', 'salt'] |       60.5871 |       -151.445 | 2005-06-16 12:47:00 |       60.5871 |       -151.445 | 2005-06-16 12:47:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  6 |       507 | profile       | ['temp', 'salt'] |       60.5517 |       -152.128 | 2005-06-16 18:14:00 |       60.5517 |       -152.128 | 2005-06-16 18:14:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  7 |       508 | profile       | ['temp', 'salt'] |       60.483  |       -151.673 | 2005-06-16 11:07:00 |       60.483  |       -151.673 | 2005-06-16 11:07:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  8 |       509 | profile       | ['temp', 'salt'] |       60.3792 |       -152.182 | 2005-06-16 20:07:00 |       60.3792 |       -152.182 | 2005-06-16 20:07:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
|  9 |       510 | profile       | ['temp', 'salt'] |       60.248  |       -151.755 | 2005-06-16 09:05:00 |       60.248  |       -151.755 | 2005-06-16 09:05:00 | https://researchworkspace.com/files/39886023/noaa_north.txt |
| 10 |       511 | profile       | ['temp', 'salt'] |       60.0233 |       -152.12  | 2005-07-28 20:04:00 |       60.0233 |       -152.12  | 2005-07-28 20:04:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 11 |       512 | profile       | ['temp', 'salt'] |       59.5661 |       -153.422 | 2005-07-29 05:12:00 |       59.5661 |       -153.422 | 2005-07-29 05:12:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 12 |       513 | profile       | ['temp', 'salt'] |       59.4828 |       -151.755 | 2005-07-30 23:40:00 |       59.4828 |       -151.755 | 2005-07-30 23:40:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 13 |       514 | profile       | ['temp', 'salt'] |       59.3018 |       -152.92  | 2005-07-29 10:51:00 |       59.3018 |       -152.92  | 2005-07-29 10:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 14 |       515 | profile       | ['temp', 'salt'] |       59.3149 |       -152.365 | 2005-07-30 19:51:00 |       59.3149 |       -152.365 | 2005-07-30 19:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 15 |       516 | profile       | ['temp', 'salt'] |       59.4001 |       -151.966 | 2005-07-30 22:32:00 |       59.4001 |       -151.966 | 2005-07-30 22:32:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 16 |       517 | profile       | ['temp', 'salt'] |       58.8901 |       -153.184 | 2005-07-29 14:36:00 |       58.8901 |       -153.184 | 2005-07-29 14:36:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 17 |       518 | profile       | ['temp', 'salt'] |       58.9305 |       -152.728 | 2005-07-30 09:24:00 |       58.9305 |       -152.728 | 2005-07-30 09:24:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 18 |       519 | profile       | ['temp', 'salt'] |       58.808  |       -152.408 | 2005-07-30 04:08:00 |       58.808  |       -152.408 | 2005-07-30 04:08:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 19 |       520 | profile       | ['temp', 'salt'] |       59.0492 |       -152.152 | 2005-07-30 11:51:00 |       59.0492 |       -152.152 | 2005-07-30 11:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 20 |       521 | profile       | ['temp', 'salt'] |       59.1207 |       -151.895 | 2005-07-30 17:33:00 |       59.1207 |       -151.895 | 2005-07-30 17:33:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 21 |       522 | profile       | ['temp', 'salt'] |       59.2112 |       -151.787 | 2005-07-30 15:36:00 |       59.2112 |       -151.787 | 2005-07-30 15:36:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 22 |       523 | profile       | ['temp', 'salt'] |       59.0129 |       -151.775 | 2005-07-30 16:03:00 |       59.0129 |       -151.775 | 2005-07-30 16:03:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |
| 23 |       524 | profile       | ['temp', 'salt'] |       59.1339 |       -151.706 | 2005-07-30 16:51:00 |       59.1339 |       -151.706 | 2005-07-30 16:51:00 | https://researchworkspace.com/files/39886022/noaa_south.txt |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_2005_noaa"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_2005_noaa")("ctd_profiles_2005_noaa")
```

## 501
        

```{code-cell}
:tags: [remove-input]

cat['501'].plot.data()
```

## 502
        

```{code-cell}
:tags: [remove-input]

cat['502'].plot.data()
```

## 503
        

```{code-cell}
:tags: [remove-input]

cat['503'].plot.data()
```

## 504
        

```{code-cell}
:tags: [remove-input]

cat['504'].plot.data()
```

## 505
        

```{code-cell}
:tags: [remove-input]

cat['505'].plot.data()
```

## 506
        

```{code-cell}
:tags: [remove-input]

cat['506'].plot.data()
```

## 507
        

```{code-cell}
:tags: [remove-input]

cat['507'].plot.data()
```

## 508
        

```{code-cell}
:tags: [remove-input]

cat['508'].plot.data()
```

## 509
        

```{code-cell}
:tags: [remove-input]

cat['509'].plot.data()
```

## 510
        

```{code-cell}
:tags: [remove-input]

cat['510'].plot.data()
```

## 511
        

```{code-cell}
:tags: [remove-input]

cat['511'].plot.data()
```

## 512
        

```{code-cell}
:tags: [remove-input]

cat['512'].plot.data()
```

## 513
        

```{code-cell}
:tags: [remove-input]

cat['513'].plot.data()
```

## 514
        

```{code-cell}
:tags: [remove-input]

cat['514'].plot.data()
```

## 515
        

```{code-cell}
:tags: [remove-input]

cat['515'].plot.data()
```

## 516
        

```{code-cell}
:tags: [remove-input]

cat['516'].plot.data()
```

## 517
        

```{code-cell}
:tags: [remove-input]

cat['517'].plot.data()
```

## 518
        

```{code-cell}
:tags: [remove-input]

cat['518'].plot.data()
```

## 519
        

```{code-cell}
:tags: [remove-input]

cat['519'].plot.data()
```

## 520
        

```{code-cell}
:tags: [remove-input]

cat['520'].plot.data()
```

## 521
        

```{code-cell}
:tags: [remove-input]

cat['521'].plot.data()
```

## 522
        

```{code-cell}
:tags: [remove-input]

cat['522'].plot.data()
```

## 523
        

```{code-cell}
:tags: [remove-input]

cat['523'].plot.data()
```

## 524
        

```{code-cell}
:tags: [remove-input]

cat['524'].plot.data()
```
