def getPath() -> str:
    import pathlib
    currentPath = pathlib.Path(__file__).parent.resolve()
    currentPath = str(currentPath)+"\config"
    return currentPath


def getConfigs(currentPath = getPath()) -> dict:
    with open(currentPath) as file:
        configs = file.read()
        configs = configs.split('\n')
        preferences:dict = {}
        for config in configs:
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

getConfigs(getPath())


