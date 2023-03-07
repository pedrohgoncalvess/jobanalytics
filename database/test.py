urls = ['https://br.linkedin.com/jobs/view/desenvolvedor-front-end-jr-at-sumus-3475143795?refId=8f8%2FrE%2Ff4X9cyyxhuO3GTA%3D%3D&trackingId=q3ktBHSyTXL8WkypglKPiQ%3D%3D&position=1&pageNum=0&trk=public_jobs_jserp-result_search-card']

from configsDir.environmentConfiguration import driverWeb, environmentsVariables
from configsDir.colors import colors
from configsDir.dataXpath import dataPaths

from database.operations.insertOperations import insertTopicsScrap, insertTextScrap
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def testTopicsInsert():
    driver = driverWeb()
    viewMore = dataPaths('viewMoreInfos')
    viewMoreKeys = list(viewMore.keys())
    for link in urls:
        driver.get(link)
        for vwkey in viewMoreKeys:
            try:
                WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, viewMore[vwkey]))).click()
            except:
                print("Tentei paizao")
        # content = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div')
        topics = driver.find_elements(by=By.CSS_SELECTOR, value='strong')
        topicList:list = []
        for topic in topics:
            topic = topic.text
            if len(topic) > 2:
                topicList.append(topic)

        print(topicList)

        if len(topicList) >= 1:
            insertTopicsScrap(topicList,link.split('?')[0])


def testTextBodyInsert():
    driver = driverWeb()
    viewMore = dataPaths('viewMoreInfos')
    viewMoreKeys = list(viewMore.keys())
    for link in urls:
        driver.get(link)
        for vwkey in viewMoreKeys:
            try:
                WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, viewMore[vwkey]))).click()
            except:
                print("Tentei paizao")
        content = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div')
        text = content.text[0:14999]
        insertTextScrap(text,link.split('?')[0])
if __name__ == '__main__':
    testTextBodyInsert()