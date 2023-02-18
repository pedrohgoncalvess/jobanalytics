from database.connection.connection import connection
from database.entities.jobs import Jobs


def treatmentInsertJobs(dictInfos:dict) -> dict:
    try:
        dictInfos['candidates']
    except:
        dictInfos.update({'candidates':'0'})
    return dictInfos


def insertJobsScrap(dictInfos:dict):
    engine, base, session = connection()
    insertJob = Jobs(
    url_job = dictInfos['urlJob'],
    vacancy_title = dictInfos['vacancyTitle'],
    vacancy_org = dictInfos['vacancyOrg'],
    experience= dictInfos['vacancyExperience'],
    candidates=dictInfos['candidates']
    )

    session.add(insertJob)
    session.commit()
    session.close()

def setErrorStatusJob(url:str):
    pass


