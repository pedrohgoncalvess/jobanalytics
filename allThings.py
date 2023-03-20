def getLinksTopics():
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from configsDir.colors import colors
    from database.operations.schedulerSchema.scheduler import getCorrectPath

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from database.operations.schedulerSchema.topic_search import listTopicsForSearch

    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()
    login = driver.find_element(by=By.XPATH,value=getCorrectPath('username'))
    login.send_keys(environmentsVariables('loginLinkedin'))
    password = driver.find_element(by=By.XPATH,value=getCorrectPath('password'))
    password.send_keys(environmentsVariables('passwordLinkedin'))
    enter = driver.find_element(by=By.XPATH,value=getCorrectPath('button'))
    enter.click()

    try:
     WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="ember32"]')))
    except:
        time.sleep(10)
    dictTopics:dict = {}
    number = [4,5]
    seniority = ['junior','pleno','senior']

    for stage in seniority:
        for topic in listTopicsForSearch():
            current_url = driver.current_url
            topic = topic + " " + stage
            url = f'https://www.linkedin.com/jobs/search?keywords={topic.replace(" ","%2C%20")}&search-bar_search-submit&position=1&pageNum=0'
            driver.get(url)
            driver.maximize_window()
            try:
                listJobs = driver.find_element(by=By.XPATH,value='//*[@id="main"]/div/section[1]/div/ul')
                jobs = listJobs.find_elements(by=By.TAG_NAME, value='li')
            except:
                continue
            for num,job in enumerate(jobs):
                for numb in number:
                    try:
                        if num >= 10:
                            xpath = f'/html/body/div[{str(numb)}]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{str(num + 1)}]/div/div[1]/div/div[2]/div[1]/a'
                            link = job.find_element(by=By.XPATH, value=xpath).get_attribute('href')
                            dictTopics.update({link: topic})
                        else:
                            xpath = f'/html/body/div[{str(numb)}]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{str(num+1)}]/div/div[1]/div[1]/div[2]/div[1]/a'
                            link = job.find_element(by=By.XPATH,value=xpath).get_attribute('href')
                            dictTopics.update({link:topic})
                    except:
                        pass
    driver.close()
    return dictTopics

lista = getLinksTopics()
listanova = []
for link in lista:
    if link not in listanova:
        listanova.append(link)
print(f"Quantidade de links scrapados foi de {len(listanova)}") #215 no primeiro scrap