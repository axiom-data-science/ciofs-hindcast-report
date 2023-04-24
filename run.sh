#!/bin/sh

# Run script to generate catalogs
python ciofs_hindcast_report/src/generate_catalogs.py

# Run script to generate pages describing datasets
python ciofs_hindcast_report/src/generate_data_pages.py

# Convert all notebooks to markdown

# find all ipynb files in ciofs_hindcast_report except under _build and .ipynb_checkpoints
# https://www.theunixschool.com/2012/07/find-command-15-examples-to-exclude.html
notebooks=$(find ciofs_hindcast_report -type d \( -name _build -o -name .ipynb_checkpoints \) -prune -o -name "*.ipynb" -print)
# to list back: echo "$notebooks"

for notebook in $( echo "$notebooks" )
do
    jupytext "$notebook" --to myst
done


# Build book
jupyter-book build ciofs_hindcast_report/