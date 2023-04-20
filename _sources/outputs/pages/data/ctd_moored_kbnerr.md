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

# Lower Cook Inlet Mooring

* CTD Moored 2006-2008 - KBNERR
* ctd_moored_kbnerr
* Aug to Oct 2006 and June 2007 to Feb 2008, 15 min sampling

Lower Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

CIRCAC is the Cook Inlet Regional Citizens Advisory Council. It was funded by MMS (pre-BOEM), OCS Study MMS 2009-041 funneled through the Coastal Marine Institute (University of Alaska Fairbanks).

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>





    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_moored_kbnerr"))
```

## Map of Time Series Location
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_moored_kbnerr")("ctd_moored_kbnerr")
    
```

## Deployment1
        

```{code-cell}
cat['Deployment1'].plot.data()
```

## Deployment2
        

```{code-cell}
cat['Deployment2'].plot.data()
```
