if __name__ == "__main__":
    resp = input("Write command => [database, scrap, scheduler, standby, constructor]: ")
    if resp.lower() == 'database':
        from database.connection.connection import checkTables
        checkTables()
    elif resp.lower() == 'scrap':
        from database.operations.schedulerSchema.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
        from sitesScrap.testLinkedin import _mainFunctionScheduler
        _mainFunctionScheduler()
        from sitesScrap.linkedin import scrapInfosJobs
        scrapInfosJobs()
    elif resp.lower() == 'scheduler':
        from sitesScrap.testLinkedin import _mainFunctionScheduler
        _mainFunctionScheduler()
    elif resp.lower() == 'standby':
        from database.operations.schedulerSchema.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
        from sitesScrap.linkedin import getLinksTopics
        getLinksTopics()
    elif resp.lower() == 'constructor':
        from database.operations.schedulerSchema.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
    else:
        from database.connection.connection import checkTables
        checkTables()
        from database.operations.schedulerSchema.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
        from sitesScrap.testLinkedin import _mainFunction
        _mainFunction()
        from sitesScrap.linkedin import getLinksTopics
        getLinksTopics()
        from sitesScrap.linkedin import scrapInfosJobs
        scrapInfosJobs()