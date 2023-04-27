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

# NOAA: Single CTD profiles across Cook Inlet

* CTD profiles 2005 - NOAA
* ctd_profiles_2005_noaa
* One-off CTD profiles in June and July 2005

CTD Profiles from NOAA.




    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_2005_noaa"))
```

## Map of CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_2005_noaa")("ctd_profiles_2005_noaa")
    
```

## 501
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |        60.722 |       -151.647 | 2005-06-16T15:34:00.000000000 |        60.722 |       -151.647 | 2005-06-16T15:34:00.000000000 |


```{code-cell}
cat['501'].plot.data()
```

## 502
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.7207 |       -151.557 | 2005-06-16T15:08:00.000000000 |       60.7207 |       -151.557 | 2005-06-16T15:08:00.000000000 |


```{code-cell}
cat['502'].plot.data()
```

## 503
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.7173 |       -151.433 | 2005-06-16T14:34:00.000000000 |       60.7173 |       -151.433 | 2005-06-16T14:34:00.000000000 |


```{code-cell}
cat['503'].plot.data()
```

## 504
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.6834 |       -151.418 | 2005-06-16T14:01:00.000000000 |       60.6834 |       -151.418 | 2005-06-16T14:01:00.000000000 |


```{code-cell}
cat['504'].plot.data()
```

## 505
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.5967 |       -151.739 | 2005-06-16T16:33:00.000000000 |       60.5967 |       -151.739 | 2005-06-16T16:33:00.000000000 |


```{code-cell}
cat['505'].plot.data()
```

## 506
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.5871 |       -151.445 | 2005-06-16T12:47:00.000000000 |       60.5871 |       -151.445 | 2005-06-16T12:47:00.000000000 |


```{code-cell}
cat['506'].plot.data()
```

## 507
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.5517 |       -152.128 | 2005-06-16T18:14:00.000000000 |       60.5517 |       -152.128 | 2005-06-16T18:14:00.000000000 |


```{code-cell}
cat['507'].plot.data()
```

## 508
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |        60.483 |       -151.673 | 2005-06-16T11:07:00.000000000 |        60.483 |       -151.673 | 2005-06-16T11:07:00.000000000 |


```{code-cell}
cat['508'].plot.data()
```

## 509
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.3792 |       -152.182 | 2005-06-16T20:07:00.000000000 |       60.3792 |       -152.182 | 2005-06-16T20:07:00.000000000 |


```{code-cell}
cat['509'].plot.data()
```

## 510
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |        60.248 |       -151.755 | 2005-06-16T09:05:00.000000000 |        60.248 |       -151.755 | 2005-06-16T09:05:00.000000000 |


```{code-cell}
cat['510'].plot.data()
```

## 511
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       60.0233 |        -152.12 | 2005-07-28T20:04:00.000000000 |       60.0233 |        -152.12 | 2005-07-28T20:04:00.000000000 |


```{code-cell}
cat['511'].plot.data()
```

## 512
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.5661 |       -153.422 | 2005-07-29T05:12:00.000000000 |       59.5661 |       -153.422 | 2005-07-29T05:12:00.000000000 |


```{code-cell}
cat['512'].plot.data()
```

## 513
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.4828 |       -151.755 | 2005-07-30T23:40:00.000000000 |       59.4828 |       -151.755 | 2005-07-30T23:40:00.000000000 |


```{code-cell}
cat['513'].plot.data()
```

## 514
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.3018 |        -152.92 | 2005-07-29T10:51:00.000000000 |       59.3018 |        -152.92 | 2005-07-29T10:51:00.000000000 |


```{code-cell}
cat['514'].plot.data()
```

## 515
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.3149 |       -152.365 | 2005-07-30T19:51:00.000000000 |       59.3149 |       -152.365 | 2005-07-30T19:51:00.000000000 |


```{code-cell}
cat['515'].plot.data()
```

## 516
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.4001 |       -151.966 | 2005-07-30T22:32:00.000000000 |       59.4001 |       -151.966 | 2005-07-30T22:32:00.000000000 |


```{code-cell}
cat['516'].plot.data()
```

## 517
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       58.8901 |       -153.184 | 2005-07-29T14:36:00.000000000 |       58.8901 |       -153.184 | 2005-07-29T14:36:00.000000000 |


```{code-cell}
cat['517'].plot.data()
```

## 518
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       58.9305 |       -152.728 | 2005-07-30T09:24:00.000000000 |       58.9305 |       -152.728 | 2005-07-30T09:24:00.000000000 |


```{code-cell}
cat['518'].plot.data()
```

## 519
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |        58.808 |       -152.408 | 2005-07-30T04:08:00.000000000 |        58.808 |       -152.408 | 2005-07-30T04:08:00.000000000 |


```{code-cell}
cat['519'].plot.data()
```

## 520
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.0492 |       -152.152 | 2005-07-30T11:51:00.000000000 |       59.0492 |       -152.152 | 2005-07-30T11:51:00.000000000 |


```{code-cell}
cat['520'].plot.data()
```

## 521
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.1207 |       -151.895 | 2005-07-30T17:33:00.000000000 |       59.1207 |       -151.895 | 2005-07-30T17:33:00.000000000 |


```{code-cell}
cat['521'].plot.data()
```

## 522
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.2112 |       -151.787 | 2005-07-30T15:36:00.000000000 |       59.2112 |       -151.787 | 2005-07-30T15:36:00.000000000 |


```{code-cell}
cat['522'].plot.data()
```

## 523
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.0129 |       -151.775 | 2005-07-30T16:03:00.000000000 |       59.0129 |       -151.775 | 2005-07-30T16:03:00.000000000 |


```{code-cell}
cat['523'].plot.data()
```

## 524
        

+++

            
|    | featuretype   | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:--------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | profile       | point     |       59.1339 |       -151.706 | 2005-07-30T16:51:00.000000000 |       59.1339 |       -151.706 | 2005-07-30T16:51:00.000000000 |


```{code-cell}
cat['524'].plot.data()
```