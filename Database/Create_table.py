import MySQLdb as DB

try:
    con = DB.connect("localhost","root","129","DAGStudy")
    print "Connect Success"


    crt_usr = """CREATE TABLE user (
                        name VARCHAR(20) NOT NULL,
                        password VARCHAR(20) NOT NULL,
                        PRIMARY KEY(name)
                        )
    """

    crt_knpoint = """CREATE TABLE knowledgePoint(
                      ID INTEGER NOT NULL AUTO_INCREMENT,
                      name VARCHAR(20) NOT NULL,
                      introduction VARCHAR(1000) NOT NULL,
                      PRIMARY KEY(ID)
                      )
    """

    crt_knrltin = """CREATE TABLE knowledgeRelation(
                      ID INTEGER NOT NULL AUTO_INCREMENT,
                      preID INTEGER NOT NULL,
                      nextID INTEGER NOT NULL,
                      PRIMARY KEY (ID),
                      FOREIGN KEY (preID) REFERENCES knowledgePoint (ID),
                      FOREIGN KEY (nextID) REFERENCES knowledgePoint (ID)
                      )"""

    crt_prblm = """CREATE TABLE problem(
                    ID INTEGER NOT NULL AUTO_INCREMENT,
                    knowledgeID INTEGER  NOT NULL,
                    text VARCHAR(1000) NOT NULL,
                    textA VARCHAR(200) NOT NULL,
                    textB VARCHAR(200) NOT NULL,
                    textC VARCHAR(200),
                    textD VARCHAR(200),
                    answer INTEGER NOT NULL,
                    PRIMARY KEY (ID),
                    FOREIGN KEY (knowledgeID) REFERENCES knowledgePoint (ID)
                    )"""

    crt_link = """CREATE TABLE link(
                    ID INTEGER NOT NULL AUTO_INCREMENT,
                    knowledgeID INTEGER NOT NULL,
                    target VARCHAR(256) NOT NULL,
                    PRIMARY KEY (ID)
                  )"""

    crt_usr_trgt = """CREATE TABLE userTarget(
                        ID INTEGER NOT NULL AUTO_INCREMENT,
                        userName VARCHAR(20) NOT NULL,
                        targetPoint INTEGER NOT NULL,
                        PRIMARY KEY (ID),
                        FOREIGN KEY (userName) REFERENCES user(name),
                        FOREIGN KEY (targetPoint) REFERENCES knowledgePoint(ID)
                      )"""

    crt_usr_Rcrd = """CREATE TABLE userRecord(
                        ID INTEGER NOT NULL AUTO_INCREMENT,
                        knowledgeID INTEGER NOT NULL,
                        userName VARCHAR(20) NOT NULL,
                        score INTEGER NOT NULL,
                        PRIMARY KEY (ID),
                        FOREIGN KEY (userName) REFERENCES user(name),
                        FOREIGN KEY (knowledgeID) REFERENCES knowledgePoint(ID)
                      )"""

    crt_table_cur = con.cursor()
    crt_table_cur.execute(crt_usr)
    print "user"
    crt_table_cur.execute(crt_knpoint)
    print "point"
    crt_table_cur.execute(crt_knrltin)
    print "relation"
    crt_table_cur.execute(crt_prblm)
    print "problem"
    crt_table_cur.execute(crt_link)
    print "link"
    crt_table_cur.execute(crt_usr_trgt)
    print "target"
    crt_table_cur.execute(crt_usr_Rcrd)
    print "record"
    con.close()

except DB.Error,e:
    print "Error %d : %s" %(e.args[0],e.args[1])
