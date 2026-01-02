import sys
import numpy as np
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


class Solver(object):
    def __init__(self):
        pass

    def solve(self, x: int, y: int):
        if (x + y) % 3 != 0:
            return 0
        A = np.matrix([[1, 2],
                       [2, 1]])
        Y = np.matrix([[x],
                       [y]])
        m, n = np.linalg.solve(A, Y)
        if m < 0:
            return 0
        if n < 0:
            return 0
        return self.cmb(int(m)+int(n), int(n)) % (10**9 + 7)

    def cmb(self, n, r):
        if n - r < r:
            r = n - r
        if r == 0:
            return 1
        if r == 1:
            return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2, r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1, r, p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])

        return result


def main():
    X, Y = [int(i) for i in input().split()]

    solver = Solver()
    print(solver.solve(X, Y))


if __name__ == "__main__":
    main()