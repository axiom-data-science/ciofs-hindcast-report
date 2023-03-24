# CIOFS Hindcast Report

Report for running and validating the CIOFS hindcast simulation and comparing with NWGOA

## Usage

### Building the book

If you'd like to develop and/or build the CIOFS Hindcast Report, you should:

1. Clone this repository
2. Build the Anaconda environment with `conda env create -f environment.yml`


To make new report pages:

1. Decide if you want to write a markdown or notebook file. Markdown files will be rendered statically whereas notebooks can be run.
2. Make a new notebook or markdown file in `ciofs_hindcast_report/report` or `ciofs_hindcast_report/appendix`, as appropriate.
3. Add new chapter to `_toc.yml` for your new file.
4. For our workflow, if you want to run code, write a notebook and then convert it to a Myst NB file. Then convert it with `jupytext NOTEBOOK_NAME.ipynb --to myst` to get a myst-flavored markdown file. (You can also convert the other way with `jupytext MARKDOWN.md --to ipynb`.)
5. Run `jupyter-book clean ciofs_hindcast_report/` to remove any existing builds (though maybe this would remove caches?)
6. Run `jupyter-book build ciofs_hindcast_report/` to build the report
7. Be sure to commit your markdown file (not ipynb file) to the repository.

A fully-rendered HTML version of the book will be built in `ciofs_hindcast_report/_build/html/`.

Use the directories `inputs`, `outputs`, and `code` for placing dependencies or outputs. Add to the paths in `__init__.py` if you add a subdirectory, so that it can be referenced similarly to other paths in the report. 


### Push static compiled files to update the report on github

Once you get the report in the form you want, with changes in the main branch, you can run the following to push the compiled html files to update the report at https://axiom-data-science.github.io/ciofs-hindcast-report:

    ghp-import -n -p -f ciofs_hindcast_report/_build/html


### Troubleshooting

If a notebook absolutely cannot be run by the Jupyter book compilation, you can instead run the notebook yourself and commit the .ipynb file itself to the repository. The notebook will be rendered into html but not run.

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
