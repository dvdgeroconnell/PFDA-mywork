# viewmysql.py
#
# Lab 08.03
#
# # David O'Connell, 17/11/2024

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="wsaa_lab")

cur = connection.cursor()
#sql = "SELECT * FROM student WHERE id = %s"
#values = (1,)
#cur.execute(sql, values)

sql = "SELECT * FROM student"
cur.execute(sql)


result = cur.fetchall()
for x in result:
    print(x)

cur.close()
connection.close()