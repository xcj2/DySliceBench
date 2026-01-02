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

(n,), (s,), _, *q = map(str.split, open(0))
*s, = s
BIT = [Bit(int(n)) for _ in [0] * 26]
for e, t in enumerate(s):
    BIT[ord(t) - 97].add(e, 1)
for a, b, c in q:
    if a == "1":
        i = int(b)
        BIT[ord(s[i - 1]) - 97].add(i - 1, -1)
        s[i - 1] = c
        BIT[ord(c) - 97].add(i - 1, 1)
    else:
        l, r = int(b), int(c)
        print(sum(BIT[i].sum(r) - BIT[i].sum(l - 1) > 0 for i in range(26)))
