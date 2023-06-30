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

# Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years

* adcp_moored_noaa_coi_other

See the full dataset page for more information: {ref}`page:adcp_moored_noaa_coi_other`

+++

## Map of Moored ADCPs



````{div} full-width                
```{figure} map_of_adcp_moored_noaa_coi_other.png
---
name: fig-map-adcp_moored_noaa_coi_other
---
Map of adcp_moored_noaa_coi_other data locations
```
````




+++

## Performance Summary

+++

### Across-channel velocity: tidally-filtered



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_across_subtidal.png
---
name: fig-overall-adcp_moored_noaa_coi_other-across-subtidal
---
Skill score for across-channel velocity, tidally-filtered
```
````




+++

### Along-channel velocity: tidally-filtered



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_along_subtidal.png
---
name: fig-overall-adcp_moored_noaa_coi_other-along-subtidal
---
Skill score for along-channel velocity, tidally-filtered
```
````




+++

### Horizontal speed: tidally-filtered



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_speed_subtidal.png
---
name: fig-overall-adcp_moored_noaa_coi_other-speed-subtidal
---
Skill score for horizontal speed, tidally-filtered
```
````




+++

## COI0206


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0206_across_subtidal.png
---
name: fig-ciofs-COI0206-across-subtidal
---
Model-data comparison for COI0206 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0206_across_subtidal.png
---
name: fig-nwgoa-COI0206-across-subtidal
---
Model-data comparison for COI0206 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0206_along_subtidal.png
---
name: fig-ciofs-COI0206-along-subtidal
---
Model-data comparison for COI0206 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0206_along_subtidal.png
---
name: fig-nwgoa-COI0206-along-subtidal
---
Model-data comparison for COI0206 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0206_speed_subtidal.png
---
name: fig-ciofs-COI0206-speed-subtidal
---
Model-data comparison for COI0206 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0206_speed_subtidal.png
---
name: fig-nwgoa-COI0206-speed-subtidal
---
Model-data comparison for COI0206 of horizontal speed
```


+++

## COI0207


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0207_across_subtidal.png
---
name: fig-ciofs-COI0207-across-subtidal
---
Model-data comparison for COI0207 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0207_across_subtidal.png
---
name: fig-nwgoa-COI0207-across-subtidal
---
Model-data comparison for COI0207 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0207_along_subtidal.png
---
name: fig-ciofs-COI0207-along-subtidal
---
Model-data comparison for COI0207 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0207_along_subtidal.png
---
name: fig-nwgoa-COI0207-along-subtidal
---
Model-data comparison for COI0207 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0207_speed_subtidal.png
---
name: fig-ciofs-COI0207-speed-subtidal
---
Model-data comparison for COI0207 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0207_speed_subtidal.png
---
name: fig-nwgoa-COI0207-speed-subtidal
---
Model-data comparison for COI0207 of horizontal speed
```


+++

## COI0213


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0213_across_subtidal.png
---
name: fig-ciofs-COI0213-across-subtidal
---
Model-data comparison for COI0213 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0213_across_subtidal.png
---
name: fig-nwgoa-COI0213-across-subtidal
---
Model-data comparison for COI0213 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0213_along_subtidal.png
---
name: fig-ciofs-COI0213-along-subtidal
---
Model-data comparison for COI0213 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0213_along_subtidal.png
---
name: fig-nwgoa-COI0213-along-subtidal
---
Model-data comparison for COI0213 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0213_speed_subtidal.png
---
name: fig-ciofs-COI0213-speed-subtidal
---
Model-data comparison for COI0213 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0213_speed_subtidal.png
---
name: fig-nwgoa-COI0213-speed-subtidal
---
Model-data comparison for COI0213 of horizontal speed
```


+++

## COI0301


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0301_across_subtidal.png
---
name: fig-ciofs-COI0301-across-subtidal
---
Model-data comparison for COI0301 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0301_across_subtidal.png
---
name: fig-nwgoa-COI0301-across-subtidal
---
Model-data comparison for COI0301 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0301_along_subtidal.png
---
name: fig-ciofs-COI0301-along-subtidal
---
Model-data comparison for COI0301 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0301_along_subtidal.png
---
name: fig-nwgoa-COI0301-along-subtidal
---
Model-data comparison for COI0301 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0301_speed_subtidal.png
---
name: fig-ciofs-COI0301-speed-subtidal
---
Model-data comparison for COI0301 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0301_speed_subtidal.png
---
name: fig-nwgoa-COI0301-speed-subtidal
---
Model-data comparison for COI0301 of horizontal speed
```


+++

## COI0302


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0302_across_subtidal.png
---
name: fig-ciofs-COI0302-across-subtidal
---
Model-data comparison for COI0302 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0302_across_subtidal.png
---
name: fig-nwgoa-COI0302-across-subtidal
---
Model-data comparison for COI0302 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0302_along_subtidal.png
---
name: fig-ciofs-COI0302-along-subtidal
---
Model-data comparison for COI0302 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0302_along_subtidal.png
---
name: fig-nwgoa-COI0302-along-subtidal
---
Model-data comparison for COI0302 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0302_speed_subtidal.png
---
name: fig-ciofs-COI0302-speed-subtidal
---
Model-data comparison for COI0302 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0302_speed_subtidal.png
---
name: fig-nwgoa-COI0302-speed-subtidal
---
Model-data comparison for COI0302 of horizontal speed
```


+++

## COI0303


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0303_across_subtidal.png
---
name: fig-ciofs-COI0303-across-subtidal
---
Model-data comparison for COI0303 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0303_across_subtidal.png
---
name: fig-nwgoa-COI0303-across-subtidal
---
Model-data comparison for COI0303 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0303_along_subtidal.png
---
name: fig-ciofs-COI0303-along-subtidal
---
Model-data comparison for COI0303 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0303_along_subtidal.png
---
name: fig-nwgoa-COI0303-along-subtidal
---
Model-data comparison for COI0303 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0303_speed_subtidal.png
---
name: fig-ciofs-COI0303-speed-subtidal
---
Model-data comparison for COI0303 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0303_speed_subtidal.png
---
name: fig-nwgoa-COI0303-speed-subtidal
---
Model-data comparison for COI0303 of horizontal speed
```


+++

## COI0306


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0306_across_subtidal.png
---
name: fig-ciofs-COI0306-across-subtidal
---
Model-data comparison for COI0306 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0306_across_subtidal.png
---
name: fig-nwgoa-COI0306-across-subtidal
---
Model-data comparison for COI0306 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0306_along_subtidal.png
---
name: fig-ciofs-COI0306-along-subtidal
---
Model-data comparison for COI0306 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0306_along_subtidal.png
---
name: fig-nwgoa-COI0306-along-subtidal
---
Model-data comparison for COI0306 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0306_speed_subtidal.png
---
name: fig-ciofs-COI0306-speed-subtidal
---
Model-data comparison for COI0306 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0306_speed_subtidal.png
---
name: fig-nwgoa-COI0306-speed-subtidal
---
Model-data comparison for COI0306 of horizontal speed
```


+++

## COI0307


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0307_across_subtidal.png
---
name: fig-ciofs-COI0307-across-subtidal
---
Model-data comparison for COI0307 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0307_across_subtidal.png
---
name: fig-nwgoa-COI0307-across-subtidal
---
Model-data comparison for COI0307 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0307_along_subtidal.png
---
name: fig-ciofs-COI0307-along-subtidal
---
Model-data comparison for COI0307 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0307_along_subtidal.png
---
name: fig-nwgoa-COI0307-along-subtidal
---
Model-data comparison for COI0307 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0307_speed_subtidal.png
---
name: fig-ciofs-COI0307-speed-subtidal
---
Model-data comparison for COI0307 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0307_speed_subtidal.png
---
name: fig-nwgoa-COI0307-speed-subtidal
---
Model-data comparison for COI0307 of horizontal speed
```


+++

## COI0418


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0418_across_subtidal.png
---
name: fig-ciofs-COI0418-across-subtidal
---
Model-data comparison for COI0418 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0418_across_subtidal.png
---
name: fig-nwgoa-COI0418-across-subtidal
---
Model-data comparison for COI0418 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0418_along_subtidal.png
---
name: fig-ciofs-COI0418-along-subtidal
---
Model-data comparison for COI0418 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0418_along_subtidal.png
---
name: fig-nwgoa-COI0418-along-subtidal
---
Model-data comparison for COI0418 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0418_speed_subtidal.png
---
name: fig-ciofs-COI0418-speed-subtidal
---
Model-data comparison for COI0418 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0418_speed_subtidal.png
---
name: fig-nwgoa-COI0418-speed-subtidal
---
Model-data comparison for COI0418 of horizontal speed
```


+++

## COI0419


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0419_across_subtidal.png
---
name: fig-ciofs-COI0419-across-subtidal
---
Model-data comparison for COI0419 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0419_across_subtidal.png
---
name: fig-nwgoa-COI0419-across-subtidal
---
Model-data comparison for COI0419 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0419_along_subtidal.png
---
name: fig-ciofs-COI0419-along-subtidal
---
Model-data comparison for COI0419 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0419_along_subtidal.png
---
name: fig-nwgoa-COI0419-along-subtidal
---
Model-data comparison for COI0419 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0419_speed_subtidal.png
---
name: fig-ciofs-COI0419-speed-subtidal
---
Model-data comparison for COI0419 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0419_speed_subtidal.png
---
name: fig-nwgoa-COI0419-speed-subtidal
---
Model-data comparison for COI0419 of horizontal speed
```


+++

## COI0420


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0420_across_subtidal.png
---
name: fig-ciofs-COI0420-across-subtidal
---
Model-data comparison for COI0420 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0420_across_subtidal.png
---
name: fig-nwgoa-COI0420-across-subtidal
---
Model-data comparison for COI0420 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0420_along_subtidal.png
---
name: fig-ciofs-COI0420-along-subtidal
---
Model-data comparison for COI0420 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0420_along_subtidal.png
---
name: fig-nwgoa-COI0420-along-subtidal
---
Model-data comparison for COI0420 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_other_ciofs/adcp_moored_noaa_coi_other_COI0420_speed_subtidal.png
---
name: fig-ciofs-COI0420-speed-subtidal
---
Model-data comparison for COI0420 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0420_speed_subtidal.png
---
name: fig-nwgoa-COI0420-speed-subtidal
---
Model-data comparison for COI0420 of horizontal speed
```


+++

## COI0421


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0421_across_subtidal.png
---
name: fig-nwgoa-COI0421-across-subtidal
---
Model-data comparison for COI0421 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0421_along_subtidal.png
---
name: fig-nwgoa-COI0421-along-subtidal
---
Model-data comparison for COI0421 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0421_speed_subtidal.png
---
name: fig-nwgoa-COI0421-speed-subtidal
---
Model-data comparison for COI0421 of horizontal speed
```


+++

## COI0422


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0422_across_subtidal.png
---
name: fig-nwgoa-COI0422-across-subtidal
---
Model-data comparison for COI0422 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0422_along_subtidal.png
---
name: fig-nwgoa-COI0422-along-subtidal
---
Model-data comparison for COI0422 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0422_speed_subtidal.png
---
name: fig-nwgoa-COI0422-speed-subtidal
---
Model-data comparison for COI0422 of horizontal speed
```


+++

## COI0801


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0801_across_subtidal.png
---
name: fig-nwgoa-COI0801-across-subtidal
---
Model-data comparison for COI0801 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0801_along_subtidal.png
---
name: fig-nwgoa-COI0801-along-subtidal
---
Model-data comparison for COI0801 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_other_nwgoa/adcp_moored_noaa_coi_other_COI0801_speed_subtidal.png
---
name: fig-nwgoa-COI0801-speed-subtidal
---
Model-data comparison for COI0801 of horizontal speed
```


+++

## COI0802


+++

## COI1201


CIOFS: Data time range is 2012-06-14 to 2012-08-14 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-14 to 2012-08-14 but model ends 2009-01-01.


+++

## COI1202


CIOFS: Data time range is 2012-06-13 to 2012-08-14 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-13 to 2012-08-14 but model ends 2009-01-01.


+++

## COI1203


CIOFS: Data time range is 2012-06-14 to 2012-08-14 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-14 to 2012-08-14 but model ends 2009-01-01.


+++

## COI1204


CIOFS: Data time range is 2012-06-16 to 2012-08-17 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-16 to 2012-08-17 but model ends 2009-01-01.


+++

## COI1205


CIOFS: Data time range is 2012-06-15 to 2012-08-15 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-15 to 2012-08-15 but model ends 2009-01-01.


+++

## COI1207


CIOFS: Data time range is 2012-06-16 to 2012-08-17 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-16 to 2012-08-17 but model ends 2009-01-01.


+++

## COI1208


CIOFS: Data time range is 2012-06-16 to 2012-08-17 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-16 to 2012-08-17 but model ends 2009-01-01.


+++

## COI1209


CIOFS: Data time range is 2012-06-17 to 2012-08-17 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-17 to 2012-08-17 but model ends 2009-01-01.


+++

## COI1210


CIOFS: Data time range is 2012-06-15 to 2012-08-16 but model ends 2008-08-25.


NWGOA: Data time range is 2012-06-15 to 2012-08-16 but model ends 2009-01-01.
