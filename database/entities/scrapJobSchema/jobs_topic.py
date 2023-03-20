from sqlalchemy import Column, String, MetaData, Table, ForeignKey,Integer
from database.connection.connection import connection
from database.entities.scrapJobSchema.jobs import Jobs

engine, base, session = connection()

metadata = MetaData()

JobsTopics = Table(
    'job_topics',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True),
    Column("id_job",Integer,ForeignKey(Jobs.columns.id)),
    Column("topic",String(100), nullable=False),
    schema = 'scrap_job'
)

metadata.create_all(engine)