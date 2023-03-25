def insertInfoDB() -> dict:
    from database.entities.datasetSchema.job_info import InfoJobs
    from database.connection.connection import connection
    from sqlalchemy import insert
    import requests
    import io
    import pandas as pd


    engine, base, session = connection()

    dictFrame:dict = {}

    res = requests.get("https://raw.githubusercontent.com/pedrohgoncalvess/jobanalytics/master/datasets/info_job.csv").content
    dfInfos = pd.read_csv(io.StringIO(res.decode('utf-8')), on_bad_lines='skip',sep=';')

    for num,line in enumerate(dfInfos['Info']):
        query = insert(InfoJobs).values(
            info = line.lower(),
            type = dfInfos['Type'][num].lower()
        )
        try:
            session.execute(query)
            session.commit()
            session.close()
        except:
            session.close()
    return dictFrame

def listInfos() -> dict:
    from database.entities.datasetSchema.job_info import InfoJobs
    from database.connection.connection import connection

    engine, base, session = connection()
    query = session.query(InfoJobs).all()

    dictInfo:dict = {}

    for line in query:
        dictInfo.update({line.tecnologie: line.type})

    return dictInfo