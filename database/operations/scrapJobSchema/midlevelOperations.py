def validationUrlExist() -> list:
    from database.connection.connection import connection
    from database.entities.scrapJobSchema.job import Jobs

    engine, base, session = connection()

    query = session.query(Jobs).values(Jobs.columns.id_job)
    links:list = []
    for row in query:
        links.append(row.id_job)

    session.close()
    return links

def formatSizeFields(size:int,field:str):
    if len(field) >= size:
        field = field[0:size]
        return field
    else:
        return field