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

# Repeat CTD profile transect along an east-west section in central Cook Inlet

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
        

```{code-cell}
cat['Transect_01'].plot.salt() + cat['Transect_01'].plot.temp()
```

## Transect_02
        

```{code-cell}
cat['Transect_02'].plot.salt() + cat['Transect_02'].plot.temp()
```

## Transect_03
        

```{code-cell}
cat['Transect_03'].plot.salt() + cat['Transect_03'].plot.temp()
```

## Transect_04
        

```{code-cell}
cat['Transect_04'].plot.salt() + cat['Transect_04'].plot.temp()
```

## Transect_05
        

```{code-cell}
cat['Transect_05'].plot.salt() + cat['Transect_05'].plot.temp()
```

## Transect_06
        

```{code-cell}
cat['Transect_06'].plot.salt() + cat['Transect_06'].plot.temp()
```

## Transect_07
        

```{code-cell}
cat['Transect_07'].plot.salt() + cat['Transect_07'].plot.temp()
```

## Transect_08
        

```{code-cell}
cat['Transect_08'].plot.salt() + cat['Transect_08'].plot.temp()
```

## Transect_09
        

```{code-cell}
cat['Transect_09'].plot.salt() + cat['Transect_09'].plot.temp()
```
