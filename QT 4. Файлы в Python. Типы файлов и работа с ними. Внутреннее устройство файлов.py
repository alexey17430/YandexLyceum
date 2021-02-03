import random


file = open('lines.txt')
sp = list(map(lambda st: st.strip(), file.readlines()))
if len(sp) > 0:
    print(random.choice(sp))
file.close()
