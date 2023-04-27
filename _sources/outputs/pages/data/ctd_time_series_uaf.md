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

# UAF: Repeat CTD profile transect along an east-west section in central Cook Inlet

* CTD time series UAF
* ctd_time_series_uaf
* 26-hour period on 9-10 August 2003

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles

Surface-to-bottom measurements of temperature, salinity, and transmissivity, as well as measurements of surface currents (vessel drift speeds) were acquired along an east-west section in central Cook Inlet, Alaska during a 26-hour period on 9-10 August 2003. These measurements are used to describe the evolution of frontal features (tide rips) and physical properties along this section during semidiurnal and diurnal tidal cycles. The observation that the amplitude of surface currents is a function of water depth is used to show that strong frontal features occur in association with steep bathymetry. The positions and strengths of these fronts vary with the semidiurnal tide. The presence of freshwater gradients alters the phase and duration of tidal currents across the section. Where mean density-driven flow is northward (along the eastern shore and near Kalgin Island), the onset of northward tidal flow (flood tide) occurs earlier and has longer duration than the onset and duration of northward tidal flow where mean density-driven flow is southward (in the shipping channel). Conversely, where mean density-driven flow is southward (in the shipping channel), the onset of southward tidal flow (ebb tide) occurs earlier and has longer duration than the onset and duration of southward tidal flow along the eastern shore and near Kalgin Island. 

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles
Stephen R. Okkonen
Institute of Marine Science
University of Alaska Fairbanks
Report: https://www.circac.org/wp-content/uploads/Okkonen_2005_hydrography-and-currents-in-Cook-Inlet.pdf


Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_time_series_uaf"))
```

## Map of Transect of CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_time_series_uaf")("ctd_time_series_uaf")
    
```

## Transect_01
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4837 |         -151.3 | 2003-08-09T23:03:00.000000000 |       60.4815 |         -151.8 | 2003-08-09T20:36:00.000000000 |


```{code-cell}
cat['Transect_01'].plot.salt() + cat['Transect_01'].plot.temp()
```

## Transect_02
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4843 |       -151.301 | 2003-08-10T01:25:00.000000000 |       60.4816 |       -151.765 | 2003-08-09T23:12:00.000000000 |


```{code-cell}
cat['Transect_02'].plot.salt() + cat['Transect_02'].plot.temp()
```

## Transect_03
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4842 |       -151.336 | 2003-08-10T04:06:00.000000000 |       60.4827 |         -151.8 | 2003-08-10T01:35:00.000000000 |


```{code-cell}
cat['Transect_03'].plot.salt() + cat['Transect_03'].plot.temp()
```

## Transect_04
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4858 |         -151.3 | 2003-08-10T07:06:00.000000000 |       60.4823 |       -151.766 | 2003-08-10T04:14:00.000000000 |


```{code-cell}
cat['Transect_04'].plot.salt() + cat['Transect_04'].plot.temp()
```

## Transect_05
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4836 |       -151.334 | 2003-08-10T10:02:00.000000000 |       60.4827 |       -151.799 | 2003-08-10T07:16:00.000000000 |


```{code-cell}
cat['Transect_05'].plot.salt() + cat['Transect_05'].plot.temp()
```

## Transect_06
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4833 |         -151.3 | 2003-08-10T12:37:00.000000000 |       60.4825 |       -151.766 | 2003-08-10T10:11:00.000000000 |


```{code-cell}
cat['Transect_06'].plot.salt() + cat['Transect_06'].plot.temp()
```

## Transect_07
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4842 |         -151.3 | 2003-08-10T16:58:00.000000000 |       60.4823 |         -151.8 | 2003-08-10T14:01:00.000000000 |


```{code-cell}
cat['Transect_07'].plot.salt() + cat['Transect_07'].plot.temp()
```

## Transect_08
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |       60.4845 |         -151.3 | 2003-08-10T20:17:00.000000000 |        60.482 |       -151.767 | 2003-08-10T17:09:00.000000000 |


```{code-cell}
cat['Transect_08'].plot.salt() + cat['Transect_08'].plot.temp()
```

## Transect_09
        

+++

            
|    | featuretype       | maptype   |   maxLatitude |   maxLongitude | maxTime                       |   minLatitude |   minLongitude | minTime                       |
|---:|:------------------|:----------|--------------:|---------------:|:------------------------------|--------------:|---------------:|:------------------------------|
|  0 | trajectoryProfile | line      |        60.484 |       -151.317 | 2003-08-10T22:59:00.000000000 |       60.4827 |         -151.8 | 2003-08-10T20:26:00.000000000 |


```{code-cell}
cat['Transect_09'].plot.salt() + cat['Transect_09'].plot.temp()
```
