def driverWeb(url = 'https://www.google.com.br'):
    from selenium import webdriver
    from configsDir.colors import colors
    import os

    paths = ['.','..']
    for pathArch in paths:
        pathDriver = f"{pathArch}/chromedriver_win32/chromedriver.exe"
        if os.path.exists(pathDriver) == True:
            driver = webdriver.Chrome(executable_path=pathDriver)
            return driver
    print(f"{colors('red')}Not found chromedriver in {os.path.abspath('..')}")

def environmentsVariables(variable:str) -> str:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv(variable)





