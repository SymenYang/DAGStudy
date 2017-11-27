import MySQLdb as DB

def execDB(command):
    con = DB.connect("localhost", "root", "129", "DAGStudy")
    cursor = con.cursor()
    con.set_character_set('utf8')
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    ret = 0
    try:
        cursor.execute(command)
        con.commit()
        ret = cursor.fetchall()
        return ret
    except DB.Error, e:
        print "Error %d : %s" % (e.args[0], e.args[1])
    return 0
