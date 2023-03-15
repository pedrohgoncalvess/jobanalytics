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


