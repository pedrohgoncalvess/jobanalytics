from database.connection.connection import connection
from sqlalchemy import func
from sqlalchemy import insert
from configsDir.colors import colors

engine, base, session = connection(messages='off')

def testInsertSchedulerSchemaPathSiteTable():

    from database.entities.schedulerSchema.paths import sitesPaths
    from database.entities.schedulerSchema.set_path import setPath



    testInfoexpected = 'testInfo'

    setPathDict = {
        'stageScrap':'linke_1115',
        'siteScrap':'linkedin'
    }

    sitePathDict = {
        'typeInfo':testInfoexpected,
        'path':'05158gwgbwobgw050518'
    }


    insertSet = insert(setPath).values(
        stage_scrap=setPathDict['stageScrap'].lower(),
        site_scrap=setPathDict['siteScrap'].lower(),
    )
    session.execute(insertSet)

    results = session.query(setPath, func.max(setPath.columns.id)).values(setPath.columns.id)
    for line in results:
        a = line.id

    insertPath = insert(sitesPaths).values(
        id_set=a,
        type_info=sitePathDict.get('typeInfo'),
        path=sitePathDict.get('path')
    )
    session.execute(insertPath)
    results = session.query(sitesPaths).all()
    for result in results:
        expected = result.type_info
    session.rollback()

    try:
        assert testInfoexpected == expected
        print(f"{colors('green')}Test testInsertSchedulerSchemaPathSiteTable passed")
    except:
        print(f"{colors('red')}Test testInsertSchedulerSchemaPathSiteTable error")


def testInsertSchedulerSchemaSetPath():
    from database.entities.schedulerSchema.set_path import setPath

    testNameSet = 'linkPath1'

    setPathDict = {
        'stageScrap':testNameSet,
        'siteScrap':'linkedin'
    }

    insertSet = insert(setPath).values(
    stage_scrap = setPathDict['stageScrap'].lower(),
    site_scrap = setPathDict['siteScrap'].lower(),
    )
    session.execute(insertSet)
    results = session.query(setPath).all()
    for result in results:
        expected = result.stage_scrap
    session.rollback()

    try:
        assert testNameSet.lower() == expected
        print(f"{colors('green')}Test testInsertSchedulerSchemaSetPath passed")
    except:
        print(f"{colors('red')}Test testInsertSchedulerSchemaSetPath error")



