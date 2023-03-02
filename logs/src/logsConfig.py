from types import FunctionType

def readConfigs():
    import os
    from os import path
    pathDir = os.path.abspath('..')
    print(pathDir)
    with open(pathDir) as config:
        configs = config.readlines()
        configs = configs.split('\n')
        print(configs)


def createDirs(func: FunctionType) -> FunctionType:
    import os
    from os import path
    pathDir = os.path.abspath('jobDataScraping/logs')
    dirs = ['scrap','database']
    for dir in dirs:
        dir = pathDir+'/'+dir
        check = path.exists(dir)
        if check == False:
            os.mkdir(dir)

    def execFunction():
        func()
    return execFunction


if __name__ == '__main__':
    readConfigs()
