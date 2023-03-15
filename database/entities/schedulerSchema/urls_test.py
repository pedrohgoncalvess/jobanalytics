from sqlalchemy import Column,Integer,String, MetaData, Table, Date
from sqlalchemy.sql import func
from database.connection.connection import connection
from database.entities.schedulerSchema.set_path import setPath

engine, base, session = connection()

metadata = MetaData()

urlTest = Table(
    'url_test',
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("url_job",String(400),nullable=False),
    Column("scraped_at",Date,nullable=False,server_default=func.now()),
    schema='scrap_scheduler'
)

metadata.create_all(engine)