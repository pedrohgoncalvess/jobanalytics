
def treatmentTopics(topics:list) -> list:
    newTopicList = list()
    for topic in topics:
        if len(topic) >= 1:
            newTopicList.append(topic)
    return newTopicList

