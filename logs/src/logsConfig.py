from types import FunctionType

def readConfigs():
    import os
    from os import path
    pathDir = os.path.abspath('jobDataScraping')
    pathDir = pathDir.split("\\src")[0]+'\\logsSettings'
    print(pathDir)
    with open(pathDir) as config:
        listConfigs:list = []
        configs = config.readlines()
        for line in configs:
            line = line.replace('\n','')
            line = line.split("=")
            listConfigs.append(line)
        for list in listConfigs:
            variavel = list[0]
            sizeList = len(list)
            if sizeList > 2:
                pass


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
