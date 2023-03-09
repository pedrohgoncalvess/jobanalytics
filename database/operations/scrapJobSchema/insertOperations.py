from database.connection.connection import connection
from sqlalchemy import insert

def treatmentInsertJobs(dictInfos:dict) -> dict:
    try:
        dictInfos['candidates']
    except:
        dictInfos.update({'candidates':'0'})
    return dictInfos


def insertJobsScrap(dictInfos:dict):
    from database.entities.scrapJobSchema.jobs import Jobs
    engine, base, session = connection()
    with engine.connect() as conn:
        insertJob = insert(Jobs).values(
        id_url = dictInfos['idurlJob'],
        vacancy_title = dictInfos['vacancyTitle'],
        vacancy_org = dictInfos['vacancyOrg'],
        experience= dictInfos['vacancyExperience'],
        candidates=dictInfos['candidates'],
        date_publish=dictInfos['datePublish']
        )
        print(insertJob)
        conn.execute(insertJob)
    print(f"Insert {insertJob} succesfully.")

def insertTopicsScrap(topics:list, idUrl:str):
    from database.entities.scrapJobSchema.jobs_topic import JobsTopics
    engine, base, session = connection()
    with engine.connect() as conn:
        for topic in topics:
            insertTopic = insert(JobsTopics).values(
                id_url = idUrl,
                topic = topic
        )
            conn.execute(insertTopic)
    print("Topic insert succesfully.")


def insertTextScrap(textJob:str,idUrl:str):
    from database.entities.scrapJobSchema.jobs_description import JobsDescriptions
    engine, base, session = connection()
    if len(textJob) > 15000:
        textJob = textJob[0:14999]
    insertText = insert(JobsDescriptions).values(
        id_url=idUrl,
        text=textJob
    )
    with engine.connect() as conn:
        conn.execute(insertText)
    conn.close()
    print("Text insert succesfully.")


def createSetPath(setPathDict:dict):
    from database.entities.schedulerSchema.set_path import setPath
    engine, base, session = connection()
    with engine.connect() as conn:
        insertSet = insert(setPath).values(
        name_set = setPathDict['nameSet'].lower(),
        site_scrap = setPathDict['siteScrap'].lower(),
        )
        conn.execute(insertSet)
