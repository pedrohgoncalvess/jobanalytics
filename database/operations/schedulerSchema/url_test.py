def insertUrlTest(url:str):
    from database.entities.schedulerSchema.urls_test import urlTest
    from database.connection.connection import connection
    from sqlalchemy import insert

    engine, base, session = connection()

    query = insert(urlTest).values(
        url_job = url
    )

    session.execute(query)
    session.commit()
    session.close()

def getLinkUrlTest():
    from database.entities.schedulerSchema.urls_test import urlTest
    from database.connection.connection import connection
    from sqlalchemy import insert
    from datetime import datetime

    engine, base, session = connection()

    today = datetime.now().strftime("%Y-%m-%d")

    query = session.query(urlTest).filter(urlTest.columns.scraped_at==today)
    for row in query:
        return row.url_job
