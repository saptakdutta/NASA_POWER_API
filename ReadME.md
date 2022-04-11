# GUI Access

GUI access for single point downloads is maintained separately here: https://power.larc.nasa.gov/data-access-viewer/

This tool exists as a back end interface that can help integrate the modeled data into your own application

# Setup

Download python and Anaconda as necessary. Use the provided environment.yml file with conda to create the virtual environment required to run this tool

# Testing Branch
This branch is the testing branch where experimental changes will be rolled out. Use at your own risk

## Data Storage
The project will be moving away from csv's as a data storage medium due to the fact that re-building the metadata is tedious and time consuming. Instead the project will focus on the HDF5 format which can be used to store local files and preserve metadata information. A legacy pathway will be enabled in the connector object dealing with downloads, so if users insist on CSV's, they can still use them.

# Overview

This repository contains an API that streamlines solar irradiation data downloads from NASA's POWER (Prediction Of Worldwide Energy Resources) program. 

# Inputs

The config file contains all the required parameters to run this tool. The main components of it are the locations.json file, parameters.csv and runtime.json

## locations.json

Locations.json consists of a json file with the locations where solar data is going to be extracted. The main JSON header is the city name, followed by a Yes/No parameter for use in the program and a latitude and longitude parameter. Ensure that the format is as follows:
```
"Ottawa":{
    "Use":"Yes",
    "Latitude": "X",
    "Longitude": "Y"
}
```
A hypothetically unlimited number of locations may be used in this tool, but do keep in mind that a larger locations.json file will require more time for data pull completion. I cannot guarantee that server timeouts will not be a problem on the POWER API side for very large data pulls.

## parameters.csv

This csv file contains pre defined parameters from the NASA POWER API. All parameters which are intended to be downloaded must be marked as "Yes" under the **Use** column. Parameters marked as "No" will simply be skipped for the runtime of the tool. More parameters can be found in the included hyperlinks to the POWER API. However, some parameters will not work wih the API call included in the library... modifications *may* have to be made to the baseline functions in order to get it to work with other params.

**Parameter(s)**: 
ALLSKY_SFC_SW_DWN       CERES SYN1deg All Sky Surface Shortwave Downward Irradiance (Wh/m^2) 
CLRSKY_SFC_SW_DWN       CERES SYN1deg Clear Sky Surface Shortwave Downward Irradiance (Wh/m^2) 
ALLSKY_KT               CERES SYN1deg All Sky Insolation Clearness Index (dimensionless) 
ALLSKY_SRF_ALB          CERES SYN1deg All Sky Surface Albedo (dimensionless) 
SZA                     CERES SYN1deg Solar Zenith Angle (Degrees) 
ALLSKY_SFC_PAR_TOT      CERES SYN1deg All Sky Surface PAR Total (W/m^2) 
ALLSKY_SFC_UV_INDEX     CERES SYN1deg All Sky Surface UV Index (dimensionless) 
ALLSKY_SFC_UVB          CERES SYN1deg All Sky Surface UVB Irradiance (W/m^2) 
ALLSKY_SFC_UVA          CERES SYN1deg All Sky Surface UVA Irradiance (W/m^2) 
CLRSKY_SFC_PAR_TOT      CERES SYN1deg Clear Sky Surface PAR Total (W/m^2) 
T2M                     MERRA-2 Temperature at 2 Meters (C) 
T2MDEW                  MERRA-2 Dew/Frost Point at 2 Meters (C) 
T2MWET                  MERRA-2 Wet Bulb Temperature at 2 Meters (C) 
QV2M                    MERRA-2 Specific Humidity at 2 Meters (g/kg) 
RH2M                    MERRA-2 Relative Humidity at 2 Meters (%) 
PRECTOTCORR             MERRA-2 Precipitation Corrected (mm/hour) 
PS                      MERRA-2 Surface Pressure (kPa) 
WS10M                   MERRA-2 Wind Speed at 10 Meters (m/s) 
WD10M                   MERRA-2 Wind Direction at 10 Meters (Degrees) 
WS50M                   MERRA-2 Wind Speed at 50 Meters (m/s) 
WD50M                   MERRA-2 Wind Direction at 50 Meters (Degrees) 

## runtime.json

This file contains important runtime variables for the tool. Timeformat can be either "UTC" or "LST". Communities should always be set to "RE", and the start and end dates ("sDate", "eDate") are up to the user to input

# Running the tool

Currently the tool is set up to run from a mac bash script. However, that should not be an issue for windows/linux users. As long as you can set up environment.yml, simply cd to the directory, and use conda to run *irradiance.py* once you've activated the required virtual environment. the tool was also developed in a hybrid notebook, so if using vscode or pycharm, you can default to that option. 

# More documentation

https://power.larc.nasa.gov/docs/services/api/temporal/hourly/

# Current Progress
- [x] Create a streamlined json/csv input interface for running the tool

- [x] Created a shell interface to run the tool so that jupyter or a python IDE is not necessary

- [x] Formatted the tool better so that all libraries are separated from main, all config options are isolated etc. 

- [x] More readable and modular code: created objects with discrete methods

- [x] integrate h5py storage medium as defaul (csv legacy pathway will be preserved)

- [x] proper logging through a logger module for easier bug detection

# Future Work
- [ ] batch file interface for windows users (currently supports macOS shell scripts)

- [ ] additional meteorological parameters such as temp, humidity, wind speed

