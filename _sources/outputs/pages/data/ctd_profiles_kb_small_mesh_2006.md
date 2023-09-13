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

(page:ctd_profiles_kb_small_mesh_2006)=
# CTD Profiles (KB small mesh 2006)

* KB small mesh 2006
* ctd_profiles_kb_small_mesh_2006
* One-off CTD profiles May 2006

CTD Profiles in Cook Inlet



```{dropdown} Dataset metadata

|    |   Dataset | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                      |
|---:|----------:|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------|
|  0 |      1001 | profile       | ['temp', 'salt'] |       59.6743 |       -151.2   | 2006-05-10 19:11:00 |       59.6743 |       -151.2   | 2006-05-10 19:11:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  1 |      1002 | profile       | ['temp', 'salt'] |       59.6467 |       -151.22  | 2006-05-10 20:10:00 |       59.6467 |       -151.22  | 2006-05-10 20:10:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  2 |      1003 | profile       | ['temp', 'salt'] |       59.636  |       -151.266 | 2006-05-10 21:18:00 |       59.636  |       -151.266 | 2006-05-10 21:18:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  3 |      1004 | profile       | ['temp', 'salt'] |       59.6227 |       -151.264 | 2006-05-10 22:25:00 |       59.6227 |       -151.264 | 2006-05-10 22:25:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  4 |      1005 | profile       | ['temp', 'salt'] |       59.6058 |       -151.307 | 2006-05-10 23:31:00 |       59.6058 |       -151.307 | 2006-05-10 23:31:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  5 |      1006 | profile       | ['temp', 'salt'] |       59.5847 |       -151.529 | 2006-05-11 17:37:00 |       59.5847 |       -151.529 | 2006-05-11 17:37:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  6 |      1007 | profile       | ['temp', 'salt'] |       59.5506 |       -151.572 | 2006-05-11 18:42:00 |       59.5506 |       -151.572 | 2006-05-11 18:42:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  7 |      1008 | profile       | ['temp', 'salt'] |       59.5385 |       -151.598 | 2006-05-11 19:46:00 |       59.5385 |       -151.598 | 2006-05-11 19:46:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  8 |      1009 | profile       | ['temp', 'salt'] |       59.5338 |       -151.655 | 2006-05-11 20:54:00 |       59.5338 |       -151.655 | 2006-05-11 20:54:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
|  9 |      1010 | profile       | ['temp', 'salt'] |       59.522  |       -151.584 | 2006-05-11 21:55:00 |       59.522  |       -151.584 | 2006-05-11 21:55:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 10 |      1011 | profile       | ['temp', 'salt'] |       59.5112 |       -151.628 | 2006-05-11 23:02:00 |       59.5112 |       -151.628 | 2006-05-11 23:02:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 11 |      1012 | profile       | ['temp', 'salt'] |       59.5691 |       -151.471 | 2006-05-12 17:33:00 |       59.5691 |       -151.471 | 2006-05-12 17:33:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 12 |      1013 | profile       | ['temp', 'salt'] |       59.5505 |       -151.572 | 2006-05-12 18:42:00 |       59.5505 |       -151.572 | 2006-05-12 18:42:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 13 |      1014 | profile       | ['temp', 'salt'] |       59.5545 |       -151.5   | 2006-05-12 19:52:00 |       59.5545 |       -151.5   | 2006-05-12 19:52:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 14 |      1015 | profile       | ['temp', 'salt'] |       59.5557 |       -151.505 | 2006-05-12 21:29:00 |       59.5557 |       -151.505 | 2006-05-12 21:29:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 15 |      1017 | profile       | ['temp', 'salt'] |       59.6645 |       -151.233 | 2006-05-15 19:37:00 |       59.6645 |       -151.233 | 2006-05-15 19:37:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 16 |      1018 | profile       | ['temp', 'salt'] |       59.6832 |       -151.2   | 2006-05-15 20:49:00 |       59.6832 |       -151.2   | 2006-05-15 20:49:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 17 |      1019 | profile       | ['temp', 'salt'] |       59.7024 |       -151.162 | 2006-05-15 22:05:00 |       59.7024 |       -151.162 | 2006-05-15 22:05:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 18 |      1020 | profile       | ['temp', 'salt'] |       59.7227 |       -151.115 | 2006-05-15 23:31:00 |       59.7227 |       -151.115 | 2006-05-15 23:31:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 19 |      1021 | profile       | ['temp', 'salt'] |       59.6296 |       -151.282 | 2006-05-16 01:06:00 |       59.6296 |       -151.282 | 2006-05-16 01:06:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 20 |      1022 | profile       | ['temp', 'salt'] |       59.6137 |       -151.277 | 2006-05-16 02:07:00 |       59.6137 |       -151.277 | 2006-05-16 02:07:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 21 |      1023 | profile       | ['temp', 'salt'] |       59.6068 |       -151.332 | 2006-05-16 16:39:00 |       59.6068 |       -151.332 | 2006-05-16 16:39:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 22 |      1024 | profile       | ['temp', 'salt'] |       59.6115 |       -151.305 | 2006-05-16 17:31:00 |       59.6115 |       -151.305 | 2006-05-16 17:31:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 23 |      1025 | profile       | ['temp', 'salt'] |       59.6278 |       -151.302 | 2006-05-16 18:30:00 |       59.6278 |       -151.302 | 2006-05-16 18:30:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 24 |      1026 | profile       | ['temp', 'salt'] |       59.639  |       -151.297 | 2006-05-16 19:33:00 |       59.639  |       -151.297 | 2006-05-16 19:33:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 25 |      1027 | profile       | ['temp', 'salt'] |       59.5309 |       -151.565 | 2006-05-16 22:21:00 |       59.5309 |       -151.565 | 2006-05-16 22:21:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |
| 26 |      1028 | profile       | ['temp', 'salt'] |       59.5496 |       -151.555 | 2006-05-16 23:46:00 |       59.5496 |       -151.555 | 2006-05-16 23:46:00 | https://researchworkspace.com/files/42200009/KBsmallmesh.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_kb_small_mesh_2006"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_kb_small_mesh_2006")("ctd_profiles_kb_small_mesh_2006")
```

## 1001
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1001'].plot.data()
```

## 1002
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1002'].plot.data()
```

## 1003
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1003'].plot.data()
```

## 1004
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1004'].plot.data()
```

## 1005
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1005'].plot.data()
```

## 1006
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1006'].plot.data()
```

## 1007
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1007'].plot.data()
```

## 1008
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1008'].plot.data()
```

## 1009
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1009'].plot.data()
```

## 1010
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1010'].plot.data()
```

## 1011
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1011'].plot.data()
```

## 1012
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1012'].plot.data()
```

## 1013
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1013'].plot.data()
```

## 1014
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1014'].plot.data()
```

## 1015
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1015'].plot.data()
```

## 1017
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1017'].plot.data()
```

## 1018
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1018'].plot.data()
```

## 1019
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1019'].plot.data()
```

## 1020
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1020'].plot.data()
```

## 1021
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1021'].plot.data()
```

## 1022
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1022'].plot.data()
```

## 1023
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1023'].plot.data()
```

## 1024
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1024'].plot.data()
```

## 1025
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1025'].plot.data()
```

## 1026
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1026'].plot.data()
```

## 1027
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1027'].plot.data()
```

## 1028
        

```{code-cell}
:tags: [full-width, remove-input]

cat['1028'].plot.data()
```
