from sqlalchemy import Column, String, MetaData, Table,Integer
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

InfoDescription = Table(
    'analytic_description',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True),
    Column("info",String(100),nullable=False),
    Column("type",String(50),nullable=False),
    Column("compost_key",String(100),unique=True, nullable=False),
    schema = 'analytics'
)

metadata.create_all(engine)