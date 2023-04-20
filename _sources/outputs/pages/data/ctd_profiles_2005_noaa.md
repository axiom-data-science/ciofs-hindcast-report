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

* CTD profiles 2005 - NOAA
* ctd_profiles_2005_noaa
* One-off CTD profiles in June and July 2005

CTD Profiles from NOAA.




    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_2005_noaa"))
```

## Map of CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_2005_noaa")("ctd_profiles_2005_noaa")
    
```

## 501
        

```{code-cell}
cat['501'].plot.data()
```

## 502
        

```{code-cell}
cat['502'].plot.data()
```

## 503
        

```{code-cell}
cat['503'].plot.data()
```

## 504
        

```{code-cell}
cat['504'].plot.data()
```

## 505
        

```{code-cell}
cat['505'].plot.data()
```

## 506
        

```{code-cell}
cat['506'].plot.data()
```

## 507
        

```{code-cell}
cat['507'].plot.data()
```

## 508
        

```{code-cell}
cat['508'].plot.data()
```

## 509
        

```{code-cell}
cat['509'].plot.data()
```

## 510
        

```{code-cell}
cat['510'].plot.data()
```

## 511
        

```{code-cell}
cat['511'].plot.data()
```

## 512
        

```{code-cell}
cat['512'].plot.data()
```

## 513
        

```{code-cell}
cat['513'].plot.data()
```

## 514
        

```{code-cell}
cat['514'].plot.data()
```

## 515
        

```{code-cell}
cat['515'].plot.data()
```

## 516
        

```{code-cell}
cat['516'].plot.data()
```

## 517
        

```{code-cell}
cat['517'].plot.data()
```

## 518
        

```{code-cell}
cat['518'].plot.data()
```

## 519
        

```{code-cell}
cat['519'].plot.data()
```

## 520
        

```{code-cell}
cat['520'].plot.data()
```

## 521
        

```{code-cell}
cat['521'].plot.data()
```

## 522
        

```{code-cell}
cat['522'].plot.data()
```

## 523
        

```{code-cell}
cat['523'].plot.data()
```

## 524
        

```{code-cell}
cat['524'].plot.data()
```
