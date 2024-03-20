#!/usr/bin/python3

'''script that list all states from the database hbtn_0e_0_usa'''

if __name__ == "__main__":
    import MySQLdb
    import sys

    connect = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )
    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    results = cur.fetchall()
    for result in results:
        print(result)

    cur.close()
    connect.close()
