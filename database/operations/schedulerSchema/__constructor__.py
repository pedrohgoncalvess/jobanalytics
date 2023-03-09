from database.connection.connection import connection
from sqlalchemy import insert
from sqlalchemy.sql import exists
from types import FunctionType


def verifySetPath(func:FunctionType):
    from database.entities.schedulerSchema.set_path import setPath

    engine, base, session = connection(messages='off')

    name_sets = ['linkedin_path_1','linkedin_path_2']
    for set in name_sets:
        query = session.query(session.query(setPath).filter(setPath.columns.name_set==set).exists()).scalar()
        if query == False:
            insertSet = insert(setPath).values(
                name_set = set,
                site_scrap = 'linkedin'
            )
            session.execute(insertSet)
    session.commit()
    def executeFunction():
        func()
    return executeFunction

@verifySetPath
def verifyPaths():
    from configsDir.dataXpath import dataPaths,viewMoreInfos
    from database.entities.schedulerSchema.paths import sitesPaths
    from database.entities.schedulerSchema.set_path import setPath

    engine, base, session = connection(messages='off')
    name_sets = ['linkedin_path_1', 'linkedin_path_2']

    dictSets:dict = {}
    for setName in name_sets:
        query = session.query(setPath).filter(setPath.columns.name_set==setName).values(setPath.columns.id)
        session.close()
        for result in query:
            idSet = result.id
            dictSets.update({setName:idSet})
    dataPathsInsert = dataPaths()
    for num,name_set in enumerate(name_sets):
        dataPath = dataPathsInsert[num]
        typesComponentsList = list(dataPath.keys())
        for type in typesComponentsList:
            queryInsert = insert(sitesPaths).values(
                id_set = dictSets.get(name_set),
                type_component = "scrap",
                type_info = type,
                path = dataPath.get(type)
            )
            try:
                session.execute(queryInsert)
                session.commit()
            except:
                session.close()



if __name__ == '__main__':
    verifyPaths()
