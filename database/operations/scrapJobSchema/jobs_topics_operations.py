from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields
import sqlalchemy

def insertTopicsScrap(topics:list, idUrl:str,session:sqlalchemy.orm.session.Session):
    from database.entities.scrapJobSchema.job_topic import JobsTopics
    from database.operations.scrapJobSchema.jobs_operations import getIdJob
    for topic in topics:
        topic = formatSizeFields(100,topic)
        insertTopic = insert(JobsTopics).values(
            id_job = getIdJob(idUrl),
            topic = topic
    )
        try:
            session.execute(insertTopic)
            session.commit()
        except Exception as err:
            print(f"Cannot insert topic because: {err}")
    session.close()

