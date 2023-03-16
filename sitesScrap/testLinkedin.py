import time


def pathsForTestScrap(type_info:str, site:str='linkedin') -> dict:
    from database.connection.connection import connection
    from sqlalchemy.sql import text

    engine, base, session = connection(messages='off')
    with engine.connect() as conn:
        query = text(f"""select paths.id,
       paths."path"
from scrap_scheduler.set_path as "set",
 scrap_scheduler.path_site as paths
 where 1=1
 and set.site_scrap = '{site}'
 and paths.type_info = '{type_info}'""")
        lines = conn.execute(query)
    results:dict = {}
    for line in lines:
        results.update({line.id:line.path})
    return results


def testLogin():
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from selenium.webdriver.common.by import By
    from configsDir.colors import colors
    from database.operations.schedulerSchema.scheduler import createSchedulerExec

    usernamePath = pathsForTestScrap('username')
    passwordPath = pathsForTestScrap('password')
    buttonLogin = pathsForTestScrap('button')

    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()
    for login in usernamePath.values():
        try:
            loginBox = driver.find_element(by=By.XPATH,value=login)
            loginBox.send_keys(environmentsVariables('loginLinkedin'))
            dicio = {'idPath':login}
            createSchedulerExec(dicio)
        except:
            pass
    for password in passwordPath.values():
        try:
            passwordBox = driver.find_element(by=By.XPATH,value=password)
            passwordBox.send_keys(environmentsVariables('passwordLinkedin'))
            dicio = {'idPath':password}
            createSchedulerExec(dicio)
        except:
            pass
    for button in buttonLogin.values():
        try:
            enter = driver.find_element(by=By.XPATH,value=button)
            enter.click()
            dicio = {'idPath': button}
            createSchedulerExec(dicio)
            driver.close()
        except:
            pass
    print(f"{colors('green')}Login passed.")


def testGetLink():

    from configsDir.environmentConfiguration import driverWeb
    from configsDir.setConfig import getConfigs
    from configsDir.colors import colors
    from database.operations.schedulerSchema.url_test import insertUrlTest

    from selenium.webdriver.common.by import By
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
    insertUrlTest(links[0].split("?")[0])
    print(f"{colors('green')}Get links passed.")


def testScrapJob():
    from configsDir.environmentConfiguration import driverWeb, environmentsVariables
    from selenium.webdriver.common.by import By
    from configsDir.colors import colors
    from database.operations.schedulerSchema.scheduler import createSchedulerExec

    usernamePath = pathsForTestScrap('username')
    passwordPath = pathsForTestScrap('password')
    buttonLogin = pathsForTestScrap('button')

    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()
    for login in usernamePath.values():
        try:
            loginBox = driver.find_element(by=By.XPATH, value=login)
            loginBox.send_keys(environmentsVariables('loginLinkedin'))
            dicio = {'idPath': login}
            createSchedulerExec(dicio)
        except:
            pass
    for password in passwordPath.values():
        try:
            passwordBox = driver.find_element(by=By.XPATH, value=password)
            passwordBox.send_keys(environmentsVariables('passwordLinkedin'))
            dicio = {'idPath': password}
            createSchedulerExec(dicio)
        except:
            pass
    for button in buttonLogin.values():
        try:
            enter = driver.find_element(by=By.XPATH, value=button)
            enter.click()
            dicio = {'idPath': button}
            createSchedulerExec(dicio)
        except:
            pass
    print(f"{colors('green')}Login passed.")

    print(driver.current_url)
    #from configsDir.environmentConfiguration import driverWeb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from configsDir.colors import colors
    from database.operations.schedulerSchema.url_test import getLinkUrlTest
    from database.operations.schedulerSchema.scheduler import createSchedulerExec

    contentsList = ['content','date_publish','candidates','vacancy_title','vacancy_experience','vacancy_org']

    link = getLinkUrlTest()
    driver = driverWeb()
    driver.get(link)

    viewMoreKeys = pathsForTestScrap('view_more')

    for vwkey in viewMoreKeys.values():
        try:
            WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH,vwkey))).click()
            createSchedulerExec({'idPath':vwkey})
        except:
            pass

    listAppend = []

    for infoKey in contentsList:
        pathsLinkedin = pathsForTestScrap(infoKey)
        for pathLink in pathsLinkedin.values():
            try:
                if infoKey != 'content':
                    text = driver.find_element(by=By.XPATH,value=pathLink).text
                    listAppend.append(text)
                    createSchedulerExec({'idPath':pathLink})
                else:
                    content = driver.find_element(by=By.XPATH,value=pathLink)
                    vacancyText = content.text
                    topics = content.find_elements(by=By.CSS_SELECTOR, value='strong')
                    listAppend.append(vacancyText)
                    listAppend.append(topics)
                    createSchedulerExec({'idPath':pathLink})
            except:
                pass
    print(f"{colors('cyan')}Finished job content scheduler")


def _mainFunction():
    from database.operations.schedulerSchema.scheduler import validateScheduler
    from configsDir.colors import colors
    if validateScheduler(stage='login') == None:
        testLogin()
        testGetLink()
        testScrapJob()
    else:
        print(f"{colors('green')}Scheduler has already been run")
