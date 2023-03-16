
def getJobLink(numberPage:int = 0) -> list:
    from configsDir.environmentConfiguration import driverWeb
    from configsDir.setConfig import getConfigs
    from configsDir.treatmentConfigs import treatmentLocation, treatmentRole
    from configsDir.colors import colors
    from selenium.webdriver.common.by import By

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
    from database.operations.scrapJobSchema.validationOperation import validationUrlExist
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

    pageNum = 0
    while len(linksValidated) <= 10:
        pageNum += 1
        print(f'Comming to page number {str(pageNum)}')
        newLinks, __ = getJobLink(pageNum)
        validatesLinks(newLinks)

    print(f"Returning {str(len(linksValidated))} urls validated")
    return linksValidated


def scrapInfosJobs(links:list = validationUrls()) -> dict:
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from configsDir.colors import colors
    from database.operations.scrapJobSchema.insertOperations import insertJobsScrap, insertTextScrap,insertTopicsScrap
    from database.operations.schedulerSchema.scheduler import getCorrectPath

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    linksList = links
    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()
    login = driver.find_element(by=By.XPATH,value=getCorrectPath('username'))
    login.send_keys(environmentsVariables('loginLinkedin'))
    password = driver.find_element(by=By.XPATH,value=getCorrectPath('password'))
    password.send_keys(environmentsVariables('passwordLinkedin'))
    enter = driver.find_element(by=By.XPATH,value=getCorrectPath('button'))
    enter.click()

    viewMore = getCorrectPath('view_more')
    infosKeys = ['content','date_publish','candidates','vacancy_title','vacancy_experience','vacancy_org']
    dictInfosVacancy: dict = {}
    try:
     WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.XPATH, viewMore)))
    except:
        time.sleep(10)

    for link in linksList:
        print(driver.current_url)
        driver.get(link)
        try:
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="ember32"]'))).click()
        except:
            continue
        dictInfosVacancy.update({'vacancy_org':link.split('at-')[1].split('-')[0].capitalize()})
        dictInfosVacancy.update({'idurlJob': link.split("?")[0]})
        for infoKey in infosKeys:
            try:
                if infoKey != 'content':
                    contentInfo = driver.find_element(by=By.XPATH,value=getCorrectPath(infoKey)).text
                    dictInfosVacancy.update({infoKey:contentInfo})
                else:
                    content = driver.find_element(by=By.XPATH,value=getCorrectPath(infoKey))
                    vacancyText = content.text
                    topics = content.find_elements(by=By.CSS_SELECTOR, value='strong')
            except Exception as err:
                print(f"{colors('red')}Error in {infoKey}. {err}")
        insertJobsScrap(dictInfosVacancy)
        insertTextScrap(vacancyText, dictInfosVacancy['idurlJob'])
        topicsList: list = []
        if len(topics) > 0:
            for topic in topics:
                topicsList.append(topic.text)
            dictInfosVacancy.update({'topicsList': topicsList})
            insertTopicsScrap(topicsList, dictInfosVacancy['idurlJob'])
    driver.close()