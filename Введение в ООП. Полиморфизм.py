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

    def delete_row(self, row):
        new_table = [self.table[i] for i in range(len(self.table)) if i != row]
        self.table.clear()
        self.table.extend(new_table)

    def delete_col(self, col):
        new_table = list()
        for elem in self.table:
            new_table.append([elem[i] for i in range(len(elem)) if i != col])
        self.table.clear()
        self.table.extend(new_table)

    def add_row(self, row):
        if self.table == [0]:
            self.table.clear()
            self.table.append([0])
        else:
            self.table.insert(row, [0 for _ in range(len(self.table[0]) if self.table else 0)])

    def add_col(self, col):

        if len(self.table) > 0:
            small_ans = list()
            for i in range(len(self.table)):
                sp = self.table[i]
                sp1 = list()
                flag = False
                if col == 0:
                    sp1.append(0)
                    flag = True
                for j in range(len(sp)):
                    if j == col and not flag:
                        sp1.append(0)
                        flag = True
                    sp1.append(sp[j])
                if not flag:
                    sp1.append(0)
                small_ans.append(sp1)
            self.table.clear()
            self.table.extend(small_ans)
        else:
            self.table.append(0)
