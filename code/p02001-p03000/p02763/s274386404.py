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
    from string import ascii_lowercase
    import sys
    input = sys.stdin.readline

    n = int(input())
    s = [ascii_lowercase.index(c) for c in input().rstrip()]
    q = int(input())

    bits = [BIT(n) for _ in range(26)]
    for base1, ord in enumerate(s, 1):
        bits[ord].add(base1, +1)

    ret = []
    for _ in range(q):
        it = iter(input().split())
        if next(it) == '1':
            # 変更
            base1 = int(next(it))

            prev_ord = s[base1 - 1]
            next_ord = ascii_lowercase.index(next(it))

            bits[prev_ord].add(base1, -1)
            bits[next_ord].add(base1, +1)

            s[base1 - 1] = next_ord

        else:
            # 返答
            start, end = map(int, it)
            res = sum(
                bits[ord].get(start - 1, end) > 0
                for ord in range(26)
            )

            ret.append(res)

    print(*ret, sep='\n')


if __name__ == '__main__':
    main()
