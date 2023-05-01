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

Dataset metadata:
|    | Dataset                      | featuretype       |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             |
|---:|:-----------------------------|:------------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|
|  0 | Kbay_timeseries              | trajectoryProfile |       59.5833 |       -151.75  | 2006-04-23 17:33:00 |       59.5833 |       -151.75  | 2006-04-22 17:06:00 |
|  1 | cmi_full_v2-Cruise_00-Line_3 | trajectoryProfile |       59.4917 |       -151.65  | 2004-03-13 12:41:00 |       59.4917 |       -151.65  | 2004-03-13 12:41:00 |
|  2 | cmi_full_v2-Cruise_00-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2004-03-13 12:27:00 |       59.5083 |       -151.65  | 2004-03-13 10:40:00 |
|  3 | cmi_full_v2-Cruise_01-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2004-04-20 18:20:00 |       58.65   |       -152.333 | 2004-04-20 08:45:00 |
|  4 | cmi_full_v2-Cruise_01-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2004-04-19 23:10:00 |       58.6133 |       -152.817 | 2004-04-19 20:37:00 |
|  5 | cmi_full_v2-Cruise_01-Line_3 | trajectoryProfile |       59.9967 |       -151.65  | 2004-05-27 05:46:00 |       59.4917 |       -152.537 | 2004-04-18 21:36:00 |
|  6 | cmi_full_v2-Cruise_01-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2004-05-27 08:04:00 |       59.5083 |       -151.65  | 2004-04-21 07:29:00 |
|  7 | cmi_full_v2-Cruise_02-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2004-05-26 21:07:00 |       58.65   |       -152.333 | 2004-05-26 11:50:00 |
|  8 | cmi_full_v2-Cruise_02-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2004-05-26 09:39:00 |       58.6133 |       -152.817 | 2004-05-26 07:18:00 |
|  9 | cmi_full_v2-Cruise_02-Line_3 | trajectoryProfile |       59.9967 |       -151.65  | 2004-05-27 05:46:00 |       59.4917 |       -152.537 | 2004-05-25 11:41:00 |
| 10 | cmi_full_v2-Cruise_02-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2004-05-27 08:04:00 |       59.5169 |       -151.65  | 2004-05-27 05:59:00 |
| 11 | cmi_full_v2-Cruise_03-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2004-06-13 20:35:00 |       58.65   |       -152.333 | 2004-06-13 11:34:00 |
| 12 | cmi_full_v2-Cruise_03-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2004-06-14 00:10:00 |       58.6133 |       -152.817 | 2004-06-13 22:11:00 |
| 13 | cmi_full_v2-Cruise_03-Line_3 | trajectoryProfile |       59.9967 |       -151.65  | 2004-06-14 23:46:00 |       59.4917 |       -152.537 | 2004-06-14 13:39:00 |
| 14 | cmi_full_v2-Cruise_03-Line_4 | trajectoryProfile |       59.6417 |       -151.65  | 2004-06-15 02:01:00 |       59.5083 |       -151.65  | 2004-06-14 23:59:00 |
| 15 | cmi_full_v2-Cruise_04-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2004-07-18 11:34:00 |       58.735  |       -152.267 | 2004-07-18 11:34:00 |
| 16 | cmi_full_v2-Cruise_04-Line_2 | trajectoryProfile |       58.665  |       -152.633 | 2004-07-18 22:46:00 |       58.6133 |       -152.767 | 2004-07-18 22:11:00 |
| 17 | cmi_full_v2-Cruise_04-Line_3 | trajectoryProfile |       59.9567 |       -151.65  | 2004-07-18 23:46:00 |       59.4917 |       -152.422 | 2004-07-17 13:24:00 |
| 18 | cmi_full_v2-Cruise_04-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2004-07-18 23:46:00 |       59.525  |       -151.65  | 2004-07-18 23:46:00 |
| 19 | cmi_full_v2-Cruise_05-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2004-09-11 03:19:00 |       58.65   |       -152.333 | 2004-08-17 13:00:00 |
| 20 | cmi_full_v2-Cruise_05-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2004-08-17 08:13:00 |       58.6133 |       -152.817 | 2004-08-17 06:26:00 |
| 21 | cmi_full_v2-Cruise_05-Line_3 | trajectoryProfile |       59.9967 |       -151.65  | 2004-08-18 04:09:00 |       59.4917 |       -152.537 | 2004-08-16 10:22:00 |
| 22 | cmi_full_v2-Cruise_05-Line_4 | trajectoryProfile |       59.6417 |       -151.65  | 2004-08-18 06:08:00 |       59.5083 |       -151.65  | 2004-08-18 04:21:00 |
| 23 | cmi_full_v2-Cruise_06-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2004-09-08 09:39:00 |       58.65   |       -152.333 | 2004-09-07 23:19:00 |
| 24 | cmi_full_v2-Cruise_06-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2004-09-08 16:41:00 |       58.6133 |       -152.817 | 2004-09-08 14:33:00 |
| 25 | cmi_full_v2-Cruise_06-Line_3 | trajectoryProfile |       59.9967 |       -151.65  | 2004-09-09 20:24:00 |       59.4917 |       -152.537 | 2004-09-09 09:03:00 |
| 26 | cmi_full_v2-Cruise_06-Line_4 | trajectoryProfile |       59.6417 |       -151.65  | 2004-09-09 20:03:00 |       59.5083 |       -151.65  | 2004-09-09 17:54:00 |
| 27 | cmi_full_v2-Cruise_07-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2005-01-09 06:16:00 |       58.65   |       -152.333 | 2005-01-08 19:06:00 |
| 28 | cmi_full_v2-Cruise_07-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2005-01-09 10:39:00 |       58.6133 |       -152.817 | 2005-01-09 08:10:00 |
| 29 | cmi_full_v2-Cruise_07-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2005-01-10 09:01:00 |       59.7717 |       -152.567 | 2005-01-10 03:07:00 |
| 30 | cmi_full_v2-Cruise_07-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2005-01-10 14:03:00 |       59.4917 |       -151.65  | 2005-01-10 11:04:00 |
| 31 | cmi_full_v2-Cruise_08-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2005-04-26 07:23:00 |       58.65   |       -152.333 | 2005-04-25 20:05:00 |
| 32 | cmi_full_v2-Cruise_08-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2005-04-26 14:45:00 |       58.6133 |       -152.817 | 2005-04-26 12:43:00 |
| 33 | cmi_full_v2-Cruise_08-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2005-04-27 10:50:00 |       59.7717 |       -152.567 | 2005-04-27 04:33:00 |
| 34 | cmi_full_v2-Cruise_08-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2005-04-25 17:42:00 |       59.4917 |       -151.65  | 2005-04-25 14:49:00 |
| 35 | cmi_full_v2-Cruise_09-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2005-06-14 18:18:00 |       58.65   |       -152.333 | 2005-06-14 10:26:00 |
| 36 | cmi_full_v2-Cruise_09-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2005-06-15 01:24:00 |       58.6133 |       -152.817 | 2005-06-14 23:37:00 |
| 37 | cmi_full_v2-Cruise_09-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2005-06-15 20:28:00 |       59.7717 |       -152.567 | 2005-06-15 15:55:00 |
| 38 | cmi_full_v2-Cruise_09-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2005-06-16 20:48:00 |       59.4917 |       -151.65  | 2005-06-16 18:46:00 |
| 39 | cmi_full_v2-Cruise_10-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2005-07-30 06:56:00 |       58.65   |       -152.333 | 2005-07-29 17:13:00 |
| 40 | cmi_full_v2-Cruise_10-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2005-07-29 12:14:00 |       58.6133 |       -152.817 | 2005-07-29 10:43:00 |
| 41 | cmi_full_v2-Cruise_10-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2005-07-28 17:57:00 |       59.7717 |       -152.567 | 2005-07-28 11:09:00 |
| 42 | cmi_full_v2-Cruise_10-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2005-07-30 18:02:00 |       59.4917 |       -151.65  | 2005-07-30 16:08:00 |
| 43 | cmi_full_v2-Cruise_11-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2005-09-05 02:18:00 |       58.65   |       -152.333 | 2005-09-04 18:41:00 |
| 44 | cmi_full_v2-Cruise_11-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2005-09-05 12:13:00 |       58.6133 |       -152.817 | 2005-09-05 10:42:00 |
| 45 | cmi_full_v2-Cruise_11-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2005-09-06 08:02:00 |       59.7717 |       -152.567 | 2005-09-06 02:46:00 |
| 46 | cmi_full_v2-Cruise_11-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2005-09-06 11:29:00 |       59.4917 |       -151.65  | 2005-09-06 09:35:00 |
| 47 | cmi_full_v2-Cruise_12-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2005-10-13 22:35:00 |       58.65   |       -152.333 | 2005-10-13 15:26:00 |
| 48 | cmi_full_v2-Cruise_12-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2005-10-14 01:40:00 |       58.6133 |       -152.817 | 2005-10-14 00:06:00 |
| 49 | cmi_full_v2-Cruise_12-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2005-10-14 19:04:00 |       59.7717 |       -152.567 | 2005-10-14 14:47:00 |
| 50 | cmi_full_v2-Cruise_12-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2005-10-14 22:50:00 |       59.4917 |       -151.65  | 2005-10-14 20:44:00 |
| 51 | cmi_full_v2-Cruise_13-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2006-07-27 02:55:00 |       58.65   |       -152.333 | 2006-07-26 19:07:00 |
| 52 | cmi_full_v2-Cruise_13-Line_3 | trajectoryProfile |       60.0067 |       -151.987 | 2006-07-26 03:26:00 |       59.81   |       -152.567 | 2006-07-26 00:02:00 |
| 53 | cmi_full_v2-Cruise_13-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2006-07-28 14:32:00 |       59.4917 |       -151.65  | 2006-07-28 12:41:00 |
| 54 | cmi_full_v2-Cruise_13-Line_6 | trajectoryProfile |       59.2117 |       -151.925 | 2006-07-28 02:39:00 |       58.865  |       -153.24  | 2006-07-27 16:41:00 |
| 55 | cmi_full_v2-Cruise_13-Line_7 | trajectoryProfile |       59.35   |       -152     | 2006-07-26 16:48:00 |       59.3083 |       -153.302 | 2006-07-26 09:08:00 |
| 56 | cmi_full_v2-Cruise_14-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2006-08-06 10:16:00 |       58.65   |       -152.333 | 2006-08-06 03:41:00 |
| 57 | cmi_full_v2-Cruise_14-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2006-08-06 19:17:00 |       58.6133 |       -152.817 | 2006-08-06 17:40:00 |
| 58 | cmi_full_v2-Cruise_14-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2006-08-05 14:02:00 |       59.7717 |       -152.567 | 2006-08-05 10:04:00 |
| 59 | cmi_full_v2-Cruise_14-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2006-08-07 14:57:00 |       59.4917 |       -151.65  | 2006-08-07 13:11:00 |
| 60 | cmi_full_v2-Cruise_14-Line_6 | trajectoryProfile |       59.2117 |       -151.925 | 2006-08-07 08:22:00 |       58.865  |       -153.24  | 2006-08-06 23:14:00 |
| 61 | cmi_full_v2-Cruise_14-Line_7 | trajectoryProfile |       59.355  |       -152     | 2006-08-06 02:06:00 |       59.3083 |       -153.302 | 2006-08-05 19:22:00 |
| 62 | cmi_full_v2-Cruise_15-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2006-08-13 02:41:00 |       58.65   |       -152.333 | 2006-08-12 19:38:00 |
| 63 | cmi_full_v2-Cruise_15-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2006-08-12 04:36:00 |       59.7717 |       -152.567 | 2006-08-12 00:23:00 |
| 64 | cmi_full_v2-Cruise_15-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2006-08-14 13:27:00 |       59.4917 |       -151.65  | 2006-08-14 11:46:00 |
| 65 | cmi_full_v2-Cruise_15-Line_6 | trajectoryProfile |       59.2117 |       -151.925 | 2006-08-14 03:21:00 |       58.865  |       -153.24  | 2006-08-13 17:40:00 |
| 66 | cmi_full_v2-Cruise_15-Line_7 | trajectoryProfile |       59.355  |       -152     | 2006-08-12 17:34:00 |       59.3083 |       -153.302 | 2006-08-12 10:17:00 |
| 67 | cmi_full_v2-Cruise_16-Line_1 | trajectoryProfile |       59.2033 |       -151.875 | 2006-09-12 13:16:00 |       58.65   |       -152.333 | 2006-09-12 06:48:00 |
| 68 | cmi_full_v2-Cruise_16-Line_2 | trajectoryProfile |       58.6867 |       -152.633 | 2006-09-13 01:43:00 |       58.6133 |       -152.817 | 2006-09-13 00:12:00 |
| 69 | cmi_full_v2-Cruise_16-Line_3 | trajectoryProfile |       60.0067 |       -151.883 | 2006-09-11 16:22:00 |       59.7717 |       -152.567 | 2006-09-11 12:16:00 |
| 70 | cmi_full_v2-Cruise_16-Line_4 | trajectoryProfile |       59.625  |       -151.65  | 2006-09-13 19:04:00 |       59.4917 |       -151.65  | 2006-09-13 17:18:00 |
| 71 | cmi_full_v2-Cruise_16-Line_6 | trajectoryProfile |       59.2117 |       -151.925 | 2006-09-13 15:03:00 |       58.865  |       -153.24  | 2006-09-13 06:13:00 |
| 72 | cmi_full_v2-Cruise_16-Line_7 | trajectoryProfile |       59.355  |       -152     | 2006-09-12 05:27:00 |       59.3083 |       -153.302 | 2006-09-11 22:06:00 |
| 73 | sue_shelikof                 | trajectoryProfile |       58.6133 |       -152.633 | 2006-09-12 22:04:00 |       58.3505 |       -152.898 | 2006-09-12 19:41:00 |
    

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
        

```{code-cell}
cat['Kbay_timeseries'].plot.salt() + cat['Kbay_timeseries'].plot.temp()
```

## Cruise_00

+++

cmi_full_v2-Cruise_00-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_00-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_00-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_00-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_00-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_00-Line_4'].plot.temp()
```

## Cruise_01

+++

cmi_full_v2-Cruise_01-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_4'].plot.temp()
```

## Cruise_02

+++

cmi_full_v2-Cruise_02-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_4'].plot.temp()
```

## Cruise_03

+++

cmi_full_v2-Cruise_03-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_4'].plot.temp()
```

## Cruise_04

+++

cmi_full_v2-Cruise_04-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_4'].plot.temp()
```

## Cruise_05

+++

cmi_full_v2-Cruise_05-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_4'].plot.temp()
```

## Cruise_06

+++

cmi_full_v2-Cruise_06-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_4'].plot.temp()
```

## Cruise_07

+++

cmi_full_v2-Cruise_07-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_4'].plot.temp()
```

## Cruise_08

+++

cmi_full_v2-Cruise_08-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_4'].plot.temp()
```

## Cruise_09

+++

cmi_full_v2-Cruise_09-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_4'].plot.temp()
```

## Cruise_10

+++

cmi_full_v2-Cruise_10-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_4'].plot.temp()
```

## Cruise_11

+++

cmi_full_v2-Cruise_11-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_4'].plot.temp()
```

## Cruise_12

+++

cmi_full_v2-Cruise_12-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_4'].plot.temp()
```

## Cruise_13

+++

cmi_full_v2-Cruise_13-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_7'].plot.temp()
```

## Cruise_14

+++

cmi_full_v2-Cruise_14-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_7'].plot.temp()
```

## Cruise_15

+++

cmi_full_v2-Cruise_15-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_7'].plot.temp()
```

## Cruise_16

+++

cmi_full_v2-Cruise_16-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_7'].plot.temp()
```

## sue_shelikof

+++

sue_shelikof
        

```{code-cell}
cat['sue_shelikof'].plot.salt() + cat['sue_shelikof'].plot.temp()
```
