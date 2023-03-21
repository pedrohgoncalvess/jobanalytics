from database.connection.connection import connection
from sqlalchemy import insert

def insertUrlForStandBy(dictInfos:dict):
    from database.entities.scrapJobSchema.job_standby import JobsStandBy
    engine, base, session = connection()
    with engine.connect() as conn:
        for idurl in list(dictInfos.keys()):
            query = insert(JobsStandBy).values(
                id_job = idurl,
                used_term = dictInfos[idurl]
            )
            try:
                conn.execute(query)
            except:
                pass
    conn.close()

def listUrlStandBy() -> dict:
    from database.entities.scrapJobSchema.job_standby import JobsStandBy
    engine, base, session = connection()

    query = session.query(JobsStandBy).all()

    dictUrl:dict = {}
    for line in query:
        dictUrl.update({line.id_job:line.used_term})

    return dictUrl
