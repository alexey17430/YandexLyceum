import sqlite3

file_name = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f'''SELECT title FROM films WHERE
genre = (SELECT id from genres where title = 'детектив') and 1995 <= year and year <= 2000''').fetchall()
for elem in result:
    print(elem[0])