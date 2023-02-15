from environmentConfiguration import openSite,environmentsVariables
from setConfig import getConfigs,getPath
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def searchJob():
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords=Desenvolvedor%20Python&location=S%C3%A3o%20Paulo%2C%20S%C3%A3o%20Paulo%2C%20Brasil&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    site, driver = openSite("https://www.linkedin.com/jobs/search/?currentJobId=3468727023&keywords=desenvolvedor%20python")
    site
    listJobs = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]')
    jobs = listJobs.find_elements_by_tag_name('li')
    for job in jobs:
        job.click()
        WebDriverWait(driver,20).until(ec.element_to_be_clickable((by.XPATH,'/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/button[1]'))).click()
        content = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]')
        print(content.text)
        time.sleep(20)
    time.sleep(500)






if __name__ == "__main__":
    searchJob()