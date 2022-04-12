'''
Author: Saptak Dutta
Email: saptak.dutta@gmail.com

This script contains a list of objects that allows for the logging
of errors and mistakes during the runtime of the tool. Work TBD
'''
#Libraries
import logging
from datetime import datetime

class autoLogger:
    def __init__(self, path):
        self.path = path
    def loggerDefine(self, logFileName):
        logging.basicConfig(filename=self.path+'/Logs/{}.log'.format(logFileName), level=logging.DEBUG)
        logging.debug('Logging activated at: {}'.format(datetime.now()))
        return ('\n Logger activated...')
    def processCompletion(self, functionName):
        logging.debug('Completed {} at {}'.format(functionName, datetime.now()))
    def warning(self, warnText):
        logging.warning('Possibe exectution warning: {}'.format(warnText))