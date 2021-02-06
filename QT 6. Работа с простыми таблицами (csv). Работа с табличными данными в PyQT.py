from sys import stdin

n, m = map(int, input().split())
ans_file = open('exam.csv', 'w', encoding='utf-8')
flag = True
for elem in stdin:
    elem = elem.strip()
    elem = elem.split()
    if int(elem[-1]) + int(elem[-2]) + int(elem[-3]) >= n and int(elem[-1]) >= m and \
            int(elem[-2]) >= m and int(elem[-3]) >= m:
        if flag:
            print('Фамилия;имя;результат 1;результат 2;результат 3;сумма', file=ans_file)
            flag = False
        s = int(elem[-1]) + int(elem[-2]) + int(elem[-3])
        print(f'{";".join(elem)};{s}', file=ans_file)
