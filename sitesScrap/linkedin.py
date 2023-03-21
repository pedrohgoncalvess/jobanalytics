def getLinksTopics():
    from configsDir.environmentConfiguration import driverWeb
    from database.operations.scrapJobSchema.job_standby_operations import listUrlStandBy,insertUrlForStandBy

    import time
    from selenium.webdriver.common.by import By
    from database.operations.schedulerSchema.topic_search_operations import listTopicsForSearch

    listJobsDB = list(listUrlStandBy().keys())

    driver = driverWeb()
    driver.get('https://www.google.com')
    driver.maximize_window()
    dictTopics:dict = {}

    seniority = ['junior','pleno','senior']
    topicsKeys = list(listTopicsForSearch().keys())
    topicsForSearch:list = []

    for topic in topicsKeys:
        if listTopicsForSearch()[topic] == 'position':
            for stage in seniority:
                newTopic = topic + " " + stage
                topicsForSearch.append(newTopic)
        else:
            newTopicStack = 'desenvolvedor ' + topic
            topicsForSearch.append(newTopicStack)


    for topic in topicsForSearch:
        current_url = driver.current_url
        url = f'https://www.linkedin.com/jobs/search?keywords={topic.replace(" ","%2C%20")}&location=Brazil&search-bar_search-submit&position=1&pageNum=0'
        driver.get(url)
        time.sleep(1)
        try:
            listJobs = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/main/section[2]/ul')
            jobs = listJobs.find_elements(by=By.TAG_NAME, value='li')
        except:
            pass
        for num,job in enumerate(jobs):
            try:
                xpath = f'/html/body/div[1]/div/main/section[2]/ul/li[{num+1}]/div/a'
                link = job.find_element(by=By.XPATH,value=xpath).get_attribute('href')
                linkCompare = link.split("?")[0]
                if linkCompare not in listJobsDB:
                    print(linkCompare)
                    dictTopics.update({linkCompare:topic})
            except:
                pass
    driver.close()
    insertUrlForStandBy(dictTopics)

def scrapInfosJobs():
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from configsDir.colors import colors
    from database.operations.scrapJobSchema.jobs_operations import insertJobsScrap
    from database.operations.scrapJobSchema.jobs_text_operations import insertTextScrap
    from database.operations.scrapJobSchema.jobs_topics_operations import insertTopicsScrap
    from database.operations.schedulerSchema.scheduler_operations import getCorrectPath
    from database.operations.scrapJobSchema.job_standby_operations import listUrlStandBy

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    linksDict = listUrlStandBy()
    linksList = list(linksDict.keys())
    dictContentPaths = getCorrectPath()


    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()
    login = driver.find_element(by=By.XPATH,value=dictContentPaths['username'])
    login.send_keys(environmentsVariables('loginLinkedin'))
    password = driver.find_element(by=By.XPATH,value=dictContentPaths['password'])
    password.send_keys(environmentsVariables('passwordLinkedin'))
    enter = driver.find_element(by=By.XPATH,value=dictContentPaths['button'])
    enter.click()

    viewMore = dictContentPaths['view_more']
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
        dictInfosVacancy.update({'researched_topic': linksDict[link]})
        dictInfosVacancy.update({'vacancy_org':link.split('at-')[1].split('-')[0].capitalize()})
        dictInfosVacancy.update({'idurlJob': link.split("?")[0]})
        for infoKey in infosKeys:
            try:
                if infoKey != 'content':
                    contentInfo = driver.find_element(by=By.XPATH,value=dictContentPaths[infoKey]).text
                    dictInfosVacancy.update({infoKey:contentInfo})
                else:
                    content = driver.find_element(by=By.XPATH,value=dictContentPaths[infoKey])
                    vacancyText = content.text
                    topics = content.find_elements(by=By.CSS_SELECTOR, value='strong')
            except:
                print(f"{colors('red')}Error in {infoKey}.")
        insertJobsScrap(dictInfosVacancy)
        insertTextScrap(vacancyText, dictInfosVacancy['idurlJob'])
        topicsList: list = []
        if len(topics) > 0:
            for topic in topics:
                try:
                    topicsList.append(topic.text)
                except:
                    pass
            dictInfosVacancy.update({'topicsList': topicsList})
            insertTopicsScrap(topicsList, dictInfosVacancy['idurlJob'])
    driver.close()