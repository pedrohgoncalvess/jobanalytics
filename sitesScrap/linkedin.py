
def getJobLink(numberPage:int = 0) -> list:
    from configsDir.environmentConfiguration import driverWeb
    from configsDir.setConfig import getConfigs
    from configsDir.treatmentConfigs import treatmentLocation, treatmentRole
    from configsDir.colors import colors

    import time
    from selenium.webdriver.common.by import By
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords={treatmentRole()}&location={treatmentLocation(getConfigs())}&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum={str(numberPage)}'
    driver = driverWeb()
    driver.get(url)
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
    return links, url


def validationUrls() -> dict:
    from database.operations.validationOperation import validationUrlExist
    links, urlGetjob = getJobLink()
    linksValidated:list = []

    def validatesLinks(links:dict):
        validation = validationUrlExist()
        for link in links:
            linkValide = link.split("?")[0]
            if linkValide not in validation:
                linksValidated.append(link)
        return linksValidated

    validatesLinks(links)

    while len(linksValidated) <= 10:
        pageNum = 0
        pageNum += 1
        print(f'Comming to page number {str(pageNum)}')
        newLinks, __ = getJobLink(pageNum)
        validatesLinks(newLinks)

    print(f"Returning {str(len(linksValidated))} urls validated")
    return linksValidated


def scrapInfosJobs(links:list = validationUrls()) -> dict:
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from configsDir.colors import colors
    from configsDir.dataXpath import dataPaths
    from database.operations.insertOperations import insertJobsScrap, insertTextScrap,insertTopicsScrap

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()
    login = driver.find_element(by=By.XPATH,value='//*[@id="session_key"]')
    login.send_keys(environmentsVariables('loginLinkedin'))
    password = driver.find_element(by=By.XPATH,value='//*[@id="session_password"]')
    password.send_keys(environmentsVariables('passwordLinkedin'))
    enter = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form/button')
    enter.click()

    viewMore = dataPaths('viewMoreInfos')
    viewMoreKeys = list(viewMore.keys())

    infosXpath = dataPaths('infosXpathAlternative')
    infosKeys = list(infosXpath.keys())

    for link in links:
        driver.get(link)
        try:
            for vwkey in viewMoreKeys:
                try:
                    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,viewMore[vwkey]))).click()
                except:
                    print(f"{colors('red')}============Not found button for click============.")
            dictInfosVacancy:dict = {}
            dictInfosVacancy.update({'idurlJob': link.split("?")[0]})
            dictInfosVacancy.update({'urlJob':link})
            for infoKey in infosKeys:
                try:
                    if infoKey != 'content':
                        contentInfo = driver.find_element(by=By.XPATH,value=infosXpath[infoKey]).text
                        dictInfosVacancy.update({infoKey:contentInfo})
                    else:
                        content = driver.find_element(by=By.XPATH,value=infosXpath[infoKey])
                        vacancyText = content.text
                        dictInfosVacancy.update({'vacancyText':vacancyText})
                        topics = content.find_elements(by=By.CSS_SELECTOR, value='strong')
                        topicsList: list = []
                        if len(topics) > 0:
                            for topic in topics:
                                topicsList.append(topic.text)
                            dictInfosVacancy.update({'topicsList': topicsList})
                            insertTopicsScrap(topicsList,dictInfosVacancy['idurlJob'])
                            insertTextScrap(vacancyText,dictInfosVacancy['idurlJob'])
                except Exception as err:
                    print(f"{colors('red')}Unable to get content {infoKey} \n {err}")
            insertJobsScrap(dictInfosVacancy)
        except Exception as err:
            print(f'{colors("red")}Could not access the link {link}. \n {err}')
            time.sleep(5)
    driver.close()
    return dictInfosVacancy

if __name__ == "__main__":
    scrapInfosJobs()