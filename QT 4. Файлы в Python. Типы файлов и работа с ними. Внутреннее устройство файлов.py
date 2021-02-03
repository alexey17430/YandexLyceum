input_file = open('input.txt')
all_files = list(map(lambda x: x.strip(), input_file.readlines()))
ans_dict = dict()
ans_sum_dict = dict()
for line in all_files:
    name, massa, edin = line.split()
    massa = int(massa)
    expan = name[name.index('.'):]
    if expan in ans_dict:
        ans_dict[expan] = ans_dict[expan] + [name]
    else:
        ans_dict[expan] = [name]
    if edin == 'MB':
        number = massa * 1024 * 1024
    elif edin == 'KB':
        number = massa * 1024
    elif edin == 'GB':
        number = massa * 1024 * 1024 * 1024
    else:
        number = massa
    if expan in ans_sum_dict:
        ans_sum_dict[expan] += number
    else:
        ans_sum_dict[expan] = number
ans_file = open('output.txt', 'w')
for key in sorted(ans_dict.keys()):
    for elem in sorted(ans_dict[key]):
        print(elem, file=ans_file)
    print('----------', file=ans_file)
    number = ans_sum_dict[key]
    if (number / 1024 / 1024 / 1024) >= 1:
        print('Summary:', round(number / 1024 / 1024 / 1024), 'GB', '\n', file=ans_file)
    elif (number / 1024 / 1024) >= 1:
        print('Summary:', round(number / 1024 / 1024), 'MB', '\n', file=ans_file)
    elif (number / 1024) >= 1:
        print('Summary:', round(number / 1024), 'KB', '\n', file=ans_file)
    else:
        print('Summary:', number, 'B', '\n', file=ans_file)
ans_file.close()
