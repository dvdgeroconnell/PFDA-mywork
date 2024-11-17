# createbooktable.py
#
# Lab 08.02
#
# # David O'Connell, 17/11/2024

import sqlite3

con = sqlite3.connect("pfda.db")
cur = con.cursor()
#sql = "DROP TABLE IF EXISTS book"
#cur.execute(sql)

sql_create = "CREATE TABLE book(title, author, ISBN)"
cur.execute(sql_create)

con.close