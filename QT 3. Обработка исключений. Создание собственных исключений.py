class DefaultList(list):
    def __init__(self, num):
        super().__init__(self)
        self.num = num

    def __getitem__(self, item):
        try:
            return list.__getitem__(self, item)
        except IndexError:
            return self.num
