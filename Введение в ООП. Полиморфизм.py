class Person:
    def __init__(self, name, second_name, family_name, phones_numbers):
        self.name = name
        self.second_name = second_name
        self.family_name = family_name
        self.phones_numbers = phones_numbers

    def get_phone(self):
        return self.phones_numbers.get('private', None)

    def get_name(self):
        return ' '.join([self.family_name, self.name, self.second_name])

    def get_work_phone(self):
        return self.phones_numbers.get('work', None)

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.second_name}! Примите участие в нашем ' \
            f'беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name_of_company, type_of_company, phones_numbers, *all_workers):
        self.name_of_company = name_of_company
        self.type_of_company = type_of_company
        self.phones_numbers = phones_numbers
        self.all_workers = all_workers

    def get_phone(self):
        if 'contact' in self.phones_numbers:
            return self.phones_numbers.get('contact')
        for worker in self.all_workers:
            if not worker.get_work_phone() is None:
                return worker.get_work_phone()

    def get_name(self):
        return self.name_of_company

    def get_sms_text(self):
        return f'Для компании {self.name_of_company} есть супер предложение! ' \
            f'Примите участие в нашем беспроигрышном конкурсе для {self.type_of_company}'


def send_sms(*args):
    for user in args:
        if not user.get_phone() is None:
            print(f'Отправлено СМС на номер {user.get_phone()} с текстом: {user.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {user.get_name()}')
