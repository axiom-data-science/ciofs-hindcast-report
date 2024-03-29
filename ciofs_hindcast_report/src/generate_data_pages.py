
import pathlib
import intake
import nbformat as nbf
import ciofs_hindcast_report as chr
import pandas as pd
import holoviews as hv
from holoviews import opts
# from bokeh.plotting import output_notebook
# output_notebook()
import warnings
warnings.filterwarnings('ignore')

def make_source_metadata_table(cat):
    source_names = chr.src.utils.get_source_names(cat)
    mdfs = []
    for source_name in source_names:
        metadata_no_plots = {"Dataset": source_name}
        metadata_no_plots.update({key:values for key, values in cat[source_name].metadata.items() if key != "plots" and key != "catalog_dir" and key != "maptype" and key != "deployments"})
        # format times better
        metadata_no_plots.update({key: str(pd.Timestamp(metadata_no_plots[key])) for key, values in metadata_no_plots.items() if (("time" in key.lower()) or ("good_data" in key.lower())) and not "zone" in key.lower()})
        mdfs.append(pd.DataFrame.from_dict(metadata_no_plots, orient="index"))
        # print(metadata_no_plots)
        # source_metadata_table.update(metadata_no_plots)
    if len(mdfs) > 0:
        mdf = pd.concat(mdfs, axis=1)
        mdf = mdf.T.reset_index(drop=True)
    else:
        mdf = pd.DataFrame()
    return mdf


def generate_dataset_notebook(slug, desc, metadata):
# def generate_dataset_notebook(slug, project_name, map_desc, summary, plottypes, header_names):

    # https://gist.github.com/fperez/9716279

    nb = nbf.v4.new_notebook()

    ## INITIAL STUFF

    imports = f"""\
import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
import holoviews as hv
from holoviews import opts
"""

    text = f"""\
(page:{slug})=
# {desc}

* {metadata["project_name"]}
* {slug}
* {metadata["time"]}

{metadata["summary"]}

{metadata["notes"]}

```{{dropdown}} Dataset metadata

{make_source_metadata_table(intake.open_catalog(chr.CAT_NAME(slug))).to_markdown()}

```


"""

    # Open catalog
    # cat = intake.open_catalog(chr.CAT_NAME(slug))
    code = f"""\
cat = intake.open_catalog(chr.CAT_NAME("{slug}"))"""

    # Add these cells to the notebook
    imports_cell = nbf.v4.new_code_cell(imports)
    imports_cell['metadata']['tags'] = ["remove-input"]  # don't show imports cell
    codecell = nbf.v4.new_code_cell(code)
    codecell['metadata']['tags'] = ["remove-input"]
    nb['cells'] = [imports_cell,
                   nbf.v4.new_markdown_cell(text),
                   codecell,
                   ]

    ## Map of Datasets
    text = f"""\
## Map of {metadata["map_description"]}
    """

    code = f"""\
getattr(chr.src.plot_dataset_on_map, "{slug}")("{slug}")
"""
    codecell = nbf.v4.new_code_cell(code)
    codecell['metadata']['tags'] = ["remove-input"]

    nb['cells'].extend([nbf.v4.new_markdown_cell(text),
                        codecell,])

    # import pdb; pdb.set_trace()
    ## REST OF IT
    cat = intake.open_catalog(chr.CAT_NAME(slug))
    source_names = chr.src.utils.get_source_names(cat)
    iheader = 0
    # for i, source_name in enumerate(source_names):
    # if header_names is not None:  # initialize
    #     current_header = header_names[0]
    header_names = metadata["header_names"]
    for isource_name, source_name in enumerate(source_names):
    
        # Put header and then date and variable
        if header_names is not None:
            
            if len(header_names) == len(source_names):
                source_md_0 = f"""\
## {header_names[isource_name]}
"""
                nb['cells'].extend([nbf.v4.new_markdown_cell(source_md_0),])
                # iheader += 1
                
            
            elif iheader < len(header_names) and header_names[iheader] in source_name:# == current_header:
            # if iheader == 0 or header_names[iheader] in source_name:# == current_header:
                # current_header = header_names[0]
                source_md_0 = f"""\

```{{div}} full-width
## {header_names[iheader]}
```
"""
                nb['cells'].extend([nbf.v4.new_markdown_cell(source_md_0),])
                iheader += 1

            source_md_1 = f"""\
{source_name}
        """

        else:
            source_md_1 = f"""\
## {source_name}
        """
        
#         # next include source metadata
#         metadata_no_plots = {key:values for key, values in cat[source_name].metadata.items() if key != "plots" and key != "catalog_dir"}
#         text = f"""\
            
# {pd.DataFrame.from_dict(metadata_no_plots, orient="index").T.to_markdown()}

# """

        # Add these cells to the notebook
        nb['cells'].extend([nbf.v4.new_markdown_cell(source_md_1)])
        #  # Add these cells to the notebook
        # nb['cells'].extend([nbf.v4.new_markdown_cell(source_md_1),
        #             nbf.v4.new_markdown_cell(text),
        #             ])
        
        
        source_code_1 = ""
        if "map" in cat[source_name].metadata["plots"]:
            source_code_1 += f"cat['{source_name}'].plot.map() + "
            del(cat[source_name].metadata["plots"]["map"])
        # speed and direction need to be "*" together instead of "+"
        if "direction" in cat[source_name].metadata["plots"]:
            source_code_1 += f"""
hv.output(widget_location='bottom')
cat['{source_name}'].plot.direction().opts(opts.VectorField(magnitude='speed_subtidal'))
"""
#             source_code_1 += f"""
# ds = cat['{source_name}'].read()
# dmap = cat['{source_name}'].plot.speed() * cat['{source_name}'].plot.direction()
# dmap = dmap[[t for t in ds['time'].values]]
# hv.HoloMap(dmap)"""
#             source_code_1 += f"""
# holomap1 = cat['{source_name}'].plot.speed()
# holomap2 = cat['{source_name}'].plot.direction()
# holomap1 * holomap2"""
#             source_code_1 += f"""
# holomap1 = hv.HoloMap(cat['{source_name}'].plot.speed())
# holomap2 = hv.HoloMap(cat['{source_name}'].plot.direction())
# holomap1 * holomap2"""
        else:
            for plot in cat[source_name].metadata["plots"]:
                source_code_1 += f"cat['{source_name}'].plot.{plot}() + "
            source_code_1 = source_code_1.rstrip(" + ")
        
        # for line plots, have one column and all subplots since otherwise
        # are huge files
        if "data" in cat[source_name].metadata["plots"]:
            if "line" in cat[source_name].metadata["plots"]["data"]["kind"]:
                # just for large enough widtg
                if cat[source_name].metadata["plots"]["data"]["width"] > 400:
                    # source_code_1 = f"({source_code_1}).cols(1)"
                    # make sure there are two y variables
                    if len(cat[source_name].metadata["plots"]["data"]["y"]) > 1:
                        source_code_1 = f"({source_code_1}).cols(1)"
                    
                # # make sure time is the x axis by checking the column name for time
                # if "T" in pd.DataFrame(columns=[cat[source_name].metadata["plots"]["data"]["x"]]).cf.axes:
        
        plot_cell = nbf.v4.new_code_cell(source_code_1)
        # # make plot wide for certain catalogs
        # if slug in ["adcp_moored_noaa_coi_2005",
        #             "adcp_moored_noaa_coi_other",
        #             "adcp_moored_noaa_kod_1",
        #             "adcp_moored_noaa_kod_2",
        #             "ctd_towed_otf_kbnerr"]:
        #     plot_cell['metadata']['tags'] = ["full-width"]
        # make all plot cells full width
        plot_cell['metadata']['tags'] = ["full-width"]
        plot_cell['metadata']['tags'].append("remove-input")
        nb['cells'].extend([plot_cell,])

    nbf.write(nb, f'{chr.DATA_PAGE_PATH(slug)}.ipynb')


def generate_dataset_summary(no_map=None):
    no_map = no_map or []

    nb = nbf.v4.new_notebook()

    ## INITIAL STUFF

    imports = f"""\
import ciofs_hindcast_report as chr
import intake
import pandas as pd
import numpy as np
import hvplot.pandas
"""

    # create markdown table
    table = {}
    for i, slug in enumerate(chr.slugs):
        cat = intake.open_catalog(chr.CAT_NAME(slug))
        table[i+1] = {"description": cat.description, "slug": cat.name}
        table[i+1].update({key: cat.metadata[key] for key in ["project_name", "time", "featuretype", "included", "notes"]})


    text = f"""\
# Datasets Considered

## Table of All Datasets

```{{div}} full-width

{pd.DataFrame.from_dict(table, orient="index").to_markdown()}

```

## Summary of Each Dataset
"""

    imports_cell = nbf.v4.new_code_cell(imports)
    imports_cell['metadata']['tags'] = ["remove-input"]  # don't show imports cell

    # Add these cells to the notebook
    nb['cells'] = [imports_cell,
                   nbf.v4.new_markdown_cell(text),
                   ]

    for slug in chr.slugs:
        cat = intake.open_catalog(chr.CAT_NAME(slug))
        # print(slug)
        text = f"""
### {cat.description}

* {cat.metadata["project_name"]}
* {cat.metadata["time"]}
* Slug: {slug}
* Included: {cat.metadata["included"]}
* Feature type: {cat.metadata["featuretype"]}
* See the full dataset page for more information: {{ref}}`page:{slug}`

{cat.metadata["summary"]}

Notes:

{cat.metadata["notes"]}

````{{div}} full-width
```{{dropdown}} Dataset metadata

{make_source_metadata_table(intake.open_catalog(chr.CAT_NAME(slug))).to_markdown()}

```
````
"""
        nb['cells'].extend([nbf.v4.new_markdown_cell(text)])

        # can input slugs for which we won't plot map
        if slug not in no_map:

            map_text = f"""


**Map of {cat.metadata["map_description"]}**
"""

            code = f"""\
getattr(chr.src.plot_dataset_on_map, "{slug}")("{slug}")
"""
            map_code = nbf.v4.new_code_cell(code)
            map_code['metadata']['tags'] = ["remove-input"]
       
            nb['cells'].extend([nbf.v4.new_markdown_cell(map_text),
                                map_code])

    nbf.write(nb, f'{chr.PATH_REPORT / "summarize_datasets"}.ipynb')


# Generate data pages
if __name__ == "__main__":
    from time import time
    for slug in ["moorings_noaa"]:#chr.slugs:
        cat = intake.open_catalog(chr.CAT_NAME(slug))
        # only make page if including dataset
        if cat.metadata["included"]:
            nb_path = pathlib.Path(f'{chr.DATA_PAGE_PATH(slug)}.ipynb')
            if not nb_path.exists():
                print(slug)
                source_names = chr.src.utils.get_source_names(cat)
                start_time = time()
                generate_dataset_notebook(slug, cat.description, cat.metadata)
                # generate_dataset_notebook(slug, cat.description, 
                #                 cat.metadata["map_description"], 
                #                 cat.metadata["summary"],
                #                 #   len(cat[source_names[0]].metadata["plots"]),
                #                 cat.metadata["header_names"],
                #                 )
                print(f"Notebook generation: Slug {slug} required time {time() - start_time}")
    #     # if not chr.CAT_NAME(slug).is_file():
    #         # getattr(chr.src.generate_data_pages, slug)(slug)
    # pass
    
    # # make dataset summary notebook
    # generate_dataset_summary(no_map=["adcp_towed_otf_kbnerr", "ctd_profiles_2005_osu"])
    
    
