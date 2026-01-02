from collections import defaultdict
n = int(input())
sl = list(input())
q = int(input())


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
        assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)


dic = defaultdict(lambda: BIT(n))
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
for idx, s in enumerate(sl):
    dic[s].add(idx+1, 1)
for _ in range(q):
    a, b, c = map(str, input().split())
    if a == "1":
        b = int(b)
        dic[sl[b-1]].add(b, -1)
        dic[c].add(b, 1)
        sl[b-1] = c
    else:
        b = int(b)
        c = int(c)
        ans = 0
        for s in ascii_lowercase:
            if dic[s].get(b-1, c) > 0:
                ans += 1
        print(ans)