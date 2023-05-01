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

# NOAA PMEL: Towed CTD on ferry at nominal 4m depth

* CTD Towed 2004-2008 Ferry in-line - NOAA PMEL
* ctd_towed_ferry_noaa_pmel
* Continuous 2004 to 2008, 5min sampling frequency


An oceanographic monitoring system aboard the Alaska Marine Highway System ferry Tustumena operated for four years in the Alaska Coastal Current (ACC) with funding from the Exxon Valdez Oil Spill Trustee Council's Gulf Ecosystem Monitoring Program, the North Pacific Research Board and the National Oceanic and Atmospheric Administration. An electronic public display aboard the ferry educated passengers about the local oceanography and mapped the ferry's progress. Sampling water at 4 m, the underway system measured: (1) temperature and salinity (used in the present report), and (2) nitrate,
(3) chlorophyll fluorescence, (4) colored dissolved organic matter fluorescence, and (5) optical beam transmittance (not used in report).

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

Dataset metadata:
|    | Dataset   | featuretype   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             |
|---:|:----------|:--------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|
|  0 | 2004-09   | trajectory    |       60.1185 |       -148.5   | 2004-09-30 21:54:00 |       57.7855 |       -152.863 | 2004-09-15 07:12:00 |
|  1 | 2004-10   | trajectory    |       60.1178 |       -148.501 | 2004-10-12 17:59:00 |       56.5761 |       -156.499 | 2004-10-01 00:18:30 |
|  2 | 2004-11   | trajectory    |       60.118  |       -148.503 | 2004-11-23 06:59:30 |       57.7867 |       -152.862 | 2004-11-08 04:57:00 |
|  3 | 2004-12   | trajectory    |       60.1183 |       -148.502 | 2004-12-30 22:56:00 |       57.789  |       -152.395 | 2004-12-01 05:25:00 |
|  4 | 2005-01   | trajectory    |       60.1185 |       -148.5   | 2005-01-31 23:59:30 |       57.7834 |       -152.863 | 2005-01-01 08:38:00 |
|  5 | 2005-02   | trajectory    |       60.1184 |       -148.501 | 2005-02-28 23:59:00 |       57.7836 |       -152.862 | 2005-02-01 00:00:00 |
|  6 | 2005-03   | trajectory    |       60.118  |       -148.501 | 2005-03-08 23:11:00 |       57.7868 |       -152.862 | 2005-03-01 00:00:00 |
|  7 | 2005-04   | trajectory    |       60.1183 |       -148.501 | 2005-04-28 23:02:30 |       56.5748 |       -156.5   | 2005-04-10 06:05:00 |
|  8 | 2005-05   | trajectory    |       60.1177 |       -148.503 | 2005-05-03 14:45:00 |       57.7868 |       -152.862 | 2005-05-02 05:21:30 |
|  9 | 2005-06   | trajectory    |       60.1188 |       -148.5   | 2005-06-30 22:57:00 |       56.571  |       -156.499 | 2005-06-08 07:34:00 |
| 10 | 2005-07   | trajectory    |       60.1189 |       -148.501 | 2005-07-31 21:15:00 |       56.5743 |       -156.499 | 2005-07-01 02:53:00 |
| 11 | 2005-08   | trajectory    |       60.1189 |       -148.502 | 2005-08-31 15:50:30 |       56.5715 |       -156.5   | 2005-08-01 02:19:30 |
| 12 | 2005-09   | trajectory    |       60.1181 |       -148.5   | 2005-09-30 21:57:00 |       57.7867 |       -153.652 | 2005-09-01 02:24:00 |
| 13 | 2005-10   | trajectory    |       59.6026 |       -151.402 | 2005-10-31 20:12:30 |       56.5791 |       -156.499 | 2005-10-01 05:43:30 |
| 14 | 2005-11   | trajectory    |       59.6424 |       -148.501 | 2005-11-16 20:41:00 |       57.7392 |       -153.482 | 2005-11-01 03:23:00 |
| 15 | 2006-05   | trajectory    |       59.6026 |       -151.402 | 2006-05-31 19:36:00 |       56.5758 |       -156.499 | 2006-05-10 18:07:30 |
| 16 | 2006-06   | trajectory    |       59.6025 |       -151.399 | 2006-06-29 14:32:30 |       56.5748 |       -156.5   | 2006-06-01 01:17:30 |
| 17 | 2006-07   | trajectory    |       59.6026 |       -151.401 | 2006-07-31 23:59:30 |       56.5737 |       -156.5   | 2006-07-03 15:46:30 |
| 18 | 2006-08   | trajectory    |       59.6026 |       -151.402 | 2006-08-31 15:59:00 |       56.5754 |       -156.499 | 2006-08-01 00:00:00 |
| 19 | 2006-09   | trajectory    |       59.6026 |       -151.401 | 2006-09-30 23:59:30 |       56.5728 |       -156.5   | 2006-09-01 02:21:30 |
| 20 | 2006-10   | trajectory    |       59.6025 |       -151.402 | 2006-10-31 22:25:30 |       56.5831 |       -156.499 | 2006-10-01 00:00:00 |
| 21 | 2006-11   | trajectory    |       59.6171 |       -151.312 | 2006-11-30 22:14:30 |       57.7867 |       -153.477 | 2006-11-01 03:21:30 |
| 22 | 2006-12   | trajectory    |       59.6059 |       -151.397 | 2006-12-31 22:20:30 |       57.7867 |       -153.474 | 2006-12-01 03:20:30 |
| 23 | 2007-01   | trajectory    |       59.6025 |       -151.404 | 2007-01-09 15:59:00 |       57.7825 |       -153.466 | 2007-01-01 03:16:30 |
| 24 | 2007-02   | trajectory    |       60.0381 |       -149.364 | 2007-02-28 17:05:30 |       57.7867 |       -153.473 | 2007-02-19 09:45:30 |
| 25 | 2007-03   | trajectory    |       59.6731 |       -151.208 | 2007-03-31 23:59:30 |       57.7867 |       -153.476 | 2007-03-01 07:18:00 |
| 26 | 2007-04   | trajectory    |       59.606  |       -151.383 | 2007-04-30 20:17:00 |       56.5775 |       -156.5   | 2007-04-01 00:00:00 |
| 27 | 2007-05   | trajectory    |       59.6031 |       -151.381 | 2007-05-31 14:06:30 |       56.576  |       -156.5   | 2007-05-01 02:42:00 |
| 28 | 2007-06   | trajectory    |       59.6027 |       -151.398 | 2007-06-28 13:59:00 |       56.5686 |       -156.499 | 2007-06-04 21:42:30 |
| 29 | 2007-07   | trajectory    |       59.6025 |       -151.402 | 2007-07-31 21:53:00 |       56.5734 |       -156.5   | 2007-07-02 23:08:00 |
| 30 | 2007-08   | trajectory    |       59.6025 |       -151.402 | 2007-08-31 20:30:00 |       56.5765 |       -156.5   | 2007-08-03 16:07:30 |
| 31 | 2007-09   | trajectory    |       59.6025 |       -151.401 | 2007-09-20 07:59:30 |       56.5883 |       -156.47  | 2007-09-01 02:26:30 |
| 32 | 2007-10   | trajectory    |       58.7303 |       -152.031 | 2007-10-01 11:59:30 |       58.5607 |       -152.12  | 2007-10-01 11:09:00 |
| 33 | 2008-03   | trajectory    |       60.8142 |       -148.5   | 2008-03-31 21:55:30 |       57.7867 |       -152.862 | 2008-03-10 18:07:00 |
| 34 | 2008-04   | trajectory    |       60.8159 |       -148.5   | 2008-04-30 22:05:30 |       57.7867 |       -152.863 | 2008-04-01 19:10:00 |
| 35 | 2008-05   | trajectory    |       59.6026 |       -151.402 | 2008-05-29 14:11:30 |       56.5747 |       -156.499 | 2008-05-01 04:51:30 |
| 36 | 2008-06   | trajectory    |       59.6025 |       -151.401 | 2008-06-30 23:59:30 |       56.5788 |       -156.499 | 2008-06-03 00:14:30 |
| 37 | 2008-07   | trajectory    |       59.6024 |       -151.4   | 2008-07-31 21:23:00 |       56.5796 |       -156.5   | 2008-07-01 00:00:00 |
| 38 | 2008-08   | trajectory    |       59.6041 |       -151.402 | 2008-08-31 21:13:00 |       56.5749 |       -156.499 | 2008-08-01 02:22:00 |
| 39 | 2008-09   | trajectory    |       59.6025 |       -151.401 | 2008-09-30 21:24:30 |       57.7867 |       -153.462 | 2008-09-01 02:20:00 |
| 40 | 2008-10   | trajectory    |       59.6026 |       -151.402 | 2008-10-31 20:22:30 |       56.5799 |       -156.498 | 2008-10-01 02:21:00 |
| 41 | 2008-11   | trajectory    |       59.6023 |       -151.402 | 2008-11-05 17:08:30 |       57.7868 |       -152.862 | 2008-11-01 02:31:30 |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_ferry_noaa_pmel"))
```

## Map of Towed CTD Paths
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_ferry_noaa_pmel")("ctd_towed_ferry_noaa_pmel")
    
```

## 2004

+++

2004-09
        

```{code-cell}
cat['2004-09'].plot.salt() + cat['2004-09'].plot.temp()
```

2004-10
        

```{code-cell}
cat['2004-10'].plot.salt() + cat['2004-10'].plot.temp()
```

2004-11
        

```{code-cell}
cat['2004-11'].plot.salt() + cat['2004-11'].plot.temp()
```

2004-12
        

```{code-cell}
cat['2004-12'].plot.salt() + cat['2004-12'].plot.temp()
```

## 2005

+++

2005-01
        

```{code-cell}
cat['2005-01'].plot.salt() + cat['2005-01'].plot.temp()
```

2005-02
        

```{code-cell}
cat['2005-02'].plot.salt() + cat['2005-02'].plot.temp()
```

2005-03
        

```{code-cell}
cat['2005-03'].plot.salt() + cat['2005-03'].plot.temp()
```

2005-04
        

```{code-cell}
cat['2005-04'].plot.salt() + cat['2005-04'].plot.temp()
```

2005-05
        

```{code-cell}
cat['2005-05'].plot.salt() + cat['2005-05'].plot.temp()
```

2005-06
        

```{code-cell}
cat['2005-06'].plot.salt() + cat['2005-06'].plot.temp()
```

2005-07
        

```{code-cell}
cat['2005-07'].plot.salt() + cat['2005-07'].plot.temp()
```

2005-08
        

```{code-cell}
cat['2005-08'].plot.salt() + cat['2005-08'].plot.temp()
```

2005-09
        

```{code-cell}
cat['2005-09'].plot.salt() + cat['2005-09'].plot.temp()
```

2005-10
        

```{code-cell}
cat['2005-10'].plot.salt() + cat['2005-10'].plot.temp()
```

2005-11
        

```{code-cell}
cat['2005-11'].plot.salt() + cat['2005-11'].plot.temp()
```

## 2006

+++

2006-05
        

```{code-cell}
cat['2006-05'].plot.salt() + cat['2006-05'].plot.temp()
```

2006-06
        

```{code-cell}
cat['2006-06'].plot.salt() + cat['2006-06'].plot.temp()
```

2006-07
        

```{code-cell}
cat['2006-07'].plot.salt() + cat['2006-07'].plot.temp()
```

2006-08
        

```{code-cell}
cat['2006-08'].plot.salt() + cat['2006-08'].plot.temp()
```

2006-09
        

```{code-cell}
cat['2006-09'].plot.salt() + cat['2006-09'].plot.temp()
```

2006-10
        

```{code-cell}
cat['2006-10'].plot.salt() + cat['2006-10'].plot.temp()
```

2006-11
        

```{code-cell}
cat['2006-11'].plot.salt() + cat['2006-11'].plot.temp()
```

2006-12
        

```{code-cell}
cat['2006-12'].plot.salt() + cat['2006-12'].plot.temp()
```

## 2007

+++

2007-01
        

```{code-cell}
cat['2007-01'].plot.salt() + cat['2007-01'].plot.temp()
```

2007-02
        

```{code-cell}
cat['2007-02'].plot.salt() + cat['2007-02'].plot.temp()
```

2007-03
        

```{code-cell}
cat['2007-03'].plot.salt() + cat['2007-03'].plot.temp()
```

2007-04
        

```{code-cell}
cat['2007-04'].plot.salt() + cat['2007-04'].plot.temp()
```

2007-05
        

```{code-cell}
cat['2007-05'].plot.salt() + cat['2007-05'].plot.temp()
```

2007-06
        

```{code-cell}
cat['2007-06'].plot.salt() + cat['2007-06'].plot.temp()
```

2007-07
        

```{code-cell}
cat['2007-07'].plot.salt() + cat['2007-07'].plot.temp()
```

2007-08
        

```{code-cell}
cat['2007-08'].plot.salt() + cat['2007-08'].plot.temp()
```

2007-09
        

```{code-cell}
cat['2007-09'].plot.salt() + cat['2007-09'].plot.temp()
```

2007-10
        

```{code-cell}
cat['2007-10'].plot.salt() + cat['2007-10'].plot.temp()
```

## 2008

+++

2008-03
        

```{code-cell}
cat['2008-03'].plot.salt() + cat['2008-03'].plot.temp()
```

2008-04
        

```{code-cell}
cat['2008-04'].plot.salt() + cat['2008-04'].plot.temp()
```

2008-05
        

```{code-cell}
cat['2008-05'].plot.salt() + cat['2008-05'].plot.temp()
```

2008-06
        

```{code-cell}
cat['2008-06'].plot.salt() + cat['2008-06'].plot.temp()
```

2008-07
        

```{code-cell}
cat['2008-07'].plot.salt() + cat['2008-07'].plot.temp()
```

2008-08
        

```{code-cell}
cat['2008-08'].plot.salt() + cat['2008-08'].plot.temp()
```

2008-09
        

```{code-cell}
cat['2008-09'].plot.salt() + cat['2008-09'].plot.temp()
```

2008-10
        

```{code-cell}
cat['2008-10'].plot.salt() + cat['2008-10'].plot.temp()
```

2008-11
        

```{code-cell}
cat['2008-11'].plot.salt() + cat['2008-11'].plot.temp()
```
