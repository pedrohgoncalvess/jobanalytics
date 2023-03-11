from sqlalchemy import Column, String, MetaData, Table, ForeignKey,Integer
from database.connection.connection import connection
from database.entities.scrapJobSchema.jobs import Jobs

engine, base, session = connection()

metadata = MetaData()

JobsDescriptions = Table(
    'jobs_description',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True),
    Column("id_job",Integer,ForeignKey(Jobs.columns.id)),
    Column("text",String(15000),nullable=False),
    schema = 'scrap_job'
)

metadata.create_all(engine)