import csv

file = open('rez.csv', encoding='UTF-8')
reader = csv.DictReader(file, delimiter=',', quotechar='"')
school, cls = map(int, input().split())
ans = list()
for elem in reader:
    user_name = elem['user_name']
    login = elem['login']
    score = elem['Score']
    login = login.split('-')
    if int(login[-3]) == school and int(login[-2]) == cls:
        ans.append([(user_name.split()[-2]), score])
for i in range(len(ans) - 1):
    for j in range(len(ans) - i - 1):
        if int(ans[j][1]) > int(ans[j + 1][1]):
            ans[j], ans[j + 1] = ans[j + 1], ans[j]
        elif int(ans[j][1]) == int(ans[j + 1][1]) and (ans[j][0]) > (ans[j + 1][0]):
            ans[j], ans[j + 1] = ans[j + 1], ans[j]
for elem in reversed(ans):
    print(*elem)
