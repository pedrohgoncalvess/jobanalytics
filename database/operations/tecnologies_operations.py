def insertTecnologiesDB() -> dict:
    from database.entities.tecnologies import Tecnologies
    from database.connection.connection import connection
    from sqlalchemy import insert
    import requests
    import io
    import pandas as pd

    engine, base, session = connection()

    dictFrame:dict = {}

    res = requests.get("https://raw.githubusercontent.com/pedrohgoncalvess/jobanalytics/master/datasets/tecnologies_jsa.csv").content
    dfTecnologies = pd.read_csv(io.StringIO(res.decode('utf-8')), on_bad_lines='skip',sep=';')

    for num,line in enumerate(dfTecnologies['Tecnology']):
        query = insert(Tecnologies).values(
            tecnologie = line.lower(),
            type = dfTecnologies['Area'][num].lower()
        )
        try:
            session.execute(query)
            session.commit()
            session.close()
        except:
            session.close()
    return dictFrame

def listTecnologies() -> dict:
    from database.entities.tecnologies import Tecnologies
    from database.connection.connection import connection

    engine, base, session = connection()
    query = session.query(Tecnologies).all()

    dictTecnologies:dict = {}

    for line in query:
        dictTecnologies.update({line.tecnologie: line.type})

    return dictTecnologies