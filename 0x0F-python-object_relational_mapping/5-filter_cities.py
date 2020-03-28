#!/usr/bin/python3

"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.name FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id
    """, (state_name, ))
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        if (i != len(query_rows) - 1):
            print(query_rows[i][0], end=', ')
        else:
            print(query_rows[i][0])
    cur.close()
    conn.close()
