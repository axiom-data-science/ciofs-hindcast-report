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

(page:ctd_transects_otf_kbnerr)=
# CTD Transect (OTF KBNERR): Repeated from Anchor Point

* CTD profiles 2003-2006 - OTF KBNERR
* ctd_transects_otf_kbnerr
* Daily in July, 2003 to 2006

CTD Transect Across Anchor Point, for GEM Project 030670.

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf
Project description: https://evostc.state.ak.us/restoration-projects/project-search/monitoring-dynamics-of-the-alaska-coastal-current-and-development-of-applications-for-management-of-cook-inlet-salmon-040670/


These data were not included in the NWGOA model/data comparison

```{dropdown} Dataset metadata

|     | Dataset    | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                        |
|----:|:-----------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:---------------------------------------------------------------|
|   0 | 2003-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-01 18:35:00 |       59.825  |       -152.438 | 2003-07-01 12:02:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   1 | 2003-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-02 12:03:00 |       59.825  |       -152.438 | 2003-07-02 06:40:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   2 | 2003-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-04 17:02:00 |       59.825  |       -152.438 | 2003-07-04 12:00:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   3 | 2003-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-05 13:05:00 |       59.825  |       -152.438 | 2003-07-05 07:51:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   4 | 2003-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-06 21:59:00 |       59.825  |       -152.438 | 2003-07-06 16:00:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   5 | 2003-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-07 11:27:00 |       59.825  |       -152.438 | 2003-07-07 06:22:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   6 | 2003-07-08 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-08 15:55:00 |       59.825  |       -152.438 | 2003-07-08 10:14:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   7 | 2003-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-09 11:54:00 |       59.825  |       -152.438 | 2003-07-09 05:43:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   8 | 2003-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-10 17:04:00 |       59.825  |       -152.438 | 2003-07-10 10:21:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|   9 | 2003-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-11 12:50:00 |       59.825  |       -152.438 | 2003-07-11 06:36:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  10 | 2003-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-12 16:26:00 |       59.825  |       -152.438 | 2003-07-12 10:24:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  11 | 2003-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-13 13:10:00 |       59.825  |       -152.438 | 2003-07-13 06:05:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  12 | 2003-07-14 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-14 20:00:00 |       59.825  |       -152.438 | 2003-07-14 12:43:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  13 | 2003-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.225 | 2003-07-15 13:39:00 |       59.8367 |       -152.438 | 2003-07-15 07:03:00 | https://researchworkspace.com/files/39890736/otf2003_sbe19.txt |
|  14 | 2003-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2003-07-16 17:56:00 |       59.825  |       -152.367 | 2003-07-16 12:24:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  15 | 2003-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-17 13:07:00 |       59.825  |       -152.438 | 2003-07-17 06:54:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  16 | 2003-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-18 19:23:00 |       59.825  |       -152.438 | 2003-07-18 13:05:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  17 | 2003-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.438 | 2003-07-19 05:59:00 |       59.8733 |       -152.438 | 2003-07-19 05:59:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  18 | 2003-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-21 10:34:00 |       59.825  |       -152.438 | 2003-07-21 04:48:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  19 | 2003-07-22 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-22 15:54:00 |       59.825  |       -152.438 | 2003-07-22 10:26:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  20 | 2003-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-23 12:57:00 |       59.825  |       -152.438 | 2003-07-23 07:00:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  21 | 2003-07-24 | trajectoryProfile | ['temp', 'salt'] |       59.8567 |       -152.152 | 2003-07-24 14:00:00 |       59.825  |       -152.33  | 2003-07-24 10:45:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  22 | 2003-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-25 12:17:00 |       59.825  |       -152.438 | 2003-07-25 06:17:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  23 | 2003-07-26 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-26 16:19:00 |       59.825  |       -152.438 | 2003-07-26 10:29:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  24 | 2003-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-28 17:06:00 |       59.825  |       -152.438 | 2003-07-28 10:52:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  25 | 2003-07-29 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-29 10:15:00 |       59.825  |       -152.438 | 2003-07-29 04:58:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  26 | 2003-07-30 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2003-07-30 14:11:00 |       59.825  |       -152.438 | 2003-07-30 09:32:00 | https://researchworkspace.com/files/39890793/otf2003_sbe25.txt |
|  27 | 2004-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.225 | 2004-07-01 13:26:00 |       59.8367 |       -152.438 | 2004-07-01 08:37:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  28 | 2004-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-02 11:18:00 |       59.825  |       -152.438 | 2004-07-02 04:46:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  29 | 2004-07-03 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-03 15:49:00 |       59.825  |       -152.438 | 2004-07-03 10:50:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  30 | 2004-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-04 10:19:00 |       59.825  |       -152.438 | 2004-07-04 05:25:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  31 | 2004-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-05 16:34:00 |       59.825  |       -152.438 | 2004-07-05 10:34:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  32 | 2004-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-06 18:23:00 |       59.825  |       -152.438 | 2004-07-06 13:37:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  33 | 2004-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-07 10:01:00 |       59.825  |       -152.438 | 2004-07-07 04:56:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  34 | 2004-07-08 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-08 17:05:00 |       59.825  |       -152.438 | 2004-07-08 10:41:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  35 | 2004-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-09 10:21:00 |       59.825  |       -152.438 | 2004-07-09 04:53:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  36 | 2004-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-10 15:20:00 |       59.825  |       -152.438 | 2004-07-10 09:16:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  37 | 2004-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-11 11:51:00 |       59.825  |       -152.438 | 2004-07-11 05:41:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  38 | 2004-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-12 15:39:00 |       59.825  |       -152.438 | 2004-07-12 10:23:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  39 | 2004-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-13 12:44:00 |       59.825  |       -152.438 | 2004-07-13 05:48:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  40 | 2004-07-14 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2004-07-14 23:48:00 |       59.825  |       -152.367 | 2004-07-14 11:31:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  41 | 2004-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-15 12:35:00 |       59.825  |       -152.438 | 2004-07-15 00:46:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  42 | 2004-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-16 18:05:00 |       59.825  |       -152.438 | 2004-07-16 10:56:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  43 | 2004-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-17 10:55:00 |       59.825  |       -152.438 | 2004-07-17 05:01:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  44 | 2004-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-18 17:16:00 |       59.825  |       -152.438 | 2004-07-18 10:52:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  45 | 2004-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-19 10:43:00 |       59.825  |       -152.438 | 2004-07-19 05:11:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  46 | 2004-07-20 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2004-07-20 15:36:00 |       59.825  |       -152.367 | 2004-07-20 11:14:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  47 | 2004-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-21 10:26:00 |       59.825  |       -152.438 | 2004-07-21 05:27:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  48 | 2004-07-22 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-22 17:38:00 |       59.825  |       -152.438 | 2004-07-22 11:11:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  49 | 2004-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-23 11:33:00 |       59.825  |       -152.438 | 2004-07-23 06:30:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  50 | 2004-07-24 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-24 16:29:00 |       59.825  |       -152.438 | 2004-07-24 10:19:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  51 | 2004-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-25 11:33:00 |       59.825  |       -152.438 | 2004-07-25 06:09:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  52 | 2004-07-27 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-27 16:42:00 |       59.825  |       -152.438 | 2004-07-27 10:16:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  53 | 2004-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-28 12:50:00 |       59.825  |       -152.438 | 2004-07-28 07:00:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  54 | 2004-07-29 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-29 16:23:00 |       59.825  |       -152.438 | 2004-07-29 10:32:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  55 | 2004-07-30 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2004-07-30 11:19:00 |       59.825  |       -152.438 | 2004-07-30 04:39:00 | https://researchworkspace.com/files/39886054/otf2004.txt       |
|  56 | 2005-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-01 21:05:00 |       59.825  |       -152.438 | 2005-07-01 14:15:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  57 | 2005-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-02 14:22:00 |       59.825  |       -152.438 | 2005-07-02 06:52:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  58 | 2005-07-03 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-03 19:16:00 |       59.825  |       -152.438 | 2005-07-03 12:56:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  59 | 2005-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-04 13:45:00 |       59.825  |       -152.438 | 2005-07-04 05:56:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  60 | 2005-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-05 21:15:00 |       59.825  |       -152.438 | 2005-07-05 12:58:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  61 | 2005-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-06 14:45:00 |       59.825  |       -152.438 | 2005-07-06 06:30:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  62 | 2005-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-07 21:07:00 |       59.825  |       -152.438 | 2005-07-07 12:29:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  63 | 2005-07-08 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-08 13:25:00 |       59.825  |       -152.438 | 2005-07-08 05:58:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  64 | 2005-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-09 18:33:00 |       59.825  |       -152.438 | 2005-07-09 11:22:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  65 | 2005-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.293 | 2005-07-10 10:43:00 |       59.85   |       -152.438 | 2005-07-10 06:59:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  66 | 2005-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-11 17:21:00 |       59.825  |       -152.438 | 2005-07-11 10:16:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  67 | 2005-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-12 14:28:00 |       59.825  |       -152.438 | 2005-07-12 07:22:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  68 | 2005-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-13 18:21:00 |       59.825  |       -152.438 | 2005-07-13 12:06:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  69 | 2005-07-14 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-14 12:30:00 |       59.825  |       -152.438 | 2005-07-14 06:42:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  70 | 2005-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-15 19:20:00 |       59.825  |       -152.438 | 2005-07-15 12:05:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  71 | 2005-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-16 13:56:00 |       59.825  |       -152.438 | 2005-07-16 07:54:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  72 | 2005-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-17 15:55:00 |       59.825  |       -152.438 | 2005-07-17 10:46:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  73 | 2005-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-18 11:23:00 |       59.825  |       -152.438 | 2005-07-18 05:38:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  74 | 2005-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-19 18:26:00 |       59.825  |       -152.438 | 2005-07-19 12:25:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  75 | 2005-07-20 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-20 15:54:00 |       59.825  |       -152.438 | 2005-07-20 07:41:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  76 | 2005-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-21 16:22:00 |       59.825  |       -152.438 | 2005-07-21 09:51:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  77 | 2005-07-22 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-22 13:36:00 |       59.825  |       -152.438 | 2005-07-22 05:40:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  78 | 2005-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-23 18:26:00 |       59.825  |       -152.438 | 2005-07-23 11:16:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  79 | 2005-07-24 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-24 14:14:00 |       59.825  |       -152.438 | 2005-07-24 06:23:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  80 | 2005-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-25 18:21:00 |       59.825  |       -152.438 | 2005-07-25 11:11:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  81 | 2005-07-26 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-26 14:00:00 |       59.825  |       -152.438 | 2005-07-26 06:32:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  82 | 2005-07-27 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-27 19:14:00 |       59.825  |       -152.438 | 2005-07-27 13:43:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  83 | 2005-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-28 12:45:00 |       59.825  |       -152.438 | 2005-07-28 06:37:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  84 | 2005-07-29 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-29 17:02:00 |       59.825  |       -152.438 | 2005-07-29 10:13:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  85 | 2005-07-30 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2005-07-30 15:37:00 |       59.825  |       -152.438 | 2005-07-30 06:55:00 | https://researchworkspace.com/files/39886055/otf2005.txt       |
|  86 | 2006-07-01 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-01 16:37:00 |       59.825  |       -152.438 | 2006-07-01 11:14:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  87 | 2006-07-02 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-02 11:40:00 |       59.825  |       -152.438 | 2006-07-02 06:38:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  88 | 2006-07-03 | trajectoryProfile | ['temp', 'salt'] |       59.825  |       -152.152 | 2006-07-03 09:29:00 |       59.825  |       -152.152 | 2006-07-03 09:29:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  89 | 2006-07-04 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2006-07-04 11:52:00 |       59.825  |       -152.367 | 2006-07-04 07:48:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  90 | 2006-07-05 | trajectoryProfile | ['temp', 'salt'] |       59.8617 |       -152.152 | 2006-07-05 14:21:00 |       59.825  |       -152.367 | 2006-07-05 10:06:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  91 | 2006-07-06 | trajectoryProfile | ['temp', 'salt'] |       59.8567 |       -152.152 | 2006-07-06 12:11:00 |       59.825  |       -152.33  | 2006-07-06 08:06:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  92 | 2006-07-07 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-07 14:15:00 |       59.825  |       -152.438 | 2006-07-07 08:15:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  93 | 2006-07-09 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-09 16:09:00 |       59.825  |       -152.438 | 2006-07-09 09:57:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  94 | 2006-07-10 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-10 12:29:00 |       59.825  |       -152.438 | 2006-07-10 06:37:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  95 | 2006-07-11 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-11 14:20:00 |       59.825  |       -152.438 | 2006-07-11 08:43:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  96 | 2006-07-12 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-12 12:17:00 |       59.825  |       -152.438 | 2006-07-12 05:45:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  97 | 2006-07-13 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-13 15:48:00 |       59.825  |       -152.438 | 2006-07-13 10:11:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  98 | 2006-07-15 | trajectoryProfile | ['temp', 'salt'] |       59.825  |       -152.152 | 2006-07-15 09:21:00 |       59.825  |       -152.152 | 2006-07-15 09:21:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
|  99 | 2006-07-16 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-16 16:34:00 |       59.825  |       -152.438 | 2006-07-16 10:40:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 100 | 2006-07-17 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-17 13:08:00 |       59.825  |       -152.438 | 2006-07-17 07:27:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 101 | 2006-07-18 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-18 13:59:00 |       59.825  |       -152.438 | 2006-07-18 08:14:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 102 | 2006-07-19 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.367 | 2006-07-19 08:28:00 |       59.8617 |       -152.438 | 2006-07-19 07:23:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 103 | 2006-07-21 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-21 16:14:00 |       59.825  |       -152.438 | 2006-07-21 09:43:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 104 | 2006-07-23 | trajectoryProfile | ['temp', 'salt'] |       59.8367 |       -152.152 | 2006-07-23 09:59:00 |       59.825  |       -152.225 | 2006-07-23 08:47:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 105 | 2006-07-25 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-25 19:30:00 |       59.825  |       -152.438 | 2006-07-25 12:55:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 106 | 2006-07-26 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-26 12:10:00 |       59.825  |       -152.438 | 2006-07-26 06:09:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 107 | 2006-07-27 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.152 | 2006-07-27 17:29:00 |       59.825  |       -152.438 | 2006-07-27 11:08:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |
| 108 | 2006-07-28 | trajectoryProfile | ['temp', 'salt'] |       59.8733 |       -152.438 | 2006-07-28 07:24:00 |       59.8733 |       -152.438 | 2006-07-28 07:24:00 | https://researchworkspace.com/files/39886053/otf2006.txt       |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_transects_otf_kbnerr"))
```

## Map of CTD Transects
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_otf_kbnerr")("ctd_transects_otf_kbnerr")
```


```{div} full-width
## 2003
```

+++

2003-07-01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-01'].plot.salt() + cat['2003-07-01'].plot.temp()
```

2003-07-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-02'].plot.salt() + cat['2003-07-02'].plot.temp()
```

2003-07-04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-04'].plot.salt() + cat['2003-07-04'].plot.temp()
```

2003-07-05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-05'].plot.salt() + cat['2003-07-05'].plot.temp()
```

2003-07-06
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-06'].plot.salt() + cat['2003-07-06'].plot.temp()
```

2003-07-07
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-07'].plot.salt() + cat['2003-07-07'].plot.temp()
```

2003-07-08
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-08'].plot.salt() + cat['2003-07-08'].plot.temp()
```

2003-07-09
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-09'].plot.salt() + cat['2003-07-09'].plot.temp()
```

2003-07-10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-10'].plot.salt() + cat['2003-07-10'].plot.temp()
```

2003-07-11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-11'].plot.salt() + cat['2003-07-11'].plot.temp()
```

2003-07-12
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-12'].plot.salt() + cat['2003-07-12'].plot.temp()
```

2003-07-13
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-13'].plot.salt() + cat['2003-07-13'].plot.temp()
```

2003-07-14
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-14'].plot.salt() + cat['2003-07-14'].plot.temp()
```

2003-07-15
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-15'].plot.salt() + cat['2003-07-15'].plot.temp()
```

2003-07-16
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-16'].plot.salt() + cat['2003-07-16'].plot.temp()
```

2003-07-17
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-17'].plot.salt() + cat['2003-07-17'].plot.temp()
```

2003-07-18
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-18'].plot.salt() + cat['2003-07-18'].plot.temp()
```

2003-07-19
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-19'].plot.salt() + cat['2003-07-19'].plot.temp()
```

2003-07-21
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-21'].plot.salt() + cat['2003-07-21'].plot.temp()
```

2003-07-22
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-22'].plot.salt() + cat['2003-07-22'].plot.temp()
```

2003-07-23
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-23'].plot.salt() + cat['2003-07-23'].plot.temp()
```

2003-07-24
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-24'].plot.salt() + cat['2003-07-24'].plot.temp()
```

2003-07-25
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-25'].plot.salt() + cat['2003-07-25'].plot.temp()
```

2003-07-26
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-26'].plot.salt() + cat['2003-07-26'].plot.temp()
```

2003-07-28
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-28'].plot.salt() + cat['2003-07-28'].plot.temp()
```

2003-07-29
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-29'].plot.salt() + cat['2003-07-29'].plot.temp()
```

2003-07-30
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2003-07-30'].plot.salt() + cat['2003-07-30'].plot.temp()
```


```{div} full-width
## 2004
```

+++

2004-07-01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-01'].plot.salt() + cat['2004-07-01'].plot.temp()
```

2004-07-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-02'].plot.salt() + cat['2004-07-02'].plot.temp()
```

2004-07-03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-03'].plot.salt() + cat['2004-07-03'].plot.temp()
```

2004-07-04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-04'].plot.salt() + cat['2004-07-04'].plot.temp()
```

2004-07-05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-05'].plot.salt() + cat['2004-07-05'].plot.temp()
```

2004-07-06
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-06'].plot.salt() + cat['2004-07-06'].plot.temp()
```

2004-07-07
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-07'].plot.salt() + cat['2004-07-07'].plot.temp()
```

2004-07-08
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-08'].plot.salt() + cat['2004-07-08'].plot.temp()
```

2004-07-09
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-09'].plot.salt() + cat['2004-07-09'].plot.temp()
```

2004-07-10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-10'].plot.salt() + cat['2004-07-10'].plot.temp()
```

2004-07-11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-11'].plot.salt() + cat['2004-07-11'].plot.temp()
```

2004-07-12
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-12'].plot.salt() + cat['2004-07-12'].plot.temp()
```

2004-07-13
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-13'].plot.salt() + cat['2004-07-13'].plot.temp()
```

2004-07-14
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-14'].plot.salt() + cat['2004-07-14'].plot.temp()
```

2004-07-15
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-15'].plot.salt() + cat['2004-07-15'].plot.temp()
```

2004-07-16
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-16'].plot.salt() + cat['2004-07-16'].plot.temp()
```

2004-07-17
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-17'].plot.salt() + cat['2004-07-17'].plot.temp()
```

2004-07-18
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-18'].plot.salt() + cat['2004-07-18'].plot.temp()
```

2004-07-19
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-19'].plot.salt() + cat['2004-07-19'].plot.temp()
```

2004-07-20
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-20'].plot.salt() + cat['2004-07-20'].plot.temp()
```

2004-07-21
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-21'].plot.salt() + cat['2004-07-21'].plot.temp()
```

2004-07-22
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-22'].plot.salt() + cat['2004-07-22'].plot.temp()
```

2004-07-23
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-23'].plot.salt() + cat['2004-07-23'].plot.temp()
```

2004-07-24
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-24'].plot.salt() + cat['2004-07-24'].plot.temp()
```

2004-07-25
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-25'].plot.salt() + cat['2004-07-25'].plot.temp()
```

2004-07-27
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-27'].plot.salt() + cat['2004-07-27'].plot.temp()
```

2004-07-28
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-28'].plot.salt() + cat['2004-07-28'].plot.temp()
```

2004-07-29
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-29'].plot.salt() + cat['2004-07-29'].plot.temp()
```

2004-07-30
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2004-07-30'].plot.salt() + cat['2004-07-30'].plot.temp()
```


```{div} full-width
## 2005
```

+++

2005-07-01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-01'].plot.salt() + cat['2005-07-01'].plot.temp()
```

2005-07-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-02'].plot.salt() + cat['2005-07-02'].plot.temp()
```

2005-07-03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-03'].plot.salt() + cat['2005-07-03'].plot.temp()
```

2005-07-04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-04'].plot.salt() + cat['2005-07-04'].plot.temp()
```

2005-07-05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-05'].plot.salt() + cat['2005-07-05'].plot.temp()
```

2005-07-06
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-06'].plot.salt() + cat['2005-07-06'].plot.temp()
```

2005-07-07
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-07'].plot.salt() + cat['2005-07-07'].plot.temp()
```

2005-07-08
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-08'].plot.salt() + cat['2005-07-08'].plot.temp()
```

2005-07-09
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-09'].plot.salt() + cat['2005-07-09'].plot.temp()
```

2005-07-10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-10'].plot.salt() + cat['2005-07-10'].plot.temp()
```

2005-07-11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-11'].plot.salt() + cat['2005-07-11'].plot.temp()
```

2005-07-12
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-12'].plot.salt() + cat['2005-07-12'].plot.temp()
```

2005-07-13
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-13'].plot.salt() + cat['2005-07-13'].plot.temp()
```

2005-07-14
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-14'].plot.salt() + cat['2005-07-14'].plot.temp()
```

2005-07-15
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-15'].plot.salt() + cat['2005-07-15'].plot.temp()
```

2005-07-16
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-16'].plot.salt() + cat['2005-07-16'].plot.temp()
```

2005-07-17
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-17'].plot.salt() + cat['2005-07-17'].plot.temp()
```

2005-07-18
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-18'].plot.salt() + cat['2005-07-18'].plot.temp()
```

2005-07-19
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-19'].plot.salt() + cat['2005-07-19'].plot.temp()
```

2005-07-20
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-20'].plot.salt() + cat['2005-07-20'].plot.temp()
```

2005-07-21
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-21'].plot.salt() + cat['2005-07-21'].plot.temp()
```

2005-07-22
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-22'].plot.salt() + cat['2005-07-22'].plot.temp()
```

2005-07-23
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-23'].plot.salt() + cat['2005-07-23'].plot.temp()
```

2005-07-24
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-24'].plot.salt() + cat['2005-07-24'].plot.temp()
```

2005-07-25
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-25'].plot.salt() + cat['2005-07-25'].plot.temp()
```

2005-07-26
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-26'].plot.salt() + cat['2005-07-26'].plot.temp()
```

2005-07-27
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-27'].plot.salt() + cat['2005-07-27'].plot.temp()
```

2005-07-28
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-28'].plot.salt() + cat['2005-07-28'].plot.temp()
```

2005-07-29
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-29'].plot.salt() + cat['2005-07-29'].plot.temp()
```

2005-07-30
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2005-07-30'].plot.salt() + cat['2005-07-30'].plot.temp()
```


```{div} full-width
## 2006
```

+++

2006-07-01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-01'].plot.salt() + cat['2006-07-01'].plot.temp()
```

2006-07-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-02'].plot.salt() + cat['2006-07-02'].plot.temp()
```

2006-07-03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-03'].plot.salt() + cat['2006-07-03'].plot.temp()
```

2006-07-04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-04'].plot.salt() + cat['2006-07-04'].plot.temp()
```

2006-07-05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-05'].plot.salt() + cat['2006-07-05'].plot.temp()
```

2006-07-06
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-06'].plot.salt() + cat['2006-07-06'].plot.temp()
```

2006-07-07
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-07'].plot.salt() + cat['2006-07-07'].plot.temp()
```

2006-07-09
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-09'].plot.salt() + cat['2006-07-09'].plot.temp()
```

2006-07-10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-10'].plot.salt() + cat['2006-07-10'].plot.temp()
```

2006-07-11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-11'].plot.salt() + cat['2006-07-11'].plot.temp()
```

2006-07-12
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-12'].plot.salt() + cat['2006-07-12'].plot.temp()
```

2006-07-13
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-13'].plot.salt() + cat['2006-07-13'].plot.temp()
```

2006-07-15
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-15'].plot.salt() + cat['2006-07-15'].plot.temp()
```

2006-07-16
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-16'].plot.salt() + cat['2006-07-16'].plot.temp()
```

2006-07-17
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-17'].plot.salt() + cat['2006-07-17'].plot.temp()
```

2006-07-18
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-18'].plot.salt() + cat['2006-07-18'].plot.temp()
```

2006-07-19
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-19'].plot.salt() + cat['2006-07-19'].plot.temp()
```

2006-07-21
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-21'].plot.salt() + cat['2006-07-21'].plot.temp()
```

2006-07-23
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-23'].plot.salt() + cat['2006-07-23'].plot.temp()
```

2006-07-25
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-25'].plot.salt() + cat['2006-07-25'].plot.temp()
```

2006-07-26
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-26'].plot.salt() + cat['2006-07-26'].plot.temp()
```

2006-07-27
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-27'].plot.salt() + cat['2006-07-27'].plot.temp()
```

2006-07-28
        

```{code-cell}
:tags: [full-width, remove-input]

cat['2006-07-28'].plot.salt() + cat['2006-07-28'].plot.temp()
```
