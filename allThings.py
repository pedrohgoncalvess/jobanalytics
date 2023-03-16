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
    WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="ember16"]')))
    print(driver.current_url)
    driver.get('https://www.linkedin.com/jobs/view/3524160164/?eBP=CwEAAAGG6GghpIgoavYxfQ_ZeU_Q9JAFK4CW7Mk_pfq0DuugxfOxr3RT3TJJxBwiOLYbwg9fDYCjk4C8snrlQGuhKk5nYfqerJuRv-98zn6aoHbSGXKhCI7kNyfoMRW8eP1KNBIQdPiGrPkXrYwREMAitIXts7X_vAT_NZmlWRz1YATk44m4Gpr_KaTdPEP6EJfjXhCBYZNurKW9riRDz_hSpQM4OuCnNgHViYOioCnfjcSAOQd27wLR3avg8WYVurCOjUAQXs4rhBU0KqslERklmbbEE4wlE9E_grYm-ORZ5MmxF0bVjPNRWDLKAfhDApCqtZRvBok0kvbuek5vGQGdn6iW_TK1EnVEWPyIAlsrM7eUk_uzLe_rVotxLFFn6cJ-8u_hhf0&refId=nE0fMBgm35xiJim7v8P%2Fyw%3D%3D&trackingId=rkl%2BU1lASiFzjm3ZJT8ziQ%3D%3D&trk=flagship3_search_srp_jobs')

    time.sleep(15000)

validateScheduler()