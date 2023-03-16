from database.connection.connection import checkTables

if __name__ == "__main__":
    checkTables()
    from database.operations.schedulerSchema.__constructor__ import _mainInit
    _mainInit()
    from sitesScrap.testLinkedin import _mainFunction
    _mainFunction()
    from sitesScrap.linkedin import scrapInfosJobs
    scrapInfosJobs()