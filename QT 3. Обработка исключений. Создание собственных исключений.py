class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(st):
    if len(st) <= 8:
        raise LengthError
    if st == st.lower() or st == st.upper():
        raise LetterError
    flag = False
    for i in st:
        if i in '1234567890':
            flag = True
            break
    if not flag:
        raise DigitError
    # english PC
    line1 = 'qwertyuiop'
    line2 = 'asdfghjkl'
    line3 = 'zxcvbnm'
    for i in range(len(st) - 2):
        elem = st[i: i + 3].lower()
        if elem in line1:
            raise SequenceError
        elif elem in line2:
            raise SequenceError
        elif elem in line3:
            raise SequenceError

    # english mac
    line1 = 'qwertzuiop'
    line2 = 'asdfghjkl'
    line3 = 'yxcvbnm'
    for i in range(len(st) - 2):
        elem = st[i: i + 3].lower()
        if elem in line1:
            raise SequenceError
        elif elem in line2:
            raise SequenceError
        elif elem in line3:
            raise SequenceError
    # russian
    line1 = 'йцукенгшщзхъ'
    line2 = 'фывапролджэё'
    line3 = 'ячсмитьбю'
    for i in range(len(st) - 2):
        elem = st[i: i + 3].lower()
        if elem in line1:
            raise SequenceError
        elif elem in line2:
            raise SequenceError
        elif elem in line3:
            raise SequenceError
    return 'ok'
