import sys


def read():
    return sys.stdin.buffer.readline().rstrip()


class FenwickTree:
    def __init__(self, n):
        self._n = n
        self._a = [0] * n

    def add(self, i, x):
        i += 1
        while i <= self._n:
            self._a[i - 1] += x
            i += i & -i

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self._a[r - 1]
            r -= r & -r
        return s


def main():
    n, q = map(int, read().split())
    fw = FenwickTree(n)
    for i, ai in enumerate(map(int, read().split())):
        fw.add(i, ai)
    for _ in range(q):
        query = [int(i) for i in read().split()]
        if query[0] == 0:
            fw.add(query[1], query[2])
        else:
            print(fw.sum(query[1], query[2]))


if __name__ == '__main__':
    main()
