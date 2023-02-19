from database.connection.connection import connection
from sqlalchemy import insert
from database.entities.jobs import Jobs


def treatmentInsertJobs(dictInfos:dict) -> dict:
    try:
        dictInfos['candidates']
    except:
        dictInfos.update({'candidates':'0'})
    return dictInfos


def insertJobsScrap(dictInfos:dict):
    engine, base, session = connection()
    print(dictInfos['idurlJob'])
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
    print(f"Insert {insertJob} succesfully.")

def setErrorStatusJob(url:str):
    pass


