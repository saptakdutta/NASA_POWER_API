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

class weatherDownloader:
    def __init__(self, format, filePath, locations, timeformat, start_time, end_time):
        self.dlFormat = format
        self.path = filePath
        self.locations = locations
        self.timeformat = timeformat
        self.sTime = start_time
        self.eTime = end_time
    def solarDownload(self, solarParams, community):
        for location in tqdm.tqdm(self.locations):
            solar = powerApiConnector().solarConnector(self.timeformat, solarParams, community, self.locations[location]['Longitude'], self.locations[location]['Latitude'], self.sTime, self.eTime)
            solar_irr = pd.DataFrame(solar['properties']['parameter'])
            solar_irr = objOperators().dfClean(solar_irr)
            if (self.dlFormat == 'CSV'):
                # Use this pathway if you insist... but you will have to rebuild ALL the metadata again...
                solar_irr.to_csv(self.path+'/Data/{}_Solar.csv'.format(location))
            else:
                #pathway to h5py data download
                solar_irr.to_hdf(self.path+'/Data/{}_Solar.h5'.format(location), '{}_Solar'.format(location))
        #For debugging       
        #return(solar_irr)
    def tempDownloader(self):
        #this is the downloader method for temperature downloads: future work (probably wet and dry bulb temp)
        pass