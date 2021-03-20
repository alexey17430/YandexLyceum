class SparseArray:
    def __init__(self):
        self.dict_of_numbers = dict()

    def __getitem__(self, key):
        return self.dict_of_numbers.get(key, 0)

    def __setitem__(self, key, value):
        self.dict_of_numbers[key] = value
