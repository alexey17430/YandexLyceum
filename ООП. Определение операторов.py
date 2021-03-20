class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day
        self.days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __sub__(self, other):
        if self.month == other.month and self.day == other.day:
            return 0

        mon1 = self.month
        mon2 = other.month
        day1 = self.day
        day2 = other.day
        all_days1 = day1 + sum(list(self.days_in_month[i - 1] for i in range(1, mon1)))
        all_days2 = day2 + sum(list(self.days_in_month[i - 1] for i in range(1, mon2)))
        return all_days1 - all_days2
