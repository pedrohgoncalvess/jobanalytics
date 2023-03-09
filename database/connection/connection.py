from sqlalchemy import create_engine, schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configsDir.environmentConfiguration import environmentsVariables as env

def connection(messages:str='on'):
    engine = create_engine(url=f"postgresql://{env('user')}:{env('password')}@{env('host_name')}/jobscrap",echo=True)
    Base = declarative_base()
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    session = SessionLocal()

    if messages == 'off':
        import logging

        logging.basicConfig()
        logging.disable(logging.WARNING)

    schemas = ['scrap_job','scrap_scheduler']
    for schemaName in schemas:
        if not engine.dialect.has_schema(engine, schemaName):
            engine.execute(schema.CreateSchema(schemaName))

    return engine, Base, session

def checkTables():
    from database.entities.scrapJobSchema.jobs import Jobs
    from database.entities.scrapJobSchema.jobs_description import JobsDescriptions
    from database.entities.scrapJobSchema.jobs_topic import JobsTopics
    from database.entities.schedulerSchema.set_path import setPath
    from database.entities.schedulerSchema.scheduler import schedulerScrap
    from database.entities.schedulerSchema.paths import sitesPaths

    if __name__ == '__main__':
        Jobs
        JobsDescriptions
        JobsTopics
        setPath
        schedulerScrap
        sitesPaths
