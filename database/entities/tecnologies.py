from sqlalchemy import Column,Integer,String, MetaData, Table
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

Tecnologies = Table(
    'tecnologies_info',
    metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("tecnologie",String(50),nullable=False, unique=True),
    Column("type",String(50), nullable=False),
)

metadata.create_all(engine)