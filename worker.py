#%% Libraries
import pandas as pd, numpy as np, requests as req, json, tqdm, sys
from pathlib import Path
from Library.connector import objOperators, powerApiConnector
from Library.runtime import workPath, weatherLocations, runTimePars
from Library.downloader import solarDownloader

# Set working path directory
cwd = Path.cwd()
path = cwd.__str__()
# Identify correct environment 
print('The downloader is currently using the following venv: {} \n'.format(sys.executable))
print('The currently used path is {}. \n'.format(path))

# Grab the locations file
locations_file = 'locations.json'
# Load in the json file
with open(path+'/Config/'+locations_file) as f:
  locations = json.load(f)
# Now only keep the locations which you want data for
for location in list(locations):
    if (locations[location]['Use'] == 'No'):
        locations.pop(location,None)

# Grab Runtime parameters
runtime_file = 'runtime.json'
with open(path+'/Config/'+runtime_file) as f:
  runtime = json.load(f)
# Available time formats: LST/UTC
timeformat = runtime['timeformat']
# Always use RE (renewable energy) for this purpose
community = runtime['communities']
# Start/end time in format: 'YYYYMMDD'
sTime = runtime['sTime']
eTime = runtime['eTime']

#%% Grab the required parameters we want to download from POWER
parameters_file = 'parameters.csv'
pars = pd.read_csv(path+'/Config/'+parameters_file)
# Only grab parameters we have selected as 'Yes'
pars = pars[pars['Use'] == 'Yes']
strTransform = objOperators()
params = strTransform.listToString(s = pars["Parameter"].to_list())

#%% API call for given location
print('Downloading data: \n')
for location in tqdm.tqdm(locations):
  solar_data = powerApiConnector()
  solar = solar_data.solarConnector(timeformat, params, community, locations[location]['Longitude'], locations[location]['Latitude'], sTime, eTime)
  solar_irr = pd.DataFrame(solar['properties']['parameter'])
  solar_irr.to_csv(path+'/Data/{}_Solar.csv'.format(location))
# %%