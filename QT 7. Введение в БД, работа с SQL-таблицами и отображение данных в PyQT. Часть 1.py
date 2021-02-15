import sqlite3

file_name = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f'''
SELECT title FROM films
    WHERE genre in (select id from genres
    where year >= 1997 AND (title = 'музыка' or title = 'анимация'))''').fetchall()
for elem in result:
    print(elem[0])