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

# Moorings (KBNERR): Kachemak Bay, Homer stations

* moorings_kbnerr_homer

See the full dataset page for more information: {ref}`page:moorings_kbnerr_homer`

+++

## Map of Moorings



````{div} full-width                
```{figure} map_of_moorings_kbnerr_homer.png
---
name: fig-map-moorings_kbnerr_homer
---
Map of moorings_kbnerr_homer data locations
```
````




+++

## Performance Summary

+++

### Sea water salinity: tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_homer_salt_subtidal.png
---
name: fig-overall-moorings_kbnerr_homer-salt-subtidal
---
Skill score for sea water salinity, tidally-filtered
```
````




+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_kbnerr_homer_salt_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_kbnerr_homer-salt-subtidal_subtract-monthly-mean
---
Skill score for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````




+++

### Sea surface height: mean subtracted, then tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_homer_ssh_subtract-mean_subtidal.png
---
name: fig-overall-moorings_kbnerr_homer-ssh-subtract-mean_subtidal
---
Skill score for sea surface height, mean subtracted, then tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_homer_temp_subtidal.png
---
name: fig-overall-moorings_kbnerr_homer-temp-subtidal
---
Skill score for sea water temperature, tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_kbnerr_homer_temp_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_kbnerr_homer-temp-subtidal_subtract-monthly-mean
---
Skill score for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````




+++

## homer-dolphin-surface-water-q


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_subtidal.png
---
name: fig-homer-dolphin-surface-water-q-salt-subtidal
---
Skill score by year for sea water salinity, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal-2008
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2008
```



````
`````

+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_subtidal_subtract-monthly-mean.png
---
name: fig-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean
---
Skill score by year for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_mean.png
---
name: fig-homer-dolphin-surface-water-q-salt
---
Sea water salinity averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-salt-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for homer-dolphin-surface-water-q of sea water salinity for 2008
```



````
`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_subtract-mean_subtidal.png
---
name: fig-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for homer-dolphin-surface-water-q of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_subtidal.png
---
name: fig-homer-dolphin-surface-water-q-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal-2008
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_subtidal_subtract-monthly-mean.png
---
name: fig-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_mean.png
---
name: fig-homer-dolphin-surface-water-q-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-homer-dolphin-surface-water-q-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for homer-dolphin-surface-water-q of sea water temperature for 2008
```



````
`````

+++

## nerrs_kach3wq


CIOFS: Data time range is 2012-05-31 to 2023-05-03 but model ends 2008-08-25.


NWGOA: Data time range is 2012-05-31 to 2023-05-03 but model ends 2009-01-01.


+++

## nerrs_kachdwq


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_salt_subtidal.png
---
name: fig-nerrs_kachdwq-salt-subtidal
---
Skill score by year for sea water salinity, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal-2003
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal-2004
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal-2005
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal-2006
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal-2007
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal-2003
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal-2004
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal-2005
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal-2006
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal-2007
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal-2008
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2008
```



````
`````

+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_salt_subtidal_subtract-monthly-mean.png
---
name: fig-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean
---
Skill score by year for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_salt_mean.png
---
name: fig-nerrs_kachdwq-salt
---
Sea water salinity averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_salt_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-salt-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for nerrs_kachdwq of sea water salinity for 2008
```



````
`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_ssh_subtract-mean_subtidal.png
---
name: fig-nerrs_kachdwq-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-ssh-subtract-mean_subtidal-2003
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-ssh-subtract-mean_subtidal-2003
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for nerrs_kachdwq of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_temp_subtidal.png
---
name: fig-nerrs_kachdwq-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal-2003
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal-2004
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal-2005
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal-2006
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal-2007
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal-2003
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal-2004
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal-2005
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal-2006
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal-2007
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal-2008
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_temp_subtidal_subtract-monthly-mean.png
---
name: fig-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_temp_mean.png
---
name: fig-nerrs_kachdwq-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_ciofs/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2003



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2003
```

##### 2004



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2004
```

##### 2005



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2005
```

##### 2006



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2006
```

##### 2007



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2007
```

##### 2008



```{figure} moorings_kbnerr_homer_nwgoa/moorings_kbnerr_homer_nerrs_kachdwq_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-nerrs_kachdwq-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for nerrs_kachdwq of sea water temperature for 2008
```



````
`````
