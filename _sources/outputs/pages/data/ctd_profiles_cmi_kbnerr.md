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

# Six repeat transects, one single transect, and one time series of CTD profiles in Cook Inlet

* CTD profiles 2004-2006 - CMI KBNERR
* ctd_profiles_cmi_kbnerr
* From 2004 to 2006

Seasonality of Boundary Conditions for Cook Inlet, Alaska

During 2004 to 2006 we collected hydrographic measurements along transect lines crossing: 1) Kennedy Entrance and Stevenson Entrance from Port Chatham to Shuyak Island; 2) Shelikof Strait from Shuyak Island to Cape Douglas; 3) Cook Inlet from Red River to Anchor Point; 4) Kachemak Bay from Barbara Point to Bluff Point, and 5) the Forelands from East Foreland to West Foreland. During the third year we added two additional lines; 6) Cape Douglas to Cape Adams, and 7) Magnet Rock to Mount Augustine. The sampling in 2006 focused on the differences in properties during the spring and neap tide periods.

CTD profiles 2004-2005 - CMI UAF seems to be transect 5 of this project.

Note
Line 4 has an incorrect latitude for station 65. This can be seen with the following if the correction is not made:
```
df = cat['cmi_full_v2-Cruise_16-Line_4'].read()
df.drop_duplicates(subset="Station")
```
because the longitude is fixed and the latitude increases linearly until station 65 and then repeats the latitude value of station 56. The values are the same for the line in all datasets, and in the report. Since the difference in latitude across line 4 is about 0.0167, I will apply that difference from station 64 and use the resulting latitude for line 4, station 65.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>


Used in the NWGOA model/data comparison.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_cmi_kbnerr"))
```

## Map of CTD Profiles in Transects
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_cmi_kbnerr")("ctd_profiles_cmi_kbnerr")
    
```

## Kbay_timeseries

+++

Kbay_timeseries
        

```{code-cell}
cat['Kbay_timeseries'].plot.salt() + cat['Kbay_timeseries'].plot.temp()
```

## Cruise_00

+++

cmi_full_v2-Cruise_00-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_00-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_00-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_00-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_00-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_00-Line_4'].plot.temp()
```

## Cruise_01

+++

cmi_full_v2-Cruise_01-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_01-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_01-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_01-Line_4'].plot.temp()
```

## Cruise_02

+++

cmi_full_v2-Cruise_02-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_02-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_02-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_02-Line_4'].plot.temp()
```

## Cruise_03

+++

cmi_full_v2-Cruise_03-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_03-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_03-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_03-Line_4'].plot.temp()
```

## Cruise_04

+++

cmi_full_v2-Cruise_04-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_04-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_04-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_04-Line_4'].plot.temp()
```

## Cruise_05

+++

cmi_full_v2-Cruise_05-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_05-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_05-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_05-Line_4'].plot.temp()
```

## Cruise_06

+++

cmi_full_v2-Cruise_06-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_06-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_06-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_06-Line_4'].plot.temp()
```

## Cruise_07

+++

cmi_full_v2-Cruise_07-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_07-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_07-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_07-Line_4'].plot.temp()
```

## Cruise_08

+++

cmi_full_v2-Cruise_08-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_08-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_08-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_08-Line_4'].plot.temp()
```

## Cruise_09

+++

cmi_full_v2-Cruise_09-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_09-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_09-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_09-Line_4'].plot.temp()
```

## Cruise_10

+++

cmi_full_v2-Cruise_10-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_10-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_10-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_10-Line_4'].plot.temp()
```

## Cruise_11

+++

cmi_full_v2-Cruise_11-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_11-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_11-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_11-Line_4'].plot.temp()
```

## Cruise_12

+++

cmi_full_v2-Cruise_12-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_12-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_12-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_12-Line_4'].plot.temp()
```

## Cruise_13

+++

cmi_full_v2-Cruise_13-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_13-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_13-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_13-Line_7'].plot.temp()
```

## Cruise_14

+++

cmi_full_v2-Cruise_14-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_14-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_14-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_14-Line_7'].plot.temp()
```

## Cruise_15

+++

cmi_full_v2-Cruise_15-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_15-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_15-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_15-Line_7'].plot.temp()
```

## Cruise_16

+++

cmi_full_v2-Cruise_16-Line_1
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_1'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_1'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_2
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_2'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_2'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_3
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_3'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_3'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_4
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_4'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_4'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_6
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_6'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_6'].plot.temp()
```

cmi_full_v2-Cruise_16-Line_7
        

```{code-cell}
cat['cmi_full_v2-Cruise_16-Line_7'].plot.salt() + cat['cmi_full_v2-Cruise_16-Line_7'].plot.temp()
```

## sue_shelikof

+++

sue_shelikof
        

```{code-cell}
cat['sue_shelikof'].plot.salt() + cat['sue_shelikof'].plot.temp()
```
