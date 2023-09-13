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

(page:hfradar)=
# HF Radar (UAF)

* HF Radar - UAF
* hfradar
* 2002-2009

HF Radar from UAF.

Files are:
* Upper Cook Inlet (System A): 2002-2003 and 2009
* Lower Cook Inlet (System B): 2006-2007

Data variables available include tidally filtered and weekly averaged along with tidal constituents calculated from hourly data.
    
Some of the data is written up in reports:
* https://espis.boem.gov/final%20reports/5009.pdf
* https://www.govinfo.gov/app/details/GOVPUB-I-47b721482d69e308aec1cca9b3e51955

![pic](https://researchworkspace.com/files/40338104/UAcoverage.gif)


These are accessed from Research Workspace where they have already been processed.

```{dropdown} Dataset metadata

|    | Dataset                              | featuretype   | key_variables   |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                                                          |
|---:|:-------------------------------------|:--------------|:----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-------------------------------------------------------------------------------------------------|
|  0 | lower-ci_system-B_2006-2007          | grid          | []              |       60.0411 |       -151.899 | 2007-11-11 00:00:00 |       59.1251 |       -153.23  | 2006-11-12 00:00:00 | https://researchworkspace.com/files/42394327/lower-ci_system-B_2006-2007_subtidal_weekly_mean.nc |
|  1 | lower-ci_system-B_2006-2007_tidecons | grid          | nan             |      nan      |        nan     | nan                 |      nan      |        nan     | nan                 | https://researchworkspace.com/files/42393598/lower-ci_system-B_2006-2007_tidecons.nc             |
|  2 | upper-ci_system-A_2002-2003          | grid          | []              |       60.7497 |       -151.358 | 2003-06-15 00:00:00 |       60.2635 |       -152.126 | 2002-12-08 00:00:00 | https://researchworkspace.com/files/42394322/upper-ci_system-A_2002-2003_subtidal_weekly_mean.nc |
|  3 | upper-ci_system-A_2002-2003_tidecons | grid          | nan             |      nan      |        nan     | nan                 |      nan      |        nan     | nan                 | https://researchworkspace.com/files/42393592/upper-ci_system-A_2002-2003_tidecons.nc             |
|  4 | upper-ci_system-A_2009               | grid          | []              |       60.7716 |       -151.378 | 2009-06-07 00:00:00 |       60.2321 |       -152.378 | 2009-04-19 00:00:00 | https://researchworkspace.com/files/42394329/upper-ci_system-A_2009_subtidal_weekly_mean.nc      |
|  5 | upper-ci_system-A_2009_tidecons      | grid          | nan             |      nan      |        nan     | nan                 |      nan      |        nan     | nan                 | https://researchworkspace.com/files/42393604/upper-ci_system-A_2009_tidecons.nc                  |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("hfradar"))
```

## Map of HF Radar Data Areas
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "hfradar")("hfradar")
```

## Lower CI/System B, 2006-2007: Weekly Subtidal Means

+++

lower-ci_system-B_2006-2007
        

```{code-cell}
:tags: [full-width, remove-input]


hv.output(widget_location='bottom')
cat['lower-ci_system-B_2006-2007'].plot.direction().opts(opts.VectorField(magnitude='speed_subtidal'))
```

## Lower CI/System B, 2006-2007: Tidal Constituents

+++

lower-ci_system-B_2006-2007_tidecons
        

```{code-cell}
:tags: [full-width, remove-input]

cat['lower-ci_system-B_2006-2007_tidecons'].plot.tidecons()
```

## Upper CI/System A, 2002-2003: Weekly Subtidal Means

+++

upper-ci_system-A_2002-2003
        

```{code-cell}
:tags: [full-width, remove-input]


hv.output(widget_location='bottom')
cat['upper-ci_system-A_2002-2003'].plot.direction().opts(opts.VectorField(magnitude='speed_subtidal'))
```

## Upper CI/System A, 2002-2003: Tidal Constituents

+++

upper-ci_system-A_2002-2003_tidecons
        

```{code-cell}
:tags: [full-width, remove-input]

cat['upper-ci_system-A_2002-2003_tidecons'].plot.tidecons()
```

## Upper CI/System A, 2009: Weekly Subtidal Means

+++

upper-ci_system-A_2009
        

```{code-cell}
:tags: [full-width, remove-input]


hv.output(widget_location='bottom')
cat['upper-ci_system-A_2009'].plot.direction().opts(opts.VectorField(magnitude='speed_subtidal'))
```

## Upper CI/System A, 2009: Tidal Constituents

+++

upper-ci_system-A_2009_tidecons
        

```{code-cell}
:tags: [full-width, remove-input]

cat['upper-ci_system-A_2009_tidecons'].plot.tidecons()
```
