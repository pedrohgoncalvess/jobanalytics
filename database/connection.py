from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environmentConfiguration import environmentsVariables as env

def connection():
    engine = create_engine(url=f"postgresql://{env('user')}:{env('password')}@{env('host_name')}/postgres")
    Base = declarative_base()
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    return engine, Base, SessionLocal
