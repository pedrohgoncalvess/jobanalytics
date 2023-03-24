def getLinksTopics():
    from configsDir.environmentConfiguration import driverWeb
    from database.operations.scrapJobSchema.job_standby_operations import listUrlStandBy,insertUrlForStandBy
    from database.operations.scrapJobSchema.midlevelOperations import validationUrlExist
    from database.connection.connection import connection

    import time
    from selenium.webdriver.common.by import By
    from database.operations.schedulerSchema.topic_search_operations import listTopicsForSearch

    _, _, session = connection()

    listJobsDBStandby = list(listUrlStandBy().keys())
    listJobsDBScraped = validationUrlExist()
    listJobsDB = [listJobsDBScraped.append(link) for link in listJobsDBStandby if link not in listJobsDBScraped]

    driver = driverWeb()
    driver.get('https://www.google.com')
    time.sleep(5000)


getLinksTopics()