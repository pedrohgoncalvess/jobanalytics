from database.connection.connection import connection
from sqlalchemy import insert

def createSetPath(sitePathDict:dict):
    from database.entities.schedulerSchema.paths import sitesPaths

    engine, base, session = connection()

    insertPath = insert(sitesPaths).values(
        id_set=sitePathDict.get('id_set'),
        type_component=sitePathDict.get('typeComponent'),
        type_info=sitePathDict.get('typeInfo'),
        path=sitePathDict.get('path')
    )
    session.execute(insertPath)
    session.commit()
    session.close()