# createmysqltable.py
#
# Lab 08.03
#
# # David O'Connell, 17/11/2024

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="wsaa_lab")

cur = connection.cursor()
sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
cur.execute(sql)

cur.close()
connection.close()