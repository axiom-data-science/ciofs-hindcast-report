
import intake
import numpy as np
import ocean_model_skill_assessor as omsa
import ciofs_hindcast_report as chr
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import fsspec
import xarray as xr

def select_colorsdata():
    # make n distinct colors for the points
    n = 20
    colors = plt.cm.tab20c(np.linspace(0,1,n)) # This returns RGBA; convert:
    colors_data = [matplotlib.colors.to_hex(color) for color in colors[:,:3]]
    return colors_data


# Plot discovered data locations
def ctd_transects_gwa(slug):
    # def remove_duplicates(maps):
    #     mapsdf = pd.DataFrame(maps, columns=["minLon","minLat","maxLon","maxLat","name","maptype"])
    #     # overwrite name column to base dropping duplicates (by transect name but without date)
    #     mapsdf["name"] = mapsdf["name"].str.split("-").str.get(0)
    #     mapsdf = mapsdf.drop_duplicates(subset=["name"], keep="first")
    #     maps = mapsdf.to_numpy()
    #     return maps
        
    two_maps = dict(extent_left=[-155.6, -148.2, 56.3, 61.5], extent_right=[-153.3, -150.9, 58.7, 60.2])

    # order of transects is: [3,4,6,7,9,alongbay]
    dds = [[20000,0],[-30000,35000],[-5000,-10000],[-10000,-20000],[-5000,-10000],[-60000,-10000]]
    
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    # df = cat[slug].read()
    source_names_to_plot = []
    for name in cat.metadata["header_names"]:
        # import pdb; pdb.set_trace()
        source_names_to_plot.append([source_name for source_name in source_names if name in source_name][0])
    # source_names_to_plot

    maps = []
    for sn in source_names_to_plot:
        # print(sn)
        df = cat[sn].read()
        # import pdb; pdb.set_trace()
        maps.append((df.cf["longitude"][0], df.cf["longitude"][-1], 
                     df.cf["latitude"][0], df.cf["latitude"][-1],
                     f"Transect {sn.split('-')[0].split('_')[1]}", "line"))
    
    # maps = np.vstack((ds.cf["longitude"].values, ds.cf["longitude"].values, 
    #                   ds.cf["latitude"].values, ds.cf["latitude"].values,
    #                   [""] * len(ds.cf["longitude"]),
    #                   ["point"] * len(ds.cf["longitude"]),
    #                  )).T

    omsa.plot.map.plot_map(np.asarray(maps),
                           figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                #   figsize=chr.figsize, 
                                  dd=dds, 
                                  annotate_fontsize=chr.annotate_fontsize, 
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=False)

    # omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
    #                               project_name="",
    #                               remove_duplicates=remove_duplicates, 
    #                               label_with_station_name=True, 
    #                               two_maps=two_maps,
    #                               dd=dds, 
    #                               annotate_fontsize=chr.annotate_fontsize, 
    #                               figsize=chr.figsize, 
    #                               map_font_size=chr.map_font_size)


def ctd_profiles_2005_noaa(slug, figname=None):

    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=[-155.6, -148.2, 56.3, 61.5], extent_right=[-153.5, -151, 58.7, 60.9])

    # points are in order
    dds = [[-15000, 5000], [0, 10000], [8000, 0], [5000, -6000]]
    dds += [[3000, 3000]]*20

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                dd=dds, 
                                annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,
                                )


def ctd_profiles_usgs_boem(slug):
        
    extent_right_large=[-153.9, -151, 58.7, 60.9]
    two_maps = dict(extent_left=[-155.6, -148.2, 56.3, 61.5], extent_right=extent_right_large,
                width_ratios=[1, 1])

    def remove_duplicates2016(maps):
        """Make a different map per year."""
        mapsdf = pd.DataFrame(maps, columns=["minLon","minLat","maxLon","maxLat","name","maptype"])
        return mapsdf[mapsdf["name"].str.contains("2016")].to_numpy()
    def remove_duplicates2017(maps):
        """Make a different map per year."""
        mapsdf = pd.DataFrame(maps, columns=["minLon","minLat","maxLon","maxLat","name","maptype"])
        return mapsdf[mapsdf["name"].str.contains("2017")].to_numpy()
    def remove_duplicates2018(maps):
        """Make a different map per year."""
        mapsdf = pd.DataFrame(maps, columns=["minLon","minLat","maxLon","maxLat","name","maptype"])
        return mapsdf[mapsdf["name"].str.contains("2018")].to_numpy()
    def remove_duplicates2019(maps):
        """Make a different map per year."""
        mapsdf = pd.DataFrame(maps, columns=["minLon","minLat","maxLon","maxLat","name","maptype"])
        return mapsdf[mapsdf["name"].str.contains("2019")].to_numpy()
    def remove_duplicates2021(maps):
        """Make a different map per year."""
        mapsdf = pd.DataFrame(maps, columns=["minLon","minLat","maxLon","maxLat","name","maptype"])
        return mapsdf[mapsdf["name"].str.contains("2021")].to_numpy()

    
    kwargs = dict(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                annotate=False,
                                # remove_duplicates=remove_duplicates,
                                two_maps=two_maps,
                                annotate_fontsize=9, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                legend=True,
                                markersize=5,
                                markeredgewidth=0.5,
                                colors_data=select_colorsdata(),
                                loc = "lower left")

    omsa.plot.map.plot_cat_on_map(**kwargs, remove_duplicates=remove_duplicates2016, suptitle="2016")
    omsa.plot.map.plot_cat_on_map(**kwargs, remove_duplicates=remove_duplicates2017, suptitle="2017")
    omsa.plot.map.plot_cat_on_map(**kwargs, remove_duplicates=remove_duplicates2018, suptitle="2018")
    omsa.plot.map.plot_cat_on_map(**kwargs, remove_duplicates=remove_duplicates2019, suptitle="2019")
    omsa.plot.map.plot_cat_on_map(**kwargs, remove_duplicates=remove_duplicates2021, suptitle="2021")


def ctd_profiles_piatt_speckman_1999(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    # source_names = chr.src.utils.get_source_names(cat)
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["Station","Lon","Lat","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Lon", y="Lat", c="Station", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=35, hover_cols=["Station","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600) * \
            ddf.hvplot.labels(x="Lon", y="Lat", text="Station", geo=True, text_alpha=0.5,
                        hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_profiles_emap_2002(slug, figname=None):

    figname = figname or f"map_of_{slug}"

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True,
                                extent=chr.extent_whole, 
                                annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,
                                )


def ctd_profiles_emap_2008(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["StationID","Lon","Lat","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Lon", y="Lat", c="StationID", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=5, hover_cols=["StationID","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600, padding=0.2) * \
            ddf.hvplot.labels(x="Lon", y="Lat", text="StationID", geo=True, text_alpha=0.5,
                            hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_profiles_kb_small_mesh_2006(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["Station","Lon","Lat","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Lon", y="Lat", c="Station", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=5, hover_cols=["Station","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600, padding=0.2) * \
        ddf.hvplot.labels(x="Lon", y="Lat", text="Station", geo=True, text_alpha=0.5,
                        hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_profiles_kbay_osu_2007(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["Station","Lon","Lat","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Lon", y="Lat", c="Station", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=5, hover_cols=["Station","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600, padding=0.2) * \
        ddf.hvplot.labels(x="Lon", y="Lat", text="Station", geo=True, text_alpha=0.5,
                        hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_profiles_north_gulf_small_mesh_2005(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["Station","Lon","Lat","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Lon", y="Lat", c="Station", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=5, hover_cols=["Station","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600, padding=0.2) * \
        ddf.hvplot.labels(x="Lon", y="Lat", text="Station", geo=True, text_alpha=0.5,
                        hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_profiles_pogibshi_2002(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["Station","Long (E)","Lat (N)","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Long (E)", y="Lat (N)", c="Station", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=5, hover_cols=["Station","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600, padding=0.2) * \
        ddf.hvplot.labels(x="Long (E)", y="Lat (N)", text="Station", geo=True, text_alpha=0.5,
                        hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_profiles_kachemack_kuletz_2005_2007(slug, figname=None):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    df = cat[f"{slug}_all"].read()
    ddf = df.reset_index()[["Station","Lon","Lat","date_time"]].drop_duplicates()
    plot = ddf.hvplot.points(x="Lon", y="Lat", c="Station", s="date_time", color="k",
                    legend=False, geo=True, tiles=True, size=5, hover_cols=["Station","date_time"],
                    coastline=False, xlabel="Longitude", ylabel="Latitude", title=slug,
                    width=600, height=600, padding=0.2) * \
        ddf.hvplot.labels(x="Lon", y="Lat", text="Station", geo=True, text_alpha=0.5,
                        hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='9pt')
    return plot


def ctd_towed_otf_kbnerr(slug):

    two_maps = dict(extent_left=[-155.6, -148.2, 56.3, 61.5], extent_right=[-152.5, -152.1, 59.76, 59.93],
                    width_ratios=[0.8, 1.2])

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    dfs = []
    for source_name in source_names:
        dfs.append(cat[source_name].read())
    df = pd.concat(dfs)

    maps = np.vstack((df.cf["longitude"].values, df.cf["longitude"].values, 
                    df.cf["latitude"].values, df.cf["latitude"].values,
                    [""] * len(df.cf["longitude"]),
                    ["point"] * len(df.cf["longitude"]),
                    )).T

    omsa.plot.map.plot_map(maps,
                        figname=f"Map of {slug}",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                legend=False,
                                annotate=False,
                        )


def ctd_towed_ferry_noaa_pmel(slug):

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-156, -150.5, 57, 59.75],
                    width_ratios=[0.4, 1.6])

    url = "https://researchworkspace.com/files/42203278/Tustumena_t_s_chl_cdom_tr_final_data_subsetted.nc"
    with fsspec.open(url) as f:
        ds = xr.open_dataset(f).cf.sel(T=slice(None,None, 100))
    
        maps = np.vstack((ds.cf["longitude"].values, ds.cf["longitude"].values, 
                        ds.cf["latitude"].values, ds.cf["latitude"].values,
                        [""] * len(ds.cf["longitude"]),
                        ["point"] * len(ds.cf["longitude"]),
                        )).T

        omsa.plot.map.plot_map(maps,
                            figname=f"Map of {slug}",
                                    label_with_station_name=True, 
                                    two_maps=two_maps,
                                    figsize=chr.figsize, 
                                    map_font_size=chr.map_font_size,
                                    legend=False,
                                    annotate=False,
                            )


def ctd_transects_otf_kbnerr(slug):
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.0, -151.5, 59.5, 60.2],
                    width_ratios=[.85,1.15])

    df = cat[source_names[0]].read()
    ddf = df.drop_duplicates(subset=["Lon (oE)", "Lat (oN)", "Station"])
    maps = np.vstack((ddf.cf["longitude"].values, ddf.cf["longitude"].values, 
                    ddf.cf["latitude"].values, ddf.cf["latitude"].values,
                    ddf.cf["station"].values,
                    ["point"] * len(ddf.cf["longitude"]),
                    )).T

    omsa.plot.map.plot_map(maps,
                           figname=f"Map of {slug}",
                           label_with_station_name=True, 
                           two_maps=two_maps,
                           figsize=chr.figsize, 
                           map_font_size=chr.map_font_size,
                           markersize=6,
                           legend=True,
                           annotate=False,
                           colors_data=select_colorsdata()
                        )


def ctd_transects_cmi_uaf(slug):
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.3, -151.0, 60.4, 61.0],
                    width_ratios=[.85,1.15])

    df = cat[source_names[0]].read()
    ddf = df.reset_index(drop=True).drop_duplicates(subset=["Longitude", "Latitude", "Station"])

    maps = np.vstack((ddf.cf["longitude"].values, ddf.cf["longitude"].values, 
                    ddf.cf["latitude"].values, ddf.cf["latitude"].values,
                    ddf.cf["station"].values,
                    ["point"] * len(ddf.cf["longitude"]),
                    )).T

    omsa.plot.map.plot_map(maps,
                            figname=f"Map of {slug}",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                        markersize=6,
                                legend=True,
                                annotate=False,
                        colors_data=select_colorsdata()
                        )


def ctd_transects_cmi_kbnerr(slug):
    cat = intake.open_catalog(chr.CAT_NAME(slug))

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.5, -151.0, 58.3, 60.1],
                    width_ratios=[.85,1.15])
    
    source_names = [
        # 'Kbay_timeseries',
                    'Cruise_16-Line_1',
                    'Cruise_16-Line_2',
                    'Cruise_16-Line_3',
                    'Cruise_16-Line_4',
                    'Cruise_16-Line_6',
                    'Cruise_16-Line_7',
                    # 'sue_shelikof',
    ]

    maps = []
    for source_name in source_names:
        df = cat[source_name].read()
        maps.append( (df.cf["longitude"][0], df.cf["longitude"][-1], 
                    df.cf["latitude"][0], df.cf["latitude"][-1],
                    f"Transect {df.cf['line'].iloc[0]}",
                    "line",) )

    source_name = 'sue_shelikof'
    df = cat[source_name].read()
    maps.append( (df.cf["longitude"].iloc[0], df.cf["longitude"].iloc[-1], 
                df.cf["latitude"].iloc[0], df.cf["latitude"].iloc[-1],
                "Transect\nSue Shelikof",
                "line",) )

    source_name = 'Kbay_timeseries'
    df = cat[source_name].read()
    maps.append( 
           (df.cf["longitude"].iloc[0], df.cf["longitude"].iloc[0], 
                    df.cf["latitude"].iloc[0], df.cf["latitude"].iloc[0],
                    f"Kachemak Bay\nStation {df.cf['station'][0]}",
                    "point",
                    )
          )

    dds = [(-10000,-40000), (-40000, 30000), (-20000, 20000), (5000,10000), (0, 35000), (25000, 5000), (-92500, -30000), (-80000,-5000)]

    omsa.plot.map.plot_map(np.asarray(maps),
                            figname=f"Map of {slug}",
                            label_with_station_name=True, 
                            two_maps=two_maps,
                           dd=dds,
                            figsize=chr.figsize, 
                            map_font_size=chr.map_font_size,
                            markersize=6,
                            legend=False,
                            annotate=True,
                            # colors_data=select_colorsdata()
                        )


def ctd_moored_circac(slug):
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    source_name = source_names[0]

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152, -151.1, 60.5, 61],
                    width_ratios=[1,1])

    ddf = cat[source_name].read()
    maps = (ddf.cf["longitude"].min(), ddf.cf["longitude"].min(), 
                    ddf.cf["latitude"].min(), ddf.cf["latitude"].min(),
                    source_name,
                    "point",
                    )

    omsa.plot.map.plot_map(np.asarray([maps]),
                            figname=f"Map of {slug}",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                figsize=chr.figsize, 
                           dd = [(0,5000)],
                                map_font_size=chr.map_font_size,
                        markersize=6,
                                legend=False,
                                annotate=True,
                        )


def ctd_moored_kbnerr(slug):
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    source_name = source_names[0]

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.2, -151.5, 59.0, 59.4],
                    width_ratios=[1,1])

    ddf = cat[source_name].read()
    maps = (ddf.cf["longitude"].min(), ddf.cf["longitude"].min(), 
                    ddf.cf["latitude"].min(), ddf.cf["latitude"].min(),
                    slug,
                    "point",
                    )

    omsa.plot.map.plot_map(np.asarray([maps]),
                            figname=f"Map of {slug}",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                figsize=chr.figsize, 
                        #    dd = [(0,5000)],
                                map_font_size=chr.map_font_size,
                        markersize=6,
                                legend=False,
                                annotate=True,
                        )


def ctd_transects_uaf(slug):
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    source_name = source_names[0]

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.4, -151.15, 60.2, 60.8],
                    width_ratios=[.85,1.15])

    df = cat[source_name].read()
    maps = (df.cf["longitude"][0], df.cf["longitude"][-1], 
                df.cf["latitude"][0], df.cf["latitude"][-1],
                slug,
                "line",) 

    omsa.plot.map.plot_map(np.asarray([maps]),
                            figname=f"Map of {slug}",
                            label_with_station_name=True, 
                            two_maps=two_maps,
                           dd=[(-50000,5000)],
                            figsize=chr.figsize, 
                            map_font_size=chr.map_font_size,
                            markersize=6,
                            legend=False,
                            annotate=True,
                        )


def ctd_transects_misc_2002(slug):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.3, -150.9, 59.15, 59.85],
                    width_ratios=[.85,1.15])

    maps = []
    for source_name in source_names:
        df = cat[source_name].read()
        maps.append( (df.cf["longitude"][0], df.cf["longitude"][-1], 
                    df.cf["latitude"][0], df.cf["latitude"][-1],
                    source_name,
                    "line",) )

    # dds = [(-10000,40000), (-40000, -30000), (0,0), (-5000,10000), (0, 35000)]

    omsa.plot.map.plot_map(np.asarray(maps),
                            figname=f"Map of {slug}",
                            label_with_station_name=True, 
                            two_maps=two_maps,
                           # dd=dds,
                            figsize=chr.figsize, 
                            map_font_size=chr.map_font_size,
                            markersize=6,
                            legend=True,
                            annotate=False,
                            colors_data=select_colorsdata()
                        )


def ctd_transects_barabara_to_bluff_2002_2003(slug):

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.0, -151.3, 59.4, 59.7],
                    width_ratios=[.85,1.15])

    df = cat[source_names[0]].read()
    station, lat, lon = list(zip(*df.reset_index(drop=True).set_index(["Station","Lat (N)", "Long (E)"]).index.unique().values))
    maps = np.vstack((lon, lon, 
                lat, lat,
                [station] * len(lon),
                ["point"] * len(lon),
                )).T.tolist()

    omsa.plot.map.plot_map(np.asarray(maps),
                            figname=f"Map of {slug}",
                            label_with_station_name=True, 
                            two_maps=two_maps,
                           # dd=dds,
                            figsize=chr.figsize, 
                            map_font_size=chr.map_font_size,
                            markersize=6,
                            legend=True,
                            annotate=False,
                            colors_data=chr.src.plot_dataset_on_map.select_colorsdata()
                        )


def ctd_towed_gwa(slug):

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.7, -150.0, 58.5, 61],
                    width_ratios=[1, 1])

    # want to show all the data so just read it in
    urls = ["https://researchworkspace.com/files/42202335/CPR_physical_data_2017_subsetted.csv",
            "https://researchworkspace.com/files/42202337/CPR_physical_data_2018_subsetted.csv",
            "https://researchworkspace.com/files/42202339/CPR_physical_data_2019_subsetted.csv",
            "https://researchworkspace.com/files/42202341/CPR_physical_data_2020_subsetted.csv",
            ]
    maps = []
    for url in urls:
        df = pd.read_csv(url)
        maps.extend(np.vstack((df.cf["longitude"].values, df.cf["longitude"].values, 
                    df.cf["latitude"].values, df.cf["latitude"].values,
                    [""] * len(df.cf["longitude"]),
                    ["point"] * len(df.cf["longitude"]),
                    )).T.tolist())

    omsa.plot.map.plot_map(np.asarray(maps),
                           figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=False,
                                  annotate=False,
                           )


def ctd_towed_gwa_temp(slug):

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.5, -150.0, 58.5, 61],
                    width_ratios=[1, 1])

    urls = ["https://researchworkspace.com/files/42202616/CPR_TemperatureData_2011_subsetted.csv",
            "https://researchworkspace.com/files/42202618/CPR_TemperatureData_2012_subsetted.csv",
            "https://researchworkspace.com/files/42202620/CPR_TemperatureData_2013_subsetted.csv",
            "https://researchworkspace.com/files/42202622/CPR_TemperatureData_2014_subsetted.csv",
            "https://researchworkspace.com/files/42202624/CPR_TemperatureData_2015_subsetted.csv",
            "https://researchworkspace.com/files/42202626/CPR_TemperatureData_2016_subsetted.csv",]
    maps = []
    for url in urls:
        df = pd.read_csv(url)
        maps.extend(np.vstack((df.cf["longitude"].values, df.cf["longitude"].values, 
                    df.cf["latitude"].values, df.cf["latitude"].values,
                    [""] * len(df.cf["longitude"]),
                    ["point"] * len(df.cf["longitude"]),
                    )).T.tolist())
    # cat = intake.open_catalog(chr.CAT_NAME(slug))
    # source_name = chr.src.utils.get_source_names(cat)[0]
    # df = cat[source_name].read()

    # maps = np.vstack((df.cf["longitude"].values, df.cf["longitude"].values, 
    #                   df.cf["latitude"].values, df.cf["latitude"].values,
    #                   [""] * len(df.cf["longitude"]),
    #                   ["point"] * len(df.cf["longitude"]),
    #                  )).T

    omsa.plot.map.plot_map(np.asarray(maps),
                           figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=False,
                                  annotate=False,
                           )


def surface_otf_adfg(slug):

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153, -151.6, 59.5, 60.2],
                    width_ratios=[0.8, 1.2])
    station_names = [4,5,6,6.5,7,8]
    lons = [-(152+9.1/60),-(152+13.5/60),-(152+17.6/60),
                    -(152+19.8/60),
                    -(152+22/60),-(152+26.3/60)]
    lats = [59+49.5/60, 59+50.2/60, 59+51/60, 59+51.4/60, 59+51.7/60, 59+52.4/60]

    maps = np.vstack((lons, lons, lats, lats, station_names, ["point"] * len(lons),)).T

    omsa.plot.map.plot_map(maps,
                           figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=True,
                                  colors_data=select_colorsdata(),
                                  annotate=False,
                           )


def moorings_uaf(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.6, -149.3, 57.5, 59.8],
                    width_ratios=[0.9, 1.1])
    
    dds = [(-50000, -10000), (-50000, 20000), (-50000, -20000), ]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                # dd=dds, 
                                # annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def moorings_nps(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-155, -152, 58, 60],
                    width_ratios=[0.9, 1.1])
    
    dds = [(-50000, 10000), (-120000, 10000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                dd=dds, 
                                # annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def moorings_noaa(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-155, -152, 57, 60],
                    width_ratios=[0.9, 1.1])
    
    dds = [(-50000, 10000), (-120000, 10000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                extent=chr.extent_whole,
                                legend=True,
                                colors_data=select_colorsdata(),
                                annotate=False,
                                markersize=7,
                                # two_maps=two_maps,
                                # dd=dds, 
                                annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def moorings_aoos_cdip(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.5, -149.5, 57, 60],
                    width_ratios=[0.9, 1.1])
    
    dds = [(-50000, 10000), (-120000, 10000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                # dd=dds, 
                                # annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def moorings_kbnerr_bear_cove_seldovia(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152, -150.5, 59, 60],
                    width_ratios=[0.9, 1.1])
    
    dds = [(-20000, 5000), (0, -6000), (0, 4000)]
    # dds = [(-20000, 5000), (-10000, 11000), (0, -6000), (0, 4000), (0, -6000), (0, 4000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                dd=dds, 
                                # annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def moorings_kbnerr_homer(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152, -150.5, 59, 60],
                    width_ratios=[0.9, 1.1])
    
    dds = [(-10000, 11000), (0, -6000), (0, 4000), ]
    # dds = [(-20000, 5000), (-10000, 11000), (0, -6000), (0, 4000), (0, -6000), (0, 4000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                dd=dds, 
                                # annotate_fontsize=10, 
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def moorings_kbnerr_historical(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.3, -150.8, 59, 60],
                    width_ratios=[0.9, 1.1])
    # kacbcwq, kacdlwq -- same as kachowq, kacpgwq, kacsewq
    dds = [(1000, 1000), (1000, 2000), (1000, -5000), (1000, 1000), (1000, 1000), (1000, 1000)]

    loc = "https://researchworkspace.com/files/40335130/sampling_stations.csv"
    sites = pd.read_csv(loc, encoding = "ISO-8859-1")
    # strip white space
    sites["Station Code"] = sites["Station Code"].str.strip()
    station_names = ["kacbcwq", "kacdlwq", "kachowq", "kacpgwq", "kacsewq"]
    sites[" Longitude"] *= -1
    ll = sites[sites["Station Code"].isin(station_names)][["Latitude "," Longitude"]].values.tolist()
    lat, lon = zip(*ll)
    
    maps = np.vstack((lon, lon, lat, lat, station_names, ["point"] * len(lon),)).T

    omsa.plot.map.plot_map(maps,
                        #    figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=False,
                                  dd=dds,
                                #   colors_data=select_colorsdata(),
                                  annotate=True,
                                  figname=figname,
                           )


def adcp_moored_noaa_coi_2005(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    maps = []
    for source_name in source_names:
        maps.append([cat[source_name].metadata["minLongitude"],
                            cat[source_name].metadata["maxLongitude"],
                            cat[source_name].metadata["minLatitude"],
                            cat[source_name].metadata["maxLatitude"],
                            source_name[5:],
                            # source_name.replace("05","YY"),
                            cat[source_name].metadata["maptype"]])
    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.6, -151, 58.4, 61],
                    width_ratios=[1, 1])
    dds = [(-10000,10000), (0,10000), (5000, 10000), (0,0),(0,0),(0,0),(0,0),(0,0), 
           (0,0),(0,0),(0,0),(0,0),(0,0), (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
           (0,-10000), (0,10000), (5000,5000), (10000,0)]
    omsa.plot.map.plot_map(np.asarray(maps),
                        #    figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=False,
                                  annotate_fontsize=10,
                                  dd=dds,
                                  annotate=True,
                                  tight_layout=True,
                                  figname=figname,
                           )


def adcp_moored_noaa_coi_other(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    maps = []
    for source_name in source_names:
        maps.append([cat[source_name].metadata["minLongitude"],
                            cat[source_name].metadata["maxLongitude"],
                            cat[source_name].metadata["minLatitude"],
                            cat[source_name].metadata["maxLatitude"],
                            source_name,
                            # source_name.replace("05","YY"),
                            cat[source_name].metadata["maptype"]])
    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-152.5, -149.5, 58.83, 61.33],
                    width_ratios=[1, 1])
    # dds = [(-10000,10000), (0,10000), (5000, 10000), (0,0),(0,0),(0,0),(0,0),(0,0), 
    #        (0,0),(0,0),(0,0),(0,0),(0,0), (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
    #        (0,-10000), (0,10000), (5000,5000), (10000,0)]
    omsa.plot.map.plot_map(np.asarray(maps),
                        #    figname=f"Map of {slug}",
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size,
                                  legend=True,
                                  annotate_fontsize=9,
                                #   dd=dds,
                                  annotate=False,
                                  tight_layout=True,
                           colors_data=select_colorsdata(),
                           loc = "lower right",
                           markersize=8,
                           figname=figname,
                           )


def adcp_moored_noaa_kod_1(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-155.75, -152, 56.6, 57.9],
                    width_ratios=[0.4, 1.6])
    
    # dds = [(-10000, 11000), (0, -6000), (0, 4000), ]
    # dds = [(-20000, 5000), (-10000, 11000), (0, -6000), (0, 4000), (0, -6000), (0, 4000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                # dd=dds, 
                                # annotate_fontsize=10, 
                                legend=True,
                                annotate=False,
                                loc="upper left",
                                colors_data=select_colorsdata(),
                                markersize=8,
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def adcp_moored_noaa_kod_2(slug, figname=None):
    figname = figname or f"map_of_{slug}"
    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-154.0, -151.75, 57.8, 58.75],
                    width_ratios=[0.4, 1.6])
    
    dds = [(-10000, 11000), (0, -6000), (0, 4000), ]
    # dds = [(-20000, 5000), (-10000, 11000), (0, -6000), (0, 4000), (0, -6000), (0, 4000)]

    omsa.plot.map.plot_cat_on_map(catalog=intake.open_catalog(chr.CAT_NAME(slug)), 
                                project_name="",
                                label_with_station_name=True, 
                                two_maps=two_maps,
                                # dd=dds, 
                                # annotate_fontsize=10, 
                                legend=True,
                                annotate=False,
                                loc="upper left",
                                colors_data=select_colorsdata(),
                                markersize=8,
                                figsize=chr.figsize, 
                                map_font_size=chr.map_font_size,
                                figname=figname,)


def hfradar(slug, figname=None):
    figname = figname or f"map_of_{slug}"

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    # just use 2 of 3 since one is a repeat
    source_names = ['lower-ci_system-B_2006-2007', 'upper-ci_system-A_2009']
    names_to_use = ["Lower CI/System B", "Upper CI/System A"]
    maps = []
    for source_name, name_to_use in zip(source_names, names_to_use):
        maps.append([cat[source_name].metadata["minLongitude"],
                            cat[source_name].metadata["maxLongitude"],
                            cat[source_name].metadata["minLatitude"],
                            cat[source_name].metadata["maxLatitude"],
                            name_to_use,
                            cat[source_name].metadata["maptype"]])
    two_maps = dict(extent_left=chr.extent_whole, extent_right=[-153.5, -151.0, 59, 61],
                    width_ratios=[1, 1])
    omsa.plot.map.plot_map(np.asarray(maps),
                                  label_with_station_name=True, 
                                  two_maps=two_maps,
                                  figsize=chr.figsize, 
                                  map_font_size=chr.map_font_size+2,
                                  legend=True,
                                  annotate_fontsize=9,
                                  annotate=False,
                                  tight_layout=True,
                           colors_data=select_colorsdata(),
                           loc = "upper left",
                           markersize=8,
                           figname=figname,
                           )
