from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields
import sqlalchemy

def insertTextScrap(textJob:str,idUrl:str,session:sqlalchemy.orm.session.Session):
    from database.entities.scrapJobSchema.job_description import JobsDescriptions
    from database.operations.scrapJobSchema.jobs_operations import getIdJob
    try:
        textJob = formatSizeFields(15000,textJob)
        insertText = insert(JobsDescriptions).values(
            id_job=getIdJob(idUrl),
            text=textJob
        )
        session.execute(insertText)
        session.commit()
        session.close()
    except Exception as err:
        session.close()
        print(f"Cannot insert text job {idUrl}. Error {err}")