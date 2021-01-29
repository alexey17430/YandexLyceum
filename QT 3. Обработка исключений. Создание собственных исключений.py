stroka = input().replace(' ', '')


def main(st):
    try:
        if st[0] != '8' and st[0] != '+':
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
        if new_st[0] == '8':
            new_st = '+7' + new_st[1:]
        elem = new_st[2:4]
        flagok = True
        for i in ['902', '903', '904', '905', '906']:
            if new_st[2:5] == i:
                flagok = False
                break
        if len(new_st) != 12:
            raise IndexError
        if elem != '91' and elem != '92' and elem != '93' and \
                elem != '98' and elem != '96' and flagok:
            if new_st[0:2] == '+7':
                return 'не определяется оператор сотовой связи'
        if not new_st.startswith('+359') and not new_st.startswith('+7') and \
                not new_st.startswith('+55') and not new_st.startswith('+1'):
            return 'не определяется код страны'
        return new_st
    except ValueError:
        return 'неверный формат'
    except IndexError:
        return 'неверное количество цифр'


print(main(stroka))
