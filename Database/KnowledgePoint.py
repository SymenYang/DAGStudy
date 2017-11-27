import DatabaseExc as DB
import Graph as GR
import Problem as PR

def insertPoint(name,intro):
    command = """INSERT INTO knowledgePoint(name,introduction)
                 VALUES('%s','%s')""" %(name,intro)
    DB.execDB(command)
    command = """SELECT MAX(ID)
                 FROM knowledgePoint"""
    p = DB.execDB(command)
    a = GR.graph()
    a.addPoint(int(p[0][0]))
    print "insert point success"
    return 0

def deletePoint(ID):
    command = """DELETE
                 FROM knowledgeRelation
                 WHERE preID = %d or nextId = %d""" %(ID,ID)
    DB.execDB(command)

    command = """DELETE
                 FROM problem
                 WHERE knowledgeID = %d""" %ID
    DB.execDB(command)

    command = """DELETE
                 FROM link
                 WHERE knowledgeID = %d""" %ID
    DB.execDB(command)

    command = """DELETE
                 FROM knowledgePoint
                 WHERE ID = %d""" %ID
    DB.execDB(command)
    print "delete point %d success" % ID
    return 0

def changePoint(ID,name,intro):
    command = """UPDATE knowledgePoint
                 SET name = '%s',introduction = '%s'
                 WHERE ID = %d""" %(name,intro,ID)
    DB.execDB(command)
    print "change point %d success" % ID
    return 0

def loadGraph():
    gra = GR.graph()
    command = """SELECT * 
                 FROM knowledgePoint"""
    points = DB.execDB(command)
    l = len(points)
    for i in range(0,l,1):
        gra.addPoint(points[i][0])
    command = """SELECT * 
                 FROM knowledgeRelation"""
    edges = DB.execDB(command)
    l = len(edges)
    for i in range(0,l,1):
        gra.addEdge(edges[i][1],edges[i][2])
    print "here"

def insertRelation(prev,nex):
    gra = GR.graph()
    if gra.testEdge(prev,nex) == 0:
        command = """INSERT INTO knowledgeRelation(preID,nextID)
                     VALUES (%d,%d)""" %(prev,nex)
        DB.execDB(command)
        print "insert %d to %d success" %(prev,nex)
        return 0
    print "edge not obey the rule"
    return 1

def getAllRelation():
    command = """SELECT * FROM knowledgeRelation"""
    ret = DB.execDB(command)
    return ret

def getAllKnowledgePoint():
    command = """SELECT ID,name
                 FROM knowledgePoint"""
    ret = DB.execDB(command)
    return ret

def getKnowledgeInfo(ID):
    command = """SELECT name,introduction
                 FROM knowledgePoint
                 WHERE ID = %d""" %ID
    ret = DB.execDB(command)
    return ret

def canLearn(ID,userName):
    command = """SELECT preID
                 FROM knowledgeRelation
                 where nextID = %d""" %ID
    prevList = DB.execDB(command)
    command = """SELECT knowledgeID
                 FROM userRecord
                 WHERE score >= 60 AND userName = '%s'""" %userName
    alrList = DB.execDB(command)
    l = len(prevList)
    l2 = len(alrList)
    for i in range(0,l,1):
        flag = False
        for j in range(0,l2,1):
            if prevList[i] == alrList[j]:
                flag = True
                break
        if not flag:
            return 1
    return 0