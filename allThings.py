def validateScheduler(site:str, stage:str):
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
        for line in result:
            if line:
                return True
            else:
                return False

print(validateScheduler('linkedin','login'))