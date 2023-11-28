"""Generate the model-data comparison notebooks to be turned into pages."""

import calendar
import intake
import nbformat as nbf
import ciofs_hindcast_report as chr
import pandas as pd
import ocean_model_skill_assessor as omsa
import matplotlib.pyplot as plt
from datetimerange import DateTimeRange
import yaml
import seaborn as sns
import numpy as np
import pathlib
import xarray as xr
import cf_pandas as cfp
import ciofs_hindcast_report.src.page_utils as pu


models = ["ciofs", "nwgoa"]
key_variables = ["ssh", "temp", "salt", "along", "across", "speed"]
# dsm = xr.open_zarr("http://xpublish-ciofs.srv.axds.co/datasets/ciofs_hindcast/zarr/")
# time_range = dict(nwgoa=[pd.Timestamp("1999-01-01"), pd.Timestamp("2009-01-01")],
#                   ciofs=[pd.Timestamp("1999-01-01"), pd.Timestamp(dsm.ocean_time[-1].values)])
time_range = dict(nwgoa=[pd.Timestamp("1999-01-01"), pd.Timestamp("2009-01-01")],
                ciofs=[pd.Timestamp("1999-01-01"), pd.Timestamp("2022-12-31")])

def isin_time_range(data_min_time, data_max_time, model):
    # import pdb; pdb.set_trace()
    data_min_time, data_max_time = pd.Timestamp(data_min_time.replace("Z","")), pd.Timestamp(data_max_time.replace("Z",""))
    data_min_time_str, data_max_time_str = str(data_min_time.date()), str(data_max_time.date())
    msg = f"""
{model.upper()}: Data time range is {data_min_time_str} to {data_max_time_str} but model ends {time_range[model][1].date()}.

"""
    if time_range[model][1] < data_min_time:
        return False, msg
    else:
        return True, ""
    
def project_name(slug, model):
    return f"{slug}_{model}"
def outdir(slug, model):
    return chr.COMP_PAGE_DIR(slug) / project_name(slug, model)
def translate(ts_mods):
    words = ""
    # import pdb; pdb.set_trace()
    if isinstance(ts_mods, str):
    # if ts_mods is not None and not np.isnan(ts_mods):
        ts_mods = ts_mods.split("_")
        for ts_mod in ts_mods:
            if len(words) > 0:
                words += ", then "
            if ts_mod == "subtidal":
                words += "tidally-filtered"
            elif ts_mod == "subtract-monthly-mean":
                words += "monthly mean from data subtracted"
            elif ts_mod == "subtract-mean":
                words += "mean subtracted"
    return words
def translate_var(key_variable):
    if key_variable == "ssh":
        return "Sea surface height"
    if key_variable == "temp":
        return "Sea water temperature"
    if key_variable == "salt":
        return "Sea water salinity"
    if key_variable == "across":
        return "Across-channel velocity"
    if key_variable == "along":
        return "Along-channel velocity"
    if key_variable == "speed":
        return "Horizontal speed"


def aggregate_overall_stats(slug, source_names=None):

    dfmodels = []
    for model in models:
        statspaths = sorted(list(outdir(slug, model).glob(f"*.yaml")))
        # import pdb; pdb.set_trace()
        all_desc = chr.src.utils.group_decoded_paths(statspaths)
        all_desc = all_desc.set_index(['slug', 'source_name', 'key_variable', 'ts_mods']).sort_index()
        
        # loop over sets of indices defining different groupings of filenames
        dfsources = []
        for ind in all_desc.index.unique():
            paths = cfp.astype(all_desc.loc[ind, "path"], list)
            val = 0
            for path in paths:
                with open(path, "r") as stream:
                    stats = yaml.safe_load(stream)                    
                val += stats["ss"]["value"]
            val /= len(paths)  # change to mean
            dfsources.append(pd.DataFrame(index=[ind], data=val, columns=[model]))
        if len(dfsources)>0:
            dfmodels.append(pd.concat(dfsources, axis=0))
    if len(dfmodels)>0:
        dfstats = pd.concat(dfmodels, axis=1)
        if not isinstance(dfstats.index, pd.MultiIndex):
            dfstats.index = pd.MultiIndex.from_tuples(dfstats.index)
        dfstats.index.names = all_desc.index.names
    return dfstats.sort_index()


def plot_overall_stats(df, figname):
    figsize = (6,len(df)*.5)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    cbar_ax = fig.add_axes([0.95, 0.11, 0.02, 0.77])
    sns.heatmap(df, annot=True, linewidths=.5, vmin=0, vmax=1, cmap="cmo.matter_r", fmt='.2f', 
                cbar_ax=cbar_ax, ax=ax)#, cbar_kws=dict(pad=0.001))
    ax.tick_params(axis='both', which='major', labelsize=14, labelbottom = False, bottom=False, top = False, labeltop=True)
    ax.tick_params(axis='y', rotation=0)
    ax.set_ylabel("")
    fig.savefig(figname, dpi=100, bbox_inches="tight")
    plt.close(fig)


def plot_mean(df, varname, figname):
    monthly_mean = df[varname].groupby(df.cf["T"].dt.month).mean()
    # monthly_mean = df[varname].groupby(df.cf["T"].dt.month).mean()
    # unclear why I have to shift this
    monthly_mean_shifted = monthly_mean.copy()
    monthly_mean_shifted.index = monthly_mean_shifted.index - 1

    df = df.set_index(df.cf["T"].dt.month)
    # df = df.set_index(df.cf["T"].dt.month)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    sns.violinplot(data=df, x=df.index, y=varname, inner="quartile", color="orange")
    monthly_mean_shifted.plot(ax=ax, marker="o", color="k", figsize=(10,5))
    xticks = ax.get_xticklabels()
    ax.set_xticks(ax.get_xticks(), labels=[calendar.month_abbr[int(i.get_text())] for i in xticks])
    ax.set_xlabel("")
    ax.set_title("Monthly means and statistical variation over time")
    fig.savefig(figname, dpi=100, bbox_inches="tight")
    plt.close(fig)


def aggregate_stats(slug):

    dfmodels = []
    for model in models:
        statspaths = sorted(list(outdir(slug, model).glob(f"*.yaml")))
        all_desc = chr.src.utils.group_decoded_paths(statspaths)        
        all_desc = all_desc.set_index(["source_name","key_variable","ts_mods","start_time"]).sort_index()
        
        # loop over each source and subsource to save mean skill score
        for ind in all_desc.index:
            path = all_desc.loc[ind, "path"]
            with open(path, "r") as stream:
                stats = yaml.safe_load(stream)
            all_desc.loc[ind,model] = stats["ss"]["value"]
        dfmodels.append(all_desc)
    if len(dfmodels)>0:
        dfstats = dfmodels[0]
        full_index = dfmodels[0].index.union(dfmodels[1].index)
        dfstats = dfstats.reindex(full_index)
        dfstats.rename(columns={"path": f"path_{models[0]}"}, inplace=True)
        dfstats[f"path_{models[1]}"] = dfmodels[1]["path"]
        # import pdb; pdb.set_trace()
        if not dfmodels[1].empty:
            dfstats["nwgoa"] = dfmodels[1]["nwgoa"]
    return dfstats.sort_index()


def plot_source_stats(df, source_name, figname):
    figsize = (6,len(df)*.5)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    cbar_ax = fig.add_axes([0.95, 0.11, 0.02, 0.77])
    sns.heatmap(df, annot=True, linewidths=.5, vmin=0, vmax=1, cmap="cmo.matter_r", fmt='.2f', 
                cbar_ax=cbar_ax, ax=ax)#, cbar_kws=dict(pad=0.001))
    ax.tick_params(axis='both', which='major', labelsize=14, labelbottom = False, bottom=False, top = False, labeltop=True)
    ax.tick_params(axis='y', rotation=0)
    ax.set_ylabel("")
    fig.suptitle(source_name, y=1.1)
    # plt.tight_layout()
    # import pdb; pdb.set_trace()
    fig.savefig(figname, dpi=100, bbox_inches="tight")
    plt.close(fig)


# def moorings_noaa():
#     text = f"""
# Overall, the CIOFS model something something, as shown in {{numref}}`Figure {{number}}<fig-overall-moorings_noaa-ssh-subtract-mean>`.

# """
#     return text

# def moorings_kbnerr_bear_cove_seldovia():
#     text = f"""
# Overall, the salinity from the CIOFS model demonstrates much less high frequency variability than the NWGOA model as shown in (update reference) {{numref}}`Figure {{number}}<fig-overall-moorings_noaa-ssh-subtract-mean>`.

# """
#     return text






def generate_page(slug):   
    # dsm = xr.open_zarr("http://xpublish-ciofs.srv.axds.co/datasets/ciofs_hindcast/zarr/")
    

     
# def moorings_noaa(slug):    
    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in models:
        paths = omsa.paths.Paths(project_name(slug, model))
        here = outdir(slug,model)
        # import pdb; pdb.set_trace()
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
            # here.symlink_to(omsa.paths.OUT_DIR(project_name(slug, model)))
    
    # also symbolically link in DATA PAGE HERE
# def project_name(slug, model):
#     return f"{slug}_{model}"
# def outdir(slug, model):
#     return 
    # import pdb; pdb.set_trace()
    # here = chr.COMP_PAGE_DIR(slug) / f"{slug}_dataset.md"
    # if not here.is_dir():
    #     here.symlink_to(chr.DATA_PAGE_PATH(slug))
    
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    
    nb = nbf.v4.new_notebook()

    ## INITIAL STUFF

    text = f"""\
# {cat.description}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`
"""

    # Add these cells to the notebook
    nb['cells'] = [pu.imports_cell(),
                   nbf.v4.new_markdown_cell(text),
                #    nbf.v4.new_code_cell(code),
                   ]

#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`
    # Add map markdown cell
    nb['cells'].extend([pu.map_cell(slug, cat.metadata["map_description"], label="", caption=""),])
    
    ## Overall summary of statistics
    dfstats = aggregate_overall_stats(slug)
    # import pdb; pdb.set_trace()
    cols_to_use = ["source_name","ciofs"]
    if "nwgoa" in dfstats.columns:
        cols_to_use.append("nwgoa")
    dfstats_by_heading = dfstats.reset_index().set_index(["key_variable","ts_mods"]).sort_index()[cols_to_use]
    
#     text = f"""\
# ## Performance Summary
# """
#     if hasattr(chr.src.generate_comparison_pages, slug):
#         text += f"""

# {getattr(chr.src.generate_comparison_pages, slug)()}
# """
#     nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
    
    for ind in dfstats_by_heading.index.unique():
        key_variable, ts_mods = ind[0], ind[1]
        # slug, key_variable(0), ts_mods (1)
        figname = chr.COMP_PAGE_DIR(slug) / f"{slug}_{key_variable}_{ts_mods}.png"
        # import pdb; pdb.set_trace()
        df_to_plot = dfstats_by_heading.loc[ind]
        if isinstance(df_to_plot, pd.Series):
            df_to_plot = df_to_plot.to_frame().transpose().reset_index(drop=True).set_index("source_name")
        else:
            df_to_plot = df_to_plot.reset_index(drop=True).set_index("source_name")
        
        # KMT: Try without this
#         # if figname.name == "moorings_kbnerr_bear_cove_seldovia_salt_subtidal.png":
#         #     import pdb; pdb.set_trace()
#         # print(figname.name)
#         plot_overall_stats(df_to_plot, figname=figname)
        
#         label = f"fig-overall-{slug}-{key_variable}-{ts_mods}"
#         caption = f"Skill score for {translate_var(key_variable).lower()}, {translate(ts_mods)}"

#         # key_variable (0), ts_mods (1)
#         text = f"""\
# ### {translate_var(key_variable)}: {translate(ts_mods)}

# {chr.src.utils.mk_fig_wide(figname.name, label, caption)}

# """
#         nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
    
    df = aggregate_stats(slug)
    # drop slug as an index
    df = df.reset_index().set_index(["source_name","key_variable","ts_mods"])

    ## Loop over source names
    for source_name in source_names:
        
        source_md_0 = f"""\
## {source_name}

"""

        for model in models:
            data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
            # import pdb; pdb.set_trace()
            data_min_time, data_max_time = pd.Timestamp(data_min_time.replace("Z","")), pd.Timestamp(data_max_time.replace("Z",""))
            data_min_time_str, data_max_time_str = str(data_min_time.date()), str(data_max_time.date())
            if time_range[model][1] < data_min_time:
                skip_nwgoa = True
                source_md_0 += f"""
{model.upper()}: Data time range is {data_min_time_str} to {data_max_time_str} but model ends {time_range[model][1].date()}.

"""
            else:
                skip_nwgoa = False
                

        nb['cells'].extend([nbf.v4.new_markdown_cell(source_md_0),])
        
        if source_name not in df.index:
            continue
        
        # find all unique combinations of 'source_name', 'key_variable', 'ts_mods'
        for ind in df.loc[source_name].index.unique():
            key_variable, ts_mods = ind[0], ind[1]
            
            # subset of df, 1 set of source_name, key_variable, and ts_mods
            dfs = df.loc[source_name].loc[ind]

            if dfs.ndim > 1:
                dfs["start_time"] = pd.to_datetime(dfs["start_time"])
                dfs["start_time"] = dfs["start_time"].dt.year
            
            # key_variable (0), ts_mods (1)
            text = f"""\
### {translate_var(key_variable)}: {translate(ts_mods)}
"""
            nb['cells'].extend([nbf.v4.new_markdown_cell(text),])

            if dfs.ndim > 1:
                # add heatmap for all years
                # slug, key_variable(0), ts_mods (1)
                figname = chr.COMP_PAGE_DIR(slug) / f"{slug}_{source_name}_{key_variable}_{ts_mods}.png"
                # import pdb; pdb.set_trace()
                # print(figname.name, len(dfs))
                
                
                # # KMT try without this
                # plot_source_stats(dfs.reset_index().set_index("start_time")[models], source_name, figname)
                # label = f"fig-{source_name}-{key_variable}-{ts_mods}"
                # caption = f"Skill score by year for {translate_var(key_variable).lower()}, {translate(ts_mods)}"
                # text = chr.src.utils.mk_fig_wide(figname.name, label, caption)
                # nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
                
                # if this is an anomaly calculation, show mean
                if "subtract-monthly-mean" in ts_mods:
                    dfd = cat[source_name].read()
                    figname = chr.COMP_PAGE_DIR(slug) / f"{slug}_{source_name}_{key_variable}_mean.png"
                    # import pdb; pdb.set_trace()
                    plot_mean(dfd, dfd.cf[key_variable].name, figname)      
                    label = ""#f"fig-{source_name}-{key_variable}"
                    caption = ""#f"{translate_var(key_variable)} averaged monthly across data range with variation across years included."
                    text = chr.src.utils.mk_fig_wide(figname.name, label, caption)
                    nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
                
            for model in models:
                
                if skip_nwgoa and model == "nwgoa":
                    continue

                header = f"""\
#### {model.upper()}

"""
                
                # loop over 1 row or multiple years of figures for 
                # source_name, key_Variable, ts_mods combination
                if isinstance(dfs, pd.Series):
                    dfs = dfs.to_frame().T

                if len(dfs) > 1:
                    header += """

``````{div} full-width 
`````{dropdown} Comparison plots by year

"""
                    
                for row in dfs.iterrows():
                    row = row[1]
                    
                    # row might be mostly nan's if it is present for one model but not the other
                    # in which case, skip
                    if model in row.index and pd.isnull(row[model]):
                        continue
                    
                    if len(dfs) > 1:
                        header += f"""\
##### {row["start_time"]}

"""

                    if isinstance(row[f'path_{model}'], pathlib.Path):
                        path = row[f'path_{model}'].with_suffix('.png').relative_to(chr.COMP_PAGE_DIR(slug))
                    elif np.isnan(row[f'path_{model}']):
                        continue
                    label = ""#f"fig-{model}-{source_name}-{key_variable}-{ts_mods}"
                    caption = ""#f"Model-data comparison for {source_name} of {translate_var(key_variable).lower()}"
                    # if len(dfs) > 1:
                    #     label += f"-{row['start_time']}"
                    #     caption += f" for {row ['start_time']}"
                    header += chr.src.utils.mk_fig_wide(path, label, caption)

                if len(dfs) > 1:
                    header += """

`````
``````
"""


                nb['cells'].extend([nbf.v4.new_markdown_cell(header),])

    nbf.write(nb, f'{chr.COMP_PAGE_DIR(slug) / slug}.ipynb')
    
    
def overview_hfradar():
    
    slug = "hfradar"
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    #symlink in map from data comp dir
    there = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}.png"
    here = chr.COMP_PAGE_DIR("overview_hfradar") / f"map_of_{slug}.png"
    if not here.exists():
        here.symlink_to(there)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:overview_hfradar)=
# Overview HF Radar Data

Detailed model-data comparison page: {{ref}}`HF Radar model-data comparison page <page:{slug}-comparison>`

Full dataset page: {{ref}}`HF Radar dataset page <page:{slug}>`

[20MB zipfile of plots](https://files.axds.co/ciofs/zip/hfradar.zip)
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(pu.map_cell(slug, cat.metadata["map_description"], label="", caption=""))

    ## Loop over models first
    for model_name in [ "ciofs","nwgoa"]:
        
        nb['cells'].append(pu.text_cell(pu.header_text(model_name.upper(), header=2)))

        for source_name in source_names:
            data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
            nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=3)))

            intimerange, msg = isin_time_range(data_min_time, data_max_time, model_name)
            text = ""
            if not intimerange:
                text += msg
            else:
                for which in ["tidal","subtidal"]:
                    text += pu.header_text(which.capitalize(), header=4)
                    loc = chr.COMP_PAGE_DIR("overview_hfradar") / f"{slug}_{source_name}_{model_name}_{which}.png"
                    loc = loc.relative_to(chr.COMP_PAGE_DIR("overview_hfradar"))
                    label = f"fig-overview-hfradar-{source_name}-{model_name}-{which}"
                    caption = f"{which.capitalize()} surface currents skill score for {model_name.upper()} and dataset {source_name}"
                    text += chr.src.utils.mk_fig_wide(loc, label, caption)
            nb['cells'].append(pu.text_cell(text))
    
    nbf.write(nb, f'{chr.COMP_PAGE_DIR("overview_hfradar") / "page"}.ipynb')
    
    
def hfradar(slug):   

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in models:
        paths = omsa.paths.Paths(project_name(slug, model))
        here = outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.description}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(pu.map_cell(slug, cat.metadata["map_description"], label="", caption=""))

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))        
        
        # Single Plots
        which_plot = ["M2 Tidal Ellipses", "K1 Tidal Ellipses", "Subtidal Mean", "Hourly", "Subtidal, 6-Hourly"]
        filesuffixs = [
                    "_M2_ellipses.png",
                    "_K1_ellipses.png",
                    "_all_east_north_remove-under-50-percent-data_units-to-meters_subtidal_mean.png",
                    "_all_east_north_remove-under-50-percent-data_units-to-meters.mp4", 
                    "_all_east_north_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H.mp4",
        ]

        for plot, filesuffix in zip(which_plot, filesuffixs):
            nb['cells'].append(pu.text_cell(pu.header_text(plot, header=3)))

            for model in models:
                nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=4)))

                text = ""
                
                intimerange, msg = isin_time_range(data_min_time, data_max_time, model)
                if not intimerange:
                    text += msg
                
                else:

                    caption = f"{plot.capitalize()} from surface currents for {model.upper()} and dataset {source_name}"
                    if ".mp4" in filesuffix:
                        loc = f"https://files.axds.co/ciofs/hfradar_{model}/{slug}_{source_name}{filesuffix}"
                        label = f"fig-{source_name}-{model}-{plot}"
                        text += chr.src.utils.mk_video_wide(loc, label, caption)

                    else:
                        loc = chr.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}{filesuffix}"
                        loc = loc.relative_to(chr.COMP_PAGE_DIR(slug))
                        label = f"fig-{source_name}-{model}-{'_'.join(which_plot)}"
                        text += chr.src.utils.mk_fig_wide(loc, label, caption)
                nb['cells'].append(pu.text_cell(text))

        
        # Dropdowns of Plots
        nb['cells'].append(pu.text_cell(pu.header_text("Tidal Constants", header=3)))
        
        tidecons = ["M2","K1","S2","N2","O1","Q1","K2","P1"]
        # whichs = ["major","minor", "inclination", "phase"]
        which_plots = ["Major Amplitude", "Minor Amplitude", "Phase", "Inclination"]
        
        for model in models:

            text = ""
            
            intimerange, msg = isin_time_range(data_min_time, data_max_time, model)
            if not intimerange:
                text += msg
                
            else:
                text = f"""
``````{{div}} full-width 
`````{{dropdown}} {model.upper()}
"""
                for which_plot in which_plots:
                    text += pu.header_text(which_plot, 3)
                    
                    for tidecon in tidecons:
                        which_name = which_plot.split()[0].lower()
                        loc = chr.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}_{tidecon}-{which_name}.png"
                        if loc.is_file():  # some tidal constants weren't run
                            loc = loc.relative_to(chr.COMP_PAGE_DIR(slug))
                            label = ""  #f"fig-{source_name}-{model}-{tidecon}-{which_name}"
                            caption = ""  #f"{tidecon} {which_plot.lower()} from surface currents for {model.upper()} and dataset {source_name}"
                            text += chr.src.utils.mk_fig_wide(loc, label, caption)
                        
                text += """

`````
``````
"""
            nb["cells"].append(pu.text_cell(text))

    nbf.write(nb, f'{chr.COMP_PAGE_DIR(slug) / slug}.ipynb')
    
    
def adcp(slug):   

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in models:
        paths = omsa.paths.Paths(project_name(slug, model))
        here = outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.description}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(pu.map_cell(slug, cat.metadata["map_description"], label="", caption=""))

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))
        
        for which_tidal in ["tidal","subtidal"]:

            nb['cells'].append(pu.text_cell(pu.header_text(which_tidal.capitalize(), header=3)))
            
            varnames = ["speed", "along", "across"]
            vardescs = ["Horizontal Speed", "Along-Channel Velocity", "Across-Channel Velocity"]
            for varname, vardesc in zip(varnames, vardescs):

                nb['cells'].append(pu.text_cell(pu.header_text(vardesc.capitalize(), header=4)))

                for model in models:
                    nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=5)))

                    text = ""
                    
                    intimerange, msg = isin_time_range(data_min_time, data_max_time, model)
                    if not intimerange:
                        text += msg
                    
                    else:

                        caption = ""  # f"{which_tidal.capitalize()} {vardesc.lower()} from moored ADCP for {model.upper()} and dataset {source_name}"
                        loc = chr.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}_{varname}"
                        if which_tidal == "subtidal":
                            loc = pathlib.Path(str(loc) + "_subtidal")
                        loc = loc.with_suffix(".png")
                        loc = loc.relative_to(chr.COMP_PAGE_DIR(slug))
                        label = ""  #f"fig-{source_name}-{model}-{varname}-{which_tidal}"
                        text += chr.src.utils.mk_fig_wide(loc, label, caption)
                    nb['cells'].append(pu.text_cell(text))

        

    nbf.write(nb, f'{chr.COMP_PAGE_DIR(slug) / slug}.ipynb')
    
    
def ctd_transects(slug):   

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in models:
        paths = omsa.paths.Paths(project_name(slug, model))
        here = outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.description}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(pu.map_cell(slug, cat.metadata["map_description"], label="", caption=""))

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))
        
        varnames = ["temp","salt"]
        vardescs = ["Sea Temperature [C]", "Salinity"]
        for varname, vardesc in zip(varnames, vardescs):

            nb['cells'].append(pu.text_cell(pu.header_text(vardesc, header=3)))

            for model in models:
                nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=4)))

                text = ""
                
                intimerange, msg = isin_time_range(data_min_time, data_max_time, model)
                if not intimerange:
                    text += msg
                
                else:

                    caption = ""  # f"{which_tidal.capitalize()} {vardesc.lower()} from moored ADCP for {model.upper()} and dataset {source_name}"
                    loc = chr.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name.replace(' ', '_')}_{varname}"
                    loc = loc.with_suffix(".png")
                    loc = loc.relative_to(chr.COMP_PAGE_DIR(slug))
                    label = ""  #f"fig-{source_name}-{model}-{varname}-{which_tidal}"
                    text += chr.src.utils.mk_fig_wide(loc, label, caption)
                nb['cells'].append(pu.text_cell(text))

    nbf.write(nb, f'{chr.COMP_PAGE_DIR(slug) / slug}.ipynb')
    
    
def ctd_profiles(slug):   

    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in models:
        paths = omsa.paths.Paths(project_name(slug, model))
        here = outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.description}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    if slug == "ctd_profiles_usgs_boem":
        figpath = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}.png"
        
        ## Map of Datasets
        figpath2016 = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}_2016.png"
        figpath2017 = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}_2017.png"
        figpath2018 = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}_2018.png"
        figpath2019 = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}_2019.png"
        figpath2021 = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}_2021.png"
        if not pathlib.Path(figpath2016).exists() and \
            not pathlib.Path(figpath2017).exists() and \
                not pathlib.Path(figpath2018).exists() and \
                    not pathlib.Path(figpath2019).exists() and \
                        not pathlib.Path(figpath2021).exists():
            getattr(chr.src.plot_dataset_on_map, slug)(slug, figpath)

        text = f"""\
## Map of {cat.metadata["map_description"]}

{chr.src.utils.mk_fig_wide(figpath2016.relative_to(chr.COMP_PAGE_DIR(slug)), label="", caption="")}
{chr.src.utils.mk_fig_wide(figpath2017.relative_to(chr.COMP_PAGE_DIR(slug)), label="", caption="")}
{chr.src.utils.mk_fig_wide(figpath2018.relative_to(chr.COMP_PAGE_DIR(slug)), label="", caption="")}
{chr.src.utils.mk_fig_wide(figpath2019.relative_to(chr.COMP_PAGE_DIR(slug)), label="", caption="")}
{chr.src.utils.mk_fig_wide(figpath2021.relative_to(chr.COMP_PAGE_DIR(slug)), label="", caption="")}

"""

        nb['cells'].append(nbf.v4.new_markdown_cell(text))
        
        
    elif slug in ["ctd_profiles_kachemack_kuletz_2005_2007","ctd_profiles_emap_2008",
                  "ctd_profiles_kb_small_mesh_2006","ctd_profiles_kbay_osu_2007",
                  "ctd_profiles_piatt_speckman_1999"]:
        text = f"""\
## Map of {cat.metadata["map_description"]}
    """

        code = f"""\
getattr(chr.src.plot_dataset_on_map, "{slug}")("{slug}")
"""
        codecell = nbf.v4.new_code_cell(code)
        codecell['metadata']['tags'] = ["remove-input"]
#         from myst_nb import glue
#         # figname = f"map_of_{slug}.png"
#         # figpath = chr.COMP_PAGE_DIR(slug) / figname
#         plot = getattr(chr.src.plot_dataset_on_map, slug)(slug)
#         glue("fig_plot", plot, display=False)
    
#         ## Map of Datasets
#         text = f"""\
# ## Map of {cat.metadata["map_description"]}

# ```{{glue:figure}} fig_plot
# ```

# """

        nb['cells'].append(codecell)
    else:
        nb['cells'].append(pu.map_cell(slug, cat.metadata["map_description"], label="", caption=""))

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))
        
        varnames = ["temp","salt"]
        vardescs = ["Sea Temperature [C]", "Salinity"]
        for varname, vardesc in zip(varnames, vardescs):

            nb['cells'].append(pu.text_cell(pu.header_text(vardesc, header=3)))

            text = ""
            
            # intimerange, msg = isin_time_range(data_min_time, data_max_time, model)
            # import pdb; pdb.set_trace()
            # if not intimerange:
            #     text += msg
            
            # else:

            caption = ""  # f"{which_tidal.capitalize()} {vardesc.lower()} from moored ADCP for {model.upper()} and dataset {source_name}"
            loc1 = chr.COMP_PAGE_DIR(slug) / f"{slug}_ciofs" / f"{slug}_{source_name.replace('.','_')}_{varname}"
            loc1 = loc1.with_suffix(".png")
            loc2 = chr.COMP_PAGE_DIR(slug) / f"{slug}_nwgoa" / f"{slug}_{source_name.replace('.','_')}_{varname}"
            loc2 = loc2.with_suffix(".png")
            label = ""  #f"fig-{source_name}-{model}-{varname}-{which_tidal}"
            if loc1.is_file():
                text += f"""
```{{image}} {loc1.relative_to(chr.COMP_PAGE_DIR(slug))}
:width: 49%
```
"""

            if loc2.is_file():
                text += f"""
```{{image}} {loc2.relative_to(chr.COMP_PAGE_DIR(slug))}
:width: 49%
```
"""
            nb['cells'].append(pu.text_cell(text))

    nbf.write(nb, f'{chr.COMP_PAGE_DIR(slug) / slug}.ipynb')


# Generate comparison pages
if __name__ == "__main__":
    # slug = "hfradar"
    # chr.src.generate_comparison_pages.hfradar(slug)

    chr.src.generate_comparison_pages.overview_hfradar()

    
    # slugs = [
    #      "ctd_transects_barabara_to_bluff_2002_2003",
    #     "ctd_transects_cmi_kbnerr", 
    #     "ctd_transects_cmi_uaf",
    #     "ctd_transects_gwa", 
    #     "ctd_transects_misc_2002",
    #     "ctd_transects_otf_kbnerr",
    #     "ctd_transects_uaf",  
    #          ]
    # for slug in slugs:
    #     print(slug)
    #     chr.src.generate_comparison_pages.ctd_transects(slug)

    # slugs = [
    #     "ctd_profiles_2005_noaa",
    #     "ctd_profiles_emap_2002",
    #     "ctd_profiles_emap_2008",
    #     "ctd_profiles_kachemack_kuletz_2005_2007",
    #     "ctd_profiles_kb_small_mesh_2006",
    #     "ctd_profiles_kbay_osu_2007",
    #     "ctd_profiles_piatt_speckman_1999",
    #     "ctd_profiles_usgs_boem",
    #          ]
    # for slug in slugs:
    #     print(slug)
    #     chr.src.generate_comparison_pages.ctd_profiles(slug)

    # slugs = [
    #     # "adcp_moored_noaa_coi_2005",
    #         #  "adcp_moored_noaa_coi_other",
    #         #  "adcp_moored_noaa_kod_1",
    #          "adcp_moored_noaa_kod_2",
    #          ]
    # for slug in slugs:
    #     chr.src.generate_comparison_pages.adcp(slug)
#     slugs = [
#         # "adcp_moored_noaa_coi_2005","adcp_moored_noaa_coi_other",
#              "adcp_moored_noaa_kod_1", "adcp_moored_noaa_kod_2"]
# #     # slugs = ["moorings_noaa","moorings_kbnerr_bear_cove_seldovia","moorings_kbnerr_homer",
# #     #          "moorings_kbnerr_historical",
# #     #              "ctd_profiles_2005_noaa","adcp_moored_noaa_coi_2005","adcp_moored_noaa_coi_other"] #chr.slugs:

    # slugs = [
    #     "moorings_aoos_cdip",
    #     "moorings_circac",
    #     "moorings_kbnerr",
    #     "moorings_kbnerr_bear_cove_seldovia",
    #     "moorings_kbnerr_historical", 
    #     "moorings_kbnerr_homer",
    #     "moorings_noaa",
    #     "moorings_nps",
    #     "moorings_uaf",
    #     ]
    # for slug in slugs:
    #     print(slug)
    #     chr.src.generate_comparison_pages.generate_page(slug)
#     #     # if hasattr(chr.src.generate_comparison_pages, slug):
#     #     #     print(slug)
#     #     #     getattr(chr.src.generate_comparison_pages, slug)(slug)
