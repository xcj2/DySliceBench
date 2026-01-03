#!/usr/bin/env python3


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * n

    def sum(self, i):
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            i = (i & (i + 1)) - 1
        return s

    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i |= i + 1


def solve(n, a):

    ans = 0

    s = []
    r = 0
    for i in range(n):
        r += a[i]
        s.append((r, i))
        if 0 <= r:
            ans += 1

    s.sort()

    bit = Bit(n)
    for tpl in s:
        _, i = tpl
        ans += bit.sum(i)
        bit.add(i, 1)

    return ans


def main():
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = []
    for _ in range(n):
        ai = input()
        ai = int(ai) - k
        a.append(ai)

    print(solve(n, a))


if __name__ == '__main__':
    main()

