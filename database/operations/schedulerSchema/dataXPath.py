
def dataPaths() -> dict:

    infosXpath:dict = {
        'content':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div',
        'date_publish':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/span',
        'candidates':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/figure/figcaption',
        'vacancy_title':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1',
        'vacancy_experience':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[1]/span'
    }

    infosXpathAlternative:dict = {
        'content':'//*[@id="job-details"]/span',
        'date_publish': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[2]/span[1]',
        'candidates': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[2]/span[2]',
        'vacancy_title': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/h1',
        'vacancy_experience': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[2]/ul/li[1]'
    }

    datas:list = [infosXpath,infosXpathAlternative]

    return datas


def viewMoreInfos() -> list:
    viewMoreInfos:dict = {
        'view_more':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]/icon'
    }

    viewMoreInfosAlternative: dict = {
        'view_more': '//*[@id="ember32"]'
    }

    viewMoreInfosAlternative_2:dict = {
        'view_more': '//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]'
    }


    listMoreInfos = [viewMoreInfos,viewMoreInfosAlternative_2,viewMoreInfosAlternative]
    return listMoreInfos

def loginPaths() -> list:
    loginPath:dict = {
        'username':'//*[@id="session_key"]',
        'password':'//*[@id="session_password"]',
        'button':'//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button'
    }

    loginPathAlternative: dict = {
        'username': '//*[@id="session_key"]',
        'password': '//*[@id="session_password"]',
        'button': '//*[@id="main-content"]/section[1]/div/div/form/button'
    }

    listPaths = [loginPath,loginPathAlternative]
    return listPaths
