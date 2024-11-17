# createmysqldb.py
#
# Lab 08.03
#
# # David O'Connell, 17/11/2024

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="")

cur = connection.cursor()
cur.execute("CREATE database wsaa_lab")

cur.close()
connection.close()