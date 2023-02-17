from configs.environmentConfiguration import openSite
from configs.setConfig import getConfigs
from configs.treatmentConfigs import treatmentLocation,treatmentRole
from sitesScrap.treatmentLinkedin import treatmentTopics

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def searchJob():
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords={treatmentRole()}&location={treatmentLocation(getConfigs())}&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    site, driver = openSite(url)
    driver.maximize_window()
    listJobs = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]')
    jobs = listJobs.find_elements(by=By.TAG_NAME,value='li')
    for job in jobs:
        divHref = job.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[2]/ul/li[1]/div/a')
        print(divHref.get_attribute('href'))
        job.click()
        WebDriverWait(driver,20).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/button[1]'))).click()
        content = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]')
        htmlBody = content.text
        topics = content.find_elements(by=By.CSS_SELECTOR,value='strong')
        topicsList = list()
        for topic in topics:
            topicsList.append(topic.text)
        if len(topicsList) == 0:
            htmlBody
        topicsList = treatmentTopics(topicsList)
        for n,namedTopic in enumerate(topicsList):
            nn = n+1
            if nn == len(topicsList):
                print(namedTopic)
                print(htmlBody.split(namedTopic)[1])
            else:
                print(namedTopic)
                print(htmlBody.split(namedTopic)[1].split(topicsList[nn])[1])
        time.sleep(30)
    time.sleep(500)


def getJobLink() -> list:
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords={treatmentRole()}&location={treatmentLocation(getConfigs())}&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    site, driver = openSite(url)
    driver.maximize_window()
    listJobs = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[2]')
    jobs = listJobs.find_elements(by=By.TAG_NAME, value='li')
    links:list = []
    for job in jobs:
        link = job.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[2]/ul/li[1]/div/a').get_attribute('href')
        links.append(link)
    driver.close()
    return links


def scrapInfosJobs(links:list = getJobLink()):
    site, driver = openSite()
    print(links)
    for link in links:
        print(link)
        driver.execute_script('window.open('');')
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        content = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div')
        htmlBody = content.text
        topics = content.find_elements(by=By.CSS_SELECTOR, value='strong')
        print(topics,htmlBody)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(10)


if __name__ == "__main__":
    scrapInfosJobs()