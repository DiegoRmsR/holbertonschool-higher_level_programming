#!/usr/bin/python3
"""
cript that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    query = db.cursor()
    query.execute("SELECT * FROM states WHERE name LIKE %s\
                  ORDER BY id ASC;", (sys.argv[4]))
    states = query.fetchall()
    for state in states:
        print(state)
    query.close()
    db.close()
