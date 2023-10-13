"""Generate currents and mean plot pages."""

import ciofs_hindcast_report as chr
import intake
import nbformat as nbf


def generate_currents_page():
    """Generate page of descriptive currents plots.
    
    This uses plots produced by plot_descriptive_currents.py.
    """
    
    slugs = ["adcp_moored_noaa_coi_2005", "adcp_moored_noaa_coi_other"]
    
    nb = nbf.v4.new_notebook()
    figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS / "model_conditions.png"
    caption = "DESCRIBE"
    text = f"""\
# Model Currents

Surface currents modeled by CIOFS and NWGOA are shown for each NOAA Cook Inlet ADCP survey location for 4 years meant to represent a range of possible behaviors.

See the full dataset pages for these ADCP data for more information: {{ref}}`page:{slugs[0]} and  {{ref}}`page:{slugs[1]}`.

The annual mean temperature represents the yearly averaged surface temperature along the southern open boundary of the CIOFS model. It is calculated by taking the open boundary forcing of CIOFS (derived from HYCOM GOFS 3.1 Global Reanalysis), extracting the surface level, and averaging this 2D slice over the year and boundary nodes to derive a single value summarizing the annual surface temperature along the southern open boundary. MORE HERE

{chr.src.utils.mk_fig(figname.relative_to(chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS), "fig-model-conditions", caption)}
"""

    # Add these cells to the notebook
    nb['cells'] = [nbf.v4.new_markdown_cell(text),
                   ]
    
    years = [1999, 2003, 2005, 2008]
    for slug in slugs:
        cat = intake.open_catalog(chr.CAT_NAME(slug))
        source_names = chr.src.utils.get_source_names(cat)
        
        for source_name in source_names:
            figname = chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES / "currents" / source_name / f"map.png"
            text = f"""
## {source_name}

{chr.src.utils.mk_fig_wide(figname.relative_to(chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS), f"fig-{source_name}-map", "caption")}
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

{chr.src.utils.mk_fig(figname.relative_to(chr.PATH_OUTPUTS_DESCRIPTIVE_PAGES_CURRENTS), f"fig-{source_name}-{i}", "caption")}
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