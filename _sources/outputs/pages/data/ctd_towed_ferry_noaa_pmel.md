---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
---

```{code-cell}
import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
```

# Towed CTD on ferry at nominal 4m depth

* CTD Towed 2004-2008 Ferry in-line - NOAA PMEL
* ctd_towed_ferry_noaa_pmel
* Continuous 2004 to 2008, 5min sampling frequency


An oceanographic monitoring system aboard the Alaska Marine Highway System ferry Tustumena operated for four years in the Alaska Coastal Current (ACC) with funding from the Exxon Valdez Oil Spill Trustee Council's Gulf Ecosystem Monitoring Program, the North Pacific Research Board and the National Oceanic and Atmospheric Administration. An electronic public display aboard the ferry educated passengers about the local oceanography and mapped the ferry's progress. Sampling water at 4 m, the underway system measured: (1) temperature and salinity (used in the present report), and (2) nitrate,
(3) chlorophyll fluorescence, (4) colored dissolved organic matter fluorescence, and (5) optical beam transmittance (not used in report).

NORTH PACIFIC RESEARCH BOARD PROJECT FINAL REPORT
Alaskan Ferry Oceanographic Monitoring in the Gulf of Alaska
NPRB Project 707 Final Report
Edward D. Cokelet and Calvin W. Mordy.
https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Final_Report_NPRB_0707.pdf

Exxon Valdez Oil Spill Gulf Ecosystem
Monitoring and Research Project Final Report
Biophysical Observations Aboard Alaska Marine Highway System Ferries
Gulf Ecosystem Monitoring and Research Project 040699
Final Report
Edward D. Cokelet, Calvin W. Mordy, Antonio J. Jenkins, W. Scott Pegau
https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/data/0-data/Final_Report_GEM_040699.pdf

Archive: https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.nodc%3A0070122/html

![pic](https://www.nodc.noaa.gov/archive/arc0031/0070122/1.1/about/0070122_map.jpg)


The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_ferry_noaa_pmel"))
```

## Map of Towed CTD Paths
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_ferry_noaa_pmel")("ctd_towed_ferry_noaa_pmel")
    
```

## 2004

+++

2004-09
        

```{code-cell}
cat['2004-09'].plot.salt() + cat['2004-09'].plot.temp()
```

2004-10
        

```{code-cell}
cat['2004-10'].plot.salt() + cat['2004-10'].plot.temp()
```

2004-11
        

```{code-cell}
cat['2004-11'].plot.salt() + cat['2004-11'].plot.temp()
```

2004-12
        

```{code-cell}
cat['2004-12'].plot.salt() + cat['2004-12'].plot.temp()
```

## 2005

+++

2005-01
        

```{code-cell}
cat['2005-01'].plot.salt() + cat['2005-01'].plot.temp()
```

2005-02
        

```{code-cell}
cat['2005-02'].plot.salt() + cat['2005-02'].plot.temp()
```

2005-03
        

```{code-cell}
cat['2005-03'].plot.salt() + cat['2005-03'].plot.temp()
```

2005-04
        

```{code-cell}
cat['2005-04'].plot.salt() + cat['2005-04'].plot.temp()
```

2005-05
        

```{code-cell}
cat['2005-05'].plot.salt() + cat['2005-05'].plot.temp()
```

2005-06
        

```{code-cell}
cat['2005-06'].plot.salt() + cat['2005-06'].plot.temp()
```

2005-07
        

```{code-cell}
cat['2005-07'].plot.salt() + cat['2005-07'].plot.temp()
```

2005-08
        

```{code-cell}
cat['2005-08'].plot.salt() + cat['2005-08'].plot.temp()
```

2005-09
        

```{code-cell}
cat['2005-09'].plot.salt() + cat['2005-09'].plot.temp()
```

2005-10
        

```{code-cell}
cat['2005-10'].plot.salt() + cat['2005-10'].plot.temp()
```

2005-11
        

```{code-cell}
cat['2005-11'].plot.salt() + cat['2005-11'].plot.temp()
```

## 2006

+++

2006-05
        

```{code-cell}
cat['2006-05'].plot.salt() + cat['2006-05'].plot.temp()
```

2006-06
        

```{code-cell}
cat['2006-06'].plot.salt() + cat['2006-06'].plot.temp()
```

2006-07
        

```{code-cell}
cat['2006-07'].plot.salt() + cat['2006-07'].plot.temp()
```

2006-08
        

```{code-cell}
cat['2006-08'].plot.salt() + cat['2006-08'].plot.temp()
```

2006-09
        

```{code-cell}
cat['2006-09'].plot.salt() + cat['2006-09'].plot.temp()
```

2006-10
        

```{code-cell}
cat['2006-10'].plot.salt() + cat['2006-10'].plot.temp()
```

2006-11
        

```{code-cell}
cat['2006-11'].plot.salt() + cat['2006-11'].plot.temp()
```

2006-12
        

```{code-cell}
cat['2006-12'].plot.salt() + cat['2006-12'].plot.temp()
```

## 2007

+++

2007-01
        

```{code-cell}
cat['2007-01'].plot.salt() + cat['2007-01'].plot.temp()
```

2007-02
        

```{code-cell}
cat['2007-02'].plot.salt() + cat['2007-02'].plot.temp()
```

2007-03
        

```{code-cell}
cat['2007-03'].plot.salt() + cat['2007-03'].plot.temp()
```

2007-04
        

```{code-cell}
cat['2007-04'].plot.salt() + cat['2007-04'].plot.temp()
```

2007-05
        

```{code-cell}
cat['2007-05'].plot.salt() + cat['2007-05'].plot.temp()
```

2007-06
        

```{code-cell}
cat['2007-06'].plot.salt() + cat['2007-06'].plot.temp()
```

2007-07
        

```{code-cell}
cat['2007-07'].plot.salt() + cat['2007-07'].plot.temp()
```

2007-08
        

```{code-cell}
cat['2007-08'].plot.salt() + cat['2007-08'].plot.temp()
```

2007-09
        

```{code-cell}
cat['2007-09'].plot.salt() + cat['2007-09'].plot.temp()
```

2007-10
        

```{code-cell}
cat['2007-10'].plot.salt() + cat['2007-10'].plot.temp()
```

## 2008

+++

2008-03
        

```{code-cell}
cat['2008-03'].plot.salt() + cat['2008-03'].plot.temp()
```

2008-04
        

```{code-cell}
cat['2008-04'].plot.salt() + cat['2008-04'].plot.temp()
```

2008-05
        

```{code-cell}
cat['2008-05'].plot.salt() + cat['2008-05'].plot.temp()
```

2008-06
        

```{code-cell}
cat['2008-06'].plot.salt() + cat['2008-06'].plot.temp()
```

2008-07
        

```{code-cell}
cat['2008-07'].plot.salt() + cat['2008-07'].plot.temp()
```

2008-08
        

```{code-cell}
cat['2008-08'].plot.salt() + cat['2008-08'].plot.temp()
```

2008-09
        

```{code-cell}
cat['2008-09'].plot.salt() + cat['2008-09'].plot.temp()
```

2008-10
        

```{code-cell}
cat['2008-10'].plot.salt() + cat['2008-10'].plot.temp()
```

2008-11
        

```{code-cell}
cat['2008-11'].plot.salt() + cat['2008-11'].plot.temp()
```
