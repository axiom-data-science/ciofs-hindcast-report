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

(page:ctd_profiles_uaf)=
# CTD Transects (UAF): Repeated in central Cook Inlet

* CTD time series UAF
* ctd_profiles_uaf
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

```{dropdown} Dataset metadata

|    | Dataset     | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                         |
|---:|:------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:----------------------------------------------------------------|
|  0 | Transect_01 | trajectoryProfile | ['temp', 'salt'] |       60.4837 |       -151.3   | 2003-08-09 23:03:00 |       60.4815 |       -151.8   | 2003-08-09 20:36:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  1 | Transect_02 | trajectoryProfile | ['temp', 'salt'] |       60.4843 |       -151.301 | 2003-08-10 01:25:00 |       60.4816 |       -151.765 | 2003-08-09 23:12:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  2 | Transect_03 | trajectoryProfile | ['temp', 'salt'] |       60.4842 |       -151.336 | 2003-08-10 04:06:00 |       60.4827 |       -151.8   | 2003-08-10 01:35:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  3 | Transect_04 | trajectoryProfile | ['temp', 'salt'] |       60.4858 |       -151.3   | 2003-08-10 07:06:00 |       60.4823 |       -151.766 | 2003-08-10 04:14:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  4 | Transect_05 | trajectoryProfile | ['temp', 'salt'] |       60.4836 |       -151.334 | 2003-08-10 10:02:00 |       60.4827 |       -151.799 | 2003-08-10 07:16:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  5 | Transect_06 | trajectoryProfile | ['temp', 'salt'] |       60.4833 |       -151.3   | 2003-08-10 12:37:00 |       60.4825 |       -151.766 | 2003-08-10 10:11:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  6 | Transect_07 | trajectoryProfile | ['temp', 'salt'] |       60.4842 |       -151.3   | 2003-08-10 16:58:00 |       60.4823 |       -151.8   | 2003-08-10 14:01:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  7 | Transect_08 | trajectoryProfile | ['temp', 'salt'] |       60.4845 |       -151.3   | 2003-08-10 20:17:00 |       60.482  |       -151.767 | 2003-08-10 17:09:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |
|  8 | Transect_09 | trajectoryProfile | ['temp', 'salt'] |       60.484  |       -151.317 | 2003-08-10 22:59:00 |       60.4827 |       -151.8   | 2003-08-10 20:26:00 | https://researchworkspace.com/files/42202256/TS%20downcasts.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_uaf"))
```

## Map of Transect of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_uaf")("ctd_profiles_uaf")
```

## Transect_01
        

```{code-cell}
:tags: [remove-input]

cat['Transect_01'].plot.salt() + cat['Transect_01'].plot.temp()
```

## Transect_02
        

```{code-cell}
:tags: [remove-input]

cat['Transect_02'].plot.salt() + cat['Transect_02'].plot.temp()
```

## Transect_03
        

```{code-cell}
:tags: [remove-input]

cat['Transect_03'].plot.salt() + cat['Transect_03'].plot.temp()
```

## Transect_04
        

```{code-cell}
:tags: [remove-input]

cat['Transect_04'].plot.salt() + cat['Transect_04'].plot.temp()
```

## Transect_05
        

```{code-cell}
:tags: [remove-input]

cat['Transect_05'].plot.salt() + cat['Transect_05'].plot.temp()
```

## Transect_06
        

```{code-cell}
:tags: [remove-input]

cat['Transect_06'].plot.salt() + cat['Transect_06'].plot.temp()
```

## Transect_07
        

```{code-cell}
:tags: [remove-input]

cat['Transect_07'].plot.salt() + cat['Transect_07'].plot.temp()
```

## Transect_08
        

```{code-cell}
:tags: [remove-input]

cat['Transect_08'].plot.salt() + cat['Transect_08'].plot.temp()
```

## Transect_09
        

```{code-cell}
:tags: [remove-input]

cat['Transect_09'].plot.salt() + cat['Transect_09'].plot.temp()
```
