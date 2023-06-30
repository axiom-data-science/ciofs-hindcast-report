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

# Moorings (KBNERR): Kachemak Bay: Bear Cove, Seldovia

* moorings_kbnerr_bear_cove_seldovia

See the full dataset page for more information: {ref}`page:moorings_kbnerr_bear_cove_seldovia`

+++

## Map of Moorings



````{div} full-width                
```{figure} map_of_moorings_kbnerr_bear_cove_seldovia.png
---
name: fig-map-moorings_kbnerr_bear_cove_seldovia
---
Map of moorings_kbnerr_bear_cove_seldovia data locations
```
````




+++

## Performance Summary



Overall, the salinity from the CIOFS model demonstrates much less high frequency variability than the NWGOA model as shown in (update reference) {numref}`Figure {number}<fig-overall-moorings_noaa-ssh-subtract-mean>`.



+++

### Sea water salinity: tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_salt_subtidal.png
---
name: fig-overall-moorings_kbnerr_bear_cove_seldovia-salt-subtidal
---
Skill score for sea water salinity, tidally-filtered
```
````




+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_salt_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_kbnerr_bear_cove_seldovia-salt-subtidal_subtract-monthly-mean
---
Skill score for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````




+++

### Sea surface height: mean subtracted, then tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_ssh_subtract-mean_subtidal.png
---
name: fig-overall-moorings_kbnerr_bear_cove_seldovia-ssh-subtract-mean_subtidal
---
Skill score for sea surface height, mean subtracted, then tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_temp_subtidal.png
---
name: fig-overall-moorings_kbnerr_bear_cove_seldovia-temp-subtidal
---
Skill score for sea water temperature, tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_temp_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_kbnerr_bear_cove_seldovia-temp-subtidal_subtract-monthly-mean
---
Skill score for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````




+++

## cdmo_nerrs_bearcove


CIOFS: Data time range is 2015-05-05 to 2015-11-20 but model ends 2008-08-25.


NWGOA: Data time range is 2015-05-05 to 2015-11-20 but model ends 2009-01-01.


+++

## nerrs_kacsdwq


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_subtidal.png
---
name: fig-nerrs_kacsdwq-salt-subtidal
---
Skill score by year for sea water salinity, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal-2004
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal-2005
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal-2006
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal-2007
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal-2004
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal-2005
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal-2006
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal-2007
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal-2008
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2008
```



````
`````

+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_subtidal_subtract-monthly-mean.png
---
name: fig-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean
---
Skill score by year for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_mean.png
---
name: fig-nerrs_kacsdwq-salt
---
Sea water salinity averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_salt_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-salt-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for nerrs_kacsdwq of sea water salinity for 2008
```



````
`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_subtract-mean_subtidal.png
---
name: fig-nerrs_kacsdwq-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for nerrs_kacsdwq of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_subtidal.png
---
name: fig-nerrs_kacsdwq-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal-2004
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal-2005
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal-2006
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal-2007
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal-2004
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal-2005
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal-2006
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal-2007
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal-2008
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_subtidal_subtract-monthly-mean.png
---
name: fig-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_mean.png
---
name: fig-nerrs_kacsdwq-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsdwq-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for nerrs_kacsdwq of sea water temperature for 2008
```



````
`````

+++

## nerrs_kacsswq


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_subtidal.png
---
name: fig-nerrs_kacsswq-salt-subtidal
---
Skill score by year for sea water salinity, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal-2004
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal-2005
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal-2006
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal-2007
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal-2004
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal-2005
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal-2006
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal-2007
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal-2008
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2008
```



````
`````

+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_subtidal_subtract-monthly-mean.png
---
name: fig-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean
---
Skill score by year for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_mean.png
---
name: fig-nerrs_kacsswq-salt
---
Sea water salinity averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_salt_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-salt-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for nerrs_kacsswq of sea water salinity for 2008
```



````
`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_subtract-mean_subtidal.png
---
name: fig-nerrs_kacsswq-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for nerrs_kacsswq of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_subtidal.png
---
name: fig-nerrs_kacsswq-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal-2004
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal-2005
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal-2006
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal-2007
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal-2004
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal-2005
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal-2006
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal-2007
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal-2008
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_subtidal_subtract-monthly-mean.png
---
name: fig-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_mean.png
---
name: fig-nerrs_kacsswq-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_ciofs/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_bear_cove_seldovia_nwgoa/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsswq_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kacsswq-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for nerrs_kacsswq of sea water temperature for 2008
```



````
`````
