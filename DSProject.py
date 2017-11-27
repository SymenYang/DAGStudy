from flask import Flask, render_template, session, redirect, url_for, escape, request, jsonify
import Database.Graph as GR
import Database.KnowledgePoint as KP
import Database.Link as LI
import Database.Problem as PR
import Database.UserDatabase as US
import Database.Target as TA
import Database.Score as SC
import json
import DAG
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/api/login', methods=['POST'])
def login():
    """
    Login function.
    add session.
    return 0 if 'login success';
    return 1 if 'no such user';
    return 2 if 'password error';
    """
    p = json.loads(request.data)
    name = p["username"]
    pwd = p["password"]
    ret = US.Login(name, pwd)
    if ret == 0:
        session['logged'] = "1"
        session['username'] = name
        return "0"
    if ret == 1:
        return "1"
    if ret == 2:
        return "2"
    return ""


@app.route('/api/getName',methods=['GET'])
def getName():
    if session.has_key('username'):
        return session['username']
    else:
        return "Login"

#TEST Function
@app.route('/test')
def test():
    return render_template("testTransition.html")

@app.route('/api/test',methods=['POST'])
def apiTest():
    p = json.loads(request.data)
    #q = json.loads(p['Data'])
    ret = {"TEST" : "5","Just test" : "hahaha"}
    return jsonify(ret)

@app.route('/api/logout')
def logout():
    session.pop('username', None)
    return "0"


@app.route('/api/register',methods=['POST'])
def register():
    p = json.loads(request.data)
    name = p["username"]
    pwd = p["password"]
    ret = US.register(name,pwd)
    if ret == 0:
        session['username'] = name
        return "0"
    if ret == 1:
        return "1"
    return ""


@app.route('/api/getDAG',methods = ['POST'])
def getDAG():
    p = json.loads(request.data)
    name = p["username"]
    Map = DAG.getAllKnowledgePoint(name)
    return jsonify(Map)


@app.route('/api/getRelation')
def getRelatio():
    MAP = DAG.getAllKnowledgePoint("Login")
    Edge = DAG.getAllRelation(MAP)
    return jsonify(Edge)


@app.route('/api/getPointInfo',methods=['POST'])
def getPointInfo():
    p = json.loads(request.data)
    ID = p["ID"]
    return KP.getKnowledgeInfo(ID)[0][1]


@app.route('/api/setTarget',methods=['POST'])
def setTarget():
    p = json.loads(request.data)
    ID = p["ID"]
    name = session['username']
    TA.addTarget(name,ID)
    return "0"


@app.route('/api/getProblems',methods = ['POST'])
def getProblems():
    p = json.loads(request.data)
    ID = p["ID"]
    problist = PR.getProblem(ID)
    l = len(problist)
    ret = []
    for i in range(0,l,1):
        ret.append({
                    "ID" : i,
                    "text" : problist[i][2],
                    "textA" : problist[i][3],
                    "textB" : problist[i][4],
                    "textC" : problist[i][5],
                    "textD" : problist[i][6],
                    "answer" : problist[i][7]})
    return jsonify(ret)

@app.route('/api/getCanLearn',methods = ['POST'])
def getCanLearn():
    p = json.loads(request.data)
    ID = p["ID"]
    name = session['username']
    ret = KP.canLearn(ID,name)
    if ret == 0:
        return "0" #can learn
    else:
        return "1" #can not


@app.route('/api/getLinks',methods = ['POST'])
def getLinks():
    p = json.loads(request.data)
    ID = p["ID"]
    list = LI.getLink(ID)
    l = len(list)
    ret = []
    for i in range(0,l,1):
        ret.append({"link" : list[i][0]})

    return jsonify(ret)


@app.route('/api/submitScore',methods = ['POST'])
def submitScore():
    p = json.loads(request.data)
    ID = p["ID"]
    score = p["score"]
    name = session['username']
    SC.submitScore(name,ID,score)
    return "%d" % score


@app.route('/')
def index():
#    session['username'] = "Login"
    return render_template("index.html")


if __name__ == '__main__':
    KP.loadGraph()
    app.run(host='0.0.0.0')
