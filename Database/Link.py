import DatabaseExc as DB

def getLink(knowID):
    command = """SELECT target
                 FROM link
                 WHERE knowledgeID = %d""" %knowID
    ret = DB.execDB(command)
    return ret

def addLink(knowID,link):
    command = """INSERT INTO link(knowledgeID,target)
                 VALUES(%d,'%s')""" %(knowID,link)
    DB.execDB(command)
    print "link added"
    return 0

def deleteLink(ID):
    command = """DELETE
                 FROM link
                 WHERE ID = %d""" %ID
    DB.execDB(command)
    print "link deleted"
    return 0