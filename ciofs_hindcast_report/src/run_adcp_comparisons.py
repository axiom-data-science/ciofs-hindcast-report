import ocean_model_skill_assessor as omsa
import ciofs_hindcast_report as chr
import intake
import cf_xarray as cfx
import cf_pandas as cfp

# import model_catalogs as mc
import xarray as xr
import pandas as pd

import extract_model as em
import xroms
import oceans.filters
import cmocean.cm as cmo


# import warnings
# warnings.filterwarnings('ignore')

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


slugs = [
    # "adcp_moored_noaa_coi_2005",
    # "adcp_moored_noaa_coi_other",
    # "adcp_moored_noaa_kod_1",
    "adcp_moored_noaa_kod_2",
]

models = ["ciofs"]
# models = ["ciofs","nwgoa"]

key_variables=["speed","along","across"]
vardescs = ["Horizontal Speed", "Along-Channel Velocity", "Across-Channel Velocity"]

# apply subtidal filter across dataset
def subtidal_dataset(ds):
    import cf_xarray
    for var in list(ds.data_vars):
        # apply to variable in Dataset if it has Time
        if len(cf_xarray.accessor._get_all(ds[var], "T")) > 0:
            ds[var] = oceans.filters.pl33tn(ds[var], mode="same")
    return ds


ts_mods = [
    [{"function": subtidal_dataset, "inputs": dict(), "name_mod": "subtidal",},],
          [],
          ]

xcmocean_options=dict(divin={'along': cmo.delta, 'across': cmo.delta}, 
                      regexin={'along': 'along', 'across':'across'}, 
                      seqin={'along': cmo.speed, 'across': cmo.speed})

kwargs_plot = dict(figsize=(20,6))

for slug in slugs:
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    for model in models:
        project_name = f"{slug}_{model}"
        
        kwargs_plot.update({"model_title": model.upper()})
        
        if "adcp_moored_noaa_kod" in slug and model == "nwgoa":
            continue
        
        for ts_mod, ts_mod_name in zip(ts_mods, ["Subtidal","Tidal"]):

            for key_variable, vardesc in zip(key_variables,vardescs):
                plot_description = f"{ts_mod_name.capitalize()} {vardesc.lower()} from moored ADCP"
                omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                         preprocess=True,
                         vocabs=None,#"general", 
                         mode="a",
                         key_variable=key_variable, 
                         alpha=5, dd=5, 
                         interpolate_horizontal=False,
                         want_vertical_interp=True,
                         model_source_name=model,
                         catalog_source_names=source_names,
                         model_only=False,
                         # user_min_time=start_time_use, user_max_time=end_time_use,
                         check_in_boundary=False,
                         need_xgcm_grid=False,  # don't need because model output is already?
                         ts_mods=ts_mod,
                         plot_map=False,
                         plot_count_title=False,
                         vocab_labels="vocab_labels",
                         xcmocean_options=xcmocean_options,
                         # override_model=False,
                         override_processed=False,
                         override_stats=False,
                         override_plot=True,
                         plot_description=plot_description,
                         kwargs_plot=kwargs_plot,
                        )
