def getLinksIndeed():
    from configsDir.environmentConfiguration import driverWeb
    from selenium.webdriver.common.by import By
    from database.operations.scrapJobSchema.job_standby_operations import insertBulkLinks
    from database.operations.scrapJobSchema.job_standby_operations import listUrlStandBy

    urlsScraped:dict = {}
    urlsDict = generateUrls()
    urls = list(urlsDict.keys())

    linksDb = list(listUrlStandBy(siteStandby='indeed').keys())

    driver = driverWeb("https://www.google.com")
    count = 0
    for url in urls:
        _ = driver.current_url
        driver.get(url)
        try:
            linksJobsXpath = driver.find_element(By.XPATH,'/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul')
            linksJobs = linksJobsXpath.find_elements(By.CSS_SELECTOR,"li")
            driver.execute_script("window.scrollTo(0, 5000)")
        except:
            continue

        for num,link in enumerate(linksJobs):
            try:
                href = link.find_element(By.XPATH,f'/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[{str(num+1)}]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a')
                linkScraped = href.get_attribute("href")
                if linkScraped not in urlsScraped:
                    if linkScraped not in linksDb:
                        urlsScraped.update({linkScraped:urlsDict[url]})
                        count += 1
            except:
                pass

    insertBulkLinks(urlsScraped,"indeed")
    print(f"Numero de vagas scrapadas: {count}")

def generateTopics() -> list:
    from database.operations.scrapJobSchema.topic_search_operations import listTopicsForSearch

    dictTopics = listTopicsForSearch()
    listTopics = list(dictTopics.keys())

    topicsForSearch:list = []

    seniority = ['junior', 'pleno', 'senior']
    for topic in listTopics:
        if dictTopics[topic] == 'position':
            for stage in seniority:
                newTopic = topic + " " + stage
                topicsForSearch.append(newTopic)
        else:
            newTopicStack = 'desenvolvedor ' + topic
            topicsForSearch.append(newTopicStack)

    return topicsForSearch

def generateUrls() -> dict:
    topicsForSearch:list = generateTopics()
    listPages = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    urls: dict = {}

    for searchTp in topicsForSearch:
        linkZ = f"https://br.indeed.com/jobs?q={searchTp.replace(' ','+')}"
        if linkZ not in urls:
            urls.update({linkZ:searchTp})
        for page in listPages:
            url = f"https://br.indeed.com/jobs?q={searchTp.replace(' ','+')}&start={page}"
            urls.update({url:searchTp})

    return urls

getLinksIndeed()