from sqlalchemy import Column,Integer,String
from database.connection import connection

engine, base, session = connection()

class Lead(base):
    __tablename__ = 'leadsInfos'
    id = Column(Integer, primary_key = True)
    email = Column(String(50))
    name = Column(String(70))
    job_title = Column(String(20))
    public_url = Column(String(100))