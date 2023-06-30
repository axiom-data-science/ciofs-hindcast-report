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

See the full dataset page for more information: {ref}`page:moorings_noaa`

+++

## Map of Moorings



````{div} full-width                
```{figure} map_of_moorings_noaa.png
---
name: fig-map-moorings_noaa
---
Map of moorings_noaa data locations
```
````




+++

## Performance Summary



Overall, the CIOFS model something something, as shown in {numref}`Figure {number}<fig-overall-moorings_noaa-ssh-subtract-mean>`.



+++

### Sea surface height: mean subtracted



````{div} full-width                
```{figure} moorings_noaa_ssh_subtract-mean.png
---
name: fig-overall-moorings_noaa-ssh-subtract-mean
---
Skill score for sea surface height, mean subtracted
```
````




+++

### Sea surface height: mean subtracted, then tidally-filtered



````{div} full-width                
```{figure} moorings_noaa_ssh_subtract-mean_subtidal.png
---
name: fig-overall-moorings_noaa-ssh-subtract-mean_subtidal
---
Skill score for sea surface height, mean subtracted, then tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered



````{div} full-width                
```{figure} moorings_noaa_temp_subtidal.png
---
name: fig-overall-moorings_noaa-temp-subtidal
---
Skill score for sea water temperature, tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_noaa_temp_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_noaa-temp-subtidal_subtract-monthly-mean
---
Skill score for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````




+++

## boulder-point


+++

### Sea surface height: mean subtracted

+++

#### ciofs



```{figure} moorings_noaa_ciofs/moorings_noaa_boulder-point_ssh_subtract-mean.png
---
name: fig-ciofs-boulder-point-ssh-subtract-mean
---
Model-data comparison for boulder-point of sea surface height
```


+++

#### nwgoa



```{figure} moorings_noaa_nwgoa/moorings_noaa_boulder-point_ssh_subtract-mean.png
---
name: fig-nwgoa-boulder-point-ssh-subtract-mean
---
Model-data comparison for boulder-point of sea surface height
```


+++

## geese-island-gps-tide-buoy


CIOFS: Data time range is 2016-06-25 to 2016-07-30 but model ends 2008-08-25.


NWGOA: Data time range is 2016-06-25 to 2016-07-30 but model ends 2009-01-01.


+++

## noaa_nos_co_ops_9455500


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455500_ssh_subtract-mean_subtidal.png
---
name: fig-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 1999
```

##### 2000



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2000
```

##### 2001



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2001
```

##### 2002



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2002
```

##### 2003



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2003
```

##### 2004



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2004
```

##### 2005



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2005
```

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 1999
```

##### 2000



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2000
```

##### 2001



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2001
```

##### 2002



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2002
```

##### 2003



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2003
```

##### 2004



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2004
```

##### 2005



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2005
```

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455500_temp_subtidal.png
---
name: fig-noaa_nos_co_ops_9455500-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal-2008
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455500_temp_subtidal_subtract-monthly-mean.png
---
name: fig-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455500_temp_mean.png
---
name: fig-noaa_nos_co_ops_9455500-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-1999
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2000
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2001
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2002
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-1999
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2000
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2001
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2002
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455500-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for noaa_nos_co_ops_9455500 of sea water temperature for 2008
```



````
`````

+++

## noaa_nos_co_ops_9455595


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455595_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455595-ssh-subtract-mean_subtidal
---
Model-data comparison for noaa_nos_co_ops_9455595 of sea surface height
```


+++

## noaa_nos_co_ops_9455920


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455920_ssh_subtract-mean_subtidal.png
---
name: fig-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 1999
```

##### 2000



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2000
```

##### 2001



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2001
```

##### 2002



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2002
```

##### 2003



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2003
```

##### 2004



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2004
```

##### 2005



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2005
```

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 1999
```

##### 2000



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2000
```

##### 2001



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2001
```

##### 2002



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2002
```

##### 2003



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2003
```

##### 2004



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2004
```

##### 2005



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2005
```

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455920_temp_subtidal.png
---
name: fig-noaa_nos_co_ops_9455920-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-1999
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2000
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2001
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2002
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2003
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2004
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2005
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal-2008
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455920_temp_subtidal_subtract-monthly-mean.png
---
name: fig-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455920_temp_mean.png
---
name: fig-noaa_nos_co_ops_9455920-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-1999
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2000
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2001
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2002
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 1999



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-1999
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 1999
```

##### 2000



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2000
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2000
```

##### 2001



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2001
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2001
```

##### 2002



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2002
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2002
```

##### 2003



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2003
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2003
```

##### 2004



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2004
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2004
```

##### 2005



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2005
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2005
```

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9455920-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for noaa_nos_co_ops_9455920 of sea water temperature for 2008
```



````
`````

+++

## noaa_nos_co_ops_9457804


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9457804_ssh_subtract-mean_subtidal.png
---
name: fig-noaa_nos_co_ops_9457804-ssh-subtract-mean_subtidal
---
Skill score by year for sea surface height, mean subtracted, then tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9457804-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea surface height for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9457804-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea surface height for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-ssh-subtract-mean_subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea surface height for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-ssh-subtract-mean_subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea surface height for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-ssh-subtract-mean_subtidal-2008
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea surface height for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9457804_temp_subtidal.png
---
name: fig-noaa_nos_co_ops_9457804-temp-subtidal
---
Skill score by year for sea water temperature, tidally-filtered
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9457804-temp-subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-ciofs-noaa_nos_co_ops_9457804-temp-subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-temp-subtidal-2006
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-temp-subtidal-2007
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01_subtidal.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-temp-subtidal-2008
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2008
```



````
`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9457804_temp_subtidal_subtract-monthly-mean.png
---
name: fig-noaa_nos_co_ops_9457804-temp-subtidal_subtract-monthly-mean
---
Skill score by year for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````


+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9457804_temp_mean.png
---
name: fig-noaa_nos_co_ops_9457804-temp
---
Sea water temperature averaged monthly across data range with variation across years included.
```
````


+++

#### ciofs



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2006



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9457804-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_ciofs/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-noaa_nos_co_ops_9457804-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2007
```



````
`````

+++

#### nwgoa



`````{div} full-width 
````{dropdown} Comparison plots by year

##### 2006



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-temp-subtidal_subtract-monthly-mean-2006
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2006
```

##### 2007



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-temp-subtidal_subtract-monthly-mean-2007
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2007
```

##### 2008



```{figure} moorings_noaa_nwgoa/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-noaa_nos_co_ops_9457804-temp-subtidal_subtract-monthly-mean-2008
---
Model-data comparison for noaa_nos_co_ops_9457804 of sea water temperature for 2008
```



````
`````

+++

## noaa_nos_co_ops_kdaa2


CIOFS: Data time range is 2018-03-03 to 2023-06-28 but model ends 2008-08-25.


NWGOA: Data time range is 2018-03-03 to 2023-06-28 but model ends 2009-01-01.


+++

## old-harbor-1


CIOFS: Data time range is 2014-09-20 to 2018-08-27 but model ends 2008-08-25.


NWGOA: Data time range is 2014-09-20 to 2018-08-27 but model ends 2009-01-01.


+++

## sitkalidak-island-gps-tide-bu


CIOFS: Data time range is 2016-06-25 to 2016-07-27 but model ends 2008-08-25.


NWGOA: Data time range is 2016-06-25 to 2016-07-27 but model ends 2009-01-01.


+++

## wmo_46077


CIOFS: Data time range is 2017-06-14 to 2023-06-28 but model ends 2008-08-25.


NWGOA: Data time range is 2017-06-14 to 2023-06-28 but model ends 2009-01-01.
