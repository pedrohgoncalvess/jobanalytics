from sqlalchemy import Column,Integer,String,DateTime, MetaData, Table, ForeignKey
from sqlalchemy import func
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

Jobs = Table(
    'job',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True,unique=True),
    Column("id_job",String(1500), unique=True),
    Column("vacancy_title",String(70),default='none'),
    Column("vacancy_org",String(70),default='none'),
    Column("experience",String(75),default='none'),
    Column("candidates",String(50), default=0),
    Column("date_publish",String(75), default='none'),
    Column("scraped_at",DateTime(timezone=True),server_default=func.now()),
    Column("researched_topic",String(50), nullable=False),
    Column("site_job",String(30), nullable=False),
    schema = 'scrap_job'
)

metadata.create_all(engine)