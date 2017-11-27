import KnowledgePoint as KP
import Problem as PR
import Score as SC
import Target as TA
import UserDatabase as US
import Graph as GR
import Link as LI

def addPoint(list):
    KP.insertPoint(list[1],list[2])
    return 0


def addProblem(list,CID):
    PR.addProblem(CID,list[1],list[2],list[3],list[4],list[5],int(list[6]))
    return 0


def addLink(list,CID):
    LI.addLink(CID,list[1])
    return 0


def addRelation(list,CID):
    KP.insertRelation(int(list[1]),CID)
    return 0

filename = raw_input("filename:")
fd = open(filename)
nowpoint = 1
KP.loadGraph()
for line in fd:
    p = line.split(',')
    if p[0] == "POINT":
        addPoint(p)
        nowpoint = nowpoint + 1
    if p[0] == "PROBLEM":
        addProblem(p,nowpoint - 1)
    if p[0] == "LINK":
        addLink(p,nowpoint - 1)
    if p[0] == "RELATION":
        addRelation(p,nowpoint - 1)
print "finish"