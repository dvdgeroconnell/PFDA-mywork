# insertbook.py
#
# Lab 08.02
#
# # David O'Connell, 17/11/2024

import sqlite3

con = sqlite3.connect("pfda.db")
cur = con.cursor()

# Check if anything in table
result = cur.execute("SELECT * FROM book")
print (result.fetchone())

insert_sql = "INSERT INTO book VALUES ('Harry1', 'Rowling1', '1234'), ('Harry2', 'Rowling2', '5678')"
cur.execute(insert_sql)
con.commit()

result = cur.execute("SELECT * FROM book")
for row in result:
    print (f"row {row}")

con.close()