import sqlite3

file_name = input()
con = sqlite3.connect(file_name)
cur = con.cursor()

result = cur.execute(f'''select title from genres where id in 
(select genre from films where 2010 <= year and year <= 2011)''')
ans = list()
for elem in result:
    if elem not in ans:
        ans.append(elem)
for elem in ans:
    print(elem[0])