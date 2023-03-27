from database.connection.connection import connection
from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields
import sqlalchemy


def insertJobsScrap(dictInfos:dict,site:str,session:sqlalchemy.orm.session.Session):
    from database.entities.scrapJobSchema.job import Jobs
    engine, base, session = connection()
    try:
        insertJob = insert(Jobs).values(
        id_job = dictInfos['idurlJob'],
        vacancy_title = formatSizeFields(70,dictInfos['vacancy_title']),
        vacancy_org = dictInfos.get("vacancy_org",dictInfos['idurlJob'].split('at-')[1].split('-')[0].capitalize()),
        experience = formatSizeFields(70,dictInfos['vacancy_experience']),
        candidates = dictInfos.get('candidates',0),
        date_publish = dictInfos['date_publish'],
        researched_topic = dictInfos.get('researched_topic'),
        site_job = site
        )
        session.execute(insertJob)
        session.commit()
        session.close()
    except Exception as err:
        session.close()
        print(f"Cannot insert {dictInfos['idurlJob']} job. Error {err}")


def getIdJob(urlJob:str):
    from database.entities.scrapJobSchema.job import Jobs
    engine, base, session = connection()

    query = session.query(Jobs).filter(Jobs.columns.id_job==urlJob).values(Jobs.columns.id)
    session.close()
    try:
        for result in query:
            idJob = result.id
        return idJob
    except:
        return False

def listJobsInDB():
    from database.entities.scrapJobSchema.job import Jobs
    engine, base, session = connection()

    query = session.query(Jobs).all()
    session.close()

    listJobs:list = []
    for line in query:
        listJobs.append(line.id_job)
    return listJobs