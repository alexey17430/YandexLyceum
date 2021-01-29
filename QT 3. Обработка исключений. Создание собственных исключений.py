stroka = input().replace(' ', '')


def main(st):
    try:
        if st[0] != '8' and st[:2] != '+7':
            raise ValueError
        new_st = ''
        otk = 0
        clo = 0
        if st.startswith('-') or st.endswith('-') or \
                ('(' in st and ')' in st and st.index(')') < st.index('(')):
            raise ValueError

        for j in range(len(st)):
            i = st[j]
            if j + 1 != len(st) and st[j] + st[j + 1] == '--':
                raise ValueError
            if i == '(':
                otk += 1
            elif i == ')':
                clo += 1
            elif i != ' ' and i != '-' and i != '(' and i != ')' and i in '+1234567890':
                new_st += i
            elif i not in '+1234567890() -\t':
                raise ValueError
        if otk == clo == 1 or otk == clo == 0:
            pass
        else:
            raise ValueError
        if new_st.startswith('8'):
            new_st = '+7' + new_st[1:]
        if len(new_st) == 12:
            return new_st
        raise ValueError
    except ValueError:
        return 'error'


print(main(stroka))
