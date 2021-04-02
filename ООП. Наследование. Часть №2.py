class Profile:
    def __init__(self, name_of_job):
        self.name_of_job = name_of_job

    def info(self):
        return ''

    def describe(self):
        print(f'{self.name_of_job} {self.info()}')


class Vacancy(Profile):
    def __init__(self, name_of_job, money):
        super().__init__(name_of_job)
        self.money = money

    def info(self):
        return f'Предлагаемая зарплата: {self.money}'


class Resume(Profile):
    def __init__(self, name_of_job, age_of_working):
        super().__init__(name_of_job)
        self.age_of_working = age_of_working

    def info(self):
        return f'Стаж работы: {self.age_of_working}'
