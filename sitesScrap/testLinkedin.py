def testLogin():
    try:
        from configsDir.environmentConfiguration import driverWeb, environmentsVariables
        import time
        from selenium.webdriver.common.by import By
        from configsDir.colors import colors

        driver = driverWeb()
        driver.get('https://www.linkedin.com/home')
        driver.maximize_window()
        login = driver.find_element(by=By.XPATH,value='//*[@id="session_key"]')
        login.send_keys(environmentsVariables('loginLinkedin'))
        password = driver.find_element(by=By.XPATH,value='//*[@id="session_password"]')
        password.send_keys(environmentsVariables('passwordLinkedin'))
        enter = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button') #'//*[@id="main-content"]/section[1]/div/div/form/button' LAST BUTTON XPATH
        enter.click()
        print(f"{colors('green')}Login passed.")
    except:
        exit('Login has no passed.')


def testGetLink():
    from configsDir.environmentConfiguration import driverWeb
    from configsDir.setConfig import getConfigs
    from configsDir.colors import colors

    from selenium.webdriver.common.by import By
    infos = getConfigs()
    url = f'https://www.linkedin.com/jobs/search?keywords=desenvolvedor&location=Brazil&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=1'
    driver = driverWeb()
    driver.get(url)
    driver.maximize_window()
    listJobs = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[2]/ul')
    jobs = listJobs.find_elements(by=By.TAG_NAME, value='li')
    links: list = []
    for num, job in enumerate(jobs):
        if num + 1 < len(jobs):
            try:
                link = job.find_element(by=By.XPATH,value=f'//*[@id="main-content"]/section[2]/ul/li[{num + 1}]/div/a').get_attribute('href')
                links.append(link)
            except:
                print(f'{colors("cyan")}Could not access the link {link}')
    driver.close()
    print(f"{colors('green')}Get links passed.")
    return links[0]

def testScrapJob(link:str):
    from configsDir.environmentConfiguration import driverWeb
    from configsDir.dataXpath import dataPaths, viewMoreInfos
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from configsDir.colors import colors

    driver = driverWeb()
    driver.get(link)

    viewMore = viewMoreInfos()
    viewMoreKeys = list(viewMore.keys())

    infosXpathList = dataPaths()

    for vwkey in viewMoreKeys:
        try:
            WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH,viewMore[vwkey]))).click()
        except:
            pass
    dictInfosVacancy:dict = {}
    for infosXpath in infosXpathList:
        errors = 0
        sucess = 0
        print(infosXpath)
        infosKeys = list(infosXpath.keys())
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
                sucess += 1
                print(sucess)
                if sucess >= 4:
                    print(f"{colors('green')}Scrap jobs passed")
                    return infosXpath
            except Exception as err:
                print(f"{colors('red')}Unable to get content {infoKey}")
                errors += 1
                if errors >= 3:
                    print(f"{str(errors)} errors are detected")


if __name__ == '__main__':
    #testLogin()
    testScrapJob(testGetLink())

