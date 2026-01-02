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
        return self.query(right) - self.query(left - 1)

    def debug(self):
        print(*[self.sec_sum(i - 1, i) for i in range(1, self.n + 1)])


def resolve():
    n, q = map(int, input().split())
    C = list(map(int, input().split()))
    query = []
    for i in range(q):
        l, r = map(int, input().split())
        query.append([l, r, i])
    query.sort(key=lambda x: x[1])

    lastAppeared = [0] * (max(C) + 1)
    prev = query[0][1]
    for i in range(prev):
        lastAppeared[C[i]] = i + 1

    bit = BIT(C + [0])
    for num in lastAppeared:
        if num == 0:
            continue
        bit.update(num, 1)

    res = [0] * q
    for L, R, idx in query:
        if R > prev:
            for j in range(prev, R):
                if lastAppeared[C[j]]:
                    num = lastAppeared[C[j]]
                    bit.update(num, -1)
                lastAppeared[C[j]] = j + 1
                num = lastAppeared[C[j]]
                bit.update(num, 1)
            prev = R
        res[idx] = bit.sec_sum(L, R)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
