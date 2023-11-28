(page:intro_comparisons)=
# Methodology

## Software

The datasets are compared with model output from the CIOFS and NWGOA models using the `ocean-model-skill-assessor` (`OMSA`) framework, as well as dependencies therein and software written for this report. Detailed documentation is available for [OMSA](http://ocean-model-skill-assessor.readthedocs.io).

## Comparison Metrics

Multiple statistical measures of the model-data comparison are given, though mean skill score is used as the main measure. 

### All Metrics 

The available statistical metrics are:

* bias: mean of the difference
* Pearson product-moment correlation coefficient
* Index of Agreement (Willmott 1981)
* mean squared error (MSE)
* Skill score: more details below
* Root Mean Square Error (RMSE)
* Also provide distance between the grid cell and data location if relevant

### Skill score

The skill score is what is shown in all performance summaries in the model-data comparison pages. Following {cite:t}`bogden1996open` and {cite:t}`hetland2006event`, the skill score is calculated as:

\begin{align}
SS &= 1 - \frac{\Sigma^N_{i=1} (d_i - m_i)^2}{\Sigma^N_{i=1} (d_i - c_i)^2},
\end{align}

where $d_i$ are data values, $m_i$ are model values at the matching time and location to the data, and $c_i$ are representative climatological values. This approach can be used to quantify how well a long term data time series is being represented by model output as compared with a simple climatological representation. If the model performs better than climatology, the value of the skill score will be greater than 0 and hopefully closer to 1; if climatology is better and the model provides no improvement, the skill score is 0 to negative. 

In some cases there is not a relevant climatology to compare with. In such cases, $c_i$ are taken as the mean of the data time series.


## Details of comparisons

### Units

| Variable                      | Unit        |
| ----------------------------- | ----------- |
| Sea water temperature         | Deg Celsius |
| Sea water salinity            | PSU         |
| Sea surface height            | m           |
| Along/across-channel velocity | m/s         |
| Speed                         | m/s         |


### Comparisons shown

One or more of the following time series modifications is used where noted to alter the data and model time series before comparison. Detailed explanations of each are given below, and which have been used are noted for each model-data comparison.

#### Tidal filtering

The tides are an important feature of Cook Inlet, and if we do not remove them from the time series we want to compare, they will dominate the model-data comparisons. Because the tides have a highly correlated signal, comparing time series with them intact from moment to moment gives a skewed comparison; if the model-data comparison at one time is close, it probably will also be at the next time. A better way to compare the model and data in a regime like this is by first filtering out the tides; we use the `pl33` filter to do so. We filter out the tides for most model-data comparisons presented here, though if a sea surface height time series is relatively short, we left it with tides to show the full comparison.

#### Long time series

Long time series of temperature or salinity tend to have significant annual cycles. In a similar way to the tides, this can skew the meaning of our statistical metrics because, for example, the large, expected temperature cycle dominates any smaller features. Because of this, we present long time series of temperature and salinity as the anomaly with respect to the monthly mean calculated from the data time series across the available years. We will often also show the comparisons without removing the monthly mean to help give an intuitive feel for how the model is behaving with respect to the data.

#### Mean subtracted

Numerical ocean models tend to not have a specific vertical datum that they are calculated with respect to. For this reason, when the sea surface height is compared between model and data, the mean of each is separately subtracted from the time series before comparison.

#### Harmonic tidal analysis

Harmonic tidal analysis was run to calculated tidal constants with the HF Radar data. We ran a Python version of the classic Matlab package T_Tide {cite:p}`pawlowicz2002classical`.