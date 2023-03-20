def listTopicsForSearch():
    from database.connection.connection import connection
    from database.entities.schedulerSchema.topic_search import topicSearch

    engine, base, session = connection()

    listTopics:list = []
    query = session.query(topicSearch).all()
    for line in query:
        listTopics.append(line.topic_search)
    return listTopics