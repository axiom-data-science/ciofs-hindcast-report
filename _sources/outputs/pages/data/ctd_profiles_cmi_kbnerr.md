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

(page:ctd_profiles_cmi_kbnerr)=
# CTD Transects, Moored CTD (CMI KBNERR): Six repeat, one single transect, one moored CTD

* CTD profiles 2004-2006 - CMI KBNERR
* ctd_profiles_cmi_kbnerr
* From 2004 to 2006

Seasonality of Boundary Conditions for Cook Inlet, Alaska

During 2004 to 2006 we collected hydrographic measurements along transect lines crossing: 1) Kennedy Entrance and Stevenson Entrance from Port Chatham to Shuyak Island; 2) Shelikof Strait from Shuyak Island to Cape Douglas; 3) Cook Inlet from Red River to Anchor Point; 4) Kachemak Bay from Barbara Point to Bluff Point, and 5) the Forelands from East Foreland to West Foreland. During the third year we added two additional lines; 6) Cape Douglas to Cape Adams, and 7) Magnet Rock to Mount Augustine. The sampling in 2006 focused on the differences in properties during the spring and neap tide periods.

CTD profiles 2004-2005 - CMI UAF seems to be transect 5 of this project.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>


Used in the NWGOA model/data comparison.

```{dropdown} Dataset metadata

|    | Dataset          | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                          |
|---:|:-----------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------|
|  0 | Cruise_00-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.625  |       -151.65  | 2004-03-13 12:27:00 |       59.5083 |       -151.65  | 2004-03-13 10:40:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  1 | Cruise_01-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-04-20 18:20:00 |       58.65   |       -152.333 | 2004-04-20 08:45:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  2 | Cruise_01-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-04-19 23:10:00 |       58.6133 |       -153.24  | 2004-04-19 15:21:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  3 | Cruise_01-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-04-19 03:19:00 |       59.7717 |       -152.537 | 2004-04-18 21:36:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  4 | Cruise_01-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.625  |       -151.65  | 2004-04-21 09:28:00 |       59.5083 |       -151.65  | 2004-04-21 07:29:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  5 | Cruise_02-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-05-26 21:07:00 |       58.65   |       -152.333 | 2004-05-26 11:50:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  6 | Cruise_02-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-05-26 09:39:00 |       58.6133 |       -153.24  | 2004-05-26 02:17:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  7 | Cruise_02-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-05-25 16:34:00 |       59.7717 |       -152.537 | 2004-05-25 11:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  8 | Cruise_02-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.625  |       -151.65  | 2004-05-27 08:04:00 |       59.5169 |       -151.65  | 2004-05-27 05:59:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
|  9 | Cruise_03-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-06-13 20:35:00 |       58.65   |       -152.333 | 2004-06-13 11:34:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 10 | Cruise_03-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-06-14 05:21:00 |       58.6133 |       -153.24  | 2004-06-13 22:11:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 11 | Cruise_03-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-06-14 18:27:00 |       59.7717 |       -152.537 | 2004-06-14 13:39:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 12 | Cruise_03-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6417 |       -151.65  | 2004-06-15 02:01:00 |       59.5083 |       -151.65  | 2004-06-14 23:59:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 13 | Cruise_05-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2004-08-17 20:55:00 |       58.65   |       -152.333 | 2004-08-17 13:00:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 14 | Cruise_05-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-08-17 08:13:00 |       58.6133 |       -153.24  | 2004-08-17 02:15:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 15 | Cruise_05-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-08-16 14:41:00 |       59.7717 |       -152.537 | 2004-08-16 10:22:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 16 | Cruise_05-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6417 |       -151.65  | 2004-08-18 06:08:00 |       59.5083 |       -151.65  | 2004-08-18 04:21:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 17 | Cruise_06-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.19   |       -151.89  | 2004-09-08 09:39:00 |       58.65   |       -152.333 | 2004-09-07 23:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 18 | Cruise_06-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2004-09-08 21:50:00 |       58.6133 |       -153.24  | 2004-09-08 14:33:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 19 | Cruise_06-Line_3 | trajectoryProfile | ['temp', 'salt'] |       59.9967 |       -151.883 | 2004-09-09 14:29:00 |       59.7717 |       -152.537 | 2004-09-09 09:03:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 20 | Cruise_06-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6417 |       -151.65  | 2004-09-09 20:03:00 |       59.5083 |       -151.65  | 2004-09-09 17:54:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 21 | Cruise_07-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-01-09 06:16:00 |       58.65   |       -152.333 | 2005-01-08 19:06:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 22 | Cruise_07-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-01-09 16:37:00 |       58.6133 |       -153.24  | 2005-01-09 08:10:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 23 | Cruise_07-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-01-10 09:01:00 |       59.7717 |       -152.567 | 2005-01-10 03:07:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 24 | Cruise_07-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-01-10 14:03:00 |       59.4917 |       -151.65  | 2005-01-10 11:04:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 25 | Cruise_08-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-04-26 07:23:00 |       58.65   |       -152.333 | 2005-04-25 20:05:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 26 | Cruise_08-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-04-26 19:48:00 |       58.6133 |       -153.24  | 2005-04-26 12:43:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 27 | Cruise_08-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-04-27 10:50:00 |       59.7717 |       -152.567 | 2005-04-27 04:33:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 28 | Cruise_08-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-04-25 17:42:00 |       59.4917 |       -151.65  | 2005-04-25 14:49:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 29 | Cruise_09-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-06-14 18:18:00 |       58.65   |       -152.333 | 2005-06-14 10:26:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 30 | Cruise_09-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-06-15 05:50:00 |       58.6133 |       -153.24  | 2005-06-14 23:37:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 31 | Cruise_09-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-06-15 20:28:00 |       59.7717 |       -152.567 | 2005-06-15 15:55:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 32 | Cruise_09-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-06-16 20:48:00 |       59.4917 |       -151.65  | 2005-06-16 18:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 33 | Cruise_10-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-07-30 06:56:00 |       58.65   |       -152.333 | 2005-07-29 17:13:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 34 | Cruise_10-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-07-29 12:14:00 |       58.6133 |       -153.24  | 2005-07-29 07:13:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 35 | Cruise_10-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-07-28 17:57:00 |       59.7717 |       -152.567 | 2005-07-28 11:09:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 36 | Cruise_10-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-07-30 18:02:00 |       59.4917 |       -151.65  | 2005-07-30 16:08:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 37 | Cruise_11-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-09-05 02:18:00 |       58.65   |       -152.333 | 2005-09-04 18:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 38 | Cruise_11-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-09-05 16:08:00 |       58.6133 |       -153.24  | 2005-09-05 10:42:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 39 | Cruise_11-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-09-06 08:02:00 |       59.7717 |       -152.567 | 2005-09-06 02:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 40 | Cruise_11-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-09-06 11:29:00 |       59.4917 |       -151.65  | 2005-09-06 09:35:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 41 | Cruise_12-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2005-10-13 22:35:00 |       58.65   |       -152.333 | 2005-10-13 15:26:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 42 | Cruise_12-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2005-10-14 06:03:00 |       58.6133 |       -153.24  | 2005-10-14 00:06:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 43 | Cruise_12-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2005-10-14 19:04:00 |       59.7717 |       -152.567 | 2005-10-14 14:47:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 44 | Cruise_12-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2005-10-14 22:50:00 |       59.4917 |       -151.65  | 2005-10-14 20:44:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 45 | Cruise_13-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-07-27 02:55:00 |       58.65   |       -152.333 | 2006-07-26 19:07:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 46 | Cruise_13-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.987 | 2006-07-26 03:26:00 |       59.81   |       -152.567 | 2006-07-26 00:02:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 47 | Cruise_13-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-07-28 14:32:00 |       59.4917 |       -151.65  | 2006-07-28 12:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 48 | Cruise_13-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-07-28 02:39:00 |       58.865  |       -153.24  | 2006-07-27 16:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 49 | Cruise_13-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.35   |       -152     | 2006-07-26 16:48:00 |       59.3083 |       -153.302 | 2006-07-26 09:08:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 50 | Cruise_14-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-08-06 10:16:00 |       58.65   |       -152.333 | 2006-08-06 03:41:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 51 | Cruise_14-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2006-08-06 22:48:00 |       58.6133 |       -153.24  | 2006-08-06 17:40:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 52 | Cruise_14-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2006-08-05 14:02:00 |       59.7717 |       -152.567 | 2006-08-05 10:04:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 53 | Cruise_14-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-08-07 14:57:00 |       59.4917 |       -151.65  | 2006-08-07 13:11:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 54 | Cruise_14-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-08-07 08:22:00 |       58.865  |       -153.24  | 2006-08-06 23:14:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 55 | Cruise_14-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.355  |       -152     | 2006-08-06 02:06:00 |       59.3083 |       -153.302 | 2006-08-05 19:22:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 56 | Cruise_15-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-08-13 02:41:00 |       58.65   |       -152.333 | 2006-08-12 19:38:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 57 | Cruise_15-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2006-08-12 04:36:00 |       59.7717 |       -152.567 | 2006-08-12 00:23:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 58 | Cruise_15-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-08-14 13:27:00 |       59.4917 |       -151.65  | 2006-08-14 11:46:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 59 | Cruise_15-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-08-14 03:21:00 |       58.865  |       -153.24  | 2006-08-13 17:40:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 60 | Cruise_15-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.355  |       -152     | 2006-08-12 17:34:00 |       59.3083 |       -153.302 | 2006-08-12 10:17:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 61 | Cruise_16-Line_1 | trajectoryProfile | ['temp', 'salt'] |       59.2033 |       -151.875 | 2006-09-12 13:16:00 |       58.65   |       -152.333 | 2006-09-12 06:48:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 62 | Cruise_16-Line_2 | trajectoryProfile | ['temp', 'salt'] |       58.8383 |       -152.633 | 2006-09-13 05:36:00 |       58.6133 |       -153.24  | 2006-09-13 00:12:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 63 | Cruise_16-Line_3 | trajectoryProfile | ['temp', 'salt'] |       60.0067 |       -151.883 | 2006-09-11 16:22:00 |       59.7717 |       -152.567 | 2006-09-11 12:16:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 64 | Cruise_16-Line_4 | trajectoryProfile | ['temp', 'salt'] |       59.6584 |       -151.65  | 2006-09-13 19:04:00 |       59.4917 |       -151.65  | 2006-09-13 17:18:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 65 | Cruise_16-Line_6 | trajectoryProfile | ['temp', 'salt'] |       59.2117 |       -151.925 | 2006-09-13 15:03:00 |       58.865  |       -153.24  | 2006-09-13 06:13:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 66 | Cruise_16-Line_7 | trajectoryProfile | ['temp', 'salt'] |       59.355  |       -152     | 2006-09-12 05:27:00 |       59.3083 |       -153.302 | 2006-09-11 22:06:00 | https://researchworkspace.com/files/42202067/cmi_full_v2.csv     |
| 67 | Kbay_timeseries  | trajectoryProfile | ['temp', 'salt'] |       59.5833 |       -151.75  | 2006-04-23 17:33:00 |       59.5833 |       -151.75  | 2006-04-22 17:06:00 | https://researchworkspace.com/files/39886046/Kbay_timeseries.txt |
| 68 | sue_shelikof     | trajectoryProfile | ['temp', 'salt'] |       58.6133 |       -152.633 | 2006-09-12 22:04:00 |       58.3505 |       -152.898 | 2006-09-12 19:41:00 | https://researchworkspace.com/files/39886061/sue_shelikof.txt    |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_cmi_kbnerr"))
```

## Map of CTD Profiles in Transects
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_cmi_kbnerr")("ctd_profiles_cmi_kbnerr")
```

## Cruise_00

+++

Cruise_00-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_00-Line_4'].plot.salt() + cat['Cruise_00-Line_4'].plot.temp()
```

## Cruise_01

+++

Cruise_01-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_01-Line_1'].plot.salt() + cat['Cruise_01-Line_1'].plot.temp()
```

Cruise_01-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_01-Line_2'].plot.salt() + cat['Cruise_01-Line_2'].plot.temp()
```

Cruise_01-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_01-Line_3'].plot.salt() + cat['Cruise_01-Line_3'].plot.temp()
```

Cruise_01-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_01-Line_4'].plot.salt() + cat['Cruise_01-Line_4'].plot.temp()
```

## Cruise_02

+++

Cruise_02-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_02-Line_1'].plot.salt() + cat['Cruise_02-Line_1'].plot.temp()
```

Cruise_02-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_02-Line_2'].plot.salt() + cat['Cruise_02-Line_2'].plot.temp()
```

Cruise_02-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_02-Line_3'].plot.salt() + cat['Cruise_02-Line_3'].plot.temp()
```

Cruise_02-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_02-Line_4'].plot.salt() + cat['Cruise_02-Line_4'].plot.temp()
```

## Cruise_03

+++

Cruise_03-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_03-Line_1'].plot.salt() + cat['Cruise_03-Line_1'].plot.temp()
```

Cruise_03-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_03-Line_2'].plot.salt() + cat['Cruise_03-Line_2'].plot.temp()
```

Cruise_03-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_03-Line_3'].plot.salt() + cat['Cruise_03-Line_3'].plot.temp()
```

Cruise_03-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_03-Line_4'].plot.salt() + cat['Cruise_03-Line_4'].plot.temp()
```

## Cruise_05

+++

Cruise_05-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_05-Line_1'].plot.salt() + cat['Cruise_05-Line_1'].plot.temp()
```

Cruise_05-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_05-Line_2'].plot.salt() + cat['Cruise_05-Line_2'].plot.temp()
```

Cruise_05-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_05-Line_3'].plot.salt() + cat['Cruise_05-Line_3'].plot.temp()
```

Cruise_05-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_05-Line_4'].plot.salt() + cat['Cruise_05-Line_4'].plot.temp()
```

## Cruise_06

+++

Cruise_06-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_06-Line_1'].plot.salt() + cat['Cruise_06-Line_1'].plot.temp()
```

Cruise_06-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_06-Line_2'].plot.salt() + cat['Cruise_06-Line_2'].plot.temp()
```

Cruise_06-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_06-Line_3'].plot.salt() + cat['Cruise_06-Line_3'].plot.temp()
```

Cruise_06-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_06-Line_4'].plot.salt() + cat['Cruise_06-Line_4'].plot.temp()
```

## Cruise_07

+++

Cruise_07-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_07-Line_1'].plot.salt() + cat['Cruise_07-Line_1'].plot.temp()
```

Cruise_07-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_07-Line_2'].plot.salt() + cat['Cruise_07-Line_2'].plot.temp()
```

Cruise_07-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_07-Line_3'].plot.salt() + cat['Cruise_07-Line_3'].plot.temp()
```

Cruise_07-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_07-Line_4'].plot.salt() + cat['Cruise_07-Line_4'].plot.temp()
```

## Cruise_08

+++

Cruise_08-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_08-Line_1'].plot.salt() + cat['Cruise_08-Line_1'].plot.temp()
```

Cruise_08-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_08-Line_2'].plot.salt() + cat['Cruise_08-Line_2'].plot.temp()
```

Cruise_08-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_08-Line_3'].plot.salt() + cat['Cruise_08-Line_3'].plot.temp()
```

Cruise_08-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_08-Line_4'].plot.salt() + cat['Cruise_08-Line_4'].plot.temp()
```

## Cruise_09

+++

Cruise_09-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_09-Line_1'].plot.salt() + cat['Cruise_09-Line_1'].plot.temp()
```

Cruise_09-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_09-Line_2'].plot.salt() + cat['Cruise_09-Line_2'].plot.temp()
```

Cruise_09-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_09-Line_3'].plot.salt() + cat['Cruise_09-Line_3'].plot.temp()
```

Cruise_09-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_09-Line_4'].plot.salt() + cat['Cruise_09-Line_4'].plot.temp()
```

## Cruise_10

+++

Cruise_10-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_10-Line_1'].plot.salt() + cat['Cruise_10-Line_1'].plot.temp()
```

Cruise_10-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_10-Line_2'].plot.salt() + cat['Cruise_10-Line_2'].plot.temp()
```

Cruise_10-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_10-Line_3'].plot.salt() + cat['Cruise_10-Line_3'].plot.temp()
```

Cruise_10-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_10-Line_4'].plot.salt() + cat['Cruise_10-Line_4'].plot.temp()
```

## Cruise_11

+++

Cruise_11-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_11-Line_1'].plot.salt() + cat['Cruise_11-Line_1'].plot.temp()
```

Cruise_11-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_11-Line_2'].plot.salt() + cat['Cruise_11-Line_2'].plot.temp()
```

Cruise_11-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_11-Line_3'].plot.salt() + cat['Cruise_11-Line_3'].plot.temp()
```

Cruise_11-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_11-Line_4'].plot.salt() + cat['Cruise_11-Line_4'].plot.temp()
```

## Cruise_12

+++

Cruise_12-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_12-Line_1'].plot.salt() + cat['Cruise_12-Line_1'].plot.temp()
```

Cruise_12-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_12-Line_2'].plot.salt() + cat['Cruise_12-Line_2'].plot.temp()
```

Cruise_12-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_12-Line_3'].plot.salt() + cat['Cruise_12-Line_3'].plot.temp()
```

Cruise_12-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_12-Line_4'].plot.salt() + cat['Cruise_12-Line_4'].plot.temp()
```

## Cruise_13

+++

Cruise_13-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_13-Line_1'].plot.salt() + cat['Cruise_13-Line_1'].plot.temp()
```

Cruise_13-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_13-Line_3'].plot.salt() + cat['Cruise_13-Line_3'].plot.temp()
```

Cruise_13-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_13-Line_4'].plot.salt() + cat['Cruise_13-Line_4'].plot.temp()
```

Cruise_13-Line_6
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_13-Line_6'].plot.salt() + cat['Cruise_13-Line_6'].plot.temp()
```

Cruise_13-Line_7
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_13-Line_7'].plot.salt() + cat['Cruise_13-Line_7'].plot.temp()
```

## Cruise_14

+++

Cruise_14-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_14-Line_1'].plot.salt() + cat['Cruise_14-Line_1'].plot.temp()
```

Cruise_14-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_14-Line_2'].plot.salt() + cat['Cruise_14-Line_2'].plot.temp()
```

Cruise_14-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_14-Line_3'].plot.salt() + cat['Cruise_14-Line_3'].plot.temp()
```

Cruise_14-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_14-Line_4'].plot.salt() + cat['Cruise_14-Line_4'].plot.temp()
```

Cruise_14-Line_6
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_14-Line_6'].plot.salt() + cat['Cruise_14-Line_6'].plot.temp()
```

Cruise_14-Line_7
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_14-Line_7'].plot.salt() + cat['Cruise_14-Line_7'].plot.temp()
```

## Cruise_15

+++

Cruise_15-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_15-Line_1'].plot.salt() + cat['Cruise_15-Line_1'].plot.temp()
```

Cruise_15-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_15-Line_3'].plot.salt() + cat['Cruise_15-Line_3'].plot.temp()
```

Cruise_15-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_15-Line_4'].plot.salt() + cat['Cruise_15-Line_4'].plot.temp()
```

Cruise_15-Line_6
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_15-Line_6'].plot.salt() + cat['Cruise_15-Line_6'].plot.temp()
```

Cruise_15-Line_7
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_15-Line_7'].plot.salt() + cat['Cruise_15-Line_7'].plot.temp()
```

## Cruise_16

+++

Cruise_16-Line_1
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_16-Line_1'].plot.salt() + cat['Cruise_16-Line_1'].plot.temp()
```

Cruise_16-Line_2
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_16-Line_2'].plot.salt() + cat['Cruise_16-Line_2'].plot.temp()
```

Cruise_16-Line_3
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_16-Line_3'].plot.salt() + cat['Cruise_16-Line_3'].plot.temp()
```

Cruise_16-Line_4
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_16-Line_4'].plot.salt() + cat['Cruise_16-Line_4'].plot.temp()
```

Cruise_16-Line_6
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_16-Line_6'].plot.salt() + cat['Cruise_16-Line_6'].plot.temp()
```

Cruise_16-Line_7
        

```{code-cell}
:tags: [remove-input]

cat['Cruise_16-Line_7'].plot.salt() + cat['Cruise_16-Line_7'].plot.temp()
```

## Kbay_timeseries

+++

Kbay_timeseries
        

```{code-cell}
:tags: [remove-input]

cat['Kbay_timeseries'].plot.salt() + cat['Kbay_timeseries'].plot.temp()
```

## sue_shelikof

+++

sue_shelikof
        

```{code-cell}
:tags: [remove-input]

cat['sue_shelikof'].plot.salt() + cat['sue_shelikof'].plot.temp()
```
