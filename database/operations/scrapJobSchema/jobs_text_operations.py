from database.connection.connection import connection
from sqlalchemy import insert
from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields

def insertTextScrap(textJob:str,idUrl:str):
    from database.entities.scrapJobSchema.job_description import JobsDescriptions
    from database.operations.scrapJobSchema.jobs_operations import getIdJob
    engine, base, session = connection()
    textJob = formatSizeFields(15000,textJob)
    insertText = insert(JobsDescriptions).values(
        id_job=getIdJob(idUrl),
        text=textJob
    )
    session.execute(insertText)
    session.commit()
    session.close()