import os
from datetime import datetime

# this file includes global functions and variable used

def printError(error_type, string):
    if error_type == 'WARNING':
        log("warning", string)
        print('WARNING: ' + string)
    elif error_type == 'ERROR':
        log("error", string)
        print('ERROR: ' + string)

def log(error_type, string):
    open('log', 'a').write("{0}\t{1}\t{2}\t{3}".format(
        os.getlogin(),
        str(datetime.now()),
        error_type,
        string
        ))
