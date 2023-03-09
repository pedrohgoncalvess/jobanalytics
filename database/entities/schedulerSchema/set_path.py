from sqlalchemy import Column,Integer,String, MetaData, Table, ForeignKey
from database.connection.connection import connection

engine, base, session = connection()

metadata = MetaData()

setPath = Table(
    'set_path',
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("stage_scrap",String(20),nullable=False, unique=True),
    Column("site_scrap",String(25), nullable=False),
    schema = 'scrap_scheduler'
)

metadata.create_all(engine)