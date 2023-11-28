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

# DONE ctd_transects_gwa_transect_6-2022-07-21_salt.nc
# transect_7-2022-07-21 salt
# transect_9-2022-07-23 salt
# transect_9-2022-08-24 salt
# transect_AlongBay-2022-07-21 salt
# transect_AlongBay-2022-08-24 both


slugs = [        
         "ctd_transects_barabara_to_bluff_2002_2003",
        "ctd_transects_otf_kbnerr",  #
        "ctd_transects_cmi_kbnerr",  #
        "ctd_transects_cmi_uaf", 
        "ctd_transects_gwa", #
        "ctd_transects_misc_2002",
        "ctd_transects_uaf",  #
]
models = ["ciofs","nwgoa"]
# key_variables=["salt"]
# vardescs = ["Salinity"]
key_variables=["temp","salt"]
vardescs = ["Sea temperature [C]", "Salinity"]

for slug in slugs:
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    # source_names = ["2004-07-15"]
    for model in models:

        kwargs_plot = dict(
            # figsize=(20,6),
            # yincrease=False,
            # invert_yaxis=True,
            model_title=model.upper(),
            make_Z_negative = "obs",
        )
        project_name = f"{slug}_{model}"

        for key_variable, vardesc in zip(key_variables, vardescs):
            slugdesc = (" ".join(slug.split("ctd_transects_")[1].split("_"))).title()
            plot_description = f"{slugdesc}: {vardesc} from CTD transect"
            omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                     preprocess=True,
                     vocabs="general", 
                     mode="a",
                     key_variable=key_variable, 
                     alpha=5, dd=5, 
                     interpolate_horizontal=True,
                     want_vertical_interp=True,
                     extrap=False,
                     model_source_name=model,
                     catalog_source_names=source_names,
                     model_only=False,
                     # user_min_time=start_time_use, user_max_time=end_time_use,
                     check_in_boundary=False,
                     need_xgcm_grid=True,
                     # ts_mods=ts_mods,
                     plot_map=False,
                     vocab_labels="vocab_labels",
                     plot_count_title=False,
                         override_processed=False,
                         override_stats=False,
                         override_plot=True,
                         plot_description=plot_description,
                         kwargs_plot=kwargs_plot,
                    )
