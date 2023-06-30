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

# Moored ADCP (NOAA): ADCP survey Cook Inlet 2005

* adcp_moored_noaa_coi_2005

See the full dataset page for more information: {ref}`page:adcp_moored_noaa_coi_2005`

+++

## Map of Moored ADCPs



````{div} full-width                
```{figure} map_of_adcp_moored_noaa_coi_2005.png
---
name: fig-map-adcp_moored_noaa_coi_2005
---
Map of adcp_moored_noaa_coi_2005 data locations
```
````




+++

## Performance Summary

+++

### Across-channel velocity: tidally-filtered



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_across_subtidal.png
---
name: fig-overall-adcp_moored_noaa_coi_2005-across-subtidal
---
Skill score for across-channel velocity, tidally-filtered
```
````




+++

### Along-channel velocity: tidally-filtered



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_along_subtidal.png
---
name: fig-overall-adcp_moored_noaa_coi_2005-along-subtidal
---
Skill score for along-channel velocity, tidally-filtered
```
````




+++

### Horizontal speed: tidally-filtered



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_speed_subtidal.png
---
name: fig-overall-adcp_moored_noaa_coi_2005-speed-subtidal
---
Skill score for horizontal speed, tidally-filtered
```
````




+++

## COI0501


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0501_across_subtidal.png
---
name: fig-ciofs-COI0501-across-subtidal
---
Model-data comparison for COI0501 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0501_across_subtidal.png
---
name: fig-nwgoa-COI0501-across-subtidal
---
Model-data comparison for COI0501 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0501_along_subtidal.png
---
name: fig-ciofs-COI0501-along-subtidal
---
Model-data comparison for COI0501 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0501_along_subtidal.png
---
name: fig-nwgoa-COI0501-along-subtidal
---
Model-data comparison for COI0501 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0501_speed_subtidal.png
---
name: fig-ciofs-COI0501-speed-subtidal
---
Model-data comparison for COI0501 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0501_speed_subtidal.png
---
name: fig-nwgoa-COI0501-speed-subtidal
---
Model-data comparison for COI0501 of horizontal speed
```


+++

## COI0502


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0502_across_subtidal.png
---
name: fig-ciofs-COI0502-across-subtidal
---
Model-data comparison for COI0502 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0502_across_subtidal.png
---
name: fig-nwgoa-COI0502-across-subtidal
---
Model-data comparison for COI0502 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0502_along_subtidal.png
---
name: fig-ciofs-COI0502-along-subtidal
---
Model-data comparison for COI0502 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0502_along_subtidal.png
---
name: fig-nwgoa-COI0502-along-subtidal
---
Model-data comparison for COI0502 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0502_speed_subtidal.png
---
name: fig-ciofs-COI0502-speed-subtidal
---
Model-data comparison for COI0502 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0502_speed_subtidal.png
---
name: fig-nwgoa-COI0502-speed-subtidal
---
Model-data comparison for COI0502 of horizontal speed
```


+++

## COI0503


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0503_across_subtidal.png
---
name: fig-ciofs-COI0503-across-subtidal
---
Model-data comparison for COI0503 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0503_across_subtidal.png
---
name: fig-nwgoa-COI0503-across-subtidal
---
Model-data comparison for COI0503 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0503_along_subtidal.png
---
name: fig-ciofs-COI0503-along-subtidal
---
Model-data comparison for COI0503 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0503_along_subtidal.png
---
name: fig-nwgoa-COI0503-along-subtidal
---
Model-data comparison for COI0503 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0503_speed_subtidal.png
---
name: fig-ciofs-COI0503-speed-subtidal
---
Model-data comparison for COI0503 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0503_speed_subtidal.png
---
name: fig-nwgoa-COI0503-speed-subtidal
---
Model-data comparison for COI0503 of horizontal speed
```


+++

## COI0504


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0504_across_subtidal.png
---
name: fig-ciofs-COI0504-across-subtidal
---
Model-data comparison for COI0504 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0504_across_subtidal.png
---
name: fig-nwgoa-COI0504-across-subtidal
---
Model-data comparison for COI0504 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0504_along_subtidal.png
---
name: fig-ciofs-COI0504-along-subtidal
---
Model-data comparison for COI0504 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0504_along_subtidal.png
---
name: fig-nwgoa-COI0504-along-subtidal
---
Model-data comparison for COI0504 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0504_speed_subtidal.png
---
name: fig-ciofs-COI0504-speed-subtidal
---
Model-data comparison for COI0504 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0504_speed_subtidal.png
---
name: fig-nwgoa-COI0504-speed-subtidal
---
Model-data comparison for COI0504 of horizontal speed
```


+++

## COI0505


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0505_across_subtidal.png
---
name: fig-ciofs-COI0505-across-subtidal
---
Model-data comparison for COI0505 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0505_across_subtidal.png
---
name: fig-nwgoa-COI0505-across-subtidal
---
Model-data comparison for COI0505 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0505_along_subtidal.png
---
name: fig-ciofs-COI0505-along-subtidal
---
Model-data comparison for COI0505 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0505_along_subtidal.png
---
name: fig-nwgoa-COI0505-along-subtidal
---
Model-data comparison for COI0505 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0505_speed_subtidal.png
---
name: fig-ciofs-COI0505-speed-subtidal
---
Model-data comparison for COI0505 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0505_speed_subtidal.png
---
name: fig-nwgoa-COI0505-speed-subtidal
---
Model-data comparison for COI0505 of horizontal speed
```


+++

## COI0506


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0506_across_subtidal.png
---
name: fig-ciofs-COI0506-across-subtidal
---
Model-data comparison for COI0506 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0506_across_subtidal.png
---
name: fig-nwgoa-COI0506-across-subtidal
---
Model-data comparison for COI0506 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0506_along_subtidal.png
---
name: fig-ciofs-COI0506-along-subtidal
---
Model-data comparison for COI0506 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0506_along_subtidal.png
---
name: fig-nwgoa-COI0506-along-subtidal
---
Model-data comparison for COI0506 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0506_speed_subtidal.png
---
name: fig-ciofs-COI0506-speed-subtidal
---
Model-data comparison for COI0506 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0506_speed_subtidal.png
---
name: fig-nwgoa-COI0506-speed-subtidal
---
Model-data comparison for COI0506 of horizontal speed
```


+++

## COI0507


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0507_across_subtidal.png
---
name: fig-ciofs-COI0507-across-subtidal
---
Model-data comparison for COI0507 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0507_across_subtidal.png
---
name: fig-nwgoa-COI0507-across-subtidal
---
Model-data comparison for COI0507 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0507_along_subtidal.png
---
name: fig-ciofs-COI0507-along-subtidal
---
Model-data comparison for COI0507 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0507_along_subtidal.png
---
name: fig-nwgoa-COI0507-along-subtidal
---
Model-data comparison for COI0507 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0507_speed_subtidal.png
---
name: fig-ciofs-COI0507-speed-subtidal
---
Model-data comparison for COI0507 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0507_speed_subtidal.png
---
name: fig-nwgoa-COI0507-speed-subtidal
---
Model-data comparison for COI0507 of horizontal speed
```


+++

## COI0508


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0508_across_subtidal.png
---
name: fig-ciofs-COI0508-across-subtidal
---
Model-data comparison for COI0508 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0508_across_subtidal.png
---
name: fig-nwgoa-COI0508-across-subtidal
---
Model-data comparison for COI0508 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0508_along_subtidal.png
---
name: fig-ciofs-COI0508-along-subtidal
---
Model-data comparison for COI0508 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0508_along_subtidal.png
---
name: fig-nwgoa-COI0508-along-subtidal
---
Model-data comparison for COI0508 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0508_speed_subtidal.png
---
name: fig-ciofs-COI0508-speed-subtidal
---
Model-data comparison for COI0508 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0508_speed_subtidal.png
---
name: fig-nwgoa-COI0508-speed-subtidal
---
Model-data comparison for COI0508 of horizontal speed
```


+++

## COI0509


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0509_across_subtidal.png
---
name: fig-ciofs-COI0509-across-subtidal
---
Model-data comparison for COI0509 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0509_across_subtidal.png
---
name: fig-nwgoa-COI0509-across-subtidal
---
Model-data comparison for COI0509 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0509_along_subtidal.png
---
name: fig-ciofs-COI0509-along-subtidal
---
Model-data comparison for COI0509 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0509_along_subtidal.png
---
name: fig-nwgoa-COI0509-along-subtidal
---
Model-data comparison for COI0509 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0509_speed_subtidal.png
---
name: fig-ciofs-COI0509-speed-subtidal
---
Model-data comparison for COI0509 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0509_speed_subtidal.png
---
name: fig-nwgoa-COI0509-speed-subtidal
---
Model-data comparison for COI0509 of horizontal speed
```


+++

## COI0510


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0510_across_subtidal.png
---
name: fig-ciofs-COI0510-across-subtidal
---
Model-data comparison for COI0510 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0510_across_subtidal.png
---
name: fig-nwgoa-COI0510-across-subtidal
---
Model-data comparison for COI0510 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0510_along_subtidal.png
---
name: fig-ciofs-COI0510-along-subtidal
---
Model-data comparison for COI0510 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0510_along_subtidal.png
---
name: fig-nwgoa-COI0510-along-subtidal
---
Model-data comparison for COI0510 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0510_speed_subtidal.png
---
name: fig-ciofs-COI0510-speed-subtidal
---
Model-data comparison for COI0510 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0510_speed_subtidal.png
---
name: fig-nwgoa-COI0510-speed-subtidal
---
Model-data comparison for COI0510 of horizontal speed
```


+++

## COI0511


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0511_across_subtidal.png
---
name: fig-ciofs-COI0511-across-subtidal
---
Model-data comparison for COI0511 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0511_across_subtidal.png
---
name: fig-nwgoa-COI0511-across-subtidal
---
Model-data comparison for COI0511 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0511_along_subtidal.png
---
name: fig-ciofs-COI0511-along-subtidal
---
Model-data comparison for COI0511 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0511_along_subtidal.png
---
name: fig-nwgoa-COI0511-along-subtidal
---
Model-data comparison for COI0511 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0511_speed_subtidal.png
---
name: fig-ciofs-COI0511-speed-subtidal
---
Model-data comparison for COI0511 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0511_speed_subtidal.png
---
name: fig-nwgoa-COI0511-speed-subtidal
---
Model-data comparison for COI0511 of horizontal speed
```


+++

## COI0512


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0512_across_subtidal.png
---
name: fig-ciofs-COI0512-across-subtidal
---
Model-data comparison for COI0512 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0512_across_subtidal.png
---
name: fig-nwgoa-COI0512-across-subtidal
---
Model-data comparison for COI0512 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0512_along_subtidal.png
---
name: fig-ciofs-COI0512-along-subtidal
---
Model-data comparison for COI0512 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0512_along_subtidal.png
---
name: fig-nwgoa-COI0512-along-subtidal
---
Model-data comparison for COI0512 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0512_speed_subtidal.png
---
name: fig-ciofs-COI0512-speed-subtidal
---
Model-data comparison for COI0512 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0512_speed_subtidal.png
---
name: fig-nwgoa-COI0512-speed-subtidal
---
Model-data comparison for COI0512 of horizontal speed
```


+++

## COI0513


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0513_across_subtidal.png
---
name: fig-ciofs-COI0513-across-subtidal
---
Model-data comparison for COI0513 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0513_across_subtidal.png
---
name: fig-nwgoa-COI0513-across-subtidal
---
Model-data comparison for COI0513 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0513_along_subtidal.png
---
name: fig-ciofs-COI0513-along-subtidal
---
Model-data comparison for COI0513 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0513_along_subtidal.png
---
name: fig-nwgoa-COI0513-along-subtidal
---
Model-data comparison for COI0513 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0513_speed_subtidal.png
---
name: fig-ciofs-COI0513-speed-subtidal
---
Model-data comparison for COI0513 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0513_speed_subtidal.png
---
name: fig-nwgoa-COI0513-speed-subtidal
---
Model-data comparison for COI0513 of horizontal speed
```


+++

## COI0514


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0514_across_subtidal.png
---
name: fig-ciofs-COI0514-across-subtidal
---
Model-data comparison for COI0514 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0514_across_subtidal.png
---
name: fig-nwgoa-COI0514-across-subtidal
---
Model-data comparison for COI0514 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0514_along_subtidal.png
---
name: fig-ciofs-COI0514-along-subtidal
---
Model-data comparison for COI0514 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0514_along_subtidal.png
---
name: fig-nwgoa-COI0514-along-subtidal
---
Model-data comparison for COI0514 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0514_speed_subtidal.png
---
name: fig-ciofs-COI0514-speed-subtidal
---
Model-data comparison for COI0514 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0514_speed_subtidal.png
---
name: fig-nwgoa-COI0514-speed-subtidal
---
Model-data comparison for COI0514 of horizontal speed
```


+++

## COI0515


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0515_across_subtidal.png
---
name: fig-ciofs-COI0515-across-subtidal
---
Model-data comparison for COI0515 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0515_across_subtidal.png
---
name: fig-nwgoa-COI0515-across-subtidal
---
Model-data comparison for COI0515 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0515_along_subtidal.png
---
name: fig-ciofs-COI0515-along-subtidal
---
Model-data comparison for COI0515 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0515_along_subtidal.png
---
name: fig-nwgoa-COI0515-along-subtidal
---
Model-data comparison for COI0515 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0515_speed_subtidal.png
---
name: fig-ciofs-COI0515-speed-subtidal
---
Model-data comparison for COI0515 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0515_speed_subtidal.png
---
name: fig-nwgoa-COI0515-speed-subtidal
---
Model-data comparison for COI0515 of horizontal speed
```


+++

## COI0516


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0516_across_subtidal.png
---
name: fig-ciofs-COI0516-across-subtidal
---
Model-data comparison for COI0516 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0516_across_subtidal.png
---
name: fig-nwgoa-COI0516-across-subtidal
---
Model-data comparison for COI0516 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0516_along_subtidal.png
---
name: fig-ciofs-COI0516-along-subtidal
---
Model-data comparison for COI0516 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0516_along_subtidal.png
---
name: fig-nwgoa-COI0516-along-subtidal
---
Model-data comparison for COI0516 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0516_speed_subtidal.png
---
name: fig-ciofs-COI0516-speed-subtidal
---
Model-data comparison for COI0516 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0516_speed_subtidal.png
---
name: fig-nwgoa-COI0516-speed-subtidal
---
Model-data comparison for COI0516 of horizontal speed
```


+++

## COI0517


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0517_across_subtidal.png
---
name: fig-ciofs-COI0517-across-subtidal
---
Model-data comparison for COI0517 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0517_across_subtidal.png
---
name: fig-nwgoa-COI0517-across-subtidal
---
Model-data comparison for COI0517 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0517_along_subtidal.png
---
name: fig-ciofs-COI0517-along-subtidal
---
Model-data comparison for COI0517 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0517_along_subtidal.png
---
name: fig-nwgoa-COI0517-along-subtidal
---
Model-data comparison for COI0517 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0517_speed_subtidal.png
---
name: fig-ciofs-COI0517-speed-subtidal
---
Model-data comparison for COI0517 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0517_speed_subtidal.png
---
name: fig-nwgoa-COI0517-speed-subtidal
---
Model-data comparison for COI0517 of horizontal speed
```


+++

## COI0518


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0518_across_subtidal.png
---
name: fig-ciofs-COI0518-across-subtidal
---
Model-data comparison for COI0518 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0518_across_subtidal.png
---
name: fig-nwgoa-COI0518-across-subtidal
---
Model-data comparison for COI0518 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0518_along_subtidal.png
---
name: fig-ciofs-COI0518-along-subtidal
---
Model-data comparison for COI0518 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0518_along_subtidal.png
---
name: fig-nwgoa-COI0518-along-subtidal
---
Model-data comparison for COI0518 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0518_speed_subtidal.png
---
name: fig-ciofs-COI0518-speed-subtidal
---
Model-data comparison for COI0518 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0518_speed_subtidal.png
---
name: fig-nwgoa-COI0518-speed-subtidal
---
Model-data comparison for COI0518 of horizontal speed
```


+++

## COI0519


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0519_across_subtidal.png
---
name: fig-ciofs-COI0519-across-subtidal
---
Model-data comparison for COI0519 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0519_across_subtidal.png
---
name: fig-nwgoa-COI0519-across-subtidal
---
Model-data comparison for COI0519 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0519_along_subtidal.png
---
name: fig-ciofs-COI0519-along-subtidal
---
Model-data comparison for COI0519 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0519_along_subtidal.png
---
name: fig-nwgoa-COI0519-along-subtidal
---
Model-data comparison for COI0519 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0519_speed_subtidal.png
---
name: fig-ciofs-COI0519-speed-subtidal
---
Model-data comparison for COI0519 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0519_speed_subtidal.png
---
name: fig-nwgoa-COI0519-speed-subtidal
---
Model-data comparison for COI0519 of horizontal speed
```


+++

## COI0520


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0520_across_subtidal.png
---
name: fig-ciofs-COI0520-across-subtidal
---
Model-data comparison for COI0520 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0520_across_subtidal.png
---
name: fig-nwgoa-COI0520-across-subtidal
---
Model-data comparison for COI0520 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0520_along_subtidal.png
---
name: fig-ciofs-COI0520-along-subtidal
---
Model-data comparison for COI0520 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0520_along_subtidal.png
---
name: fig-nwgoa-COI0520-along-subtidal
---
Model-data comparison for COI0520 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0520_speed_subtidal.png
---
name: fig-ciofs-COI0520-speed-subtidal
---
Model-data comparison for COI0520 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0520_speed_subtidal.png
---
name: fig-nwgoa-COI0520-speed-subtidal
---
Model-data comparison for COI0520 of horizontal speed
```


+++

## COI0521


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0521_across_subtidal.png
---
name: fig-ciofs-COI0521-across-subtidal
---
Model-data comparison for COI0521 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0521_across_subtidal.png
---
name: fig-nwgoa-COI0521-across-subtidal
---
Model-data comparison for COI0521 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0521_along_subtidal.png
---
name: fig-ciofs-COI0521-along-subtidal
---
Model-data comparison for COI0521 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0521_along_subtidal.png
---
name: fig-nwgoa-COI0521-along-subtidal
---
Model-data comparison for COI0521 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0521_speed_subtidal.png
---
name: fig-ciofs-COI0521-speed-subtidal
---
Model-data comparison for COI0521 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0521_speed_subtidal.png
---
name: fig-nwgoa-COI0521-speed-subtidal
---
Model-data comparison for COI0521 of horizontal speed
```


+++

## COI0522


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0522_across_subtidal.png
---
name: fig-ciofs-COI0522-across-subtidal
---
Model-data comparison for COI0522 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0522_across_subtidal.png
---
name: fig-nwgoa-COI0522-across-subtidal
---
Model-data comparison for COI0522 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0522_along_subtidal.png
---
name: fig-ciofs-COI0522-along-subtidal
---
Model-data comparison for COI0522 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0522_along_subtidal.png
---
name: fig-nwgoa-COI0522-along-subtidal
---
Model-data comparison for COI0522 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0522_speed_subtidal.png
---
name: fig-ciofs-COI0522-speed-subtidal
---
Model-data comparison for COI0522 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0522_speed_subtidal.png
---
name: fig-nwgoa-COI0522-speed-subtidal
---
Model-data comparison for COI0522 of horizontal speed
```


+++

## COI0523


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0523_across_subtidal.png
---
name: fig-ciofs-COI0523-across-subtidal
---
Model-data comparison for COI0523 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0523_across_subtidal.png
---
name: fig-nwgoa-COI0523-across-subtidal
---
Model-data comparison for COI0523 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0523_along_subtidal.png
---
name: fig-ciofs-COI0523-along-subtidal
---
Model-data comparison for COI0523 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0523_along_subtidal.png
---
name: fig-nwgoa-COI0523-along-subtidal
---
Model-data comparison for COI0523 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0523_speed_subtidal.png
---
name: fig-ciofs-COI0523-speed-subtidal
---
Model-data comparison for COI0523 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0523_speed_subtidal.png
---
name: fig-nwgoa-COI0523-speed-subtidal
---
Model-data comparison for COI0523 of horizontal speed
```


+++

## COI0524


+++

### Across-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0524_across_subtidal.png
---
name: fig-ciofs-COI0524-across-subtidal
---
Model-data comparison for COI0524 of across-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0524_across_subtidal.png
---
name: fig-nwgoa-COI0524-across-subtidal
---
Model-data comparison for COI0524 of across-channel velocity
```


+++

### Along-channel velocity: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0524_along_subtidal.png
---
name: fig-ciofs-COI0524-along-subtidal
---
Model-data comparison for COI0524 of along-channel velocity
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0524_along_subtidal.png
---
name: fig-nwgoa-COI0524-along-subtidal
---
Model-data comparison for COI0524 of along-channel velocity
```


+++

### Horizontal speed: tidally-filtered

+++

#### ciofs



```{figure} adcp_moored_noaa_coi_2005_ciofs/adcp_moored_noaa_coi_2005_COI0524_speed_subtidal.png
---
name: fig-ciofs-COI0524-speed-subtidal
---
Model-data comparison for COI0524 of horizontal speed
```


+++

#### nwgoa



```{figure} adcp_moored_noaa_coi_2005_nwgoa/adcp_moored_noaa_coi_2005_COI0524_speed_subtidal.png
---
name: fig-nwgoa-COI0524-speed-subtidal
---
Model-data comparison for COI0524 of horizontal speed
```
