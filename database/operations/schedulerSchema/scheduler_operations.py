from database.connection.connection import connection
from sqlalchemy import insert

def createSchedulerExec(schedulerDict:dict):
    from database.entities.schedulerSchema.scheduler import schedulerScrap
    from database.entities.schedulerSchema.paths import sitesPaths

    engine, base, session = connection()

    path = schedulerDict.get('idPath')
    query = session.query(sitesPaths).filter(sitesPaths.columns.path==path).values(sitesPaths.columns.id)
    for result in query:
        idPath = result.id

    insertPathTested = insert(schedulerScrap).values(
        id_path=idPath
    )
    session.execute(insertPathTested)
    session.commit()
    session.close()

def validateScheduler(stage:str,site:str='linkedin'):
    from database.connection.connection import connection
    from sqlalchemy.sql import text
    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")


    engine, base, session = connection(messages='off')
    with engine.connect() as conn:
        query = text(f"select 1 from scrap_scheduler.scheduler where exists ( select 1  from scrap_scheduler.scheduler sch "
                     f"inner join scrap_scheduler.path_site ps on ps.id = sch.id_path "
                     f"inner join scrap_scheduler.set_path sp on sp.id = ps.id_set "
                     f"where 1=1"
                     f"and sch.tested_at = '{today}'"
                     f"and sp.site_scrap = '{site}'"
                     f"and sp.stage_scrap = '{stage}')"
                     f"group by 1")
        result = conn.execute(query)
        print(query)
        for line in result:
            a = line
            if a == None:
                return False
            else:
                return True

def getCorrectPath(type_info:str):
    from database.connection.connection import connection
    from sqlalchemy.sql import text
    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")

    engine, base, session = connection(messages='off')

    query = text(f"""with scheduler as (
    select ps.path 
    from scrap_scheduler.scheduler sch 
    inner join scrap_scheduler.path_site ps on ps.id = sch.id_path 
    inner join scrap_scheduler.set_path sp on sp.id = ps.id_set 
    where 1=1 
    and sp.site_scrap = 'linkedin' 
    and ps.type_info = '{type_info}' 
    and sch.tested_at = '{today}'
) select * from scheduler""")

    with engine.connect() as conn:
        result = conn.execute(query)
        path = result.fetchone()
        path = path[0]
    return path




