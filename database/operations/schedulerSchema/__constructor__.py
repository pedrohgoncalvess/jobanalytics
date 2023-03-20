from database.connection.connection import connection
from sqlalchemy import insert
from types import FunctionType
from database.operations.schedulerSchema.dataSchedulers import dataPaths,viewMoreInfos,loginPaths

engine, base, session = connection(messages='off')

def verifySetPath(func:FunctionType):
    from database.entities.schedulerSchema.set_path import setPath


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

def inputVacancyTable():
    from database.operations.schedulerSchema.dataSchedulers import topics_search
    from database.entities.schedulerSchema.topic_search import topicSearch

    listTopics = topics_search()

    for topic in listTopics:
        query = insert(topicSearch).values(
            topic_search = topic
        )
        session.execute(query)
        try:
            session.commit()
            session.close()
        except:
            session.close()



def _mainInit():
    verifyPaths(dataPaths(),stage = 'scrap')
    verifyPaths(loginPaths(),stage = 'login')
    verifyPaths(viewMoreInfos(),stage='view_more_infos')
    inputVacancyTable()
