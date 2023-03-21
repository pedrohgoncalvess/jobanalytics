from database.connection.connection import connection
from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields

def insertTopicsScrap(topics:list, idUrl:str):
    from database.entities.scrapJobSchema.job_topic import JobsTopics
    from database.operations.scrapJobSchema.jobs_operations import getIdJob
    engine, base, session = connection()
    with engine.connect() as conn:
        for topic in topics:
            topic = formatSizeFields(100,topic)
            insertTopic = insert(JobsTopics).values(
                id_job = getIdJob(idUrl),
                topic = topic
        )
            try:
                conn.execute(insertTopic)
            except Exception as err:
                print(f"Cannot insert topic because: {err}")
    conn.close()

