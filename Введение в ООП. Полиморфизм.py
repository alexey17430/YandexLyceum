class Selector:
    def __init__(self, number):
        self.number = number.copy()

    def get_odds(self):
        return list(filter(lambda x: x % 2 != 0, self.number))

    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.number))
