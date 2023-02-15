import os

from selenium import webdriver

def openSite(endereco = 'https://www.google.com.br') :
    driver = webdriver.Chrome(executable_path=r'C:\Users\Pedro\Desktop\WorkSpace\Projetos\jobDataScraping\chromedriver_win32\chromedriver.exe')
    return driver.get(endereco), driver

def environmentsVariables(variable:str) -> str:
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv(variable)





