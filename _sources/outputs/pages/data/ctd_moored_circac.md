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
import cmocean.cm as cmo
```

# CIRCAC: Central Cook Inlet Mooring

* CTD Moored 2006 - CIRCAC
* ctd_moored_circac
* Two weeks in August 2006, 15 min sampling

Central Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

CIRCAC is the Cook Inlet Regional Citizens Advisory Council. It was funded by MMS (pre-BOEM), OCS Study MMS 2009-041 funneled through the Coastal Marine Institute (University of Alaska Fairbanks).

This mooring was damaged so it was removed.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>





Dataset metadata:
|    | Dataset           | featuretype   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             |
|---:|:------------------|:--------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|
|  0 | ctd_moored_circac | timeSeries    |       60.7617 |       -151.505 | 2006-08-28 18:32:00 |       60.7617 |       -151.505 | 2006-08-11 23:32:00 |
    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_moored_circac"))
```

## Map of Time Series Location
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_moored_circac")("ctd_moored_circac")
    
```

## ctd_moored_circac
        

```{code-cell}
cat['ctd_moored_circac'].plot.data()
```
