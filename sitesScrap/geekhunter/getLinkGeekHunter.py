def getLinkGeek():
    from configsDir.environmentConfiguration import driverWeb
    import time
    from selenium.webdriver.common.by import By
    from database.connection.connection import connection
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from database.operations.scrapJobSchema.job_standby_operations import insertUrlForStandBy

    engine, base, session = connection()

    driver = driverWeb()
    url = 'https://www.geekhunter.com.br/vagas?utmSource=direct&utmMedium=%28none%29&utmCampaign='
    driver.get(url)

    dictVacancies = {}
    for i in (range(500)):

        divVacancies = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/section')
        vacancies = divVacancies.find_elements(By.TAG_NAME, 'div')
        for vacancy in vacancies:
            link = vacancy.get_attribute("href")
            if link != None:
                dictVacancies.update({f"https://www.geekhunter.com.br{link}": "geek hunter"})
        try:
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div/div/section/div/div[12]/div/button[11]/div').click()
            WebDriverWait(driver, 15).until(
                ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[4]')))
        except:
            time.sleep(2)
    insertUrlForStandBy(dictVacancies, "geekhunter", session)


getLinkGeek()