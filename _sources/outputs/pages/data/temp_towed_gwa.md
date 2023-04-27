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

# GWA: Towed CTD at nominal 7m depth, temperature only

* Temperature towed 2011-2016 - GWA
* temp_towed_gwa
* Approximately monthly in summer from 2011 to 2016, 5min sampling frequency

Temperature only: Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska.

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2011-2016.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Converted some local times, ship track outside domain is not included.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("temp_towed_gwa"))
```

## Map of Flow through on Ship of Opportunity
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "temp_towed_gwa")("temp_towed_gwa")
    
```

## 2011

+++

2011-06-20
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |       59.2073 |       -150.532 | 2011-06-20T17:40:00.000000000 |       58.8066 |       -152.133 | 2011-06-20T14:50:00.000000000 |


```{code-cell}
cat['2011-06-20'].plot.temp()
```

2011-07-23
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |       59.0286 |       -150.526 | 2011-07-23T18:00:00.000000000 |       58.8215 |       -151.448 | 2011-07-23T16:25:00.000000000 |


```{code-cell}
cat['2011-07-23'].plot.temp()
```

2011-08-22
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |       59.1542 |         -150.5 | 2011-08-22T18:05:00.000000000 |       58.8112 |       -152.048 | 2011-08-22T15:20:00.000000000 |


```{code-cell}
cat['2011-08-22'].plot.temp()
```

## 2012

+++

2012-04-09
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         60.58 |        -150.52 | 2012-04-10T02:05:00.000000000 |         58.82 |        -152.13 | 2012-04-09T19:30:00.000000000 |


```{code-cell}
cat['2012-04-09'].plot.temp()
```

2012-05-13
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.41 |        -150.52 | 2012-05-13T03:30:00.000000000 |         58.82 |        -152.14 | 2012-05-13T00:15:00.000000000 |


```{code-cell}
cat['2012-05-13'].plot.temp()
```

2012-06-11
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.34 |        -150.51 | 2012-06-12T03:10:00.000000000 |         58.81 |        -152.13 | 2012-06-11T23:55:00.000000000 |


```{code-cell}
cat['2012-06-11'].plot.temp()
```

2012-09-16
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.54 |        -150.52 | 2012-09-16T05:15:00.000000000 |         58.82 |        -152.13 | 2012-09-16T00:25:00.000000000 |


```{code-cell}
cat['2012-09-16'].plot.temp()
```

2012-10-16
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |          60.5 |        -150.51 | 2012-10-16T09:45:00.000000000 |         58.81 |        -152.13 | 2012-10-16T01:50:00.000000000 |


```{code-cell}
cat['2012-10-16'].plot.temp()
```

## 2013

+++

2013-04-14
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         60.51 |        -150.53 | 2013-04-14T11:00:00.000000000 |         58.81 |        -152.13 | 2013-04-14T03:05:00.000000000 |


```{code-cell}
cat['2013-04-14'].plot.temp()
```

2013-05-13
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.73 |         -150.5 | 2013-05-14T02:15:00.000000000 |         58.81 |        -152.13 | 2013-05-13T21:35:00.000000000 |


```{code-cell}
cat['2013-05-13'].plot.temp()
```

2013-06-15
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.47 |        -150.52 | 2013-06-16T02:00:00.000000000 |         58.81 |        -152.13 | 2013-06-15T22:15:00.000000000 |


```{code-cell}
cat['2013-06-15'].plot.temp()
```

2013-07-15
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |          59.2 |        -150.51 | 2013-07-16T02:40:00.000000000 |         58.82 |         -152.1 | 2013-07-15T23:55:00.000000000 |


```{code-cell}
cat['2013-07-15'].plot.temp()
```

2013-08-17
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.43 |         -150.5 | 2013-08-18T02:30:00.000000000 |          58.8 |        -152.13 | 2013-08-17T22:35:00.000000000 |


```{code-cell}
cat['2013-08-17'].plot.temp()
```

## 2014

+++

2014-04-27
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.22 |        -150.53 | 2014-04-27T04:20:00.000000000 |         58.82 |        -152.13 | 2014-04-27T01:00:00.000000000 |


```{code-cell}
cat['2014-04-27'].plot.temp()
```

2014-05-27
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.11 |        -150.51 | 2014-05-27T03:55:00.000000000 |          58.8 |        -151.99 | 2014-05-27T01:10:00.000000000 |


```{code-cell}
cat['2014-05-27'].plot.temp()
```

2014-06-29
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.01 |        -150.51 | 2014-06-29T04:45:00.000000000 |         58.77 |        -151.66 | 2014-06-29T02:35:00.000000000 |


```{code-cell}
cat['2014-06-29'].plot.temp()
```

2014-07-29
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.52 |        -150.52 | 2014-07-29T05:00:00.000000000 |         58.81 |        -152.28 | 2014-07-29T00:35:00.000000000 |


```{code-cell}
cat['2014-07-29'].plot.temp()
```

2014-08-31
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.05 |        -150.51 | 2014-08-31T03:50:00.000000000 |         58.82 |        -151.82 | 2014-08-31T01:40:00.000000000 |


```{code-cell}
cat['2014-08-31'].plot.temp()
```

## 2015

+++

2015-08-23
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.56 |         -150.5 | 2015-08-23T14:35:00.000000000 |         58.78 |        -152.13 | 2015-08-23T10:05:00.000000000 |


```{code-cell}
cat['2015-08-23'].plot.temp()
```

2015-09-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         60.53 |         -150.5 | 2015-09-01T16:10:00.000000000 |         58.66 |        -152.13 | 2015-09-01T08:05:00.000000000 |


```{code-cell}
cat['2015-09-01'].plot.temp()
```

## 2016

+++

2016-04-17
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.34 |        -150.53 | 2016-04-17T03:35:00.000000000 |         58.82 |        -152.16 | 2016-04-17T00:15:00.000000000 |


```{code-cell}
cat['2016-04-17'].plot.temp()
```

2016-05-16
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.39 |         -150.5 | 2016-05-17T03:30:00.000000000 |         58.79 |        -152.18 | 2016-05-16T23:15:00.000000000 |


```{code-cell}
cat['2016-05-16'].plot.temp()
```

2016-06-19
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.23 |         -150.5 | 2016-06-19T03:35:00.000000000 |         58.78 |        -152.15 | 2016-06-19T00:10:00.000000000 |


```{code-cell}
cat['2016-06-19'].plot.temp()
```

2016-07-19
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.07 |        -150.51 | 2016-07-19T03:50:00.000000000 |          58.8 |         -151.9 | 2016-07-19T01:05:00.000000000 |


```{code-cell}
cat['2016-07-19'].plot.temp()
```

2016-08-29
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.22 |        -150.52 | 2016-08-30T03:20:00.000000000 |         58.81 |        -152.14 | 2016-08-29T23:45:00.000000000 |


```{code-cell}
cat['2016-08-29'].plot.temp()
```

2016-10-02
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.15 |         -150.5 | 2016-10-02T04:55:00.000000000 |         58.81 |        -152.03 | 2016-10-02T01:55:00.000000000 |


```{code-cell}
cat['2016-10-02'].plot.temp()
```
