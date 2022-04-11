import tqdm, pandas as pd, h5py as hPy
from Library.connector import powerApiConnector

class solarDownloader:
    def __init__(self, format):
        self.dlFormat = format
    def solarDownload(self, path, locations, timeformat, params, community, sTime, eTime):
        for location in tqdm.tqdm(locations):
            solar_data = powerApiConnector()
            solar = solar_data.solarConnector(timeformat, params, community, locations[location]['Longitude'], locations[location]['Latitude'], sTime, eTime)
            if (self.dlFormat == 'CSV'):
                solar_irr = pd.DataFrame(solar['properties']['parameter'])
                solar_irr.to_csv(path+'/Data/{}_Solar.csv'.format(location))
            else:
                #pathway to h5py data download
                break