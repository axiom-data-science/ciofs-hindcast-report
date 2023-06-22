# Processing input files for 20-year CIOFS hindcast

## Background
The objective of this project is to convert the [CIOFS operational model from NOAA CO-OPS](https://tidesandcurrents.noaa.gov/ofs/dev/ciofs/ciofs_info.html) into a hindcast model and perform the hindcast run for the years 1998 to 2018. The year 1998 will serve as the spin-up period, and the resulting model output will be from January 1st, 1999 to December 31st, 2018.

The same model parameters from the CO-OPS operational CIOFS will be used for the hindcast, including the model grid and bathymetry, the locations of river inputs, and harmonic tides. However, other input files that are time-dependent need to be prepared for the hindcast. These include the initial condition file, open boundary condition files, meteorological forcing files, and river input files.

Data sources for these input files are based on spatial and temporal availability. The initial and open boundary conditions will be extracted from HYCOM GOFS 3.1 Global products, which are available every three hours from 1994 to the present, with a 0.04° resolution. Meteorological forcing data will be obtained from ERA5, covering the period from 1940 to the present, with an hourly temporal resolution and a 0.25° spatial resolution. River data will be sourced from USGS stations, and the preparation of the river files is covered [here](./river_forcing_demo.md).

Codes used to generate the initial condition file, open boundary condition files, and meteorological forcing files are ERA5-ROMS (https://github.com/trondkr/ERA5-ROMS) and pyroms (https://github.com/ESMG/pyroms). Docker was used to create the environment and dependencies for these codes, and apply minor bug fixes for pyroms. Here is the contents of the dockerfile:
```
FROM ubuntu:latest

ADD .cdsapirc /root/
RUN apt-get update && apt-get install -y wget bzip2 git libnetcdf-dev libnetcdff-dev gfortran

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh && \
    bash Miniconda3-py39_23.1.0-1-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-py39_23.1.0-1-Linux-x86_64.sh

# Set up conda environment and install Mamba
ENV PATH /opt/conda/bin:$PATH
# Install mamba
RUN conda install -y mamba -c conda-forge

RUN mamba install -y -c conda-forge numpy==1.23.5 scipy matplotlib basemap netcdf4 nco pynco cftime lpsolve55 pip xarray xesmf cartopy numba
RUN sed -i 's/import\ ESMF/import\ esmpy\ as\ ESMF/g' /opt/conda/lib/python3.9/site-packages/xesmf/backend.py
# install pyroms
RUN git clone https://github.com/ESMG/pyroms.git
RUN sed -i 's/np\.float/float/g' pyroms/pyroms/pyroms/grid.py
RUN sed -i 's/self\.hc = min(self\.hmin, self\.Tcline)/self\.hc = min(max(0, self\.hmin), self\.Tcline)/g' pyroms/pyroms/pyroms/vgrid.py
RUN sed -i '20d' pyroms/pyroms_toolbox/pyroms_toolbox/Grid_HYCOM/get_nc_Grid_HYCOM2.py
RUN pip install -e pyroms/pyroms
RUN pip install -e pyroms/pyroms_toolbox
RUN pip install -e pyroms/bathy_smoother

# install cdsapi for ERA5-ROMS
RUN git clone https://github.com/trondkr/ERA5-ROMS.git
RUN pip install cdsapi

# For interactive shell
RUN conda init bash
RUN echo "conda activate base" >> /home/$USERNAME/.bashrc

# Set the default command to launch a bash shell
CMD ["/bin/bash"]
```
Build the docker image:

`docker build -t pyroms .`

Unless otherwise specified, the time zone for all times is UTC.

## Meteorological forcing files
Using ERA5-ROMS is straightforward with not much modifications in the code. The following is a portion of the modified code in `ECMWF_query.py`:
```
self.use_era5 = True
self.start_year = 1998
self.end_year = 2009
self.project = "CIOFS"
self.area = "62/-158/56/-148"
# self.area = self.get_area_for_project(self.project)
self.skip_existing_files=True
self.resultsdir = "/mnt/vault/ciofs/input/ERA5/"
#self.resultsdir = "../{}/".format(self.project)
self.debug = False

self.extract_data_every_N_hours = True
self.time_units = "days since 1948-01-01 00:00:00"
self.optionals = True  # optional variables to extract depending on ROMS version (Rutgers or Kate)
self.ROMS_version = "Rutgers"  # "Rutgers" or "Kate" - the sea-ice component of Kates ROMS version uses downward
# shortwave and not net shortwave to account for albedo of ice.
```
An API key is required to retrieve ERA5 data. Create an account on [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/). On the user profile page find the UID and API Key. Create the following file:
```
$ cat ~/.cdsapirc
url: https://cds.climate.copernicus.eu/api/v2
key: <UID>:<API key>
```

The following command launches ERA5-ROMS in a docker container:
```
docker run -v /home/mpiuser/project-ciofs-hindcast/hindcast_input:/hindcast_input -v /mnt/vault/ciofs:/mnt/vault/ciofs pyroms python /hindcast_input/ERA5-ROMS/ECMWF_tools.py 
```
## Initial condition and open boundary condition files

Initial and open boundary conditions are derived from the HYCOM + NCODA Global 1/12 Analysis data products. `pyroms` provided example scripts to process HYCOM data, which we modified to fit our needs.

Modify and run these files to retrieve the appropriate HYCOM data subsets for subsequent processing:

* get_hycom_GLBy0.08_ssh.py
* get_hycom_GLBy0.08_temp.py
* get_hycom_GLBy0.08_salt.py
* get_hycom_GLBy0.08_u.py
* get_hycom_GLBy0.08_v.py

One initial condition file was created for 1998-01-01 00:00:00 when the hindcast simulation begins. This file was created by executing `make_ic_file.py`. 

The code to generate open boundary condition files is `make_bdry_files.py`. This generates the file `HYCOM_GLBv0.08_all_1998_001_000h_ic_CIOFS.nc`.

The interpolation functions shared by both scripts uses ESMF to perform interpolations between the HYCOM and ROMS grids.

## Tidal forcing file

The harmonic tides input file used by NOAA COOPS’ CIOFS model was provided to us. Although tidal harmonics are not time-dependent, ROMS need to be told what the reference time is. Following [(]this page](https://www.myroms.org/projects/src/ticket/896), a new variable needs to be added to the tidal input file. Such a variable was added to the tidal input file `nos.ciofs.roms.tides.20230201.t00z.nc` (zero_phase_date = 20230101.0000). The following python code performs such a modification:
```
import netCDF4 as nc
import numpy as np
import datetime

def add_tide_date(ncfile, tide_ref):
    """
    Adds zero phase date to existing tidal NetCDF file.

    Converted from https://github.com/jcwarner-usgs/COAWST/blob/master/Tools/mfiles/rutgers/forcing/add_tide_date.m
    %=========================================================================%
    %  Copyright (c) 2002-2020 The ROMS/TOMS Group                            %
    %    Licensed under a MIT/X style license                                 %
    %    See License_ROMS.txt                           Hernan G. Arango      %
    %=========================================================================%

    Parameters
    ----------
    ncfile : str
        Existing ROMS tidal NetCDF file name.
    tide_ref : np.datetime64
        Tide reference date.

    Returns
    -------
    None

    """
    # Inquire input NetCDF file.
    with nc.Dataset(ncfile, 'a') as dset:
        got_zero_phase_date = 'zero_phase_date' in dset.variables

        # If appropriate, define zero phase date variable.
        if not got_zero_phase_date:
            var = dset.createVariable('zero_phase_date', np.double)
            var.long_name = 'tide reference date for zero phase'
            var.units = 'days as %Y%m%d.%f'
            var.C_format = '%13.4f'
            var.FORTRAN_format = '(f13.4)'

            dayfrac = tide_ref.astype(int) - np.fix(tide_ref.astype(int))
            tidedate = round(float(tide_ref.astype(datetime.datetime).strftime('%Y%m%d')) + dayfrac, 4)
            var[:] = tidedate


ncfile = 'nos.ciofs.roms.tides.20230201.t00z.nc'
tide_ref = np.datetime64('2023-01-01')
add_tide_date(ncfile, tide_ref)
```

## ROMS configuration files

### Standard input file `axiom.ciofs.hindcast.*.in`

For the initial simulation we use the generated initial condition file by setting `ININAME = HYCOM_GLBv0.08_all_1998_001_000h_ic_CIOFS.nc`, set `NRREC` to 0. For subsequent restart runs:

* set `NRREC` back to -1;
* set `ININAME` to the restart file generated from the * previous run;
* change `DSTART` and `NSTEPS` accordingly.

Because we are performing a multi-decadal hindcast using harmonic tides as an open boundary condition, the nodal correction switch should be turned on in the `.in` file:
```
! If tide generating forces, set switch (T/F) to apply a 18.6-year lunar
! nodal correction to equilibrium tide constituents.

           Lnodal =  T
```
The ROMS time step `DT == 4.0d0` was remain unchanged from the COOPS version. We set the following parameters to output history files daily with hourly intervals, and restart files daily:
```
NRST == 21600
NHIS == 900     
NDEFHIS == 21600
```

### Variable metadata file varinfo.yaml

The following list shows the variables and attributes that require modification in varinfo.yaml to match those in the input forcing files. The corrected attributes for each variable are also provided below.
```
  - variable:       zeta_south
    time:           ocean_time
  - variable:       ubar_south
    time:           ocean_time
  - variable:       vbar_south
    time:           ocean_time
  - variable:       temp_south
    time:           ocean_time
  - variable:       salt_south
    time:           ocean_time
  - variable:       Pair
    units:          Pascal    
    scale:          0.01d0
  - variable:       Tair
    time:           Tair_time
  - variable:       *SWRAD
    time:           swrad_time
  - variable:       lwrad_down
    time:           lwrad_time
```
 