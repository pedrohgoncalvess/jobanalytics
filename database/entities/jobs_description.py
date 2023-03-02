from sqlalchemy import Column,Integer,String, MetaData, Table, ForeignKey
from database.connection.connection import connection
from database.entities.jobs import Jobs

engine, base, session = connection()

metadata = MetaData()

JobsDescriptions = Table(
    'jobs_description',
    metadata,
    Column("id_url",String(300),ForeignKey(Jobs.columns.id_url)),
    Column("text",String(15000),nullable=False),
    schema = 'scrap_jobs'
)

metadata.create_all(engine)