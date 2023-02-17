import os
from configs.colors import colors


def getPath() -> str:
    import os
    path = os.path.abspath('..')
    archives = os.listdir('..')
    for arch in archives:
        if arch == 'config':
            path = path+'\config'
            return path
    print(f"{colors('red')}Not found archive 'configs' in {path} path")
    exit()


def getConfigs(currentPath = getPath()) -> dict:
    with open(currentPath) as file:
        configs = file.read()
        configs = configs.split('\n')
        preferences:dict = {}
        for config in configs:
            if len(config) == 0:
                continue
            preference = config.split('=')
            for r,prefer in enumerate(preference):
                preference[r] = prefer.rstrip().lstrip()
            temporaryDict = {preference[0]:preference[1]}
            preferences.update(temporaryDict)
        keys = list(preferences.keys())
        for key in keys:
            value = preferences[key]
            value = str(value)
            if value.find(',') != -1:
                value = value.split(',')
                preferences.update({key:value})
    return preferences
