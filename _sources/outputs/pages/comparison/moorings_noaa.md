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
from IPython.display import Image, display
```

# Moorings (NOAA): across Cook Inlet

* moorings_noaa

See the {doc}`full dataset page <ciofs_hindcast_report/outputs/pages/data/moorings_noaa>` for more information.


+++

## Map of Moorings
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "moorings_noaa")("moorings_noaa")
    
```

## Performance Summary

+++

### ssh, subtract-mean

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_ssh_subtract-mean.png"))
```

### ssh, subtract-mean_subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_ssh_subtract-mean_subtidal.png"))
```

### temp, subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_temp_subtidal.png"))
```

### temp, subtidal_subtract-monthly-mean

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_temp_subtidal_subtract-monthly-mean.png"))
```

## boulder-point


+++

### ssh, subtract-mean

+++

#### ciofs


```{code-cell}
:tags: [remove-input, full-width]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_boulder-point_ssh_subtract-mean.png"))
```

#### nwgoa


```{code-cell}
:tags: [remove-input, full-width]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_boulder-point_ssh_subtract-mean.png"))
```

## geese-island-gps-tide-buoy


+++

## noaa_nos_co_ops_9455500


+++

### ssh, subtract-mean_subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9455500_ssh_subtract-mean_subtidal.png"))
```

#### ciofs


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png"))
```

#### nwgoa


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png"))
```

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png"))
```

### temp, subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9455500_temp_subtidal.png"))
```

#### ciofs


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal.png"))
```

#### nwgoa


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal.png"))
```

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01_subtidal.png"))
```

### temp, subtidal_subtract-monthly-mean

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9455500_temp_subtidal_subtract-monthly-mean.png"))
```

#### ciofs


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png"))
```

#### nwgoa


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png"))
```

## noaa_nos_co_ops_9455595


+++

### ssh, subtract-mean_subtidal

+++

#### ciofs


+++

#### nwgoa


+++

## noaa_nos_co_ops_9455920


+++

### ssh, subtract-mean_subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9455920_ssh_subtract-mean_subtidal.png"))
```

#### ciofs


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png"))
```

#### nwgoa


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png"))
```

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png"))
```

### temp, subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9455920_temp_subtidal.png"))
```

#### ciofs


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal.png"))
```

#### nwgoa


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal.png"))
```

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01_subtidal.png"))
```

### temp, subtidal_subtract-monthly-mean

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9455920_temp_subtidal_subtract-monthly-mean.png"))
```

#### ciofs


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_ciofs/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png"))
```

#### nwgoa


+++

##### 1999


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2000


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2001


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2002


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2003


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2004


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2005


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png"))
```

## noaa_nos_co_ops_9457804


+++

### ssh, subtract-mean_subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9457804_ssh_subtract-mean_subtidal.png"))
```

#### ciofs


+++

#### nwgoa


+++

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png"))
```

### temp, subtidal

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9457804_temp_subtidal.png"))
```

#### ciofs


+++

#### nwgoa


+++

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01_subtidal.png"))
```

### temp, subtidal_subtract-monthly-mean

```{code-cell}
:tags: [remove-input]

display(Image(filename="/Users/kthyng/projects/ciofs-hindcast-report/ciofs_hindcast_report/outputs/pages/comparison/moorings_noaa_noaa_nos_co_ops_9457804_temp_subtidal_subtract-monthly-mean.png"))
```

#### ciofs


+++

#### nwgoa


+++

##### 2006


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2007


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png"))
```

##### 2008


```{code-cell}
:tags: [remove-input, full-width, hide-output]

display(Image(filename="/Users/kthyng/Library/Caches/ocean-model-skill-assessor/moorings_noaa_nwgoa/out/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png"))
```

## noaa_nos_co_ops_kdaa2


+++

## old-harbor-1


+++

## sitkalidak-island-gps-tide-bu


+++

## wmo_46077
