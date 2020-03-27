#!/usr/bin/python3

"""Script that lists all states with a name starting with N
"""
import sys

if len(sys.argv) > 3:
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
