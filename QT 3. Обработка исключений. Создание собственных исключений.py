# LBYL
password = input().strip()


def main(st):
    try:
        assert len(st) > 8
        assert st != st.lower()
        flag = False
        for i in st:
            if i in '1234567890':
                flag = True
                break
        assert flag
        # english PC
        line1 = 'qwertyuiop'
        line2 = 'asdfghjkl'
        line3 = 'zxcvbnm'
        for i in range(len(st) - 2):
            elem = st[i: i + 3].lower()
            assert elem not in line1
            assert elem not in line2
            assert elem not in line3

        # english mac
        line1 = 'qwertzuiop'
        line2 = 'asdfghjkl'
        line3 = 'yxcvbnm'
        for i in range(len(st) - 2):
            elem = st[i: i + 3].lower()
            assert elem not in line1
            assert elem not in line2
            assert elem not in line3
        # russian
        line1 = 'йцукенгшщзхъ'
        line2 = 'фывапролджэё'
        line3 = 'ячсмитьбю'
        for i in range(len(st) - 2):
            elem = st[i: i + 3].lower()
            assert elem not in line1
            assert elem not in line2
            assert elem not in line3
        raise IndexError
    except AssertionError:
        return 'error'
    except IndexError:
        return 'ok'


print(main(password))
