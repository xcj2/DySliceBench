# -*- coding: utf-8 -*-
"""
Dictionary - Map: Range Search
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_8_C&lang=jp

"""
from bisect import insort, bisect_right, bisect_left

class Range_map:
    def __init__(self):
        self.rm = dict()
        self.lr = []

    def insert(self, x, y):
        if x not in self.rm:
            insort(self.lr, x)
        self.rm[x] = y

    def get(self, x):
        print(self.rm.get(x, 0))

    def delete(self, x):
        if x in self.rm:
            self.rm[x] = 0

    def dump(self, l, r):
        lb = bisect_left(self.lr, l)
        ub = bisect_right(self.lr, r)
        for i in range(lb, ub):
            k = self.lr[i]
            if k in self.rm and self.rm[k] != 0:
                print(f'{k} {self.rm[k]}')


rm = Range_map()
for _ in range(int(input())):
    op, x, y = (input() + ' 1').split()[:3]
    if op == '0':
        rm.insert(x, int(y))
    elif op == '1':
        rm.get(x)
    elif op == '2':
        rm.delete(x)
    else:
        rm.dump(x, y)

