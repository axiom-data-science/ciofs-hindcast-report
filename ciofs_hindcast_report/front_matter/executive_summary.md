# Summary and Recommendations

## Summary

A 24-year (1999–2022) hindcast simulation for the Cook Inlet Operational Forecast System (CIOFS) model has been run and made publicly accessible [^ciofs_hindcast] in order to meet the goal of the Cook Inlet Circulation Modeling project to develop the resources and tools needed to calculate oil spill trajectories. The operational version of CIOFS [^ciofs_forecast] is run by the National Ocean Service Center for Operational Oceanographic Products and Services and generates nowcasts and 48-hour forecasts 4 times per day and generally captures the highly-variable bathymetry and tides of Cook Inlet making it potentially well-suited for coastal planning and resource management applications. However, the model currently uses limited freshwater forcing and its accuracy is unclear for subtidal currents, temperature, and salinity patterns, all of which are important for ecological applications and oil spill response. To address these gaps, the Cook Inlet Circulation Model project, in addition to generating the hindcast 3-dimensional oceanographic model output, has assessed hindcast CIOFS skill by comparing it to the Northwest Gulf of Alaska (NWGOA) three-dimensional ocean circulation model [^nwgoa] and validated the CIOFS hindcasts using physical measurements to assess the accuracy of model
results.

We find that the MODEL-MODEL SUMMARY

The model-data comparisons point to CIOFS lacking enough freshwater input into the system to have neither realistic salinity variability nor accurate salinity. NWGOA seems to have enough freshwater input, leading to realistic variability, but not enough horizontal resolution to accurate calculate its transport. The major seasonal sea water temperature signal is well-captured in both models, but temperature anomaly is not well-captured. CIOFS is better at capturing cross-channel variation than NWGOA, and NWGOA better captures vertical variation in temperature. Both models mostly capture both the tidal and subtidal sea surface height well. Additionally, both model capture along-channel surface currents in two channels, but mostly do poorly with across-channel currents, and subtidal in either direction. CIOFS performs better than NWGOA for horizontal speed so is capturing the kinetic energy in the model but missing the directionality which may be related to local bathymetric gradients that are not in the bathymetry data.


The Cook Inlet Circulation Modeling project contributes to the OSRI’s main goals to
understand Arctic and sub-Arctic marine environments, inform oil spill prevention and response,
as well as enhance oil spill response efforts. Outputs from this effort will help drive future
development of particle trajectory tools for oil spill response planning, resource management,
and data visualizations to better meet the needs of marine pilots and industry in Cook Inlet.

## Recommendations

The CIOFS hindcast model requires almost 100TB of storage space, presenting a challenge for serving it. The CIOFS hindcast model, CIOFS operational model, and NWGOA are all available through a THREDDS Data Server (TDS), a typical way to serve model output. We also experimented with serving the model output using `xpublish` [^xpublish], which provides a modern approach for serving files via multiple API endpoints. This approach has potential but is also still under active development. Assuming development goes well, we expect to serve through `xpublish` more over time.


[^ciofs_hindcast]: [https://portal.aoos.org/#module-metadata/ff82ba46-9d33-487e-aa83-d57c7521d6b0](https://portal.aoos.org/#module-metadata/ff82ba46-9d33-487e-aa83-d57c7521d6b0)
[^ciofs_forecast]: [https://portal.aoos.org/#module-metadata/60fb5c3c-3b2f-44eb-9d14-536fcaeebbe6](https://portal.aoos.org/#module-metadata/60fb5c3c-3b2f-44eb-9d14-536fcaeebbe6)
[^nwgoa]: [https://portal.aoos.org/#module-metadata/641707a8-e4f6-48d9-821d-f858cf6be410](https://portal.aoos.org/#module-metadata/641707a8-e4f6-48d9-821d-f858cf6be410)
[^xpublish]: [https://xpublish.readthedocs.io/](https://xpublish.readthedocs.io/)

