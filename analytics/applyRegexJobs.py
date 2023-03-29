import psycopg2
import pandas as pd

def connectionWithDb():
    connect = psycopg2.connect("dbname=jobscrap user=postgres password=fodao002")
    conn = connect.cursor()
    return conn

def prepareDataFrames():
    conn = connectionWithDb()
    try:
        conn.execute("""select jb.id,jb.vacancy_title,jb.researched_topic,jb.site_job, jb.vacancy_title || ' ' || jd.text from scrap_job.job jb
                              inner join scrap_job.job_description jd on jd.id_job = jb.id
                              where jd.status = 'waiting'
                              """)
        discDf = pd.DataFrame(conn.fetchall())
        discDf.rename(columns={0: "ID",
                               1: "Titulo da vaga",
                               2: "Topico pesquisado",
                               3: "Site",
                               4: "Description"
                               }, inplace=True)


        conn.execute("select * from dataset_schema.tecnologies_info")
        tecDf = pd.DataFrame(conn.fetchall())
        tecDf.rename(columns={0: "ID",
                              1: "Tecnologie",
                              2: "Type"}, inplace=True)
        conn.execute("""
                    select * from dataset_schema.job_info
        """)
        dfInfo = pd.DataFrame(conn.fetchall())
        dfInfo.rename(columns={0: "ID",
                               1: "Info",
                               2: "Type"
                               }, inplace=True)

        conn.close()
        return discDf,tecDf,dfInfo
    except Exception as err:
        print(err)
        conn.close()


def listPunctationFunc():
    from string import punctuation
    listPunctation: list = []
    for ponto in punctuation:
        if ponto == '#' or ponto == '+':
            pass
        else:
            listPunctation.append(ponto)
    return listPunctation


def columnTreatment1():
    import unidecode
    discDf, tecDf, dfInfo = prepareDataFrames()

    newColumn: list = []
    for disc in discDf.Description:
        disc = disc.lower()
        disc = unidecode.unidecode(disc)
        disc = disc.replace("\n\n", " ")
        disc = disc.replace("\n", " ")
        disc = disc.replace("/"," ")
        newColumn.append(disc)
    discDf['Treatment1'] = newColumn

    return discDf


def columnTreatment2():
    stacksList = ['programming language', 'framework', 'database', 'planning and management', 'data', 'other']
    discDf, tecDf, dfInfo = prepareDataFrames()

    listPunctation = listPunctationFunc()
    discDf = columnTreatment1()

    for stack in stacksList:
        listTecnologies = list(tecDf.Tecnologie.loc[tecDf['Type'] == stack])
        tecCount = 0
        newColumn: list = []
        for disc in discDf.Treatment1:
            vetorize = disc.split(" ")
            newVetor: list = []
            for word in vetorize:
                word = word.replace(" ", "")
                for pnt in listPunctation:
                    word = word.replace(pnt, "")
                newVetor.append(word)

            listColumn: list = []

            for wordT in newVetor:
                if wordT in listTecnologies:
                    tecCount += 1
                    if wordT not in listColumn:
                        listColumn.append(wordT)

            for tec in listTecnologies:
                if tec.find(" ") != -1:
                    if disc.find(tec) != -1:
                        tecCount += 1
                        listColumn.append(tec)
            newColumn.append(str(listColumn).replace("[", "").replace("]", "").replace("'", ""))

        discDf[stack] = newColumn
        print(f"{stack} counter number:{str(tecCount)}")
    return discDf


def listaBenef():
    discDf, tecDf, dfInfo = prepareDataFrames()
    dfJob = columnTreatment2()
    listInfos = ['benefit', 'culture', 'model', 'requirement', 'seniority']
    for typeinfo in listInfos:
        newColumn: list = []
        benefCount = 0
        for line in dfJob.Treatment1:
            newLineColumn: list = []
            for info in dfInfo.Info.loc[dfInfo['Type'] == typeinfo]:
                if line.find(info) != -1:
                    if info not in newLineColumn:
                        newLineColumn.append(info)
                        benefCount += 1
            newColumn.append(str(newLineColumn).replace("[", "").replace("]", "").replace("'", ""))
        dfJob[typeinfo] = newColumn

        print(f"{typeinfo} counter number:{str(benefCount)}")

    return dfJob


def parseColumns():
    df = listaBenef()
    from database.operations.analyticsSchema.analytic_description import insertInfoDescription

    columns = ['programming language', 'framework', 'database', 'planning and management', 'data', 'other', 'benefit',
               'culture', 'model', 'requirement', 'seniority']

    for column in columns:
        for num, line in enumerate(list(df[column])):
            if len(line) > 0:
                lineDict = {}
                infos = line.split(',')
                for info in infos:
                    idLine = df['ID'].iloc[num]
                    idLine = str(idLine)
                    info = info.replace(" ", "")
                    lineDict.update({"id_job": idLine, "info": info, "type": column, "compost_key": f"{idLine}-{info}"})
                    insertInfoDescription(lineDict)

parseColumns()