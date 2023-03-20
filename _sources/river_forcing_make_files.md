---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import matplotlib.pyplot as plt

from create_river_roms import *
import os
from IPython.display import Code

plt.rc('font', size=16)
```

# Make monthly river forcing files for 1998–2018

```{code-cell} ipython3
base = "output/river"

def run_year(year):
    
        start, end = f"{year}-1-1T00", f"{year+1}-1-1T00"

        fname = pd.Timestamp(start).strftime("axiom.ciofs.river.%Y%m%d.nc")
        fname = f"{base}/{fname}"
        
        if not os.path.exists(fname) or not os.path.exists(fname.replace(".nc",".txt")):
            ds = create_river_forcing_file(start, end, ndays=7, skip_last=False)
            ds.to_netcdf(fname)
        
        print(Code(fname.replace(".nc",".txt")))

        
def plot_year(year):
    locs = f"{base}/axiom.ciofs.river.{year}*.nc"
    ds = xr.open_mfdataset(locs, concat_dim="time", combine='nested')
    ds = ds.swap_dims({"time": "river_time"})

    unique_inds = list(set([station_list_file.index(station_list_file[i]) for i in range(nrivers)]))
    labels = [station_list_file[i] for i in unique_inds]
    nrepeats = [station_list_file.count(station) for station in labels]
    abs(ds["river_transport"].isel(river=unique_inds)*nrepeats).plot.line(x="river_time", lw=3, figsize=(15,7));
    plt.legend(labels)

    ds["river_temp"].isel(s_rho=0, river=unique_inds).plot.line(x="river_time", lw=3, figsize=(15,7));
    plt.legend(labels)
```

## 1998

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 1998
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 1999

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 1999
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2000

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2000
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2001

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2001
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2002

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2002
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2003

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2003
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2004

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2004
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2005

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2005
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2006

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: true
tags: [hide-output]
---
year = 2006
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2007

```{code-cell} ipython3
:tags: [hide-output]

year = 2007
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2008

```{code-cell} ipython3
:tags: [hide-output]

year = 2008
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2009

```{code-cell} ipython3
:tags: [hide-output]

year = 2009
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2010

```{code-cell} ipython3
:tags: [hide-output]

year = 2010
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2011

```{code-cell} ipython3
:tags: [hide-output]

year = 2011
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2012

```{code-cell} ipython3
:tags: [hide-output]

year = 2012
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2013

```{code-cell} ipython3
:tags: [hide-output]

year = 2013
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2014

```{code-cell} ipython3
:tags: [hide-output]

year = 2014
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2015

```{code-cell} ipython3
:tags: [hide-output]

year = 2015
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2016

```{code-cell} ipython3
:tags: [hide-output]

year = 2016
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2017

```{code-cell} ipython3
:tags: [hide-output]

year = 2017
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

## 2018

```{code-cell} ipython3
:tags: [hide-output]

year = 2018
run_year(year)
```

```{code-cell} ipython3
plot_year(year)
```

```{code-cell} ipython3

```
