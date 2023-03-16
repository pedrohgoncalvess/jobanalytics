import time


def validateScheduler():
    from configsDir.environmentConfiguration import driverWeb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    driver = driverWeb()
    driver.get('https://www.linkedin.com/home')
    driver.maximize_window()

    login = driver.find_element(By.XPATH,value='//*[@id="session_key"]')
    password = driver.find_element(By.XPATH,value='//*[@id="session_password"]')
    login.send_keys('pedro_gonsalves@outlook.com.br')
    password.send_keys('fodao002')
    enter = driver.find_element(By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')
    enter.click()
    print(driver.current_url)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3483369383&keywords=engenheiro%20de%20dados&refresh=true")

    time.sleep(1500)
validateScheduler()