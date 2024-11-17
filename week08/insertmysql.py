# insertmysql.py
#
# Lab 08.03
#
# # David O'Connell, 17/11/2024

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="wsaa_lab")

cur = connection.cursor()
sql = "INSERT INTO student (name, age) VALUES (%s, %s)"
values = ("Mary",21)
cur.execute(sql, values)

connection.commit()
print("1 record inserted, ID: ", cur.lastrowid)
cur.close()
connection.close()