import sys
sys.setrecursionlimit(1000000)


def input():
    return sys.stdin.readline()


n = int(input())
aa = {}
for j,i in enumerate(map(int,input().split())):
    if i in aa:
        aa[i].append(j)
    else:
        aa[i] = [j]
a = [0] * n
for k,i in enumerate(sorted(list(aa))):
    for j in aa[i]:
        a[j] = k+1


class SegmentTree:
    def __init__(self, a, func=max, one=-10 ** 18):
        self.logn = (len(a) - 1).bit_length()
        self.n = 1 << self.logn
        self.func = func
        self.one = one

        self.b = [self.one] * (2 * self.n - 1)
        for i, j in enumerate(a):
            self.b[i + self.n - 1] = j
        for i in reversed(range(self.n - 1)):
            self.b[i] = self.func(self.b[i * 2 + 1], self.b[i * 2 + 2])

    def get_item(self, i):
        return self.b[i + self.n - 1]

    def update(self, index, x):
        i = index + self.n - 1
        self.b[i] = x
        while i != 0:
            i = (i - 1) // 2
            self.b[i] = self.func(self.b[i * 2 + 1], self.b[i * 2 + 2])

    def update_func(self, index, x):
        i = index + self.n - 1
        self.b[i] = self.func(self.b[i], x)
        while i != 0:
            i = (i - 1) // 2
            self.b[i] = self.func(self.b[i * 2 + 1], self.b[i * 2 + 2])

    def get_segment(self, l, r):
        l += self.n
        r += self.n
        s = self.one
        while l < r:
            if r & 1:
                r -= 1
                s = self.func(s, self.b[r - 1])
            if l & 1:
                s = self.func(s, self.b[r - 1])
                l += 1
            l >>= 1
            r >>= 1
        return s


e = [[] for _ in range(n)]
for _ in range(n - 1):
    aa, bb = [int(i) - 1 for i in input().split()]
    e[aa].append(bb)
    e[bb].append(aa)
seg = SegmentTree([0] * (max(a)+2), max, 0)
ans1 = [0] * n
ans1[0] = 1
ans2 = [0] * n
ans2[0] = 1


def dfs(i=0, r=-1):

    y = seg.get_segment(0, a[i])
    ans1[i] = y + 1
    ans2[i] = max(ans2[r], ans1[i])

    be = seg.get_item(a[i])
    seg.update_func(a[i], ans1[i])
    for j in e[i]:
        if j == r:
            continue
        dfs(j, i)
    seg.update(a[i], be)


dfs()
print("\n".join(map(str,(ans2))))
