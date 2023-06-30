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

(page:ctd_towed_ferry_noaa_pmel)=
# Underway CTD (NOAA PMEL): Towed on ferry

* CTD Towed 2004-2008 Ferry in-line - NOAA PMEL
* ctd_towed_ferry_noaa_pmel
* Continuous 2004 to 2008, 5min sampling frequency


An oceanographic monitoring system aboard the Alaska Marine Highway System ferry Tustumena operated for four years in the Alaska Coastal Current (ACC) with funding from the Exxon Valdez Oil Spill Trustee Council's Gulf Ecosystem Monitoring Program, the North Pacific Research Board and the National Oceanic and Atmospheric Administration. An electronic public display aboard the ferry educated passengers about the local oceanography and mapped the ferry's progress. Sampling water at 4 m, the underway system measured: (1) temperature and salinity (used in the present report), and (2) nitrate,
(3) chlorophyll fluorescence, (4) colored dissolved organic matter fluorescence, and (5) optical beam transmittance (not used in report).

Nominal 4 meter depth.

NORTH PACIFIC RESEARCH BOARD PROJECT FINAL REPORT
Alaskan Ferry Oceanographic Monitoring in the Gulf of Alaska
NPRB Project 707 Final Report
Edward D. Cokelet and Calvin W. Mordy.
https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Final_Report_NPRB_0707.pdf

Exxon Valdez Oil Spill Gulf Ecosystem
Monitoring and Research Project Final Report
Biophysical Observations Aboard Alaska Marine Highway System Ferries
Gulf Ecosystem Monitoring and Research Project 040699
Final Report
Edward D. Cokelet, Calvin W. Mordy, Antonio J. Jenkins, W. Scott Pegau
https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Final_Report_GEM_040699.pdf

Archive: https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.nodc%3A0070122/html

![pic](https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/about/0070122_map.jpg)


The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency.

```{dropdown} Dataset metadata

|    | Dataset   | featuretype   | key_variables   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                                        |
|---:|:----------|:--------------|:----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------------------------------------|
|  0 | 2004-10   | trajectory    | []              |       60.1176 |       -148.512 | 2004-10-12 17:55:00 |       56.5869 |       -156.487 | 2004-10-01 00:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  1 | 2004-11   | trajectory    | []              |       60.1153 |       -148.503 | 2004-11-23 06:55:00 |       57.7869 |       -152.861 | 2004-11-08 04:55:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  2 | 2004-12   | trajectory    | []              |       60.1177 |       -148.51  | 2004-12-30 22:55:00 |       57.7931 |       -152.377 | 2004-12-01 05:25:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  3 | 2004-9    | trajectory    | []              |       60.118  |       -148.51  | 2004-09-30 21:50:00 |       57.787  |       -152.861 | 2004-09-15 07:10:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  4 | 2005-1    | trajectory    | []              |       60.1174 |       -148.507 | 2005-01-31 23:55:00 |       57.7841 |       -152.862 | 2005-01-01 08:35:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  5 | 2005-10   | trajectory    | []              |       59.6025 |       -151.403 | 2005-10-31 20:10:00 |       56.5857 |       -156.49  | 2005-10-01 05:40:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  6 | 2005-11   | trajectory    | []              |       59.6423 |       -148.507 | 2005-11-16 20:40:00 |       57.7401 |       -153.48  | 2005-11-01 03:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  7 | 2005-2    | trajectory    | []              |       60.1183 |       -148.51  | 2005-02-28 23:55:00 |       57.7838 |       -152.862 | 2005-02-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  8 | 2005-3    | trajectory    | []              |       60.1173 |       -148.529 | 2005-03-08 23:10:00 |       57.7868 |       -152.86  | 2005-03-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
|  9 | 2005-4    | trajectory    | []              |       60.1166 |       -148.521 | 2005-04-28 23:00:00 |       56.5825 |       -156.494 | 2005-04-10 06:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 10 | 2005-5    | trajectory    | []              |       60.1161 |       -148.531 | 2005-05-03 14:45:00 |       57.787  |       -152.861 | 2005-05-02 05:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 11 | 2005-6    | trajectory    | []              |       60.1188 |       -148.5   | 2005-06-30 22:55:00 |       56.5725 |       -156.496 | 2005-06-08 07:30:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 12 | 2005-7    | trajectory    | []              |       60.1184 |       -148.512 | 2005-07-31 21:15:00 |       56.5772 |       -156.494 | 2005-07-01 02:50:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 13 | 2005-8    | trajectory    | []              |       60.1181 |       -148.51  | 2005-08-31 15:50:00 |       56.5715 |       -156.5   | 2005-08-01 02:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 14 | 2005-9    | trajectory    | []              |       60.1178 |       -148.511 | 2005-09-30 21:55:00 |       57.7869 |       -153.645 | 2005-09-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 15 | 2006-10   | trajectory    | []              |       59.6025 |       -151.403 | 2006-10-31 22:25:00 |       56.5905 |       -156.485 | 2006-10-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 16 | 2006-11   | trajectory    | []              |       59.6169 |       -151.317 | 2006-11-30 22:10:00 |       57.7867 |       -153.477 | 2006-11-01 03:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 17 | 2006-12   | trajectory    | []              |       59.6056 |       -151.399 | 2006-12-31 22:20:00 |       57.7868 |       -153.473 | 2006-12-01 03:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 18 | 2006-5    | trajectory    | []              |       59.6025 |       -151.402 | 2006-05-31 19:35:00 |       56.5865 |       -156.479 | 2006-05-10 18:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 19 | 2006-6    | trajectory    | []              |       59.6025 |       -151.402 | 2006-06-29 14:30:00 |       56.58   |       -156.497 | 2006-06-01 01:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 20 | 2006-7    | trajectory    | []              |       59.6024 |       -151.402 | 2006-07-31 23:55:00 |       56.579  |       -156.495 | 2006-07-03 15:45:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 21 | 2006-8    | trajectory    | []              |       59.6026 |       -151.402 | 2006-08-31 15:55:00 |       56.583  |       -156.493 | 2006-08-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 22 | 2006-9    | trajectory    | []              |       59.6025 |       -151.401 | 2006-09-30 23:55:00 |       56.5744 |       -156.497 | 2006-09-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 23 | 2007-1    | trajectory    | []              |       59.6024 |       -151.404 | 2007-01-09 15:55:00 |       57.7828 |       -153.466 | 2007-01-01 03:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 24 | 2007-10   | trajectory    | []              |       58.7269 |       -152.039 | 2007-10-01 11:55:00 |       58.5762 |       -152.118 | 2007-10-01 11:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 25 | 2007-2    | trajectory    | []              |       60.0201 |       -149.372 | 2007-02-28 17:05:00 |       57.7867 |       -153.468 | 2007-02-19 09:45:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 26 | 2007-3    | trajectory    | []              |       59.6731 |       -151.211 | 2007-03-31 23:55:00 |       57.7867 |       -153.476 | 2007-03-01 07:15:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 27 | 2007-4    | trajectory    | []              |       59.6028 |       -151.388 | 2007-04-30 20:15:00 |       56.5819 |       -156.492 | 2007-04-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 28 | 2007-5    | trajectory    | []              |       59.6025 |       -151.382 | 2007-05-31 14:05:00 |       56.5826 |       -156.494 | 2007-05-01 02:40:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 29 | 2007-6    | trajectory    | []              |       59.6027 |       -151.401 | 2007-06-28 13:55:00 |       56.576  |       -156.498 | 2007-06-04 21:40:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 30 | 2007-7    | trajectory    | []              |       59.6025 |       -151.403 | 2007-07-31 21:50:00 |       56.581  |       -156.494 | 2007-07-02 23:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 31 | 2007-8    | trajectory    | []              |       59.6023 |       -151.402 | 2007-08-31 20:30:00 |       56.5844 |       -156.497 | 2007-08-03 16:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 32 | 2007-9    | trajectory    | []              |       59.6025 |       -151.401 | 2007-09-20 07:55:00 |       56.598  |       -156.453 | 2007-09-01 02:25:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 33 | 2008-10   | trajectory    | []              |       59.6023 |       -151.402 | 2008-10-31 20:20:00 |       56.5825 |       -156.496 | 2008-10-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 34 | 2008-11   | trajectory    | []              |       59.6023 |       -151.404 | 2008-11-05 17:05:00 |       57.7868 |       -152.862 | 2008-11-01 02:30:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 35 | 2008-3    | trajectory    | []              |       60.814  |       -148.501 | 2008-03-31 21:55:00 |       57.7868 |       -152.862 | 2008-03-10 18:05:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 36 | 2008-4    | trajectory    | []              |       60.8154 |       -148.5   | 2008-04-30 22:05:00 |       57.7868 |       -152.862 | 2008-04-01 19:10:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 37 | 2008-5    | trajectory    | []              |       59.6025 |       -151.402 | 2008-05-29 14:10:00 |       56.5776 |       -156.494 | 2008-05-01 04:50:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 38 | 2008-6    | trajectory    | []              |       59.6025 |       -151.402 | 2008-06-30 23:55:00 |       56.5844 |       -156.496 | 2008-06-03 00:10:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 39 | 2008-7    | trajectory    | []              |       59.6023 |       -151.401 | 2008-07-31 21:20:00 |       56.5831 |       -156.5   | 2008-07-01 00:00:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 40 | 2008-8    | trajectory    | []              |       59.6033 |       -151.403 | 2008-08-31 21:10:00 |       56.5826 |       -156.494 | 2008-08-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |
| 41 | 2008-9    | trajectory    | []              |       59.6025 |       -151.402 | 2008-09-30 21:20:00 |       57.7868 |       -153.462 | 2008-09-01 02:20:00 | https://researchworkspace.com/files/42202265/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_ferry_noaa_pmel"))
```

## Map of Towed CTD Paths
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_towed_ferry_noaa_pmel")("ctd_towed_ferry_noaa_pmel")
```

## 2004

+++

2004-10
        

```{code-cell}
:tags: [remove-input]

cat['2004-10'].plot.salt() + cat['2004-10'].plot.temp()
```

2004-11
        

```{code-cell}
:tags: [remove-input]

cat['2004-11'].plot.salt() + cat['2004-11'].plot.temp()
```

2004-12
        

```{code-cell}
:tags: [remove-input]

cat['2004-12'].plot.salt() + cat['2004-12'].plot.temp()
```

2004-9
        

```{code-cell}
:tags: [remove-input]

cat['2004-9'].plot.salt() + cat['2004-9'].plot.temp()
```

## 2005

+++

2005-1
        

```{code-cell}
:tags: [remove-input]

cat['2005-1'].plot.salt() + cat['2005-1'].plot.temp()
```

2005-10
        

```{code-cell}
:tags: [remove-input]

cat['2005-10'].plot.salt() + cat['2005-10'].plot.temp()
```

2005-11
        

```{code-cell}
:tags: [remove-input]

cat['2005-11'].plot.salt() + cat['2005-11'].plot.temp()
```

2005-2
        

```{code-cell}
:tags: [remove-input]

cat['2005-2'].plot.salt() + cat['2005-2'].plot.temp()
```

2005-3
        

```{code-cell}
:tags: [remove-input]

cat['2005-3'].plot.salt() + cat['2005-3'].plot.temp()
```

2005-4
        

```{code-cell}
:tags: [remove-input]

cat['2005-4'].plot.salt() + cat['2005-4'].plot.temp()
```

2005-5
        

```{code-cell}
:tags: [remove-input]

cat['2005-5'].plot.salt() + cat['2005-5'].plot.temp()
```

2005-6
        

```{code-cell}
:tags: [remove-input]

cat['2005-6'].plot.salt() + cat['2005-6'].plot.temp()
```

2005-7
        

```{code-cell}
:tags: [remove-input]

cat['2005-7'].plot.salt() + cat['2005-7'].plot.temp()
```

2005-8
        

```{code-cell}
:tags: [remove-input]

cat['2005-8'].plot.salt() + cat['2005-8'].plot.temp()
```

2005-9
        

```{code-cell}
:tags: [remove-input]

cat['2005-9'].plot.salt() + cat['2005-9'].plot.temp()
```

## 2006

+++

2006-10
        

```{code-cell}
:tags: [remove-input]

cat['2006-10'].plot.salt() + cat['2006-10'].plot.temp()
```

2006-11
        

```{code-cell}
:tags: [remove-input]

cat['2006-11'].plot.salt() + cat['2006-11'].plot.temp()
```

2006-12
        

```{code-cell}
:tags: [remove-input]

cat['2006-12'].plot.salt() + cat['2006-12'].plot.temp()
```

2006-5
        

```{code-cell}
:tags: [remove-input]

cat['2006-5'].plot.salt() + cat['2006-5'].plot.temp()
```

2006-6
        

```{code-cell}
:tags: [remove-input]

cat['2006-6'].plot.salt() + cat['2006-6'].plot.temp()
```

2006-7
        

```{code-cell}
:tags: [remove-input]

cat['2006-7'].plot.salt() + cat['2006-7'].plot.temp()
```

2006-8
        

```{code-cell}
:tags: [remove-input]

cat['2006-8'].plot.salt() + cat['2006-8'].plot.temp()
```

2006-9
        

```{code-cell}
:tags: [remove-input]

cat['2006-9'].plot.salt() + cat['2006-9'].plot.temp()
```

## 2007

+++

2007-1
        

```{code-cell}
:tags: [remove-input]

cat['2007-1'].plot.salt() + cat['2007-1'].plot.temp()
```

2007-10
        

```{code-cell}
:tags: [remove-input]

cat['2007-10'].plot.salt() + cat['2007-10'].plot.temp()
```

2007-2
        

```{code-cell}
:tags: [remove-input]

cat['2007-2'].plot.salt() + cat['2007-2'].plot.temp()
```

2007-3
        

```{code-cell}
:tags: [remove-input]

cat['2007-3'].plot.salt() + cat['2007-3'].plot.temp()
```

2007-4
        

```{code-cell}
:tags: [remove-input]

cat['2007-4'].plot.salt() + cat['2007-4'].plot.temp()
```

2007-5
        

```{code-cell}
:tags: [remove-input]

cat['2007-5'].plot.salt() + cat['2007-5'].plot.temp()
```

2007-6
        

```{code-cell}
:tags: [remove-input]

cat['2007-6'].plot.salt() + cat['2007-6'].plot.temp()
```

2007-7
        

```{code-cell}
:tags: [remove-input]

cat['2007-7'].plot.salt() + cat['2007-7'].plot.temp()
```

2007-8
        

```{code-cell}
:tags: [remove-input]

cat['2007-8'].plot.salt() + cat['2007-8'].plot.temp()
```

2007-9
        

```{code-cell}
:tags: [remove-input]

cat['2007-9'].plot.salt() + cat['2007-9'].plot.temp()
```

## 2008

+++

2008-10
        

```{code-cell}
:tags: [remove-input]

cat['2008-10'].plot.salt() + cat['2008-10'].plot.temp()
```

2008-11
        

```{code-cell}
:tags: [remove-input]

cat['2008-11'].plot.salt() + cat['2008-11'].plot.temp()
```

2008-3
        

```{code-cell}
:tags: [remove-input]

cat['2008-3'].plot.salt() + cat['2008-3'].plot.temp()
```

2008-4
        

```{code-cell}
:tags: [remove-input]

cat['2008-4'].plot.salt() + cat['2008-4'].plot.temp()
```

2008-5
        

```{code-cell}
:tags: [remove-input]

cat['2008-5'].plot.salt() + cat['2008-5'].plot.temp()
```

2008-6
        

```{code-cell}
:tags: [remove-input]

cat['2008-6'].plot.salt() + cat['2008-6'].plot.temp()
```

2008-7
        

```{code-cell}
:tags: [remove-input]

cat['2008-7'].plot.salt() + cat['2008-7'].plot.temp()
```

2008-8
        

```{code-cell}
:tags: [remove-input]

cat['2008-8'].plot.salt() + cat['2008-8'].plot.temp()
```

2008-9
        

```{code-cell}
:tags: [remove-input]

cat['2008-9'].plot.salt() + cat['2008-9'].plot.temp()
```
