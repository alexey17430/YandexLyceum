import csv

file = open('wares.csv', encoding='UTF-8')
reader = csv.DictReader(file, delimiter=';')
for elem in reader:
    if int(elem['Old price']) - int(elem['New price']) > 0:
        print(elem['Name'])
