from database.connection.connection import connection
from sqlalchemy import insert

def createSchedulerExec(schedulerDict:dict):
    from database.entities.schedulerSchema.scheduler import schedulerScrap
    from database.entities.schedulerSchema.paths import sitesPaths

    engine, base, session = connection()

    path = schedulerDict.get('idPath')
    query = session.query(sitesPaths).filter(sitesPaths.columns.path==path).values(sitesPaths.columns.id)
    for result in query:
        idPath = result.id

    insertPathTested = insert(schedulerScrap).values(
        id_path=idPath
    )
    session.execute(insertPathTested)
    session.commit()
    session.close()

