def driverWeb(url = 'https://www.google.com.br', openTab:str = 'Y'):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=r'../chromedriver_win32/chromedriver.exe')
    if openTab == 'Y':
        return driver.get(url), driver
    else:
        return driver

def environmentsVariables(variable:str) -> str:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv(variable)





