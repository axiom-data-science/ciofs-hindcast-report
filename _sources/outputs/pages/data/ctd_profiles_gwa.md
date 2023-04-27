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

# GWA: Six repeat transects in Cook Inlet

* CTD profiles 2012-2021 - GWA
* ctd_profiles_gwa
* Quarterly repeats from 2012 to 2021


The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    

Not used in the NWGOA model/data comparison.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_gwa"))
```

## Map of Transects
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_gwa")("ctd_profiles_gwa")
    
```

## transect_3

+++

transect_3-2012-05-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2012-05-02T23:56:00.000000000 |         59.78 |       -152.567 | 2012-05-02T17:54:00.000000000 |


```{code-cell}
cat['transect_3-2012-05-02'].plot.salt() + cat['transect_3-2012-05-02'].plot.temp()
```

transect_3-2012-07-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2012-07-29T20:35:00.000000000 |         59.78 |       -152.567 | 2012-07-29T15:04:00.000000000 |


```{code-cell}
cat['transect_3-2012-07-29'].plot.salt() + cat['transect_3-2012-07-29'].plot.temp()
```

transect_3-2012-10-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2012-10-29T13:30:00.000000000 |         59.78 |       -152.567 | 2012-10-29T08:55:00.000000000 |


```{code-cell}
cat['transect_3-2012-10-29'].plot.salt() + cat['transect_3-2012-10-29'].plot.temp()
```

transect_3-2013-04-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2013-04-20T22:41:00.000000000 |         59.78 |       -152.567 | 2013-04-20T18:08:00.000000000 |


```{code-cell}
cat['transect_3-2013-04-20'].plot.salt() + cat['transect_3-2013-04-20'].plot.temp()
```

transect_3-2013-07-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2013-07-19T15:28:00.000000000 |         59.78 |       -152.567 | 2013-07-19T09:59:00.000000000 |


```{code-cell}
cat['transect_3-2013-07-19'].plot.salt() + cat['transect_3-2013-07-19'].plot.temp()
```

transect_3-2013-11-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2013-11-08T16:35:00.000000000 |         59.78 |       -152.567 | 2013-11-08T12:08:00.000000000 |


```{code-cell}
cat['transect_3-2013-11-08'].plot.salt() + cat['transect_3-2013-11-08'].plot.temp()
```

transect_3-2014-04-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2014-04-11T15:03:00.000000000 |         59.78 |       -152.567 | 2014-04-11T10:53:00.000000000 |


```{code-cell}
cat['transect_3-2014-04-11'].plot.salt() + cat['transect_3-2014-04-11'].plot.temp()
```

transect_3-2014-07-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.883 | 2014-07-22T14:23:00.000000000 |        59.772 |       -152.567 | 2014-07-22T08:01:00.000000000 |


```{code-cell}
cat['transect_3-2014-07-22'].plot.salt() + cat['transect_3-2014-07-22'].plot.temp()
```

transect_3-2014-10-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2014-10-13T17:30:00.000000000 |         59.78 |       -152.567 | 2014-10-13T13:13:00.000000000 |


```{code-cell}
cat['transect_3-2014-10-13'].plot.salt() + cat['transect_3-2014-10-13'].plot.temp()
```

transect_3-2015-02-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2015-02-22T16:01:00.000000000 |         59.78 |       -152.567 | 2015-02-22T11:47:00.000000000 |


```{code-cell}
cat['transect_3-2015-02-22'].plot.salt() + cat['transect_3-2015-02-22'].plot.temp()
```

transect_3-2015-04-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2015-04-12T19:18:00.000000000 |         59.78 |       -152.567 | 2015-04-12T14:34:00.000000000 |


```{code-cell}
cat['transect_3-2015-04-12'].plot.salt() + cat['transect_3-2015-04-12'].plot.temp()
```

transect_3-2015-11-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2015-11-04T13:17:00.000000000 |         59.78 |       -152.567 | 2015-11-04T03:32:00.000000000 |


```{code-cell}
cat['transect_3-2015-11-04'].plot.salt() + cat['transect_3-2015-11-04'].plot.temp()
```

transect_3-2016-02-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2016-02-14T18:00:00.000000000 |         59.78 |       -152.567 | 2016-02-14T13:25:00.000000000 |


```{code-cell}
cat['transect_3-2016-02-14'].plot.salt() + cat['transect_3-2016-02-14'].plot.temp()
```

transect_3-2016-04-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.905 | 2016-04-11T11:03:00.000000000 |         59.78 |       -152.567 | 2016-04-11T06:52:00.000000000 |


```{code-cell}
cat['transect_3-2016-04-11'].plot.salt() + cat['transect_3-2016-04-11'].plot.temp()
```

transect_3-2016-08-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -151.883 | 2016-08-29T15:21:00.000000000 |        59.772 |       -152.567 | 2016-08-29T08:13:00.000000000 |


```{code-cell}
cat['transect_3-2016-08-29'].plot.salt() + cat['transect_3-2016-08-29'].plot.temp()
```

transect_3-2017-04-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.997 |       -151.905 | 2017-04-19T23:59:00.000000000 |         59.78 |       -152.537 | 2017-04-19T19:35:00.000000000 |


```{code-cell}
cat['transect_3-2017-04-19'].plot.salt() + cat['transect_3-2017-04-19'].plot.temp()
```

transect_3-2017-04-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.007 |       -152.567 | 2017-04-20T00:12:00.000000000 |        60.007 |       -152.567 | 2017-04-20T00:12:00.000000000 |


```{code-cell}
cat['transect_3-2017-04-20'].plot.salt() + cat['transect_3-2017-04-20'].plot.temp()
```

transect_3-2017-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2017-07-25T13:17:00.000000000 |         59.78 |        -152.04 | 2017-07-25T12:29:00.000000000 |


```{code-cell}
cat['transect_3-2017-07-25'].plot.salt() + cat['transect_3-2017-07-25'].plot.temp()
```

transect_3-2018-06-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2018-06-25T11:17:00.000000000 |         59.78 |        -152.04 | 2018-06-25T10:41:00.000000000 |


```{code-cell}
cat['transect_3-2018-06-25'].plot.salt() + cat['transect_3-2018-06-25'].plot.temp()
```

transect_3-2018-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2018-07-26T12:41:00.000000000 |         59.78 |        -152.04 | 2018-07-26T12:00:00.000000000 |


```{code-cell}
cat['transect_3-2018-07-26'].plot.salt() + cat['transect_3-2018-07-26'].plot.temp()
```

transect_3-2018-09-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.863 |       -151.987 | 2018-09-13T11:18:00.000000000 |         59.81 |       -152.145 | 2018-09-13T10:48:00.000000000 |


```{code-cell}
cat['transect_3-2018-09-13'].plot.salt() + cat['transect_3-2018-09-13'].plot.temp()
```

transect_3-2019-02-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2019-02-08T15:46:00.000000000 |         59.78 |        -152.04 | 2019-02-08T15:05:00.000000000 |


```{code-cell}
cat['transect_3-2019-02-08'].plot.salt() + cat['transect_3-2019-02-08'].plot.temp()
```

transect_3-2019-05-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.81 |       -151.905 | 2019-05-14T13:11:00.000000000 |         59.78 |       -151.987 | 2019-05-14T12:39:00.000000000 |


```{code-cell}
cat['transect_3-2019-05-14'].plot.salt() + cat['transect_3-2019-05-14'].plot.temp()
```

transect_3-2019-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.935 | 2019-07-25T14:05:00.000000000 |         59.79 |        -152.04 | 2019-07-25T13:25:00.000000000 |


```{code-cell}
cat['transect_3-2019-07-25'].plot.salt() + cat['transect_3-2019-07-25'].plot.temp()
```

transect_3-2019-09-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2019-09-16T13:53:00.000000000 |         59.78 |        -152.04 | 2019-09-16T13:09:00.000000000 |


```{code-cell}
cat['transect_3-2019-09-16'].plot.salt() + cat['transect_3-2019-09-16'].plot.temp()
```

transect_3-2020-07-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2020-07-29T10:45:00.000000000 |         59.78 |        -152.04 | 2020-07-29T10:08:00.000000000 |


```{code-cell}
cat['transect_3-2020-07-29'].plot.salt() + cat['transect_3-2020-07-29'].plot.temp()
```

transect_3-2021-04-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.905 | 2021-04-16T11:44:00.000000000 |         59.78 |        -152.04 | 2021-04-16T11:02:00.000000000 |


```{code-cell}
cat['transect_3-2021-04-16'].plot.salt() + cat['transect_3-2021-04-16'].plot.temp()
```

transect_3-2021-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.827 |       -151.935 | 2021-07-16T15:44:00.000000000 |         59.79 |        -152.04 | 2021-07-16T15:05:00.000000000 |


```{code-cell}
cat['transect_3-2021-07-16'].plot.salt() + cat['transect_3-2021-07-16'].plot.temp()
```

## transect_4

+++

transect_4-2012-05-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2012-05-02T15:35:00.000000000 |        59.492 |        -151.65 | 2012-05-02T13:15:00.000000000 |


```{code-cell}
cat['transect_4-2012-05-02'].plot.salt() + cat['transect_4-2012-05-02'].plot.temp()
```

transect_4-2012-05-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2012-05-31T13:25:00.000000000 |        59.492 |        -151.65 | 2012-05-31T10:58:00.000000000 |


```{code-cell}
cat['transect_4-2012-05-31'].plot.salt() + cat['transect_4-2012-05-31'].plot.temp()
```

transect_4-2012-06-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2012-06-05T17:30:00.000000000 |        59.492 |        -151.65 | 2012-06-05T09:16:00.000000000 |


```{code-cell}
cat['transect_4-2012-06-05'].plot.salt() + cat['transect_4-2012-06-05'].plot.temp()
```

transect_4-2012-07-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2012-07-31T11:02:00.000000000 |        59.492 |        -151.65 | 2012-07-31T08:36:00.000000000 |


```{code-cell}
cat['transect_4-2012-07-31'].plot.salt() + cat['transect_4-2012-07-31'].plot.temp()
```

transect_4-2012-08-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2012-08-15T16:00:00.000000000 |        59.492 |        -151.65 | 2012-08-15T14:34:00.000000000 |


```{code-cell}
cat['transect_4-2012-08-15'].plot.salt() + cat['transect_4-2012-08-15'].plot.temp()
```

transect_4-2012-10-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2012-10-29T17:43:00.000000000 |        59.492 |        -151.65 | 2012-10-29T15:45:00.000000000 |


```{code-cell}
cat['transect_4-2012-10-29'].plot.salt() + cat['transect_4-2012-10-29'].plot.temp()
```

transect_4-2013-02-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2013-02-12T15:17:00.000000000 |        59.492 |        -151.65 | 2013-02-12T12:59:00.000000000 |


```{code-cell}
cat['transect_4-2013-02-12'].plot.salt() + cat['transect_4-2013-02-12'].plot.temp()
```

transect_4-2013-04-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2013-04-21T11:45:00.000000000 |        59.492 |        -151.65 | 2013-04-21T09:26:00.000000000 |


```{code-cell}
cat['transect_4-2013-04-21'].plot.salt() + cat['transect_4-2013-04-21'].plot.temp()
```

transect_4-2013-06-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2013-06-06T11:15:00.000000000 |        59.492 |        -151.65 | 2013-06-06T09:45:00.000000000 |


```{code-cell}
cat['transect_4-2013-06-06'].plot.salt() + cat['transect_4-2013-06-06'].plot.temp()
```

transect_4-2013-07-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2013-07-19T20:55:00.000000000 |        59.492 |        -151.65 | 2013-07-19T17:50:00.000000000 |


```{code-cell}
cat['transect_4-2013-07-19'].plot.salt() + cat['transect_4-2013-07-19'].plot.temp()
```

transect_4-2013-10-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2013-10-29T14:44:00.000000000 |        59.492 |        -151.65 | 2013-10-29T12:18:00.000000000 |


```{code-cell}
cat['transect_4-2013-10-29'].plot.salt() + cat['transect_4-2013-10-29'].plot.temp()
```

transect_4-2014-02-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2014-02-15T15:34:00.000000000 |        59.492 |        -151.65 | 2014-02-15T13:23:00.000000000 |


```{code-cell}
cat['transect_4-2014-02-15'].plot.salt() + cat['transect_4-2014-02-15'].plot.temp()
```

transect_4-2014-04-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2014-04-11T18:27:00.000000000 |        59.492 |        -151.65 | 2014-04-11T16:30:00.000000000 |


```{code-cell}
cat['transect_4-2014-04-11'].plot.salt() + cat['transect_4-2014-04-11'].plot.temp()
```

transect_4-2014-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2014-07-21T22:13:00.000000000 |        59.492 |        -151.65 | 2014-07-21T18:36:00.000000000 |


```{code-cell}
cat['transect_4-2014-07-21'].plot.salt() + cat['transect_4-2014-07-21'].plot.temp()
```

transect_4-2014-08-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2014-08-13T16:04:00.000000000 |        59.492 |        -151.65 | 2014-08-13T14:02:00.000000000 |


```{code-cell}
cat['transect_4-2014-08-13'].plot.salt() + cat['transect_4-2014-08-13'].plot.temp()
```

transect_4-2014-10-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2014-10-13T11:23:00.000000000 |        59.492 |        -151.65 | 2014-10-13T08:58:00.000000000 |


```{code-cell}
cat['transect_4-2014-10-13'].plot.salt() + cat['transect_4-2014-10-13'].plot.temp()
```

transect_4-2015-02-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2015-02-12T12:40:00.000000000 |        59.492 |        -151.65 | 2015-02-12T10:26:00.000000000 |


```{code-cell}
cat['transect_4-2015-02-12'].plot.salt() + cat['transect_4-2015-02-12'].plot.temp()
```

transect_4-2015-02-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.542 |        -151.65 | 2015-02-24T18:13:00.000000000 |        59.542 |        -151.65 | 2015-02-24T18:13:00.000000000 |


```{code-cell}
cat['transect_4-2015-02-24'].plot.salt() + cat['transect_4-2015-02-24'].plot.temp()
```

transect_4-2015-04-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2015-04-08T11:08:00.000000000 |        59.492 |        -151.65 | 2015-04-08T09:08:00.000000000 |


```{code-cell}
cat['transect_4-2015-04-08'].plot.salt() + cat['transect_4-2015-04-08'].plot.temp()
```

transect_4-2015-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.542 |        -151.65 | 2015-08-14T15:55:00.000000000 |        59.492 |        -151.65 | 2015-08-14T15:07:00.000000000 |


```{code-cell}
cat['transect_4-2015-08-14'].plot.salt() + cat['transect_4-2015-08-14'].plot.temp()
```

transect_4-2015-09-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2015-09-24T16:19:00.000000000 |        59.492 |        -151.65 | 2015-09-24T15:05:00.000000000 |


```{code-cell}
cat['transect_4-2015-09-24'].plot.salt() + cat['transect_4-2015-09-24'].plot.temp()
```

transect_4-2015-10-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2015-10-19T17:58:00.000000000 |        59.492 |        -151.65 | 2015-10-19T16:26:00.000000000 |


```{code-cell}
cat['transect_4-2015-10-19'].plot.salt() + cat['transect_4-2015-10-19'].plot.temp()
```

transect_4-2015-11-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.542 |        -151.65 | 2015-11-03T16:29:00.000000000 |        59.542 |        -151.65 | 2015-11-03T16:29:00.000000000 |


```{code-cell}
cat['transect_4-2015-11-03'].plot.salt() + cat['transect_4-2015-11-03'].plot.temp()
```

transect_4-2015-11-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2015-11-04T18:51:00.000000000 |        59.492 |        -151.65 | 2015-11-04T15:32:00.000000000 |


```{code-cell}
cat['transect_4-2015-11-04'].plot.salt() + cat['transect_4-2015-11-04'].plot.temp()
```

transect_4-2015-12-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2015-12-10T15:13:00.000000000 |        59.492 |        -151.65 | 2015-12-10T13:40:00.000000000 |


```{code-cell}
cat['transect_4-2015-12-10'].plot.salt() + cat['transect_4-2015-12-10'].plot.temp()
```

transect_4-2016-02-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2016-02-09T12:34:00.000000000 |        59.492 |        -151.65 | 2016-02-09T10:35:00.000000000 |


```{code-cell}
cat['transect_4-2016-02-09'].plot.salt() + cat['transect_4-2016-02-09'].plot.temp()
```

transect_4-2016-04-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2016-04-11T15:13:00.000000000 |        59.492 |        -151.65 | 2016-04-11T13:11:00.000000000 |


```{code-cell}
cat['transect_4-2016-04-11'].plot.salt() + cat['transect_4-2016-04-11'].plot.temp()
```

transect_4-2016-07-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2016-07-27T14:30:00.000000000 |        59.492 |        -151.65 | 2016-07-27T12:40:00.000000000 |


```{code-cell}
cat['transect_4-2016-07-27'].plot.salt() + cat['transect_4-2016-07-27'].plot.temp()
```

transect_4-2016-10-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2016-10-13T16:34:00.000000000 |        59.492 |        -151.65 | 2016-10-13T14:51:00.000000000 |


```{code-cell}
cat['transect_4-2016-10-13'].plot.salt() + cat['transect_4-2016-10-13'].plot.temp()
```

transect_4-2016-12-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2016-12-13T16:01:00.000000000 |        59.492 |        -151.65 | 2016-12-13T13:49:00.000000000 |


```{code-cell}
cat['transect_4-2016-12-13'].plot.salt() + cat['transect_4-2016-12-13'].plot.temp()
```

transect_4-2017-04-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2017-04-20T15:56:00.000000000 |        59.492 |        -151.65 | 2017-04-20T13:38:00.000000000 |


```{code-cell}
cat['transect_4-2017-04-20'].plot.salt() + cat['transect_4-2017-04-20'].plot.temp()
```

transect_4-2017-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2017-07-25T11:53:00.000000000 |        59.492 |        -151.65 | 2017-07-25T09:48:00.000000000 |


```{code-cell}
cat['transect_4-2017-07-25'].plot.salt() + cat['transect_4-2017-07-25'].plot.temp()
```

transect_4-2017-10-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2017-10-17T13:33:00.000000000 |        59.492 |        -151.65 | 2017-10-17T11:33:00.000000000 |


```{code-cell}
cat['transect_4-2017-10-17'].plot.salt() + cat['transect_4-2017-10-17'].plot.temp()
```

transect_4-2018-04-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2018-04-23T15:11:00.000000000 |        59.492 |        -151.65 | 2018-04-23T13:18:00.000000000 |


```{code-cell}
cat['transect_4-2018-04-23'].plot.salt() + cat['transect_4-2018-04-23'].plot.temp()
```

transect_4-2018-06-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2018-06-25T14:32:00.000000000 |        59.492 |        -151.65 | 2018-06-25T12:26:00.000000000 |


```{code-cell}
cat['transect_4-2018-06-25'].plot.salt() + cat['transect_4-2018-06-25'].plot.temp()
```

transect_4-2018-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2018-07-24T12:08:00.000000000 |        59.492 |        -151.65 | 2018-07-24T10:24:00.000000000 |


```{code-cell}
cat['transect_4-2018-07-24'].plot.salt() + cat['transect_4-2018-07-24'].plot.temp()
```

transect_4-2018-09-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2018-09-13T13:42:00.000000000 |        59.492 |        -151.65 | 2018-09-13T12:04:00.000000000 |


```{code-cell}
cat['transect_4-2018-09-13'].plot.salt() + cat['transect_4-2018-09-13'].plot.temp()
```

transect_4-2019-02-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2019-02-07T12:28:00.000000000 |        59.492 |        -151.65 | 2019-02-07T10:34:00.000000000 |


```{code-cell}
cat['transect_4-2019-02-07'].plot.salt() + cat['transect_4-2019-02-07'].plot.temp()
```

transect_4-2019-05-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2019-05-14T11:24:00.000000000 |        59.492 |        -151.65 | 2019-05-14T09:36:00.000000000 |


```{code-cell}
cat['transect_4-2019-05-14'].plot.salt() + cat['transect_4-2019-05-14'].plot.temp()
```

transect_4-2019-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2019-07-25T17:01:00.000000000 |        59.492 |        -151.65 | 2019-07-25T14:37:00.000000000 |


```{code-cell}
cat['transect_4-2019-07-25'].plot.salt() + cat['transect_4-2019-07-25'].plot.temp()
```

transect_4-2019-09-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2019-09-16T16:29:00.000000000 |        59.492 |        -151.65 | 2019-09-16T14:27:00.000000000 |


```{code-cell}
cat['transect_4-2019-09-16'].plot.salt() + cat['transect_4-2019-09-16'].plot.temp()
```

transect_4-2020-02-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2020-02-14T14:31:00.000000000 |        59.492 |        -151.65 | 2020-02-14T12:52:00.000000000 |


```{code-cell}
cat['transect_4-2020-02-14'].plot.salt() + cat['transect_4-2020-02-14'].plot.temp()
```

transect_4-2020-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2020-07-23T11:43:00.000000000 |        59.492 |        -151.65 | 2020-07-23T09:39:00.000000000 |


```{code-cell}
cat['transect_4-2020-07-23'].plot.salt() + cat['transect_4-2020-07-23'].plot.temp()
```

transect_4-2020-09-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2020-09-21T13:34:00.000000000 |        59.492 |        -151.65 | 2020-09-21T11:51:00.000000000 |


```{code-cell}
cat['transect_4-2020-09-21'].plot.salt() + cat['transect_4-2020-09-21'].plot.temp()
```

transect_4-2021-02-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2021-02-17T13:08:00.000000000 |        59.492 |        -151.65 | 2021-02-17T11:39:00.000000000 |


```{code-cell}
cat['transect_4-2021-02-17'].plot.salt() + cat['transect_4-2021-02-17'].plot.temp()
```

transect_4-2021-04-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2021-04-16T13:54:00.000000000 |        59.492 |        -151.65 | 2021-04-16T12:16:00.000000000 |


```{code-cell}
cat['transect_4-2021-04-16'].plot.salt() + cat['transect_4-2021-04-16'].plot.temp()
```

transect_4-2021-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2021-07-16T14:21:00.000000000 |        59.492 |        -151.65 | 2021-07-16T12:30:00.000000000 |


```{code-cell}
cat['transect_4-2021-07-16'].plot.salt() + cat['transect_4-2021-07-16'].plot.temp()
```

transect_4-2021-09-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2021-09-17T12:43:00.000000000 |        59.492 |        -151.65 | 2021-09-17T11:00:00.000000000 |


```{code-cell}
cat['transect_4-2021-09-17'].plot.salt() + cat['transect_4-2021-09-17'].plot.temp()
```

transect_4-2022-03-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2022-03-01T12:55:00.000000000 |        59.492 |        -151.65 | 2022-03-01T11:50:00.000000000 |


```{code-cell}
cat['transect_4-2022-03-01'].plot.salt() + cat['transect_4-2022-03-01'].plot.temp()
```

transect_4-2022-04-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2022-04-13T11:26:00.000000000 |        59.492 |        -151.65 | 2022-04-13T10:15:00.000000000 |


```{code-cell}
cat['transect_4-2022-04-13'].plot.salt() + cat['transect_4-2022-04-13'].plot.temp()
```

transect_4-2022-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.633 |        -151.65 | 2022-07-23T12:19:00.000000000 |        59.492 |        -151.65 | 2022-07-23T10:46:00.000000000 |


```{code-cell}
cat['transect_4-2022-07-23'].plot.salt() + cat['transect_4-2022-07-23'].plot.temp()
```

## transect_6

+++

transect_6-2012-05-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2012-05-03T23:56:00.000000000 |         58.93 |       -152.993 | 2012-05-03T17:38:00.000000000 |


```{code-cell}
cat['transect_6-2012-05-03'].plot.salt() + cat['transect_6-2012-05-03'].plot.temp()
```

transect_6-2012-05-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        58.915 |       -153.048 | 2012-05-04T01:43:00.000000000 |        58.872 |       -153.212 | 2012-05-04T00:18:00.000000000 |


```{code-cell}
cat['transect_6-2012-05-04'].plot.salt() + cat['transect_6-2012-05-04'].plot.temp()
```

transect_6-2012-07-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2012-07-30T23:38:00.000000000 |        58.887 |       -153.158 | 2012-07-30T15:02:00.000000000 |


```{code-cell}
cat['transect_6-2012-07-30'].plot.salt() + cat['transect_6-2012-07-30'].plot.temp()
```

transect_6-2012-07-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         58.88 |       -153.185 | 2012-07-31T00:40:00.000000000 |        58.869 |       -153.225 | 2012-07-31T00:05:00.000000000 |


```{code-cell}
cat['transect_6-2012-07-31'].plot.salt() + cat['transect_6-2012-07-31'].plot.temp()
```

transect_6-2012-10-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2012-10-28T18:55:00.000000000 |        58.869 |       -153.225 | 2012-10-28T07:54:00.000000000 |


```{code-cell}
cat['transect_6-2012-10-28'].plot.salt() + cat['transect_6-2012-10-28'].plot.temp()
```

transect_6-2013-04-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2013-04-19T20:50:00.000000000 |        58.869 |       -153.225 | 2013-04-19T09:27:00.000000000 |


```{code-cell}
cat['transect_6-2013-04-19'].plot.salt() + cat['transect_6-2013-04-19'].plot.temp()
```

transect_6-2013-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.075 |       -152.445 | 2013-07-21T23:45:00.000000000 |        58.869 |       -153.225 | 2013-07-21T18:28:00.000000000 |


```{code-cell}
cat['transect_6-2013-07-21'].plot.salt() + cat['transect_6-2013-07-21'].plot.temp()
```

transect_6-2013-07-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2013-07-22T03:45:00.000000000 |        59.088 |        -152.39 | 2013-07-22T00:08:00.000000000 |


```{code-cell}
cat['transect_6-2013-07-22'].plot.salt() + cat['transect_6-2013-07-22'].plot.temp()
```

transect_6-2013-11-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2013-11-06T17:31:00.000000000 |        58.869 |       -153.225 | 2013-11-06T09:07:00.000000000 |


```{code-cell}
cat['transect_6-2013-11-06'].plot.salt() + cat['transect_6-2013-11-06'].plot.temp()
```

transect_6-2014-04-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2014-04-06T17:31:00.000000000 |        58.869 |       -153.225 | 2014-04-06T09:18:00.000000000 |


```{code-cell}
cat['transect_6-2014-04-06'].plot.salt() + cat['transect_6-2014-04-06'].plot.temp()
```

transect_6-2014-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2014-07-23T20:04:00.000000000 |        58.869 |       -153.225 | 2014-07-23T08:40:00.000000000 |


```{code-cell}
cat['transect_6-2014-07-23'].plot.salt() + cat['transect_6-2014-07-23'].plot.temp()
```

transect_6-2014-10-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2014-10-18T09:13:00.000000000 |        58.869 |       -153.225 | 2014-10-18T00:27:00.000000000 |


```{code-cell}
cat['transect_6-2014-10-18'].plot.salt() + cat['transect_6-2014-10-18'].plot.temp()
```

transect_6-2015-02-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.19 |       -152.007 | 2015-02-23T23:55:00.000000000 |        58.869 |       -153.225 | 2015-02-23T15:26:00.000000000 |


```{code-cell}
cat['transect_6-2015-02-23'].plot.salt() + cat['transect_6-2015-02-23'].plot.temp()
```

transect_6-2015-02-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2015-02-24T00:32:00.000000000 |        59.197 |        -151.98 | 2015-02-24T00:08:00.000000000 |


```{code-cell}
cat['transect_6-2015-02-24'].plot.salt() + cat['transect_6-2015-02-24'].plot.temp()
```

transect_6-2015-04-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2015-04-08T04:32:00.000000000 |        59.075 |       -152.445 | 2015-04-08T01:00:00.000000000 |


```{code-cell}
cat['transect_6-2015-04-08'].plot.salt() + cat['transect_6-2015-04-08'].plot.temp()
```

transect_6-2015-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2015-08-14T12:00:00.000000000 |        59.161 |       -152.117 | 2015-08-14T10:33:00.000000000 |


```{code-cell}
cat['transect_6-2015-08-14'].plot.salt() + cat['transect_6-2015-08-14'].plot.temp()
```

transect_6-2016-02-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2016-02-15T18:53:00.000000000 |        58.869 |       -153.225 | 2016-02-15T10:19:00.000000000 |


```{code-cell}
cat['transect_6-2016-02-15'].plot.salt() + cat['transect_6-2016-02-15'].plot.temp()
```

transect_6-2016-04-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2016-04-10T15:59:00.000000000 |        58.869 |       -153.225 | 2016-04-10T07:45:00.000000000 |


```{code-cell}
cat['transect_6-2016-04-10'].plot.salt() + cat['transect_6-2016-04-10'].plot.temp()
```

transect_6-2016-08-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2016-08-31T19:05:00.000000000 |        58.869 |       -153.225 | 2016-08-31T07:41:00.000000000 |


```{code-cell}
cat['transect_6-2016-08-31'].plot.salt() + cat['transect_6-2016-08-31'].plot.temp()
```

transect_6-2016-12-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2016-12-12T22:07:00.000000000 |        59.017 |       -152.665 | 2016-12-12T16:55:00.000000000 |


```{code-cell}
cat['transect_6-2016-12-12'].plot.salt() + cat['transect_6-2016-12-12'].plot.temp()
```

transect_6-2017-04-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2017-04-18T22:13:00.000000000 |       58.8689 |        -153.24 | 2017-04-18T12:18:00.000000000 |


```{code-cell}
cat['transect_6-2017-04-18'].plot.salt() + cat['transect_6-2017-04-18'].plot.temp()
```

transect_6-2017-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2017-07-26T13:02:00.000000000 |        59.175 |       -152.062 | 2017-07-26T12:24:00.000000000 |


```{code-cell}
cat['transect_6-2017-07-26'].plot.salt() + cat['transect_6-2017-07-26'].plot.temp()
```

transect_6-2017-11-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2017-11-02T13:08:00.000000000 |         59.19 |       -152.007 | 2017-11-02T12:24:00.000000000 |


```{code-cell}
cat['transect_6-2017-11-02'].plot.salt() + cat['transect_6-2017-11-02'].plot.temp()
```

transect_6-2018-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2018-07-18T11:50:00.000000000 |        59.161 |       -152.117 | 2018-07-18T10:16:00.000000000 |


```{code-cell}
cat['transect_6-2018-07-18'].plot.salt() + cat['transect_6-2018-07-18'].plot.temp()
```

transect_6-2018-09-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2018-09-17T12:23:00.000000000 |        59.161 |       -152.117 | 2018-09-17T11:04:00.000000000 |


```{code-cell}
cat['transect_6-2018-09-17'].plot.salt() + cat['transect_6-2018-09-17'].plot.temp()
```

transect_6-2019-02-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2019-02-08T12:32:00.000000000 |        59.161 |       -152.117 | 2019-02-08T11:23:00.000000000 |


```{code-cell}
cat['transect_6-2019-02-08'].plot.salt() + cat['transect_6-2019-02-08'].plot.temp()
```

transect_6-2019-05-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2019-05-12T14:43:00.000000000 |        58.869 |       -153.225 | 2019-05-12T05:33:00.000000000 |


```{code-cell}
cat['transect_6-2019-05-12'].plot.salt() + cat['transect_6-2019-05-12'].plot.temp()
```

transect_6-2019-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2019-07-25T10:43:00.000000000 |        59.161 |       -152.117 | 2019-07-25T09:19:00.000000000 |


```{code-cell}
cat['transect_6-2019-07-25'].plot.salt() + cat['transect_6-2019-07-25'].plot.temp()
```

transect_6-2020-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2020-07-24T10:25:00.000000000 |        59.175 |       -152.062 | 2020-07-24T09:23:00.000000000 |


```{code-cell}
cat['transect_6-2020-07-24'].plot.salt() + cat['transect_6-2020-07-24'].plot.temp()
```

transect_6-2020-09-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2020-09-20T10:43:00.000000000 |        59.161 |       -152.117 | 2020-09-20T09:27:00.000000000 |


```{code-cell}
cat['transect_6-2020-09-20'].plot.salt() + cat['transect_6-2020-09-20'].plot.temp()
```

transect_6-2021-02-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2021-02-16T12:10:00.000000000 |        59.175 |       -152.062 | 2021-02-16T11:22:00.000000000 |


```{code-cell}
cat['transect_6-2021-02-16'].plot.salt() + cat['transect_6-2021-02-16'].plot.temp()
```

transect_6-2021-04-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2021-04-14T16:53:00.000000000 |        58.869 |       -153.225 | 2021-04-14T07:06:00.000000000 |


```{code-cell}
cat['transect_6-2021-04-14'].plot.salt() + cat['transect_6-2021-04-14'].plot.temp()
```

transect_6-2021-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2021-07-21T11:54:00.000000000 |        59.175 |       -152.062 | 2021-07-21T10:50:00.000000000 |


```{code-cell}
cat['transect_6-2021-07-21'].plot.salt() + cat['transect_6-2021-07-21'].plot.temp()
```

transect_6-2021-10-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.212 |       -151.925 | 2021-10-05T11:40:00.000000000 |        59.197 |        -151.98 | 2021-10-05T11:03:00.000000000 |


```{code-cell}
cat['transect_6-2021-10-05'].plot.salt() + cat['transect_6-2021-10-05'].plot.temp()
```

transect_6-2022-02-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.205 |       -151.952 | 2022-02-28T11:26:00.000000000 |        59.205 |       -151.952 | 2022-02-28T11:26:00.000000000 |


```{code-cell}
cat['transect_6-2022-02-28'].plot.salt() + cat['transect_6-2022-02-28'].plot.temp()
```

transect_6-2022-04-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.205 |       -151.952 | 2022-04-12T10:12:00.000000000 |        59.205 |       -151.952 | 2022-04-12T10:12:00.000000000 |


```{code-cell}
cat['transect_6-2022-04-12'].plot.salt() + cat['transect_6-2022-04-12'].plot.temp()
```

transect_6-2022-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.205 |       -151.952 | 2022-07-21T11:11:00.000000000 |        59.205 |       -151.952 | 2022-07-21T11:11:00.000000000 |


```{code-cell}
cat['transect_6-2022-07-21'].plot.salt() + cat['transect_6-2022-07-21'].plot.temp()
```

## transect_7

+++

transect_7-2012-07-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.335 |       -152.032 | 2012-07-30T11:04:00.000000000 |         59.31 |       -152.847 | 2012-07-30T06:53:00.000000000 |


```{code-cell}
cat['transect_7-2012-07-30'].plot.salt() + cat['transect_7-2012-07-30'].plot.temp()
```

transect_7-2012-10-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.333 |       -152.032 | 2012-10-28T23:52:00.000000000 |         59.31 |       -152.782 | 2012-10-28T20:01:00.000000000 |


```{code-cell}
cat['transect_7-2012-10-28'].plot.salt() + cat['transect_7-2012-10-28'].plot.temp()
```

transect_7-2012-10-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.847 | 2012-10-29T02:53:00.000000000 |        59.335 |       -153.302 | 2012-10-29T00:24:00.000000000 |


```{code-cell}
cat['transect_7-2012-10-29'].plot.salt() + cat['transect_7-2012-10-29'].plot.temp()
```

transect_7-2013-04-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |           -152 | 2013-04-20T14:03:00.000000000 |        59.308 |       -153.302 | 2013-04-20T06:29:00.000000000 |


```{code-cell}
cat['transect_7-2013-04-20'].plot.salt() + cat['transect_7-2013-04-20'].plot.temp()
```

transect_7-2013-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2013-07-18T19:56:00.000000000 |         59.31 |       -153.302 | 2013-07-18T12:36:00.000000000 |


```{code-cell}
cat['transect_7-2013-07-18'].plot.salt() + cat['transect_7-2013-07-18'].plot.temp()
```

transect_7-2014-02-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.097 | 2014-02-17T12:00:00.000000000 |        59.312 |       -153.302 | 2014-02-17T06:14:00.000000000 |


```{code-cell}
cat['transect_7-2014-02-17'].plot.salt() + cat['transect_7-2014-02-17'].plot.temp()
```

transect_7-2014-04-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2014-04-07T09:52:00.000000000 |         59.31 |       -153.302 | 2014-04-07T03:17:00.000000000 |


```{code-cell}
cat['transect_7-2014-04-07'].plot.salt() + cat['transect_7-2014-04-07'].plot.temp()
```

transect_7-2014-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2014-07-24T16:53:00.000000000 |         59.31 |       -153.302 | 2014-07-24T08:00:00.000000000 |


```{code-cell}
cat['transect_7-2014-07-24'].plot.salt() + cat['transect_7-2014-07-24'].plot.temp()
```

transect_7-2014-10-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2014-10-17T17:42:00.000000000 |         59.31 |       -152.196 | 2014-10-17T16:12:00.000000000 |


```{code-cell}
cat['transect_7-2014-10-17'].plot.salt() + cat['transect_7-2014-10-17'].plot.temp()
```

transect_7-2014-10-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2014-10-18T19:16:00.000000000 |         59.31 |       -153.302 | 2014-10-18T12:49:00.000000000 |


```{code-cell}
cat['transect_7-2014-10-18'].plot.salt() + cat['transect_7-2014-10-18'].plot.temp()
```

transect_7-2015-02-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2015-02-24T12:02:00.000000000 |         59.31 |       -153.302 | 2015-02-24T05:35:00.000000000 |


```{code-cell}
cat['transect_7-2015-02-24'].plot.salt() + cat['transect_7-2015-02-24'].plot.temp()
```

transect_7-2015-04-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2015-04-13T07:51:00.000000000 |         59.31 |       -153.302 | 2015-04-13T01:35:00.000000000 |


```{code-cell}
cat['transect_7-2015-04-13'].plot.salt() + cat['transect_7-2015-04-13'].plot.temp()
```

transect_7-2015-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2015-08-14T13:38:00.000000000 |         59.31 |       -152.196 | 2015-08-14T12:30:00.000000000 |


```{code-cell}
cat['transect_7-2015-08-14'].plot.salt() + cat['transect_7-2015-08-14'].plot.temp()
```

transect_7-2016-02-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2016-02-16T06:43:00.000000000 |         59.31 |       -153.302 | 2016-02-16T00:02:00.000000000 |


```{code-cell}
cat['transect_7-2016-02-16'].plot.salt() + cat['transect_7-2016-02-16'].plot.temp()
```

transect_7-2016-08-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |           -152 | 2016-08-30T15:26:00.000000000 |        59.308 |       -153.302 | 2016-08-30T07:43:00.000000000 |


```{code-cell}
cat['transect_7-2016-08-30'].plot.salt() + cat['transect_7-2016-08-30'].plot.temp()
```

transect_7-2016-12-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2016-12-13T11:20:00.000000000 |         59.31 |       -152.196 | 2016-12-13T10:09:00.000000000 |


```{code-cell}
cat['transect_7-2016-12-13'].plot.salt() + cat['transect_7-2016-12-13'].plot.temp()
```

transect_7-2017-04-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.35 |       -152.032 | 2017-04-19T15:57:00.000000000 |         59.31 |       -153.302 | 2017-04-19T08:20:00.000000000 |


```{code-cell}
cat['transect_7-2017-04-19'].plot.salt() + cat['transect_7-2017-04-19'].plot.temp()
```

transect_7-2017-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.097 | 2017-07-26T11:52:00.000000000 |        59.312 |       -152.196 | 2017-07-26T11:10:00.000000000 |


```{code-cell}
cat['transect_7-2017-07-26'].plot.salt() + cat['transect_7-2017-07-26'].plot.temp()
```

transect_7-2017-11-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.312 |       -152.032 | 2017-11-02T14:31:00.000000000 |         59.31 |       -152.097 | 2017-11-02T14:00:00.000000000 |


```{code-cell}
cat['transect_7-2017-11-02'].plot.salt() + cat['transect_7-2017-11-02'].plot.temp()
```

transect_7-2018-03-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.31 |       -152.065 | 2018-03-27T12:51:00.000000000 |         59.31 |       -152.065 | 2018-03-27T12:51:00.000000000 |


```{code-cell}
cat['transect_7-2018-03-27'].plot.salt() + cat['transect_7-2018-03-27'].plot.temp()
```

transect_7-2018-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.313 |       -152.032 | 2018-07-18T13:03:00.000000000 |         59.31 |        -152.13 | 2018-07-18T12:26:00.000000000 |


```{code-cell}
cat['transect_7-2018-07-18'].plot.salt() + cat['transect_7-2018-07-18'].plot.temp()
```

transect_7-2018-09-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2018-09-17T13:47:00.000000000 |         59.31 |       -152.196 | 2018-09-17T12:57:00.000000000 |


```{code-cell}
cat['transect_7-2018-09-17'].plot.salt() + cat['transect_7-2018-09-17'].plot.temp()
```

transect_7-2019-02-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.065 | 2019-02-08T13:52:00.000000000 |         59.31 |       -152.196 | 2019-02-08T13:06:00.000000000 |


```{code-cell}
cat['transect_7-2019-02-08'].plot.salt() + cat['transect_7-2019-02-08'].plot.temp()
```

transect_7-2019-05-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2019-05-12T16:35:00.000000000 |         59.31 |       -152.196 | 2019-05-12T15:30:00.000000000 |


```{code-cell}
cat['transect_7-2019-05-12'].plot.salt() + cat['transect_7-2019-05-12'].plot.temp()
```

transect_7-2019-07-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2019-07-25T12:03:00.000000000 |         59.31 |       -152.196 | 2019-07-25T11:02:00.000000000 |


```{code-cell}
cat['transect_7-2019-07-25'].plot.salt() + cat['transect_7-2019-07-25'].plot.temp()
```

transect_7-2019-09-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2019-09-19T15:42:00.000000000 |         59.31 |       -152.196 | 2019-09-19T14:48:00.000000000 |


```{code-cell}
cat['transect_7-2019-09-19'].plot.salt() + cat['transect_7-2019-09-19'].plot.temp()
```

transect_7-2020-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2020-07-24T11:43:00.000000000 |         59.31 |       -152.196 | 2020-07-24T10:57:00.000000000 |


```{code-cell}
cat['transect_7-2020-07-24'].plot.salt() + cat['transect_7-2020-07-24'].plot.temp()
```

transect_7-2020-09-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2020-09-20T12:09:00.000000000 |         59.31 |       -152.196 | 2020-09-20T11:19:00.000000000 |


```{code-cell}
cat['transect_7-2020-09-20'].plot.salt() + cat['transect_7-2020-09-20'].plot.temp()
```

transect_7-2021-02-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.315 |       -152.032 | 2021-02-16T13:35:00.000000000 |         59.31 |       -152.196 | 2021-02-16T12:44:00.000000000 |


```{code-cell}
cat['transect_7-2021-02-16'].plot.salt() + cat['transect_7-2021-02-16'].plot.temp()
```

transect_7-2021-04-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.313 |       -152.032 | 2021-04-14T18:14:00.000000000 |         59.31 |        -152.13 | 2021-04-14T17:32:00.000000000 |


```{code-cell}
cat['transect_7-2021-04-14'].plot.salt() + cat['transect_7-2021-04-14'].plot.temp()
```

transect_7-2021-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.313 |       -152.032 | 2021-07-21T13:01:00.000000000 |         59.31 |        -152.13 | 2021-07-21T12:24:00.000000000 |


```{code-cell}
cat['transect_7-2021-07-21'].plot.salt() + cat['transect_7-2021-07-21'].plot.temp()
```

transect_7-2021-10-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.312 |       -152.032 | 2021-10-05T12:35:00.000000000 |         59.31 |       -152.097 | 2021-10-05T12:05:00.000000000 |


```{code-cell}
cat['transect_7-2021-10-05'].plot.salt() + cat['transect_7-2021-10-05'].plot.temp()
```

transect_7-2022-02-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.31 |       -152.065 | 2022-02-28T12:05:00.000000000 |         59.31 |       -152.065 | 2022-02-28T12:05:00.000000000 |


```{code-cell}
cat['transect_7-2022-02-28'].plot.salt() + cat['transect_7-2022-02-28'].plot.temp()
```

transect_7-2022-04-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.31 |       -152.065 | 2022-04-12T10:52:00.000000000 |         59.31 |       -152.065 | 2022-04-12T10:52:00.000000000 |


```{code-cell}
cat['transect_7-2022-04-12'].plot.salt() + cat['transect_7-2022-04-12'].plot.temp()
```

transect_7-2022-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |         59.31 |       -152.065 | 2022-07-21T11:55:00.000000000 |         59.31 |       -152.065 | 2022-07-21T11:55:00.000000000 |


```{code-cell}
cat['transect_7-2022-07-21'].plot.salt() + cat['transect_7-2022-07-21'].plot.temp()
```

## transect_9

+++

transect_9-2012-02-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-02-14T13:40:00.000000000 |       59.5702 |       -151.404 | 2012-02-14T12:31:00.000000000 |


```{code-cell}
cat['transect_9-2012-02-14'].plot.salt() + cat['transect_9-2012-02-14'].plot.temp()
```

transect_9-2012-03-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-03-14T15:27:00.000000000 |       59.5702 |       -151.404 | 2012-03-14T14:05:00.000000000 |


```{code-cell}
cat['transect_9-2012-03-14'].plot.salt() + cat['transect_9-2012-03-14'].plot.temp()
```

transect_9-2012-04-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-04-10T19:17:00.000000000 |       59.5702 |       -151.404 | 2012-04-10T18:02:00.000000000 |


```{code-cell}
cat['transect_9-2012-04-10'].plot.salt() + cat['transect_9-2012-04-10'].plot.temp()
```

transect_9-2012-04-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5794 |       -151.357 | 2012-04-26T18:50:00.000000000 |       59.5702 |       -151.379 | 2012-04-26T18:03:00.000000000 |


```{code-cell}
cat['transect_9-2012-04-26'].plot.salt() + cat['transect_9-2012-04-26'].plot.temp()
```

transect_9-2012-05-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-05-31T19:22:00.000000000 |       59.5702 |       -151.404 | 2012-05-31T12:13:00.000000000 |


```{code-cell}
cat['transect_9-2012-05-31'].plot.salt() + cat['transect_9-2012-05-31'].plot.temp()
```

transect_9-2012-06-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-06-05T18:35:00.000000000 |       59.5702 |       -151.404 | 2012-06-05T10:16:00.000000000 |


```{code-cell}
cat['transect_9-2012-06-05'].plot.salt() + cat['transect_9-2012-06-05'].plot.temp()
```

transect_9-2012-06-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-06-27T09:52:00.000000000 |       59.5702 |       -151.404 | 2012-06-27T08:32:00.000000000 |


```{code-cell}
cat['transect_9-2012-06-27'].plot.salt() + cat['transect_9-2012-06-27'].plot.temp()
```

transect_9-2012-07-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-07-02T15:28:00.000000000 |       59.5702 |       -151.404 | 2012-07-02T14:08:00.000000000 |


```{code-cell}
cat['transect_9-2012-07-02'].plot.salt() + cat['transect_9-2012-07-02'].plot.temp()
```

transect_9-2012-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-07-21T18:04:00.000000000 |       59.5702 |       -151.404 | 2012-07-21T16:41:00.000000000 |


```{code-cell}
cat['transect_9-2012-07-21'].plot.salt() + cat['transect_9-2012-07-21'].plot.temp()
```

transect_9-2012-08-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-08-03T16:45:00.000000000 |       59.5702 |       -151.404 | 2012-08-03T15:25:00.000000000 |


```{code-cell}
cat['transect_9-2012-08-03'].plot.salt() + cat['transect_9-2012-08-03'].plot.temp()
```

transect_9-2012-08-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-08-15T15:46:00.000000000 |       59.5702 |       -151.404 | 2012-08-15T14:09:00.000000000 |


```{code-cell}
cat['transect_9-2012-08-15'].plot.salt() + cat['transect_9-2012-08-15'].plot.temp()
```

transect_9-2012-08-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-08-26T12:14:00.000000000 |       59.5702 |       -151.404 | 2012-08-26T10:55:00.000000000 |


```{code-cell}
cat['transect_9-2012-08-26'].plot.salt() + cat['transect_9-2012-08-26'].plot.temp()
```

transect_9-2012-08-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.362 | 2012-08-31T16:35:00.000000000 |       59.5718 |       -151.404 | 2012-08-31T15:14:00.000000000 |


```{code-cell}
cat['transect_9-2012-08-31'].plot.salt() + cat['transect_9-2012-08-31'].plot.temp()
```

transect_9-2012-09-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-09-21T19:18:00.000000000 |       59.5702 |       -151.404 | 2012-09-21T09:32:00.000000000 |


```{code-cell}
cat['transect_9-2012-09-21'].plot.salt() + cat['transect_9-2012-09-21'].plot.temp()
```

transect_9-2012-10-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-10-12T14:10:00.000000000 |       59.5702 |       -151.404 | 2012-10-12T12:45:00.000000000 |


```{code-cell}
cat['transect_9-2012-10-12'].plot.salt() + cat['transect_9-2012-10-12'].plot.temp()
```

transect_9-2012-10-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2012-10-29T20:53:00.000000000 |       59.5702 |       -151.404 | 2012-10-29T19:10:00.000000000 |


```{code-cell}
cat['transect_9-2012-10-29'].plot.salt() + cat['transect_9-2012-10-29'].plot.temp()
```

transect_9-2013-01-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-01-04T20:12:00.000000000 |       59.5702 |       -151.404 | 2013-01-04T18:04:00.000000000 |


```{code-cell}
cat['transect_9-2013-01-04'].plot.salt() + cat['transect_9-2013-01-04'].plot.temp()
```

transect_9-2013-02-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-02-12T11:22:00.000000000 |       59.5702 |       -151.404 | 2013-02-12T09:18:00.000000000 |


```{code-cell}
cat['transect_9-2013-02-12'].plot.salt() + cat['transect_9-2013-02-12'].plot.temp()
```

transect_9-2013-03-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-03-15T20:12:00.000000000 |       59.5702 |       -151.404 | 2013-03-15T17:58:00.000000000 |


```{code-cell}
cat['transect_9-2013-03-15'].plot.salt() + cat['transect_9-2013-03-15'].plot.temp()
```

transect_9-2013-04-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-04-21T16:18:00.000000000 |       59.5702 |       -151.404 | 2013-04-21T14:30:00.000000000 |


```{code-cell}
cat['transect_9-2013-04-21'].plot.salt() + cat['transect_9-2013-04-21'].plot.temp()
```

transect_9-2013-05-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-05-21T13:59:00.000000000 |       59.5702 |       -151.404 | 2013-05-21T12:07:00.000000000 |


```{code-cell}
cat['transect_9-2013-05-21'].plot.salt() + cat['transect_9-2013-05-21'].plot.temp()
```

transect_9-2013-06-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-06-06T11:50:00.000000000 |       59.5702 |       -151.404 | 2013-06-06T10:12:00.000000000 |


```{code-cell}
cat['transect_9-2013-06-06'].plot.salt() + cat['transect_9-2013-06-06'].plot.temp()
```

transect_9-2013-06-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-06-19T12:42:00.000000000 |       59.5702 |       -151.404 | 2013-06-19T10:48:00.000000000 |


```{code-cell}
cat['transect_9-2013-06-19'].plot.salt() + cat['transect_9-2013-06-19'].plot.temp()
```

transect_9-2013-06-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-06-28T15:09:00.000000000 |       59.5702 |       -151.404 | 2013-06-28T13:18:00.000000000 |


```{code-cell}
cat['transect_9-2013-06-28'].plot.salt() + cat['transect_9-2013-06-28'].plot.temp()
```

transect_9-2013-07-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-07-05T16:02:00.000000000 |       59.5702 |       -151.404 | 2013-07-05T14:33:00.000000000 |


```{code-cell}
cat['transect_9-2013-07-05'].plot.salt() + cat['transect_9-2013-07-05'].plot.temp()
```

transect_9-2013-07-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-07-09T19:06:00.000000000 |       59.5702 |       -151.404 | 2013-07-09T17:10:00.000000000 |


```{code-cell}
cat['transect_9-2013-07-09'].plot.salt() + cat['transect_9-2013-07-09'].plot.temp()
```

transect_9-2013-07-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-07-22T10:16:00.000000000 |       59.5702 |       -151.404 | 2013-07-22T09:01:00.000000000 |


```{code-cell}
cat['transect_9-2013-07-22'].plot.salt() + cat['transect_9-2013-07-22'].plot.temp()
```

transect_9-2013-08-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-08-07T16:38:00.000000000 |       59.5702 |       -151.404 | 2013-08-07T15:25:00.000000000 |


```{code-cell}
cat['transect_9-2013-08-07'].plot.salt() + cat['transect_9-2013-08-07'].plot.temp()
```

transect_9-2013-08-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-08-30T12:54:00.000000000 |       59.5702 |       -151.404 | 2013-08-30T11:15:00.000000000 |


```{code-cell}
cat['transect_9-2013-08-30'].plot.salt() + cat['transect_9-2013-08-30'].plot.temp()
```

transect_9-2013-09-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-09-25T15:13:00.000000000 |       59.5702 |       -151.404 | 2013-09-25T13:36:00.000000000 |


```{code-cell}
cat['transect_9-2013-09-25'].plot.salt() + cat['transect_9-2013-09-25'].plot.temp()
```

transect_9-2013-10-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-10-29T10:52:00.000000000 |       59.5702 |       -151.404 | 2013-10-29T09:08:00.000000000 |


```{code-cell}
cat['transect_9-2013-10-29'].plot.salt() + cat['transect_9-2013-10-29'].plot.temp()
```

transect_9-2013-12-03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2013-12-03T16:02:00.000000000 |       59.5702 |       -151.404 | 2013-12-03T14:16:00.000000000 |


```{code-cell}
cat['transect_9-2013-12-03'].plot.salt() + cat['transect_9-2013-12-03'].plot.temp()
```

transect_9-2014-01-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-01-09T15:39:00.000000000 |       59.5702 |       -151.404 | 2014-01-09T13:55:00.000000000 |


```{code-cell}
cat['transect_9-2014-01-09'].plot.salt() + cat['transect_9-2014-01-09'].plot.temp()
```

transect_9-2014-02-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-02-15T11:55:00.000000000 |       59.5702 |       -151.404 | 2014-02-15T10:24:00.000000000 |


```{code-cell}
cat['transect_9-2014-02-15'].plot.salt() + cat['transect_9-2014-02-15'].plot.temp()
```

transect_9-2014-03-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-03-28T15:26:00.000000000 |       59.5702 |       -151.404 | 2014-03-28T13:43:00.000000000 |


```{code-cell}
cat['transect_9-2014-03-28'].plot.salt() + cat['transect_9-2014-03-28'].plot.temp()
```

transect_9-2014-04-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-04-11T21:00:00.000000000 |       59.5702 |       -151.404 | 2014-04-11T19:49:00.000000000 |


```{code-cell}
cat['transect_9-2014-04-11'].plot.salt() + cat['transect_9-2014-04-11'].plot.temp()
```

transect_9-2014-05-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-05-28T17:20:00.000000000 |       59.5702 |       -151.404 | 2014-05-28T15:22:00.000000000 |


```{code-cell}
cat['transect_9-2014-05-28'].plot.salt() + cat['transect_9-2014-05-28'].plot.temp()
```

transect_9-2014-06-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-06-18T18:53:00.000000000 |       59.5702 |       -151.404 | 2014-06-18T16:51:00.000000000 |


```{code-cell}
cat['transect_9-2014-06-18'].plot.salt() + cat['transect_9-2014-06-18'].plot.temp()
```

transect_9-2014-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-07-21T17:18:00.000000000 |       59.5702 |       -151.404 | 2014-07-21T14:44:00.000000000 |


```{code-cell}
cat['transect_9-2014-07-21'].plot.salt() + cat['transect_9-2014-07-21'].plot.temp()
```

transect_9-2014-08-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-08-13T12:37:00.000000000 |       59.5702 |       -151.404 | 2014-08-13T10:20:00.000000000 |


```{code-cell}
cat['transect_9-2014-08-13'].plot.salt() + cat['transect_9-2014-08-13'].plot.temp()
```

transect_9-2014-10-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-10-19T11:31:00.000000000 |       59.5702 |       -151.404 | 2014-10-19T10:03:00.000000000 |


```{code-cell}
cat['transect_9-2014-10-19'].plot.salt() + cat['transect_9-2014-10-19'].plot.temp()
```

transect_9-2014-11-25
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-11-25T17:08:00.000000000 |       59.5702 |       -151.404 | 2014-11-25T15:40:00.000000000 |


```{code-cell}
cat['transect_9-2014-11-25'].plot.salt() + cat['transect_9-2014-11-25'].plot.temp()
```

transect_9-2014-12-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2014-12-17T12:50:00.000000000 |       59.5702 |       -151.404 | 2014-12-17T11:11:00.000000000 |


```{code-cell}
cat['transect_9-2014-12-17'].plot.salt() + cat['transect_9-2014-12-17'].plot.temp()
```

transect_9-2015-01-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-01-16T15:25:00.000000000 |       59.5702 |       -151.404 | 2015-01-16T14:01:00.000000000 |


```{code-cell}
cat['transect_9-2015-01-16'].plot.salt() + cat['transect_9-2015-01-16'].plot.temp()
```

transect_9-2015-02-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-02-12T17:06:00.000000000 |       59.5702 |       -151.404 | 2015-02-12T15:45:00.000000000 |


```{code-cell}
cat['transect_9-2015-02-12'].plot.salt() + cat['transect_9-2015-02-12'].plot.temp()
```

transect_9-2015-02-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.385 | 2015-02-24T19:26:00.000000000 |       59.5824 |       -151.404 | 2015-02-24T19:14:00.000000000 |


```{code-cell}
cat['transect_9-2015-02-24'].plot.salt() + cat['transect_9-2015-02-24'].plot.temp()
```

transect_9-2015-03-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-03-31T14:43:00.000000000 |       59.5702 |       -151.404 | 2015-03-31T13:07:00.000000000 |


```{code-cell}
cat['transect_9-2015-03-31'].plot.salt() + cat['transect_9-2015-03-31'].plot.temp()
```

transect_9-2015-04-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-04-08T15:26:00.000000000 |       59.5702 |       -151.404 | 2015-04-08T13:54:00.000000000 |


```{code-cell}
cat['transect_9-2015-04-08'].plot.salt() + cat['transect_9-2015-04-08'].plot.temp()
```

transect_9-2015-05-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-05-28T13:29:00.000000000 |       59.5702 |       -151.404 | 2015-05-28T11:38:00.000000000 |


```{code-cell}
cat['transect_9-2015-05-28'].plot.salt() + cat['transect_9-2015-05-28'].plot.temp()
```

transect_9-2015-06-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-06-26T12:43:00.000000000 |       59.5702 |       -151.404 | 2015-06-26T10:38:00.000000000 |


```{code-cell}
cat['transect_9-2015-06-26'].plot.salt() + cat['transect_9-2015-06-26'].plot.temp()
```

transect_9-2015-07-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-07-10T11:51:00.000000000 |       59.5702 |       -151.404 | 2015-07-10T09:48:00.000000000 |


```{code-cell}
cat['transect_9-2015-07-10'].plot.salt() + cat['transect_9-2015-07-10'].plot.temp()
```

transect_9-2015-07-29
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-07-29T15:18:00.000000000 |       59.5702 |       -151.404 | 2015-07-29T13:21:00.000000000 |


```{code-cell}
cat['transect_9-2015-07-29'].plot.salt() + cat['transect_9-2015-07-29'].plot.temp()
```

transect_9-2015-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-08-14T18:30:00.000000000 |       59.5702 |       -151.404 | 2015-08-14T16:45:00.000000000 |


```{code-cell}
cat['transect_9-2015-08-14'].plot.salt() + cat['transect_9-2015-08-14'].plot.temp()
```

transect_9-2015-09-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-09-04T11:20:00.000000000 |       59.5702 |       -151.404 | 2015-09-04T09:22:00.000000000 |


```{code-cell}
cat['transect_9-2015-09-04'].plot.salt() + cat['transect_9-2015-09-04'].plot.temp()
```

transect_9-2015-09-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-09-24T14:29:00.000000000 |       59.5702 |       -151.404 | 2015-09-24T13:16:00.000000000 |


```{code-cell}
cat['transect_9-2015-09-24'].plot.salt() + cat['transect_9-2015-09-24'].plot.temp()
```

transect_9-2015-10-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-10-19T15:42:00.000000000 |       59.5702 |       -151.404 | 2015-10-19T14:12:00.000000000 |


```{code-cell}
cat['transect_9-2015-10-19'].plot.salt() + cat['transect_9-2015-10-19'].plot.temp()
```

transect_9-2015-11-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-11-04T22:31:00.000000000 |       59.5702 |       -151.404 | 2015-11-04T20:30:00.000000000 |


```{code-cell}
cat['transect_9-2015-11-04'].plot.salt() + cat['transect_9-2015-11-04'].plot.temp()
```

transect_9-2015-12-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2015-12-10T13:04:00.000000000 |       59.5702 |       -151.404 | 2015-12-10T11:42:00.000000000 |


```{code-cell}
cat['transect_9-2015-12-10'].plot.salt() + cat['transect_9-2015-12-10'].plot.temp()
```

transect_9-2016-01-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-01-07T13:36:00.000000000 |       59.5702 |       -151.404 | 2016-01-07T12:07:00.000000000 |


```{code-cell}
cat['transect_9-2016-01-07'].plot.salt() + cat['transect_9-2016-01-07'].plot.temp()
```

transect_9-2016-02-09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-02-09T15:03:00.000000000 |       59.5702 |       -151.404 | 2016-02-09T13:48:00.000000000 |


```{code-cell}
cat['transect_9-2016-02-09'].plot.salt() + cat['transect_9-2016-02-09'].plot.temp()
```

transect_9-2016-04-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-04-07T15:45:00.000000000 |       59.5702 |       -151.404 | 2016-04-07T14:05:00.000000000 |


```{code-cell}
cat['transect_9-2016-04-07'].plot.salt() + cat['transect_9-2016-04-07'].plot.temp()
```

transect_9-2016-05-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-05-12T14:23:00.000000000 |       59.5702 |       -151.404 | 2016-05-12T12:59:00.000000000 |


```{code-cell}
cat['transect_9-2016-05-12'].plot.salt() + cat['transect_9-2016-05-12'].plot.temp()
```

transect_9-2016-06-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-06-16T13:30:00.000000000 |       59.5702 |       -151.404 | 2016-06-16T11:52:00.000000000 |


```{code-cell}
cat['transect_9-2016-06-16'].plot.salt() + cat['transect_9-2016-06-16'].plot.temp()
```

transect_9-2016-07-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-07-27T11:57:00.000000000 |       59.5702 |       -151.404 | 2016-07-27T10:18:00.000000000 |


```{code-cell}
cat['transect_9-2016-07-27'].plot.salt() + cat['transect_9-2016-07-27'].plot.temp()
```

transect_9-2016-09-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-09-23T12:22:00.000000000 |       59.5702 |       -151.404 | 2016-09-23T10:40:00.000000000 |


```{code-cell}
cat['transect_9-2016-09-23'].plot.salt() + cat['transect_9-2016-09-23'].plot.temp()
```

transect_9-2016-10-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-10-13T14:11:00.000000000 |       59.5702 |       -151.404 | 2016-10-13T12:40:00.000000000 |


```{code-cell}
cat['transect_9-2016-10-13'].plot.salt() + cat['transect_9-2016-10-13'].plot.temp()
```

transect_9-2016-11-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-11-10T15:04:00.000000000 |       59.5702 |       -151.404 | 2016-11-10T13:24:00.000000000 |


```{code-cell}
cat['transect_9-2016-11-10'].plot.salt() + cat['transect_9-2016-11-10'].plot.temp()
```

transect_9-2016-12-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2016-12-13T19:10:00.000000000 |       59.5702 |       -151.404 | 2016-12-13T17:30:00.000000000 |


```{code-cell}
cat['transect_9-2016-12-13'].plot.salt() + cat['transect_9-2016-12-13'].plot.temp()
```

transect_9-2017-01-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-01-11T14:19:00.000000000 |       59.5702 |       -151.404 | 2017-01-11T12:38:00.000000000 |


```{code-cell}
cat['transect_9-2017-01-11'].plot.salt() + cat['transect_9-2017-01-11'].plot.temp()
```

transect_9-2017-02-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-02-07T12:09:00.000000000 |       59.5702 |       -151.404 | 2017-02-07T10:36:00.000000000 |


```{code-cell}
cat['transect_9-2017-02-07'].plot.salt() + cat['transect_9-2017-02-07'].plot.temp()
```

transect_9-2017-03-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-03-28T15:24:00.000000000 |       59.5702 |       -151.404 | 2017-03-28T13:50:00.000000000 |


```{code-cell}
cat['transect_9-2017-03-28'].plot.salt() + cat['transect_9-2017-03-28'].plot.temp()
```

transect_9-2017-04-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-04-20T22:51:00.000000000 |       59.5702 |       -151.404 | 2017-04-20T21:10:00.000000000 |


```{code-cell}
cat['transect_9-2017-04-20'].plot.salt() + cat['transect_9-2017-04-20'].plot.temp()
```

transect_9-2017-05-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-05-30T13:49:00.000000000 |       59.5702 |       -151.404 | 2017-05-30T12:05:00.000000000 |


```{code-cell}
cat['transect_9-2017-05-30'].plot.salt() + cat['transect_9-2017-05-30'].plot.temp()
```

transect_9-2017-06-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-06-28T13:09:00.000000000 |       59.5702 |       -151.404 | 2017-06-28T11:20:00.000000000 |


```{code-cell}
cat['transect_9-2017-06-28'].plot.salt() + cat['transect_9-2017-06-28'].plot.temp()
```

transect_9-2017-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-07-24T10:54:00.000000000 |       59.5702 |       -151.404 | 2017-07-24T09:03:00.000000000 |


```{code-cell}
cat['transect_9-2017-07-24'].plot.salt() + cat['transect_9-2017-07-24'].plot.temp()
```

transect_9-2017-08-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-08-24T18:32:00.000000000 |       59.5702 |       -151.404 | 2017-08-24T16:59:00.000000000 |


```{code-cell}
cat['transect_9-2017-08-24'].plot.salt() + cat['transect_9-2017-08-24'].plot.temp()
```

transect_9-2017-09-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-09-22T16:15:00.000000000 |       59.5702 |       -151.404 | 2017-09-22T14:42:00.000000000 |


```{code-cell}
cat['transect_9-2017-09-22'].plot.salt() + cat['transect_9-2017-09-22'].plot.temp()
```

transect_9-2017-10-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-10-17T15:31:00.000000000 |       59.5702 |       -151.404 | 2017-10-17T14:00:00.000000000 |


```{code-cell}
cat['transect_9-2017-10-17'].plot.salt() + cat['transect_9-2017-10-17'].plot.temp()
```

transect_9-2017-11-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-11-07T17:16:00.000000000 |       59.5702 |       -151.404 | 2017-11-07T15:47:00.000000000 |


```{code-cell}
cat['transect_9-2017-11-07'].plot.salt() + cat['transect_9-2017-11-07'].plot.temp()
```

transect_9-2017-12-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2017-12-14T12:07:00.000000000 |       59.5702 |       -151.404 | 2017-12-14T10:38:00.000000000 |


```{code-cell}
cat['transect_9-2017-12-14'].plot.salt() + cat['transect_9-2017-12-14'].plot.temp()
```

transect_9-2018-01-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-01-17T14:54:00.000000000 |       59.5702 |       -151.404 | 2018-01-17T13:26:00.000000000 |


```{code-cell}
cat['transect_9-2018-01-17'].plot.salt() + cat['transect_9-2018-01-17'].plot.temp()
```

transect_9-2018-03-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-03-02T16:11:00.000000000 |       59.5702 |       -151.404 | 2018-03-02T14:46:00.000000000 |


```{code-cell}
cat['transect_9-2018-03-02'].plot.salt() + cat['transect_9-2018-03-02'].plot.temp()
```

transect_9-2018-03-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-03-27T11:31:00.000000000 |       59.5702 |       -151.404 | 2018-03-27T09:56:00.000000000 |


```{code-cell}
cat['transect_9-2018-03-27'].plot.salt() + cat['transect_9-2018-03-27'].plot.temp()
```

transect_9-2018-04-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-04-23T12:34:00.000000000 |       59.5702 |       -151.404 | 2018-04-23T10:52:00.000000000 |


```{code-cell}
cat['transect_9-2018-04-23'].plot.salt() + cat['transect_9-2018-04-23'].plot.temp()
```

transect_9-2018-05-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-05-24T15:34:00.000000000 |       59.5702 |       -151.404 | 2018-05-24T14:07:00.000000000 |


```{code-cell}
cat['transect_9-2018-05-24'].plot.salt() + cat['transect_9-2018-05-24'].plot.temp()
```

transect_9-2018-06-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-06-22T15:07:00.000000000 |       59.5702 |       -151.404 | 2018-06-22T13:40:00.000000000 |


```{code-cell}
cat['transect_9-2018-06-22'].plot.salt() + cat['transect_9-2018-06-22'].plot.temp()
```

transect_9-2018-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-07-24T14:14:00.000000000 |       59.5702 |       -151.404 | 2018-07-24T12:43:00.000000000 |


```{code-cell}
cat['transect_9-2018-07-24'].plot.salt() + cat['transect_9-2018-07-24'].plot.temp()
```

transect_9-2018-08-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-08-23T15:59:00.000000000 |       59.5702 |       -151.404 | 2018-08-23T14:14:00.000000000 |


```{code-cell}
cat['transect_9-2018-08-23'].plot.salt() + cat['transect_9-2018-08-23'].plot.temp()
```

transect_9-2018-09-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-09-13T15:35:00.000000000 |       59.5702 |       -151.404 | 2018-09-13T14:10:00.000000000 |


```{code-cell}
cat['transect_9-2018-09-13'].plot.salt() + cat['transect_9-2018-09-13'].plot.temp()
```

transect_9-2018-10-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-10-17T15:51:00.000000000 |       59.5702 |       -151.404 | 2018-10-17T14:28:00.000000000 |


```{code-cell}
cat['transect_9-2018-10-17'].plot.salt() + cat['transect_9-2018-10-17'].plot.temp()
```

transect_9-2018-11-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-11-08T15:08:00.000000000 |       59.5702 |       -151.404 | 2018-11-08T13:43:00.000000000 |


```{code-cell}
cat['transect_9-2018-11-08'].plot.salt() + cat['transect_9-2018-11-08'].plot.temp()
```

transect_9-2018-12-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2018-12-06T15:48:00.000000000 |       59.5702 |       -151.404 | 2018-12-06T14:28:00.000000000 |


```{code-cell}
cat['transect_9-2018-12-06'].plot.salt() + cat['transect_9-2018-12-06'].plot.temp()
```

transect_9-2019-02-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-02-07T16:38:00.000000000 |       59.5702 |       -151.404 | 2019-02-07T15:17:00.000000000 |


```{code-cell}
cat['transect_9-2019-02-07'].plot.salt() + cat['transect_9-2019-02-07'].plot.temp()
```

transect_9-2019-03-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5925 |       -151.357 | 2019-03-19T14:41:00.000000000 |       59.5702 |       -151.399 | 2019-03-19T13:16:00.000000000 |


```{code-cell}
cat['transect_9-2019-03-19'].plot.salt() + cat['transect_9-2019-03-19'].plot.temp()
```

transect_9-2019-04-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-04-24T15:17:00.000000000 |       59.5702 |       -151.404 | 2019-04-24T13:37:00.000000000 |


```{code-cell}
cat['transect_9-2019-04-24'].plot.salt() + cat['transect_9-2019-04-24'].plot.temp()
```

transect_9-2019-05-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-05-14T18:41:00.000000000 |       59.5702 |       -151.404 | 2019-05-14T17:25:00.000000000 |


```{code-cell}
cat['transect_9-2019-05-14'].plot.salt() + cat['transect_9-2019-05-14'].plot.temp()
```

transect_9-2019-06-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-06-19T17:57:00.000000000 |       59.5702 |       -151.404 | 2019-06-19T15:57:00.000000000 |


```{code-cell}
cat['transect_9-2019-06-19'].plot.salt() + cat['transect_9-2019-06-19'].plot.temp()
```

transect_9-2019-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-07-23T17:18:00.000000000 |       59.5702 |       -151.404 | 2019-07-23T15:24:00.000000000 |


```{code-cell}
cat['transect_9-2019-07-23'].plot.salt() + cat['transect_9-2019-07-23'].plot.temp()
```

transect_9-2019-09-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-09-16T11:37:00.000000000 |       59.5702 |       -151.404 | 2019-09-16T09:29:00.000000000 |


```{code-cell}
cat['transect_9-2019-09-16'].plot.salt() + cat['transect_9-2019-09-16'].plot.temp()
```

transect_9-2019-10-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-10-30T16:08:00.000000000 |       59.5702 |       -151.404 | 2019-10-30T14:21:00.000000000 |


```{code-cell}
cat['transect_9-2019-10-30'].plot.salt() + cat['transect_9-2019-10-30'].plot.temp()
```

transect_9-2019-11-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-11-15T17:29:00.000000000 |       59.5702 |       -151.404 | 2019-11-15T15:44:00.000000000 |


```{code-cell}
cat['transect_9-2019-11-15'].plot.salt() + cat['transect_9-2019-11-15'].plot.temp()
```

transect_9-2019-12-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2019-12-12T15:32:00.000000000 |       59.5702 |       -151.404 | 2019-12-12T14:00:00.000000000 |


```{code-cell}
cat['transect_9-2019-12-12'].plot.salt() + cat['transect_9-2019-12-12'].plot.temp()
```

transect_9-2020-02-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5794 |       -151.357 | 2020-02-06T14:30:00.000000000 |       59.5702 |       -151.379 | 2020-02-06T13:55:00.000000000 |


```{code-cell}
cat['transect_9-2020-02-06'].plot.salt() + cat['transect_9-2020-02-06'].plot.temp()
```

transect_9-2020-03-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2020-03-18T15:46:00.000000000 |       59.5702 |       -151.404 | 2020-03-18T14:20:00.000000000 |


```{code-cell}
cat['transect_9-2020-03-18'].plot.salt() + cat['transect_9-2020-03-18'].plot.temp()
```

transect_9-2020-06-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2020-06-04T12:39:00.000000000 |       59.5702 |       -151.404 | 2020-06-04T11:24:00.000000000 |


```{code-cell}
cat['transect_9-2020-06-04'].plot.salt() + cat['transect_9-2020-06-04'].plot.temp()
```

transect_9-2020-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2020-07-24T14:45:00.000000000 |       59.5702 |       -151.404 | 2020-07-24T13:02:00.000000000 |


```{code-cell}
cat['transect_9-2020-07-24'].plot.salt() + cat['transect_9-2020-07-24'].plot.temp()
```

transect_9-2020-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2020-08-14T15:15:00.000000000 |       59.5702 |       -151.404 | 2020-08-14T13:47:00.000000000 |


```{code-cell}
cat['transect_9-2020-08-14'].plot.salt() + cat['transect_9-2020-08-14'].plot.temp()
```

transect_9-2020-09-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2020-09-21T11:12:00.000000000 |       59.5702 |       -151.404 | 2020-09-21T09:35:00.000000000 |


```{code-cell}
cat['transect_9-2020-09-21'].plot.salt() + cat['transect_9-2020-09-21'].plot.temp()
```

transect_9-2020-10-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5925 |       -151.357 | 2020-10-15T15:43:00.000000000 |       59.5702 |       -151.399 | 2020-10-15T14:32:00.000000000 |


```{code-cell}
cat['transect_9-2020-10-15'].plot.salt() + cat['transect_9-2020-10-15'].plot.temp()
```

transect_9-2020-12-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2020-12-28T11:54:00.000000000 |       59.5702 |       -151.404 | 2020-12-28T10:50:00.000000000 |


```{code-cell}
cat['transect_9-2020-12-28'].plot.salt() + cat['transect_9-2020-12-28'].plot.temp()
```

transect_9-2021-01-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-01-13T15:24:00.000000000 |       59.5702 |       -151.404 | 2021-01-13T14:11:00.000000000 |


```{code-cell}
cat['transect_9-2021-01-13'].plot.salt() + cat['transect_9-2021-01-13'].plot.temp()
```

transect_9-2021-02-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-02-17T14:47:00.000000000 |       59.5702 |       -151.404 | 2021-02-17T13:36:00.000000000 |


```{code-cell}
cat['transect_9-2021-02-17'].plot.salt() + cat['transect_9-2021-02-17'].plot.temp()
```

transect_9-2021-03-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-03-23T16:30:00.000000000 |       59.5702 |       -151.404 | 2021-03-23T15:08:00.000000000 |


```{code-cell}
cat['transect_9-2021-03-23'].plot.salt() + cat['transect_9-2021-03-23'].plot.temp()
```

transect_9-2021-04-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-04-16T17:52:00.000000000 |       59.5702 |       -151.404 | 2021-04-16T16:37:00.000000000 |


```{code-cell}
cat['transect_9-2021-04-16'].plot.salt() + cat['transect_9-2021-04-16'].plot.temp()
```

transect_9-2021-05-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-05-06T16:01:00.000000000 |       59.5702 |       -151.404 | 2021-05-06T14:42:00.000000000 |


```{code-cell}
cat['transect_9-2021-05-06'].plot.salt() + cat['transect_9-2021-05-06'].plot.temp()
```

transect_9-2021-06-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5925 |       -151.357 | 2021-06-21T15:21:00.000000000 |       59.5702 |       -151.399 | 2021-06-21T14:05:00.000000000 |


```{code-cell}
cat['transect_9-2021-06-21'].plot.salt() + cat['transect_9-2021-06-21'].plot.temp()
```

transect_9-2021-07-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-07-16T11:34:00.000000000 |       59.5702 |       -151.404 | 2021-07-16T09:37:00.000000000 |


```{code-cell}
cat['transect_9-2021-07-16'].plot.salt() + cat['transect_9-2021-07-16'].plot.temp()
```

transect_9-2021-08-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-08-17T16:16:00.000000000 |       59.5702 |       -151.404 | 2021-08-17T14:45:00.000000000 |


```{code-cell}
cat['transect_9-2021-08-17'].plot.salt() + cat['transect_9-2021-08-17'].plot.temp()
```

transect_9-2021-09-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-09-17T14:37:00.000000000 |       59.5702 |       -151.404 | 2021-09-17T13:13:00.000000000 |


```{code-cell}
cat['transect_9-2021-09-17'].plot.salt() + cat['transect_9-2021-09-17'].plot.temp()
```

transect_9-2021-10-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-10-21T16:39:00.000000000 |       59.5702 |       -151.404 | 2021-10-21T15:07:00.000000000 |


```{code-cell}
cat['transect_9-2021-10-21'].plot.salt() + cat['transect_9-2021-10-21'].plot.temp()
```

transect_9-2021-11-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-11-14T16:06:00.000000000 |       59.5702 |       -151.404 | 2021-11-14T14:33:00.000000000 |


```{code-cell}
cat['transect_9-2021-11-14'].plot.salt() + cat['transect_9-2021-11-14'].plot.temp()
```

transect_9-2021-12-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2021-12-18T15:11:00.000000000 |       59.5702 |       -151.404 | 2021-12-18T13:53:00.000000000 |


```{code-cell}
cat['transect_9-2021-12-18'].plot.salt() + cat['transect_9-2021-12-18'].plot.temp()
```

transect_9-2022-01-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-01-31T15:33:00.000000000 |       59.5702 |       -151.404 | 2022-01-31T14:08:00.000000000 |


```{code-cell}
cat['transect_9-2022-01-31'].plot.salt() + cat['transect_9-2022-01-31'].plot.temp()
```

transect_9-2022-03-01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-03-01T14:36:00.000000000 |       59.5702 |       -151.404 | 2022-03-01T13:22:00.000000000 |


```{code-cell}
cat['transect_9-2022-03-01'].plot.salt() + cat['transect_9-2022-03-01'].plot.temp()
```

transect_9-2022-03-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-03-22T13:19:00.000000000 |       59.5702 |       -151.404 | 2022-03-22T12:05:00.000000000 |


```{code-cell}
cat['transect_9-2022-03-22'].plot.salt() + cat['transect_9-2022-03-22'].plot.temp()
```

transect_9-2022-04-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-04-13T13:00:00.000000000 |       59.5702 |       -151.404 | 2022-04-13T11:57:00.000000000 |


```{code-cell}
cat['transect_9-2022-04-13'].plot.salt() + cat['transect_9-2022-04-13'].plot.temp()
```

transect_9-2022-05-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-05-23T15:45:00.000000000 |       59.5702 |       -151.404 | 2022-05-23T14:38:00.000000000 |


```{code-cell}
cat['transect_9-2022-05-23'].plot.salt() + cat['transect_9-2022-05-23'].plot.temp()
```

transect_9-2022-06-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-06-24T15:32:00.000000000 |       59.5702 |       -151.404 | 2022-06-24T14:19:00.000000000 |


```{code-cell}
cat['transect_9-2022-06-24'].plot.salt() + cat['transect_9-2022-06-24'].plot.temp()
```

transect_9-2022-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-07-23T14:34:00.000000000 |       59.5702 |       -151.404 | 2022-07-23T13:23:00.000000000 |


```{code-cell}
cat['transect_9-2022-07-23'].plot.salt() + cat['transect_9-2022-07-23'].plot.temp()
```

transect_9-2022-08-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.596 |       -151.357 | 2022-08-24T15:06:00.000000000 |       59.5702 |       -151.404 | 2022-08-24T14:08:00.000000000 |


```{code-cell}
cat['transect_9-2022-08-24'].plot.salt() + cat['transect_9-2022-08-24'].plot.temp()
```

## transect_AlongBay

+++

transect_AlongBay-2012-08-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2012-08-15T11:31:00.000000000 |          59.5 |       -151.888 | 2012-08-15T09:35:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2012-08-15'].plot.salt() + cat['transect_AlongBay-2012-08-15'].plot.temp()
```

transect_AlongBay-2013-02-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2013-02-12T23:59:00.000000000 |          59.5 |       -151.888 | 2013-02-12T16:35:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2013-02-12'].plot.salt() + cat['transect_AlongBay-2013-02-12'].plot.temp()
```

transect_AlongBay-2013-02-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.7203 |       -151.125 | 2013-02-13T00:30:00.000000000 |       59.7203 |       -151.125 | 2013-02-13T00:27:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2013-02-13'].plot.salt() + cat['transect_AlongBay-2013-02-13'].plot.temp()
```

transect_AlongBay-2013-06-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2013-06-06T13:44:00.000000000 |          59.5 |       -151.888 | 2013-06-06T12:06:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2013-06-06'].plot.salt() + cat['transect_AlongBay-2013-06-06'].plot.temp()
```

transect_AlongBay-2014-03-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.6583 |       -151.208 | 2014-03-28T17:31:00.000000000 |          59.5 |       -151.888 | 2014-03-28T11:51:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2014-03-28'].plot.salt() + cat['transect_AlongBay-2014-03-28'].plot.temp()
```

transect_AlongBay-2014-05-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.632 |        -151.25 | 2014-05-28T14:38:00.000000000 |        59.525 |        -151.65 | 2014-05-28T10:49:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2014-05-28'].plot.salt() + cat['transect_AlongBay-2014-05-28'].plot.temp()
```

transect_AlongBay-2014-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2014-08-14T14:25:00.000000000 |          59.5 |       -151.888 | 2014-08-14T09:20:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2014-08-14'].plot.salt() + cat['transect_AlongBay-2014-08-14'].plot.temp()
```

transect_AlongBay-2015-07-10
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2015-07-10T17:54:00.000000000 |        59.445 |           -152 | 2015-07-10T12:43:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2015-07-10'].plot.salt() + cat['transect_AlongBay-2015-07-10'].plot.temp()
```

transect_AlongBay-2015-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.563 |        -151.46 | 2015-08-14T16:26:00.000000000 |        59.445 |           -152 | 2015-08-14T14:15:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2015-08-14'].plot.salt() + cat['transect_AlongBay-2015-08-14'].plot.temp()
```

transect_AlongBay-2016-01-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.613 |       -151.295 | 2016-01-07T15:56:00.000000000 |        59.552 |        -151.53 | 2016-01-07T14:16:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2016-01-07'].plot.salt() + cat['transect_AlongBay-2016-01-07'].plot.temp()
```

transect_AlongBay-2016-05-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.632 |        -151.25 | 2016-05-12T20:00:00.000000000 |        59.383 |        -152.05 | 2016-05-12T16:02:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2016-05-12'].plot.salt() + cat['transect_AlongBay-2016-05-12'].plot.temp()
```

transect_AlongBay-2016-06-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.712 |       -151.116 | 2016-06-16T16:36:00.000000000 |        59.525 |        -151.65 | 2016-06-16T14:36:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2016-06-16'].plot.salt() + cat['transect_AlongBay-2016-06-16'].plot.temp()
```

transect_AlongBay-2016-07-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.632 |        -151.25 | 2016-07-27T16:50:00.000000000 |          59.5 |       -151.888 | 2016-07-27T14:59:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2016-07-27'].plot.salt() + cat['transect_AlongBay-2016-07-27'].plot.temp()
```

transect_AlongBay-2017-01-11
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5824 |       -151.385 | 2017-01-11T15:52:00.000000000 |        59.525 |        -151.65 | 2017-01-11T15:04:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-01-11'].plot.salt() + cat['transect_AlongBay-2017-01-11'].plot.temp()
```

transect_AlongBay-2017-02-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.592 |        -151.35 | 2017-02-07T16:49:00.000000000 |          59.5 |       -151.888 | 2017-02-07T13:02:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-02-07'].plot.salt() + cat['transect_AlongBay-2017-02-07'].plot.temp()
```

transect_AlongBay-2017-03-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.6583 |       -151.208 | 2017-03-28T13:14:00.000000000 |          59.5 |       -151.888 | 2017-03-28T10:49:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-03-28'].plot.salt() + cat['transect_AlongBay-2017-03-28'].plot.temp()
```

transect_AlongBay-2017-04-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.613 |       -151.295 | 2017-04-20T20:20:00.000000000 |          59.5 |       -151.888 | 2017-04-20T16:57:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-04-20'].plot.salt() + cat['transect_AlongBay-2017-04-20'].plot.temp()
```

transect_AlongBay-2017-05-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2017-05-30T16:37:00.000000000 |        59.525 |        -151.65 | 2017-05-30T14:28:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-05-30'].plot.salt() + cat['transect_AlongBay-2017-05-30'].plot.temp()
```

transect_AlongBay-2017-06-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.632 |        -151.25 | 2017-06-28T15:27:00.000000000 |        59.525 |        -151.65 | 2017-06-28T13:47:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-06-28'].plot.salt() + cat['transect_AlongBay-2017-06-28'].plot.temp()
```

transect_AlongBay-2017-07-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2017-07-24T14:59:00.000000000 |        59.525 |        -151.65 | 2017-07-24T12:13:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-07-24'].plot.salt() + cat['transect_AlongBay-2017-07-24'].plot.temp()
```

transect_AlongBay-2017-07-26
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.552 |        -151.53 | 2017-07-26T10:46:00.000000000 |        59.383 |        -152.05 | 2017-07-26T09:18:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-07-26'].plot.salt() + cat['transect_AlongBay-2017-07-26'].plot.temp()
```

transect_AlongBay-2017-08-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2017-08-24T16:22:00.000000000 |        59.525 |        -151.65 | 2017-08-24T14:03:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-08-24'].plot.salt() + cat['transect_AlongBay-2017-08-24'].plot.temp()
```

transect_AlongBay-2017-09-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2017-09-22T13:26:00.000000000 |          59.5 |       -151.888 | 2017-09-22T10:39:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-09-22'].plot.salt() + cat['transect_AlongBay-2017-09-22'].plot.temp()
```

transect_AlongBay-2017-10-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2017-10-20T14:02:00.000000000 |        59.518 |       -151.728 | 2017-10-20T11:01:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-10-20'].plot.salt() + cat['transect_AlongBay-2017-10-20'].plot.temp()
```

transect_AlongBay-2017-11-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5824 |       -151.385 | 2017-11-02T17:10:00.000000000 |        59.383 |        -152.05 | 2017-11-02T15:04:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-11-02'].plot.salt() + cat['transect_AlongBay-2017-11-02'].plot.temp()
```

transect_AlongBay-2017-11-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2017-11-07T14:55:00.000000000 |          59.5 |       -151.888 | 2017-11-07T11:49:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-11-07'].plot.salt() + cat['transect_AlongBay-2017-11-07'].plot.temp()
```

transect_AlongBay-2017-12-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.6583 |       -151.208 | 2017-12-14T14:33:00.000000000 |        59.525 |        -151.65 | 2017-12-14T12:53:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2017-12-14'].plot.salt() + cat['transect_AlongBay-2017-12-14'].plot.temp()
```

transect_AlongBay-2018-01-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2018-01-17T12:41:00.000000000 |        59.525 |        -151.65 | 2018-01-17T10:45:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-01-17'].plot.salt() + cat['transect_AlongBay-2018-01-17'].plot.temp()
```

transect_AlongBay-2018-03-02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.6583 |       -151.208 | 2018-03-02T14:15:00.000000000 |          59.5 |       -151.888 | 2018-03-02T11:40:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-03-02'].plot.salt() + cat['transect_AlongBay-2018-03-02'].plot.temp()
```

transect_AlongBay-2018-03-27
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.712 |       -151.116 | 2018-03-27T16:38:00.000000000 |        59.383 |        -152.05 | 2018-03-27T13:18:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-03-27'].plot.salt() + cat['transect_AlongBay-2018-03-27'].plot.temp()
```

transect_AlongBay-2018-04-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-04-23T18:30:00.000000000 |          59.5 |       -151.888 | 2018-04-23T15:40:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-04-23'].plot.salt() + cat['transect_AlongBay-2018-04-23'].plot.temp()
```

transect_AlongBay-2018-05-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-05-24T13:24:00.000000000 |          59.5 |       -151.888 | 2018-05-24T10:31:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-05-24'].plot.salt() + cat['transect_AlongBay-2018-05-24'].plot.temp()
```

transect_AlongBay-2018-06-22
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-06-22T13:06:00.000000000 |          59.5 |       -151.888 | 2018-06-22T10:13:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-06-22'].plot.salt() + cat['transect_AlongBay-2018-06-22'].plot.temp()
```

transect_AlongBay-2018-07-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-07-18T16:42:00.000000000 |        59.383 |        -152.05 | 2018-07-18T13:19:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-07-18'].plot.salt() + cat['transect_AlongBay-2018-07-18'].plot.temp()
```

transect_AlongBay-2018-08-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-08-23T13:37:00.000000000 |          59.5 |       -151.888 | 2018-08-23T10:28:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-08-23'].plot.salt() + cat['transect_AlongBay-2018-08-23'].plot.temp()
```

transect_AlongBay-2018-09-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-09-17T17:35:00.000000000 |        59.383 |        -152.05 | 2018-09-17T14:08:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-09-17'].plot.salt() + cat['transect_AlongBay-2018-09-17'].plot.temp()
```

transect_AlongBay-2018-10-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-10-17T13:39:00.000000000 |          59.5 |       -151.888 | 2018-10-17T10:33:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-10-17'].plot.salt() + cat['transect_AlongBay-2018-10-17'].plot.temp()
```

transect_AlongBay-2018-11-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-11-08T12:53:00.000000000 |        59.552 |        -151.53 | 2018-11-08T10:47:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-11-08'].plot.salt() + cat['transect_AlongBay-2018-11-08'].plot.temp()
```

transect_AlongBay-2018-12-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2018-12-06T13:54:00.000000000 |          59.5 |       -151.888 | 2018-12-06T10:53:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2018-12-06'].plot.salt() + cat['transect_AlongBay-2018-12-06'].plot.temp()
```

transect_AlongBay-2019-02-07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-02-07T14:44:00.000000000 |        59.552 |        -151.53 | 2019-02-07T12:45:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-02-07'].plot.salt() + cat['transect_AlongBay-2019-02-07'].plot.temp()
```

transect_AlongBay-2019-03-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-03-19T12:34:00.000000000 |          59.5 |       -151.888 | 2019-03-19T09:13:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-03-19'].plot.salt() + cat['transect_AlongBay-2019-03-19'].plot.temp()
```

transect_AlongBay-2019-04-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-04-24T12:58:00.000000000 |        59.518 |       -151.728 | 2019-04-24T09:58:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-04-24'].plot.salt() + cat['transect_AlongBay-2019-04-24'].plot.temp()
```

transect_AlongBay-2019-05-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-05-14T16:45:00.000000000 |          59.5 |       -151.888 | 2019-05-14T14:00:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-05-14'].plot.salt() + cat['transect_AlongBay-2019-05-14'].plot.temp()
```

transect_AlongBay-2019-06-19
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.712 |       -151.116 | 2019-06-19T14:53:00.000000000 |          59.5 |       -151.888 | 2019-06-19T11:21:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-06-19'].plot.salt() + cat['transect_AlongBay-2019-06-19'].plot.temp()
```

transect_AlongBay-2019-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-07-23T14:36:00.000000000 |          59.5 |       -151.888 | 2019-07-23T11:05:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-07-23'].plot.salt() + cat['transect_AlongBay-2019-07-23'].plot.temp()
```

transect_AlongBay-2019-10-30
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-10-30T13:46:00.000000000 |        59.518 |       -151.728 | 2019-10-30T10:43:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-10-30'].plot.salt() + cat['transect_AlongBay-2019-10-30'].plot.temp()
```

transect_AlongBay-2019-11-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2019-11-15T15:06:00.000000000 |        59.518 |       -151.728 | 2019-11-15T11:52:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-11-15'].plot.salt() + cat['transect_AlongBay-2019-11-15'].plot.temp()
```

transect_AlongBay-2019-12-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2019-12-12T13:32:00.000000000 |        59.518 |       -151.728 | 2019-12-12T10:38:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2019-12-12'].plot.salt() + cat['transect_AlongBay-2019-12-12'].plot.temp()
```

transect_AlongBay-2020-02-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-02-06T13:20:00.000000000 |        59.518 |       -151.728 | 2020-02-06T10:28:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-02-06'].plot.salt() + cat['transect_AlongBay-2020-02-06'].plot.temp()
```

transect_AlongBay-2020-03-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-03-18T13:42:00.000000000 |        59.518 |       -151.728 | 2020-03-18T10:27:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-03-18'].plot.salt() + cat['transect_AlongBay-2020-03-18'].plot.temp()
```

transect_AlongBay-2020-06-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-06-04T14:17:00.000000000 |          59.5 |       -151.888 | 2020-06-04T09:48:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-06-04'].plot.salt() + cat['transect_AlongBay-2020-06-04'].plot.temp()
```

transect_AlongBay-2020-07-08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-07-08T16:53:00.000000000 |       59.5824 |       -151.385 | 2020-07-08T15:22:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-07-08'].plot.salt() + cat['transect_AlongBay-2020-07-08'].plot.temp()
```

transect_AlongBay-2020-07-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-07-23T15:00:00.000000000 |          59.5 |       -151.888 | 2020-07-23T12:15:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-07-23'].plot.salt() + cat['transect_AlongBay-2020-07-23'].plot.temp()
```

transect_AlongBay-2020-08-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-08-14T13:10:00.000000000 |          59.5 |       -151.888 | 2020-08-14T09:56:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-08-14'].plot.salt() + cat['transect_AlongBay-2020-08-14'].plot.temp()
```

transect_AlongBay-2020-09-20
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-09-20T15:44:00.000000000 |        59.383 |        -152.05 | 2020-09-20T12:24:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-09-20'].plot.salt() + cat['transect_AlongBay-2020-09-20'].plot.temp()
```

transect_AlongBay-2020-10-15
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-10-15T13:59:00.000000000 |          59.5 |       -151.888 | 2020-10-15T11:07:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-10-15'].plot.salt() + cat['transect_AlongBay-2020-10-15'].plot.temp()
```

transect_AlongBay-2020-12-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2020-12-28T14:41:00.000000000 |        59.525 |        -151.65 | 2020-12-28T12:42:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2020-12-28'].plot.salt() + cat['transect_AlongBay-2020-12-28'].plot.temp()
```

transect_AlongBay-2021-01-13
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2021-01-13T13:46:00.000000000 |        59.518 |       -151.728 | 2021-01-13T11:20:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-01-13'].plot.salt() + cat['transect_AlongBay-2021-01-13'].plot.temp()
```

transect_AlongBay-2021-02-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2021-02-16T16:43:00.000000000 |        59.383 |        -152.05 | 2021-02-16T13:51:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-02-16'].plot.salt() + cat['transect_AlongBay-2021-02-16'].plot.temp()
```

transect_AlongBay-2021-03-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2021-03-23T14:41:00.000000000 |        59.518 |       -151.728 | 2021-03-23T11:57:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-03-23'].plot.salt() + cat['transect_AlongBay-2021-03-23'].plot.temp()
```

transect_AlongBay-2021-04-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       59.5824 |       -151.385 | 2021-04-14T22:00:00.000000000 |        59.383 |        -152.05 | 2021-04-14T18:52:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-04-14'].plot.salt() + cat['transect_AlongBay-2021-04-14'].plot.temp()
```

transect_AlongBay-2021-04-16
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2021-04-16T16:11:00.000000000 |        59.518 |       -151.728 | 2021-04-16T14:04:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-04-16'].plot.salt() + cat['transect_AlongBay-2021-04-16'].plot.temp()
```

transect_AlongBay-2021-05-06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-05-06T13:41:00.000000000 |          59.5 |       -151.888 | 2021-05-06T10:19:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-05-06'].plot.salt() + cat['transect_AlongBay-2021-05-06'].plot.temp()
```

transect_AlongBay-2021-06-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-06-21T13:28:00.000000000 |        59.518 |       -151.728 | 2021-06-21T10:23:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-06-21'].plot.salt() + cat['transect_AlongBay-2021-06-21'].plot.temp()
```

transect_AlongBay-2021-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-07-21T16:51:00.000000000 |        59.383 |        -152.05 | 2021-07-21T13:18:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-07-21'].plot.salt() + cat['transect_AlongBay-2021-07-21'].plot.temp()
```

transect_AlongBay-2021-08-17
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-08-17T14:06:00.000000000 |          59.5 |       -151.888 | 2021-08-17T10:30:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-08-17'].plot.salt() + cat['transect_AlongBay-2021-08-17'].plot.temp()
```

transect_AlongBay-2021-10-04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-10-04T14:41:00.000000000 |          59.5 |       -151.888 | 2021-10-04T11:30:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-10-04'].plot.salt() + cat['transect_AlongBay-2021-10-04'].plot.temp()
```

transect_AlongBay-2021-10-05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.445 |           -152 | 2021-10-05T13:04:00.000000000 |        59.383 |        -152.05 | 2021-10-05T12:50:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-10-05'].plot.salt() + cat['transect_AlongBay-2021-10-05'].plot.temp()
```

transect_AlongBay-2021-10-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-10-21T14:31:00.000000000 |        59.518 |       -151.728 | 2021-10-21T10:46:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-10-21'].plot.salt() + cat['transect_AlongBay-2021-10-21'].plot.temp()
```

transect_AlongBay-2021-11-14
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2021-11-14T13:53:00.000000000 |        59.518 |       -151.728 | 2021-11-14T10:32:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-11-14'].plot.salt() + cat['transect_AlongBay-2021-11-14'].plot.temp()
```

transect_AlongBay-2021-12-18
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2021-12-18T13:30:00.000000000 |        59.518 |       -151.728 | 2021-12-18T10:48:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2021-12-18'].plot.salt() + cat['transect_AlongBay-2021-12-18'].plot.temp()
```

transect_AlongBay-2022-01-31
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2022-01-31T13:28:00.000000000 |        59.518 |       -151.728 | 2022-01-31T10:35:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-01-31'].plot.salt() + cat['transect_AlongBay-2022-01-31'].plot.temp()
```

transect_AlongBay-2022-02-28
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2022-02-28T15:23:00.000000000 |        59.383 |        -152.05 | 2022-02-28T12:23:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-02-28'].plot.salt() + cat['transect_AlongBay-2022-02-28'].plot.temp()
```

transect_AlongBay-2022-03-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.687 |       -151.165 | 2022-03-21T16:06:00.000000000 |        59.518 |       -151.728 | 2022-03-21T13:33:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-03-21'].plot.salt() + cat['transect_AlongBay-2022-03-21'].plot.temp()
```

transect_AlongBay-2022-04-12
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2022-04-12T15:13:00.000000000 |        59.383 |        -152.05 | 2022-04-12T11:10:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-04-12'].plot.salt() + cat['transect_AlongBay-2022-04-12'].plot.temp()
```

transect_AlongBay-2022-05-23
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2022-05-23T13:58:00.000000000 |          59.5 |       -151.888 | 2022-05-23T10:34:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-05-23'].plot.salt() + cat['transect_AlongBay-2022-05-23'].plot.temp()
```

transect_AlongBay-2022-06-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2022-06-24T13:41:00.000000000 |          59.5 |       -151.888 | 2022-06-24T10:12:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-06-24'].plot.salt() + cat['transect_AlongBay-2022-06-24'].plot.temp()
```

transect_AlongBay-2022-07-21
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2022-07-21T16:24:00.000000000 |        59.383 |        -152.05 | 2022-07-21T12:25:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-07-21'].plot.salt() + cat['transect_AlongBay-2022-07-21'].plot.temp()
```

transect_AlongBay-2022-08-24
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        59.742 |       -151.057 | 2022-08-24T13:20:00.000000000 |          59.5 |       -151.888 | 2022-08-24T09:46:00.000000000 |


```{code-cell}
cat['transect_AlongBay-2022-08-24'].plot.salt() + cat['transect_AlongBay-2022-08-24'].plot.temp()
```
