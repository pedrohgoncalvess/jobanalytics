from database.connection.connection import connection
import pandas as pd

engine, base, session = connection()

def queryTextsJobs():
    from database.entities.jobs_description import JobsDescriptions
    query = session.query(JobsDescriptions)
    dataText = pd.read_sql(query.statement, session.bind)
    return dataText

def queryTecnologies():
    from sqlalchemy.sql import text
    query = text('select * from tecnologies_info')
    with engine.connect() as conn:
        data = conn.execute(query)
        for row in data:
            print(row)

#queryTextsJobs()
print(queryTecnologies())