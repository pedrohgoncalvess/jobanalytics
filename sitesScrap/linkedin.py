from configs.environmentConfiguration import openSite
from configs.setConfig import getConfigs
from configs.treatmentConfigs import treatmentLocation

import time
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from sitesScrap.treatmentLinkedin import treatmentTopics

def searchJob():
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords=Desenvolvedor%20Python&location={treatmentLocation(getConfigs())}&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    site, driver = openSite(url)
    listJobs = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]')
    jobs = listJobs.find_elements_by_tag_name('li')
    for job in jobs:
        job.click()
        WebDriverWait(driver,20).until(ec.element_to_be_clickable((by.XPATH,'/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/button[1]'))).click()
        content = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]')
        htmlBody = content.text
        topics = content.find_elements_by_css_selector('strong')
        topicsList = list()
        for topic in topics:
            topicsList.append(topic.text)
        topicsList = treatmentTopics(topicsList)
        for n,namedTopic in enumerate(topicsList):
            nn = n+1
            if nn == len(topicsList):
                print(namedTopic)
                print(htmlBody.split(namedTopic)[1])
            else:
                print(namedTopic)
                print(htmlBody.split(namedTopic)[1].split(topicsList[nn])[1])
        time.sleep(100)
    time.sleep(500)



if __name__ == "__main__":
    searchJob()