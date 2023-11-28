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
    # "ctd_profiles_2005_noaa",  # done
        # "ctd_profiles_emap_2002",  # done
        # "ctd_profiles_emap_2008",  # done
        "ctd_profiles_kachemack_kuletz_2005_2007",  # done
        # "ctd_profiles_kb_small_mesh_2006", # done
        # "ctd_profiles_kbay_osu_2007", # done
        # "ctd_profiles_piatt_speckman_1999",  # done
        # "ctd_profiles_usgs_boem", # done
]
# models = ["ciofs"]
models = ["nwgoa","ciofs"]
key_variables=["temp","salt"]
vardescs = ["Sea temperature [C]", "Salinity"]


for slug in slugs:
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    # source_names = ["502"]
    # source_names = ['101.0']

    for model in models:
        project_name = f"{slug}_{model}"
        kwargs_plot = {"model_label": model.upper()}

        for key_variable, vardesc in zip(key_variables, vardescs):
            plot_description = f"{vardesc} from CTD profile"
            omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                     preprocess=True,
                     vocabs=chr.vocab,
                     # vocabs=["general", chr.vocab], 
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
                     need_xgcm_grid=True,
                     # ts_mods=ts_mods,
                     plot_map=False,
                     plot_count_title=False,
                     vocab_labels="vocab_labels",
                     plot_description=plot_description,
                     kwargs_plot=kwargs_plot,
                         override_model=False,
                         override_processed=False,
                         override_stats=True,
                         override_plot=True,
                    )
