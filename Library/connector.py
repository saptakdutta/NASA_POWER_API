'''
Author: Saptak Dutta
Email: saptak.dutta@gmail.com

This script contains a list of objects that allows the user to connect to 
simulated solar weather parameters from NASA's POWER API
'''
# Libraries
import requests as req, pandas as pd

# Functions
class objOperators:
    def __init__(self):
        pass
    #list to string
    def listToString(self, s):
        listToStr = ','.join(map(str, s))
        # return string
        return listToStr
    #Dataframe return
    def dfClean(self, df):
        '''Enter in a time column and a value column to have one cleaned up as a datetime and the other as a float64'''
        df = df.reset_index()
        df = df.rename({'index':'DateTime'}, axis =1)
        df['DateTime'] = pd.to_datetime(df['DateTime'], format = '%Y%m%d%H')
        df = df.set_index('DateTime')
        return df

class powerApiConnector:
    def __init__(self):
        pass
    #POWER Single Point Download Connector
    def powerSPConnector(self, timeformat, params, community, longitude, latitude, sTime, eTime):
        url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?Time='+timeformat+'&parameters='+params+'&community='+community+'&longitude='+longitude+'&latitude='+latitude+'&start='+sTime+'&end='+eTime+'&format=JSON'
        data = req.get(url)
        data = data.json()
        return data