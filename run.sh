#!/bin/sh

# # Run script to generate catalogs
# python ciofs_hindcast_report/src/generate_catalogs.py

# Run script to generate pages describing datasets
python ciofs_hindcast_report/src/generate_data_pages.py

# Run script to generate comparison pages
python ciofs_hindcast_report/src/generate_comparison_pages.py

# descriptive plots
python ciofs_hindcast_report/src/plot_descriptive_currents.py
python ciofs_hindcast_report/src/generate_descriptive_pages.py

# Convert all notebooks to markdown

# find all ipynb files in ciofs_hindcast_report except under _build and .ipynb_checkpoints
# https://www.theunixschool.com/2012/07/find-command-15-examples-to-exclude.html
notebooks=$(find ciofs_hindcast_report -type d \( -name _build -o -name .ipynb_checkpoints  -o -name _save_notebooks \) -prune -o -name "*.ipynb" -print)
# notebooks=$(find ciofs_hindcast_report -type d \( -name _build -o -name .ipynb_checkpoints \) -prune -o -name "*.ipynb" -print)
# to list back: echo "$notebooks"

for notebook in $( echo "$notebooks" )
do
    jupytext "$notebook" --to myst
done


# Build book
jupyter-book build ciofs_hindcast_report/