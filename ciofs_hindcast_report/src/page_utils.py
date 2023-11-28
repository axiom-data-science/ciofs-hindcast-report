"""Utilities for generating pages."""


import ciofs_hindcast_report as chr
import nbformat as nbf
import pathlib

def map_cell(slug, map_description, figname=None, label=None, caption=None):
    if figname is None:
        figname = f"map_of_{slug}.png"
    if label is None:
        label = f"fig-map-{slug}"
    if caption is None:
        caption = f"Map of {slug} data locations"
    # run the map code
    figpath = chr.COMP_PAGE_DIR(slug) / figname
    # import pdb; pdb.set_trace()
    if not pathlib.Path(figpath).exists():
        getattr(chr.src.plot_dataset_on_map, slug)(slug, figpath)
    
    ## Map of Datasets
    text = f"""\
## Map of {map_description}

{chr.src.utils.mk_fig_wide(figpath.relative_to(chr.COMP_PAGE_DIR(slug)), label, caption)}

"""

    return nbf.v4.new_markdown_cell(text)


def add_tag_to_cell(cell, tag):
    cell['metadata']["tags"] = cell['metadata'].get("tags", [])
    cell['metadata']['tags'].append(tag)
    return cell


def imports_cell():
    imports = f"""\
import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
from IPython.display import Image, display
"""

    # Add these cells to the notebook
    imports_cell = nbf.v4.new_code_cell(imports)
    imports_cell = add_tag_to_cell(imports_cell, "remove-input")  # don't show imports cell
    
    return imports_cell


def text_cell(text, header=None):
    return nbf.v4.new_markdown_cell(text)


def header_text(text, header):
    text = f"""\
{"#"*header} {text}

"""
    return text
