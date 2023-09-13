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
import holoviews as hv
from holoviews import opts
```

(page:ctd_transects_cmi_uaf)=
# CTD Transect (CMI UAF): from East Foreland Lighthouse

* CTD profiles 2004-2005 - CMI UAF
* ctd_transects_cmi_uaf
* 10 cruises, approximately monthly for summer months, in 2004 and 2005

Seasonality of Boundary Conditions for Cook Inlet, Alaska: Transect (3) at East Foreland Lighthouse.

9 CTD profiles at stations across 10 cruises in (approximately) the same locations. Approximately monthly for summer months, 2004 and 2005.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/files/39885971/2009_041.pdf


Used in the NWGOA model/data comparison.

```{dropdown} Dataset metadata

|    | Dataset   | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                            |
|---:|:----------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------------|
|  0 | Cruise-01 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.418 | 2004-05-21 10:34:00 |        60.716 |       -151.683 | 2004-05-21 09:23:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  1 | Cruise-02 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2004-06-24 09:08:00 |        60.716 |       -151.683 | 2004-06-24 07:07:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  2 | Cruise-03 | trajectoryProfile | ['temp', 'salt'] |        60.718 |       -151.417 | 2004-08-08 09:20:00 |        60.716 |       -151.683 | 2004-08-08 07:55:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  3 | Cruise-04 | trajectoryProfile | ['temp', 'salt'] |        60.718 |       -151.417 | 2004-09-17 08:25:00 |        60.715 |       -151.684 | 2004-09-17 07:00:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  4 | Cruise-05 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2004-10-09 14:37:00 |        60.713 |       -151.683 | 2004-10-09 13:21:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  5 | Cruise-06 | trajectoryProfile | ['temp', 'salt'] |        60.72  |       -151.45  | 2005-03-30 12:49:00 |        60.72  |       -151.65  | 2005-03-30 11:22:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  6 | Cruise-07 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-05-02 12:32:00 |        60.715 |       -151.683 | 2005-05-02 11:13:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  7 | Cruise-08 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-06-01 13:23:00 |        60.715 |       -151.683 | 2005-06-01 12:03:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  8 | Cruise-09 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-08-26 11:08:00 |        60.715 |       -151.683 | 2005-08-26 09:35:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |
|  9 | Cruise-10 | trajectoryProfile | ['temp', 'salt'] |        60.717 |       -151.417 | 2005-10-03 18:50:00 |        60.716 |       -151.684 | 2005-10-03 17:39:00 | https://researchworkspace.com/files/39886038/all_forelands_ctd.txt |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_transects_cmi_uaf"))
```

## Map of CTD Transects
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_cmi_uaf")("ctd_transects_cmi_uaf")
```

## Cruise-01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-01'].plot.salt() + cat['Cruise-01'].plot.temp()
```

## Cruise-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-02'].plot.salt() + cat['Cruise-02'].plot.temp()
```

## Cruise-03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-03'].plot.salt() + cat['Cruise-03'].plot.temp()
```

## Cruise-04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-04'].plot.salt() + cat['Cruise-04'].plot.temp()
```

## Cruise-05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-05'].plot.salt() + cat['Cruise-05'].plot.temp()
```

## Cruise-06
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-06'].plot.salt() + cat['Cruise-06'].plot.temp()
```

## Cruise-07
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-07'].plot.salt() + cat['Cruise-07'].plot.temp()
```

## Cruise-08
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-08'].plot.salt() + cat['Cruise-08'].plot.temp()
```

## Cruise-09
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-09'].plot.salt() + cat['Cruise-09'].plot.temp()
```

## Cruise-10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cruise-10'].plot.salt() + cat['Cruise-10'].plot.temp()
```
