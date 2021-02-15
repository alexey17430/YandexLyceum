import sqlite3

file_name = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f'''SELECT title FROM films WHERE title like "%?"''').fetchall()
for elem in result:
    print(elem[0])
