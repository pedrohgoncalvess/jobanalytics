from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields
import sqlalchemy

def insertTopicsScrap(topics:list, idUrl:str):
    from database.entities.scrapJobSchema.job_topic import JobsTopics
    from database.operations.scrapJobSchema.jobs_operations import getIdJob
    from database.connection.connection import connection

    engine, base, session = connection()

    for topic in topics:
        topic = formatSizeFields(100,topic)
        insertTopic = insert(JobsTopics).values(
            id_job = getIdJob(idUrl),
            topic = topic
    )
        try:
            session.execute(insertTopic)
            session.commit()
            session.close()
        except Exception as err:
            session.close()
            print(f"Cannot insert topic because: {err}")

