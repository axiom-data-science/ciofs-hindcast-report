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

# Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths

* CTD Towed 2003 - OTF KBNERR
* ctd_towed_otf_kbnerr
* July 2003, 5min sampling frequency

Towed CTD Profiles.


Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_towed_otf_kbnerr"))
```

## Map of Towed CTD Profiles
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_otf_kbnerr")("ctd_towed_otf_kbnerr")
    
```

## mic071303
        

```{code-cell}
cat['mic071303'].plot.map() + cat['mic071303'].plot.salt() + cat['mic071303'].plot.temp()
```

## mic071903
        

```{code-cell}
cat['mic071903'].plot.map() + cat['mic071903'].plot.salt() + cat['mic071903'].plot.temp()
```

## mic072003
        

```{code-cell}
cat['mic072003'].plot.map() + cat['mic072003'].plot.salt() + cat['mic072003'].plot.temp()
```

## mic072103
        

```{code-cell}
cat['mic072103'].plot.map() + cat['mic072103'].plot.salt() + cat['mic072103'].plot.temp()
```

## mic072203
        

```{code-cell}
cat['mic072203'].plot.map() + cat['mic072203'].plot.salt() + cat['mic072203'].plot.temp()
```

## mic072403
        

```{code-cell}
cat['mic072403'].plot.map() + cat['mic072403'].plot.salt() + cat['mic072403'].plot.temp()
```

## mic072503
        

```{code-cell}
cat['mic072503'].plot.map() + cat['mic072503'].plot.salt() + cat['mic072503'].plot.temp()
```

## mic072603
        

```{code-cell}
cat['mic072603'].plot.map() + cat['mic072603'].plot.salt() + cat['mic072603'].plot.temp()
```

## mic072803_65-8
        

```{code-cell}
cat['mic072803_65-8'].plot.map() + cat['mic072803_65-8'].plot.salt() + cat['mic072803_65-8'].plot.temp()
```

## mic072903
        

```{code-cell}
cat['mic072903'].plot.map() + cat['mic072903'].plot.salt() + cat['mic072903'].plot.temp()
```

## mic073003
        

```{code-cell}
cat['mic073003'].plot.map() + cat['mic073003'].plot.salt() + cat['mic073003'].plot.temp()
```
