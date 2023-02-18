
def dataPaths(data:str) -> dict:
    viewMoreInfos:dict = {
        'exibirMais':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]/icon',
        'verMais':'//*[@id="ember32"]'
    }

    infosXpath:dict = {
        'content':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div',
        'datePublish':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/span',
        'candidates':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[2]/figure/figcaption',
        'vacancyOrg':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]/a',
        'vacancyTitle':'//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/h1',
        'vacancyExperience':'//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[1]/span'
    }

    datas:list = {'viewMoreInfos':viewMoreInfos,'infosXpath':infosXpath}

    return datas[data]
