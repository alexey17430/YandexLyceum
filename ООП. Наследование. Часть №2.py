class Summator:
    def transform(self, n):
        return list(range(1, n + 1))

    def sum(self, n):
        return sum(self.transform(n))


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return list(i ** self.b for i in range(1, n + 1))


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)
