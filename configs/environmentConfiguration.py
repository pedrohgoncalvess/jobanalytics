def openSite(endereco = 'https://www.google.com.br') :
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=r'/chromedriver_win32/chromedriver.exe')
    return driver.get(endereco), driver

def environmentsVariables(variable:str) -> str:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv(variable)





