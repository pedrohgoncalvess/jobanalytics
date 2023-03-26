def getLinksTopics():
    from configsDir.environmentConfiguration import driverWeb
    from database.operations.scrapJobSchema.job_standby_operations import listUrlStandBy,insertUrlForStandBy
    from database.operations.scrapJobSchema.midlevelOperations import validationUrlExist
    from database.connection.connection import connection

    import time
    from selenium.webdriver.common.by import By
    from database.operations.scrapJobSchema.topic_search_operations import listTopicsForSearch

    _, _, session = connection()

    listJobsDBStandby = list(listUrlStandBy().keys())
    listJobsDBScraped = validationUrlExist()
    listJobsDB = [listJobsDBScraped.append(link) for link in listJobsDBStandby if link not in listJobsDBScraped]

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
                else:
                    print("This link exist in DB")
            except:
                pass
    driver.close()
    insertUrlForStandBy(dictTopics,'linkedin',session)