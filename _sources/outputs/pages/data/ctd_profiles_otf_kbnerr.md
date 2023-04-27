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

# OTF KBNERR: Repeat CTD transect from Anchor Point in Cook Inlet

* CTD profiles 2003-2006 - OTF KBNERR
* ctd_profiles_otf_kbnerr
* Daily in July, 2003 to 2006

CTD Profiles Across Anchor Point Transect, for GEM Project 030670.

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf
Project description: https://evostc.state.ak.us/restoration-projects/project-search/monitoring-dynamics-of-the-alaska-coastal-current-and-development-of-applications-for-management-of-cook-inlet-salmon-040670/


These data were not included in the NWGOA model/data comparison

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_otf_kbnerr"))
```

## Map of CTD Profiles in Consistent Transect
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_otf_kbnerr")("ctd_profiles_otf_kbnerr")
    
```

## 2003

+++

2003-07-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-01T18:35:00.000000000 |        59.825 |       -152.438 | 2003-07-01T12:02:00.000000000 |


```{code-cell}
cat['2003-07-01'].plot.salt() + cat['2003-07-01'].plot.temp()
```

2003-07-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-02T12:03:00.000000000 |        59.825 |       -152.438 | 2003-07-02T06:40:00.000000000 |


```{code-cell}
cat['2003-07-02'].plot.salt() + cat['2003-07-02'].plot.temp()
```

2003-07-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-04T17:02:00.000000000 |        59.825 |       -152.438 | 2003-07-04T12:00:00.000000000 |


```{code-cell}
cat['2003-07-04'].plot.salt() + cat['2003-07-04'].plot.temp()
```

2003-07-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-05T13:05:00.000000000 |        59.825 |       -152.438 | 2003-07-05T07:51:00.000000000 |


```{code-cell}
cat['2003-07-05'].plot.salt() + cat['2003-07-05'].plot.temp()
```

2003-07-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-06T21:59:00.000000000 |        59.825 |       -152.438 | 2003-07-06T16:00:00.000000000 |


```{code-cell}
cat['2003-07-06'].plot.salt() + cat['2003-07-06'].plot.temp()
```

2003-07-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-07T11:27:00.000000000 |        59.825 |       -152.438 | 2003-07-07T06:22:00.000000000 |


```{code-cell}
cat['2003-07-07'].plot.salt() + cat['2003-07-07'].plot.temp()
```

2003-07-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-08T15:55:00.000000000 |        59.825 |       -152.438 | 2003-07-08T10:14:00.000000000 |


```{code-cell}
cat['2003-07-08'].plot.salt() + cat['2003-07-08'].plot.temp()
```

2003-07-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-09T11:54:00.000000000 |        59.825 |       -152.438 | 2003-07-09T05:43:00.000000000 |


```{code-cell}
cat['2003-07-09'].plot.salt() + cat['2003-07-09'].plot.temp()
```

2003-07-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-10T17:04:00.000000000 |        59.825 |       -152.438 | 2003-07-10T10:21:00.000000000 |


```{code-cell}
cat['2003-07-10'].plot.salt() + cat['2003-07-10'].plot.temp()
```

2003-07-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-11T12:50:00.000000000 |        59.825 |       -152.438 | 2003-07-11T06:36:00.000000000 |


```{code-cell}
cat['2003-07-11'].plot.salt() + cat['2003-07-11'].plot.temp()
```

2003-07-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-12T16:26:00.000000000 |        59.825 |       -152.438 | 2003-07-12T10:24:00.000000000 |


```{code-cell}
cat['2003-07-12'].plot.salt() + cat['2003-07-12'].plot.temp()
```

2003-07-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-13T13:10:00.000000000 |        59.825 |       -152.438 | 2003-07-13T06:05:00.000000000 |


```{code-cell}
cat['2003-07-13'].plot.salt() + cat['2003-07-13'].plot.temp()
```

2003-07-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-14T20:00:00.000000000 |        59.825 |       -152.438 | 2003-07-14T12:43:00.000000000 |


```{code-cell}
cat['2003-07-14'].plot.salt() + cat['2003-07-14'].plot.temp()
```

2003-07-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.225 | 2003-07-15T13:39:00.000000000 |       59.8367 |       -152.438 | 2003-07-15T07:03:00.000000000 |


```{code-cell}
cat['2003-07-15'].plot.salt() + cat['2003-07-15'].plot.temp()
```

2003-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8617 |       -152.152 | 2003-07-16T17:56:00.000000000 |        59.825 |       -152.367 | 2003-07-16T12:24:00.000000000 |


```{code-cell}
cat['2003-07-16'].plot.salt() + cat['2003-07-16'].plot.temp()
```

2003-07-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-17T13:07:00.000000000 |        59.825 |       -152.438 | 2003-07-17T06:54:00.000000000 |


```{code-cell}
cat['2003-07-17'].plot.salt() + cat['2003-07-17'].plot.temp()
```

2003-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-18T19:23:00.000000000 |        59.825 |       -152.438 | 2003-07-18T13:05:00.000000000 |


```{code-cell}
cat['2003-07-18'].plot.salt() + cat['2003-07-18'].plot.temp()
```

2003-07-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.438 | 2003-07-19T05:59:00.000000000 |       59.8733 |       -152.438 | 2003-07-19T05:59:00.000000000 |


```{code-cell}
cat['2003-07-19'].plot.salt() + cat['2003-07-19'].plot.temp()
```

2003-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-21T10:34:00.000000000 |        59.825 |       -152.438 | 2003-07-21T04:48:00.000000000 |


```{code-cell}
cat['2003-07-21'].plot.salt() + cat['2003-07-21'].plot.temp()
```

2003-07-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-22T15:54:00.000000000 |        59.825 |       -152.438 | 2003-07-22T10:26:00.000000000 |


```{code-cell}
cat['2003-07-22'].plot.salt() + cat['2003-07-22'].plot.temp()
```

2003-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-23T12:57:00.000000000 |        59.825 |       -152.438 | 2003-07-23T07:00:00.000000000 |


```{code-cell}
cat['2003-07-23'].plot.salt() + cat['2003-07-23'].plot.temp()
```

2003-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8567 |       -152.152 | 2003-07-24T14:00:00.000000000 |        59.825 |        -152.33 | 2003-07-24T10:45:00.000000000 |


```{code-cell}
cat['2003-07-24'].plot.salt() + cat['2003-07-24'].plot.temp()
```

2003-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-25T12:17:00.000000000 |        59.825 |       -152.438 | 2003-07-25T06:17:00.000000000 |


```{code-cell}
cat['2003-07-25'].plot.salt() + cat['2003-07-25'].plot.temp()
```

2003-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-26T16:19:00.000000000 |        59.825 |       -152.438 | 2003-07-26T10:29:00.000000000 |


```{code-cell}
cat['2003-07-26'].plot.salt() + cat['2003-07-26'].plot.temp()
```

2003-07-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-28T17:06:00.000000000 |        59.825 |       -152.438 | 2003-07-28T10:52:00.000000000 |


```{code-cell}
cat['2003-07-28'].plot.salt() + cat['2003-07-28'].plot.temp()
```

2003-07-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-29T10:15:00.000000000 |        59.825 |       -152.438 | 2003-07-29T04:58:00.000000000 |


```{code-cell}
cat['2003-07-29'].plot.salt() + cat['2003-07-29'].plot.temp()
```

2003-07-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2003-07-30T14:11:00.000000000 |        59.825 |       -152.438 | 2003-07-30T09:32:00.000000000 |


```{code-cell}
cat['2003-07-30'].plot.salt() + cat['2003-07-30'].plot.temp()
```

## 2004

+++

2004-07-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.225 | 2004-07-01T13:26:00.000000000 |       59.8367 |       -152.438 | 2004-07-01T08:37:00.000000000 |


```{code-cell}
cat['2004-07-01'].plot.salt() + cat['2004-07-01'].plot.temp()
```

2004-07-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-02T11:18:00.000000000 |        59.825 |       -152.438 | 2004-07-02T04:46:00.000000000 |


```{code-cell}
cat['2004-07-02'].plot.salt() + cat['2004-07-02'].plot.temp()
```

2004-07-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-03T15:49:00.000000000 |        59.825 |       -152.438 | 2004-07-03T10:50:00.000000000 |


```{code-cell}
cat['2004-07-03'].plot.salt() + cat['2004-07-03'].plot.temp()
```

2004-07-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-04T10:19:00.000000000 |        59.825 |       -152.438 | 2004-07-04T05:25:00.000000000 |


```{code-cell}
cat['2004-07-04'].plot.salt() + cat['2004-07-04'].plot.temp()
```

2004-07-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-05T16:34:00.000000000 |        59.825 |       -152.438 | 2004-07-05T10:34:00.000000000 |


```{code-cell}
cat['2004-07-05'].plot.salt() + cat['2004-07-05'].plot.temp()
```

2004-07-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-06T18:23:00.000000000 |        59.825 |       -152.438 | 2004-07-06T13:37:00.000000000 |


```{code-cell}
cat['2004-07-06'].plot.salt() + cat['2004-07-06'].plot.temp()
```

2004-07-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-07T10:01:00.000000000 |        59.825 |       -152.438 | 2004-07-07T04:56:00.000000000 |


```{code-cell}
cat['2004-07-07'].plot.salt() + cat['2004-07-07'].plot.temp()
```

2004-07-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-08T17:05:00.000000000 |        59.825 |       -152.438 | 2004-07-08T10:41:00.000000000 |


```{code-cell}
cat['2004-07-08'].plot.salt() + cat['2004-07-08'].plot.temp()
```

2004-07-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-09T10:21:00.000000000 |        59.825 |       -152.438 | 2004-07-09T04:53:00.000000000 |


```{code-cell}
cat['2004-07-09'].plot.salt() + cat['2004-07-09'].plot.temp()
```

2004-07-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-10T15:20:00.000000000 |        59.825 |       -152.438 | 2004-07-10T09:16:00.000000000 |


```{code-cell}
cat['2004-07-10'].plot.salt() + cat['2004-07-10'].plot.temp()
```

2004-07-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-11T11:51:00.000000000 |        59.825 |       -152.438 | 2004-07-11T05:41:00.000000000 |


```{code-cell}
cat['2004-07-11'].plot.salt() + cat['2004-07-11'].plot.temp()
```

2004-07-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-12T15:39:00.000000000 |        59.825 |       -152.438 | 2004-07-12T10:23:00.000000000 |


```{code-cell}
cat['2004-07-12'].plot.salt() + cat['2004-07-12'].plot.temp()
```

2004-07-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-13T12:44:00.000000000 |        59.825 |       -152.438 | 2004-07-13T05:48:00.000000000 |


```{code-cell}
cat['2004-07-13'].plot.salt() + cat['2004-07-13'].plot.temp()
```

2004-07-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8617 |       -152.152 | 2004-07-14T23:48:00.000000000 |        59.825 |       -152.367 | 2004-07-14T11:31:00.000000000 |


```{code-cell}
cat['2004-07-14'].plot.salt() + cat['2004-07-14'].plot.temp()
```

2004-07-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-15T12:35:00.000000000 |        59.825 |       -152.438 | 2004-07-15T00:46:00.000000000 |


```{code-cell}
cat['2004-07-15'].plot.salt() + cat['2004-07-15'].plot.temp()
```

2004-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-16T18:05:00.000000000 |        59.825 |       -152.438 | 2004-07-16T10:56:00.000000000 |


```{code-cell}
cat['2004-07-16'].plot.salt() + cat['2004-07-16'].plot.temp()
```

2004-07-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-17T10:55:00.000000000 |        59.825 |       -152.438 | 2004-07-17T05:01:00.000000000 |


```{code-cell}
cat['2004-07-17'].plot.salt() + cat['2004-07-17'].plot.temp()
```

2004-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-18T17:16:00.000000000 |        59.825 |       -152.438 | 2004-07-18T10:52:00.000000000 |


```{code-cell}
cat['2004-07-18'].plot.salt() + cat['2004-07-18'].plot.temp()
```

2004-07-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-19T10:43:00.000000000 |        59.825 |       -152.438 | 2004-07-19T05:11:00.000000000 |


```{code-cell}
cat['2004-07-19'].plot.salt() + cat['2004-07-19'].plot.temp()
```

2004-07-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8617 |       -152.152 | 2004-07-20T15:36:00.000000000 |        59.825 |       -152.367 | 2004-07-20T11:14:00.000000000 |


```{code-cell}
cat['2004-07-20'].plot.salt() + cat['2004-07-20'].plot.temp()
```

2004-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-21T10:26:00.000000000 |        59.825 |       -152.438 | 2004-07-21T05:27:00.000000000 |


```{code-cell}
cat['2004-07-21'].plot.salt() + cat['2004-07-21'].plot.temp()
```

2004-07-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-22T17:38:00.000000000 |        59.825 |       -152.438 | 2004-07-22T11:11:00.000000000 |


```{code-cell}
cat['2004-07-22'].plot.salt() + cat['2004-07-22'].plot.temp()
```

2004-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-23T11:33:00.000000000 |        59.825 |       -152.438 | 2004-07-23T06:30:00.000000000 |


```{code-cell}
cat['2004-07-23'].plot.salt() + cat['2004-07-23'].plot.temp()
```

2004-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-24T16:29:00.000000000 |        59.825 |       -152.438 | 2004-07-24T10:19:00.000000000 |


```{code-cell}
cat['2004-07-24'].plot.salt() + cat['2004-07-24'].plot.temp()
```

2004-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-25T11:33:00.000000000 |        59.825 |       -152.438 | 2004-07-25T06:09:00.000000000 |


```{code-cell}
cat['2004-07-25'].plot.salt() + cat['2004-07-25'].plot.temp()
```

2004-07-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-27T16:42:00.000000000 |        59.825 |       -152.438 | 2004-07-27T10:16:00.000000000 |


```{code-cell}
cat['2004-07-27'].plot.salt() + cat['2004-07-27'].plot.temp()
```

2004-07-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-28T12:50:00.000000000 |        59.825 |       -152.438 | 2004-07-28T07:00:00.000000000 |


```{code-cell}
cat['2004-07-28'].plot.salt() + cat['2004-07-28'].plot.temp()
```

2004-07-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-29T16:23:00.000000000 |        59.825 |       -152.438 | 2004-07-29T10:32:00.000000000 |


```{code-cell}
cat['2004-07-29'].plot.salt() + cat['2004-07-29'].plot.temp()
```

2004-07-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2004-07-30T11:19:00.000000000 |        59.825 |       -152.438 | 2004-07-30T04:39:00.000000000 |


```{code-cell}
cat['2004-07-30'].plot.salt() + cat['2004-07-30'].plot.temp()
```

## 2005

+++

2005-07-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-01T21:05:00.000000000 |        59.825 |       -152.438 | 2005-07-01T14:15:00.000000000 |


```{code-cell}
cat['2005-07-01'].plot.salt() + cat['2005-07-01'].plot.temp()
```

2005-07-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-02T14:22:00.000000000 |        59.825 |       -152.438 | 2005-07-02T06:52:00.000000000 |


```{code-cell}
cat['2005-07-02'].plot.salt() + cat['2005-07-02'].plot.temp()
```

2005-07-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-03T19:16:00.000000000 |        59.825 |       -152.438 | 2005-07-03T12:56:00.000000000 |


```{code-cell}
cat['2005-07-03'].plot.salt() + cat['2005-07-03'].plot.temp()
```

2005-07-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-04T13:45:00.000000000 |        59.825 |       -152.438 | 2005-07-04T05:56:00.000000000 |


```{code-cell}
cat['2005-07-04'].plot.salt() + cat['2005-07-04'].plot.temp()
```

2005-07-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-05T21:15:00.000000000 |        59.825 |       -152.438 | 2005-07-05T12:58:00.000000000 |


```{code-cell}
cat['2005-07-05'].plot.salt() + cat['2005-07-05'].plot.temp()
```

2005-07-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-06T14:45:00.000000000 |        59.825 |       -152.438 | 2005-07-06T06:30:00.000000000 |


```{code-cell}
cat['2005-07-06'].plot.salt() + cat['2005-07-06'].plot.temp()
```

2005-07-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-07T21:07:00.000000000 |        59.825 |       -152.438 | 2005-07-07T12:29:00.000000000 |


```{code-cell}
cat['2005-07-07'].plot.salt() + cat['2005-07-07'].plot.temp()
```

2005-07-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-08T13:25:00.000000000 |        59.825 |       -152.438 | 2005-07-08T05:58:00.000000000 |


```{code-cell}
cat['2005-07-08'].plot.salt() + cat['2005-07-08'].plot.temp()
```

2005-07-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-09T18:33:00.000000000 |        59.825 |       -152.438 | 2005-07-09T11:22:00.000000000 |


```{code-cell}
cat['2005-07-09'].plot.salt() + cat['2005-07-09'].plot.temp()
```

2005-07-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.293 | 2005-07-10T10:43:00.000000000 |         59.85 |       -152.438 | 2005-07-10T06:59:00.000000000 |


```{code-cell}
cat['2005-07-10'].plot.salt() + cat['2005-07-10'].plot.temp()
```

2005-07-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-11T17:21:00.000000000 |        59.825 |       -152.438 | 2005-07-11T10:16:00.000000000 |


```{code-cell}
cat['2005-07-11'].plot.salt() + cat['2005-07-11'].plot.temp()
```

2005-07-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-12T14:28:00.000000000 |        59.825 |       -152.438 | 2005-07-12T07:22:00.000000000 |


```{code-cell}
cat['2005-07-12'].plot.salt() + cat['2005-07-12'].plot.temp()
```

2005-07-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-13T18:21:00.000000000 |        59.825 |       -152.438 | 2005-07-13T12:06:00.000000000 |


```{code-cell}
cat['2005-07-13'].plot.salt() + cat['2005-07-13'].plot.temp()
```

2005-07-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-14T12:30:00.000000000 |        59.825 |       -152.438 | 2005-07-14T06:42:00.000000000 |


```{code-cell}
cat['2005-07-14'].plot.salt() + cat['2005-07-14'].plot.temp()
```

2005-07-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-15T19:20:00.000000000 |        59.825 |       -152.438 | 2005-07-15T12:05:00.000000000 |


```{code-cell}
cat['2005-07-15'].plot.salt() + cat['2005-07-15'].plot.temp()
```

2005-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-16T13:56:00.000000000 |        59.825 |       -152.438 | 2005-07-16T07:54:00.000000000 |


```{code-cell}
cat['2005-07-16'].plot.salt() + cat['2005-07-16'].plot.temp()
```

2005-07-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-17T15:55:00.000000000 |        59.825 |       -152.438 | 2005-07-17T10:46:00.000000000 |


```{code-cell}
cat['2005-07-17'].plot.salt() + cat['2005-07-17'].plot.temp()
```

2005-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-18T11:23:00.000000000 |        59.825 |       -152.438 | 2005-07-18T05:38:00.000000000 |


```{code-cell}
cat['2005-07-18'].plot.salt() + cat['2005-07-18'].plot.temp()
```

2005-07-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-19T18:26:00.000000000 |        59.825 |       -152.438 | 2005-07-19T12:25:00.000000000 |


```{code-cell}
cat['2005-07-19'].plot.salt() + cat['2005-07-19'].plot.temp()
```

2005-07-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-20T15:54:00.000000000 |        59.825 |       -152.438 | 2005-07-20T07:41:00.000000000 |


```{code-cell}
cat['2005-07-20'].plot.salt() + cat['2005-07-20'].plot.temp()
```

2005-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-21T16:22:00.000000000 |        59.825 |       -152.438 | 2005-07-21T09:51:00.000000000 |


```{code-cell}
cat['2005-07-21'].plot.salt() + cat['2005-07-21'].plot.temp()
```

2005-07-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-22T13:36:00.000000000 |        59.825 |       -152.438 | 2005-07-22T05:40:00.000000000 |


```{code-cell}
cat['2005-07-22'].plot.salt() + cat['2005-07-22'].plot.temp()
```

2005-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-23T18:26:00.000000000 |        59.825 |       -152.438 | 2005-07-23T11:16:00.000000000 |


```{code-cell}
cat['2005-07-23'].plot.salt() + cat['2005-07-23'].plot.temp()
```

2005-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-24T14:14:00.000000000 |        59.825 |       -152.438 | 2005-07-24T06:23:00.000000000 |


```{code-cell}
cat['2005-07-24'].plot.salt() + cat['2005-07-24'].plot.temp()
```

2005-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-25T18:21:00.000000000 |        59.825 |       -152.438 | 2005-07-25T11:11:00.000000000 |


```{code-cell}
cat['2005-07-25'].plot.salt() + cat['2005-07-25'].plot.temp()
```

2005-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-26T14:00:00.000000000 |        59.825 |       -152.438 | 2005-07-26T06:32:00.000000000 |


```{code-cell}
cat['2005-07-26'].plot.salt() + cat['2005-07-26'].plot.temp()
```

2005-07-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-27T19:14:00.000000000 |        59.825 |       -152.438 | 2005-07-27T13:43:00.000000000 |


```{code-cell}
cat['2005-07-27'].plot.salt() + cat['2005-07-27'].plot.temp()
```

2005-07-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-28T12:45:00.000000000 |        59.825 |       -152.438 | 2005-07-28T06:37:00.000000000 |


```{code-cell}
cat['2005-07-28'].plot.salt() + cat['2005-07-28'].plot.temp()
```

2005-07-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-29T17:02:00.000000000 |        59.825 |       -152.438 | 2005-07-29T10:13:00.000000000 |


```{code-cell}
cat['2005-07-29'].plot.salt() + cat['2005-07-29'].plot.temp()
```

2005-07-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2005-07-30T15:37:00.000000000 |        59.825 |       -152.438 | 2005-07-30T06:55:00.000000000 |


```{code-cell}
cat['2005-07-30'].plot.salt() + cat['2005-07-30'].plot.temp()
```

## 2006

+++

2006-07-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-01T16:37:00.000000000 |        59.825 |       -152.438 | 2006-07-01T11:14:00.000000000 |


```{code-cell}
cat['2006-07-01'].plot.salt() + cat['2006-07-01'].plot.temp()
```

2006-07-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-02T11:40:00.000000000 |        59.825 |       -152.438 | 2006-07-02T06:38:00.000000000 |


```{code-cell}
cat['2006-07-02'].plot.salt() + cat['2006-07-02'].plot.temp()
```

2006-07-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.825 |       -152.152 | 2006-07-03T09:29:00.000000000 |        59.825 |       -152.152 | 2006-07-03T09:29:00.000000000 |


```{code-cell}
cat['2006-07-03'].plot.salt() + cat['2006-07-03'].plot.temp()
```

2006-07-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8617 |       -152.152 | 2006-07-04T11:52:00.000000000 |        59.825 |       -152.367 | 2006-07-04T07:48:00.000000000 |


```{code-cell}
cat['2006-07-04'].plot.salt() + cat['2006-07-04'].plot.temp()
```

2006-07-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8617 |       -152.152 | 2006-07-05T14:21:00.000000000 |        59.825 |       -152.367 | 2006-07-05T10:06:00.000000000 |


```{code-cell}
cat['2006-07-05'].plot.salt() + cat['2006-07-05'].plot.temp()
```

2006-07-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8567 |       -152.152 | 2006-07-06T12:11:00.000000000 |        59.825 |        -152.33 | 2006-07-06T08:06:00.000000000 |


```{code-cell}
cat['2006-07-06'].plot.salt() + cat['2006-07-06'].plot.temp()
```

2006-07-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-07T14:15:00.000000000 |        59.825 |       -152.438 | 2006-07-07T08:15:00.000000000 |


```{code-cell}
cat['2006-07-07'].plot.salt() + cat['2006-07-07'].plot.temp()
```

2006-07-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-09T16:09:00.000000000 |        59.825 |       -152.438 | 2006-07-09T09:57:00.000000000 |


```{code-cell}
cat['2006-07-09'].plot.salt() + cat['2006-07-09'].plot.temp()
```

2006-07-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-10T12:29:00.000000000 |        59.825 |       -152.438 | 2006-07-10T06:37:00.000000000 |


```{code-cell}
cat['2006-07-10'].plot.salt() + cat['2006-07-10'].plot.temp()
```

2006-07-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-11T14:20:00.000000000 |        59.825 |       -152.438 | 2006-07-11T08:43:00.000000000 |


```{code-cell}
cat['2006-07-11'].plot.salt() + cat['2006-07-11'].plot.temp()
```

2006-07-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-12T12:17:00.000000000 |        59.825 |       -152.438 | 2006-07-12T05:45:00.000000000 |


```{code-cell}
cat['2006-07-12'].plot.salt() + cat['2006-07-12'].plot.temp()
```

2006-07-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-13T15:48:00.000000000 |        59.825 |       -152.438 | 2006-07-13T10:11:00.000000000 |


```{code-cell}
cat['2006-07-13'].plot.salt() + cat['2006-07-13'].plot.temp()
```

2006-07-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |        59.825 |       -152.152 | 2006-07-15T09:21:00.000000000 |        59.825 |       -152.152 | 2006-07-15T09:21:00.000000000 |


```{code-cell}
cat['2006-07-15'].plot.salt() + cat['2006-07-15'].plot.temp()
```

2006-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-16T16:34:00.000000000 |        59.825 |       -152.438 | 2006-07-16T10:40:00.000000000 |


```{code-cell}
cat['2006-07-16'].plot.salt() + cat['2006-07-16'].plot.temp()
```

2006-07-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-17T13:08:00.000000000 |        59.825 |       -152.438 | 2006-07-17T07:27:00.000000000 |


```{code-cell}
cat['2006-07-17'].plot.salt() + cat['2006-07-17'].plot.temp()
```

2006-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-18T13:59:00.000000000 |        59.825 |       -152.438 | 2006-07-18T08:14:00.000000000 |


```{code-cell}
cat['2006-07-18'].plot.salt() + cat['2006-07-18'].plot.temp()
```

2006-07-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.367 | 2006-07-19T08:28:00.000000000 |       59.8617 |       -152.438 | 2006-07-19T07:23:00.000000000 |


```{code-cell}
cat['2006-07-19'].plot.salt() + cat['2006-07-19'].plot.temp()
```

2006-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-21T16:14:00.000000000 |        59.825 |       -152.438 | 2006-07-21T09:43:00.000000000 |


```{code-cell}
cat['2006-07-21'].plot.salt() + cat['2006-07-21'].plot.temp()
```

2006-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8367 |       -152.152 | 2006-07-23T09:59:00.000000000 |        59.825 |       -152.225 | 2006-07-23T08:47:00.000000000 |


```{code-cell}
cat['2006-07-23'].plot.salt() + cat['2006-07-23'].plot.temp()
```

2006-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-25T19:30:00.000000000 |        59.825 |       -152.438 | 2006-07-25T12:55:00.000000000 |


```{code-cell}
cat['2006-07-25'].plot.salt() + cat['2006-07-25'].plot.temp()
```

2006-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-26T12:10:00.000000000 |        59.825 |       -152.438 | 2006-07-26T06:09:00.000000000 |


```{code-cell}
cat['2006-07-26'].plot.salt() + cat['2006-07-26'].plot.temp()
```

2006-07-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.152 | 2006-07-27T17:29:00.000000000 |        59.825 |       -152.438 | 2006-07-27T11:08:00.000000000 |


```{code-cell}
cat['2006-07-27'].plot.salt() + cat['2006-07-27'].plot.temp()
```

2006-07-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | point     |       59.8733 |       -152.438 | 2006-07-28T07:24:00.000000000 |       59.8733 |       -152.438 | 2006-07-28T07:24:00.000000000 |


```{code-cell}
cat['2006-07-28'].plot.salt() + cat['2006-07-28'].plot.temp()
```
