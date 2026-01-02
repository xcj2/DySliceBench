import bisect
import sys

input = sys.stdin.readline
num2alpha = lambda c: chr(c + 97)
alpha2num = lambda c: ord(c) - ord("a")


class SegTreeMax:
    def __init__(self, l):
        self.N = 1
        while self.N < l:
            self.N *= 2
        self.L = [0 for _ in range(self.N * 2 - 1)]

    def update(self, k, v):
        k += self.N - 1
        self.L[k] = v
        while k > 0:
            k = (k - 1) // 2
            self.L[k] = max(self.L[k * 2 + 1], self.L[k * 2 + 2])

    def append(self, k, v):
        k += self.N - 1
        self.L[k] += 2 ** v
        while k > 0:
            k = (k - 1) // 2
            self.L[k] = self.L[k * 2 + 1] | self.L[k * 2 + 2]

    def delete(self, k, v):
        k += self.N - 1
        self.L[k] -= 2 ** v
        while k > 0:
            k = (k - 1) // 2
            self.L[k] = self.L[k * 2 + 1] | self.L[k * 2 + 2]

    def query(self, a, b):
        return self.inquiry(0, self.N, 0, a, b)

    def inquiry(self, l, r, k, a, b):
        if r <= a or l >= b:
            return 0
        if a <= l and b >= r:
            return self.L[k]
        vl = self.inquiry(l, (l + r) // 2, k * 2 + 1, a, b)
        vr = self.inquiry((l + r) // 2, r, k * 2 + 2, a, b)
        return vl | vr


def main():
    N = int(input())
    Stri = input()
    L = []
    for c in Stri:
        L.append(c)
    Q = int(input())
    S = SegTreeMax(N)
    for i in range(N):
        S.append(i, alpha2num(L[i]))

    for _ in range(Q):
        a, b, c = input().split()
        if a == "1":
            i = int(b) - 1
            S.delete(i, alpha2num(L[i]))
            L[i] = c
            S.append(i, alpha2num(c))

        else:
            l = int(b) - 1
            r = int(c)
            res = S.query(l, r)
            p = 0
            for i in range(26):
                p += res & 1
                res >>= 1
            print(p)


main()
