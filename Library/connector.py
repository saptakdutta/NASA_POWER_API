'''
Author: Saptak Dutta
Email: saptak.dutta@gmail.com

This script contains a list of functional programs that allows the user to pull 
simulated solar weather parameters from NASA's POWER API
'''
# Libraries
import numpy as np, json, requests as req, pandas as pd, h5py as hPy

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
    def cleanup(self, df, colname1, colname2):
        '''Enter in a time column and a value column to have one cleaned up as a datetime and the other as a float64'''
        df[colname1] = pd.to_datetime(df[colname1], format = '%Y%m%d%H')
        df[colname2] = df[colname2].astype(float)
        df[colname1] = df[colname1].dt.tz_localize('UTC').dt.tz_convert('EST')
        return df

class powerApiConnector:
    def __init__(self):
        pass
    #POWER SolarConnector
    def solarConnector(self, timeformat, params, community, longitude, latitude, sTime, eTime):
        url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?Time='+timeformat+'&parameters='+params+'&community='+community+'&longitude='+longitude+'&latitude='+latitude+'&start='+sTime+'&end='+eTime+'&format=JSON'
        solar = req.get(url)
        solar = solar.json()
        return solar

class weatherConnector:
    def __init_(self):
        pass
    #This object is meant to represent pulling non solar data from enviro can's historical weather database