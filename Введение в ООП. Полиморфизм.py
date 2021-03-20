class Table:
    """
    rows - количество списков внутри списка
    cols - длина маленьких списков
    """
    def __init__(self, rows, cols):
        self.table = list()
        for i in range(rows):
            small_ans = list()
            for j in range(cols):
                small_ans.append(0)
            self.table.append(small_ans)
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        try:
            ans = self.table[row][col]
        except IndexError:
            ans = None
        if row < 0 or col < 0:
            ans = None
        return ans

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0]) if self.table else 0
