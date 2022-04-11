# Libraries
import pandas as pd, tqdm
from Library.connector import objOperators
from Library.runtime import workPath, weatherLocations, runTimePars
from Library.downloader import solarDownloader

#%% Set working path directory
envPath = workPath().vEnvPath()
filePath = workPath().toolPath()
# Identify correct environment 
print('The downloader is currently using the following venv: {} \n'.format(envPath))
print('The currently used path is {}. \n'.format(filePath))

# Grab the locations file
locations = weatherLocations().weatherLoc('locations.json',filePath)
# Grab Runtime parameters
sTime, eTime, timeformat, community = runTimePars().runTime('runtime.json', filePath)
# Grab the required weather parameters we want to download from POWER
parameters_file = 'parameters.csv'
pars = pd.read_csv(filePath+'/Config/'+parameters_file)
# Only grab parameters we have selected as 'Yes'
pars = pars[pars['Use'] == 'Yes']
strTransform = objOperators()
params = strTransform.listToString(s = pars["Parameter"].to_list())

# API call for given location
print('Downloading data: \n')
download = solarDownloader('CSV').solarDownload(filePath,locations, timeformat, params, community, sTime, eTime)
