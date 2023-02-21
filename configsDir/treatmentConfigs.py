from configsDir.setConfig import getConfigs
from configsDir.colors import colors

def treatmentLocation(dictConfigs:dict = getConfigs()):
    try:
        location = dictConfigs['location']
        location = location.replace('|', '')
        location = location.replace(' ','%2C%20')
    except:
        print(f"{colors('cyan')}The default location has been defined")
        location = 'brazil'
    return location

def treatmentRole(dictConfigs:dict = getConfigs()):
    try:
        role = dictConfigs['role']
        role = role.replace(' ','%2C%20')
        return role
    except:
        print(f"{colors('red')}Please put the vacancy of interest in the configs file")
        exit()