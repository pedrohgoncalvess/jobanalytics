def validationUrlExist(url:str) -> bool:
    from database.connection.connection import connection
    from database.entities.jobs import Jobs
    engine, base, session = connection()

    exist = session.query(
        session.query(Jobs).filter_by(id_url=url).exists()
    ).scalar()

    return exist

