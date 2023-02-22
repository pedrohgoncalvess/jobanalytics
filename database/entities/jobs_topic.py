from sqlalchemy import Column,Integer,String, MetaData, Table, ForeignKey
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

JobsTopics = Table(
    'jobs_topics',
    metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("id_url",String(300),nullable=False),
    Column("topic",String(100), nullable=False),
    schema = 'info_jobs'
)

metadata.create_all(engine)