# LBYL
password = input().strip()


def main(st):
    if len(st) <= 8:
        return False
    if st == st.lower():
        return False
    flag = False
    for i in st:
        if i in '1234567890':
            flag = True
            break
    if not flag:
        return False
    # english PC
    line1 = 'qwertyuiop'
    line2 = 'asdfghjkl'
    line3 = 'zxcvbnm'
    for i in range(len(st) - 2):
        elem = st[i: i + 3].lower()
        if elem in line1:
            return False
        elif elem in line2:
            return False
        elif elem in line3:
            return False

    # english mac
    line1 = 'qwertzuiop'
    line2 = 'asdfghjkl'
    line3 = 'yxcvbnm'
    for i in range(len(st) - 2):
        elem = st[i: i + 3].lower()
        if elem in line1:
            return False
        elif elem in line2:
            return False
        elif elem in line3:
            return False
    # russian
    line1 = 'йцукенгшщзхъ'
    line2 = 'фывапролджэё'
    line3 = 'ячсмитьбю'
    for i in range(len(st) - 2):
        elem = st[i: i + 3].lower()
        if elem in line1:
            return False
        elif elem in line2:
            return False
        elif elem in line3:
            return False
    return True


if main(password):
    print('ok')
else:
    print('error')
