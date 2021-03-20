class MinStat:
    def __init__(self):
        self.all_numbers = list()

    def add_number(self, chislo):
        self.all_numbers.append(chislo)

    def result(self):
        return min(self.all_numbers) if self.all_numbers else None


class MaxStat(MinStat):
    def result(self):
        return max(self.all_numbers) if self.all_numbers else None


class AverageStat(MinStat):
    def result(self):
        return sum(self.all_numbers) / len(self.all_numbers) if self.all_numbers else None
