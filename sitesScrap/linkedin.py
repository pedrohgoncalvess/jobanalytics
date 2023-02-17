from configs.environmentConfiguration import driverWeb,environmentsVariables
from configs.setConfig import getConfigs
from configs.treatmentConfigs import treatmentLocation,treatmentRole
from sitesScrap.treatmentLinkedin import treatmentTopics
from configs.colors import colors

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def getJobLink() -> list:
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords={treatmentRole()}&location={treatmentLocation(getConfigs())}&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    site, driver = driverWeb(url=url)
    driver.maximize_window()
    listJobs = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[2]/ul')
    jobs = listJobs.find_elements(by=By.TAG_NAME, value='li')
    links:list = []
    for num,job in enumerate(jobs):
        if num+1 < len(jobs):
            try:
                link = job.find_element(by=By.XPATH, value=f'//*[@id="main-content"]/section[2]/ul/li[{num+1}]/div/a').get_attribute('href')
                links.append(link)
            except:
                print(f'{colors("cyan")}Could not access the link {link}')
    driver.close()
    return links


def scrapInfosJobs(links:list = getJobLink()):

    site, driver = driverWeb(url='https://www.linkedin.com/home')
    login = driver.find_element(by=By.XPATH,value='//*[@id="session_key"]')
    login.send_keys(environmentsVariables('loginLinkedin'))
    password = driver.find_element(by=By.XPATH,value='//*[@id="session_password"]')
    password.send_keys(environmentsVariables('passwordLinkedin'))
    enter = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form/button')
    enter.click()

    for link in links:
        driver.execute_script('window.open('');')
        driver.maximize_window()
        #driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        print(link.split('/view/')[1].split('-at')[0])
        try:
            vacancyTitle = link.split('/view/')[1].split('-at')[0]
            vacancyOrg = link.split('-at')[1].split('-')[1]
            buttonShowMore = driver.find_element(by=By.XPATH,value='//*[@id="ember32"]')
            content = driver.find_element(by=By.XPATH,value='//*[@id="job-details"]')
            htmlBody = content.text
            topics = content.find_elements(by=By.CSS_SELECTOR, value='strong')
        except Exception as err:
            print(f'{colors("red")}Could not access the link {link}. \n {err}')
            time.sleep(55)
        #driver.close()
        #driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)


def test():
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords={treatmentRole()}&location={treatmentLocation(getConfigs())}&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    site, driver = driverWeb(url=url)
    driver.maximize_window()
    time.sleep(500)
    driver.close()

if __name__ == "__main__":
    #test()
    scrapInfosJobs()