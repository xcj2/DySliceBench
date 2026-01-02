from operator import itemgetter
import sys


class BIT:
    def __init__(self, size: int):
        self.size = size + 1
        self.array = [0] * self.size

    def add(self, i):
        while i < self.size:
            self.array[i] += 1
            i += i & -i

    def sub(self, i):
        while i < self.size:
            self.array[i] -= 1
            i += i & -i

    def sum(self, a, b):
        s = 0
        i = b
        while i > 0:
            s += self.array[i]
            i -= i & -i
        i = a - 1
        while i > 0:
            s -= self.array[i]
            i -= i & -i
        return s


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, read().split())
    c = [int(i) - 1 for i in read().split()]
    queries = [(0, 0, 0) for _ in range(q)]
    for i in range(q):
        l, r = map(int, read().split())
        queries[i] = (i, l, r)
    queries = iter(sorted(queries, key=itemgetter(2)))
    last = [0] * n
    bit = BIT(n)
    ans = [-1] * q
    k, l, r = next(queries)
    for i in range(n):
        ci = c[i]
        li = last[ci]
        if li > 0:
            bit.sub(li)
        last[ci] = i + 1
        bit.add(i + 1)
        while i + 1 == r:
            ans[k] = bit.sum(l, r)
            try:
                k, l, r = next(queries)
            except StopIteration:
                break
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
