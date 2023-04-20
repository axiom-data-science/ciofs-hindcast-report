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

# Six repeat transects in Cook Inlet

* CTD profiles 2012-2021 - GWA
* ctd_profiles_gwa
* Quarterly repeats from 2012 to 2021


The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    

Not used in the NWGOA model/data comparison.

    

```{code-cell}
cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_gwa"))
```

## Map of Transects
    

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_gwa")("ctd_profiles_gwa")
    
```

## transect_3

+++

transect_3-2012-05-02
        

```{code-cell}
cat['transect_3-2012-05-02'].plot.salt() + cat['transect_3-2012-05-02'].plot.temp()
```

transect_3-2012-07-29
        

```{code-cell}
cat['transect_3-2012-07-29'].plot.salt() + cat['transect_3-2012-07-29'].plot.temp()
```

transect_3-2012-10-29
        

```{code-cell}
cat['transect_3-2012-10-29'].plot.salt() + cat['transect_3-2012-10-29'].plot.temp()
```

transect_3-2013-04-20
        

```{code-cell}
cat['transect_3-2013-04-20'].plot.salt() + cat['transect_3-2013-04-20'].plot.temp()
```

transect_3-2013-07-19
        

```{code-cell}
cat['transect_3-2013-07-19'].plot.salt() + cat['transect_3-2013-07-19'].plot.temp()
```

transect_3-2013-11-08
        

```{code-cell}
cat['transect_3-2013-11-08'].plot.salt() + cat['transect_3-2013-11-08'].plot.temp()
```

transect_3-2014-04-11
        

```{code-cell}
cat['transect_3-2014-04-11'].plot.salt() + cat['transect_3-2014-04-11'].plot.temp()
```

transect_3-2014-07-22
        

```{code-cell}
cat['transect_3-2014-07-22'].plot.salt() + cat['transect_3-2014-07-22'].plot.temp()
```

transect_3-2014-10-13
        

```{code-cell}
cat['transect_3-2014-10-13'].plot.salt() + cat['transect_3-2014-10-13'].plot.temp()
```

transect_3-2015-02-22
        

```{code-cell}
cat['transect_3-2015-02-22'].plot.salt() + cat['transect_3-2015-02-22'].plot.temp()
```

transect_3-2015-04-12
        

```{code-cell}
cat['transect_3-2015-04-12'].plot.salt() + cat['transect_3-2015-04-12'].plot.temp()
```

transect_3-2015-11-04
        

```{code-cell}
cat['transect_3-2015-11-04'].plot.salt() + cat['transect_3-2015-11-04'].plot.temp()
```

transect_3-2016-02-14
        

```{code-cell}
cat['transect_3-2016-02-14'].plot.salt() + cat['transect_3-2016-02-14'].plot.temp()
```

transect_3-2016-04-11
        

```{code-cell}
cat['transect_3-2016-04-11'].plot.salt() + cat['transect_3-2016-04-11'].plot.temp()
```

transect_3-2016-08-29
        

```{code-cell}
cat['transect_3-2016-08-29'].plot.salt() + cat['transect_3-2016-08-29'].plot.temp()
```

transect_3-2017-04-19
        

```{code-cell}
cat['transect_3-2017-04-19'].plot.salt() + cat['transect_3-2017-04-19'].plot.temp()
```

transect_3-2017-04-20
        

```{code-cell}
cat['transect_3-2017-04-20'].plot.salt() + cat['transect_3-2017-04-20'].plot.temp()
```

transect_3-2017-07-25
        

```{code-cell}
cat['transect_3-2017-07-25'].plot.salt() + cat['transect_3-2017-07-25'].plot.temp()
```

transect_3-2018-06-25
        

```{code-cell}
cat['transect_3-2018-06-25'].plot.salt() + cat['transect_3-2018-06-25'].plot.temp()
```

transect_3-2018-07-26
        

```{code-cell}
cat['transect_3-2018-07-26'].plot.salt() + cat['transect_3-2018-07-26'].plot.temp()
```

transect_3-2018-09-13
        

```{code-cell}
cat['transect_3-2018-09-13'].plot.salt() + cat['transect_3-2018-09-13'].plot.temp()
```

transect_3-2019-02-08
        

```{code-cell}
cat['transect_3-2019-02-08'].plot.salt() + cat['transect_3-2019-02-08'].plot.temp()
```

transect_3-2019-05-14
        

```{code-cell}
cat['transect_3-2019-05-14'].plot.salt() + cat['transect_3-2019-05-14'].plot.temp()
```

transect_3-2019-07-25
        

```{code-cell}
cat['transect_3-2019-07-25'].plot.salt() + cat['transect_3-2019-07-25'].plot.temp()
```

transect_3-2019-09-16
        

```{code-cell}
cat['transect_3-2019-09-16'].plot.salt() + cat['transect_3-2019-09-16'].plot.temp()
```

transect_3-2020-07-29
        

```{code-cell}
cat['transect_3-2020-07-29'].plot.salt() + cat['transect_3-2020-07-29'].plot.temp()
```

transect_3-2021-04-16
        

```{code-cell}
cat['transect_3-2021-04-16'].plot.salt() + cat['transect_3-2021-04-16'].plot.temp()
```

transect_3-2021-07-16
        

```{code-cell}
cat['transect_3-2021-07-16'].plot.salt() + cat['transect_3-2021-07-16'].plot.temp()
```

## transect_4

+++

transect_4-2012-05-02
        

```{code-cell}
cat['transect_4-2012-05-02'].plot.salt() + cat['transect_4-2012-05-02'].plot.temp()
```

transect_4-2012-05-31
        

```{code-cell}
cat['transect_4-2012-05-31'].plot.salt() + cat['transect_4-2012-05-31'].plot.temp()
```

transect_4-2012-06-05
        

```{code-cell}
cat['transect_4-2012-06-05'].plot.salt() + cat['transect_4-2012-06-05'].plot.temp()
```

transect_4-2012-07-31
        

```{code-cell}
cat['transect_4-2012-07-31'].plot.salt() + cat['transect_4-2012-07-31'].plot.temp()
```

transect_4-2012-08-15
        

```{code-cell}
cat['transect_4-2012-08-15'].plot.salt() + cat['transect_4-2012-08-15'].plot.temp()
```

transect_4-2012-10-29
        

```{code-cell}
cat['transect_4-2012-10-29'].plot.salt() + cat['transect_4-2012-10-29'].plot.temp()
```

transect_4-2013-02-12
        

```{code-cell}
cat['transect_4-2013-02-12'].plot.salt() + cat['transect_4-2013-02-12'].plot.temp()
```

transect_4-2013-04-21
        

```{code-cell}
cat['transect_4-2013-04-21'].plot.salt() + cat['transect_4-2013-04-21'].plot.temp()
```

transect_4-2013-06-06
        

```{code-cell}
cat['transect_4-2013-06-06'].plot.salt() + cat['transect_4-2013-06-06'].plot.temp()
```

transect_4-2013-07-19
        

```{code-cell}
cat['transect_4-2013-07-19'].plot.salt() + cat['transect_4-2013-07-19'].plot.temp()
```

transect_4-2013-10-29
        

```{code-cell}
cat['transect_4-2013-10-29'].plot.salt() + cat['transect_4-2013-10-29'].plot.temp()
```

transect_4-2014-02-15
        

```{code-cell}
cat['transect_4-2014-02-15'].plot.salt() + cat['transect_4-2014-02-15'].plot.temp()
```

transect_4-2014-04-11
        

```{code-cell}
cat['transect_4-2014-04-11'].plot.salt() + cat['transect_4-2014-04-11'].plot.temp()
```

transect_4-2014-07-21
        

```{code-cell}
cat['transect_4-2014-07-21'].plot.salt() + cat['transect_4-2014-07-21'].plot.temp()
```

transect_4-2014-08-13
        

```{code-cell}
cat['transect_4-2014-08-13'].plot.salt() + cat['transect_4-2014-08-13'].plot.temp()
```

transect_4-2014-10-13
        

```{code-cell}
cat['transect_4-2014-10-13'].plot.salt() + cat['transect_4-2014-10-13'].plot.temp()
```

transect_4-2015-02-12
        

```{code-cell}
cat['transect_4-2015-02-12'].plot.salt() + cat['transect_4-2015-02-12'].plot.temp()
```

transect_4-2015-02-24
        

```{code-cell}
cat['transect_4-2015-02-24'].plot.salt() + cat['transect_4-2015-02-24'].plot.temp()
```

transect_4-2015-04-08
        

```{code-cell}
cat['transect_4-2015-04-08'].plot.salt() + cat['transect_4-2015-04-08'].plot.temp()
```

transect_4-2015-08-14
        

```{code-cell}
cat['transect_4-2015-08-14'].plot.salt() + cat['transect_4-2015-08-14'].plot.temp()
```

transect_4-2015-09-24
        

```{code-cell}
cat['transect_4-2015-09-24'].plot.salt() + cat['transect_4-2015-09-24'].plot.temp()
```

transect_4-2015-10-19
        

```{code-cell}
cat['transect_4-2015-10-19'].plot.salt() + cat['transect_4-2015-10-19'].plot.temp()
```

transect_4-2015-11-03
        

```{code-cell}
cat['transect_4-2015-11-03'].plot.salt() + cat['transect_4-2015-11-03'].plot.temp()
```

transect_4-2015-11-04
        

```{code-cell}
cat['transect_4-2015-11-04'].plot.salt() + cat['transect_4-2015-11-04'].plot.temp()
```

transect_4-2015-12-10
        

```{code-cell}
cat['transect_4-2015-12-10'].plot.salt() + cat['transect_4-2015-12-10'].plot.temp()
```

transect_4-2016-02-09
        

```{code-cell}
cat['transect_4-2016-02-09'].plot.salt() + cat['transect_4-2016-02-09'].plot.temp()
```

transect_4-2016-04-11
        

```{code-cell}
cat['transect_4-2016-04-11'].plot.salt() + cat['transect_4-2016-04-11'].plot.temp()
```

transect_4-2016-07-27
        

```{code-cell}
cat['transect_4-2016-07-27'].plot.salt() + cat['transect_4-2016-07-27'].plot.temp()
```

transect_4-2016-10-13
        

```{code-cell}
cat['transect_4-2016-10-13'].plot.salt() + cat['transect_4-2016-10-13'].plot.temp()
```

transect_4-2016-12-13
        

```{code-cell}
cat['transect_4-2016-12-13'].plot.salt() + cat['transect_4-2016-12-13'].plot.temp()
```

transect_4-2017-04-20
        

```{code-cell}
cat['transect_4-2017-04-20'].plot.salt() + cat['transect_4-2017-04-20'].plot.temp()
```

transect_4-2017-07-25
        

```{code-cell}
cat['transect_4-2017-07-25'].plot.salt() + cat['transect_4-2017-07-25'].plot.temp()
```

transect_4-2017-10-17
        

```{code-cell}
cat['transect_4-2017-10-17'].plot.salt() + cat['transect_4-2017-10-17'].plot.temp()
```

transect_4-2018-04-23
        

```{code-cell}
cat['transect_4-2018-04-23'].plot.salt() + cat['transect_4-2018-04-23'].plot.temp()
```

transect_4-2018-06-25
        

```{code-cell}
cat['transect_4-2018-06-25'].plot.salt() + cat['transect_4-2018-06-25'].plot.temp()
```

transect_4-2018-07-24
        

```{code-cell}
cat['transect_4-2018-07-24'].plot.salt() + cat['transect_4-2018-07-24'].plot.temp()
```

transect_4-2018-09-13
        

```{code-cell}
cat['transect_4-2018-09-13'].plot.salt() + cat['transect_4-2018-09-13'].plot.temp()
```

transect_4-2019-02-07
        

```{code-cell}
cat['transect_4-2019-02-07'].plot.salt() + cat['transect_4-2019-02-07'].plot.temp()
```

transect_4-2019-05-14
        

```{code-cell}
cat['transect_4-2019-05-14'].plot.salt() + cat['transect_4-2019-05-14'].plot.temp()
```

transect_4-2019-07-25
        

```{code-cell}
cat['transect_4-2019-07-25'].plot.salt() + cat['transect_4-2019-07-25'].plot.temp()
```

transect_4-2019-09-16
        

```{code-cell}
cat['transect_4-2019-09-16'].plot.salt() + cat['transect_4-2019-09-16'].plot.temp()
```

transect_4-2020-02-14
        

```{code-cell}
cat['transect_4-2020-02-14'].plot.salt() + cat['transect_4-2020-02-14'].plot.temp()
```

transect_4-2020-07-23
        

```{code-cell}
cat['transect_4-2020-07-23'].plot.salt() + cat['transect_4-2020-07-23'].plot.temp()
```

transect_4-2020-09-21
        

```{code-cell}
cat['transect_4-2020-09-21'].plot.salt() + cat['transect_4-2020-09-21'].plot.temp()
```

transect_4-2021-02-17
        

```{code-cell}
cat['transect_4-2021-02-17'].plot.salt() + cat['transect_4-2021-02-17'].plot.temp()
```

transect_4-2021-04-16
        

```{code-cell}
cat['transect_4-2021-04-16'].plot.salt() + cat['transect_4-2021-04-16'].plot.temp()
```

transect_4-2021-07-16
        

```{code-cell}
cat['transect_4-2021-07-16'].plot.salt() + cat['transect_4-2021-07-16'].plot.temp()
```

transect_4-2021-09-17
        

```{code-cell}
cat['transect_4-2021-09-17'].plot.salt() + cat['transect_4-2021-09-17'].plot.temp()
```

transect_4-2022-03-01
        

```{code-cell}
cat['transect_4-2022-03-01'].plot.salt() + cat['transect_4-2022-03-01'].plot.temp()
```

transect_4-2022-04-13
        

```{code-cell}
cat['transect_4-2022-04-13'].plot.salt() + cat['transect_4-2022-04-13'].plot.temp()
```

transect_4-2022-07-23
        

```{code-cell}
cat['transect_4-2022-07-23'].plot.salt() + cat['transect_4-2022-07-23'].plot.temp()
```

## transect_6

+++

transect_6-2012-05-03
        

```{code-cell}
cat['transect_6-2012-05-03'].plot.salt() + cat['transect_6-2012-05-03'].plot.temp()
```

transect_6-2012-05-04
        

```{code-cell}
cat['transect_6-2012-05-04'].plot.salt() + cat['transect_6-2012-05-04'].plot.temp()
```

transect_6-2012-07-30
        

```{code-cell}
cat['transect_6-2012-07-30'].plot.salt() + cat['transect_6-2012-07-30'].plot.temp()
```

transect_6-2012-07-31
        

```{code-cell}
cat['transect_6-2012-07-31'].plot.salt() + cat['transect_6-2012-07-31'].plot.temp()
```

transect_6-2012-10-28
        

```{code-cell}
cat['transect_6-2012-10-28'].plot.salt() + cat['transect_6-2012-10-28'].plot.temp()
```

transect_6-2013-04-19
        

```{code-cell}
cat['transect_6-2013-04-19'].plot.salt() + cat['transect_6-2013-04-19'].plot.temp()
```

transect_6-2013-07-21
        

```{code-cell}
cat['transect_6-2013-07-21'].plot.salt() + cat['transect_6-2013-07-21'].plot.temp()
```

transect_6-2013-07-22
        

```{code-cell}
cat['transect_6-2013-07-22'].plot.salt() + cat['transect_6-2013-07-22'].plot.temp()
```

transect_6-2013-11-06
        

```{code-cell}
cat['transect_6-2013-11-06'].plot.salt() + cat['transect_6-2013-11-06'].plot.temp()
```

transect_6-2014-04-06
        

```{code-cell}
cat['transect_6-2014-04-06'].plot.salt() + cat['transect_6-2014-04-06'].plot.temp()
```

transect_6-2014-07-23
        

```{code-cell}
cat['transect_6-2014-07-23'].plot.salt() + cat['transect_6-2014-07-23'].plot.temp()
```

transect_6-2014-10-18
        

```{code-cell}
cat['transect_6-2014-10-18'].plot.salt() + cat['transect_6-2014-10-18'].plot.temp()
```

transect_6-2015-02-23
        

```{code-cell}
cat['transect_6-2015-02-23'].plot.salt() + cat['transect_6-2015-02-23'].plot.temp()
```

transect_6-2015-02-24
        

```{code-cell}
cat['transect_6-2015-02-24'].plot.salt() + cat['transect_6-2015-02-24'].plot.temp()
```

transect_6-2015-04-08
        

```{code-cell}
cat['transect_6-2015-04-08'].plot.salt() + cat['transect_6-2015-04-08'].plot.temp()
```

transect_6-2015-08-14
        

```{code-cell}
cat['transect_6-2015-08-14'].plot.salt() + cat['transect_6-2015-08-14'].plot.temp()
```

transect_6-2016-02-15
        

```{code-cell}
cat['transect_6-2016-02-15'].plot.salt() + cat['transect_6-2016-02-15'].plot.temp()
```

transect_6-2016-04-10
        

```{code-cell}
cat['transect_6-2016-04-10'].plot.salt() + cat['transect_6-2016-04-10'].plot.temp()
```

transect_6-2016-08-31
        

```{code-cell}
cat['transect_6-2016-08-31'].plot.salt() + cat['transect_6-2016-08-31'].plot.temp()
```

transect_6-2016-12-12
        

```{code-cell}
cat['transect_6-2016-12-12'].plot.salt() + cat['transect_6-2016-12-12'].plot.temp()
```

transect_6-2017-04-18
        

```{code-cell}
cat['transect_6-2017-04-18'].plot.salt() + cat['transect_6-2017-04-18'].plot.temp()
```

transect_6-2017-07-26
        

```{code-cell}
cat['transect_6-2017-07-26'].plot.salt() + cat['transect_6-2017-07-26'].plot.temp()
```

transect_6-2017-11-02
        

```{code-cell}
cat['transect_6-2017-11-02'].plot.salt() + cat['transect_6-2017-11-02'].plot.temp()
```

transect_6-2018-07-18
        

```{code-cell}
cat['transect_6-2018-07-18'].plot.salt() + cat['transect_6-2018-07-18'].plot.temp()
```

transect_6-2018-09-17
        

```{code-cell}
cat['transect_6-2018-09-17'].plot.salt() + cat['transect_6-2018-09-17'].plot.temp()
```

transect_6-2019-02-08
        

```{code-cell}
cat['transect_6-2019-02-08'].plot.salt() + cat['transect_6-2019-02-08'].plot.temp()
```

transect_6-2019-05-12
        

```{code-cell}
cat['transect_6-2019-05-12'].plot.salt() + cat['transect_6-2019-05-12'].plot.temp()
```

transect_6-2019-07-25
        

```{code-cell}
cat['transect_6-2019-07-25'].plot.salt() + cat['transect_6-2019-07-25'].plot.temp()
```

transect_6-2020-07-24
        

```{code-cell}
cat['transect_6-2020-07-24'].plot.salt() + cat['transect_6-2020-07-24'].plot.temp()
```

transect_6-2020-09-20
        

```{code-cell}
cat['transect_6-2020-09-20'].plot.salt() + cat['transect_6-2020-09-20'].plot.temp()
```

transect_6-2021-02-16
        

```{code-cell}
cat['transect_6-2021-02-16'].plot.salt() + cat['transect_6-2021-02-16'].plot.temp()
```

transect_6-2021-04-14
        

```{code-cell}
cat['transect_6-2021-04-14'].plot.salt() + cat['transect_6-2021-04-14'].plot.temp()
```

transect_6-2021-07-21
        

```{code-cell}
cat['transect_6-2021-07-21'].plot.salt() + cat['transect_6-2021-07-21'].plot.temp()
```

transect_6-2021-10-05
        

```{code-cell}
cat['transect_6-2021-10-05'].plot.salt() + cat['transect_6-2021-10-05'].plot.temp()
```

transect_6-2022-02-28
        

```{code-cell}
cat['transect_6-2022-02-28'].plot.salt() + cat['transect_6-2022-02-28'].plot.temp()
```

transect_6-2022-04-12
        

```{code-cell}
cat['transect_6-2022-04-12'].plot.salt() + cat['transect_6-2022-04-12'].plot.temp()
```

transect_6-2022-07-21
        

```{code-cell}
cat['transect_6-2022-07-21'].plot.salt() + cat['transect_6-2022-07-21'].plot.temp()
```

## transect_7

+++

transect_7-2012-07-30
        

```{code-cell}
cat['transect_7-2012-07-30'].plot.salt() + cat['transect_7-2012-07-30'].plot.temp()
```

transect_7-2012-10-28
        

```{code-cell}
cat['transect_7-2012-10-28'].plot.salt() + cat['transect_7-2012-10-28'].plot.temp()
```

transect_7-2012-10-29
        

```{code-cell}
cat['transect_7-2012-10-29'].plot.salt() + cat['transect_7-2012-10-29'].plot.temp()
```

transect_7-2013-04-20
        

```{code-cell}
cat['transect_7-2013-04-20'].plot.salt() + cat['transect_7-2013-04-20'].plot.temp()
```

transect_7-2013-07-18
        

```{code-cell}
cat['transect_7-2013-07-18'].plot.salt() + cat['transect_7-2013-07-18'].plot.temp()
```

transect_7-2014-02-17
        

```{code-cell}
cat['transect_7-2014-02-17'].plot.salt() + cat['transect_7-2014-02-17'].plot.temp()
```

transect_7-2014-04-07
        

```{code-cell}
cat['transect_7-2014-04-07'].plot.salt() + cat['transect_7-2014-04-07'].plot.temp()
```

transect_7-2014-07-24
        

```{code-cell}
cat['transect_7-2014-07-24'].plot.salt() + cat['transect_7-2014-07-24'].plot.temp()
```

transect_7-2014-10-17
        

```{code-cell}
cat['transect_7-2014-10-17'].plot.salt() + cat['transect_7-2014-10-17'].plot.temp()
```

transect_7-2014-10-18
        

```{code-cell}
cat['transect_7-2014-10-18'].plot.salt() + cat['transect_7-2014-10-18'].plot.temp()
```

transect_7-2015-02-24
        

```{code-cell}
cat['transect_7-2015-02-24'].plot.salt() + cat['transect_7-2015-02-24'].plot.temp()
```

transect_7-2015-04-13
        

```{code-cell}
cat['transect_7-2015-04-13'].plot.salt() + cat['transect_7-2015-04-13'].plot.temp()
```

transect_7-2015-08-14
        

```{code-cell}
cat['transect_7-2015-08-14'].plot.salt() + cat['transect_7-2015-08-14'].plot.temp()
```

transect_7-2016-02-16
        

```{code-cell}
cat['transect_7-2016-02-16'].plot.salt() + cat['transect_7-2016-02-16'].plot.temp()
```

transect_7-2016-08-30
        

```{code-cell}
cat['transect_7-2016-08-30'].plot.salt() + cat['transect_7-2016-08-30'].plot.temp()
```

transect_7-2016-12-13
        

```{code-cell}
cat['transect_7-2016-12-13'].plot.salt() + cat['transect_7-2016-12-13'].plot.temp()
```

transect_7-2017-04-19
        

```{code-cell}
cat['transect_7-2017-04-19'].plot.salt() + cat['transect_7-2017-04-19'].plot.temp()
```

transect_7-2017-07-26
        

```{code-cell}
cat['transect_7-2017-07-26'].plot.salt() + cat['transect_7-2017-07-26'].plot.temp()
```

transect_7-2017-11-02
        

```{code-cell}
cat['transect_7-2017-11-02'].plot.salt() + cat['transect_7-2017-11-02'].plot.temp()
```

transect_7-2018-03-27
        

```{code-cell}
cat['transect_7-2018-03-27'].plot.salt() + cat['transect_7-2018-03-27'].plot.temp()
```

transect_7-2018-07-18
        

```{code-cell}
cat['transect_7-2018-07-18'].plot.salt() + cat['transect_7-2018-07-18'].plot.temp()
```

transect_7-2018-09-17
        

```{code-cell}
cat['transect_7-2018-09-17'].plot.salt() + cat['transect_7-2018-09-17'].plot.temp()
```

transect_7-2019-02-08
        

```{code-cell}
cat['transect_7-2019-02-08'].plot.salt() + cat['transect_7-2019-02-08'].plot.temp()
```

transect_7-2019-05-12
        

```{code-cell}
cat['transect_7-2019-05-12'].plot.salt() + cat['transect_7-2019-05-12'].plot.temp()
```

transect_7-2019-07-25
        

```{code-cell}
cat['transect_7-2019-07-25'].plot.salt() + cat['transect_7-2019-07-25'].plot.temp()
```

transect_7-2019-09-19
        

```{code-cell}
cat['transect_7-2019-09-19'].plot.salt() + cat['transect_7-2019-09-19'].plot.temp()
```

transect_7-2020-07-24
        

```{code-cell}
cat['transect_7-2020-07-24'].plot.salt() + cat['transect_7-2020-07-24'].plot.temp()
```

transect_7-2020-09-20
        

```{code-cell}
cat['transect_7-2020-09-20'].plot.salt() + cat['transect_7-2020-09-20'].plot.temp()
```

transect_7-2021-02-16
        

```{code-cell}
cat['transect_7-2021-02-16'].plot.salt() + cat['transect_7-2021-02-16'].plot.temp()
```

transect_7-2021-04-14
        

```{code-cell}
cat['transect_7-2021-04-14'].plot.salt() + cat['transect_7-2021-04-14'].plot.temp()
```

transect_7-2021-07-21
        

```{code-cell}
cat['transect_7-2021-07-21'].plot.salt() + cat['transect_7-2021-07-21'].plot.temp()
```

transect_7-2021-10-05
        

```{code-cell}
cat['transect_7-2021-10-05'].plot.salt() + cat['transect_7-2021-10-05'].plot.temp()
```

transect_7-2022-02-28
        

```{code-cell}
cat['transect_7-2022-02-28'].plot.salt() + cat['transect_7-2022-02-28'].plot.temp()
```

transect_7-2022-04-12
        

```{code-cell}
cat['transect_7-2022-04-12'].plot.salt() + cat['transect_7-2022-04-12'].plot.temp()
```

transect_7-2022-07-21
        

```{code-cell}
cat['transect_7-2022-07-21'].plot.salt() + cat['transect_7-2022-07-21'].plot.temp()
```

## transect_9

+++

transect_9-2012-02-14
        

```{code-cell}
cat['transect_9-2012-02-14'].plot.salt() + cat['transect_9-2012-02-14'].plot.temp()
```

transect_9-2012-03-14
        

```{code-cell}
cat['transect_9-2012-03-14'].plot.salt() + cat['transect_9-2012-03-14'].plot.temp()
```

transect_9-2012-04-10
        

```{code-cell}
cat['transect_9-2012-04-10'].plot.salt() + cat['transect_9-2012-04-10'].plot.temp()
```

transect_9-2012-04-26
        

```{code-cell}
cat['transect_9-2012-04-26'].plot.salt() + cat['transect_9-2012-04-26'].plot.temp()
```

transect_9-2012-05-31
        

```{code-cell}
cat['transect_9-2012-05-31'].plot.salt() + cat['transect_9-2012-05-31'].plot.temp()
```

transect_9-2012-06-05
        

```{code-cell}
cat['transect_9-2012-06-05'].plot.salt() + cat['transect_9-2012-06-05'].plot.temp()
```

transect_9-2012-06-27
        

```{code-cell}
cat['transect_9-2012-06-27'].plot.salt() + cat['transect_9-2012-06-27'].plot.temp()
```

transect_9-2012-07-02
        

```{code-cell}
cat['transect_9-2012-07-02'].plot.salt() + cat['transect_9-2012-07-02'].plot.temp()
```

transect_9-2012-07-21
        

```{code-cell}
cat['transect_9-2012-07-21'].plot.salt() + cat['transect_9-2012-07-21'].plot.temp()
```

transect_9-2012-08-03
        

```{code-cell}
cat['transect_9-2012-08-03'].plot.salt() + cat['transect_9-2012-08-03'].plot.temp()
```

transect_9-2012-08-15
        

```{code-cell}
cat['transect_9-2012-08-15'].plot.salt() + cat['transect_9-2012-08-15'].plot.temp()
```

transect_9-2012-08-26
        

```{code-cell}
cat['transect_9-2012-08-26'].plot.salt() + cat['transect_9-2012-08-26'].plot.temp()
```

transect_9-2012-08-31
        

```{code-cell}
cat['transect_9-2012-08-31'].plot.salt() + cat['transect_9-2012-08-31'].plot.temp()
```

transect_9-2012-09-21
        

```{code-cell}
cat['transect_9-2012-09-21'].plot.salt() + cat['transect_9-2012-09-21'].plot.temp()
```

transect_9-2012-10-12
        

```{code-cell}
cat['transect_9-2012-10-12'].plot.salt() + cat['transect_9-2012-10-12'].plot.temp()
```

transect_9-2012-10-29
        

```{code-cell}
cat['transect_9-2012-10-29'].plot.salt() + cat['transect_9-2012-10-29'].plot.temp()
```

transect_9-2013-01-04
        

```{code-cell}
cat['transect_9-2013-01-04'].plot.salt() + cat['transect_9-2013-01-04'].plot.temp()
```

transect_9-2013-02-12
        

```{code-cell}
cat['transect_9-2013-02-12'].plot.salt() + cat['transect_9-2013-02-12'].plot.temp()
```

transect_9-2013-03-15
        

```{code-cell}
cat['transect_9-2013-03-15'].plot.salt() + cat['transect_9-2013-03-15'].plot.temp()
```

transect_9-2013-04-21
        

```{code-cell}
cat['transect_9-2013-04-21'].plot.salt() + cat['transect_9-2013-04-21'].plot.temp()
```

transect_9-2013-05-21
        

```{code-cell}
cat['transect_9-2013-05-21'].plot.salt() + cat['transect_9-2013-05-21'].plot.temp()
```

transect_9-2013-06-06
        

```{code-cell}
cat['transect_9-2013-06-06'].plot.salt() + cat['transect_9-2013-06-06'].plot.temp()
```

transect_9-2013-06-19
        

```{code-cell}
cat['transect_9-2013-06-19'].plot.salt() + cat['transect_9-2013-06-19'].plot.temp()
```

transect_9-2013-06-28
        

```{code-cell}
cat['transect_9-2013-06-28'].plot.salt() + cat['transect_9-2013-06-28'].plot.temp()
```

transect_9-2013-07-05
        

```{code-cell}
cat['transect_9-2013-07-05'].plot.salt() + cat['transect_9-2013-07-05'].plot.temp()
```

transect_9-2013-07-09
        

```{code-cell}
cat['transect_9-2013-07-09'].plot.salt() + cat['transect_9-2013-07-09'].plot.temp()
```

transect_9-2013-07-22
        

```{code-cell}
cat['transect_9-2013-07-22'].plot.salt() + cat['transect_9-2013-07-22'].plot.temp()
```

transect_9-2013-08-07
        

```{code-cell}
cat['transect_9-2013-08-07'].plot.salt() + cat['transect_9-2013-08-07'].plot.temp()
```

transect_9-2013-08-30
        

```{code-cell}
cat['transect_9-2013-08-30'].plot.salt() + cat['transect_9-2013-08-30'].plot.temp()
```

transect_9-2013-09-25
        

```{code-cell}
cat['transect_9-2013-09-25'].plot.salt() + cat['transect_9-2013-09-25'].plot.temp()
```

transect_9-2013-10-29
        

```{code-cell}
cat['transect_9-2013-10-29'].plot.salt() + cat['transect_9-2013-10-29'].plot.temp()
```

transect_9-2013-12-03
        

```{code-cell}
cat['transect_9-2013-12-03'].plot.salt() + cat['transect_9-2013-12-03'].plot.temp()
```

transect_9-2014-01-09
        

```{code-cell}
cat['transect_9-2014-01-09'].plot.salt() + cat['transect_9-2014-01-09'].plot.temp()
```

transect_9-2014-02-15
        

```{code-cell}
cat['transect_9-2014-02-15'].plot.salt() + cat['transect_9-2014-02-15'].plot.temp()
```

transect_9-2014-03-28
        

```{code-cell}
cat['transect_9-2014-03-28'].plot.salt() + cat['transect_9-2014-03-28'].plot.temp()
```

transect_9-2014-04-11
        

```{code-cell}
cat['transect_9-2014-04-11'].plot.salt() + cat['transect_9-2014-04-11'].plot.temp()
```

transect_9-2014-05-28
        

```{code-cell}
cat['transect_9-2014-05-28'].plot.salt() + cat['transect_9-2014-05-28'].plot.temp()
```

transect_9-2014-06-18
        

```{code-cell}
cat['transect_9-2014-06-18'].plot.salt() + cat['transect_9-2014-06-18'].plot.temp()
```

transect_9-2014-07-21
        

```{code-cell}
cat['transect_9-2014-07-21'].plot.salt() + cat['transect_9-2014-07-21'].plot.temp()
```

transect_9-2014-08-13
        

```{code-cell}
cat['transect_9-2014-08-13'].plot.salt() + cat['transect_9-2014-08-13'].plot.temp()
```

transect_9-2014-10-19
        

```{code-cell}
cat['transect_9-2014-10-19'].plot.salt() + cat['transect_9-2014-10-19'].plot.temp()
```

transect_9-2014-11-25
        

```{code-cell}
cat['transect_9-2014-11-25'].plot.salt() + cat['transect_9-2014-11-25'].plot.temp()
```

transect_9-2014-12-17
        

```{code-cell}
cat['transect_9-2014-12-17'].plot.salt() + cat['transect_9-2014-12-17'].plot.temp()
```

transect_9-2015-01-16
        

```{code-cell}
cat['transect_9-2015-01-16'].plot.salt() + cat['transect_9-2015-01-16'].plot.temp()
```

transect_9-2015-02-12
        

```{code-cell}
cat['transect_9-2015-02-12'].plot.salt() + cat['transect_9-2015-02-12'].plot.temp()
```

transect_9-2015-02-24
        

```{code-cell}
cat['transect_9-2015-02-24'].plot.salt() + cat['transect_9-2015-02-24'].plot.temp()
```

transect_9-2015-03-31
        

```{code-cell}
cat['transect_9-2015-03-31'].plot.salt() + cat['transect_9-2015-03-31'].plot.temp()
```

transect_9-2015-04-08
        

```{code-cell}
cat['transect_9-2015-04-08'].plot.salt() + cat['transect_9-2015-04-08'].plot.temp()
```

transect_9-2015-05-28
        

```{code-cell}
cat['transect_9-2015-05-28'].plot.salt() + cat['transect_9-2015-05-28'].plot.temp()
```

transect_9-2015-06-26
        

```{code-cell}
cat['transect_9-2015-06-26'].plot.salt() + cat['transect_9-2015-06-26'].plot.temp()
```

transect_9-2015-07-10
        

```{code-cell}
cat['transect_9-2015-07-10'].plot.salt() + cat['transect_9-2015-07-10'].plot.temp()
```

transect_9-2015-07-29
        

```{code-cell}
cat['transect_9-2015-07-29'].plot.salt() + cat['transect_9-2015-07-29'].plot.temp()
```

transect_9-2015-08-14
        

```{code-cell}
cat['transect_9-2015-08-14'].plot.salt() + cat['transect_9-2015-08-14'].plot.temp()
```

transect_9-2015-09-04
        

```{code-cell}
cat['transect_9-2015-09-04'].plot.salt() + cat['transect_9-2015-09-04'].plot.temp()
```

transect_9-2015-09-24
        

```{code-cell}
cat['transect_9-2015-09-24'].plot.salt() + cat['transect_9-2015-09-24'].plot.temp()
```

transect_9-2015-10-19
        

```{code-cell}
cat['transect_9-2015-10-19'].plot.salt() + cat['transect_9-2015-10-19'].plot.temp()
```

transect_9-2015-11-04
        

```{code-cell}
cat['transect_9-2015-11-04'].plot.salt() + cat['transect_9-2015-11-04'].plot.temp()
```

transect_9-2015-12-10
        

```{code-cell}
cat['transect_9-2015-12-10'].plot.salt() + cat['transect_9-2015-12-10'].plot.temp()
```

transect_9-2016-01-07
        

```{code-cell}
cat['transect_9-2016-01-07'].plot.salt() + cat['transect_9-2016-01-07'].plot.temp()
```

transect_9-2016-02-09
        

```{code-cell}
cat['transect_9-2016-02-09'].plot.salt() + cat['transect_9-2016-02-09'].plot.temp()
```

transect_9-2016-04-07
        

```{code-cell}
cat['transect_9-2016-04-07'].plot.salt() + cat['transect_9-2016-04-07'].plot.temp()
```

transect_9-2016-05-12
        

```{code-cell}
cat['transect_9-2016-05-12'].plot.salt() + cat['transect_9-2016-05-12'].plot.temp()
```

transect_9-2016-06-16
        

```{code-cell}
cat['transect_9-2016-06-16'].plot.salt() + cat['transect_9-2016-06-16'].plot.temp()
```

transect_9-2016-07-27
        

```{code-cell}
cat['transect_9-2016-07-27'].plot.salt() + cat['transect_9-2016-07-27'].plot.temp()
```

transect_9-2016-09-23
        

```{code-cell}
cat['transect_9-2016-09-23'].plot.salt() + cat['transect_9-2016-09-23'].plot.temp()
```

transect_9-2016-10-13
        

```{code-cell}
cat['transect_9-2016-10-13'].plot.salt() + cat['transect_9-2016-10-13'].plot.temp()
```

transect_9-2016-11-10
        

```{code-cell}
cat['transect_9-2016-11-10'].plot.salt() + cat['transect_9-2016-11-10'].plot.temp()
```

transect_9-2016-12-13
        

```{code-cell}
cat['transect_9-2016-12-13'].plot.salt() + cat['transect_9-2016-12-13'].plot.temp()
```

transect_9-2017-01-11
        

```{code-cell}
cat['transect_9-2017-01-11'].plot.salt() + cat['transect_9-2017-01-11'].plot.temp()
```

transect_9-2017-02-07
        

```{code-cell}
cat['transect_9-2017-02-07'].plot.salt() + cat['transect_9-2017-02-07'].plot.temp()
```

transect_9-2017-03-28
        

```{code-cell}
cat['transect_9-2017-03-28'].plot.salt() + cat['transect_9-2017-03-28'].plot.temp()
```

transect_9-2017-04-20
        

```{code-cell}
cat['transect_9-2017-04-20'].plot.salt() + cat['transect_9-2017-04-20'].plot.temp()
```

transect_9-2017-05-30
        

```{code-cell}
cat['transect_9-2017-05-30'].plot.salt() + cat['transect_9-2017-05-30'].plot.temp()
```

transect_9-2017-06-28
        

```{code-cell}
cat['transect_9-2017-06-28'].plot.salt() + cat['transect_9-2017-06-28'].plot.temp()
```

transect_9-2017-07-24
        

```{code-cell}
cat['transect_9-2017-07-24'].plot.salt() + cat['transect_9-2017-07-24'].plot.temp()
```

transect_9-2017-08-24
        

```{code-cell}
cat['transect_9-2017-08-24'].plot.salt() + cat['transect_9-2017-08-24'].plot.temp()
```

transect_9-2017-09-22
        

```{code-cell}
cat['transect_9-2017-09-22'].plot.salt() + cat['transect_9-2017-09-22'].plot.temp()
```

transect_9-2017-10-17
        

```{code-cell}
cat['transect_9-2017-10-17'].plot.salt() + cat['transect_9-2017-10-17'].plot.temp()
```

transect_9-2017-11-07
        

```{code-cell}
cat['transect_9-2017-11-07'].plot.salt() + cat['transect_9-2017-11-07'].plot.temp()
```

transect_9-2017-12-14
        

```{code-cell}
cat['transect_9-2017-12-14'].plot.salt() + cat['transect_9-2017-12-14'].plot.temp()
```

transect_9-2018-01-17
        

```{code-cell}
cat['transect_9-2018-01-17'].plot.salt() + cat['transect_9-2018-01-17'].plot.temp()
```

transect_9-2018-03-02
        

```{code-cell}
cat['transect_9-2018-03-02'].plot.salt() + cat['transect_9-2018-03-02'].plot.temp()
```

transect_9-2018-03-27
        

```{code-cell}
cat['transect_9-2018-03-27'].plot.salt() + cat['transect_9-2018-03-27'].plot.temp()
```

transect_9-2018-04-23
        

```{code-cell}
cat['transect_9-2018-04-23'].plot.salt() + cat['transect_9-2018-04-23'].plot.temp()
```

transect_9-2018-05-24
        

```{code-cell}
cat['transect_9-2018-05-24'].plot.salt() + cat['transect_9-2018-05-24'].plot.temp()
```

transect_9-2018-06-22
        

```{code-cell}
cat['transect_9-2018-06-22'].plot.salt() + cat['transect_9-2018-06-22'].plot.temp()
```

transect_9-2018-07-24
        

```{code-cell}
cat['transect_9-2018-07-24'].plot.salt() + cat['transect_9-2018-07-24'].plot.temp()
```

transect_9-2018-08-23
        

```{code-cell}
cat['transect_9-2018-08-23'].plot.salt() + cat['transect_9-2018-08-23'].plot.temp()
```

transect_9-2018-09-13
        

```{code-cell}
cat['transect_9-2018-09-13'].plot.salt() + cat['transect_9-2018-09-13'].plot.temp()
```

transect_9-2018-10-17
        

```{code-cell}
cat['transect_9-2018-10-17'].plot.salt() + cat['transect_9-2018-10-17'].plot.temp()
```

transect_9-2018-11-08
        

```{code-cell}
cat['transect_9-2018-11-08'].plot.salt() + cat['transect_9-2018-11-08'].plot.temp()
```

transect_9-2018-12-06
        

```{code-cell}
cat['transect_9-2018-12-06'].plot.salt() + cat['transect_9-2018-12-06'].plot.temp()
```

transect_9-2019-02-07
        

```{code-cell}
cat['transect_9-2019-02-07'].plot.salt() + cat['transect_9-2019-02-07'].plot.temp()
```

transect_9-2019-03-19
        

```{code-cell}
cat['transect_9-2019-03-19'].plot.salt() + cat['transect_9-2019-03-19'].plot.temp()
```

transect_9-2019-04-24
        

```{code-cell}
cat['transect_9-2019-04-24'].plot.salt() + cat['transect_9-2019-04-24'].plot.temp()
```

transect_9-2019-05-14
        

```{code-cell}
cat['transect_9-2019-05-14'].plot.salt() + cat['transect_9-2019-05-14'].plot.temp()
```

transect_9-2019-06-19
        

```{code-cell}
cat['transect_9-2019-06-19'].plot.salt() + cat['transect_9-2019-06-19'].plot.temp()
```

transect_9-2019-07-23
        

```{code-cell}
cat['transect_9-2019-07-23'].plot.salt() + cat['transect_9-2019-07-23'].plot.temp()
```

transect_9-2019-09-16
        

```{code-cell}
cat['transect_9-2019-09-16'].plot.salt() + cat['transect_9-2019-09-16'].plot.temp()
```

transect_9-2019-10-30
        

```{code-cell}
cat['transect_9-2019-10-30'].plot.salt() + cat['transect_9-2019-10-30'].plot.temp()
```

transect_9-2019-11-15
        

```{code-cell}
cat['transect_9-2019-11-15'].plot.salt() + cat['transect_9-2019-11-15'].plot.temp()
```

transect_9-2019-12-12
        

```{code-cell}
cat['transect_9-2019-12-12'].plot.salt() + cat['transect_9-2019-12-12'].plot.temp()
```

transect_9-2020-02-06
        

```{code-cell}
cat['transect_9-2020-02-06'].plot.salt() + cat['transect_9-2020-02-06'].plot.temp()
```

transect_9-2020-03-18
        

```{code-cell}
cat['transect_9-2020-03-18'].plot.salt() + cat['transect_9-2020-03-18'].plot.temp()
```

transect_9-2020-06-04
        

```{code-cell}
cat['transect_9-2020-06-04'].plot.salt() + cat['transect_9-2020-06-04'].plot.temp()
```

transect_9-2020-07-24
        

```{code-cell}
cat['transect_9-2020-07-24'].plot.salt() + cat['transect_9-2020-07-24'].plot.temp()
```

transect_9-2020-08-14
        

```{code-cell}
cat['transect_9-2020-08-14'].plot.salt() + cat['transect_9-2020-08-14'].plot.temp()
```

transect_9-2020-09-21
        

```{code-cell}
cat['transect_9-2020-09-21'].plot.salt() + cat['transect_9-2020-09-21'].plot.temp()
```

transect_9-2020-10-15
        

```{code-cell}
cat['transect_9-2020-10-15'].plot.salt() + cat['transect_9-2020-10-15'].plot.temp()
```

transect_9-2020-12-28
        

```{code-cell}
cat['transect_9-2020-12-28'].plot.salt() + cat['transect_9-2020-12-28'].plot.temp()
```

transect_9-2021-01-13
        

```{code-cell}
cat['transect_9-2021-01-13'].plot.salt() + cat['transect_9-2021-01-13'].plot.temp()
```

transect_9-2021-02-17
        

```{code-cell}
cat['transect_9-2021-02-17'].plot.salt() + cat['transect_9-2021-02-17'].plot.temp()
```

transect_9-2021-03-23
        

```{code-cell}
cat['transect_9-2021-03-23'].plot.salt() + cat['transect_9-2021-03-23'].plot.temp()
```

transect_9-2021-04-16
        

```{code-cell}
cat['transect_9-2021-04-16'].plot.salt() + cat['transect_9-2021-04-16'].plot.temp()
```

transect_9-2021-05-06
        

```{code-cell}
cat['transect_9-2021-05-06'].plot.salt() + cat['transect_9-2021-05-06'].plot.temp()
```

transect_9-2021-06-21
        

```{code-cell}
cat['transect_9-2021-06-21'].plot.salt() + cat['transect_9-2021-06-21'].plot.temp()
```

transect_9-2021-07-16
        

```{code-cell}
cat['transect_9-2021-07-16'].plot.salt() + cat['transect_9-2021-07-16'].plot.temp()
```

transect_9-2021-08-17
        

```{code-cell}
cat['transect_9-2021-08-17'].plot.salt() + cat['transect_9-2021-08-17'].plot.temp()
```

transect_9-2021-09-17
        

```{code-cell}
cat['transect_9-2021-09-17'].plot.salt() + cat['transect_9-2021-09-17'].plot.temp()
```

transect_9-2021-10-21
        

```{code-cell}
cat['transect_9-2021-10-21'].plot.salt() + cat['transect_9-2021-10-21'].plot.temp()
```

transect_9-2021-11-14
        

```{code-cell}
cat['transect_9-2021-11-14'].plot.salt() + cat['transect_9-2021-11-14'].plot.temp()
```

transect_9-2021-12-18
        

```{code-cell}
cat['transect_9-2021-12-18'].plot.salt() + cat['transect_9-2021-12-18'].plot.temp()
```

transect_9-2022-01-31
        

```{code-cell}
cat['transect_9-2022-01-31'].plot.salt() + cat['transect_9-2022-01-31'].plot.temp()
```

transect_9-2022-03-01
        

```{code-cell}
cat['transect_9-2022-03-01'].plot.salt() + cat['transect_9-2022-03-01'].plot.temp()
```

transect_9-2022-03-22
        

```{code-cell}
cat['transect_9-2022-03-22'].plot.salt() + cat['transect_9-2022-03-22'].plot.temp()
```

transect_9-2022-04-13
        

```{code-cell}
cat['transect_9-2022-04-13'].plot.salt() + cat['transect_9-2022-04-13'].plot.temp()
```

transect_9-2022-05-23
        

```{code-cell}
cat['transect_9-2022-05-23'].plot.salt() + cat['transect_9-2022-05-23'].plot.temp()
```

transect_9-2022-06-24
        

```{code-cell}
cat['transect_9-2022-06-24'].plot.salt() + cat['transect_9-2022-06-24'].plot.temp()
```

transect_9-2022-07-23
        

```{code-cell}
cat['transect_9-2022-07-23'].plot.salt() + cat['transect_9-2022-07-23'].plot.temp()
```

transect_9-2022-08-24
        

```{code-cell}
cat['transect_9-2022-08-24'].plot.salt() + cat['transect_9-2022-08-24'].plot.temp()
```

## transect_AlongBay

+++

transect_AlongBay-2012-08-15
        

```{code-cell}
cat['transect_AlongBay-2012-08-15'].plot.salt() + cat['transect_AlongBay-2012-08-15'].plot.temp()
```

transect_AlongBay-2013-02-12
        

```{code-cell}
cat['transect_AlongBay-2013-02-12'].plot.salt() + cat['transect_AlongBay-2013-02-12'].plot.temp()
```

transect_AlongBay-2013-02-13
        

```{code-cell}
cat['transect_AlongBay-2013-02-13'].plot.salt() + cat['transect_AlongBay-2013-02-13'].plot.temp()
```

transect_AlongBay-2013-06-06
        

```{code-cell}
cat['transect_AlongBay-2013-06-06'].plot.salt() + cat['transect_AlongBay-2013-06-06'].plot.temp()
```

transect_AlongBay-2014-03-28
        

```{code-cell}
cat['transect_AlongBay-2014-03-28'].plot.salt() + cat['transect_AlongBay-2014-03-28'].plot.temp()
```

transect_AlongBay-2014-05-28
        

```{code-cell}
cat['transect_AlongBay-2014-05-28'].plot.salt() + cat['transect_AlongBay-2014-05-28'].plot.temp()
```

transect_AlongBay-2014-08-14
        

```{code-cell}
cat['transect_AlongBay-2014-08-14'].plot.salt() + cat['transect_AlongBay-2014-08-14'].plot.temp()
```

transect_AlongBay-2015-07-10
        

```{code-cell}
cat['transect_AlongBay-2015-07-10'].plot.salt() + cat['transect_AlongBay-2015-07-10'].plot.temp()
```

transect_AlongBay-2015-08-14
        

```{code-cell}
cat['transect_AlongBay-2015-08-14'].plot.salt() + cat['transect_AlongBay-2015-08-14'].plot.temp()
```

transect_AlongBay-2016-01-07
        

```{code-cell}
cat['transect_AlongBay-2016-01-07'].plot.salt() + cat['transect_AlongBay-2016-01-07'].plot.temp()
```

transect_AlongBay-2016-05-12
        

```{code-cell}
cat['transect_AlongBay-2016-05-12'].plot.salt() + cat['transect_AlongBay-2016-05-12'].plot.temp()
```

transect_AlongBay-2016-06-16
        

```{code-cell}
cat['transect_AlongBay-2016-06-16'].plot.salt() + cat['transect_AlongBay-2016-06-16'].plot.temp()
```

transect_AlongBay-2016-07-27
        

```{code-cell}
cat['transect_AlongBay-2016-07-27'].plot.salt() + cat['transect_AlongBay-2016-07-27'].plot.temp()
```

transect_AlongBay-2017-01-11
        

```{code-cell}
cat['transect_AlongBay-2017-01-11'].plot.salt() + cat['transect_AlongBay-2017-01-11'].plot.temp()
```

transect_AlongBay-2017-02-07
        

```{code-cell}
cat['transect_AlongBay-2017-02-07'].plot.salt() + cat['transect_AlongBay-2017-02-07'].plot.temp()
```

transect_AlongBay-2017-03-28
        

```{code-cell}
cat['transect_AlongBay-2017-03-28'].plot.salt() + cat['transect_AlongBay-2017-03-28'].plot.temp()
```

transect_AlongBay-2017-04-20
        

```{code-cell}
cat['transect_AlongBay-2017-04-20'].plot.salt() + cat['transect_AlongBay-2017-04-20'].plot.temp()
```

transect_AlongBay-2017-05-30
        

```{code-cell}
cat['transect_AlongBay-2017-05-30'].plot.salt() + cat['transect_AlongBay-2017-05-30'].plot.temp()
```

transect_AlongBay-2017-06-28
        

```{code-cell}
cat['transect_AlongBay-2017-06-28'].plot.salt() + cat['transect_AlongBay-2017-06-28'].plot.temp()
```

transect_AlongBay-2017-07-24
        

```{code-cell}
cat['transect_AlongBay-2017-07-24'].plot.salt() + cat['transect_AlongBay-2017-07-24'].plot.temp()
```

transect_AlongBay-2017-07-26
        

```{code-cell}
cat['transect_AlongBay-2017-07-26'].plot.salt() + cat['transect_AlongBay-2017-07-26'].plot.temp()
```

transect_AlongBay-2017-08-24
        

```{code-cell}
cat['transect_AlongBay-2017-08-24'].plot.salt() + cat['transect_AlongBay-2017-08-24'].plot.temp()
```

transect_AlongBay-2017-09-22
        

```{code-cell}
cat['transect_AlongBay-2017-09-22'].plot.salt() + cat['transect_AlongBay-2017-09-22'].plot.temp()
```

transect_AlongBay-2017-10-20
        

```{code-cell}
cat['transect_AlongBay-2017-10-20'].plot.salt() + cat['transect_AlongBay-2017-10-20'].plot.temp()
```

transect_AlongBay-2017-11-02
        

```{code-cell}
cat['transect_AlongBay-2017-11-02'].plot.salt() + cat['transect_AlongBay-2017-11-02'].plot.temp()
```

transect_AlongBay-2017-11-07
        

```{code-cell}
cat['transect_AlongBay-2017-11-07'].plot.salt() + cat['transect_AlongBay-2017-11-07'].plot.temp()
```

transect_AlongBay-2017-12-14
        

```{code-cell}
cat['transect_AlongBay-2017-12-14'].plot.salt() + cat['transect_AlongBay-2017-12-14'].plot.temp()
```

transect_AlongBay-2018-01-17
        

```{code-cell}
cat['transect_AlongBay-2018-01-17'].plot.salt() + cat['transect_AlongBay-2018-01-17'].plot.temp()
```

transect_AlongBay-2018-03-02
        

```{code-cell}
cat['transect_AlongBay-2018-03-02'].plot.salt() + cat['transect_AlongBay-2018-03-02'].plot.temp()
```

transect_AlongBay-2018-03-27
        

```{code-cell}
cat['transect_AlongBay-2018-03-27'].plot.salt() + cat['transect_AlongBay-2018-03-27'].plot.temp()
```

transect_AlongBay-2018-04-23
        

```{code-cell}
cat['transect_AlongBay-2018-04-23'].plot.salt() + cat['transect_AlongBay-2018-04-23'].plot.temp()
```

transect_AlongBay-2018-05-24
        

```{code-cell}
cat['transect_AlongBay-2018-05-24'].plot.salt() + cat['transect_AlongBay-2018-05-24'].plot.temp()
```

transect_AlongBay-2018-06-22
        

```{code-cell}
cat['transect_AlongBay-2018-06-22'].plot.salt() + cat['transect_AlongBay-2018-06-22'].plot.temp()
```

transect_AlongBay-2018-07-18
        

```{code-cell}
cat['transect_AlongBay-2018-07-18'].plot.salt() + cat['transect_AlongBay-2018-07-18'].plot.temp()
```

transect_AlongBay-2018-08-23
        

```{code-cell}
cat['transect_AlongBay-2018-08-23'].plot.salt() + cat['transect_AlongBay-2018-08-23'].plot.temp()
```

transect_AlongBay-2018-09-17
        

```{code-cell}
cat['transect_AlongBay-2018-09-17'].plot.salt() + cat['transect_AlongBay-2018-09-17'].plot.temp()
```

transect_AlongBay-2018-10-17
        

```{code-cell}
cat['transect_AlongBay-2018-10-17'].plot.salt() + cat['transect_AlongBay-2018-10-17'].plot.temp()
```

transect_AlongBay-2018-11-08
        

```{code-cell}
cat['transect_AlongBay-2018-11-08'].plot.salt() + cat['transect_AlongBay-2018-11-08'].plot.temp()
```

transect_AlongBay-2018-12-06
        

```{code-cell}
cat['transect_AlongBay-2018-12-06'].plot.salt() + cat['transect_AlongBay-2018-12-06'].plot.temp()
```

transect_AlongBay-2019-02-07
        

```{code-cell}
cat['transect_AlongBay-2019-02-07'].plot.salt() + cat['transect_AlongBay-2019-02-07'].plot.temp()
```

transect_AlongBay-2019-03-19
        

```{code-cell}
cat['transect_AlongBay-2019-03-19'].plot.salt() + cat['transect_AlongBay-2019-03-19'].plot.temp()
```

transect_AlongBay-2019-04-24
        

```{code-cell}
cat['transect_AlongBay-2019-04-24'].plot.salt() + cat['transect_AlongBay-2019-04-24'].plot.temp()
```

transect_AlongBay-2019-05-14
        

```{code-cell}
cat['transect_AlongBay-2019-05-14'].plot.salt() + cat['transect_AlongBay-2019-05-14'].plot.temp()
```

transect_AlongBay-2019-06-19
        

```{code-cell}
cat['transect_AlongBay-2019-06-19'].plot.salt() + cat['transect_AlongBay-2019-06-19'].plot.temp()
```

transect_AlongBay-2019-07-23
        

```{code-cell}
cat['transect_AlongBay-2019-07-23'].plot.salt() + cat['transect_AlongBay-2019-07-23'].plot.temp()
```

transect_AlongBay-2019-10-30
        

```{code-cell}
cat['transect_AlongBay-2019-10-30'].plot.salt() + cat['transect_AlongBay-2019-10-30'].plot.temp()
```

transect_AlongBay-2019-11-15
        

```{code-cell}
cat['transect_AlongBay-2019-11-15'].plot.salt() + cat['transect_AlongBay-2019-11-15'].plot.temp()
```

transect_AlongBay-2019-12-12
        

```{code-cell}
cat['transect_AlongBay-2019-12-12'].plot.salt() + cat['transect_AlongBay-2019-12-12'].plot.temp()
```

transect_AlongBay-2020-02-06
        

```{code-cell}
cat['transect_AlongBay-2020-02-06'].plot.salt() + cat['transect_AlongBay-2020-02-06'].plot.temp()
```

transect_AlongBay-2020-03-18
        

```{code-cell}
cat['transect_AlongBay-2020-03-18'].plot.salt() + cat['transect_AlongBay-2020-03-18'].plot.temp()
```

transect_AlongBay-2020-06-04
        

```{code-cell}
cat['transect_AlongBay-2020-06-04'].plot.salt() + cat['transect_AlongBay-2020-06-04'].plot.temp()
```

transect_AlongBay-2020-07-08
        

```{code-cell}
cat['transect_AlongBay-2020-07-08'].plot.salt() + cat['transect_AlongBay-2020-07-08'].plot.temp()
```

transect_AlongBay-2020-07-23
        

```{code-cell}
cat['transect_AlongBay-2020-07-23'].plot.salt() + cat['transect_AlongBay-2020-07-23'].plot.temp()
```

transect_AlongBay-2020-08-14
        

```{code-cell}
cat['transect_AlongBay-2020-08-14'].plot.salt() + cat['transect_AlongBay-2020-08-14'].plot.temp()
```

transect_AlongBay-2020-09-20
        

```{code-cell}
cat['transect_AlongBay-2020-09-20'].plot.salt() + cat['transect_AlongBay-2020-09-20'].plot.temp()
```

transect_AlongBay-2020-10-15
        

```{code-cell}
cat['transect_AlongBay-2020-10-15'].plot.salt() + cat['transect_AlongBay-2020-10-15'].plot.temp()
```

transect_AlongBay-2020-12-28
        

```{code-cell}
cat['transect_AlongBay-2020-12-28'].plot.salt() + cat['transect_AlongBay-2020-12-28'].plot.temp()
```

transect_AlongBay-2021-01-13
        

```{code-cell}
cat['transect_AlongBay-2021-01-13'].plot.salt() + cat['transect_AlongBay-2021-01-13'].plot.temp()
```

transect_AlongBay-2021-02-16
        

```{code-cell}
cat['transect_AlongBay-2021-02-16'].plot.salt() + cat['transect_AlongBay-2021-02-16'].plot.temp()
```

transect_AlongBay-2021-03-23
        

```{code-cell}
cat['transect_AlongBay-2021-03-23'].plot.salt() + cat['transect_AlongBay-2021-03-23'].plot.temp()
```

transect_AlongBay-2021-04-14
        

```{code-cell}
cat['transect_AlongBay-2021-04-14'].plot.salt() + cat['transect_AlongBay-2021-04-14'].plot.temp()
```

transect_AlongBay-2021-04-16
        

```{code-cell}
cat['transect_AlongBay-2021-04-16'].plot.salt() + cat['transect_AlongBay-2021-04-16'].plot.temp()
```

transect_AlongBay-2021-05-06
        

```{code-cell}
cat['transect_AlongBay-2021-05-06'].plot.salt() + cat['transect_AlongBay-2021-05-06'].plot.temp()
```

transect_AlongBay-2021-06-21
        

```{code-cell}
cat['transect_AlongBay-2021-06-21'].plot.salt() + cat['transect_AlongBay-2021-06-21'].plot.temp()
```

transect_AlongBay-2021-07-21
        

```{code-cell}
cat['transect_AlongBay-2021-07-21'].plot.salt() + cat['transect_AlongBay-2021-07-21'].plot.temp()
```

transect_AlongBay-2021-08-17
        

```{code-cell}
cat['transect_AlongBay-2021-08-17'].plot.salt() + cat['transect_AlongBay-2021-08-17'].plot.temp()
```

transect_AlongBay-2021-10-04
        

```{code-cell}
cat['transect_AlongBay-2021-10-04'].plot.salt() + cat['transect_AlongBay-2021-10-04'].plot.temp()
```

transect_AlongBay-2021-10-05
        

```{code-cell}
cat['transect_AlongBay-2021-10-05'].plot.salt() + cat['transect_AlongBay-2021-10-05'].plot.temp()
```

transect_AlongBay-2021-10-21
        

```{code-cell}
cat['transect_AlongBay-2021-10-21'].plot.salt() + cat['transect_AlongBay-2021-10-21'].plot.temp()
```

transect_AlongBay-2021-11-14
        

```{code-cell}
cat['transect_AlongBay-2021-11-14'].plot.salt() + cat['transect_AlongBay-2021-11-14'].plot.temp()
```

transect_AlongBay-2021-12-18
        

```{code-cell}
cat['transect_AlongBay-2021-12-18'].plot.salt() + cat['transect_AlongBay-2021-12-18'].plot.temp()
```

transect_AlongBay-2022-01-31
        

```{code-cell}
cat['transect_AlongBay-2022-01-31'].plot.salt() + cat['transect_AlongBay-2022-01-31'].plot.temp()
```

transect_AlongBay-2022-02-28
        

```{code-cell}
cat['transect_AlongBay-2022-02-28'].plot.salt() + cat['transect_AlongBay-2022-02-28'].plot.temp()
```

transect_AlongBay-2022-03-21
        

```{code-cell}
cat['transect_AlongBay-2022-03-21'].plot.salt() + cat['transect_AlongBay-2022-03-21'].plot.temp()
```

transect_AlongBay-2022-04-12
        

```{code-cell}
cat['transect_AlongBay-2022-04-12'].plot.salt() + cat['transect_AlongBay-2022-04-12'].plot.temp()
```

transect_AlongBay-2022-05-23
        

```{code-cell}
cat['transect_AlongBay-2022-05-23'].plot.salt() + cat['transect_AlongBay-2022-05-23'].plot.temp()
```

transect_AlongBay-2022-06-24
        

```{code-cell}
cat['transect_AlongBay-2022-06-24'].plot.salt() + cat['transect_AlongBay-2022-06-24'].plot.temp()
```

transect_AlongBay-2022-07-21
        

```{code-cell}
cat['transect_AlongBay-2022-07-21'].plot.salt() + cat['transect_AlongBay-2022-07-21'].plot.temp()
```

transect_AlongBay-2022-08-24
        

```{code-cell}
cat['transect_AlongBay-2022-08-24'].plot.salt() + cat['transect_AlongBay-2022-08-24'].plot.temp()
```
