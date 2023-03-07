from sqlalchemy import Column,Integer,String, MetaData, Table, ForeignKey, Date
from sqlalchemy import func
from database.connection.connection import connection
from database.entities.paths_fields.set_path import setPath

engine, base, session = connection()

metadata = MetaData()

schedulerScrap = Table(
    'scheduler',
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("id_set",Integer,ForeignKey(setPath.columns.id)),
    Column("tested_at",Date,server_default=func.now()),
    schema='scrap_scheduler'
)

metadata.create_all(engine)