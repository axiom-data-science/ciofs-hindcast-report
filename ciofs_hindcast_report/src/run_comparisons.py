"""run the comparison OMSA calls necessary to make the comparison notebooks."""

import ocean_model_skill_assessor as omsa
import ciofs_hindcast_report as chr
import intake
import cf_xarray

import xarray as xr
import pandas as pd

import extract_model as em
import xroms



text = """
sources:
  ciofs:
    driver: zarr
    description: CIOFS hindcast
    args:
      consolidated: true
      urlpath: http://xpublish-ciofs.srv.axds.co/datasets/ciofs_hindcast/zarr/
      chunks: {}
      
  nwgoa:
    driver: zarr
    description: NWGOA hindcast
    args:
      consolidated: true
      urlpath: http://xpublish-nwgoa.srv.axds.co/datasets/nwgoa_all/zarr/
"""

file = open("test_cat.yaml","w")
file.writelines(text)
file.close()

cat_model = intake.open_catalog("test_cat.yaml")


def moorings_noaa(slug):

    project_name = slug # "ciofs_moorings" 
    # slug = "moorings_kbnerr_homer"
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    
    # Deal with long time series which have to be split into smaller chunks
    # and have mean subtracted to get anomalies.
    vars = ["temp"]
    source_names = ["noaa_nos_co_ops_9455500", "noaa_nos_co_ops_9455920", "noaa_nos_co_ops_9457804",
                    "noaa_nos_co_ops_kdaa2", "wmo_46077"]
    models = ["ciofs", "nwgoa"]
    
    for var in vars:
        for source_name in source_names:

            # time series for modification
            df = cat[source_name].read()
            monthly_mean = df.cf[var].groupby(df.cf["T"].dt.month).mean()
            ts_mods = [{"function": chr.src.utils.calculate_anomaly, 
                        "inputs": dict(monthly_mean=monthly_mean),}]

            start_time = cat[source_name].metadata["minTime"].replace("Z","")
            if start_time < "1999-01-01":
                start_time = "1999-01-01"
            end_time = cat[source_name].metadata["maxTime"].replace("Z","")

            if pd.Timestamp(end_time) - pd.Timestamp(start_time) > pd.Timedelta("365 days"):
                # split into 6 month time periods
                dates = pd.date_range(start_time, end_time, freq="6MS")
                for i, date in enumerate(dates[:-1]):
                    start_time_use, end_time_use = date, dates[i+1]
                    
                    for model in models:

                        omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                                preprocess=True,
                                vocabs="general", 
                                mode="a",
                                key_variable=var, 
                                alpha=5, dd=5, 
                                interpolate_horizontal=False,
                                model_source_name=model,
                                catalog_source_names=[source_name],
                                model_only=False,
                                user_min_time=start_time_use, user_max_time=end_time_use,
                                check_in_boundary=False,
                                need_xgcm_grid=False,
                                ts_mods=ts_mods,
                                plot_map=False,
                                )
