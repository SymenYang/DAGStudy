import Database.KnowledgePoint as KP
import Database.Score as SC
import Database.Target as TA
import Database.Graph as GR
def getAllKnowledgePoint(userName):
    points = KP.getAllKnowledgePoint()
    ret = []
    l = len(points)
    for i in range(0,l,1):
        ret.append({ "ID":points[i][0] , "name" : points[i][1], "proc" : 0, "type" : 0})
    if userName == "Login":
        return ret
    else:
        tgr = TA.getTarget(userName)
        Gra = GR.graph()
        tl = len(tgr)
        for i in range(0,tl,1):
            li = Gra.getPrevPoint(tgr[i][0])
            ll = len(li)
            for j in range(0,ll,1):
                for k in range(0,l,1):
                    if ret[k]["ID"] == li[j]:
                        ret[k]["type"] = 1
                        break
        sco = SC.getAllScore(userName)
        sl = len(sco)
        for i in range(0,sl,1):
            for j in range(0,l,1):
                if ret[j]["ID"] == sco[i][0]:
                    ret[j]["proc"] = max(ret[j]["proc"],sco[i][1])
                    break
    return ret

def getAllRelation(points):
    rel = KP.getAllRelation()
    l = len(rel)
    ret = []
    pl = len(points)
    for i in range(0,l,1):
        target = 0
        source = 0
        for j in range(0,pl,1):
            if points[j]["ID"] == rel[i][1]:
                source = j
            if points[j]["ID"] == rel[i][2]:
                target = j
        ret.append({"source" : source,"target" : target})
    return ret