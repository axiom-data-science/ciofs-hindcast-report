"""From notebook plot_hfradar_ss.ipynb"""

import cartopy
import ciofs_hindcast_report as chr
import cmocean.cm as cmo
import matplotlib.pyplot as plt
import numpy as np
import ocean_model_skill_assessor as omsa
import pathlib
import xarray as xr

import warnings
warnings.filterwarnings('ignore')

import cf_pandas as cfp
import cf_xarray as cfx

vocab = cfp.Vocab()

reg = cfp.Reg(include_exact="u", ignore_case=True)
vocab.make_entry("east", reg.pattern(), attr="name")
reg = cfp.Reg(include_exact="u_eastward", ignore_case=True)
vocab.make_entry("east", reg.pattern(), attr="name")

reg = cfp.Reg(include_exact="v", ignore_case=True)
vocab.make_entry("north", reg.pattern(), attr="name")
reg = cfp.Reg(include_exact="v_northward", ignore_case=True)
vocab.make_entry("north", reg.pattern(), attr="name")

cfx.set_options(custom_criteria=vocab.vocab)

def read_files(model_name, which, source_name):
    base = f"/Users/kthyng/Library/Caches/ocean-model-skill-assessor/hfradar_{model_name}/processed"
    
    if which == "tidal":
        path = f"hfradar_{source_name}_all_east_remove-under-50-percent-data_units-to-meters"
        path_data = pathlib.Path(base) / f"{path}_data.nc"
        path_model_east = pathlib.Path(base) / f"{path}_model.nc"
        path = f"hfradar_{source_name}_all_north_remove-under-50-percent-data_units-to-meters"
        path_model_north = pathlib.Path(base) / f"{path}_model.nc"
    elif which == "subtidal":
        path = f"hfradar_{source_name}_all_east_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H"
        path_data = pathlib.Path(base) / f"{path}_data.nc"
        path_model_east = pathlib.Path(base) / f"{path}_model.nc"
        path = f"hfradar_{source_name}_all_north_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H"
        path_model_north = pathlib.Path(base) / f"{path}_model.nc"
    obs = xr.open_dataset(path_data)
    model_east = xr.open_dataset(path_model_east)
    model_east = model_east.assign_coords({"lon": model_east["lon"], "lat": model_east["lat"]})
    model_north = xr.open_dataset(path_model_north)
    model_north = model_north.assign_coords({"lon": model_north["lon"], "lat": model_north["lat"]})
    return obs, model_east, model_north

def calculate_ss(obs, model, key):
    ssarr = np.zeros(model.cf[key].shape[1:])*np.nan
    for i in range(obs.cf[key].shape[1]):
        for j in range(obs.cf[key].shape[2]):
            if not obs.cf[key][:,i,j].isnull().all() and not model.cf[key][:,i,j].isnull().all():
                ssarr[i,j] = omsa.stats.compute_murphy_skill_score(obs.cf[key][:,i,j], model.cf[key].squeeze()[:,i,j])
    ss = xr.Dataset()
    ss[key] = (("x", "y"), ssarr)
    ss = ss.assign_coords({"lon": model["lon"], "lat": model["lat"]})
    
    return ss[key]


source_names = [
    'lower-ci_system-B_2006-2007',
 'upper-ci_system-A_2002-2003',
 'upper-ci_system-A_2009'
]

extents = [
    (-153.05, -151.7, 59.1, 60.0), 
    (-152.15, -151.2, 60.2, 60.8), 
    (-152.15, -151.2, 60.2, 60.8)
    ]

# Calculate skill scores

ss = {}
for source_name in source_names:
    sss = []
    for model_name in ["nwgoa", "ciofs"]:
        
        for which in ["tidal","subtidal"]:
            
            if source_name == "upper-ci_system-A_2009" and model_name == "nwgoa":
                continue

            obs, model_east, model_north = read_files(model_name, which, source_name)
            sstemp1 = calculate_ss(obs, model_east, "east")
            sstemp2 = calculate_ss(obs, model_north, "north")
            sstemp = xr.merge([sstemp1, sstemp2])
            sstemp = sstemp.rename({"east": f"{model_name}_{which}_east", "north": f"{model_name}_{which}_north"})
            sss.append(sstemp)

    ss[source_name] = xr.merge(sss, compat='override')
    # ss[source_name] = ss[source_name].rename({"east": f"{model_name}_{which}_east", "north": f"{model_name}_{which}_north"})

for source_name in source_names:
    # ss[source_name].to_netcdf(f"supporting_files/hfradar_ss_{source_name}.nc")
    ss[source_name].to_netcdf(f"{chr.COMP_PAGE_DIR('overview_hfradar')}/hfradar_ss_{source_name}.nc")


# make plots
fs = 14
def plot(model_name, source_name, which, extent):
    proj = cartopy.crs.LambertAzimuthalEqualArea(central_longitude=np.mean(extent[:2]), central_latitude=np.mean(extent[2:]))

    fig, axes = plt.subplots(1, 2, layout="constrained", figsize=(11,8), subplot_kw = dict(projection=proj, frameon=False))

    key = f"{model_name}_{which}_east"
    omsa.plot.map.setup_ax(axes[0], left_labels=True, bottom_labels=True, top_labels=False, fontsize=12)
    ss[source_name][key].plot(x="lon", y="lat", vmin=-1, ax=axes[0], transform=omsa.plot.map.pc, 
                              cmap=cmo.curl, add_colorbar=False)
    axes[0].set_extent(extent)
    axes[0].set_title("Eastward Surface Velocity [m/s]", fontsize=fs)

    key = f"{model_name}_{which}_north"
    omsa.plot.map.setup_ax(axes[1], left_labels=False, bottom_labels=True, top_labels=False, fontsize=14)
    mappable = ss[source_name][key].plot(x="lon", y="lat", vmin=-1, ax=axes[1], transform=omsa.plot.map.pc, 
                                         cmap=cmo.curl, add_colorbar=False)
    axes[1].set_extent(extent)
    axes[1].set_title("Northward Surface Velocity [m/s]", fontsize=fs)

    cbar1 = fig.colorbar(mappable, ax=axes, orientation="horizontal", shrink=0.5)
    cbar1.set_label("Skill Score", fontsize=fs)
    cbar1.ax.tick_params(axis="both", labelsize=13)

    # figname = f"{chr.PATH_OUTPUTS_COMP_PAGES}/plots/hfradar_{source_name}_{model_name}_{which}.png"
    figname = f"{chr.COMP_PAGE_DIR('overview_hfradar')}/hfradar_{source_name}_{model_name}_{which}.png"
    fig.suptitle(f"{model_name.upper()} Skill Score with {which.capitalize()} {source_name.split('_tidecons')[0]}", fontsize=16);
    fig.savefig(figname, dpi=100)
    plt.close(fig)

# model_name, source_name, which, extent = "ciofs", source_names[0], "subtidal", extents[0]

for source_name, extent in zip(source_names, extents):
    sss = []
    for model_name in ["nwgoa", "ciofs"]:
        
        for which in ["tidal","subtidal"]:
            
            if source_name == "upper-ci_system-A_2009" and model_name == "nwgoa":
                continue

            plot(model_name, source_name, which, extent)
