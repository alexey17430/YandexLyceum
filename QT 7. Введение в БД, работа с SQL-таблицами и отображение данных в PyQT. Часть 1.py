import sqlite3

file_name = input()
con = sqlite3.connect(file_name)
cur = con.cursor()

result = cur.execute(f'''select title from films where duration <= 85''')

for elem in result:
    print(elem[0])