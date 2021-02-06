import csv

file = open('salary.csv', encoding='UTF-8')
reader = list(csv.DictReader(file, delimiter=';'))
name = input()
year1, year2 = input().split()
ans_file = open('out_file.csv', 'w', encoding='UTF-8')
flag = True
for elem in reader:
    if elem['Федеральный округ'] != name:
        continue
    first, second = elem[year1], elem[year2]
    if (int(second) - int(first)) / int(first) * 100 < 4:
        if flag:
            print(f'Субъект;{year1};{year2}', file=ans_file)
            flag = False
        print(f'{elem["Субъект"]};{first};{second}', file=ans_file)
