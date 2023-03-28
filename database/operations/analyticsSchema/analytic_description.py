def insertInfoDescription(dictInfo:dict):
    from database.entities.analyticsSchema.analytic_description import InfoDescription
    from sqlalchemy import insert
    from database.connection.connection import connection

    engine, base, session = connection()

    insert = insert(InfoDescription).values(
        id_job=dictInfo.get("id_job"),
        info=dictInfo.get("info"),
        type=dictInfo.get("type"),
        compost_key=dictInfo.get("compost_key")
    )

    try:
        session.execute(insert)
        session.commit()
        session.close()
        print("Insert successfully")
    except Exception as err:
        print(f"Cannot insert job info: {err}")
        session.close()
