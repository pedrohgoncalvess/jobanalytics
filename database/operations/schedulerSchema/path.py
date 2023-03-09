from database.connection.connection import connection
from sqlalchemy import insert

def createPathSite(sitePathDict:dict):
    from database.entities.schedulerSchema.paths import sitesPaths

    engine, base, session = connection()

    insertPath = insert(sitesPaths).values(
        name_set=sitePathDict['nameSet'].lower(),
        site_scrap=sitePathDict['siteScrap'].lower(),
    )
    session.execute(insertPath)
    session.commit()
    session.close()