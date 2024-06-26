#!/usr/bin/python3
''' the main() shows the states in the database "hbtn_0e_0_usa"
in order of their id '''
import MySQLdb
import sys


def main():
    if (len(sys.argv) == 4):
        username = sys.argv[1]
        password = sys.argv[2]
        name = sys.argv[3]
        db = MySQLdb.connect(
                host="localhost",
                port=3306, user=username,
                passwd=password,
                db=name)
        cursor = db.cursor()
        cursor.execute(''' SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON (states.id = cities.state_id)
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
