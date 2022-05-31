# this file includes global functions and variable used

def printError(error_type, string):
    if error_type == 'WARNING':
        print('WARNING: ' + string)
    elif error_type == 'ERROR':
        print('ERROR: ' + string)
