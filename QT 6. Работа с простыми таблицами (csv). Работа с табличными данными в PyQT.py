import csv

file = open('vps.csv', encoding='UTF-8')
reader = (csv.DictReader(file, delimiter=';'))
number = int(input())
for elem in reader:
    if not int(elem['соответствует в %']) < number:
        print(elem['Специальность'])