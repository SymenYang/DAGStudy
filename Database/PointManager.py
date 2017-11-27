import KnowledgePoint as KP
import Problem as PR
import Score as SC
import Target as TA
import UserDatabase as US
import Graph as GR
import Link as LI



def changeNI(ID,name,introduction):
    newName = raw_input("please input new name.The previous one is %s" %name)
    newIntro = raw_input("please input new introduction,The previous one is %s" %introduction)
    KP.changePoint(ID,newName,newIntro)
    return 0


def dealProblem(ID):
    while True:
        print """    1.list problems
    2.delete a problem
    3.add a problem
    4.change a problem
    0.quit"""
        p = PR.getProblem(ID)
        command = raw_input("please input the number(0~4):")
        if command == "0":
            break
        if command == "1":
            l = len(p)
            for j in range(0,l,1):
                print "%d" %j + " : " + p[j][2] + "," + p[j][3] + "," + p[j][4] + "," + p[j][5] + "," + p[j][6] + "," + "%d" %p[j][7]
        if command == "2":
            number = int(raw_input("input the ID you want to delete:"))
            PR.deleteProblem(p[number][0])
        if command == "3":
            text = raw_input("input the text:")
            textA = raw_input("input the text of option A:")
            textB = raw_input("input the text of option B:")
            textC = raw_input("input the text of option C:")
            textD = raw_input("input the text of option D:")
            answer = 5
            while answer < 1 or answer > 4:
                answer = int(raw_input("input the answer (1~4):"))
            PR.addProblem(ID,text,textA,textB,textC,textD,answer)
        if command == "4":
            number = int(raw_input("input the ID you want to change:"))
            text = raw_input("input the text:")
            textA = raw_input("input the text of option A:")
            textB = raw_input("input the text of option B:")
            textC = raw_input("input the text of option C:")
            textD = raw_input("input the text of option D:")
            answer = 5
            while answer < 1 or answer > 4:
                answer = int(raw_input("input the answer (1~4):"))
            PR.changeProblem(p[number][0],ID,text,textA,textB,textC,textD,answer)
    return 0


def dealLink(ID):
    while True:
        print """    1.list links
       2.delete a link
       3.add a link
       0.quit"""
        L = LI.getLink(ID)
        command = raw_input("please input the number(0~3):")
        if command == "0":
            break
        if command == "1":
            l = len(L)
            for j in range(0,l,1):
                print "%d:" %j + L[j][2]
        if command == "2":
            number = int(raw_input("input the ID you want to delete:"))
            LI.deleteLink(L[number][0])
        if command == "3":
            link = raw_input("please input the link you want add:")
            LI.addLink(ID,link)
    return 0


def deletePoint(ID):
    if ID == 1:
        print "you can't delete the root point"
        return 0
    KP.deletePoint(ID)
    return 0


def createPoint():
    name = raw_input("please input point name:")
    intro = raw_input("please input point introduction:")
    KP.insertPoint(name,intro)
    return 0


def changePoint(ID):
    nID = int(raw_input("please input the ID:"))
    p = KP.getKnowledgeInfo(nID)
    if len(p) == 0:
        print "point not exist"
    else:
        return nID
    return ID


def listPoint():
    list = KP.getAllKnowledgePoint()
    l = len(list)
    for j in range(0,l,1):
        print "%d:" %list[j][0] + list[j][1]
    return 0


def addRelation():
    prev = int(raw_input("please input the prev ID:"))
    nex = int(raw_input("please input the next ID:"))
    KP.insertRelation(prev,nex)
    return 0

def display(CKLID):
    print "Current Knowledge Point %d" %CKLID
    cinfo = KP.getKnowledgeInfo(CKLID)
    print cinfo[0][0]
    print cinfo[0][1]
    print "select list command:"
    print """    1.Change this knowledge point's name&info
    2.deal this knowledge point's problem
    3.deal this knowledge point's link
    4.delete this knowledge point
    5.create a new knowledge point
    6.change to another knowledge point
    7.list all knowledge point
    8.add a relation
    0.quit"""
    command = raw_input("please input the number(0~7):")
    if command == '1':
        changeNI(CKLID,cinfo[0][0],cinfo[0][1])
        return CKLID
    if command == '2':
        dealProblem(CKLID)
        return CKLID
    if command == '3':
        dealLink(CKLID)
        return CKLID
    if command == '4':
        deletePoint(CKLID)
        return 1
    if command == '5':
        createPoint()
        return CKLID
    if command == '6':
        CKLID = changePoint(CKLID)
        return CKLID
    if command == '7':
        listPoint()
        return CKLID
    if command == '8':
        addRelation()
        return CKLID
    if command == '0':
        print "Bye~"
        return 0
    print "please input correctly"
    return 1


if __name__ == '__main__':
    CKLID = 1
    KP.loadGraph()
    while (1):
        CKLID = display(CKLID)
        if CKLID == 0:
            break

