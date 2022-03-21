#%% Libraries
import pandas as pd, numpy as np, requests as req, json, tqdm
from pathlib import Path
from scipy.interpolate import interp1d, interp2d
from ConnLib.connector import cleanup, listToString, connector

#%% Set working path directory
cwd = Path.cwd()
path = cwd.__str__()

#Grab the locations
locations_file = 'locations.json'
#load in the json file
with open(path+'/Config/'+locations_file) as f:
  locations = json.load(f)
#Now only keep the locations which you want data for
for location in list(locations):
    if (locations[location]['Use'] == 'No'):
        locations.pop(location,None)

# Grab the required parameters
parameters_file = 'parameters.csv'
pars = pd.read_csv(path+'/Config/'+parameters_file)
pars = pars[pars['Use'] == 'Yes']
params = listToString(pars["Parameter"].to_list())

# Available time formats: LST/UTC
timeformat = 'UTC'
#Always use RE (renewable energy) for this purpose
community = 'RE'
# Start/end time in format: 'YYYYMMDD'
sTime = '20200101'
eTime = '20200201'

#%% API call for given location
for location in tqdm.tqdm(locations):
    solar = connector(timeformat, params, community, locations[location]['Longitude'], locations[location]['Latitude'], sTime, eTime)
    #Isolate only the required solar parameter
    data = solar['properties']['parameter']['ALLSKY_SFC_SW_DWN']
    solar_irr = pd.DataFrame({'Time':data.keys(),
                              'Solar Irradiation':data.values()})
    cleanup(solar_irr,'Time','Solar Irradiation')
    solar_irr.to_csv(path+'/Data/{}_Solar.csv'.format(location), index=False)

# %%
