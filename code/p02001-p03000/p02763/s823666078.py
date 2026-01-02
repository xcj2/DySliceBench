import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
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
        return self.query(right) - self.query(left)

    def debug(self):
        print(*[self.sec_sum(i - 1, i) for i in range(1, self.n + 1)])


def resolve():
    n = int(input())
    S = list(input().rstrip())
    q = int(input())
    query = [list(input().split()) for _ in range(q)]

    bits = [BIT(S) for _ in range(26)]
    for i in range(n):
        bits[ord(S[i]) - ord("a")].update(i + 1, 1)

    for j in range(q):
        if query[j][0] == "1":
            _, i, c = query[j]
            i = int(i) - 1
            bits[ord(S[i]) - ord("a")].update(i + 1, -1)
            bits[ord(c) - ord("a")].update(i + 1, 1)
            S[i] = c
        else:
            _, l, r = query[j]
            l, r = int(l), int(r)
            res = 0
            for k in range(26):
                if bits[k].sec_sum(l - 1, r):
                    res += 1
            print(res)


if __name__ == '__main__':
    resolve()
