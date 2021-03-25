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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id;", (sName,))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
