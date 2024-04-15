#!/usr/bin/python3
''' the main() shows the states in the database "hbtn_0e_0_usa"
in order of their id '''
import MySQLdb
import sys


def main():
    if (len(sys.argv) == 5):
        username = sys.argv[1]
        password = sys.argv[2]
        name = sys.argv[3]
        state_1 = sys.argv[4]
        db = MySQLdb.connect(
                host="localhost",
                port=3306, user=username,
                passwd=password,
                db=name)
        cursor = db.cursor()
        query = '''SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        '''.format(state_1)
        cursor.execute(query, (state_1,))
        rows = cursor.fetchall()

        for i, row in enumerate(rows):
            row_str = f"{row[0]}"
            print(row_str, end=", ")
            if (i == len(rows) - 1):
                print(row_str, end="\n")


if __name__ == "__main__":
    main()
