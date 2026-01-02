# -*- coding: utf-8 -*-
"""
Set - Multi-Set
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_D&lang=jp

"""
from bisect import insort, bisect_right, bisect_left

class Multi_set:
    def __init__(self):
        self.total = 0
        self.ms = dict()
        self.lr = []

    def insert(self, x):
        self.total += 1
        if x in self.ms:
            self.ms[x] += 1
        else:
            self.ms[x] = 1
            insort(self.lr, x)
        print(self.total)

    def find(self, x):
        print(self.ms.get(x, 0))

    def delete(self, x):
        if x in self.ms:
            self.total -= self.ms[x]
            self.ms[x] = 0

    def dump(self, l, r):
        lb = bisect_left(self.lr, l)
        ub = bisect_right(self.lr, r)
        for i in range(lb, ub):
            k = self.lr[i]
            v = self.ms[k]
            print(f'{k}\n' * v, end='')


ms = Multi_set()
for _ in range(int(input())):
    op, x, y = (input() + ' 1').split()[:3]
    if op == '0':
        ms.insert(int(x))
    elif op == '1':
        ms.find(int(x))
    elif op == '2':
        ms.delete(int(x))
    else:
        ms.dump(int(x), int(y))

