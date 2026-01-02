from functools import reduce


class Solver(object):
    def __init__(self):
        self.n, self.x = list(map(int, input().split(" ")))
        self.x_s = list(map(int, input().split(" ")))

    def solve(self):
        self.shifted = [abs(self.x - i) for i in self.x_s]
        print(Solver.gcd(self.shifted))

    @staticmethod
    def gcd(numbers):
        if len(numbers) < 1:
            raise ValueError
        if len(numbers) == 1:
            return numbers[0]
        return reduce(Solver.pair_gcd, numbers)

    @staticmethod
    def pair_gcd(a, b):
        """a = bq + r"""
        a, b = (max(a, b), min(a, b))
        if b == 0:
            return a
        else:
            r = a % b
            return Solver.pair_gcd(b, r)


if __name__ == "__main__":
    s = Solver()
    s.solve()