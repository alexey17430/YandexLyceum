import sqlite3

file_name = input()
con = sqlite3.connect(file_name)
cur = con.cursor()
result = cur.execute(f'''SELECT year FROM films WHERE title like "Х%"''').fetchall()
ans = list()
for elem in result:
    if elem[0] not in ans:
        ans.append(elem[0])
for elem in ans:
    print(elem)