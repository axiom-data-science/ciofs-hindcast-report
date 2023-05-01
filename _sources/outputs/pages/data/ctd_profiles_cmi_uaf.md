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

# CMI UAF: CTD transect from East Foreland Lighthouse in Cook Inlet

* CTD profiles 2004-2005 - CMI UAF
* ctd_profiles_cmi_uaf
* 10 cruises, approximately monthly for summer months, in 2004 and 2005

Seasonality of Boundary Conditions for Cook Inlet, Alaska: Transect (3) at East Foreland Lighthouse.

9 CTD profiles at stations across 10 cruises in (approximately) the same locations. Approximately monthly for summer months, 2004 and 2005.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf


Used in the NWGOA model/data comparison.

Dataset metadata:
|    | Dataset              | featuretype       |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             |
|---:|:---------------------|:------------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|
|  0 | Cruise-01_2004-05-21 | trajectoryProfile |        60.717 |       -151.418 | 2004-05-21 10:34:00 |        60.716 |       -151.683 | 2004-05-21 09:23:00 |
|  1 | Cruise-02_2004-06-24 | trajectoryProfile |        60.717 |       -151.417 | 2004-06-24 09:08:00 |        60.716 |       -151.683 | 2004-06-24 07:07:00 |
|  2 | Cruise-03_2004-08-08 | trajectoryProfile |        60.718 |       -151.417 | 2004-08-08 09:20:00 |        60.716 |       -151.683 | 2004-08-08 07:55:00 |
|  3 | Cruise-04_2004-09-17 | trajectoryProfile |        60.718 |       -151.417 | 2004-09-17 08:25:00 |        60.715 |       -151.684 | 2004-09-17 07:00:00 |
|  4 | Cruise-05_2004-10-09 | trajectoryProfile |        60.717 |       -151.417 | 2004-10-09 14:37:00 |        60.713 |       -151.683 | 2004-10-09 13:21:00 |
|  5 | Cruise-06_2005-03-30 | trajectoryProfile |        60.72  |       -151.45  | 2005-03-30 12:49:00 |        60.72  |       -151.65  | 2005-03-30 11:22:00 |
|  6 | Cruise-07_2005-05-02 | trajectoryProfile |        60.717 |       -151.417 | 2005-05-02 12:32:00 |        60.715 |       -151.683 | 2005-05-02 11:13:00 |
|  7 | Cruise-08_2005-06-01 | trajectoryProfile |        60.717 |       -151.417 | 2005-06-01 13:23:00 |        60.715 |       -151.683 | 2005-06-01 12:03:00 |
|  8 | Cruise-09_2005-08-26 | trajectoryProfile |        60.717 |       -151.417 | 2005-08-26 11:08:00 |        60.715 |       -151.683 | 2005-08-26 09:35:00 |
|  9 | Cruise-10_2005-10-03 | trajectoryProfile |        60.717 |       -151.417 | 2005-10-03 18:50:00 |        60.716 |       -151.684 | 2005-10-03 17:39:00 |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_cmi_uaf"))
```

## Map of CTD Profiles in a Transect
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_cmi_uaf")("ctd_profiles_cmi_uaf")
    
```

## 2004

+++

Cruise-01_2004-05-21
        

```{code-cell}
cat['Cruise-01_2004-05-21'].plot.salt() + cat['Cruise-01_2004-05-21'].plot.temp()
```

Cruise-02_2004-06-24
        

```{code-cell}
cat['Cruise-02_2004-06-24'].plot.salt() + cat['Cruise-02_2004-06-24'].plot.temp()
```

Cruise-03_2004-08-08
        

```{code-cell}
cat['Cruise-03_2004-08-08'].plot.salt() + cat['Cruise-03_2004-08-08'].plot.temp()
```

Cruise-04_2004-09-17
        

```{code-cell}
cat['Cruise-04_2004-09-17'].plot.salt() + cat['Cruise-04_2004-09-17'].plot.temp()
```

Cruise-05_2004-10-09
        

```{code-cell}
cat['Cruise-05_2004-10-09'].plot.salt() + cat['Cruise-05_2004-10-09'].plot.temp()
```

## 2005

+++

Cruise-06_2005-03-30
        

```{code-cell}
cat['Cruise-06_2005-03-30'].plot.salt() + cat['Cruise-06_2005-03-30'].plot.temp()
```

Cruise-07_2005-05-02
        

```{code-cell}
cat['Cruise-07_2005-05-02'].plot.salt() + cat['Cruise-07_2005-05-02'].plot.temp()
```

Cruise-08_2005-06-01
        

```{code-cell}
cat['Cruise-08_2005-06-01'].plot.salt() + cat['Cruise-08_2005-06-01'].plot.temp()
```

Cruise-09_2005-08-26
        

```{code-cell}
cat['Cruise-09_2005-08-26'].plot.salt() + cat['Cruise-09_2005-08-26'].plot.temp()
```

Cruise-10_2005-10-03
        

```{code-cell}
cat['Cruise-10_2005-10-03'].plot.salt() + cat['Cruise-10_2005-10-03'].plot.temp()
```
