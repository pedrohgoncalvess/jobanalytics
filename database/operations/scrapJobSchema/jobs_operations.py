from database.connection.connection import connection
from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields

def insertJobsScrap(dictInfos:dict):
    from database.entities.scrapJobSchema.job import Jobs
    engine, base, session = connection()
    with engine.connect() as conn:
        insertJob = insert(Jobs).values(
        id_job = dictInfos['idurlJob'],
        vacancy_title = formatSizeFields(70,dictInfos['vacancy_title']),
        vacancy_org = dictInfos.get("vacancy_org",dictInfos['idurlJob'].split('at-')[1].split('-')[0].capitalize()),
        experience = dictInfos.get('vacancy_experience','None'),
        candidates = dictInfos.get('candidates',0),
        date_publish = dictInfos['date_publish'],
        researched_topic = dictInfos.get('researched_topic')
        )
        try:
            conn.execute(insertJob)
            conn.close()
            print(f"Insert {insertJob} succesfully.")
        except Exception as err:
            print(f"Cannot insert {formatSizeFields(70,dictInfos['vacancy_title'])} job. Error {err}")
            conn.close()


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