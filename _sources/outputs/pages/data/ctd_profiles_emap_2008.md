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

(page:ctd_profiles_emap_2008)=
# CTD Profiles (emap 2008)

* emap 2008
* ctd_profiles_emap_2008
* One-off CTD profiles August to October 2008

CTD Profiles in Cook Inlet



```{dropdown} Dataset metadata

|    | Dataset     | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                |
|---:|:------------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------------|
|  0 | AKCI08-001  | profile       | ['temp', 'salt'] |       58.8677 |       -153.314 | 2008-08-06 15:09:00 |       58.8677 |       -153.314 | 2008-08-06 15:09:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  1 | AKCI08-002  | profile       | ['temp', 'salt'] |       59.1065 |       -153.417 | 2008-08-06 18:08:00 |       59.1065 |       -153.417 | 2008-08-06 18:08:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  2 | AKCI08-003  | profile       | ['temp', 'salt'] |       60.5112 |       -151.852 | 2008-08-14 14:51:00 |       60.5112 |       -151.852 | 2008-08-14 14:51:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  3 | AKCI08-004  | profile       | ['temp', 'salt'] |       60.9415 |       -151.508 | 2008-08-20 10:59:00 |       60.9415 |       -151.508 | 2008-08-20 10:59:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  4 | AKCI08-005  | profile       | ['temp', 'salt'] |       60.2248 |       -151.425 | 2008-08-28 10:01:00 |       60.2248 |       -151.425 | 2008-08-28 10:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  5 | AKCI08-007  | profile       | ['temp', 'salt'] |       60.8294 |       -151.679 | 2008-08-24 08:40:00 |       60.8294 |       -151.679 | 2008-08-24 08:40:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  6 | AKCI08-008  | profile       | ['temp', 'salt'] |       60.9409 |       -151.109 | 2008-08-19 18:33:00 |       60.9409 |       -151.109 | 2008-08-19 18:33:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  7 | AKCI08-009  | profile       | ['temp', 'salt'] |       59.4453 |       -152.145 | 2008-08-04 12:57:00 |       59.4453 |       -152.145 | 2008-08-04 12:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  8 | AKCI08-011  | profile       | ['temp', 'salt'] |       60.8088 |       -151.717 | 2008-08-24 19:40:00 |       60.8088 |       -151.717 | 2008-08-24 19:40:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
|  9 | AKCI08-012  | profile       | ['temp', 'salt'] |       60.8944 |       -151.171 | 2008-08-19 15:23:00 |       60.8944 |       -151.171 | 2008-08-19 15:23:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 10 | AKCI08-013  | profile       | ['temp', 'salt'] |       59.3351 |       -152.772 | 2008-08-05 13:53:00 |       59.3351 |       -152.772 | 2008-08-05 13:53:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 11 | AKCI08-015  | profile       | ['temp', 'salt'] |       60.7357 |       -151.663 | 2008-08-23 16:20:00 |       60.7357 |       -151.663 | 2008-08-23 16:20:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 12 | AKCI08-016  | profile       | ['temp', 'salt'] |       60.7442 |       -151.334 | 2008-08-25 15:52:00 |       60.7442 |       -151.334 | 2008-08-25 15:52:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 13 | AKCI08-017  | profile       | ['temp', 'salt'] |       59.7346 |       -152.474 | 2008-08-10 12:11:00 |       59.7346 |       -152.474 | 2008-08-10 12:11:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 14 | AKCI08-018  | profile       | ['temp', 'salt'] |       59.2343 |       -153.805 | 2008-08-08 15:05:00 |       59.2343 |       -153.805 | 2008-08-08 15:05:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 15 | AKCI08-021  | profile       | ['temp', 'salt'] |       60.2332 |       -152.453 | 2008-08-27 16:26:00 |       60.2332 |       -152.453 | 2008-08-27 16:26:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 16 | AKCI08-023  | profile       | ['temp', 'salt'] |       60.8161 |       -151.721 | 2008-08-24 14:52:00 |       60.8161 |       -151.721 | 2008-08-24 14:52:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 17 | AKCI08-024  | profile       | ['temp', 'salt'] |       60.9327 |       -151.318 | 2008-08-19 20:50:00 |       60.9327 |       -151.318 | 2008-08-19 20:50:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 18 | AKCI08-026  | profile       | ['temp', 'salt'] |      nan      |        nan     | 2008-10-07 14:57:00 |      nan      |        nan     | 2008-10-07 14:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 19 | AKCI08-027  | profile       | ['temp', 'salt'] |       60.806  |       -151.688 | 2008-08-24 19:17:00 |       60.806  |       -151.688 | 2008-08-24 19:17:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 20 | AKCI08-028  | profile       | ['temp', 'salt'] |       60.8132 |       -151.257 | 2008-08-20 16:01:00 |       60.8132 |       -151.257 | 2008-08-20 16:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 21 | AKCI08-029  | profile       | ['temp', 'salt'] |       59.2728 |       -153.239 | 2008-08-06 20:51:00 |       59.2728 |       -153.239 | 2008-08-06 20:51:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 22 | AKCI08-031  | profile       | ['temp', 'salt'] |       60.7403 |       -151.56  | 2008-08-23 15:23:00 |       60.7403 |       -151.56  | 2008-08-23 15:23:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 23 | AKCI08-032  | profile       | ['temp', 'salt'] |       60.8086 |       -151.75  | 2008-08-24 13:53:00 |       60.8086 |       -151.75  | 2008-08-24 13:53:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 24 | AKCI08-033  | profile       | ['temp', 'salt'] |       59.8117 |       -151.853 | 2008-08-29 09:45:00 |       59.8117 |       -151.853 | 2008-08-29 09:45:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 25 | AKCI08-035  | profile       | ['temp', 'salt'] |       60.8567 |       -151.631 | 2008-08-24 06:55:00 |       60.8567 |       -151.631 | 2008-08-24 06:55:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 26 | AKCI08-037A | profile       | ['temp', 'salt'] |       60.1194 |       -152.035 | 2008-08-27 20:41:00 |       60.1194 |       -152.035 | 2008-08-27 20:41:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 27 | AKCI08-037B | profile       | ['temp', 'salt'] |       60.2001 |       -152.13  | 2008-08-13 13:00:00 |       60.2001 |       -152.13  | 2008-08-13 13:00:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 28 | AKCI08-039  | profile       | ['temp', 'salt'] |       60.2001 |       -152.13  | 2008-08-24 09:35:00 |       60.2001 |       -152.13  | 2008-08-24 09:35:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 29 | AKCI08-040  | profile       | ['temp', 'salt'] |       60.8302 |       -151.696 | 2008-08-24 22:26:00 |       60.8302 |       -151.696 | 2008-08-24 22:26:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 30 | AKCI08-041  | profile       | ['temp', 'salt'] |       59.0867 |       -153     | 2008-08-05 17:15:00 |       59.0867 |       -153     | 2008-08-05 17:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 31 | AKCI08-042  | profile       | ['temp', 'salt'] |       61.1948 |       -150.164 | 2008-09-16 09:36:00 |       61.1948 |       -150.164 | 2008-09-16 09:36:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 32 | AKCI08-043  | profile       | ['temp', 'salt'] |       60.7986 |       -151.585 | 2008-08-23 18:32:00 |       60.7986 |       -151.585 | 2008-08-23 18:32:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 33 | AKCI08-044  | profile       | ['temp', 'salt'] |       60.817  |       -151.207 | 2008-08-20 18:28:00 |       60.817  |       -151.207 | 2008-08-20 18:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 34 | AKCI08-045  | profile       | ['temp', 'salt'] |       59.4423 |       -153.34  | 2008-08-07 12:25:00 |       59.4423 |       -153.34  | 2008-08-07 12:25:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 35 | AKCI08-047  | profile       | ['temp', 'salt'] |       60.8552 |       -151.395 | 2008-08-20 14:21:00 |       60.8552 |       -151.395 | 2008-08-20 14:21:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 36 | AKCI08-048  | profile       | ['temp', 'salt'] |       60.815  |       -151.749 | 2008-08-24 13:34:00 |       60.815  |       -151.749 | 2008-08-24 13:34:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 37 | AKCI08-049  | profile       | ['temp', 'salt'] |       59.9768 |       -151.894 | 2008-08-12 16:28:00 |       59.9768 |       -151.894 | 2008-08-12 16:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 38 | AKCI08-050  | profile       | ['temp', 'salt'] |       59.7616 |       -152.94  | 2008-08-09 16:57:00 |       59.7616 |       -152.94  | 2008-08-09 16:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 39 | AKCI08-051  | profile       | ['temp', 'salt'] |       60.8364 |       -151.719 | 2008-08-24 20:11:00 |       60.8364 |       -151.719 | 2008-08-24 20:11:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 40 | AKCI08-052  | profile       | ['temp', 'salt'] |       60.9262 |       -150.952 | 2008-08-23 11:13:00 |       60.9262 |       -150.952 | 2008-08-23 11:13:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 41 | AKCI08-054  | profile       | ['temp', 'salt'] |       60.9524 |       -150.926 | 2008-08-23 11:50:00 |       60.9524 |       -150.926 | 2008-08-23 11:50:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 42 | AKCI08-055  | profile       | ['temp', 'salt'] |       60.8109 |       -151.601 | 2008-08-23 19:07:00 |       60.8109 |       -151.601 | 2008-08-23 19:07:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 43 | AKCI08-056  | profile       | ['temp', 'salt'] |       61.0415 |       -151.017 | 2008-08-22 10:06:00 |       61.0415 |       -151.017 | 2008-08-22 10:06:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 44 | AKCI08-057  | profile       | ['temp', 'salt'] |       58.9358 |       -153.228 | 2008-08-06 11:56:00 |       58.9358 |       -153.228 | 2008-08-06 11:56:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 45 | AKCI08-058  | profile       | ['temp', 'salt'] |       61.1952 |       -150.818 | 2008-10-07 13:15:00 |       61.1952 |       -150.818 | 2008-10-07 13:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 46 | AKCI08-059  | profile       | ['temp', 'salt'] |       60.7365 |       -151.372 | 2008-08-25 16:15:00 |       60.7365 |       -151.372 | 2008-08-25 16:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 47 | AKCI08-060  | profile       | ['temp', 'salt'] |       60.763  |       -151.281 | 2008-08-25 20:01:00 |       60.763  |       -151.281 | 2008-08-25 20:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 48 | AKCI08-061  | profile       | ['temp', 'salt'] |       59.4014 |       -153.652 | 2008-08-08 21:57:00 |       59.4014 |       -153.652 | 2008-08-08 21:57:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 49 | AKCI08-063  | profile       | ['temp', 'salt'] |       60.8503 |       -151.444 | 2008-08-20 12:48:00 |       60.8503 |       -151.444 | 2008-08-20 12:48:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 50 | AKCI08-065  | profile       | ['temp', 'salt'] |       59.2405 |       -153.516 | 2008-08-08 17:25:00 |       59.2405 |       -153.516 | 2008-08-08 17:25:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 51 | AKCI08-066  | profile       | ['temp', 'salt'] |       60.6011 |       -151.883 | 2008-08-14 17:19:00 |       60.6011 |       -151.883 | 2008-08-14 17:19:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 52 | AKCI08-067  | profile       | ['temp', 'salt'] |       60.9769 |       -151.441 | 2008-08-20 09:12:00 |       60.9769 |       -151.441 | 2008-08-20 09:12:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 53 | AKCI08-069  | profile       | ['temp', 'salt'] |       60.8257 |       -151.716 | 2008-08-24 12:58:00 |       60.8257 |       -151.716 | 2008-08-24 12:58:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 54 | AKCI08-070  | profile       | ['temp', 'salt'] |       60.9609 |       -151.143 | 2008-08-19 16:39:00 |       60.9609 |       -151.143 | 2008-08-19 16:39:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 55 | AKCI08-071  | profile       | ['temp', 'salt'] |       59.318  |       -152.315 | 2008-08-05 11:15:00 |       59.318  |       -152.315 | 2008-08-05 11:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 56 | AKCI08-072  | profile       | ['temp', 'salt'] |       60.7895 |       -151.686 | 2008-08-23 17:24:00 |       60.7895 |       -151.686 | 2008-08-23 17:24:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 57 | AKCI08-073  | profile       | ['temp', 'salt'] |       60.8552 |       -151.121 | 2008-08-23 09:51:00 |       60.8552 |       -151.121 | 2008-08-23 09:51:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 58 | AKCI08-074  | profile       | ['temp', 'salt'] |       59.5334 |       -153.034 | 2008-08-07 15:06:00 |       59.5334 |       -153.034 | 2008-08-07 15:06:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 59 | AKCI08-076  | profile       | ['temp', 'salt'] |      nan      |        nan     | 2008-08-20 16:32:00 |      nan      |        nan     | 2008-08-20 16:32:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 60 | AKCI08-079  | profile       | ['temp', 'salt'] |       60.9406 |       -151.547 | 2008-08-20 10:30:00 |       60.9406 |       -151.547 | 2008-08-20 10:30:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 61 | AKCI08-080  | profile       | ['temp', 'salt'] |       60.9699 |       -150.637 | 2008-08-22 13:39:00 |       60.9699 |       -150.637 | 2008-08-22 13:39:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 62 | AKCI08-081  | profile       | ['temp', 'salt'] |       60.815  |       -151.694 | 2008-08-24 08:01:00 |       60.815  |       -151.694 | 2008-08-24 08:01:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 63 | AKCI08-083  | profile       | ['temp', 'salt'] |       59.6899 |       -152.383 | 2008-08-12 12:16:00 |       59.6899 |       -152.383 | 2008-08-12 12:16:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 64 | AKCI08-084  | profile       | ['temp', 'salt'] |       60.793  |       -151.72  | 2008-08-24 15:28:00 |       60.793  |       -151.72  | 2008-08-24 15:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 65 | AKCI08-086  | profile       | ['temp', 'salt'] |       59.5548 |       -152.581 | 2008-08-10 15:14:00 |       59.5548 |       -152.581 | 2008-08-10 15:14:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 66 | AKCI08-087  | profile       | ['temp', 'salt'] |       60.489  |       -151.319 | 2008-08-26 15:47:00 |       60.489  |       -151.319 | 2008-08-26 15:47:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 67 | AKCI08-088  | profile       | ['temp', 'salt'] |       60.8052 |       -151.738 | 2008-08-24 14:15:00 |       60.8052 |       -151.738 | 2008-08-24 14:15:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 68 | KB01        | profile       | ['temp', 'salt'] |       59.6007 |       -151.387 | 2008-08-03 13:44:00 |       59.6007 |       -151.387 | 2008-08-03 13:44:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 69 | KB02        | profile       | ['temp', 'salt'] |       59.6091 |       -151.316 | 2008-08-02 15:22:00 |       59.6091 |       -151.316 | 2008-08-02 15:22:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 70 | KB03        | profile       | ['temp', 'salt'] |       59.6425 |       -151.32  | 2008-08-03 10:14:00 |       59.6425 |       -151.32  | 2008-08-03 10:14:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 71 | KB04        | profile       | ['temp', 'salt'] |       59.6575 |       -151.236 | 2008-08-03 11:39:00 |       59.6575 |       -151.236 | 2008-08-03 11:39:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 72 | KB05        | profile       | ['temp', 'salt'] |       59.7198 |       -151.136 | 2008-08-03 13:56:00 |       59.7198 |       -151.136 | 2008-08-03 13:56:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |
| 73 | KRM         | profile       | ['temp', 'salt'] |       60.547  |       -151.283 | 2008-08-06 14:28:00 |       60.547  |       -151.283 | 2008-08-06 14:28:00 | https://researchworkspace.com/files/42199537/Cook_EMAP_CTD-data_08.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_emap_2008"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_emap_2008")("ctd_profiles_emap_2008")
```

## AKCI08-001
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-001'].plot.data()
```

## AKCI08-002
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-002'].plot.data()
```

## AKCI08-003
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-003'].plot.data()
```

## AKCI08-004
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-004'].plot.data()
```

## AKCI08-005
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-005'].plot.data()
```

## AKCI08-007
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-007'].plot.data()
```

## AKCI08-008
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-008'].plot.data()
```

## AKCI08-009
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-009'].plot.data()
```

## AKCI08-011
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-011'].plot.data()
```

## AKCI08-012
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-012'].plot.data()
```

## AKCI08-013
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-013'].plot.data()
```

## AKCI08-015
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-015'].plot.data()
```

## AKCI08-016
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-016'].plot.data()
```

## AKCI08-017
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-017'].plot.data()
```

## AKCI08-018
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-018'].plot.data()
```

## AKCI08-021
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-021'].plot.data()
```

## AKCI08-023
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-023'].plot.data()
```

## AKCI08-024
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-024'].plot.data()
```

## AKCI08-026
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-026'].plot.data()
```

## AKCI08-027
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-027'].plot.data()
```

## AKCI08-028
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-028'].plot.data()
```

## AKCI08-029
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-029'].plot.data()
```

## AKCI08-031
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-031'].plot.data()
```

## AKCI08-032
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-032'].plot.data()
```

## AKCI08-033
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-033'].plot.data()
```

## AKCI08-035
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-035'].plot.data()
```

## AKCI08-037A
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-037A'].plot.data()
```

## AKCI08-037B
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-037B'].plot.data()
```

## AKCI08-039
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-039'].plot.data()
```

## AKCI08-040
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-040'].plot.data()
```

## AKCI08-041
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-041'].plot.data()
```

## AKCI08-042
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-042'].plot.data()
```

## AKCI08-043
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-043'].plot.data()
```

## AKCI08-044
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-044'].plot.data()
```

## AKCI08-045
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-045'].plot.data()
```

## AKCI08-047
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-047'].plot.data()
```

## AKCI08-048
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-048'].plot.data()
```

## AKCI08-049
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-049'].plot.data()
```

## AKCI08-050
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-050'].plot.data()
```

## AKCI08-051
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-051'].plot.data()
```

## AKCI08-052
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-052'].plot.data()
```

## AKCI08-054
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-054'].plot.data()
```

## AKCI08-055
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-055'].plot.data()
```

## AKCI08-056
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-056'].plot.data()
```

## AKCI08-057
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-057'].plot.data()
```

## AKCI08-058
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-058'].plot.data()
```

## AKCI08-059
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-059'].plot.data()
```

## AKCI08-060
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-060'].plot.data()
```

## AKCI08-061
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-061'].plot.data()
```

## AKCI08-063
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-063'].plot.data()
```

## AKCI08-065
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-065'].plot.data()
```

## AKCI08-066
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-066'].plot.data()
```

## AKCI08-067
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-067'].plot.data()
```

## AKCI08-069
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-069'].plot.data()
```

## AKCI08-070
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-070'].plot.data()
```

## AKCI08-071
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-071'].plot.data()
```

## AKCI08-072
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-072'].plot.data()
```

## AKCI08-073
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-073'].plot.data()
```

## AKCI08-074
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-074'].plot.data()
```

## AKCI08-076
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-076'].plot.data()
```

## AKCI08-079
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-079'].plot.data()
```

## AKCI08-080
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-080'].plot.data()
```

## AKCI08-081
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-081'].plot.data()
```

## AKCI08-083
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-083'].plot.data()
```

## AKCI08-084
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-084'].plot.data()
```

## AKCI08-086
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-086'].plot.data()
```

## AKCI08-087
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-087'].plot.data()
```

## AKCI08-088
        

```{code-cell}
:tags: [full-width, remove-input]

cat['AKCI08-088'].plot.data()
```

## KB01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KB01'].plot.data()
```

## KB02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KB02'].plot.data()
```

## KB03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KB03'].plot.data()
```

## KB04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KB04'].plot.data()
```

## KB05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KB05'].plot.data()
```

## KRM
        

```{code-cell}
:tags: [full-width, remove-input]

cat['KRM'].plot.data()
```
