#!/usr/bin/python3

"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 4:
        import MySQLdb

        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_searched = sys.argv[4]

        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=db_name, charset="utf8")
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM states
            WHERE name = %s
            ORDER BY states.id""", (state_searched, ))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
