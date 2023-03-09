from sqlalchemy import Column, String, MetaData, Table, ForeignKey
from database.connection.connection import connection
from database.entities.scrapJobSchema.jobs import Jobs

engine, base, session = connection()

metadata = MetaData()

JobsTopics = Table(
    'jobs_topics',
    metadata,
    Column("id_url",String(300),ForeignKey(Jobs.columns.id_url)),
    Column("topic",String(100), nullable=False),
    schema = 'scrap_job'
)

metadata.create_all(engine)