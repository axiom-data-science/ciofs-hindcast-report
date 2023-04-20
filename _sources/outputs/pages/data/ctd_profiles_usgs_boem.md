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

# Single CTD profiles across Cook Inlet

* CTD profiles - USGS BOEM
* ctd_profiles_usgs_boem
* One-off CTD profiles from 2016 to 2021 in July

USGS Cook Inlet fish and bird survey CTD profiles.
    
CTD profiles collected in Cook Inlet from 2016-2021 by Mayumi Arimitsu as part of BOEM sponsored research on fish and bird distributions in Cook Inlet. The profiles are collected in July for the years 2016-2021.

The scientific project is described here: https://www.usgs.gov/centers/alaska-science-center/science/cook-inlet-seabird-and-forage-fish-study#overview.




    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_usgs_boem"))
```

## Map of CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_usgs_boem")("ctd_profiles_usgs_boem")
    
```

## 2016

+++

2016102001
        

```{code-cell}
cat['2016102001'].plot.data()
```

2016106001
        

```{code-cell}
cat['2016106001'].plot.data()
```

2016120001
        

```{code-cell}
cat['2016120001'].plot.data()
```

2016122201
        

```{code-cell}
cat['2016122201'].plot.data()
```

2016123001
        

```{code-cell}
cat['2016123001'].plot.data()
```

2016123002
        

```{code-cell}
cat['2016123002'].plot.data()
```

2016125001
        

```{code-cell}
cat['2016125001'].plot.data()
```

2016126001
        

```{code-cell}
cat['2016126001'].plot.data()
```

2016126002
        

```{code-cell}
cat['2016126002'].plot.data()
```

2016205701
        

```{code-cell}
cat['2016205701'].plot.data()
```

2016206001
        

```{code-cell}
cat['2016206001'].plot.data()
```

2016221001
        

```{code-cell}
cat['2016221001'].plot.data()
```

2016223001
        

```{code-cell}
cat['2016223001'].plot.data()
```

2016223002
        

```{code-cell}
cat['2016223002'].plot.data()
```

2016224001
        

```{code-cell}
cat['2016224001'].plot.data()
```

2016225001
        

```{code-cell}
cat['2016225001'].plot.data()
```

2016226001
        

```{code-cell}
cat['2016226001'].plot.data()
```

## 2017

+++

2017101001
        

```{code-cell}
cat['2017101001'].plot.data()
```

2017103001
        

```{code-cell}
cat['2017103001'].plot.data()
```

2017120001
        

```{code-cell}
cat['2017120001'].plot.data()
```

2017122001
        

```{code-cell}
cat['2017122001'].plot.data()
```

2017123001
        

```{code-cell}
cat['2017123001'].plot.data()
```

2017124001
        

```{code-cell}
cat['2017124001'].plot.data()
```

2017125001
        

```{code-cell}
cat['2017125001'].plot.data()
```

2017125002
        

```{code-cell}
cat['2017125002'].plot.data()
```

2017201001
        

```{code-cell}
cat['2017201001'].plot.data()
```

2017204001
        

```{code-cell}
cat['2017204001'].plot.data()
```

2017205001
        

```{code-cell}
cat['2017205001'].plot.data()
```

2017206001
        

```{code-cell}
cat['2017206001'].plot.data()
```

2017207001
        

```{code-cell}
cat['2017207001'].plot.data()
```

2017212001
        

```{code-cell}
cat['2017212001'].plot.data()
```

2017214001
        

```{code-cell}
cat['2017214001'].plot.data()
```

2017220001
        

```{code-cell}
cat['2017220001'].plot.data()
```

2017223001
        

```{code-cell}
cat['2017223001'].plot.data()
```

2017224001
        

```{code-cell}
cat['2017224001'].plot.data()
```

2017225001
        

```{code-cell}
cat['2017225001'].plot.data()
```

## 2018

+++

2018104001
        

```{code-cell}
cat['2018104001'].plot.data()
```

2018120001
        

```{code-cell}
cat['2018120001'].plot.data()
```

2018121001
        

```{code-cell}
cat['2018121001'].plot.data()
```

2018122001
        

```{code-cell}
cat['2018122001'].plot.data()
```

2018123001
        

```{code-cell}
cat['2018123001'].plot.data()
```

2018124001
        

```{code-cell}
cat['2018124001'].plot.data()
```

2018125001
        

```{code-cell}
cat['2018125001'].plot.data()
```

2018126001
        

```{code-cell}
cat['2018126001'].plot.data()
```

2018203001
        

```{code-cell}
cat['2018203001'].plot.data()
```

2018203002
        

```{code-cell}
cat['2018203002'].plot.data()
```

2018205001
        

```{code-cell}
cat['2018205001'].plot.data()
```

2018208001
        

```{code-cell}
cat['2018208001'].plot.data()
```

2018214002
        

```{code-cell}
cat['2018214002'].plot.data()
```

2018221001
        

```{code-cell}
cat['2018221001'].plot.data()
```

2018223001
        

```{code-cell}
cat['2018223001'].plot.data()
```

2018223002
        

```{code-cell}
cat['2018223002'].plot.data()
```

2018225001
        

```{code-cell}
cat['2018225001'].plot.data()
```

## 2019

+++

2019106001
        

```{code-cell}
cat['2019106001'].plot.data()
```

2019121001
        

```{code-cell}
cat['2019121001'].plot.data()
```

2019122001
        

```{code-cell}
cat['2019122001'].plot.data()
```

2019123001
        

```{code-cell}
cat['2019123001'].plot.data()
```

2019125001
        

```{code-cell}
cat['2019125001'].plot.data()
```

2019126001
        

```{code-cell}
cat['2019126001'].plot.data()
```

2019205001
        

```{code-cell}
cat['2019205001'].plot.data()
```

2019210001
        

```{code-cell}
cat['2019210001'].plot.data()
```

2019221001
        

```{code-cell}
cat['2019221001'].plot.data()
```

2019223001
        

```{code-cell}
cat['2019223001'].plot.data()
```

2019223002
        

```{code-cell}
cat['2019223002'].plot.data()
```

2019226001
        

```{code-cell}
cat['2019226001'].plot.data()
```

## 2021

+++

2021105001
        

```{code-cell}
cat['2021105001'].plot.data()
```

2021122001
        

```{code-cell}
cat['2021122001'].plot.data()
```

2021123001
        

```{code-cell}
cat['2021123001'].plot.data()
```

2021124001
        

```{code-cell}
cat['2021124001'].plot.data()
```

2021125001
        

```{code-cell}
cat['2021125001'].plot.data()
```

2021126001
        

```{code-cell}
cat['2021126001'].plot.data()
```

2021205001
        

```{code-cell}
cat['2021205001'].plot.data()
```

2021210001
        

```{code-cell}
cat['2021210001'].plot.data()
```

2021221001
        

```{code-cell}
cat['2021221001'].plot.data()
```

2021223001
        

```{code-cell}
cat['2021223001'].plot.data()
```

2021223002
        

```{code-cell}
cat['2021223002'].plot.data()
```

2021224001
        

```{code-cell}
cat['2021224001'].plot.data()
```

2021226001
        

```{code-cell}
cat['2021226001'].plot.data()
```
