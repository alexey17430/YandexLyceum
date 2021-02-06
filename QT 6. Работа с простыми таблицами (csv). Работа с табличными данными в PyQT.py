import csv

file = open('wares.csv', encoding='UTF-8')
reader = csv.reader(file, delimiter=';')
spisok = sorted(reader, key=lambda x: int(x[1]))
ans = list()
money = 1000
for elem in spisok:
    for i in range(10):
        name, cost = elem
        cost = int(cost)
        if cost <= money:
            ans.append(name)
            money -= cost
    if money <= 0:
        break
if len(ans) == 0:
    print('error')
else:
    print(', '.join(ans))