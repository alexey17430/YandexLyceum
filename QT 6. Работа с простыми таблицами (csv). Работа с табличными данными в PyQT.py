import csv

file = open('input.csv', encoding='UTF-8')
reader = list(csv.reader(file, delimiter=';'))
start_town = reader[-1][0]
finish_town = reader[-1][1]
del reader[-1]
all_ways = dict()
for elem in reader:
    if (elem[0] == start_town and elem[1] == finish_town and (elem[0], elem[1]) not in all_ways) or\
            elem[0] == start_town and elem[1] == finish_town and\
            (elem[0], elem[1]) in all_ways and all_ways[(elem[0], elem[1])] < int(elem[2]):
        all_ways[(elem[0], elem[1])] = int(elem[2])
    else:
        if elem[0] == start_town:
            for next_elem in reader:
                if next_elem[0] == elem[1] and next_elem[1] == finish_town:
                    s = int(elem[2]) + int(next_elem[2])
                    letters = (elem[0], next_elem[0], next_elem[1])
                    if letters in all_ways and all_ways[letters] > s or letters not in all_ways:
                        all_ways[letters] = s
                        break
print(*min(all_ways, key=lambda x: all_ways[x]))
