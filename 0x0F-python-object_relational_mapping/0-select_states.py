#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa:
# Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)