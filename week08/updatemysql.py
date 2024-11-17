# updatemysql.py
#
# Lab 08.03
#
# # David O'Connell, 17/11/2024

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="wsaa_lab")

cur = connection.cursor()
sql = "UPDATE student SET name=%s, age=%s WHERE id=%s"
values = ("Joe", 33, 1)
cur.execute(sql, values)
connection.commit()
print("Updated")

cur.close()
connection.close()