#Libraries 
import sys as sys, json, pandas as pd
from pathlib import Path
from Library.connector import objOperators

class workPath:
    def __init__(self) :
        #define the path of the virtual environment and the tool
        pass
    def vEnvPath(self):
        v_EnvPath = sys.executable
        return (v_EnvPath)
    def toolPath(self):
        cwd = Path.cwd()
        tool_Path = cwd.__str__()
        return tool_Path

class weatherLocations:
    def __init__(self):
        pass
    def weatherLoc(self, fileName, filePath):
        # Load in the json file
        with open(filePath+'/Config/'+fileName) as f:
            locations_file = json.load(f)
            # Now only keep the locations which you want data for
            for location in list(locations_file):
                if (locations_file[location]['Use'] == 'No'):
                    locations_file.pop(location,None)
        return locations_file

class runTimePars:
    def __init__(self) -> None:
        pass
    def runTime(self, fileName, filePath):
        with open(filePath+'/Config/'+fileName) as f:
            runtime = json.load(f)
        # Available time formats: LST/UTC
        timeformat = runtime['timeformat']
        # Always use RE (renewable energy) for this purpose
        community = runtime['communities']
        # Start/end time in format: 'YYYYMMDD'
        sTime = runtime['sTime']
        eTime = runtime['eTime']
        return sTime, eTime, timeformat, community

class weatherParams:
    def __init__(self):
        pass
    def dlParams(self, fileName, filePath):
        pars = pd.read_csv(filePath+'/Config/'+fileName)
        # Only grab parameters we have selected as 'Yes'
        pars = pars[pars['Use'] == 'Yes']
        strTransform = objOperators()
        params = strTransform.listToString(s = pars["Parameter"].to_list())
        return params