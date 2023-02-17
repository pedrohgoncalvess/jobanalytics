from configs.setConfig import getConfigs
from configs.colors import colors

def treatmentLocation(dictConfigs:dict = getConfigs()):
    try:
        location = dictConfigs['location']
        location = location.replace('|', '')
        location = location.replace(' ','%2C%20')
    except:
        print(f"{colors('cyan')}The default location has been defined")
        location = 'brazil'
    return location

treatmentLocation()