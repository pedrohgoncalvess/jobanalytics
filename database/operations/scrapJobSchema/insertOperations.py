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
    print(dictInfos['idurlJob'])
    with engine.connect() as conn:
        insertJob = insert(Jobs).values(
        id_job = dictInfos.get("vacancy_org",dictInfos['idurlJob'].split('at-')[1].split('-')[0].capitalize()),
        vacancy_title = dictInfos['vacancy_title'],
        vacancy_org = dictInfos['vacancy_org'],
        experience = dictInfos['vacancy_experience'],
        candidates = dictInfos.get('candidates',0),
        date_publish = dictInfos['date_publish']
        )
        conn.execute(insertJob)
    print(f"Insert {insertJob} succesfully.")

def insertTopicsScrap(topics:list, idUrl:str):
    from database.entities.scrapJobSchema.jobs_topic import JobsTopics
    engine, base, session = connection()
    with engine.connect() as conn:
        for topic in topics:
            if len(topic) > 99:
                topic = topic[0:99]
            insertTopic = insert(JobsTopics).values(
                id_job = getIdJob(idUrl),
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
        id_job=getIdJob(idUrl),
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

def getIdJob(urlJob:str):
    from database.entities.scrapJobSchema.jobs import Jobs
    engine, base, session = connection()

    query = session.query(Jobs).filter(Jobs.columns.id_job==urlJob).values(Jobs.columns.id)
    try:
        for result in query:
            idJob = result.id

        return idJob
    except:
        return False

