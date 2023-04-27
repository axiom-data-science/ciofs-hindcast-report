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

# GWA: Towed CTD at nominal 7m depth

* CTD Towed 2017-2019 - GWA
* ctd_towed_gwa
* Approximately monthly in summer from 2017 to 2020, 5min sampling frequency

Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2017-2020. 2017 and 2018 have salinity and temperature, 2019 and 2020 have only temperature.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Made all longitudes negative west values, converted some local times, 2019 and 2020 only have temperature, ship track outside domain is not included, resampled from 2min to 5min.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_gwa"))
```

## Map of Flow through on Ship of Opportunity
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_gwa")("ctd_towed_gwa")
    
```

## 2017

+++

2017-04-29
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.355 |        -150.52 | 2017-04-30T03:30:00.000000000 |        58.795 |        -152.08 | 2017-04-29T23:35:00.000000000 |


```{code-cell}
cat['2017-04-29'].plot.salt() + cat['2017-04-29'].plot.temp()
```

2017-05-30
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |       59.3067 |       -150.503 | 2017-05-30T03:40:00.000000000 |         58.79 |        -152.08 | 2017-05-30T00:00:00.000000000 |


```{code-cell}
cat['2017-05-30'].plot.salt() + cat['2017-05-30'].plot.temp()
```

2017-08-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.02 |        -150.52 | 2017-08-01T03:20:00.000000000 |         58.81 |        -151.38 | 2017-08-01T01:35:00.000000000 |


```{code-cell}
cat['2017-08-01'].plot.salt() + cat['2017-08-01'].plot.temp()
```

2017-09-03
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.035 |        -150.52 | 2017-09-03T04:35:00.000000000 |          58.8 |       -151.555 | 2017-09-03T02:25:00.000000000 |


```{code-cell}
cat['2017-09-03'].plot.salt() + cat['2017-09-03'].plot.temp()
```

2017-10-03
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.165 |        -150.58 | 2017-10-03T03:25:00.000000000 |       58.8133 |        -152.08 | 2017-10-03T00:20:00.000000000 |


```{code-cell}
cat['2017-10-03'].plot.salt() + cat['2017-10-03'].plot.temp()
```

2017-10-24
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.115 |       -150.525 | 2017-10-24T04:10:00.000000000 |         58.81 |       -151.825 | 2017-10-24T01:35:00.000000000 |


```{code-cell}
cat['2017-10-24'].plot.salt() + cat['2017-10-24'].plot.temp()
```

## 2018

+++

2018-04-17
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.165 |       -150.525 | 2018-04-17T11:35:00.000000000 |        58.815 |        -152.12 | 2018-04-17T08:15:00.000000000 |


```{code-cell}
cat['2018-04-17'].plot.salt() + cat['2018-04-17'].plot.temp()
```

2018-05-19
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.11 |       -150.505 | 2018-05-19T19:00:00.000000000 |       58.8167 |         -151.7 | 2018-05-19T15:25:00.000000000 |


```{code-cell}
cat['2018-05-19'].plot.salt() + cat['2018-05-19'].plot.temp()
```

2018-06-18
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.965 |        -150.53 | 2018-06-18T19:20:00.000000000 |        58.805 |        -152.13 | 2018-06-18T14:25:00.000000000 |


```{code-cell}
cat['2018-06-18'].plot.salt() + cat['2018-06-18'].plot.temp()
```

2018-07-21
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |        59.475 |       -150.525 | 2018-07-21T21:00:00.000000000 |        58.805 |        -152.08 | 2018-07-21T17:05:00.000000000 |


```{code-cell}
cat['2018-07-21'].plot.salt() + cat['2018-07-21'].plot.temp()
```

## 2019

+++

2019-04-11
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.38 |        -123.69 | 2019-04-30T23:55:00.000000000 |         48.27 |        -152.13 | 2019-04-11T05:45:00.000000000 |


```{code-cell}
cat['2019-04-11'].plot.temp()
```

2019-05-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         58.94 |        -141.32 | 2019-05-31T23:55:00.000000000 |         55.84 |        -151.01 | 2019-05-01T00:00:00.000000000 |


```{code-cell}
cat['2019-05-01'].plot.temp()
```

2019-08-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.37 |        -124.96 | 2019-08-31T23:55:00.000000000 |         48.52 |        -152.17 | 2019-08-01T00:00:00.000000000 |


```{code-cell}
cat['2019-08-01'].plot.temp()
```

2019-09-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.34 |        -127.24 | 2019-09-16T23:00:00.000000000 |         49.53 |        -152.12 | 2019-09-01T00:00:00.000000000 |


```{code-cell}
cat['2019-09-01'].plot.temp()
```

## 2020

+++

2020-07-07
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         59.42 |       -150.512 | 2020-07-31T23:55:00.000000000 |         58.79 |       -152.153 | 2020-07-07T01:25:00.000000000 |


```{code-cell}
cat['2020-07-07'].plot.temp()
```

2020-08-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |          59.4 |       -150.513 | 2020-08-31T23:55:00.000000000 |         58.79 |       -152.133 | 2020-08-01T00:00:00.000000000 |


```{code-cell}
cat['2020-08-01'].plot.temp()
```

2020-09-01
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectory    | point     |         60.52 |       -150.516 | 2020-09-08T23:05:00.000000000 |         58.77 |         -152.2 | 2020-09-01T00:00:00.000000000 |


```{code-cell}
cat['2020-09-01'].plot.temp()
```