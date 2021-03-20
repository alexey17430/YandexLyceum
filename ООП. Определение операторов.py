class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = dict()
        for i in range(len(coefficients)):
            self.coefficients[i] = [coefficients[i]]

    def __call__(self, x):
        answer = 0
        for key, values in self.coefficients.items():
            for value in values:
                answer += value * (x ** key)
        return answer

    def __add__(self, other):
        new_coefficients = dict()
        dlina = len(self.coefficients) if len(self.coefficients) >= len(other.coefficients)\
            else len(other.coefficients)
        for i in range(dlina):
            new_coefficients[i] = self.coefficients.get(i, [0]) + (other.coefficients.get(i, [0]))
        return Polynomial(list(sum(value)for key, value in new_coefficients.items()))
