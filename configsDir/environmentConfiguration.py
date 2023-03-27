def driverWeb():
    from selenium import webdriver
    from configsDir.colors import colors
    import os

    try:
        pathDriver = environmentsVariables("pathdriver")
        driver = webdriver.Chrome(executable_path=pathDriver)
        return driver
    except:
        print(f"{colors('red')}Not found chromedriver in {os.path.abspath('..')}")
        exit()

def environmentsVariables(variable:str) -> str:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv(variable)