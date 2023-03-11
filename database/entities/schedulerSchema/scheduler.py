from sqlalchemy import Column,Integer,String, MetaData, Table, ForeignKey, Date
from sqlalchemy import func
from database.connection.connection import connection
from database.entities.schedulerSchema.paths import sitesPaths

engine, base, session = connection()

metadata = MetaData()

schedulerScrap = Table(
    'scheduler',
    metadata,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("id_path",Integer,ForeignKey(sitesPaths.columns.id)),
    Column("tested_at",Date,server_default=func.now()),
    schema='scrap_scheduler'
)

metadata.create_all(engine)