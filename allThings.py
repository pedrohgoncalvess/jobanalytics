import time


def validateScheduler():
    from configsDir.environmentConfiguration import driverWeb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    driver = driverWeb()
    driver.get('https://br.linkedin.com/jobs/view/analista-de-dados-s%C3%A3o-paulo-at-algar-telecom-3521161493?refId=x6dSzQfJ8Bg2uOWYEh5QtA%3D%3D&trackingId=%2F4lqqJUJMd6RdBR%2BvzLAyQ%3D%3D&position=4&pageNum=0&trk=public_jobs_jserp-result_search-card')
    driver.maximize_window()

    # login = driver.find_element(By.XPATH,value='//*[@id="session_key"]')
    # password = driver.find_element(By.XPATH,value='//*[@id="session_password"]')
    # login.send_keys('pedro_gonsalves@outlook.com.br')
    # password.send_keys('fodao002')
    # enter = driver.find_element(By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')
    # enter.click()
    time.sleep(15000)

validateScheduler()