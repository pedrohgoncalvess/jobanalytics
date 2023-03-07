
def dataPaths() -> dict:

    infosXpath:dict = {
        'content':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div',
        'datePublish':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/span',
        'candidates':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/figure/figcaption',
        'vacancyTitle':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1',
        'vacancyExperience':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[1]/span'
    }

    infosXpathAlternative = {
        'content':'//*[@id="job-details"]/span',
        'datePublish': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[2]/span[1]',
        'candidates': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[2]/span[2]',
        'vacancyTitle': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/h1',
        'vacancyExperience': '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[2]/ul/li[1]'
    }

    datas:list = [infosXpath,infosXpathAlternative]

    return datas


def viewMoreInfos() -> dict:
    viewMoreInfos:dict = {
        'exibirMais':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]/icon',
        'verMais':'//*[@id="ember32"]',
        'exibirMais2':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]'

    }
    return viewMoreInfos
