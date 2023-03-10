from database.connection.connection import connection
from sqlalchemy import insert
from types import FunctionType
from database.operations.schedulerSchema.dataXPath import dataPaths,viewMoreInfos,loginPaths


def verifySetPath(func:FunctionType):
    from database.entities.schedulerSchema.set_path import setPath

    engine, base, session = connection(messages='off')

    name_sets = ['scrap','login','view_more_infos']
    for set in name_sets:
        query = session.query(session.query(setPath).filter(setPath.columns.stage_scrap==set).exists()).scalar()
        if query == False:
            insertSet = insert(setPath).values(
                stage_scrap = set,
                site_scrap = 'linkedin'
            )
            session.execute(insertSet)
    session.commit()
    def executeFunction(dataPathsInsert,stage):
        func(dataPathsInsert,stage)
    return executeFunction

@verifySetPath
def verifyPaths(dataPathsInsert:list,stage:str):
    from database.entities.schedulerSchema.paths import sitesPaths
    from database.entities.schedulerSchema.set_path import setPath

    engine, base, session = connection(messages='off')

    dictSets:dict = {}
    query = session.query(setPath).filter(setPath.columns.stage_scrap==stage).values(setPath.columns.id)
    session.close()
    for result in query:
        idSet = result.id
        dictSets.update({stage:idSet})
    for dataPath in dataPathsInsert:
        typesComponentsList = list(dataPath.keys())
        for type in typesComponentsList:
            queryInsert = insert(sitesPaths).values(
                id_set = dictSets.get(stage),
                type_info = type,
                path = dataPath.get(type)
            )
            try:
                session.execute(queryInsert)
                session.commit()
            except:
                session.close()


if __name__ == '__main__':
    verifyPaths(dataPaths(),stage = 'scrap')
    verifyPaths(loginPaths(),stage = 'login')
    verifyPaths(viewMoreInfos(),stage='view_more_infos')
