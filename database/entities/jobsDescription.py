from sqlalchemy import Column,Integer,String, MetaData
from database.connection.connection import connection

engine, base, session = connection()

class JobsDescription(base):
    __tablename__ = 'jobs_description'
    id = Column(Integer, primary_key = True, autoincrement=True)
    url_job = Column(String(300), unique=True, nullable=False)
    topic = Column(String(100), nullable=False)
    text_topic = Column(String(500), nullable=False)
    text_body = Column(String(5000),nullable=False)
    schema = 'infoJobs'

JobsDescription.__table__

metadata = MetaData()
metadata.create_all(engine, checkfirst=True)