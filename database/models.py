from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy import func
from database.connection import connection

engine, base, session = connection()

class Jobs(base):
    __tablename__ = 'Jobs'
    id = Column(Integer, primary_key = True)
    url = Column(String(270), unique=True)
    scraped_at = Column(DateTime(timezone=True),server_default=func.now())
    status = Column(String(10), default='waiting')