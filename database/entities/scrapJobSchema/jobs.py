from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey
from sqlalchemy import func
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

Jobs = Table(
    'jobs',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True,unique=True),
    Column("id_job",String(300), unique=True),
    Column("vacancy_title",String(70),default='none'),
    Column("vacancy_org",String(70),default='none'),
    Column("experience",String(75),default='none'),
    Column("candidates",String(50), default=0),
    Column("date_publish",String(75), default='none'),
    Column("scraped_at",DateTime(timezone=True),server_default=func.now()),
    Column("status",String(10), default='waiting'),
    schema = 'scrap_job'
)

metadata.create_all(engine)