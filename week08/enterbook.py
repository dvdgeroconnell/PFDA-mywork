# enterbook.py
#
# Lab 08.02
#
# # David O'Connell, 17/11/2024

import sqlite3

con = sqlite3.connect("pfda.db")
cur = con.cursor()

book = {}
book['title'] = input("please enter book title: ")
book['author'] = input("please enter book author: ")
book['ISBN'] = input("Please enter book ISBN: ")
print("You entered\n",book)

data = [book]
enter_sql = "INSERT INTO book VALUES (:title, :author, :ISBN)"

cur.executemany(enter_sql, data)
con.commit()

result = cur.execute("SELECT * FROM book")
for row in result:
    print (f"row {row}")

con.close()