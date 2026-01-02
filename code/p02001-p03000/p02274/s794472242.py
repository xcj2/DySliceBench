import sys

def solve():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().split()))
    b = compress(a)

    ft = FenwickTree(max(b) + 1)
    ans = 0

    for bi in reversed(b):
        ans += ft.psum(bi + 1)
        ft.add(bi, 1)

    print(ans)

def compress(a):
    n = len(a)
    a = [(ai, i) for i, ai in enumerate(a)]
    a.sort()

    num = -1
    p = -1

    b = [None] * n

    for val, idx in a:
        if val > p:
            num += 1

        b[idx] = num
        p = val

    return b

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.b = [0] * (n + 1)

    def add(self, i, x):
        i += 1

        while i <= self.n:
            self.b[i] += x
            i += i & (-i)

    def psum(self, r):
        res = 0

        while r > 0:
            res += self.b[r]
            r -= r & (-r)

        return res

if __name__ == '__main__':
    solve()