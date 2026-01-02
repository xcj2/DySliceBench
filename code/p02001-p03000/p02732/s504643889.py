# ABC159d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    from collections import Counter
    import math

    def c_count(n, r):  # 組み合わせ
        if n - r < 0:
            return 0
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    class Combination:  # メモ化組み合わせ
        def __init__(self):
            super().__init__()
            self.dp = dict()

        def count(self, n, r):
            if self.dp.get((n, r)) != None:
                return self.dp[(n, r)]
            self.dp[(n, r)] = c_count(n, r)
            return self.dp[(n, r)]

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    d = Combination()
    e = dict()

    ss = 0

    for i in c:
        #print(i, c[i])
        e[i] = d.count(c[i], 2)
        # print(e[i])
        ss += e[i]

    for i in range(n):
        t = e[a[i]]
        w = t * (c[a[i]] - 2) // c[a[i]]
        #print(a[i], t, w)
        w = w if w >= 0 else 0
        print(ss-t+w)


if __name__ == '__main__':
    main()
