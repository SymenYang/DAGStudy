import DatabaseExc as DB

def addTarget(name,knowID):
    command = """SELECT * 
                 FROM userTarget
                 WHERE userName = '%s' AND targetPoint = %d""" %(name,knowID)
    exis = DB.execDB(command)
    if len(exis) != 0:
        print "target already exist"
        return 1
    command = """INSERT INTO userTarget(userName,targetPoint)
                 VALUES('%s',%d)""" %(name,knowID)
    DB.execDB(command)
    print "add target success"
    return 0

def deleteTarget(name,knowID):
    command = """DELETE
                 FROM userTarget
                 WHERE userName = '%s' AND targetPoint = %d""" %(name,knowID)
    DB.execDB(command)
    print "delete success"
    return 0

def getTarget(name):
    command = """SELECT targetPoint 
                 FROM userTarget
                 WHERE userName = '%s'""" %name
    return DB.execDB(command)
