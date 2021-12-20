#%% Libraries
import pandas as pd, numpy as np, requests as req, json

#%%Sample parameters
# Available time formats: LST/UTC
timeformat = 'LST'
# Change up the params as fit. Righ now we are only looking at solar params but you can also get temp, hum and wind
params = 'ALLSKY_SFC_SW_DWN,CLRSKY_SFC_SW_DWN,ALLSKY_SRF_ALB,SZA,ALLSKY_SFC_PAR_TOT,ALLSKY_KT,CLRSKY_SFC_PAR_TOT,ALLSKY_SFC_UVA,ALLSKY_SFC_UVB,ALLSKY_SFC_UV_INDEX'
#Always use RE (renewable energy) for this purpose
community = 'RE' 
#Obtain LAT/LON from google maps
location = {
    'latitude':'45.5017',
    'longitude':'-73.5673'
    }
# Start/end time in format: 'YYYYMMDD'
sTime = '20210101'
eTime = '20210331'

#%% API call for given lat/long
url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?Time='+timeformat+'&parameters='+params+'&community='+community+'&longitude='+location['longitude']+'&latitude='+location['latitude']+'&start='+sTime+'&end='+eTime+'&format=JSON'
solar = req.get(url)

solar = solar.json()
solar['properties']['parameter']['ALLSKY_SFC_SW_DWN']

# %%
