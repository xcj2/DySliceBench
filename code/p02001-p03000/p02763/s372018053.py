import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


class BIT:
    def __init__(self, L):
        self.n = len(L)
        self.bit = [0] * (self.n + 1)

    def update(self, idx, x):
        while idx <= self.n:
            self.bit[idx] += x
            idx += idx & (-idx)

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    def sec_sum(self, left, right):
        return self.query(right) - self.query(left - 1)

    def debug(self):
        print(*[self.sec_sum(i, i) for i in range(1, self.n + 1)])


def resolve():
    n = int(input())
    S = list(input().rstrip())
    q = int(input())

    bits = [BIT(S) for _ in range(26)]
    for idx in range(1, n + 1):
        s = S[idx - 1]
        bits[ord(s) - ord("a")].update(idx, 1)

    for _ in range(q):
        query = list(input().split())
        if query[0] == "1":
            i, c = int(query[1]), query[2]
            prev = S[i - 1]
            bits[ord(prev) - ord("a")].update(i, -1)
            bits[ord(c) - ord("a")].update(i, 1)
            S[i - 1] = c
        else:
            l, r = int(query[1]), int(query[2])
            res = 0
            for j in range(26):
                if bits[j].sec_sum(l, r):
                    res += 1
            print(res)


if __name__ == '__main__':
    resolve()
