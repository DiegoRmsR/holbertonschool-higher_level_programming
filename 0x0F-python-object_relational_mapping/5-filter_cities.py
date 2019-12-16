#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    query = db.cursor()
    query.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON states.id = cities.state_id WHERE states.name = %s
    ORDER BY cities.id ASC;", (sys.argv[4],))
    states = query.fetchall()

    print(", ".join([state[1] for state in states]))
    query.close()
    db.close()
