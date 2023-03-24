from database.connection.connection import connection
from sqlalchemy import insert
import sqlalchemy

def insertUrlForStandBy(dictInfos:dict, siteScrap:str,session:sqlalchemy.orm.session.Session):
    from database.entities.scrapJobSchema.job_standby import JobsStandBy

    for idurl in list(dictInfos.keys()):
        query = insert(JobsStandBy).values(
            id_job = idurl,
            used_term = dictInfos[idurl],
            site = siteScrap
        )
        try:
            session.execute(query)
            session.commit()
        except Exception as err:
            print(err)
            session.close()
    session.close()

def listUrlStandBy() -> dict:
    from database.entities.scrapJobSchema.job_standby import JobsStandBy
    engine, base, session = connection()

    query = session.query(JobsStandBy).filter(JobsStandBy.columns.status=='waiting').all()

    dictUrl:dict = {}
    for line in query:
        dictUrl.update({line.id_job:line.used_term})
    session.close()

    return dictUrl