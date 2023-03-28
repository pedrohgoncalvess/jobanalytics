if __name__ == "__main__":
    resp = input("Write command => [database, scrap, scheduler, standby, constructor]: ")
    if resp.lower() == 'database':
        from database.connection.connection import checkTables
        checkTables()
    elif resp.lower() == 'scrap':
        from database.operations.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
        from sitesScrap.linkedin.testLinkedin import _mainFunctionScheduler
        _mainFunctionScheduler()
        respScrap = input("Choose site for realize scrap => [linkedin, indeed]: ")
        if respScrap.lower() == 'linkedin':
            from sitesScrap.linkedin.scrapLinkedin import scrapInfosJobs
            scrapInfosJobs()
        elif respScrap.lower() == 'indeed':
            from sitesScrap.indeed.scrapIndeed import scrapLinks
            scrapLinks()
    elif resp.lower() == 'scheduler':
        from sitesScrap.linkedin.testLinkedin import _mainFunctionScheduler
        _mainFunctionScheduler()
    elif resp.lower() == 'standby':
        from database.operations.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
        respStandby = input("Choose site get links => [linkedin, indeed]: ")
        if respStandby.lower() == 'linkedin':
            from sitesScrap.linkedin.getLinkLinkedin import getLinksTopics
            getLinksTopics()
        elif respStandby.lower() == 'scrap':
            from sitesScrap.indeed.getLinkIndeed import getLinksIndeed
            getLinksIndeed()
    elif resp.lower() == 'constructor':
        from database.operations.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
    else:
        from database.connection.connection import checkTables
        checkTables()
        from database.operations.__constructor__ import _mainInitConstructor
        _mainInitConstructor()
        from sitesScrap.linkedin.testLinkedin import _mainFunction
        _mainFunction()
        from sitesScrap.linkedin import getLinksTopics
        getLinksTopics()
        from sitesScrap.linkedin import scrapInfosJobs
        scrapInfosJobs()