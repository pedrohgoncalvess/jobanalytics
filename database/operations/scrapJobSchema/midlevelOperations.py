from database.connection.connection import connection
from sqlalchemy import insert
from sqlalchemy.sql.schema import Table
from database.entities.scrapJobSchema.jobs import Jobs

def treatmentInsertJobs(dictInfos:dict) -> dict:
    try:
        dictInfos['candidates']
    except:
        dictInfos.update({'candidates':'0'})
    return dictInfos

def validationUrlExist(table:Table = Jobs) -> bool:

    from database.connection.connection import connection
    engine, base, session = connection()

    query = session.query(table).all()
    links:list = []
    for row in query:
        links.append(row.id_job)

    return links

def formatSizeFields(size:int,field:str):
    if len(field) > size:
        field = field[0:size]
    return field