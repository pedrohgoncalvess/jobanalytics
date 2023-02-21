from sqlalchemy import Column,Integer,String, MetaData, Table
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

JobsDescriptions = Table(
    'jobs_description',
    metadata,
    Column("id_url",String(300),nullable=False, primary_key=True, unique=True),
    Column("text",String(15000)),
    schema = 'info_jobs'
)

metadata.create_all(engine)