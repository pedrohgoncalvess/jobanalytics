from database.connection.connection import connection
from sqlalchemy import func
from sqlalchemy import insert
from configsDir.colors import colors

engine, base, session = connection(messages='off')

def testInsertSchedulerSchemaPathSiteTable():

    from database.entities.paths_fields.paths import sitesPaths
    from database.entities.paths_fields.set_path import setPath



    testInfoexpected = 'testInfo'

    setPathDict = {
        'nameSet':'linke_1115',
        'siteScrap':'linkedin'
    }

    sitePathDict = {
        'typeComponent':'testeComponent',
        'typeInfo':testInfoexpected,
        'path':'05158gwgbwobgw050518'
    }


    insertSet = insert(setPath).values(
        name_set=setPathDict['nameSet'].lower(),
        site_scrap=setPathDict['siteScrap'].lower(),
    )
    session.execute(insertSet)

    results = session.query(setPath, func.max(setPath.columns.id)).values(setPath.columns.id)
    for line in results:
        a = line.id

    insertPath = insert(sitesPaths).values(
        id_set=a,
        type_component=sitePathDict.get('typeComponent'),
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
    from database.entities.paths_fields.set_path import setPath

    testNameSet = 'linkPath1'

    setPathDict = {
        'nameSet':testNameSet,
        'siteScrap':'linkedin'
    }

    insertSet = insert(setPath).values(
    name_set = setPathDict['nameSet'].lower(),
    site_scrap = setPathDict['siteScrap'].lower(),
    )
    session.execute(insertSet)
    results = session.query(setPath).all()
    for result in results:
        expected = result.name_set
    session.rollback()

    try:
        assert testNameSet.lower() == expected
        print(f"{colors('green')}Test testInsertSchedulerSchemaSetPath passed")
    except:
        print(f"{colors('red')}Test testInsertSchedulerSchemaSetPath error")



