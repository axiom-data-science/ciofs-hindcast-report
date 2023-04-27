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

# CMI KBNERR: Six repeat transects, one single transect, and one time series of CTD profiles in Cook Inlet

* CTD profiles 2004-2006 - CMI KBNERR
* ctd_profiles_cmi_kbnerr
* From 2004 to 2006

Seasonality of Boundary Conditions for Cook Inlet, Alaska

During 2004 to 2006 we collected hydrographic measurements along transect lines crossing: 1) Kennedy Entrance and Stevenson Entrance from Port Chatham to Shuyak Island; 2) Shelikof Strait from Shuyak Island to Cape Douglas; 3) Cook Inlet from Red River to Anchor Point; 4) Kachemak Bay from Barbara Point to Bluff Point, and 5) the Forelands from East Foreland to West Foreland. During the third year we added two additional lines; 6) Cape Douglas to Cape Adams, and 7) Magnet Rock to Mount Augustine. The sampling in 2006 focused on the differences in properties during the spring and neap tide periods.

CTD profiles 2004-2005 - CMI UAF seems to be transect 5 of this project.

Note
Line 4 has an incorrect latitude for station 65. This can be seen with the following if the correction is not made:
```
df = cat['cmi_full_v2-Cruise_16-Line_4'].read()
df.drop_duplicates(subset="Station")
```
because the longitude is fixed and the latitude increases linearly until station 65 and then repeats the latitude value of station 56. The values are the same for the line in all datasets, and in the report. Since the difference in latitude across line 4 is about 0.0167, I will apply that difference from station 64 and use the resulting latitude for line 4, station 65.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>


Used in the NWGOA model/data comparison.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_cmi_kbnerr"))
```

## Map of CTD Profiles in Transects
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_cmi_kbnerr")("ctd_profiles_cmi_kbnerr")
    
```

## Kbay_timeseries

+++

Kbay_timeseries
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.5833 |        -151.75 | 2006-04-23T17:33:00.000000000 |       59.5833 |        -151.75 | 2006-04-22T17:06:00.000000000 |


```{code-cell}
cat['Kbay_timeseries'].plot.salt() + cat['Kbay_timeseries'].plot.temp()
```

## Cruise_00

+++

cmi_full_v2-Cruise_00-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.4917 |        -151.65 | 2004-03-13T12:41:00.000000000 |       59.4917 |        -151.65 | 2004-03-13T12:41:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_00-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_00-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_00-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2004-03-13T12:27:00.000000000 |       59.5083 |        -151.65 | 2004-03-13T10:40:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_00-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_00-Line_4'].plot.temp()
```

## Cruise_01

+++

cmi_full_v2-Cruise_01-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2004-04-20T18:20:00.000000000 |         58.65 |       -152.333 | 2004-04-20T08:45:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2004-04-19T23:10:00.000000000 |       58.6133 |       -152.817 | 2004-04-19T20:37:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.9967 |        -151.65 | 2004-05-27T05:46:00.000000000 |       59.4917 |       -152.537 | 2004-04-18T21:36:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2004-05-27T08:04:00.000000000 |       59.5083 |        -151.65 | 2004-04-21T07:29:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_4'].plot.temp()
```

## Cruise_02

+++

cmi_full_v2-Cruise_02-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2004-05-26T21:07:00.000000000 |         58.65 |       -152.333 | 2004-05-26T11:50:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2004-05-26T09:39:00.000000000 |       58.6133 |       -152.817 | 2004-05-26T07:18:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.9967 |        -151.65 | 2004-05-27T05:46:00.000000000 |       59.4917 |       -152.537 | 2004-05-25T11:41:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2004-05-27T08:04:00.000000000 |       59.5169 |        -151.65 | 2004-05-27T05:59:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_4'].plot.temp()
```

## Cruise_03

+++

cmi_full_v2-Cruise_03-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2004-06-13T20:35:00.000000000 |         58.65 |       -152.333 | 2004-06-13T11:34:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2004-06-14T00:10:00.000000000 |       58.6133 |       -152.817 | 2004-06-13T22:11:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.9967 |        -151.65 | 2004-06-14T23:46:00.000000000 |       59.4917 |       -152.537 | 2004-06-14T13:39:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.6417 |        -151.65 | 2004-06-15T02:01:00.000000000 |       59.5083 |        -151.65 | 2004-06-14T23:59:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_4'].plot.temp()
```

## Cruise_04

+++

cmi_full_v2-Cruise_04-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2004-07-18T11:34:00.000000000 |        58.735 |       -152.267 | 2004-07-18T11:34:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        58.665 |       -152.633 | 2004-07-18T22:46:00.000000000 |       58.6133 |       -152.767 | 2004-07-18T22:11:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.9567 |        -151.65 | 2004-07-18T23:46:00.000000000 |       59.4917 |       -152.422 | 2004-07-17T13:24:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2004-07-18T23:46:00.000000000 |        59.525 |        -151.65 | 2004-07-18T23:46:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_4'].plot.temp()
```

## Cruise_05

+++

cmi_full_v2-Cruise_05-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2004-09-11T03:19:00.000000000 |         58.65 |       -152.333 | 2004-08-17T13:00:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2004-08-17T08:13:00.000000000 |       58.6133 |       -152.817 | 2004-08-17T06:26:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.9967 |        -151.65 | 2004-08-18T04:09:00.000000000 |       59.4917 |       -152.537 | 2004-08-16T10:22:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.6417 |        -151.65 | 2004-08-18T06:08:00.000000000 |       59.5083 |        -151.65 | 2004-08-18T04:21:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_4'].plot.temp()
```

## Cruise_06

+++

cmi_full_v2-Cruise_06-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2004-09-08T09:39:00.000000000 |         58.65 |       -152.333 | 2004-09-07T23:19:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2004-09-08T16:41:00.000000000 |       58.6133 |       -152.817 | 2004-09-08T14:33:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.9967 |        -151.65 | 2004-09-09T20:24:00.000000000 |       59.4917 |       -152.537 | 2004-09-09T09:03:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.6417 |        -151.65 | 2004-09-09T20:03:00.000000000 |       59.5083 |        -151.65 | 2004-09-09T17:54:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_4'].plot.temp()
```

## Cruise_07

+++

cmi_full_v2-Cruise_07-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2005-01-09T06:16:00.000000000 |         58.65 |       -152.333 | 2005-01-08T19:06:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2005-01-09T10:39:00.000000000 |       58.6133 |       -152.817 | 2005-01-09T08:10:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2005-01-10T09:01:00.000000000 |       59.7717 |       -152.567 | 2005-01-10T03:07:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2005-01-10T14:03:00.000000000 |       59.4917 |        -151.65 | 2005-01-10T11:04:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_4'].plot.temp()
```

## Cruise_08

+++

cmi_full_v2-Cruise_08-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2005-04-26T07:23:00.000000000 |         58.65 |       -152.333 | 2005-04-25T20:05:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2005-04-26T14:45:00.000000000 |       58.6133 |       -152.817 | 2005-04-26T12:43:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2005-04-27T10:50:00.000000000 |       59.7717 |       -152.567 | 2005-04-27T04:33:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2005-04-25T17:42:00.000000000 |       59.4917 |        -151.65 | 2005-04-25T14:49:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_4'].plot.temp()
```

## Cruise_09

+++

cmi_full_v2-Cruise_09-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2005-06-14T18:18:00.000000000 |         58.65 |       -152.333 | 2005-06-14T10:26:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2005-06-15T01:24:00.000000000 |       58.6133 |       -152.817 | 2005-06-14T23:37:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2005-06-15T20:28:00.000000000 |       59.7717 |       -152.567 | 2005-06-15T15:55:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2005-06-16T20:48:00.000000000 |       59.4917 |        -151.65 | 2005-06-16T18:46:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_4'].plot.temp()
```

## Cruise_10

+++

cmi_full_v2-Cruise_10-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2005-07-30T06:56:00.000000000 |         58.65 |       -152.333 | 2005-07-29T17:13:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2005-07-29T12:14:00.000000000 |       58.6133 |       -152.817 | 2005-07-29T10:43:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2005-07-28T17:57:00.000000000 |       59.7717 |       -152.567 | 2005-07-28T11:09:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2005-07-30T18:02:00.000000000 |       59.4917 |        -151.65 | 2005-07-30T16:08:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_4'].plot.temp()
```

## Cruise_11

+++

cmi_full_v2-Cruise_11-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2005-09-05T02:18:00.000000000 |         58.65 |       -152.333 | 2005-09-04T18:41:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2005-09-05T12:13:00.000000000 |       58.6133 |       -152.817 | 2005-09-05T10:42:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2005-09-06T08:02:00.000000000 |       59.7717 |       -152.567 | 2005-09-06T02:46:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2005-09-06T11:29:00.000000000 |       59.4917 |        -151.65 | 2005-09-06T09:35:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_4'].plot.temp()
```

## Cruise_12

+++

cmi_full_v2-Cruise_12-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2005-10-13T22:35:00.000000000 |         58.65 |       -152.333 | 2005-10-13T15:26:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2005-10-14T01:40:00.000000000 |       58.6133 |       -152.817 | 2005-10-14T00:06:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2005-10-14T19:04:00.000000000 |       59.7717 |       -152.567 | 2005-10-14T14:47:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2005-10-14T22:50:00.000000000 |       59.4917 |        -151.65 | 2005-10-14T20:44:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_4'].plot.temp()
```

## Cruise_13

+++

cmi_full_v2-Cruise_13-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2006-07-27T02:55:00.000000000 |         58.65 |       -152.333 | 2006-07-26T19:07:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.987 | 2006-07-26T03:26:00.000000000 |         59.81 |       -152.567 | 2006-07-26T00:02:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2006-07-28T14:32:00.000000000 |       59.4917 |        -151.65 | 2006-07-28T12:41:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_6
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2117 |       -151.925 | 2006-07-28T02:39:00.000000000 |        58.865 |        -153.24 | 2006-07-27T16:41:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_7
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |         59.35 |           -152 | 2006-07-26T16:48:00.000000000 |       59.3083 |       -153.302 | 2006-07-26T09:08:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_7'].plot.temp()
```

## Cruise_14

+++

cmi_full_v2-Cruise_14-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2006-08-06T10:16:00.000000000 |         58.65 |       -152.333 | 2006-08-06T03:41:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2006-08-06T19:17:00.000000000 |       58.6133 |       -152.817 | 2006-08-06T17:40:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2006-08-05T14:02:00.000000000 |       59.7717 |       -152.567 | 2006-08-05T10:04:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2006-08-07T14:57:00.000000000 |       59.4917 |        -151.65 | 2006-08-07T13:11:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_6
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2117 |       -151.925 | 2006-08-07T08:22:00.000000000 |        58.865 |        -153.24 | 2006-08-06T23:14:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_7
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.355 |           -152 | 2006-08-06T02:06:00.000000000 |       59.3083 |       -153.302 | 2006-08-05T19:22:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_7'].plot.temp()
```

## Cruise_15

+++

cmi_full_v2-Cruise_15-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2006-08-13T02:41:00.000000000 |         58.65 |       -152.333 | 2006-08-12T19:38:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2006-08-12T04:36:00.000000000 |       59.7717 |       -152.567 | 2006-08-12T00:23:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2006-08-14T13:27:00.000000000 |       59.4917 |        -151.65 | 2006-08-14T11:46:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_6
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2117 |       -151.925 | 2006-08-14T03:21:00.000000000 |        58.865 |        -153.24 | 2006-08-13T17:40:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_7
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.355 |           -152 | 2006-08-12T17:34:00.000000000 |       59.3083 |       -153.302 | 2006-08-12T10:17:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_7'].plot.temp()
```

## Cruise_16

+++

cmi_full_v2-Cruise_16-Line_1
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2033 |       -151.875 | 2006-09-12T13:16:00.000000000 |         58.65 |       -152.333 | 2006-09-12T06:48:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_2
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6867 |       -152.633 | 2006-09-13T01:43:00.000000000 |       58.6133 |       -152.817 | 2006-09-13T00:12:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_3
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       60.0067 |       -151.883 | 2006-09-11T16:22:00.000000000 |       59.7717 |       -152.567 | 2006-09-11T12:16:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_4
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.625 |        -151.65 | 2006-09-13T19:04:00.000000000 |       59.4917 |        -151.65 | 2006-09-13T17:18:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_6
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.2117 |       -151.925 | 2006-09-13T15:03:00.000000000 |        58.865 |        -153.24 | 2006-09-13T06:13:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_7
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.355 |           -152 | 2006-09-12T05:27:00.000000000 |       59.3083 |       -153.302 | 2006-09-11T22:06:00.000000000 |


```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_7'].plot.temp()
```

## sue_shelikof

+++

sue_shelikof
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       58.6133 |       -152.633 | 2006-09-12T22:04:00.000000000 |       58.3505 |       -152.898 | 2006-09-12T19:41:00.000000000 |


```{code-cell}
cat['sue_shelikof'].plot.salt() + cat['sue_shelikof'].plot.temp()
```
