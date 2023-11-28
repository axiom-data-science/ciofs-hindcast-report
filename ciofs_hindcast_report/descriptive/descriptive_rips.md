---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3.10.0 ('ciofs')
  language: python
  name: python3
---

# Rip plots

Rips are well-known features of Cook Inlet [{cite:t}`regionmapping`, {cite:t}`okkonen2003measurements`, {cite:t}`potter2010surface`]. However, they can be difficult to capture in numerical simulations. The animations below aim to demonstrate whether or not rips may be captured in two numerical models. The animations show vertical velocity 5 m below mean sea level, therefore, rips would show up as negative vertical velocity, or blue in the plots. There are four time periods presented: a neap and a spring tide for summer and winter seasons. 

The CIOFS model (left side in each animation) has much higher horizontal resolution than the NWGOA model (right side) ({ref}`page:model_description`) and that is readily apparent in the results. Accordingly, the CIOFS model is able to capture much finer resolution features such as are seen in the animations. Some activity along the known western or mid-channel rips is noticeable for the CIOFS model.

[32MB zipfile of plots](https://files.axds.co/ciofs/zip/descriptive_rips.zip)

```{code-cell} ipython3
:tags: [remove-input]

import xarray as xr
import hvplot.xarray
```

+++ {"jupyter": {"outputs_hidden": true}, "tags": ["full-width"]}

## Summer, spring tide (July 2004)

```{div} full-width
<video controls width=1000px src="../_static/descriptive_rips/rip_2004-07-03.mp4"></video>
```

+++ {"jupyter": {"outputs_hidden": true}, "tags": ["full-width"]}

## Summer, neap tide (August 2004)

```{div} full-width
<video controls width=1000px src="../_static/descriptive_rips/rip_2004-08-10.mp4"></video>
```

+++ {"jupyter": {"outputs_hidden": true}, "tags": ["full-width"]}

## Winter, spring tide (December 2004)

```{div} full-width
<video controls width=1000px src="../_static/descriptive_rips/rip_2004-12-13.mp4"></video>
```

+++ {"jupyter": {"outputs_hidden": true}, "tags": ["full-width"]}

## Winter, neap tide (December 2004)

```{div} full-width
<video controls width=1000px src="../_static/descriptive_rips/rip_2004-12-05.mp4"></video>
```
