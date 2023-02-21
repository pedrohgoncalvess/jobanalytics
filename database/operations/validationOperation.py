def validationUrlExist() -> bool:
    from database.connection.connection import connection
    from database.entities.jobs import Jobs
    engine, base, session = connection()

    query = session.query(Jobs).all()
    links:list = []
    for row in query:
        links.append(row.id_url)

    return links

validationUrlExist()

