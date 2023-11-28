"""Generate currents and mean plot pages."""

import ciofs_hindcast_report as chr
import intake
import nbformat as nbf
import ciofs_hindcast_report.src.page_utils as pu


def generate_currents_page():
    """Generate page of descriptive currents plots.
    
    This uses plots produced by plot_descriptive_currents.py.
    """
    
    slugs = ["adcp_moored_noaa_coi_2005", "adcp_moored_noaa_coi_other"]
    
    nb = nbf.v4.new_notebook()
    figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS / "model_conditions.png"
    caption = "Summarized forcing conditions for CIOFS by year for differentiation."
    text = f"""\
# Model Currents

Surface currents modeled by CIOFS and NWGOA are shown for each NOAA Cook Inlet ADCP survey location for 4 years meant to represent a range of possible behaviors.

See the full dataset pages for these ADCP data for more information: {{ref}}`page:{slugs[0]}` and  {{ref}}`page:{slugs[1]}`.

The annual mean temperature represents the yearly averaged surface temperature along the southern open boundary of the CIOFS model. It is calculated by taking the open boundary forcing of CIOFS (derived from HYCOM GOFS 3.1 Global Reanalysis), extracting the surface level, and averaging this 2D slice over the year and boundary nodes to derive a single value summarizing the annual surface temperature along the southern open boundary. The inflow is calculated as a sum across the rivers for the year, relative across the years.

Looking at the spread of years, which only include the years that NWGOA was also run, we chose the warm year as 2003 and cool year as 1999 since they have relatively equal river forcing. We were not able to disentangle the river forcing from the temperature forcing so chose two years at opposite ends of the spread: 2005 (warm and more river inflow) and 2008 (cool and less river inflow). These are the years shown below.

Zip file of plots below: [430MB zipfile of currents plots](https://files.axds.co/ciofs/zip/descriptive_currents.zip)

{chr.src.utils.mk_fig(figname.relative_to(chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS), "fig-model-conditions", caption)}
"""
    # 
    # Add these cells to the notebook
    nb['cells'] = [nbf.v4.new_markdown_cell(text),
                   ]
    
    # # set up maps for the 2 ADCP datasources
    # for slug in slugs:
    #     #symlink in map from data comp dir
    #     there = chr.COMP_PAGE_DIR(slug) / f"map_of_{slug}.png"
    #     here = chr.COMP_PAGE_DIR("overview_hfradar") / f"map_of_{slug}.png"
    #     if not here.exists():
    #         here.symlink_to(there)
        
    #     cat = intake.open_catalog(chr.CAT_NAME(slug))
    #     nb['cells'].append(pu.map_cell(slug, cat.metadata["map_description"], label="",))
    
    
    years = [1999, 2003, 2005, 2008]
    for slug in slugs:
        cat = intake.open_catalog(chr.CAT_NAME(slug))
        source_names = chr.src.utils.get_source_names(cat)
        
        for source_name in source_names:
            figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES / "currents" / source_name / f"map.png"
            text = f"""
## {source_name}

{chr.src.utils.mk_fig_wide(figname.relative_to(chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS), "", "")}
"""
            for year in years:
                text += f"""
### {year}
`````{{div}} full-width 
````{{dropdown}} Comparison plots by month

"""
                fignames = sorted((chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS / source_name).glob(f"{year}*.png"))
                # import pdb; pdb.set_trace()
                for i, figname in enumerate(fignames):
                    text += f"""

{chr.src.utils.mk_fig(figname.relative_to(chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS), "", "")}
"""

                text += f"""
````
`````
"""
                
            nb['cells'] += [nbf.v4.new_markdown_cell(text),
                        ]


    nbf.write(nb, f'{chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS / "page"}.ipynb')
    


# Generate pages
if __name__ == "__main__":

    generate_currents_page()