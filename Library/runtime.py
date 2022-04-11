#Libraries 
import sys as sys, json
from pathlib import Path

class workPath:
    def __init__(self) :
        #define the path of the virtual environment and the tool
        v_EnvPath = sys.executable
        cwd = Path.cwd()
        tool_Path = cwd.__str__()
    def vEnvPath(self):
        return self.v_EnvPath
    def toolPath(self):
        return self.tool_Path

class weatherLocations:
    def __init__(self):
        pass
    def weatherLocations(self, fileName, filePath):
        locations_file = fileName
        # Load in the json file
        with open(filePath+'/Config/'+locations_file) as f:
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
        runtime_file = fileName
        with open(filePath+'/Config/'+runtime_file) as f:
            runtime = json.load(f)
        # Available time formats: LST/UTC
        timeformat = runtime['timeformat']
        # Always use RE (renewable energy) for this purpose
        community = runtime['communities']
        # Start/end time in format: 'YYYYMMDD'
        sTime = runtime['sTime']
        eTime = runtime['eTime']
        return sTime, eTime, timeformat, community