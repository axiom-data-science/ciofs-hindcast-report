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
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.418 | 2004-05-21T10:34:00.000000000 |        60.716 |       -151.683 | 2004-05-21T09:23:00.000000000 |


```{code-cell}
cat['Cruise-01_2004-05-21'].plot.salt() + cat['Cruise-01_2004-05-21'].plot.temp()
```

Cruise-02_2004-06-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.417 | 2004-06-24T09:08:00.000000000 |        60.716 |       -151.683 | 2004-06-24T07:07:00.000000000 |


```{code-cell}
cat['Cruise-02_2004-06-24'].plot.salt() + cat['Cruise-02_2004-06-24'].plot.temp()
```

Cruise-03_2004-08-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.718 |       -151.417 | 2004-08-08T09:20:00.000000000 |        60.716 |       -151.683 | 2004-08-08T07:55:00.000000000 |


```{code-cell}
cat['Cruise-03_2004-08-08'].plot.salt() + cat['Cruise-03_2004-08-08'].plot.temp()
```

Cruise-04_2004-09-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.718 |       -151.417 | 2004-09-17T08:25:00.000000000 |        60.715 |       -151.684 | 2004-09-17T07:00:00.000000000 |


```{code-cell}
cat['Cruise-04_2004-09-17'].plot.salt() + cat['Cruise-04_2004-09-17'].plot.temp()
```

Cruise-05_2004-10-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.417 | 2004-10-09T14:37:00.000000000 |        60.713 |       -151.683 | 2004-10-09T13:21:00.000000000 |


```{code-cell}
cat['Cruise-05_2004-10-09'].plot.salt() + cat['Cruise-05_2004-10-09'].plot.temp()
```

## 2005

+++

Cruise-06_2005-03-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |         60.72 |        -151.45 | 2005-03-30T12:49:00.000000000 |         60.72 |        -151.65 | 2005-03-30T11:22:00.000000000 |


```{code-cell}
cat['Cruise-06_2005-03-30'].plot.salt() + cat['Cruise-06_2005-03-30'].plot.temp()
```

Cruise-07_2005-05-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.417 | 2005-05-02T12:32:00.000000000 |        60.715 |       -151.683 | 2005-05-02T11:13:00.000000000 |


```{code-cell}
cat['Cruise-07_2005-05-02'].plot.salt() + cat['Cruise-07_2005-05-02'].plot.temp()
```

Cruise-08_2005-06-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.417 | 2005-06-01T13:23:00.000000000 |        60.715 |       -151.683 | 2005-06-01T12:03:00.000000000 |


```{code-cell}
cat['Cruise-08_2005-06-01'].plot.salt() + cat['Cruise-08_2005-06-01'].plot.temp()
```

Cruise-09_2005-08-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.417 | 2005-08-26T11:08:00.000000000 |        60.715 |       -151.683 | 2005-08-26T09:35:00.000000000 |


```{code-cell}
cat['Cruise-09_2005-08-26'].plot.salt() + cat['Cruise-09_2005-08-26'].plot.temp()
```

Cruise-10_2005-10-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        60.717 |       -151.417 | 2005-10-03T18:50:00.000000000 |        60.716 |       -151.684 | 2005-10-03T17:39:00.000000000 |


```{code-cell}
cat['Cruise-10_2005-10-03'].plot.salt() + cat['Cruise-10_2005-10-03'].plot.temp()
```
