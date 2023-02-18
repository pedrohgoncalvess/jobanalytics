from sqlalchemy import Column,Integer,String
from database.connection.connection import connection

engine, base, session = connection()

class JobsDescription(base):
    __tablename__ = 'jobs_description'
    id = Column(Integer, primary_key = True, autoincrement=True)
    url_job = Column(String(300), unique=True, nullable=False)
    topic = Column(String(50), nullable=False)
    text_body = Column(String(3000),nullable=False)