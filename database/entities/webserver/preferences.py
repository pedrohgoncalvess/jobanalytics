from sqlalchemy import Column, String, MetaData, Table,Integer
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

PreferencesUser = Table(
    'preferences',
    metadata,
    Column("id",Integer,autoincrement=True,primary_key=True),
    Column("tecnologie",String(50),nullable=False),
    Column("type",String(30),nullable=False),
    schema = 'web_server'
)

metadata.create_all(engine)