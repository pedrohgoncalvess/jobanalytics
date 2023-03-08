from database.connection.connection import connection
from sqlalchemy import insert
from sqlalchemy.sql import text as sa_text
from sqlalchemy.sql.schema import Table



def createSetPath(setPathDict:dict):
    from database.entities.paths_fields.set_path import setPath
    engine, base, session = connection()
    insertSet = insert(setPath).values(
    name_set = setPathDict['nameSet'].lower(),
    site_scrap = setPathDict['siteScrap'].lower(),
    )
    session.execute(insertSet)
    results = session.query(setPath).all()
    for result in results:
        print(result)
    session.rollback()

def createPathSite(sitePathDict:dict):
    from database.entities.paths_fields.paths import sitesPaths
    engine, base, session = connection()

    insertPath = insert(sitesPaths).values(
            #id_set =
    )

    results = session.query(sitesPaths).all()
    for result in results:
        print(result)
    session.rollback()

