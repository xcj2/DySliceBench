#!/usr/bin/env python3
class Bit:
    # Binary Indexed Tree
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i + 1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

(n, q), c, *d = [[*map(int, o.split())] for o in open(0)]

d = sorted(enumerate(d), key = lambda x: x[1][1])

B = Bit(n)
ans = [-1] * q
last = [-1] * (n + 1)
ind = 0  # [-, ind) まで確認終了
for i, (l, r) in d:
    for j in range(ind, r):
        if last[c[j]] != -1:
            B.add(last[c[j]], -1)
        B.add(j, 1)
        last[c[j]] = j
    ind = r
    ans[i] = B.sum(r) - B.sum(l - 1)
for a in ans:
    print(a)
