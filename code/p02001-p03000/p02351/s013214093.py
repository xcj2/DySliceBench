import sys

def solve():
    N, Q = map(int, sys.stdin.readline().split())

    p = FenwickTree(N + 1)
    q = FenwickTree(N + 1)

    for qi in range(Q):
        query = sys.stdin.readline().rstrip()

        if query[0] == '0':
            c, s, t, x = map(int, query.split())
            s -= 1
            p.add(s, -s*x)
            p.add(t, t*x)
            q.add(s, x)
            q.add(t, -x)
        else:
            c, s, t = map(int, query.split())
            s -= 1

            res = p.get_sum(t) + q.get_sum(t)*t
            res -= p.get_sum(s) + q.get_sum(s)*s

            print(res)

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.data = [0]*(size + 1)

    def add(self, i, x):
        i += 1

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