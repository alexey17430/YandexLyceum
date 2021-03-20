class Rectangle:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def intersection(self, other):
        if self.x2 <= other.x1 or self.x1 >= other.x2:
            return None
        elif self.y1 >= other.y2 or self.y2 <= other.y1:
            return None
        else:
            answer = list()  # x1, x2, y1, y2
            if self.x1 < other.x1:
                answer.append(other.x1)
            else:
                answer.append(self.x1)

            if self.x2 < other.x2:
                answer.append(self.x2)
            else:
                answer.append(other.x2)

            if self.y1 < other.y1:
                answer.append(other.y1)
            else:
                answer.append(self.y1)

            if self.y2 < other.y2:
                answer.append(self.y2)
            else:
                answer.append(other.y2)

            return Rectangle(min(answer[0], answer[1]), min(answer[2], answer[3]),
                             abs(answer[0] - answer[1]), abs(answer[2] - answer[3]))

    def get_x(self):
        return self.x1

    def get_y(self):
        return self.y1

    def get_w(self):
        return self.x2 - self.x1

    def get_h(self):
        return self.y2 - self.y1
