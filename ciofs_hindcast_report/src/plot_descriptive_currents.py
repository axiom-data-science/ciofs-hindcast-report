"""Create plots for descriptive currents."""

import calendar
import ciofs_hindcast_report as chr
import pathlib
import intake
import matplotlib.pyplot as plt
import numpy as np
import ocean_model_skill_assessor as omsa
import pandas as pd
import xarray as xr
from pkg_resources import resource_filename


def plot_conditions_by_year():
    """Plot demonstrating which years we chose for comparison."""

    figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS / "model_conditions.png"

    if not figname.is_file():
        # which year has least freshwater inflow?
        base = pathlib.Path(resource_filename('ciofs_hindcast_report', 'outputs/river/'))
        filenames = sorted(base.glob("*.nc"))
        names, amount = [], []
        for filename in filenames:
            ds = xr.open_dataset(filename)
            name, am = filename.stem.split(".")[-1], float(abs(ds["river_transport"]).sum())
            names.append(name)
            amount.append(am)
        df = pd.DataFrame()

        df["names"] = names
        df["amount"] = amount
        df = df.set_index("names")
        years = df.index.str[:4]
        df.index = years

        df["btemp"] = [7.844708316646332,
        6.971172803393505,
        7.402817733629916,
        7.791735696133526,
        7.539496581666969,
        8.200041633816003,
        7.892812963405801,
        8.211099679774506,
        7.262236844656301,
        6.8742485020144315,
        6.7892666659546235,
        6.965271686999888,
        7.450744268718988,
        6.955870918497511,
        6.469058706081817,
        7.138168009871586,
        8.120113958536287,
        8.414058228099279,
        8.982089575084155,
        7.715756226007947,
        7.838449744327721,
        8.631264702608583,
        7.8968712646071735,
        7.097802804770749,
        7.424779225403698]


        df = df.loc["1999":"2008"]

        df["btemp"] = df["btemp"]/df["btemp"].max()
        df["amount"] = df["amount"]/df["amount"].max()

        years = [1999, 2003, 2005, 2008]

        ax = df.loc["1999":"2008"].plot(kind="scatter", x="amount", y="btemp")
        ax.hlines(df.loc["1999":"2008"]["btemp"].mean(), *ax.get_xlim(), "0.5")
        ax.vlines(df.loc["1999":"2008"]["amount"].mean(), *ax.get_ylim(), "0.5")
        for row in df.loc["1999":"2008"][["amount","btemp"]].iterrows():
            ax.annotate(row[0], (row[1]["amount"], row[1]["btemp"]), fontsize=12)

        df.loc[list(map(str, years))].plot(kind="scatter", x="amount", y="btemp", marker="o", color="r", 
                                                s=50, ax=ax)
        ax.set_xlabel("Relative river inflow", fontsize=13)
        ax.set_ylabel("Relative forced boundary temperature", fontsize=13)
        ax.set_title("Representation of forcing conditions by year");
        plt.savefig(figname, bbox_inches="tight")


def calc_speed_direction(U, V):
    speed = np.sqrt(U**2 + V**2)
    direction = np.arctan2(V, U)
    direction[direction<0] += 2*np.pi
    return speed, direction
    

def plot(dsc, dsn, figname, source_name):
    
    time = pd.Timestamp(dsc.ocean_time[0].values)
    month = calendar.month_name[time.month][:3]
    year = time.year
    name = f"{month} {year}"
    
    # calculate velocity component differences
    du = dsc["east"] - dsn["u_eastward"]
    dv = dsc["north"] - dsn["v_northward"]

    Us, Vs = [dsc["east"], dsn["u_eastward"], du], [dsc["north"], dsn["v_northward"], dv]
    titles = ["CIOFS", "NWGOA", "CIOFS-NWGOA"]
    vmax = 0
    for U, V in zip(Us, Vs):
        speed, direction = calc_speed_direction(U, V)
        vmax = max(vmax, speed.max())

    # define binning
    rbins = np.linspace(0, vmax, 20)
    abins = np.linspace(0, 2*np.pi, 33)

    hmax = 0
    for U, V in zip(Us, Vs):
        speed, direction = calc_speed_direction(U, V)
        hist, _, _ = np.histogram2d(direction, speed, bins=(abins, rbins))
        hmax = max(hmax, hist.max())
    
    fig = plt.figure(figsize=(16,6), layout="constrained")
    axes = fig.subplots(1, len(Us), subplot_kw=dict(projection="polar"))

    for U, V, ax, title in zip(Us, Vs, axes, titles):
        speed, direction = calc_speed_direction(U, V)
        hist, _, _ = np.histogram2d(direction, speed, bins=(abins, rbins))
        A, R = np.meshgrid(abins, rbins)
        mappable = ax.pcolormesh(A, R, hist.T, vmax=hmax, cmap="cmo.rain")
        ax.tick_params(which="both", labelsize=14)
        # ax.set_rticks([1, 2, 3, 4, 5, 6])
        # have 4 radial ticks
        ax.yaxis.get_major_locator().base.set_params(nbins=6)
        ax.set_xticklabels(["E","","N","","W","","S",""])
        ax.set_title(title, fontsize=18)

    ax_cbar = fig.add_axes([0.25, -0.05, 0.5, 0.05])
    cb = plt.colorbar(mappable, cax=ax_cbar, orientation='horizontal')
    cb.set_label(f"Currents [m/s] at {source_name}; number of occurrences", fontsize=16)
    cb.ax.tick_params(which="both", size=16, labelsize=16)
    fig.suptitle(name, fontsize=20)
    figname.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(figname, bbox_inches="tight")
    # fig.savefig(f"plots/currents_{name}.png", bbox_inches="tight")


def plot_map(cat, source_name, figname):
    maps = [[cat[source_name].metadata["minLongitude"],
                    cat[source_name].metadata["maxLongitude"],
                    cat[source_name].metadata["minLatitude"],
                    cat[source_name].metadata["maxLatitude"],
                    source_name,
                    # source_name.replace("05","YY"),
                    cat[source_name].metadata["maptype"]]]
    two_maps = dict(extent_left=chr.extent_whole, extent_right=[maps[0][0]-0.5, maps[0][0]+0.5, 
                                                                maps[0][2]-0.25, maps[0][2]+0.25],
                width_ratios=[1, 1])
    # two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.6, -151, 58.4, 61],
    #             width_ratios=[1, 1])
    figname.parent.mkdir(parents=True, exist_ok=True)
    omsa.plot.map.plot_map(np.asarray(maps),
                        #    figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=False,
                                  annotate_fontsize=12,
                                  # dd=dds,
                                #   annotate=True,
                                  tight_layout=True,
                                  figname=figname,
                           )

   
def run_through_sources(year, slug):

    base = pathlib.Path(resource_filename('ciofs_hindcast_report', 'report/supporting_files/descriptive_currents'))

    loc = base / f"velocity_ciofs_{year}-01-01_{year+1}-1-1_all_coi_locs.nc"
    dscfull = xr.open_dataset(loc)

    loc = base / f"velocity_nwgoa_{year}-01-01_{year+1}-1-1_all_coi_locs.nc"
    dsnfull = xr.open_dataset(loc)
    
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    # for each location, plot a map and then 4 years of plots
    for source_name in source_names:
        iloc = source_names.index(source_name)
        figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES / "currents" / source_name / f"map.png"
        if not figname.is_file():
            plot_map(cat, source_name, figname)
        dates = pd.date_range(start=f"{year}-1-1", end=f"{year+1}-1-1", freq="1MS")
        time_slices = [slice(dates[i],dates[i+1]) for i, _ in enumerate(dates[:-1])]
        for tslice in time_slices:
            dsc, dsn = dscfull.sel(ocean_time=tslice), dsnfull.sel(ocean_time=tslice)
            month = tslice.start.month
            year = tslice.start.year
            figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES / "currents" / source_name / f"{year}_{str(month).zfill(2)}.png"
            if not figname.is_file():
                plot(dsc.isel(locs=iloc), dsn.isel(locs=iloc), figname, source_name)


# Generate pages
if __name__ == "__main__":
    slugs = ["adcp_moored_noaa_coi_2005", "adcp_moored_noaa_coi_other"]
    years = [1999, 2003, 2005, 2008]

    for year in years:
        for slug in slugs:
            run_through_sources(year, slug)
            # try:
            #     run_through_sources(year, slug)
            # except FileNotFoundError:
            #     continue
    
    plot_conditions_by_year()