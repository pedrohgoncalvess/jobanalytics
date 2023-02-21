from sqlalchemy import create_engine, schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configsDir.environmentConfiguration import environmentsVariables as env

def connection():
    engine = create_engine(url=f"postgresql://{env('user')}:{env('password')}@{env('host_name')}/postgres",echo=True)
    Base = declarative_base()
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    session = SessionLocal()

    if not engine.dialect.has_schema(engine, "info_jobs"):
        engine.execute(schema.CreateSchema("info_jobs"))

    return engine, Base, session
