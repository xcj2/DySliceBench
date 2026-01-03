# 解説を見た

# https://tjkendev.github.io/procon-library/python/range_query/bit.html
# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = (int(input()) - K for _ in range(N))

    acc = (0,) + tuple(accumulate(A))

    def compress(iter):
        convert = {x: i for i, x in enumerate(sorted(iter), start=1)}
        # BITで扱うので、1-indexedにする
        # 値kがa番目とa+1番目に含まれているとき、k:a->k:a+1で上書きされる
        return (convert[x] for x in iter)

    comacc = compress(acc)

    ret = 0

    b = BIT(N + 1)
    for x in comacc:
        ret += b.sum(x)
        b.add(x, 1)

    print(ret)


if __name__ == '__main__':
    main()
