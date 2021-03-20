class Queue:
    def __init__(self, *queue):
        self.queue = list(queue)

    def append(self, *value):
        for elem in value:
            self.queue.append(elem)

    def copy(self):
        ans = list()
        for elem in self.queue:
            ans.append(elem)
        return Queue(*ans)

    def pop(self):
        if len(self.queue) == 0:
            return None
        ans = self.queue[0]
        del self.queue[0]
        return ans

    def extend(self, other):
        for elem in other.queue:
            self.queue.append(elem)

    def next(self):
        return Queue(*list(self.queue[1:]))

    def __add__(self, other):
        ans = list()
        for elem in self.queue:
            ans.append(elem)
        for elem in other.queue:
            ans.append(elem)
        return Queue(*ans)

    def __iadd__(self, other):
        self.append(*other.queue)
        return self

    def __eq__(self, other):
        return self.queue == other.queue

    def __rshift__(self, n):
        ans = list()
        for i in self.queue:
            if n == 0:
                ans.append(i)
            else:
                n -= 1
        return Queue(*ans)

    def __str__(self):
        ans = '['
        for i in range(len(self.queue)):
            if i + 1 == len(self.queue):
                ans += str(self.queue[i])
            else:
                ans += str(self.queue[i]) + ' -> '
        ans += ']'
        return ans

    def __next__(self):
        return Queue(*list(self.queue[1:]))
