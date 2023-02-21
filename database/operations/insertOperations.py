from database.connection.connection import connection
from sqlalchemy import insert

def treatmentInsertJobs(dictInfos:dict) -> dict:
    try:
        dictInfos['candidates']
    except:
        dictInfos.update({'candidates':'0'})
    return dictInfos


def insertJobsScrap(dictInfos:dict):
    from database.entities.jobs import Jobs
    engine, base, session = connection()
    with engine.connect() as conn:
        insertJob = insert(Jobs).values(
        id_url = dictInfos['idurlJob'],
        url_job = dictInfos['urlJob'],
        vacancy_title = dictInfos['vacancyTitle'],
        vacancy_org = dictInfos['vacancyOrg'],
        experience= dictInfos['vacancyExperience'],
        candidates=dictInfos['candidates'],
        date_publish=dictInfos['datePublish']
        )
        conn.execute(insertJob)
        conn.close()
    print(f"Insert {insertJob} succesfully.")

def insertTopicsScrap(topics:list, idUrl:str):
    from database.entities.jobs_topic import JobsTopics
    engine, base, session = connection()
    with engine.connect() as conn:
        for topic in topics:
            insertTopic = insert(JobsTopics).values(
                id_url = idUrl,
                topic = topic
        )
            conn.execute(insertTopic)
    conn.close()
    print(f"Topic insert succesfully.")


def insertTextScrap(textJob:str,idUrl:str):
    from database.entities.jobs_description import JobsDescriptions
    engine, base, session = connection()
    insertText = insert(JobsDescriptions).values(
        id_url=idUrl,
        text=textJob
    )
    with engine.connect() as conn:
        conn.execute(insertText)
    conn.close()
    print(f"Text insert succesfully.")
