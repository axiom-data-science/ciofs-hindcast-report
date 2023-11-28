"""Plot tidal ellipses for HF Radar model-data comparisons.

Also plot surfaces of the tidal constants.
"""

import cartopy
import ciofs_hindcast_report as chr
import cmocean.cm as cmo
import intake
import matplotlib.pyplot as plt
import numpy as np
import ocean_model_skill_assessor as omsa
import pathlib
import ttide as tt
import xarray as xr

def calc_tidecons(ds, save_file):
    """for model output"""

    if not save_file.is_file():
        # calculate tidal constituents from hourly data
        vel = ds.cf[ukey] + 1j*ds.cf[vkey]
        tfitall = np.zeros((ds.cf[ukey].shape[1], ds.cf[ukey].shape[2], len(tidecons), 4))* np.nan
        for i in range(ds.cf[ukey].shape[1]):
            for j in range(ds.cf[ukey].shape[2]):
                if vel[:,i,j].notnull().sum() > 5:
                    try:
                        tfit = tt.t_tide(vel[:,i,j].values, out_style=None)
                    except ValueError:
                        import pdb; pdb.set_trace()
                    # major, minor, inclination, phase
                    for ntidecon, tidecon in enumerate(tidecons):
                        try:
                            tfitall[i,j,ntidecon,:] = tfit["tidecon"][tfit["nameu"] == bytes(f"{tidecon}  ", encoding="utf-8")].squeeze()[[0,2,4,6]]
                        except IndexError:
        #                         print(f"did not run for {tidecon}")
                            tfitall[i,j,ntidecon,:] = np.nan

        # add tidal constituent constants to dataset
        ds2 = xr.Dataset()
        ds2["tidecons"] = (("x", "y", "ntidecons", "tideconvals"), tfitall)
        ds2["ntidecons"] = tidecons
        ds2["tideconvals"] = ["major", "minor", "inclination", "phase"]
        ds2 = ds2.assign_coords({"lon": ds["lon"], "lat": ds["lat"]})

        # save
        ds2.to_netcdf(save_file)
    else:
        ds2 = xr.open_dataset(save_file)
    
    return ds2

def match_nans(ds, dd):
    ds_vars = [var for var in list(ds.data_vars) if ds[var].ndim >= 3]
    inds = (~dd[list(dd.data_vars)[0]].isnull()).values
    ds_masked = ds[ds_vars].where(inds) 
    return ds_masked


def plot_surfaces(cat, source_name, extent, model, obs, tide, which, unit, cmap_seq, cmap_div,
                  denom, model_file_name1, featuretype, figsize, proj):
    plot_description = f'Surface currents from {cat[source_name].metadata["minTime"][:10]} to {cat[source_name].metadata["maxTime"][:10]}'
    model = match_nans(model, obs)
    obssub = (obs["tidecons"].sel(ntidecons=tide, tideconvals=which)/denom).to_dataset()
    obssub["T"] = "other"
    obssub["tidecons"].encoding["coordinates"] = "lat lon"
    
    modelsub = model["tidecons"].sel(ntidecons=tide, tideconvals=which).to_dataset()
    modelsub["T"] = "other"
    modelsub = modelsub.assign_coords({"lat": obssub.lat, "lon": obssub.lon})
    modelsub["tidecons"].encoding["coordinates"] = "lat lon"
    
    # unwrap phase
    if which == "phase":
        phasevaluesobs = obssub["tidecons"].values.copy()
        indobs = ~np.isnan(phasevaluesobs)
        unwrappedobs = np.unwrap(phasevaluesobs[indobs], period=360)
        
        phasevaluesmodel = modelsub["tidecons"].values.copy()
        indmodel = ~np.isnan(phasevaluesmodel)
        unwrappedmodel = np.unwrap(phasevaluesmodel[indmodel], period=360)
        if ((unwrappedobs < 0).sum() > 3) or ((unwrappedmodel < 0).sum() > 3):
            # import pdb; pdb.set_trace()
            unwrappedobs += 360
            unwrappedmodel += 360
        phasevaluesmodel[indmodel] = unwrappedmodel
        phasevaluesobs[indobs] = unwrappedobs
        # obssub["tidecons"].values = phasevalues
        
        # check if range of resultant phases is more than originally in which case use original
        newmin = min(np.nanmin(phasevaluesmodel), np.nanmin(phasevaluesobs))
        newmax = max(np.nanmax(phasevaluesmodel), np.nanmax(phasevaluesobs))
        newdiff = newmax - newmin
        
        oldmin = min(np.nanmin(modelsub["tidecons"]), np.nanmin(obssub["tidecons"]))
        oldmax = max(np.nanmax(modelsub["tidecons"]), np.nanmax(obssub["tidecons"]))
        olddiff = oldmax - oldmin
        
        if newdiff < olddiff:  # switch to new setup
            obssub["tidecons"].values = phasevaluesobs
            modelsub["tidecons"].values = phasevaluesmodel

        
        # phasevalues = modelsub["tidecons"].values
        # ind = ~np.isnan(phasevalues)
        # unwrapped = np.unwrap(phasevalues[ind], period=360)
        # if any(unwrapped < 0):
        #     unwrapped += 360
        # phasevalues[ind] = unwrapped
        
    #     cmap_div = cmap_seq
    # else:
    #     cmap_div = cmo.tarn

    key_variable_data = "tidecons"
    stats = omsa.stats.compute_stats(
        obssub.cf[key_variable_data], modelsub.cf[key_variable_data].squeeze()
    )
    title = omsa.plot.create_title(stats, f"{tide}-{which}", obssub, source_name, featuretype, plot_description)
    xname, yname, zname = "longitude", "latitude", "tidecons"
    xlabel, ylabel, zlabel = "", "", f"{tide} {which.capitalize()} Tidal Constant [{unit}]"

    figname = pathlib.Path(model_file_name1).parent.parent / "out" / f"hfradar_{source_name}_{tide}-{which}.png"
    with xr.set_options(cmap_sequential=cmap_seq, cmap_divergent=cmap_div):
        fig = omsa.plot.surface.plot(
            obssub.squeeze(),
            modelsub.squeeze(),
            xname,
            yname,
            zname,
            title,
            xlabel=xlabel,
            ylabel=ylabel,
            zlabel=zlabel,
            model_title=model_name.upper(),
            kind="pcolormesh",
            plot_on_map=True,
            figname=figname,
            return_plot=True,
            figsize=figsize,
            proj=proj,
            extent=extent,
            # **kwargs,
        )
    plt.close(fig)


def plot_ellipse(cat, source_name, figsize_ell, proj, extent, dd, tide, obs, 
                 model, legend, model_name,model_file_name1, denom):
    suptitle = f'{tide} tidal ellipses from surface currents in dataset {source_name} ({cat[source_name].metadata["minTime"][:10]} to {cat[source_name].metadata["maxTime"][:10]})'
    

    fig, axes = plt.subplots(
        1,
        3,
        figsize=figsize_ell,
        layout="constrained",
        subplot_kw=dict(projection=proj, frameon=False),
    )
    #  sharex=True, sharey=True)
    omsa.plot.map.setup_ax(axes[0], left_labels=True, bottom_labels=True, top_labels=False, fontsize=12)
    axes[0].set_extent(extent, crs=omsa.plot.map.pc)
    axes[0].set_title("Observation", fontsize=omsa.plot.surface.fs_title)

    from matplotlib.collections import EllipseCollection

    dx, dy = dd
    X, Y = obs.lon.values[::dx,::dy], obs.lat.values[::dx,::dy]
    XY = np.column_stack((X.ravel(), Y.ravel()))
    # major, minor, inclination, phase
    ww = obs["tidecons"].sel(ntidecons=tide)[::dx,::dy,0].values/100/denom
    hh = obs["tidecons"].sel(ntidecons=tide)[::dx,::dy,1].values/100/denom
    aa = obs["tidecons"].sel(ntidecons=tide)[::dx,::dy,2].values
    # ww = tfitall["M2"][::dx,::dy,0] / 800
    # hh = tfitall["M2"][::dx,::dy,1] / 800
    # aa = tfitall["M2"][::dx,::dy,2]
    ec = EllipseCollection(ww, hh, aa, units='width', offsets=XY,
                            offset_transform=omsa.plot.map.pc,
                            color="0.5", lw=1, ec="0.3")
    axes[0].add_collection(ec, omsa.plot.map.pc)

    # add legend ellipse
    ec = EllipseCollection([legend[0]/denom], [legend[1]/denom], [0], units='width', offsets=[extent[0]+0.1, extent[3]-.025],
                        offset_transform=omsa.plot.map.pc,
                        color="0.5", lw=1, ec="0.3", zorder=10)#, alpha=0.5)
    axes[0].add_collection(ec, omsa.plot.map.pc)
    axes[0].annotate(f"{legend[0]} m/s major\n{legend[1]} minor", (extent[0]+0.05, extent[3]-.08), xycoords=omsa.plot.map.pc)

    omsa.plot.map.setup_ax(axes[1], left_labels=False, bottom_labels=True, top_labels=False, fontsize=12)
    axes[1].set_extent(extent, crs=omsa.plot.map.pc)
    axes[1].set_title(model_name.upper(), fontsize=omsa.plot.surface.fs_title)

    # major, minor, inclination, phase
    wwm = model["tidecons"].sel(ntidecons=tide)[::dx,::dy,0].values/denom
    hhm = model["tidecons"].sel(ntidecons=tide)[::dx,::dy,1].values/denom
    aam = model["tidecons"].sel(ntidecons=tide)[::dx,::dy,2].values
    ec = EllipseCollection(wwm, hhm, aam, units='width', offsets=XY,
                        offset_transform=omsa.plot.map.pc,
                        color="0.5", lw=1, ec="0.3")#, alpha=0.5)
    axes[1].add_collection(ec, omsa.plot.map.pc)
    
    omsa.plot.map.setup_ax(axes[2], left_labels=False, bottom_labels=True, top_labels=False, fontsize=12)
    axes[2].set_extent(extent, crs=omsa.plot.map.pc)
    axes[2].set_title("Obs - Model", fontsize=omsa.plot.surface.fs_title)
    wwdiff = ww - wwm
    hhdiff = hh - hhm
    aadiff = aa - aam
    ec = EllipseCollection(wwdiff, hhdiff, aadiff, units='width', offsets=XY,
                        offset_transform=omsa.plot.map.pc,
                        color="0.5", lw=1, ec="0.3")#, alpha=0.5)
    axes[2].add_collection(ec, omsa.plot.map.pc)

    fig.suptitle(suptitle, wrap=True, fontsize=omsa.plot.surface.fs_title)  # , loc="left")
    figname = pathlib.Path(model_file_name1).parent.parent / "out" / f"hfradar_{source_name}_{tide}_ellipses.png"
    fig.savefig(figname, dpi=100)  # , bbox_inches="tight")
    
    
    plt.close(fig)


model_name = "ciofs"  # "ciofs"

slug = "hfradar"

cat = intake.open_catalog(chr.CAT_NAME(slug))
source_names = [
    'lower-ci_system-B_2006-2007_tidecons_base',
 'upper-ci_system-A_2002-2003_tidecons_base',
 'upper-ci_system-A_2009_tidecons_base'
]

dds = [
    [1, 3],
    [2, 3],
       [4, 6],
]
legends = [
    {"M2": [0.75, 0.25], "K1": [0.1, 0.025],},
    {"M2": [0.5, 0.1], "K1": [0.05, 0.01],},
    {"M2": [1.0, 0.3], "K1": [0.1, 0.03],},
]
denoms_ell = {"M2": 8, "K1": 2}

extents = [
    (-153.05, -151.7, 59.1, 60.0), 
    (-152.15, -151.2, 60.2, 60.8), 
    (-152.15, -151.2, 60.2, 60.8)
    ]
figsize = (15,8.5)
figsize_ell = (15,7)

# source_name = source_names[0]
# extent = extents[0]
for source_name, extent, dd, legend in zip(source_names, extents, dds, legends):
    print(source_name)
    obs = cat[source_name].read()
    source_name = source_name.split("_tide")[0]
    proj = cartopy.crs.LambertAzimuthalEqualArea(central_longitude=np.mean(extent[:2]), central_latitude=np.mean(extent[2:]))
    # proj = cartopy.crs.AzimuthalEquidistant(central_longitude=-151, central_latitude=60)

    tidecons = ["M2","S2","K2","K1","N2","P1","O1","Q1"]
    whichs = ["major","minor", "inclination", "phase"]
    featuretype = "grid"

    # Model output
    ukey, vkey = "east", "north"
    model_file_name1 = f"/Users/kthyng/Library/Caches/ocean-model-skill-assessor/hfradar_{model_name}/model_output/hfradar_{source_name}_all_{ukey}.nc"
    model_file_name2 = f"/Users/kthyng/Library/Caches/ocean-model-skill-assessor/hfradar_{model_name}/model_output/hfradar_{source_name}_all_{vkey}.nc"
    ds = xr.open_mfdataset([model_file_name1, model_file_name2])
    ds = ds.assign_coords({"lon": ds.lon,"lat": ds.lat, "s_rho": ds.s_rho})

    # run on model output (already run on data)
    save_file = pathlib.Path(model_file_name1).parent / f"{slug}_{source_name}_tidecons.nc"
    model = calc_tidecons(ds, save_file)

    model = match_nans(model, obs)

    ## PLOTS ##


    for tide in tidecons:
        
        # tidal ellipses
        if tide in ["M2","K1"]:
            
            plot_ellipse(cat, source_name, figsize_ell, proj, extent, dd, tide, obs, 
                 model, legend[tide], model_name,model_file_name1, denoms_ell[tide])            
            
        
        for which in whichs:
            
            if which in ["phase", "inclination"]:
                cmap_seq = cmo.phase
                cmap_div = cmo.phase
                unit = "deg"
                denom = 1
            else:
                cmap_seq = cmo.rain
                cmap_div = cmo.tarn
                unit = "m"
                denom = 100
        
            # Surface Plots
            print(tide,which)
            plot_surfaces(cat, source_name, extent, model, obs, tide, which, unit, cmap_seq, cmap_div, 
                          denom, model_file_name1, featuretype, figsize, proj)
