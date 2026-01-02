import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())

    ft = FenwickTree(n)

    for qi in range(q):
        query = sys.stdin.readline().rstrip()

        if query[0] == '0':
            c, s, t, x = map(int, query.split())
            ft.add(s, x)
            ft.add(t + 1, -x)
        else:
            c, i = map(int, query.split())

            print(ft.get_sum(i))


class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.data = [0]*(size + 1)

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & (-i)

    def get_sum(self, r):
        res = 0

        while r > 0:
            res += self.data[r]
            r -= r & (-r)

        return res

if __name__ == '__main__':
    solve()