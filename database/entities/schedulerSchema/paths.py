from sqlalchemy import Column,Integer,String, MetaData, Table, ForeignKey
from database.connection.connection import connection
from database.entities.schedulerSchema.set_path import setPath

engine, base, session = connection()

metadata = MetaData()

sitesPaths = Table(
    'paths_sites',
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("id_set",Integer,ForeignKey(setPath.columns.id)),
    Column("type_component",String(25),nullable=False),
    Column("type_info",String(20),nullable=False),
    Column("path",String(1000), nullable=False, unique=True),
    schema='scrap_scheduler'
)

metadata.create_all(engine)