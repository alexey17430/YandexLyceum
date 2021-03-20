class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, chislo):
        self.year = chislo

    def set_month(self, chislo):
        self.month = chislo

    def set_day(self, chislo):
        self.day = chislo

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        month = self.month if self.month >= 10 else '0' + str(self.month)
        day = self.day if self.day >= 10 else '0' + str(self.day)
        year = self.year
        return f'{month}.{day}.{year}'


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, chislo):
        self.year = chislo

    def set_month(self, chislo):
        self.month = chislo

    def set_day(self, chislo):
        self.day = chislo

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        month = self.month if self.month >= 10 else '0' + str(self.month)
        day = self.day if self.day >= 10 else '0' + str(self.day)
        year = self.year
        return f'{day}.{month}.{year}'
