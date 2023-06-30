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

# CTD Profiles (NOAA): across Cook Inlet

* ctd_profiles_2005_noaa

See the full dataset page for more information: {ref}`page:ctd_profiles_2005_noaa`

+++

## Map of CTD Profiles



````{div} full-width                
```{figure} map_of_ctd_profiles_2005_noaa.png
---
name: fig-map-ctd_profiles_2005_noaa
---
Map of ctd_profiles_2005_noaa data locations
```
````




+++

## Performance Summary

+++

### Sea water salinity: 



````{div} full-width                
```{figure} ctd_profiles_2005_noaa_salt_nan.png
---
name: fig-overall-ctd_profiles_2005_noaa-salt-nan
---
Skill score for sea water salinity, 
```
````




+++

### Sea water temperature: 



````{div} full-width                
```{figure} ctd_profiles_2005_noaa_temp_nan.png
---
name: fig-overall-ctd_profiles_2005_noaa-temp-nan
---
Skill score for sea water temperature, 
```
````




+++

## 501


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_501_salt.png
---
name: fig-ciofs-501-salt-nan
---
Model-data comparison for 501 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_501_salt.png
---
name: fig-nwgoa-501-salt-nan
---
Model-data comparison for 501 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_501_temp.png
---
name: fig-ciofs-501-temp-nan
---
Model-data comparison for 501 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_501_temp.png
---
name: fig-nwgoa-501-temp-nan
---
Model-data comparison for 501 of sea water temperature
```


+++

## 502


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_502_salt.png
---
name: fig-ciofs-502-salt-nan
---
Model-data comparison for 502 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_502_salt.png
---
name: fig-nwgoa-502-salt-nan
---
Model-data comparison for 502 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_502_temp.png
---
name: fig-ciofs-502-temp-nan
---
Model-data comparison for 502 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_502_temp.png
---
name: fig-nwgoa-502-temp-nan
---
Model-data comparison for 502 of sea water temperature
```


+++

## 503


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_503_salt.png
---
name: fig-ciofs-503-salt-nan
---
Model-data comparison for 503 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_503_salt.png
---
name: fig-nwgoa-503-salt-nan
---
Model-data comparison for 503 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_503_temp.png
---
name: fig-ciofs-503-temp-nan
---
Model-data comparison for 503 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_503_temp.png
---
name: fig-nwgoa-503-temp-nan
---
Model-data comparison for 503 of sea water temperature
```


+++

## 504


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_504_salt.png
---
name: fig-ciofs-504-salt-nan
---
Model-data comparison for 504 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_504_salt.png
---
name: fig-nwgoa-504-salt-nan
---
Model-data comparison for 504 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_504_temp.png
---
name: fig-ciofs-504-temp-nan
---
Model-data comparison for 504 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_504_temp.png
---
name: fig-nwgoa-504-temp-nan
---
Model-data comparison for 504 of sea water temperature
```


+++

## 505


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_505_salt.png
---
name: fig-ciofs-505-salt-nan
---
Model-data comparison for 505 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_505_salt.png
---
name: fig-nwgoa-505-salt-nan
---
Model-data comparison for 505 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_505_temp.png
---
name: fig-ciofs-505-temp-nan
---
Model-data comparison for 505 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_505_temp.png
---
name: fig-nwgoa-505-temp-nan
---
Model-data comparison for 505 of sea water temperature
```


+++

## 506


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_506_salt.png
---
name: fig-ciofs-506-salt-nan
---
Model-data comparison for 506 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_506_salt.png
---
name: fig-nwgoa-506-salt-nan
---
Model-data comparison for 506 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_506_temp.png
---
name: fig-ciofs-506-temp-nan
---
Model-data comparison for 506 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_506_temp.png
---
name: fig-nwgoa-506-temp-nan
---
Model-data comparison for 506 of sea water temperature
```


+++

## 507


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_507_salt.png
---
name: fig-ciofs-507-salt-nan
---
Model-data comparison for 507 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_507_salt.png
---
name: fig-nwgoa-507-salt-nan
---
Model-data comparison for 507 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_507_temp.png
---
name: fig-ciofs-507-temp-nan
---
Model-data comparison for 507 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_507_temp.png
---
name: fig-nwgoa-507-temp-nan
---
Model-data comparison for 507 of sea water temperature
```


+++

## 508


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_508_salt.png
---
name: fig-ciofs-508-salt-nan
---
Model-data comparison for 508 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_508_salt.png
---
name: fig-nwgoa-508-salt-nan
---
Model-data comparison for 508 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_508_temp.png
---
name: fig-ciofs-508-temp-nan
---
Model-data comparison for 508 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_508_temp.png
---
name: fig-nwgoa-508-temp-nan
---
Model-data comparison for 508 of sea water temperature
```


+++

## 509


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_509_salt.png
---
name: fig-ciofs-509-salt-nan
---
Model-data comparison for 509 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_509_salt.png
---
name: fig-nwgoa-509-salt-nan
---
Model-data comparison for 509 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_509_temp.png
---
name: fig-ciofs-509-temp-nan
---
Model-data comparison for 509 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_509_temp.png
---
name: fig-nwgoa-509-temp-nan
---
Model-data comparison for 509 of sea water temperature
```


+++

## 510


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_510_salt.png
---
name: fig-ciofs-510-salt-nan
---
Model-data comparison for 510 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_510_salt.png
---
name: fig-nwgoa-510-salt-nan
---
Model-data comparison for 510 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_510_temp.png
---
name: fig-ciofs-510-temp-nan
---
Model-data comparison for 510 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_510_temp.png
---
name: fig-nwgoa-510-temp-nan
---
Model-data comparison for 510 of sea water temperature
```


+++

## 511


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_511_salt.png
---
name: fig-ciofs-511-salt-nan
---
Model-data comparison for 511 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_511_salt.png
---
name: fig-nwgoa-511-salt-nan
---
Model-data comparison for 511 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_511_temp.png
---
name: fig-ciofs-511-temp-nan
---
Model-data comparison for 511 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_511_temp.png
---
name: fig-nwgoa-511-temp-nan
---
Model-data comparison for 511 of sea water temperature
```


+++

## 512


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_512_salt.png
---
name: fig-ciofs-512-salt-nan
---
Model-data comparison for 512 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_512_salt.png
---
name: fig-nwgoa-512-salt-nan
---
Model-data comparison for 512 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_512_temp.png
---
name: fig-ciofs-512-temp-nan
---
Model-data comparison for 512 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_512_temp.png
---
name: fig-nwgoa-512-temp-nan
---
Model-data comparison for 512 of sea water temperature
```


+++

## 513


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_513_salt.png
---
name: fig-ciofs-513-salt-nan
---
Model-data comparison for 513 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_513_salt.png
---
name: fig-nwgoa-513-salt-nan
---
Model-data comparison for 513 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_513_temp.png
---
name: fig-ciofs-513-temp-nan
---
Model-data comparison for 513 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_513_temp.png
---
name: fig-nwgoa-513-temp-nan
---
Model-data comparison for 513 of sea water temperature
```


+++

## 514


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_514_salt.png
---
name: fig-ciofs-514-salt-nan
---
Model-data comparison for 514 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_514_salt.png
---
name: fig-nwgoa-514-salt-nan
---
Model-data comparison for 514 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_514_temp.png
---
name: fig-ciofs-514-temp-nan
---
Model-data comparison for 514 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_514_temp.png
---
name: fig-nwgoa-514-temp-nan
---
Model-data comparison for 514 of sea water temperature
```


+++

## 515


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_515_salt.png
---
name: fig-ciofs-515-salt-nan
---
Model-data comparison for 515 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_515_salt.png
---
name: fig-nwgoa-515-salt-nan
---
Model-data comparison for 515 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_515_temp.png
---
name: fig-ciofs-515-temp-nan
---
Model-data comparison for 515 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_515_temp.png
---
name: fig-nwgoa-515-temp-nan
---
Model-data comparison for 515 of sea water temperature
```


+++

## 516


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_516_salt.png
---
name: fig-ciofs-516-salt-nan
---
Model-data comparison for 516 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_516_salt.png
---
name: fig-nwgoa-516-salt-nan
---
Model-data comparison for 516 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_516_temp.png
---
name: fig-ciofs-516-temp-nan
---
Model-data comparison for 516 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_516_temp.png
---
name: fig-nwgoa-516-temp-nan
---
Model-data comparison for 516 of sea water temperature
```


+++

## 517


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_517_salt.png
---
name: fig-ciofs-517-salt-nan
---
Model-data comparison for 517 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_517_salt.png
---
name: fig-nwgoa-517-salt-nan
---
Model-data comparison for 517 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_517_temp.png
---
name: fig-ciofs-517-temp-nan
---
Model-data comparison for 517 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_517_temp.png
---
name: fig-nwgoa-517-temp-nan
---
Model-data comparison for 517 of sea water temperature
```


+++

## 518


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_518_salt.png
---
name: fig-ciofs-518-salt-nan
---
Model-data comparison for 518 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_518_salt.png
---
name: fig-nwgoa-518-salt-nan
---
Model-data comparison for 518 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_518_temp.png
---
name: fig-ciofs-518-temp-nan
---
Model-data comparison for 518 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_518_temp.png
---
name: fig-nwgoa-518-temp-nan
---
Model-data comparison for 518 of sea water temperature
```


+++

## 519


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_519_salt.png
---
name: fig-ciofs-519-salt-nan
---
Model-data comparison for 519 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_519_salt.png
---
name: fig-nwgoa-519-salt-nan
---
Model-data comparison for 519 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_519_temp.png
---
name: fig-ciofs-519-temp-nan
---
Model-data comparison for 519 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_519_temp.png
---
name: fig-nwgoa-519-temp-nan
---
Model-data comparison for 519 of sea water temperature
```


+++

## 520


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_520_salt.png
---
name: fig-ciofs-520-salt-nan
---
Model-data comparison for 520 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_520_salt.png
---
name: fig-nwgoa-520-salt-nan
---
Model-data comparison for 520 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_520_temp.png
---
name: fig-ciofs-520-temp-nan
---
Model-data comparison for 520 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_520_temp.png
---
name: fig-nwgoa-520-temp-nan
---
Model-data comparison for 520 of sea water temperature
```


+++

## 521


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_521_salt.png
---
name: fig-ciofs-521-salt-nan
---
Model-data comparison for 521 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_521_salt.png
---
name: fig-nwgoa-521-salt-nan
---
Model-data comparison for 521 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_521_temp.png
---
name: fig-ciofs-521-temp-nan
---
Model-data comparison for 521 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_521_temp.png
---
name: fig-nwgoa-521-temp-nan
---
Model-data comparison for 521 of sea water temperature
```


+++

## 522


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_522_salt.png
---
name: fig-ciofs-522-salt-nan
---
Model-data comparison for 522 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_522_salt.png
---
name: fig-nwgoa-522-salt-nan
---
Model-data comparison for 522 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_522_temp.png
---
name: fig-ciofs-522-temp-nan
---
Model-data comparison for 522 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_522_temp.png
---
name: fig-nwgoa-522-temp-nan
---
Model-data comparison for 522 of sea water temperature
```


+++

## 523


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_523_salt.png
---
name: fig-ciofs-523-salt-nan
---
Model-data comparison for 523 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_523_salt.png
---
name: fig-nwgoa-523-salt-nan
---
Model-data comparison for 523 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_523_temp.png
---
name: fig-ciofs-523-temp-nan
---
Model-data comparison for 523 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_523_temp.png
---
name: fig-nwgoa-523-temp-nan
---
Model-data comparison for 523 of sea water temperature
```


+++

## 524


+++

### Sea water salinity: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_524_salt.png
---
name: fig-ciofs-524-salt-nan
---
Model-data comparison for 524 of sea water salinity
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_524_salt.png
---
name: fig-nwgoa-524-salt-nan
---
Model-data comparison for 524 of sea water salinity
```


+++

### Sea water temperature: 

+++

#### ciofs



```{figure} ctd_profiles_2005_noaa_ciofs/ctd_profiles_2005_noaa_524_temp.png
---
name: fig-ciofs-524-temp-nan
---
Model-data comparison for 524 of sea water temperature
```


+++

#### nwgoa



```{figure} ctd_profiles_2005_noaa_nwgoa/ctd_profiles_2005_noaa_524_temp.png
---
name: fig-nwgoa-524-temp-nan
---
Model-data comparison for 524 of sea water temperature
```
