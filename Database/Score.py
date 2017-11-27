import DatabaseExc as DB

def submitScore(userName,knowID,score):
    command = """INSERT INTO userRecord(userName,knowledgeID,score)
                 VALUES ('%s',%d,%d)""" %(userName,knowID,score)
    DB.execDB(command)
    print "submit success"
    return 0


def getAllScore(userName):
    command = """SELECT knowledgeID,score
                 FROM userRecord
                 WHERE userName = '%s'""" %userName
    ret = DB.execDB(command)
    return ret