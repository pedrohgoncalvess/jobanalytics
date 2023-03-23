def listTopicsForSearch():
    from database.connection.connection import connection
    from database.entities.schedulerSchema.topic_search import topicSearch

    engine, base, session = connection()

    listTopics:dict = {}
    query = session.query(topicSearch).all()
    for line in query:
        listTopics.update({line.topic_search:line.topic_classification})
    session.close()

    listTopicsKeys:list = sorted(list(listTopics.keys()))
    newDictTopics:dict = {}
    for key in listTopicsKeys:
        newDictTopics.update({key:listTopics[key]})

    return newDictTopics