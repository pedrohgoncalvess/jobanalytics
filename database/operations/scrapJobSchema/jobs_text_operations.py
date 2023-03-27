def insertTextScrap(textJob:str,idUrl:str):
    from database.entities.scrapJobSchema.job_description import JobsDescriptions
    from database.operations.scrapJobSchema.jobs_operations import getIdJob
    from sqlalchemy import insert

    from database.connection.connection import connection
    from database.operations.scrapJobSchema.midlevelOperations import formatSizeFields


    engine, base, session = connection()
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