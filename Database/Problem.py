import DatabaseExc as DB

def addProblem(knowID,text,textA,textB,textC,textD,ans):
    command = """INSERT INTO problem(knowledgeID,text,textA,textB,textC,textD,answer)
                 VALUES (%d,'%s','%s','%s','%s','%s',%d)""" %(knowID,text,textA,textB,textC,textD,ans)
    DB.execDB(command)
    print "add problem success"
    return 0

def deleteProblem(ID):
    command = """DELETE 
                 FROM problem
                 WHERE ID = %d""" %ID
    DB.execDB(command)
    "delete problem success"
    return 0

def getProblem(knowID):
    command = """SELECT *
                 FROM problem
                 WHERE knowledgeID = %d""" %knowID
    ret = DB.execDB(command)
    print "got Problem"
    return ret

def changeProblem(ID,knowID,text,textA,textB,textC,textD,ans):
    command = """UPDATE problem
                 SET knowledgeID = %d,text = '%s',textA = '%s',textB = '%s',textC = '%s',textD = '%s',answer = %d
                 WHERE ID = %d""" %(knowID,text,textA,textB,textC,textD,ans,ID)
    ret = DB.execDB(command)
    print "changed"
    return 0