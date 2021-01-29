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


class WordError(PasswordError):
    pass


def check_password(st):
    sp_of_errors = list()

    def check_length(st):
        try:
            if len(st) <= 8:
                raise LengthError
            return 'ok'
        except LengthError:
            sp_of_errors.append('LengthError')

    def check_letter(st):
        try:
            if st == st.lower() or st == st.upper():
                raise LetterError
            return 'ok'
        except LetterError:
            sp_of_errors.append('LetterError')

    def check_digit(st):
        try:
            flag = False
            for i in st:
                if i in '1234567890':
                    flag = True
                    break
            if not flag:
                raise DigitError
            return 'ok'
        except DigitError:
            sp_of_errors.append('DigitError')

    def check_sequence(st):
        try:
            # english PC
            sp1 = ['qwertyuiop',
                   'asdfghjkl',
                   'zxcvbnm']
            sp2 = ['qwertzuiop',
                   'asdfghjkl',
                   'yxcvbnm']
            sp3 = ['йцукенгшщзхъ',
                   'ёфывапролджэ',
                   'ячсмитьбю']

            for spisok in (sp1, sp2, sp3):
                line1, line2, line3 = spisok
                for i in range(len(st) - 2):
                    elem = st[i: i + 3].lower()
                    if elem in line1:
                        raise SequenceError
                    elif elem in line2:
                        raise SequenceError
                    elif elem in line3:
                        raise SequenceError
            return 'ok'
        except SequenceError:
            sp_of_errors.append('SequenceError')

    def check_word(passw):
        try:
            for word in dictionary:
                word = word.strip()
                passw = passw.strip()
                if word in passw:
                    raise WordError
            return 'ok'
        except WordError as err:
            sp_of_errors.append(err.__class__.__name__)

    check_word(st)
    check_length(st)
    check_letter(st)
    check_digit(st)
    check_sequence(st)

    for err in sp_of_errors:
        dict_of_errors[err] = dict_of_errors.get(err, 0) + 1


dict_of_errors = dict()
dictionary = open('top-9999-words.txt').readlines()
dict_of_errors['SequenceError'] = -1
passwords = open('top 10000 passwd.txt', 'r')
n = 0
for password in passwords:
    password.strip()
    password = password.strip()
    check_password(password)
for key in sorted(dict_of_errors.keys()):
    print(f'{key} - {dict_of_errors[key]}')
