def insertTecnologiesDB():
    from database.entities.tecnologies import Tecnologies
    from database.connection.connection import connection
    from sqlalchemy import insert
    import pandas as pd

    engine, base, session = connection()

    dictFrame:dict = {}
    dfTecnologies = pd.read_csv("../../datasets/tecnologies_jsa.csv",on_bad_lines='skip',sep=';')
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

