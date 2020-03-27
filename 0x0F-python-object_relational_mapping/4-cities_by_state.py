#!/usr/bin/python3

"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 3:
        import MySQLdb

        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=db_name, charset="utf8")
        cur = conn.cursor()
        cur.execute("""
            SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id
        """)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
