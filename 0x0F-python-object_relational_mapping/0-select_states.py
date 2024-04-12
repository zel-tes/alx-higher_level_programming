#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", port=3306, password="root/root", database="hbtn_0e_0_usa")
cursor = db.cursor()
cursor.execute("SELECT states.id, states.name FROM states ORDER BY states.id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)
