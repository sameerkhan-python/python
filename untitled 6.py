class Number:
    def __init__(self, n):
        self.n = n

    def __floordiv__(self, num):
        return self.n // num.n

n = Number(5)
m = Number(2)

print(n // m)