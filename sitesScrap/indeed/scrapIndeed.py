import time


def scrapLinks():
    from configsDir.environmentConfiguration import driverWeb
    from selenium.webdriver.common.by import By
    from database.operations.scrapJobSchema.job_standby_operations import listUrlStandBy
    from database.operations.scrapJobSchema.jobs_operations import insertJobsScrap
    from database.operations.scrapJobSchema.jobs_text_operations import insertTextScrap
    from database.operations.datasetSchema.job_info_operations import listInfos

    dictLinksStandby = listUrlStandBy(siteStandby='indeed')
    linksDb = list(dictLinksStandby.keys())

    benefitsInDb = listInfos()

    dictInsertInfo = {}
    driver = driverWeb()
    driver.get("https://www.google.com")
    for link in linksDb:
        try:
            _ = driver.current_url
            driver.get(link)
            vacancyTitle = driver.find_element(By.TAG_NAME,"h1").text
            vacancyOrg = driver.find_element(By.CLASS_NAME,"jobsearch-CompanyInfoContainer").text.split("\n")[0]
            content = driver.find_element(By.ID, 'jobDescriptionText').text
            annDiv = driver.find_elements(By.TAG_NAME,'span')
            for a in annDiv:
                if a.text.find("Anunciada:") != -1:
                    announc = a.text
            try:
                moreinfos = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[4]/div/div/div[1]/div[1]/div[5]/div[2]/div/div[2]').text
                content = f"{content} {moreinfos}"
            except:
                pass
            try:
                benefits = driver.find_element(By.ID, 'benefits').text
                benefits = benefits.replace('Benefícios','').replace('Retirados da descrição completa da vaga','')
                content = f"{content} {benefits}"
                incrementBenefits(benefits,benefitsInDb)
            except:
                pass

            dictInsertInfo.update({"vacancy_title":vacancyTitle,"idurlJob":link,"vacancy_org":vacancyOrg,
                                   "candidates": "indeed","vacancy_experience":"indeed",
                                   "date_publish": announc,"researched_topic":dictLinksStandby[link]
                                   })


            insertJobsScrap(dictInsertInfo,"indeed")
            insertTextScrap(content,link)

        except Exception as err:
            print(f"Cannot scrap/insert job. Error: {err}")
            time.sleep(5)
            driver.close()
            driver = driverWeb()
            driver.get("https://www.google.com")
            continue


def incrementBenefits(benefits:str,benefitsInDb:dict):
    import unidecode
    from database.operations.datasetSchema.job_info_operations import insertNewInfoJob

    benefitsInDb = list(benefitsInDb.keys())


    benefitsTreatment = benefits.lower()
    benefitsTreatment = unidecode.unidecode(benefitsTreatment)
    benefitsTreatment = benefitsTreatment.split("\n")

    listBenefitInsert = {}
    for benefit in benefitsTreatment:
        if len(benefit) != 0:
            if benefit not in benefitsInDb:
                listBenefitInsert.update({benefit:"benefit"})
    if len(listBenefitInsert.keys()) > 0:
        insertNewInfoJob(listBenefitInsert)
