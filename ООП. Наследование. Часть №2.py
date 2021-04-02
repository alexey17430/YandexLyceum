class Summator:
    def transform(self, n):
        return list(range(1, n + 1))

    def sum(self, n):
        return sum(self.transform(n))


class SquareSummator(Summator):
    def transform(self, n):
        return list(i ** 2 for i in range(1, n + 1))


class CubeSummator(Summator):
    def transform(self, n):
        return list(i ** 3 for i in range(1, n + 1))
