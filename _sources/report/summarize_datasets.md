---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
---

```{code-cell}
import ciofs_hindcast_report as chr
import intake
import pandas as pd
import numpy as np
```

# Datasets Considered

## Table of All Datasets

|    | description                                                                                                                                                        | slug                       | project_name                                                                                | time                                                                       | featuretype       | included   | notes                                                                                                                                                                                                       |
|---:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|:--------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|:------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | GWA: Six repeat transects in Cook Inlet                                                                                                                            | ctd_profiles_gwa           | CTD profiles 2012-2021 - GWA                                                                | Quarterly repeats from 2012 to 2021                                        | trajectoryProfile | True       | Not used in the NWGOA model/data comparison.                                                                                                                                                                |
|  2 | NOAA: Single CTD profiles across Cook Inlet                                                                                                                        | ctd_profiles_2005_noaa     | CTD profiles 2005 - NOAA                                                                    | One-off CTD profiles in June and July 2005                                 | profile           | True       |                                                                                                                                                                                                             |
|  3 | USGS BOEM: Single CTD profiles across Cook Inlet                                                                                                                   | ctd_profiles_usgs_boem     | CTD profiles - USGS BOEM                                                                    | One-off CTD profiles from 2016 to 2021 in July                             | profile           | True       |                                                                                                                                                                                                             |
|  4 | OTF KBNERR: Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths                                                               | ctd_towed_otf_kbnerr       | CTD Towed 2003 - OTF KBNERR                                                                 | July 2003, 5min sampling frequency                                         | trajectoryProfile | True       | Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency. |
|  5 | NOAA PMEL: Towed CTD on ferry at nominal 4m depth                                                                                                                  | ctd_towed_ferry_noaa_pmel  | CTD Towed 2004-2008 Ferry in-line - NOAA PMEL                                               | Continuous 2004 to 2008, 5min sampling frequency                           | trajectory        | True       | The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency.                                                    |
|  6 | OTF KBNERR: Repeat CTD transect from Anchor Point in Cook Inlet                                                                                                    | ctd_profiles_otf_kbnerr    | CTD profiles 2003-2006 - OTF KBNERR                                                         | Daily in July, 2003 to 2006                                                | trajectoryProfile | True       | These data were not included in the NWGOA model/data comparison                                                                                                                                             |
|  7 | CMI UAF: CTD transect from East Foreland Lighthouse in Cook Inlet                                                                                                  | ctd_profiles_cmi_uaf       | CTD profiles 2004-2005 - CMI UAF                                                            | 10 cruises, approximately monthly for summer months, in 2004 and 2005      | trajectoryProfile | True       | Used in the NWGOA model/data comparison.                                                                                                                                                                    |
|  8 | CMI KBNERR: Six repeat transects, one single transect, and one time series of CTD profiles in Cook Inlet                                                           | ctd_profiles_cmi_kbnerr    | CTD profiles 2004-2006 - CMI KBNERR                                                         | From 2004 to 2006                                                          | trajectoryProfile | True       | Used in the NWGOA model/data comparison.                                                                                                                                                                    |
|  9 | CIRCAC: Central Cook Inlet Mooring                                                                                                                                 | ctd_moored_circac          | CTD Moored 2006 - CIRCAC                                                                    | Two weeks in August 2006, 15 min sampling                                  | timeSeries        | True       |                                                                                                                                                                                                             |
| 10 | KBNERR: Lower Cook Inlet Mooring                                                                                                                                   | ctd_moored_kbnerr          | CTD Moored 2006-2008 - KBNERR                                                               | Aug to Oct 2006 and June 2007 to Feb 2008, 15 min sampling                 | timeSeries        | True       |                                                                                                                                                                                                             |
| 11 | UAF: Repeat CTD profile transect along an east-west section in central Cook Inlet                                                                                  | ctd_time_series_uaf        | CTD time series UAF                                                                         | 26-hour period on 9-10 August 2003                                         | trajectoryProfile | True       | Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison.                                                                                                                |
| 12 | OSU: Time series of CTD profiles at several locations in Cook Inlet                                                                                                | ctd_profiles_2005_osu      | CTD profiles 2005 - OSU                                                                     | June 2005                                                                  | timeSeriesProfile | False      | Locations given are too low resolution making them incorrectly on land.                                                                                                                                     |
| 13 | GWA: Towed CTD at nominal 7m depth                                                                                                                                 | ctd_towed_gwa              | CTD Towed 2017-2019 - GWA                                                                   | Approximately monthly in summer from 2017 to 2020, 5min sampling frequency | trajectory        | True       | Made all longitudes negative west values, converted some local times, 2019 and 2020 only have temperature, ship track outside domain is not included, resampled from 2min to 5min.                          |
| 14 | GWA: Towed CTD at nominal 7m depth, temperature only                                                                                                               | temp_towed_gwa             | Temperature towed 2011-2016 - GWA                                                           | Approximately monthly in summer from 2011 to 2016, 5min sampling frequency | trajectory        | True       | Converted some local times, ship track outside domain is not included.                                                                                                                                      |
| 15 | UAF Moorings: Kodiak Island and Peterson Bay, Cook Inlet                                                                                                           | moorings_uaf               | Moorings from University of Alaska Fairbanks (UAF)                                          | From 2013 to present, variable                                             | timeSeries        | True       |                                                                                                                                                                                                             |
| 16 | NPS Moorings: Chinitna Bay and Aguchik Island, Cook Inlet                                                                                                          | moorings_nps               | Moorings from National Parks Service (NPS)                                                  | From 2018 to 2019, variable                                                | timeSeries        | True       |                                                                                                                                                                                                             |
| 17 | NOAA Moorings: Geese Island, Sitkalidak Island, Bear Cove, Anchorage, Kodiak Island, Alitak, Seldovia, Old Harbor, Boulder Point, Albatross Banks, Shelikof Strait | moorings_noaa              | Moorings from NOAA                                                                          | From 1999 (and earlier) to 2023, variable                                  | timeSeries        | True       |                                                                                                                                                                                                             |
| 18 | CDIP Buoys: Lower Cook Inlet, Kodiak, Central Cook Inlet                                                                                                           | moorings_aoos_cdip         | Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP) | From , variable                                                            | timeSeries        | True       |                                                                                                                                                                                                             |
| 19 | OTF ADF&G: Long term station sampling                                                                                                                              | surface_otf_adfg           | surface Temp Sal - OTF ADF&G                                                                | Daily sampling mostly in July 1979 to 2021                                 | trajectoryProfile | False      | Not used because no times associated with data.                                                                                                                                                             |
| 20 | Historical KBNERR Moorings: Kachemak Bay                                                                                                                           | moorings_kbnerr_historical | Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)          | From 2001 to 2003, variable                                                | timeSeries        | True       | These are accessed from Research Workspace.                                                                                                                                                                 |

## Summary of Each Dataset

+++


### CTD profiles 2012-2021 - GWA

* GWA: Six repeat transects in Cook Inlet
* Quarterly repeats from 2012 to 2021
* Slug: ctd_profiles_gwa
* Included: True
* Feature type: trajectoryProfile


The Kachemak Bay Research Reserve (KBRR) and NOAA Kasitsna Bay Laboratory jointly work to complete oceanographic monitoring in Kachemak Bay and lower Cook Inlet, in order to provide the physical data needed for comprehensive restoration monitoring in the Exxon Valdez oil spill (EVOS) affected area. This project utilized small boat oceanographic and plankton surveys at existing KBRR water quality monitoring stations to assess spatial, seasonal and inter-annual variability in water mass movement. In addition, this work leveraged information from previous oceanographic surveys in the region, provided environmental information that aided a concurrent Gulf Watch benthic monitoring project, and benefited from a new NOAA ocean circulation model for Cook Inlet.

Surveys are conducted annually along five primary transects; two in Kachemak Bay and three in lower Cook Inlet, Alaska. Oceanographic data were collected via vertical CTD casts from surface to bottom, zooplankton and phytoplankton tows were made in the upper water column, and seabird and marine mammal observations were performed opportunistically. We also collect meteorological data and water quality measurements in Homer Harbor and Anchor Point year-round at stations as part of our National Estuarine Research Reserve (NERR) System-wide Monitoring program in Seldovia and Homer harbors, and in ice-free months at a mooring near the head of Kachemak Bay.

Project files and further description can be found here: https://gulf-of-alaska.portal.aoos.org/#metadata/4e28304c-22a1-4976-8881-7289776e4173/project
    

Notes:

Not used in the NWGOA model/data comparison.

**Map of Transects**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_gwa")("ctd_profiles_gwa")
        
```


### CTD profiles 2005 - NOAA

* NOAA: Single CTD profiles across Cook Inlet
* One-off CTD profiles in June and July 2005
* Slug: ctd_profiles_2005_noaa
* Included: True
* Feature type: profile

CTD Profiles from NOAA.


Notes:



**Map of CTD Profiles**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_2005_noaa")("ctd_profiles_2005_noaa")
        
```


### CTD profiles - USGS BOEM

* USGS BOEM: Single CTD profiles across Cook Inlet
* One-off CTD profiles from 2016 to 2021 in July
* Slug: ctd_profiles_usgs_boem
* Included: True
* Feature type: profile

USGS Cook Inlet fish and bird survey CTD profiles.
    
CTD profiles collected in Cook Inlet from 2016-2021 by Mayumi Arimitsu as part of BOEM sponsored research on fish and bird distributions in Cook Inlet. The profiles are collected in July for the years 2016-2021.

The scientific project is described here: https://www.usgs.gov/centers/alaska-science-center/science/cook-inlet-seabird-and-forage-fish-study#overview.


Notes:



**Map of CTD Profiles**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_usgs_boem")("ctd_profiles_usgs_boem")
        
```


### CTD Towed 2003 - OTF KBNERR

* OTF KBNERR: Short, high resolution towed CTD in the middle of Cook Inlet at nominal 4 and 10m depths
* July 2003, 5min sampling frequency
* Slug: ctd_towed_otf_kbnerr
* Included: True
* Feature type: trajectoryProfile

Towed CTD Profiles.


Notes:

Two files that were about 30 minutes long were not included (mic071203 and mic072803_4-5). These data were not included in the NWGOA model/data comparison. Resampled from 5sec to 5min sampling frequency.

**Map of Towed CTD Profiles**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_otf_kbnerr")("ctd_towed_otf_kbnerr")
        
```


### CTD Towed 2004-2008 Ferry in-line - NOAA PMEL

* NOAA PMEL: Towed CTD on ferry at nominal 4m depth
* Continuous 2004 to 2008, 5min sampling frequency
* Slug: ctd_towed_ferry_noaa_pmel
* Included: True
* Feature type: trajectory


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


Notes:

The ferry regularly traveled outside of the domain of interest and those times are not included. Data was resampled from 30s to 5min sampling frequency.

**Map of Towed CTD Paths**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_ferry_noaa_pmel")("ctd_towed_ferry_noaa_pmel")
        
```


### CTD profiles 2003-2006 - OTF KBNERR

* OTF KBNERR: Repeat CTD transect from Anchor Point in Cook Inlet
* Daily in July, 2003 to 2006
* Slug: ctd_profiles_otf_kbnerr
* Included: True
* Feature type: trajectoryProfile

CTD Profiles Across Anchor Point Transect, for GEM Project 030670.

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf
Project description: https://evostc.state.ak.us/restoration-projects/project-search/monitoring-dynamics-of-the-alaska-coastal-current-and-development-of-applications-for-management-of-cook-inlet-salmon-040670/


Notes:

These data were not included in the NWGOA model/data comparison

**Map of CTD Profiles in Consistent Transect**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_otf_kbnerr")("ctd_profiles_otf_kbnerr")
        
```


### CTD profiles 2004-2005 - CMI UAF

* CMI UAF: CTD transect from East Foreland Lighthouse in Cook Inlet
* 10 cruises, approximately monthly for summer months, in 2004 and 2005
* Slug: ctd_profiles_cmi_uaf
* Included: True
* Feature type: trajectoryProfile

Seasonality of Boundary Conditions for Cook Inlet, Alaska: Transect (3) at East Foreland Lighthouse.

9 CTD profiles at stations across 10 cruises in (approximately) the same locations. Approximately monthly for summer months, 2004 and 2005.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf


Notes:

Used in the NWGOA model/data comparison.

**Map of CTD Profiles in a Transect**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_cmi_uaf")("ctd_profiles_cmi_uaf")
        
```


### CTD profiles 2004-2006 - CMI KBNERR

* CMI KBNERR: Six repeat transects, one single transect, and one time series of CTD profiles in Cook Inlet
* From 2004 to 2006
* Slug: ctd_profiles_cmi_kbnerr
* Included: True
* Feature type: trajectoryProfile

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


Notes:

Used in the NWGOA model/data comparison.

**Map of CTD Profiles in Transects**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_cmi_kbnerr")("ctd_profiles_cmi_kbnerr")
        
```


### CTD Moored 2006 - CIRCAC

* CIRCAC: Central Cook Inlet Mooring
* Two weeks in August 2006, 15 min sampling
* Slug: ctd_moored_circac
* Included: True
* Feature type: timeSeries

Central Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

CIRCAC is the Cook Inlet Regional Citizens Advisory Council. It was funded by MMS (pre-BOEM), OCS Study MMS 2009-041 funneled through the Coastal Marine Institute (University of Alaska Fairbanks).

This mooring was damaged so it was removed.

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>



Notes:



**Map of Time Series Location**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_moored_circac")("ctd_moored_circac")
        
```


### CTD Moored 2006-2008 - KBNERR

* KBNERR: Lower Cook Inlet Mooring
* Aug to Oct 2006 and June 2007 to Feb 2008, 15 min sampling
* Slug: ctd_moored_kbnerr
* Included: True
* Feature type: timeSeries

Lower Cook Inlet Mooring from: Seasonality of Boundary Conditions for Cook Inlet, Alaska

CIRCAC is the Cook Inlet Regional Citizens Advisory Council. It was funded by MMS (pre-BOEM), OCS Study MMS 2009-041 funneled through the Coastal Marine Institute (University of Alaska Fairbanks).

Part of the project:
Seasonality of Boundary Conditions for Cook Inlet, Alaska
Steve Okkonen Principal Investigator
Co-principal Investigators: Scott Pegau Susan Saupe
Final Report
OCS Study MMS 2009-041
August 2009
Report: https://researchworkspace.com/file/39885971/2009_041.pdf

<img src="https://user-images.githubusercontent.com/3487237/233167915-c0b2b0e1-151e-4cef-a647-e6311345dbf9.jpg" alt="alt text" width="300"/>



Notes:



**Map of Time Series Location**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_moored_kbnerr")("ctd_moored_kbnerr")
        
```


### CTD time series UAF

* UAF: Repeat CTD profile transect along an east-west section in central Cook Inlet
* 26-hour period on 9-10 August 2003
* Slug: ctd_time_series_uaf
* Included: True
* Feature type: trajectoryProfile

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles

Surface-to-bottom measurements of temperature, salinity, and transmissivity, as well as measurements of surface currents (vessel drift speeds) were acquired along an east-west section in central Cook Inlet, Alaska during a 26-hour period on 9-10 August 2003. These measurements are used to describe the evolution of frontal features (tide rips) and physical properties along this section during semidiurnal and diurnal tidal cycles. The observation that the amplitude of surface currents is a function of water depth is used to show that strong frontal features occur in association with steep bathymetry. The positions and strengths of these fronts vary with the semidiurnal tide. The presence of freshwater gradients alters the phase and duration of tidal currents across the section. Where mean density-driven flow is northward (along the eastern shore and near Kalgin Island), the onset of northward tidal flow (flood tide) occurs earlier and has longer duration than the onset and duration of northward tidal flow where mean density-driven flow is southward (in the shipping channel). Conversely, where mean density-driven flow is southward (in the shipping channel), the onset of southward tidal flow (ebb tide) occurs earlier and has longer duration than the onset and duration of southward tidal flow along the eastern shore and near Kalgin Island. 

Observations of hydrography and currents in central Cook Inlet, Alaska during diurnal
and semidiurnal tidal cycles
Stephen R. Okkonen
Institute of Marine Science
University of Alaska Fairbanks
Report: https://www.circac.org/wp-content/uploads/Okkonen_2005_hydrography-and-currents-in-Cook-Inlet.pdf


Notes:

Year for day 2 was corrected from 2004 to 2003. Not used in the NWGOA model/data comparison.

**Map of Transect of CTD Profiles**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_time_series_uaf")("ctd_time_series_uaf")
        
```


### CTD profiles 2005 - OSU

* OSU: Time series of CTD profiles at several locations in Cook Inlet
* June 2005
* Slug: ctd_profiles_2005_osu
* Included: False
* Feature type: timeSeriesProfile



Notes:

Locations given are too low resolution making them incorrectly on land.

**Map of Repeat CTD Profiles at Several Locations**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_profiles_2005_osu")("ctd_profiles_2005_osu")
        
```


### CTD Towed 2017-2019 - GWA

* GWA: Towed CTD at nominal 7m depth
* Approximately monthly in summer from 2017 to 2020, 5min sampling frequency
* Slug: ctd_towed_gwa
* Included: True
* Feature type: trajectory

Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2017-2020. 2017 and 2018 have salinity and temperature, 2019 and 2020 have only temperature.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Notes:

Made all longitudes negative west values, converted some local times, 2019 and 2020 only have temperature, ship track outside domain is not included, resampled from 2min to 5min.

**Map of Flow through on Ship of Opportunity**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "ctd_towed_gwa")("ctd_towed_gwa")
        
```


### Temperature towed 2011-2016 - GWA

* GWA: Towed CTD at nominal 7m depth, temperature only
* Approximately monthly in summer from 2011 to 2016, 5min sampling frequency
* Slug: temp_towed_gwa
* Included: True
* Feature type: trajectory

Temperature only: Environmental Drivers: Continuous Plankton Recorders, Gulf Watch Alaska.

This project is a component of the integrated Long-term Monitoring of Marine Conditions and Injured Resources and Services submitted by McCammon et. al. Many important species, including herring, forage outside of Prince William Sound for at least some of their life history (salmon, birds and marine mammals for example) so an understanding of the productivity of these shelf and offshore areas is important to understanding and predicting fluctuations in resource abundance. The Continuous Plankton Recorder (CPR) has sampled a continuous transect extending from the inner part of Cook Inlet, onto the open continental shelf and across the shelf break into the open Gulf of Alaska monthly through spring and summer since 2004. There are also data from 2000-2003 from a previous transect. The current transect intersects with the outer part of the Seward Line and provides complementary large scale data to compare with the more local, finer scale plankton sampling on the shelf and in PWS. Resulting data will enable us to identify where the incidences of high or low plankton are, which components of the community are influenced, and whether the whole region is responding in a similar way to meteorological variability. Evidence from CPR sampling over the past decade suggests that the regions are not synchronous in their response to ocean climate forcing. The data can also be used to try to explain how the interannual variation in ocean food sources creates interannual variability in PWS zooplankton, and when changes in ocean zooplankton are to be seen inside PWS. The CPR survey is a cost-effective, ship-of-opportunity based sampling program supported in the past by the EVOS TC that includes local involvement and has a proven track record.

Nominal 7m depth, 2011-2016.

Project overview: https://gulf-of-alaska.portal.aoos.org/#metadata/87f56b09-2c7d-4373-944e-94de748b6d4b/project


Notes:

Converted some local times, ship track outside domain is not included.

**Map of Flow through on Ship of Opportunity**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "temp_towed_gwa")("temp_towed_gwa")
        
```


### Moorings from University of Alaska Fairbanks (UAF)

* UAF Moorings: Kodiak Island and Peterson Bay, Cook Inlet
* From 2013 to present, variable
* Slug: moorings_uaf
* Included: True
* Feature type: timeSeries

Moorings from UAF


Notes:



**Map of Moorings**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_uaf")("moorings_uaf")
        
```


### Moorings from National Parks Service (NPS)

* NPS Moorings: Chinitna Bay and Aguchik Island, Cook Inlet
* From 2018 to 2019, variable
* Slug: moorings_nps
* Included: True
* Feature type: timeSeries

Moorings from NPS


Notes:



**Map of Moorings**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_nps")("moorings_nps")
        
```


### Moorings from NOAA

* NOAA Moorings: Geese Island, Sitkalidak Island, Bear Cove, Anchorage, Kodiak Island, Alitak, Seldovia, Old Harbor, Boulder Point, Albatross Banks, Shelikof Strait
* From 1999 (and earlier) to 2023, variable
* Slug: moorings_noaa
* Included: True
* Feature type: timeSeries

Moorings from NOAA


Notes:



**Map of Moorings**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_noaa")("moorings_noaa")
        
```


### Moorings from Alaska Ocean Observing System (AOOS)/ Coastal Data Information Program (CDIP)

* CDIP Buoys: Lower Cook Inlet, Kodiak, Central Cook Inlet
* From , variable
* Slug: moorings_aoos_cdip
* Included: True
* Feature type: timeSeries

Moorings from AOOS/CDIP


Notes:



**Map of Moorings**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_aoos_cdip")("moorings_aoos_cdip")
        
```


### surface Temp Sal - OTF ADF&G

* OTF ADF&G: Long term station sampling
* Daily sampling mostly in July 1979 to 2021
* Slug: surface_otf_adfg
* Included: False
* Feature type: trajectoryProfile

Long term surface sampling

This project used a vessel of opportunity to collect physical oceanographic and fisheries data at six stations along a transect across lower Cook Inlet from Anchor Point (AP) to the Red River delta each day during July. Logistical support for the field sampling was provided in part by the Alaska Department of Fish and Game which has chartered a drift gillnet vessel annually to fish along this transect providing inseason projections of the size of sockeye salmon runs entering Cook Inlet. This project funded collection of physical oceanographic data on board the chartered vessel to help identify intrusions of the Alaska Coastal Current (ACC) into Cook Inlet and test six hypotheses regarding effects of changing oceanographic conditions on migratory behavior and catchability of sockeye salmon entering Cook Inlet. In 2003-2007, a conductivity-temperature-depth profiler was deployed at each station. In 2003-2005, current velocities were estimated along the transect using a towed acoustic Doppler current profiler, and salmon relative abundance and vertical distribution was estimated using towed fisheries acoustic equipment.

Willette, T.M., W.S. Pegau, and R.D. DeCino. 2010. Monitoring dynamics of the Alaska coastal current and development of applications for management of Cook Inlet salmon - a pilot study. Exxon Valdez Oil Spill Gulf Ecosystem Monitoring and Research Project Final Report (GEM Project 030670), Alaska Department of Fish and Game, Commercial Fisheries Division, Soldotna, Alaska.

Report: https://evostc.state.ak.us/media/2176/2004-040670-final.pdf


Notes:

Not used because no times associated with data.

**Map of Stations**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "surface_otf_adfg")("surface_otf_adfg")
        
```


### Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)

* Historical KBNERR Moorings: Kachemak Bay
* From 2001 to 2003, variable
* Slug: moorings_kbnerr_historical
* Included: True
* Feature type: timeSeries

Historical moorings from Kachemak Bay National Estuarine Research Reserve (KBNERR)
    
More information: https://accs.uaa.alaska.edu/kbnerr/


Notes:

These are accessed from Research Workspace.

**Map of Moorings**

```{code-cell}
getattr(chr.src.plot_dataset_on_map, "moorings_kbnerr_historical")("moorings_kbnerr_historical")
        
```
