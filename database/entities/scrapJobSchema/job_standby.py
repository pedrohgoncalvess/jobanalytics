from sqlalchemy import Column, String, MetaData, Table,Integer
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

JobsStandBy = Table(
    'job_standby',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True),
    Column("id_job",String(500),nullable=False,unique=True),
    Column("used_term",String(20),nullable=False),
    Column("status",String(10),default='waiting'),
    schema = 'scrap_job'
)

metadata.create_all(engine)