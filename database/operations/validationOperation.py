from sqlalchemy.sql.schema import Table
from database.entities.scrapJobSchema.jobs import Jobs

def validationUrlExist(table:Table = Jobs) -> bool:
    from database.connection.connection import connection
    engine, base, session = connection()

    query = session.query(table).all()
    links:list = []
    for row in query:
        links.append(row.id_url)

    return links

