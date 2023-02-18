from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy import func
from database.connection.connection import connection

engine, base, session = connection()

class Jobs(base):
    __tablename__ = 'Jobs'
    id = Column(Integer, primary_key = True, autoincrement=True)
    url_job = Column(String(300), unique=True, nullable=False)
    vacancy_title = Column(String(70))
    vacancy_org = Column(String(70))
    experience = Column(String(25))
    candidates = Column(Integer)
    scraped_at = Column(DateTime(timezone=True),server_default=func.now())
    status = Column(String(10), default='waiting')