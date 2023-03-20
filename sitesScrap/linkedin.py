def scrapInfosJobs():
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from configsDir.colors import colors
    from database.operations.scrapJobSchema.jobs_operations import insertJobsScrap
    from database.operations.scrapJobSchema.jobs_text_operations import insertTextScrap
    from database.operations.scrapJobSchema.jobs_topics_operations import insertTopicsScrap
    from database.operations.schedulerSchema.scheduler_operations import getCorrectPath

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    linksDict = getLinksTopics()
    linksList = list(linksDict.keys())
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
        print(link)
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
                try:
                    topicsList.append(topic.text)
                except:
                    pass
            dictInfosVacancy.update({'topicsList': topicsList})
            insertTopicsScrap(topicsList, dictInfosVacancy['idurlJob'])
    driver.close()