# Libraries
from Library.runtime import workPath, weatherLocations, runTimePars, weatherParams
from Library.downloader import solarDownloader

#%% Set working path directory
envPath = workPath().vEnvPath()
filePath = workPath().toolPath()
# Identify correct environment 
print('The downloader is currently using the following venv: {} \n'.format(envPath))
print('The currently used path is {}. \n'.format(filePath))

# Grab the locations file
locations = weatherLocations().weatherLoc('locations.json',filePath)
# Grab runtime parameters
sTime, eTime, timeformat, community = runTimePars().runTime('runtime.json', filePath)
# Grab the required weather parameters we want to download from POWER
params = weatherParams().dlParams('parameters.csv',filePath)

# API call for given location
print('Downloading data: \n')
download = solarDownloader('CSV').solarDownload(filePath,locations, timeformat, params, community, sTime, eTime)
