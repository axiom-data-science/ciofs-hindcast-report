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

# Repeat CTD transect from Anchor Point in Cook Inlet

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
        

```{code-cell}
cat['2003-07-01'].plot.salt() + cat['2003-07-01'].plot.temp()
```

2003-07-02
        

```{code-cell}
cat['2003-07-02'].plot.salt() + cat['2003-07-02'].plot.temp()
```

2003-07-04
        

```{code-cell}
cat['2003-07-04'].plot.salt() + cat['2003-07-04'].plot.temp()
```

2003-07-05
        

```{code-cell}
cat['2003-07-05'].plot.salt() + cat['2003-07-05'].plot.temp()
```

2003-07-06
        

```{code-cell}
cat['2003-07-06'].plot.salt() + cat['2003-07-06'].plot.temp()
```

2003-07-07
        

```{code-cell}
cat['2003-07-07'].plot.salt() + cat['2003-07-07'].plot.temp()
```

2003-07-08
        

```{code-cell}
cat['2003-07-08'].plot.salt() + cat['2003-07-08'].plot.temp()
```

2003-07-09
        

```{code-cell}
cat['2003-07-09'].plot.salt() + cat['2003-07-09'].plot.temp()
```

2003-07-10
        

```{code-cell}
cat['2003-07-10'].plot.salt() + cat['2003-07-10'].plot.temp()
```

2003-07-11
        

```{code-cell}
cat['2003-07-11'].plot.salt() + cat['2003-07-11'].plot.temp()
```

2003-07-12
        

```{code-cell}
cat['2003-07-12'].plot.salt() + cat['2003-07-12'].plot.temp()
```

2003-07-13
        

```{code-cell}
cat['2003-07-13'].plot.salt() + cat['2003-07-13'].plot.temp()
```

2003-07-14
        

```{code-cell}
cat['2003-07-14'].plot.salt() + cat['2003-07-14'].plot.temp()
```

2003-07-15
        

```{code-cell}
cat['2003-07-15'].plot.salt() + cat['2003-07-15'].plot.temp()
```

2003-07-16
        

```{code-cell}
cat['2003-07-16'].plot.salt() + cat['2003-07-16'].plot.temp()
```

2003-07-17
        

```{code-cell}
cat['2003-07-17'].plot.salt() + cat['2003-07-17'].plot.temp()
```

2003-07-18
        

```{code-cell}
cat['2003-07-18'].plot.salt() + cat['2003-07-18'].plot.temp()
```

2003-07-19
        

```{code-cell}
cat['2003-07-19'].plot.salt() + cat['2003-07-19'].plot.temp()
```

2003-07-21
        

```{code-cell}
cat['2003-07-21'].plot.salt() + cat['2003-07-21'].plot.temp()
```

2003-07-22
        

```{code-cell}
cat['2003-07-22'].plot.salt() + cat['2003-07-22'].plot.temp()
```

2003-07-23
        

```{code-cell}
cat['2003-07-23'].plot.salt() + cat['2003-07-23'].plot.temp()
```

2003-07-24
        

```{code-cell}
cat['2003-07-24'].plot.salt() + cat['2003-07-24'].plot.temp()
```

2003-07-25
        

```{code-cell}
cat['2003-07-25'].plot.salt() + cat['2003-07-25'].plot.temp()
```

2003-07-26
        

```{code-cell}
cat['2003-07-26'].plot.salt() + cat['2003-07-26'].plot.temp()
```

2003-07-28
        

```{code-cell}
cat['2003-07-28'].plot.salt() + cat['2003-07-28'].plot.temp()
```

2003-07-29
        

```{code-cell}
cat['2003-07-29'].plot.salt() + cat['2003-07-29'].plot.temp()
```

2003-07-30
        

```{code-cell}
cat['2003-07-30'].plot.salt() + cat['2003-07-30'].plot.temp()
```

## 2004

+++

2004-07-01
        

```{code-cell}
cat['2004-07-01'].plot.salt() + cat['2004-07-01'].plot.temp()
```

2004-07-02
        

```{code-cell}
cat['2004-07-02'].plot.salt() + cat['2004-07-02'].plot.temp()
```

2004-07-03
        

```{code-cell}
cat['2004-07-03'].plot.salt() + cat['2004-07-03'].plot.temp()
```

2004-07-04
        

```{code-cell}
cat['2004-07-04'].plot.salt() + cat['2004-07-04'].plot.temp()
```

2004-07-05
        

```{code-cell}
cat['2004-07-05'].plot.salt() + cat['2004-07-05'].plot.temp()
```

2004-07-06
        

```{code-cell}
cat['2004-07-06'].plot.salt() + cat['2004-07-06'].plot.temp()
```

2004-07-07
        

```{code-cell}
cat['2004-07-07'].plot.salt() + cat['2004-07-07'].plot.temp()
```

2004-07-08
        

```{code-cell}
cat['2004-07-08'].plot.salt() + cat['2004-07-08'].plot.temp()
```

2004-07-09
        

```{code-cell}
cat['2004-07-09'].plot.salt() + cat['2004-07-09'].plot.temp()
```

2004-07-10
        

```{code-cell}
cat['2004-07-10'].plot.salt() + cat['2004-07-10'].plot.temp()
```

2004-07-11
        

```{code-cell}
cat['2004-07-11'].plot.salt() + cat['2004-07-11'].plot.temp()
```

2004-07-12
        

```{code-cell}
cat['2004-07-12'].plot.salt() + cat['2004-07-12'].plot.temp()
```

2004-07-13
        

```{code-cell}
cat['2004-07-13'].plot.salt() + cat['2004-07-13'].plot.temp()
```

2004-07-14
        

```{code-cell}
cat['2004-07-14'].plot.salt() + cat['2004-07-14'].plot.temp()
```

2004-07-15
        

```{code-cell}
cat['2004-07-15'].plot.salt() + cat['2004-07-15'].plot.temp()
```

2004-07-16
        

```{code-cell}
cat['2004-07-16'].plot.salt() + cat['2004-07-16'].plot.temp()
```

2004-07-17
        

```{code-cell}
cat['2004-07-17'].plot.salt() + cat['2004-07-17'].plot.temp()
```

2004-07-18
        

```{code-cell}
cat['2004-07-18'].plot.salt() + cat['2004-07-18'].plot.temp()
```

2004-07-19
        

```{code-cell}
cat['2004-07-19'].plot.salt() + cat['2004-07-19'].plot.temp()
```

2004-07-20
        

```{code-cell}
cat['2004-07-20'].plot.salt() + cat['2004-07-20'].plot.temp()
```

2004-07-21
        

```{code-cell}
cat['2004-07-21'].plot.salt() + cat['2004-07-21'].plot.temp()
```

2004-07-22
        

```{code-cell}
cat['2004-07-22'].plot.salt() + cat['2004-07-22'].plot.temp()
```

2004-07-23
        

```{code-cell}
cat['2004-07-23'].plot.salt() + cat['2004-07-23'].plot.temp()
```

2004-07-24
        

```{code-cell}
cat['2004-07-24'].plot.salt() + cat['2004-07-24'].plot.temp()
```

2004-07-25
        

```{code-cell}
cat['2004-07-25'].plot.salt() + cat['2004-07-25'].plot.temp()
```

2004-07-27
        

```{code-cell}
cat['2004-07-27'].plot.salt() + cat['2004-07-27'].plot.temp()
```

2004-07-28
        

```{code-cell}
cat['2004-07-28'].plot.salt() + cat['2004-07-28'].plot.temp()
```

2004-07-29
        

```{code-cell}
cat['2004-07-29'].plot.salt() + cat['2004-07-29'].plot.temp()
```

2004-07-30
        

```{code-cell}
cat['2004-07-30'].plot.salt() + cat['2004-07-30'].plot.temp()
```

## 2005

+++

2005-07-01
        

```{code-cell}
cat['2005-07-01'].plot.salt() + cat['2005-07-01'].plot.temp()
```

2005-07-02
        

```{code-cell}
cat['2005-07-02'].plot.salt() + cat['2005-07-02'].plot.temp()
```

2005-07-03
        

```{code-cell}
cat['2005-07-03'].plot.salt() + cat['2005-07-03'].plot.temp()
```

2005-07-04
        

```{code-cell}
cat['2005-07-04'].plot.salt() + cat['2005-07-04'].plot.temp()
```

2005-07-05
        

```{code-cell}
cat['2005-07-05'].plot.salt() + cat['2005-07-05'].plot.temp()
```

2005-07-06
        

```{code-cell}
cat['2005-07-06'].plot.salt() + cat['2005-07-06'].plot.temp()
```

2005-07-07
        

```{code-cell}
cat['2005-07-07'].plot.salt() + cat['2005-07-07'].plot.temp()
```

2005-07-08
        

```{code-cell}
cat['2005-07-08'].plot.salt() + cat['2005-07-08'].plot.temp()
```

2005-07-09
        

```{code-cell}
cat['2005-07-09'].plot.salt() + cat['2005-07-09'].plot.temp()
```

2005-07-10
        

```{code-cell}
cat['2005-07-10'].plot.salt() + cat['2005-07-10'].plot.temp()
```

2005-07-11
        

```{code-cell}
cat['2005-07-11'].plot.salt() + cat['2005-07-11'].plot.temp()
```

2005-07-12
        

```{code-cell}
cat['2005-07-12'].plot.salt() + cat['2005-07-12'].plot.temp()
```

2005-07-13
        

```{code-cell}
cat['2005-07-13'].plot.salt() + cat['2005-07-13'].plot.temp()
```

2005-07-14
        

```{code-cell}
cat['2005-07-14'].plot.salt() + cat['2005-07-14'].plot.temp()
```

2005-07-15
        

```{code-cell}
cat['2005-07-15'].plot.salt() + cat['2005-07-15'].plot.temp()
```

2005-07-16
        

```{code-cell}
cat['2005-07-16'].plot.salt() + cat['2005-07-16'].plot.temp()
```

2005-07-17
        

```{code-cell}
cat['2005-07-17'].plot.salt() + cat['2005-07-17'].plot.temp()
```

2005-07-18
        

```{code-cell}
cat['2005-07-18'].plot.salt() + cat['2005-07-18'].plot.temp()
```

2005-07-19
        

```{code-cell}
cat['2005-07-19'].plot.salt() + cat['2005-07-19'].plot.temp()
```

2005-07-20
        

```{code-cell}
cat['2005-07-20'].plot.salt() + cat['2005-07-20'].plot.temp()
```

2005-07-21
        

```{code-cell}
cat['2005-07-21'].plot.salt() + cat['2005-07-21'].plot.temp()
```

2005-07-22
        

```{code-cell}
cat['2005-07-22'].plot.salt() + cat['2005-07-22'].plot.temp()
```

2005-07-23
        

```{code-cell}
cat['2005-07-23'].plot.salt() + cat['2005-07-23'].plot.temp()
```

2005-07-24
        

```{code-cell}
cat['2005-07-24'].plot.salt() + cat['2005-07-24'].plot.temp()
```

2005-07-25
        

```{code-cell}
cat['2005-07-25'].plot.salt() + cat['2005-07-25'].plot.temp()
```

2005-07-26
        

```{code-cell}
cat['2005-07-26'].plot.salt() + cat['2005-07-26'].plot.temp()
```

2005-07-27
        

```{code-cell}
cat['2005-07-27'].plot.salt() + cat['2005-07-27'].plot.temp()
```

2005-07-28
        

```{code-cell}
cat['2005-07-28'].plot.salt() + cat['2005-07-28'].plot.temp()
```

2005-07-29
        

```{code-cell}
cat['2005-07-29'].plot.salt() + cat['2005-07-29'].plot.temp()
```

2005-07-30
        

```{code-cell}
cat['2005-07-30'].plot.salt() + cat['2005-07-30'].plot.temp()
```

## 2006

+++

2006-07-01
        

```{code-cell}
cat['2006-07-01'].plot.salt() + cat['2006-07-01'].plot.temp()
```

2006-07-02
        

```{code-cell}
cat['2006-07-02'].plot.salt() + cat['2006-07-02'].plot.temp()
```

2006-07-03
        

```{code-cell}
cat['2006-07-03'].plot.salt() + cat['2006-07-03'].plot.temp()
```

2006-07-04
        

```{code-cell}
cat['2006-07-04'].plot.salt() + cat['2006-07-04'].plot.temp()
```

2006-07-05
        

```{code-cell}
cat['2006-07-05'].plot.salt() + cat['2006-07-05'].plot.temp()
```

2006-07-06
        

```{code-cell}
cat['2006-07-06'].plot.salt() + cat['2006-07-06'].plot.temp()
```

2006-07-07
        

```{code-cell}
cat['2006-07-07'].plot.salt() + cat['2006-07-07'].plot.temp()
```

2006-07-09
        

```{code-cell}
cat['2006-07-09'].plot.salt() + cat['2006-07-09'].plot.temp()
```

2006-07-10
        

```{code-cell}
cat['2006-07-10'].plot.salt() + cat['2006-07-10'].plot.temp()
```

2006-07-11
        

```{code-cell}
cat['2006-07-11'].plot.salt() + cat['2006-07-11'].plot.temp()
```

2006-07-12
        

```{code-cell}
cat['2006-07-12'].plot.salt() + cat['2006-07-12'].plot.temp()
```

2006-07-13
        

```{code-cell}
cat['2006-07-13'].plot.salt() + cat['2006-07-13'].plot.temp()
```

2006-07-15
        

```{code-cell}
cat['2006-07-15'].plot.salt() + cat['2006-07-15'].plot.temp()
```

2006-07-16
        

```{code-cell}
cat['2006-07-16'].plot.salt() + cat['2006-07-16'].plot.temp()
```

2006-07-17
        

```{code-cell}
cat['2006-07-17'].plot.salt() + cat['2006-07-17'].plot.temp()
```

2006-07-18
        

```{code-cell}
cat['2006-07-18'].plot.salt() + cat['2006-07-18'].plot.temp()
```

2006-07-19
        

```{code-cell}
cat['2006-07-19'].plot.salt() + cat['2006-07-19'].plot.temp()
```

2006-07-21
        

```{code-cell}
cat['2006-07-21'].plot.salt() + cat['2006-07-21'].plot.temp()
```

2006-07-23
        

```{code-cell}
cat['2006-07-23'].plot.salt() + cat['2006-07-23'].plot.temp()
```

2006-07-25
        

```{code-cell}
cat['2006-07-25'].plot.salt() + cat['2006-07-25'].plot.temp()
```

2006-07-26
        

```{code-cell}
cat['2006-07-26'].plot.salt() + cat['2006-07-26'].plot.temp()
```

2006-07-27
        

```{code-cell}
cat['2006-07-27'].plot.salt() + cat['2006-07-27'].plot.temp()
```

2006-07-28
        

```{code-cell}
cat['2006-07-28'].plot.salt() + cat['2006-07-28'].plot.temp()
```
