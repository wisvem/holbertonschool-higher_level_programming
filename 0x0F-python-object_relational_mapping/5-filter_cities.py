#!/usr/bin/python3
"""Conn module"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    myU = argv[1]
    myP = argv[2]
    myDB = argv[3]
    sName = argv[4]
    myH = "localhost"
    db = MySQLdb.connect(host=myH, port=3306, user=myU, passwd=myP, db=myDB)
    cur = db.cursor()
    myQ = "SELECT c.name FROM cities AS c, states AS s "
    myQ += "WHERE s.name = %s AND s.id = c.state_id ORDER BY c.id;"
    cur.execute(myQ, (sName,))
    result = cur.fetchall()
    if (len(result) is not 0):
        for row in result:
            for col in row:
                if (result.index(row) is len(result) - 1):
                    print(col)
                else:
                    print(col, end=', ')
    else:
        print()
    cur.close()
    db.close()
