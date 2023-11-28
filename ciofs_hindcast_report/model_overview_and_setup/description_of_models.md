(page:model_description)=
# Model Descriptions

## CIOFS

The Cook Inlet Operational Forecast System (CIOFS)
[{cite:t}`noaaCookInlet`, {cite:t}`zhang_ciofs`] is focused on simulating the coastal
oceanography of Cook Inlet in Alaska, based on the Regional Ocean
Modeling System (ROMS) [{cite:t}`Shchepetkin2005`, {cite:t}`McWilliams2009`]. The model
domain extends from the offshore waters of the inlet to the inner
estuaries and navigational channels ({numref}`Fig. {number}<fig-ciofs-bathy>`). The horizontal grid has 1,132 by
777 grid points, with spacing ranging from 10 meters in the estuaries to
3.5 kilometers in the deeper offshore waters. Vertically, the model uses
30 sigma layers that follow the bathymetric terrain. Bathymetry is based
on the best available soundings, shoreline, and digital elevation data
in order to accurately represent the complex inlet geometry and support
wetting/drying processes.



```{figure} ../report/ciofs_bathy.png
---
name: fig-ciofs-bathy
---
CIOFS domain with bathymetry.
```


The 20-year hindcast (1999--2018) product with hourly 3D hydrographic
fields was produced by Axiom Data Science. For surface forcing, CIOFS
primarily uses wind, temperature, and humidity fields from ECMWF
Reanalysis v5 (ERA5) {cite:p}`Hersbach2020`. Lateral ocean boundary conditions
including temperature, salinity, and sub-tidal water levels come from
HYCOM Global Ocean Forecasting System (GOFS) 3.1 Reanalysis
{cite:p}`hycomgofs`. Tidal forcing at the open boundary comes from the NOS
CO-OPS version of CIOFS [{cite:t}`noaaCookInlet`; {cite:t}`zhang_ciofs`] which is derived
from the ADCIRC tidal database {cite:p}`adcircADCIRCTidal`. River inputs use
real-time discharge observations from 12 major rivers supplied by the
USGS {cite:p}`usgs_2016`.

See more details about the open boundary forcing files in {ref}`page:open_boundaries` and river forcing files in {ref}`page:river1` and {ref}`page:river2`. The CIOFS hindcast landing page in the AOOS portal is [https://portal.aoos.org/#module-metadata/ff82ba46-9d33-487e-aa83-d57c7521d6b0](https://portal.aoos.org/#module-metadata/ff82ba46-9d33-487e-aa83-d57c7521d6b0) and for the forecast is [https://portal.aoos.org/#module-metadata/60fb5c3c-3b2f-44eb-9d14-536fcaeebbe6](https://portal.aoos.org/#module-metadata/60fb5c3c-3b2f-44eb-9d14-536fcaeebbe6).

## NWGOA

The NWGOA model {cite:t}`Danielson2020` is a high-resolution regional ocean
model focused on the northwest Gulf of Alaska, including Cook Inlet,
Shelikof Strait, Prince William Sound, and Kodiak Island  ({numref}`Fig. {number}<fig-nwgoa-bathy>`). It uses the
Regional Ocean Modeling System (ROMS) and has a horizontal resolution of
approximately 1.5 km with 50 vertical layers. The model domain extends
1,100 km in the east-west direction and 550 km in the north-south
direction, capturing important freshwater source regions like the Copper
River delta and Prince William Sound.


```{figure} ../report/nwgoa_bathy.png
---
name: fig-nwgoa-bathy
---
NWGOA domain with bathymetry.
```

It is one-way nested within a larger 10 km Northeast Pacific (NEP) model
that provides oceanic boundary conditions. Atmospheric forcing comes
from the MERRA global reanalysis product {cite:p}`Rienecker2011`. Tides are
included based on the global TPXO tidal inversion {cite:p}`Egbert2002`. A
high-resolution gridded terrestrial discharge model was used to better
represent freshwater inputs from rivers and coastal runoff. The model
uses an updated bathymetric grid based on the 1 km Alaska Region Digital
Elevation Model (ARDEM) and includes a sea ice model
[{cite:t}`Danielson2011`; {cite:t}`Danielson2015`]. It was integrated from 1999 to 2008 to
overlap with available observations.

The NWGOA model landing page in the AOOS portal is [https://portal.aoos.org/#module-metadata/641707a8-e4f6-48d9-821d-f858cf6be410](https://portal.aoos.org/#module-metadata/641707a8-e4f6-48d9-821d-f858cf6be410).