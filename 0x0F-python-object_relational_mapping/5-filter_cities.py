#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa:
 Your script should take 3 arguments: mysql username, mysql password
 and database name (no argument validation needed) """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities JOIN states
                ON cities.state_id= states.id
                WHERE states.name = (%s)
                ORDER BY cities.id""", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
