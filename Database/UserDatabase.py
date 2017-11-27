import MySQLdb as DB

def register(name,pwd):
    con = DB.connect("localhost","root","129","DAGStudy")
    cursor  = con.cursor()
    srch_usr = """SELECT name 
                  FROM user
                  WHERE name = '%s'  """ % name
    cursor.execute(srch_usr)
    ret = cursor.fetchall()
    if len(ret) == 0:
        add_usr = """INSERT INTO user VALUE('%s','%s')""" %(name,pwd)
        cursor.execute(add_usr)
        con.commit()
        print "registe success"
    else:
        print "user already exists"
        return 1
    return 0


def Login(name,pwd):
    con = DB.connect("localhost","root","129","DAGStudy")
    cursor  = con.cursor()
    srch_usr = """SELECT name,password 
                  FROM user
                  WHERE name = '%s'  """ % name
    cursor.execute(srch_usr)
    ret = cursor.fetchall()
    if len(ret) != 1:
        print "no such user"
        return 1
    else:
        if pwd != ret[0][1]:
            print "password error"
            return 2
        else:
            print "%s login success" % name
            return 0


def changePassword(name,pwd,npwd):
    con = DB.connect("localhost","root","129","DAGStudy")
    cursor  = con.cursor();
    srch_usr = """SELECT name,password 
                  FROM user
                  WHERE name = '%s'  """ % name
    cursor.execute(srch_usr)
    ret = cursor.fetchall()
    if len(ret) != 1:
        print "no such user"
        return 1
    else:
        if pwd != ret[0][1]:
            print "password error"
            return 2
        else:
            chng_pwd = """UPDATE user 
                          SET password = '%s'
                          WHERE name = '%s'""" %(npwd,name)
            cursor.execute(chng_pwd)
            con.commit()
            print "changed success"
            return 0

