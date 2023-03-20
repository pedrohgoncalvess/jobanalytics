from sqlalchemy import Column,Integer,String, MetaData, Table
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

topicSearch = Table(
    'topic_search',
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("topic_search",String(50),nullable=False,unique=True),
    Column("topic_classification",String(10), nullable=False),
    schema='scrap_scheduler'
)

metadata.create_all(engine)