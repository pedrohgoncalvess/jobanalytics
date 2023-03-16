from database.connection.connection import checkTables

if __name__ == "__main__":
    checkTables()
    from sitesScrap.testLinkedin import _mainFunction
    _mainFunction()
    from sitesScrap.linkedin import scrapInfosJobs
    scrapInfosJobs()