class ReversedList:
    def __init__(self, sp):
        self.sp = sp

    def __len__(self):
        return len(self.sp)

    def __getitem__(self, key):
        return list(reversed(self.sp))[key]
