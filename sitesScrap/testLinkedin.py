def testLogin():
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

if __name__ == '__main__':
    testLogin()