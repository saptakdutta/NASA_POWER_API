'''
Author: Saptak Dutta
Email: saptak.dutta@gmail.com

This script contains a list of objects that allows the user to download 
simulated solar weather parameters from NASA's POWER API
'''
#Libraries
from time import time
import tqdm, pandas as pd
from Library.connector import powerApiConnector, objOperators
from Library.logger import autoLogger

class weatherDownloader:
    def __init__(self, format, filePath, locations, timeformat, start_time, end_time):
        self.dlFormat = format
        self.path = filePath
        self.locations = locations
        self.timeformat = timeformat
        self.sTime = start_time
        self.eTime = end_time
    def powerDownload(self, apiParams, community):
        for location in tqdm.tqdm(self.locations):
            solar = powerApiConnector().powerSPConnector(self.timeformat, apiParams, community, self.locations[location]['Longitude'], self.locations[location]['Latitude'], self.sTime, self.eTime)
            data = pd.DataFrame(solar['properties']['parameter'])
            data = objOperators().dfClean(data)
            if (self.dlFormat == 'CSV'):
                # Use this pathway if you insist... but you will have to rebuild ALL the metadata again...
                data.to_csv(self.path+'/Data/{}_POWER.csv'.format(location))
            else:
                #pathway to h5py data download
                data.to_hdf(self.path+'/Data/{}_POWER.h5'.format(location), '{}_POWER'.format(location))
            #Log the completion
            autoLogger(self.path).processCompletion('{}_POWER'.format(location))
        #For debugging       
        #return(data)