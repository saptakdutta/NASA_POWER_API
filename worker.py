#%% Libraries
from Library.runtime import workPath, weatherLocations, runTimePars, weatherParams
from Library.downloader import weatherDownloader
from Library.logger import autoLogger

# Set working path directory
envPath = workPath().vEnvPath()
filePath = workPath().toolPath()
print(autoLogger(filePath).loggerDefine('ErrorLogs'))
# Identify correct environment 
print('The downloader is currently using the following venv: {} \n'.format(envPath))
print('The currently used path is {}. \n'.format(filePath))

# Grab the locations file
locations = weatherLocations().weatherLoc('locations.json',filePath)
autoLogger(filePath).processCompletion('locations')
# Grab runtime parameters
sTime, eTime, timeformat, community = runTimePars().runTime('runtime.json', filePath)
autoLogger(filePath).processCompletion('runtime params')
# Grab the required weather parameters we want to download from POWER
params = weatherParams().dlParams('parameters.csv',filePath)
autoLogger(filePath).processCompletion('solar_params')

#%% API call for given location
print('Downloading data: \n')
download = weatherDownloader('hdf5', filePath, locations, timeformat, sTime, eTime).powerDownload(params, community)
autoLogger(filePath).processCompletion('all downloads')

# %%
