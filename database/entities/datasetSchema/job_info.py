from sqlalchemy import Column,Integer,String, MetaData, Table
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

InfoJobs = Table(
    'job_info',
    metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("info",String(50),nullable=False, unique=True),
    Column("type",String(50), nullable=False),
    schema = 'dataset_schema'
)

metadata.create_all(engine)