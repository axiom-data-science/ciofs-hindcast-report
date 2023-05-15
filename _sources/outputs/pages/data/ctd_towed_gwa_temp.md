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

# Underway CTD (GWA): Towed, temperature only

* Temperature towed 2011-2016 - GWA
* ctd_towed_gwa_temp
* Approximately monthly in summer from 2011 to 2016, 5min sampling frequency

Temperature only: Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska.

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2011-2016.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Converted some local times, ship track outside domain is not included.

<details><summary>Dataset metadata:</summary>

|    | Dataset    | featuretype   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                             |
|---:|:-----------|:--------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:------------------------------------------------------------------------------------|
|  0 | 2011-06-20 | trajectory    |       59.2073 |       -150.532 | 2011-06-20 17:40:00 |       58.8066 |       -152.133 | 2011-06-20 14:50:00 | https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv |
|  1 | 2011-07-23 | trajectory    |       59.0286 |       -150.526 | 2011-07-23 18:00:00 |       58.8215 |       -151.448 | 2011-07-23 16:25:00 | https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv |
|  2 | 2011-08-22 | trajectory    |       59.1542 |       -150.5   | 2011-08-22 18:05:00 |       58.8112 |       -152.048 | 2011-08-22 15:20:00 | https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv |
|  3 | 2012-04-09 | trajectory    |       60.58   |       -150.52  | 2012-04-10 02:05:00 |       58.82   |       -152.13  | 2012-04-09 19:30:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  4 | 2012-05-13 | trajectory    |       59.41   |       -150.52  | 2012-05-13 03:30:00 |       58.82   |       -152.14  | 2012-05-13 00:15:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  5 | 2012-06-11 | trajectory    |       59.34   |       -150.51  | 2012-06-12 03:10:00 |       58.81   |       -152.13  | 2012-06-11 23:55:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  6 | 2012-09-16 | trajectory    |       59.54   |       -150.52  | 2012-09-16 05:15:00 |       58.82   |       -152.13  | 2012-09-16 00:25:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  7 | 2012-10-16 | trajectory    |       60.5    |       -150.51  | 2012-10-16 09:45:00 |       58.81   |       -152.13  | 2012-10-16 01:50:00 | https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv |
|  8 | 2013-04-14 | trajectory    |       60.51   |       -150.53  | 2013-04-14 11:00:00 |       58.81   |       -152.13  | 2013-04-14 03:05:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
|  9 | 2013-05-13 | trajectory    |       59.73   |       -150.5   | 2013-05-14 02:15:00 |       58.81   |       -152.13  | 2013-05-13 21:35:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 10 | 2013-06-15 | trajectory    |       59.47   |       -150.52  | 2013-06-16 02:00:00 |       58.81   |       -152.13  | 2013-06-15 22:15:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 11 | 2013-07-15 | trajectory    |       59.2    |       -150.51  | 2013-07-16 02:40:00 |       58.82   |       -152.1   | 2013-07-15 23:55:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 12 | 2013-08-17 | trajectory    |       59.43   |       -150.5   | 2013-08-18 02:30:00 |       58.8    |       -152.13  | 2013-08-17 22:35:00 | https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv |
| 13 | 2014-04-27 | trajectory    |       59.22   |       -150.53  | 2014-04-27 04:20:00 |       58.82   |       -152.13  | 2014-04-27 01:00:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 14 | 2014-05-27 | trajectory    |       59.11   |       -150.51  | 2014-05-27 03:55:00 |       58.8    |       -151.99  | 2014-05-27 01:10:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 15 | 2014-06-29 | trajectory    |       59.01   |       -150.51  | 2014-06-29 04:45:00 |       58.77   |       -151.66  | 2014-06-29 02:35:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 16 | 2014-07-29 | trajectory    |       59.52   |       -150.52  | 2014-07-29 05:00:00 |       58.81   |       -152.28  | 2014-07-29 00:35:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 17 | 2014-08-31 | trajectory    |       59.05   |       -150.51  | 2014-08-31 03:50:00 |       58.82   |       -151.82  | 2014-08-31 01:40:00 | https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv |
| 18 | 2015-08-23 | trajectory    |       59.56   |       -150.5   | 2015-08-23 14:35:00 |       58.78   |       -152.13  | 2015-08-23 10:05:00 | https://researchworkspace.com/files/42202624/CPR_TemperatureData_2015_subsetted.csv |
| 19 | 2015-09-01 | trajectory    |       60.53   |       -150.5   | 2015-09-01 16:10:00 |       58.66   |       -152.13  | 2015-09-01 08:05:00 | https://researchworkspace.com/files/42202624/CPR_TemperatureData_2015_subsetted.csv |
| 20 | 2016-04-17 | trajectory    |       59.34   |       -150.53  | 2016-04-17 03:35:00 |       58.82   |       -152.16  | 2016-04-17 00:15:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 21 | 2016-05-16 | trajectory    |       59.39   |       -150.5   | 2016-05-17 03:30:00 |       58.79   |       -152.18  | 2016-05-16 23:15:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 22 | 2016-06-19 | trajectory    |       59.23   |       -150.5   | 2016-06-19 03:35:00 |       58.78   |       -152.15  | 2016-06-19 00:10:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 23 | 2016-07-19 | trajectory    |       59.07   |       -150.51  | 2016-07-19 03:50:00 |       58.8    |       -151.9   | 2016-07-19 01:05:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 24 | 2016-08-29 | trajectory    |       59.22   |       -150.52  | 2016-08-30 03:20:00 |       58.81   |       -152.14  | 2016-08-29 23:45:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |
| 25 | 2016-10-02 | trajectory    |       59.15   |       -150.5   | 2016-10-02 04:55:00 |       58.81   |       -152.03  | 2016-10-02 01:55:00 | https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv |

</details>



```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_gwa_temp"))
```

## Map of Flow through on Ship of Opportunity
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_gwa_temp")("ctd_towed_gwa_temp")
    
```

## 2011

+++

2011-06-20
        

```{code-cell}
:tags: [full-width]

cat['2011-06-20'].plot.temp()
```

2011-07-23
        

```{code-cell}
:tags: [full-width]

cat['2011-07-23'].plot.temp()
```

2011-08-22
        

```{code-cell}
:tags: [full-width]

cat['2011-08-22'].plot.temp()
```

## 2012

+++

2012-04-09
        

```{code-cell}
:tags: [full-width]

cat['2012-04-09'].plot.temp()
```

2012-05-13
        

```{code-cell}
:tags: [full-width]

cat['2012-05-13'].plot.temp()
```

2012-06-11
        

```{code-cell}
:tags: [full-width]

cat['2012-06-11'].plot.temp()
```

2012-09-16
        

```{code-cell}
:tags: [full-width]

cat['2012-09-16'].plot.temp()
```

2012-10-16
        

```{code-cell}
:tags: [full-width]

cat['2012-10-16'].plot.temp()
```

## 2013

+++

2013-04-14
        

```{code-cell}
:tags: [full-width]

cat['2013-04-14'].plot.temp()
```

2013-05-13
        

```{code-cell}
:tags: [full-width]

cat['2013-05-13'].plot.temp()
```

2013-06-15
        

```{code-cell}
:tags: [full-width]

cat['2013-06-15'].plot.temp()
```

2013-07-15
        

```{code-cell}
:tags: [full-width]

cat['2013-07-15'].plot.temp()
```

2013-08-17
        

```{code-cell}
:tags: [full-width]

cat['2013-08-17'].plot.temp()
```

## 2014

+++

2014-04-27
        

```{code-cell}
:tags: [full-width]

cat['2014-04-27'].plot.temp()
```

2014-05-27
        

```{code-cell}
:tags: [full-width]

cat['2014-05-27'].plot.temp()
```

2014-06-29
        

```{code-cell}
:tags: [full-width]

cat['2014-06-29'].plot.temp()
```

2014-07-29
        

```{code-cell}
:tags: [full-width]

cat['2014-07-29'].plot.temp()
```

2014-08-31
        

```{code-cell}
:tags: [full-width]

cat['2014-08-31'].plot.temp()
```

## 2015

+++

2015-08-23
        

```{code-cell}
:tags: [full-width]

cat['2015-08-23'].plot.temp()
```

2015-09-01
        

```{code-cell}
:tags: [full-width]

cat['2015-09-01'].plot.temp()
```

## 2016

+++

2016-04-17
        

```{code-cell}
:tags: [full-width]

cat['2016-04-17'].plot.temp()
```

2016-05-16
        

```{code-cell}
:tags: [full-width]

cat['2016-05-16'].plot.temp()
```

2016-06-19
        

```{code-cell}
:tags: [full-width]

cat['2016-06-19'].plot.temp()
```

2016-07-19
        

```{code-cell}
:tags: [full-width]

cat['2016-07-19'].plot.temp()
```

2016-08-29
        

```{code-cell}
:tags: [full-width]

cat['2016-08-29'].plot.temp()
```

2016-10-02
        

```{code-cell}
:tags: [full-width]

cat['2016-10-02'].plot.temp()
```
