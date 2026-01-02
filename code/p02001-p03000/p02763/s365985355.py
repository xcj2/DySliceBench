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
    import sys

    input = sys.stdin.readline

    n = int(input())  # 5 * 10 ** 5
    s = input().rstrip()

    base = ord('a')
    *s, = (ord(c) - base for c in s)

    q = int(input())  # 2 * 10 ** 4

    bits = [BIT(n + 1) for _ in range(26)]
    for i, x in enumerate(s, 1):
        bits[x].add(i, 1)

    ret = []
    for _ in range(q):
        query = iter(input().split())
        if next(query) == '1':
            # 変更
            pos = int(next(query))

            bf = s[pos - 1]
            char = ord(next(query)) - base

            bits[bf].add(pos, -1)
            s[pos - 1] = char

            bits[char].add(pos, 1)

        else:
            # 返答
            l = int(next(query))
            r = int(next(query))

            tt = 0
            for x in range(26):
                if bits[x].get(l - 1, r) > 0:
                    tt += 1
            ret.append(tt)

    print(*ret, sep='\n')


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
