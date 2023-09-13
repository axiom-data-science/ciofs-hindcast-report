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

(page:ctd_transects_misc_2002)=
# CTD transects (2002)

* CTD transects 2002
* ctd_transects_misc_2002
* 2002

Miscellaneous CTD transects in Cook Inlet from 2002




```{dropdown} Dataset metadata

|    | Dataset         | featuretype       | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                          |
|---:|:----------------|:------------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------------|
|  0 | Bear_Jul-02     | trajectoryProfile | ['temp', 'salt'] |       59.7535 |       -151.07  | 2002-07-26 17:45:00 |       59.7302 |       -151.123 | 2002-07-26 17:18:00 | https://researchworkspace.com/files/42186319/Bear_Jul-02.csv     |
|  1 | Cohen           | trajectoryProfile | ['temp', 'salt'] |       59.5959 |       -151.415 | 2002-07-24 18:28:00 |       59.5392 |       -151.481 | 2002-07-24 17:24:00 | https://researchworkspace.com/files/42186397/Cohen.csv           |
|  2 | Glacier         | trajectoryProfile | ['temp', 'salt'] |       59.6954 |       -151.196 | 2002-07-26 19:22:00 |       59.6519 |       -151.258 | 2002-07-26 18:46:00 | https://researchworkspace.com/files/42199559/Glacier.csv         |
|  3 | Peterson_Jul-02 | trajectoryProfile | ['temp', 'salt'] |       59.6012 |       -151.274 | 2002-07-24 17:12:00 |       59.5977 |       -151.407 | 2002-07-24 15:48:00 | https://researchworkspace.com/files/42199566/Peterson_Jul-02.csv |
|  4 | PtAdam_jul-02   | trajectoryProfile | ['temp', 'salt'] |       59.2591 |       -152.001 | 2002-07-28 23:09:00 |       59.2559 |       -152.097 | 2002-07-28 22:27:00 | https://researchworkspace.com/files/42200000/PtAdam_jul-02.csv   |
|  5 | pogibshi_Jul-02 | trajectoryProfile | ['temp', 'salt'] |       59.7455 |       -151.866 | 2002-07-25 19:57:00 |       59.4259 |       -151.892 | 2002-07-25 16:08:00 | https://researchworkspace.com/files/42199989/pogibshi_Jul-02.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_transects_misc_2002"))
```

## Map of CTD Transects
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_transects_misc_2002")("ctd_transects_misc_2002")
```

## Bear_Jul-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Bear_Jul-02'].plot.salt() + cat['Bear_Jul-02'].plot.temp()
```

## Cohen
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Cohen'].plot.salt() + cat['Cohen'].plot.temp()
```

## Glacier
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Glacier'].plot.salt() + cat['Glacier'].plot.temp()
```

## Peterson_Jul-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['Peterson_Jul-02'].plot.salt() + cat['Peterson_Jul-02'].plot.temp()
```

## PtAdam_jul-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['PtAdam_jul-02'].plot.salt() + cat['PtAdam_jul-02'].plot.temp()
```

## pogibshi_Jul-02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['pogibshi_Jul-02'].plot.salt() + cat['pogibshi_Jul-02'].plot.temp()
```
