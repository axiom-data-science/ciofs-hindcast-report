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

# Moorings (KBNERR): Historical, Kachemak Bay

* moorings_kbnerr_historical

See the full dataset page for more information: {ref}`page:moorings_kbnerr_historical`

+++

## Map of Moorings



````{div} full-width                
```{figure} map_of_moorings_kbnerr_historical.png
---
name: fig-map-moorings_kbnerr_historical
---
Map of moorings_kbnerr_historical data locations
```
````




+++

## Performance Summary

+++

### Sea water salinity: tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_historical_salt_subtidal.png
---
name: fig-overall-moorings_kbnerr_historical-salt-subtidal
---
Skill score for sea water salinity, tidally-filtered
```
````




+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_kbnerr_historical_salt_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_kbnerr_historical-salt-subtidal_subtract-monthly-mean
---
Skill score for sea water salinity, tidally-filtered, then monthly mean from data subtracted
```
````




+++

### Sea water temperature: tidally-filtered



````{div} full-width                
```{figure} moorings_kbnerr_historical_temp_subtidal.png
---
name: fig-overall-moorings_kbnerr_historical-temp-subtidal
---
Skill score for sea water temperature, tidally-filtered
```
````




+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted



````{div} full-width                
```{figure} moorings_kbnerr_historical_temp_subtidal_subtract-monthly-mean.png
---
name: fig-overall-moorings_kbnerr_historical-temp-subtidal_subtract-monthly-mean
---
Skill score for sea water temperature, tidally-filtered, then monthly mean from data subtracted
```
````




+++

## kacbcwq


+++

### Sea water salinity: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: fig-ciofs-kacbcwq-salt-subtidal
---
Model-data comparison for kacbcwq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: fig-nwgoa-kacbcwq-salt-subtidal
---
Model-data comparison for kacbcwq of sea water salinity
```


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-kacbcwq-salt-subtidal_subtract-monthly-mean
---
Model-data comparison for kacbcwq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-kacbcwq-salt-subtidal_subtract-monthly-mean
---
Model-data comparison for kacbcwq of sea water salinity
```


+++

### Sea water temperature: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-ciofs-kacbcwq-temp-subtidal
---
Model-data comparison for kacbcwq of sea water temperature
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-nwgoa-kacbcwq-temp-subtidal
---
Model-data comparison for kacbcwq of sea water temperature
```


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-kacbcwq-temp-subtidal_subtract-monthly-mean
---
Model-data comparison for kacbcwq of sea water temperature
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-kacbcwq-temp-subtidal_subtract-monthly-mean
---
Model-data comparison for kacbcwq of sea water temperature
```


+++

## kacdlwq


+++

### Sea water salinity: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacdlwq_salt_subtidal.png
---
name: fig-ciofs-kacdlwq-salt-subtidal
---
Model-data comparison for kacdlwq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacdlwq_salt_subtidal.png
---
name: fig-nwgoa-kacdlwq-salt-subtidal
---
Model-data comparison for kacdlwq of sea water salinity
```


+++

### Sea water temperature: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacdlwq_temp_subtidal.png
---
name: fig-ciofs-kacdlwq-temp-subtidal
---
Model-data comparison for kacdlwq of sea water temperature
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacdlwq_temp_subtidal.png
---
name: fig-nwgoa-kacdlwq-temp-subtidal
---
Model-data comparison for kacdlwq of sea water temperature
```


+++

## kachowq


+++

### Sea water salinity: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01_subtidal.png
---
name: fig-ciofs-kachowq-salt-subtidal
---
Model-data comparison for kachowq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01_subtidal.png
---
name: fig-nwgoa-kachowq-salt-subtidal
---
Model-data comparison for kachowq of sea water salinity
```


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-kachowq-salt-subtidal_subtract-monthly-mean
---
Model-data comparison for kachowq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-kachowq-salt-subtidal_subtract-monthly-mean
---
Model-data comparison for kachowq of sea water salinity
```


+++

### Sea water temperature: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01_subtidal.png
---
name: fig-ciofs-kachowq-temp-subtidal
---
Model-data comparison for kachowq of sea water temperature
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01_subtidal.png
---
name: fig-nwgoa-kachowq-temp-subtidal
---
Model-data comparison for kachowq of sea water temperature
```


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-kachowq-temp-subtidal_subtract-monthly-mean
---
Model-data comparison for kachowq of sea water temperature
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-kachowq-temp-subtidal_subtract-monthly-mean
---
Model-data comparison for kachowq of sea water temperature
```


+++

## kacpgwq


+++

### Sea water salinity: tidally-filtered

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: fig-ciofs-kacpgwq-salt-subtidal
---
Model-data comparison for kacpgwq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: fig-nwgoa-kacpgwq-salt-subtidal
---
Model-data comparison for kacpgwq of sea water salinity
```


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++

#### ciofs



```{figure} moorings_kbnerr_historical_ciofs/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-ciofs-kacpgwq-salt-subtidal_subtract-monthly-mean
---
Model-data comparison for kacpgwq of sea water salinity
```


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-kacpgwq-salt-subtidal_subtract-monthly-mean
---
Model-data comparison for kacpgwq of sea water salinity
```


+++

### Sea water temperature: tidally-filtered

+++

#### ciofs


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacpgwq_temp_2002-01-01_2003-01-01_subtidal.png
---
name: fig-nwgoa-kacpgwq-temp-subtidal
---
Model-data comparison for kacpgwq of sea water temperature
```


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++

#### ciofs


+++

#### nwgoa



```{figure} moorings_kbnerr_historical_nwgoa/moorings_kbnerr_historical_kacpgwq_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: fig-nwgoa-kacpgwq-temp-subtidal_subtract-monthly-mean
---
Model-data comparison for kacpgwq of sea water temperature
```


+++

## kacsewq
