from database.connection.connection import checkTables

if __name__ == "__main__":
    resp = input("Write command: ")
    if resp.lower() == 'database':
        from database.connection.connection import checkTables
        checkTables()
    elif resp.lower() == 'scrap':
        from database.operations.schedulerSchema.__constructor__ import _mainInit
        _mainInit()
        from sitesScrap.testLinkedin import _mainFunction
        _mainFunction()
        from sitesScrap.linkedin import scrapInfosJobs
        scrapInfosJobs()
    else:
        from database.connection.connection import checkTables
        checkTables()
        from database.operations.schedulerSchema.__constructor__ import _mainInit
        _mainInit()
        from sitesScrap.testLinkedin import _mainFunction
        _mainFunction()
        from sitesScrap.linkedin import getLinksTopics
        getLinksTopics()
        from sitesScrap.linkedin import scrapInfosJobs
        scrapInfosJobs()