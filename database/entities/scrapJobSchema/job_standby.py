from sqlalchemy import Column, String, MetaData, Table,Integer,DateTime
from database.connection.connection import connection
from sqlalchemy import func

engine, base, session = connection()

metadata = MetaData()

JobsStandBy = Table(
    'job_standby',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True),
    Column("id_job",String(1500),nullable=False,unique=True),
    Column("used_term",String(50),nullable=False),
    Column("status",String(10),default='waiting'),
    Column("scraped_at",DateTime(timezone=True),server_default=func.now()),
    Column("site",String(25),nullable=False,default='none'),
    schema = 'scrap_job'
)

metadata.create_all(engine)