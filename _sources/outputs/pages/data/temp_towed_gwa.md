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

# Towed CTD at nominal 7m depth

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
        

```{code-cell}
cat['2011-06-20'].plot.temp()
```

2011-07-23
        

```{code-cell}
cat['2011-07-23'].plot.temp()
```

2011-08-22
        

```{code-cell}
cat['2011-08-22'].plot.temp()
```

## 2012

+++

2012-04-09
        

```{code-cell}
cat['2012-04-09'].plot.temp()
```

2012-05-13
        

```{code-cell}
cat['2012-05-13'].plot.temp()
```

2012-06-11
        

```{code-cell}
cat['2012-06-11'].plot.temp()
```

2012-09-16
        

```{code-cell}
cat['2012-09-16'].plot.temp()
```

2012-10-16
        

```{code-cell}
cat['2012-10-16'].plot.temp()
```

## 2013

+++

2013-04-14
        

```{code-cell}
cat['2013-04-14'].plot.temp()
```

2013-05-13
        

```{code-cell}
cat['2013-05-13'].plot.temp()
```

2013-06-15
        

```{code-cell}
cat['2013-06-15'].plot.temp()
```

2013-07-15
        

```{code-cell}
cat['2013-07-15'].plot.temp()
```

2013-08-17
        

```{code-cell}
cat['2013-08-17'].plot.temp()
```

## 2014

+++

2014-04-27
        

```{code-cell}
cat['2014-04-27'].plot.temp()
```

2014-05-27
        

```{code-cell}
cat['2014-05-27'].plot.temp()
```

2014-06-29
        

```{code-cell}
cat['2014-06-29'].plot.temp()
```

2014-07-29
        

```{code-cell}
cat['2014-07-29'].plot.temp()
```

2014-08-31
        

```{code-cell}
cat['2014-08-31'].plot.temp()
```

## 2015

+++

2015-08-23
        

```{code-cell}
cat['2015-08-23'].plot.temp()
```

2015-09-01
        

```{code-cell}
cat['2015-09-01'].plot.temp()
```

## 2016

+++

2016-04-17
        

```{code-cell}
cat['2016-04-17'].plot.temp()
```

2016-05-16
        

```{code-cell}
cat['2016-05-16'].plot.temp()
```

2016-06-19
        

```{code-cell}
cat['2016-06-19'].plot.temp()
```

2016-07-19
        

```{code-cell}
cat['2016-07-19'].plot.temp()
```

2016-08-29
        

```{code-cell}
cat['2016-08-29'].plot.temp()
```

2016-10-02
        

```{code-cell}
cat['2016-10-02'].plot.temp()
```
