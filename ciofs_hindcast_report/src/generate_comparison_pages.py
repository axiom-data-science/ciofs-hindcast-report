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
# sns.set_theme()

models = ["ciofs", "nwgoa"]
key_variables = ["ssh", "temp", "salt", "along", "across", "speed"]
# dsm = xr.open_zarr("http://xpublish-ciofs.srv.axds.co/datasets/ciofs_hindcast/zarr/")
# time_range = dict(nwgoa=[pd.Timestamp("1999-01-01"), pd.Timestamp("2009-01-01")],
#                   ciofs=[pd.Timestamp("1999-01-01"), pd.Timestamp(dsm.ocean_time[-1].values)])

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

def mk_fig(path, label, caption):

    text = f"""

```{{figure}} {path}
---
name: {label}
---
{caption}
```

"""
    return text

def mk_fig_wide(path, label, caption):

    text = f"""

````{{div}} full-width                
```{{figure}} {path}
---
name: {label}
---
{caption}
```
````

"""
    return text


def aggregate_overall_stats(slug):

    dfmodels = []
    for model in models:
        statspaths = sorted(list(outdir(slug, model).glob(f"*.yaml")))
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
    monthly_mean = df[varname].groupby(df.cf["T"].month).mean()
    # monthly_mean = df[varname].groupby(df.cf["T"].dt.month).mean()
    # unclear why I have to shift this
    monthly_mean_shifted = monthly_mean.copy()
    monthly_mean_shifted.index = monthly_mean_shifted.index - 1

    df = df.set_index(df.cf["T"].month)
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


def moorings_noaa():
    text = f"""
Overall, the CIOFS model something something, as shown in {{numref}}`Figure {{number}}<fig-overall-moorings_noaa-ssh-subtract-mean>`.

"""
    return text

def moorings_kbnerr_bear_cove_seldovia():
    text = f"""
Overall, the salinity from the CIOFS model demonstrates much less high frequency variability than the NWGOA model as shown in (update reference) {{numref}}`Figure {{number}}<fig-overall-moorings_noaa-ssh-subtract-mean>`.

"""
    return text






def generate_page(slug):   
    dsm = xr.open_zarr("http://xpublish-ciofs.srv.axds.co/datasets/ciofs_hindcast/zarr/")
    
    time_range = dict(nwgoa=[pd.Timestamp("1999-01-01"), pd.Timestamp("2009-01-01")],
                  ciofs=[pd.Timestamp("1999-01-01"), pd.Timestamp(dsm.ocean_time[-1].values)])

     
# def moorings_noaa(slug):    
    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in models:
        here = outdir(slug,model)
        # import pdb; pdb.set_trace()
        if not here.exists():
            here.symlink_to(omsa.paths.OUT_DIR(project_name(slug, model)))
    
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

    imports = f"""\
import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
from IPython.display import Image, display
"""

    text = f"""\
# {cat.description}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`
"""

    # Add these cells to the notebook
    imports_cell = nbf.v4.new_code_cell(imports)
    imports_cell['metadata']['tags'] = ["remove-input"]  # don't show imports cell
    nb['cells'] = [imports_cell,
                   nbf.v4.new_markdown_cell(text),
                #    nbf.v4.new_code_cell(code),
                   ]

    # run the map code
    figname = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}.png"
    # import pdb; pdb.set_trace()
    if not pathlib.Path(figname).exists():
        getattr(chr.src.plot_dataset_on_map, slug)(slug, figname)
    
    ## Map of Datasets
    text = f"""\
## Map of {cat.metadata["map_description"]}

{mk_fig_wide(figname.relative_to(chr.COMP_PAGE_DIR(slug)), f"fig-map-{slug}", f"Map of {slug} data locations")}

"""
#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
    
    
    ## Overall summary of statistics
    dfstats = aggregate_overall_stats(slug)
    
    dfstats_by_heading = dfstats.reset_index().set_index(["key_variable","ts_mods"]).sort_index()[["source_name","ciofs","nwgoa"]]
    
    text = f"""\
## Performance Summary
"""
    if hasattr(chr.src.generate_comparison_pages, slug):
        text += f"""

{getattr(chr.src.generate_comparison_pages, slug)()}
"""
    nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
    
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
        
        # if figname.name == "moorings_kbnerr_bear_cove_seldovia_salt_subtidal.png":
        #     import pdb; pdb.set_trace()
        # print(figname.name)
        plot_overall_stats(df_to_plot, figname=figname)
        
        label = f"fig-overall-{slug}-{key_variable}-{ts_mods}"
        caption = f"Skill score for {translate_var(key_variable).lower()}, {translate(ts_mods)}"

        # key_variable (0), ts_mods (1)
        text = f"""\
### {translate_var(key_variable)}: {translate(ts_mods)}

{mk_fig_wide(figname.name, label, caption)}

"""
        nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
    
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
                source_md_0 += f"""
{model.upper()}: Data time range is {data_min_time_str} to {data_max_time_str} but model ends {time_range[model][1].date()}.

"""

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
                plot_source_stats(dfs.reset_index().set_index("start_time")[models], source_name, figname)
                label = f"fig-{source_name}-{key_variable}-{ts_mods}"
                caption = f"Skill score by year for {translate_var(key_variable).lower()}, {translate(ts_mods)}"
                text = mk_fig_wide(figname.name, label, caption)
                nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
                
                # if this is an anomaly calculation, show mean
                if "subtract-monthly-mean" in ts_mods:
                    dfd = cat[source_name].read()
                    figname = chr.COMP_PAGE_DIR(slug) / f"{slug}_{source_name}_{key_variable}_mean.png"
                    # import pdb; pdb.set_trace()
                    plot_mean(dfd, dfd.cf[key_variable].name, figname)      
                    label = f"fig-{source_name}-{key_variable}"
                    caption = f"{translate_var(key_variable)} averaged monthly across data range with variation across years included."
                    text = mk_fig_wide(figname.name, label, caption)
                    nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
                
            for model in models:

                header = f"""\
#### {model}

"""
                
                # loop over 1 row or multiple years of figures for 
                # source_name, key_Variable, ts_mods combination
                if isinstance(dfs, pd.Series):
                    dfs = dfs.to_frame().T

                if len(dfs) > 1:
                    header += """

`````{div} full-width 
````{dropdown} Comparison plots by year

"""
                    
                for row in dfs.iterrows():
                    row = row[1]
                    
                    # row might be mostly nan's if it is present for one model but not the other
                    # in which case, skip
                    if pd.isnull(row[model]):
                        continue
                    
                    if len(dfs) > 1:
                        header += f"""\
##### {row["start_time"]}

"""
                    path = row[f'path_{model}'].with_suffix('.png').relative_to(chr.COMP_PAGE_DIR(slug))
                    # import pdb; pdb.set_trace()
                    label = f"fig-{model}-{source_name}-{key_variable}-{ts_mods}"
                    caption = f"Model-data comparison for {source_name} of {translate_var(key_variable).lower()}"
                    if len(dfs) > 1:
                        label += f"-{row['start_time']}"
                        caption += f" for {row ['start_time']}"
                    header += mk_fig(path, label, caption)

                if len(dfs) > 1:
                    header += """

````
`````
"""


                nb['cells'].extend([nbf.v4.new_markdown_cell(header),])

    nbf.write(nb, f'{chr.COMP_PAGE_DIR(slug) / slug}.ipynb')


# Generate comparison pages
if __name__ == "__main__":
    slugs = ["moorings_noaa","moorings_kbnerr_bear_cove_seldovia","moorings_kbnerr_homer",
             "moorings_kbnerr_historical",
                 "ctd_profiles_2005_noaa","adcp_moored_noaa_coi_2005","adcp_moored_noaa_coi_other"] #chr.slugs:
    # slugs = ["moorings_noaa"]
    for slug in slugs:
        print(slug)
        chr.src.generate_comparison_pages.generate_page(slug)
        # if hasattr(chr.src.generate_comparison_pages, slug):
        #     print(slug)
        #     getattr(chr.src.generate_comparison_pages, slug)(slug)
