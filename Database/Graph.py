class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class edge:
    come = 0
    to = 0
    type = True
    nextEdge = 0

    def __init__(self,com,t,typ,nex):
        self.come = com
        self.to = t
        self.type = typ
        self.nextEdge = nex
        return

class point:
    id = 0
    head  = -1

    def __init__(self,nid):
        self.id = nid
        return

class graph(Singleton):
    trans = {}
    retrans = {}
    pointArr = {}
    edgeArr = {}
    pointCnt = 0
    edgeCnt = 0
    lastToHead = 0
    lastComHead = 0
    visited = {}
    deep = {}
    queue = []
    calcDeep = False
    hasInstance = False

    def __init__(self):
        return


    def addPoint(self,t):
        self.trans[t] = self.pointCnt
        self.retrans[self.pointCnt] = t
        self.pointArr[self.pointCnt] = point(self.pointCnt)
        self.visited[self.pointCnt] = False
        self.pointCnt = self.pointCnt + 1

    def addEdge(self,com,to):
        com = self.trans[com]
        to = self.trans[to]
        a = self.pointArr[com].head
        self.lastComHead = a
        b = self.pointArr[to].head
        self.lastToHead = b
        self.edgeArr[self.edgeCnt] = edge(com, to, True, a)
        self.pointArr[com].head = self.edgeCnt
        self.edgeCnt = self.edgeCnt + 1
        self.edgeArr[self.edgeCnt] = edge(to, com, False, b)
        self.pointArr[to].head = self.edgeCnt
        self.edgeCnt = self.edgeCnt + 1

    def clearVisted(self):
        for i in range(0,self.pointCnt,1):
            self.visited[i] = False

    def dfs(self,nowID):
        self.visited[nowID] = True
        i = self.pointArr[nowID].head
        while i != -1:
            q = self.edgeArr[i].to
            t = self.edgeArr[i].type
            if t:
                if self.visited[q]:
                    return False
                else:
                    f = self.dfs(q)
                    if not f:
                        return False
            i = self.edgeArr[i].nextEdge
        self.visited[nowID] = False
        return True

    def removeLastEdge(self):
        if self.lastComHead == -2:
            return 1
        self.edgeCnt = self.edgeCnt - 2
        com = self.edgeArr[self.edgeCnt].come
        to = self.edgeArr[self.edgeCnt].to
        self.pointArr[com].head = self.lastComHead
        self.pointArr[to].head = self.lastToHead
        self.lastComHead = -2
        self.lastToHead = -2
        return 0

    def dfs2(self,nowID):
        self.visited[nowID] = True
        i = self.pointArr[nowID].head
        while i != -1:
            q = self.edgeArr[i].to
            t = self.edgeArr[i].type
            if not t:
                if not self.visited[q]:
                    f = self.dfs2(q)
            i = self.edgeArr[i].nextEdge
        return

    def getPrevPoint(self,ID):
        ID = self.trans[ID]
        self.clearVisted()
        self.dfs2(ID)
        ret = []
        for i in range(0,self.pointCnt,1):
            if self.visited[i]:
                ret.append(self.retrans[i])
        return ret

    def testEdge(self,come,to):
        self.addEdge(come,to)
        if self.dfs(0):
            self.clearVisted()
            return 0
        else:
            self.removeLastEdge()
            self.clearVisted()
            return 1

