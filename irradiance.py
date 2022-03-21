#%% Libraries
import pandas as pd, numpy as np, requests as req, json, tqdm
from pathlib import Path
from scipy.interpolate import interp1d, interp2d

#%% Set working path directory
cwd = Path.cwd()
path = cwd.__str__()

# Define Functions
# Function to convert list to str
def listToString(s):
    listToStr = ','.join(map(str, s))
    # return string
    return listToStr

#Grab the locations
locations_file = 'locations.json'
#load in the json file
with open(path+'/'+locations_file) as f:
  locations = json.load(f)
#Now only keep the locations which you want data for
for location in list(locations):
    if (locations[location]['Use'] == 'No'):
        locations.pop(location,None)

# Grab the required parameters
pars = pd.read_csv(path+'/parameters.csv')
pars = pars[pars['Use'] == 'Yes']
params = listToString(pars["Parameter"].to_list())

# Available time formats: LST/UTC
timeformat = 'UTC'
#Always use RE (renewable energy) for this purpose
community = 'RE'
# Start/end time in format: 'YYYYMMDD'
sTime = '20200101'
eTime = '20200705'

#%% API call for given location
for location in tqdm.tqdm(locations):
    url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?Time='+timeformat+'&parameters='+params+'&community='+community+'&longitude='+locations[location]['Longitude']+'&latitude='+locations[location]['Latitude']+'&start='+sTime+'&end='+eTime+'&format=JSON'
    solar = req.get(url)
    solar = solar.json()
    #Isolate only the required solar parameter
    data = solar['properties']['parameter']['ALLSKY_SFC_SW_DWN']
    solar_irr = pd.DataFrame({'Time':data.keys(),
                              'Solar Irradiation':data.values()})
    solar_irr['Time'] = pd.to_datetime(solar_irr['Time'], format = '%Y%m%d%H')
    solar_irr = solar_irr.set_index('Time').resample('15min').ffill()
    solar_irr['Solar Irradiation'] = solar_irr['Solar Irradiation'].astype(float)
    solar_irr = solar_irr.reset_index()
    solar_irr['Time'] = solar_irr['Time'].dt.tz_localize('UTC').dt.tz_convert('EST')
    solar_irr.to_csv(path+'/Data/{}_Solar.csv'.format(location), index=False)

# %%
