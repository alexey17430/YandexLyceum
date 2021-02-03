price = open('prices.txt')
su = 0
for elem in price.readlines():
    elem = elem.strip()
    name, colvo, cost = elem.split('\t')
    su += float(colvo) * float(cost)
su = str(su)
if '.' in su and len(su[su.index('.') + 1:]) == 1:
    su += '0'

print(su)
