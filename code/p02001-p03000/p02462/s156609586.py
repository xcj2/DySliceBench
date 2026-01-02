# -*- coding: utf-8 -*-
"""
Dictionary - Multi-Map
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_8_D&lang=jp

"""
from bisect import insort, bisect_right, bisect_left

class Multi_map:
    def __init__(self):
        self.mm = dict()
        self.lr = []

    def insert(self, x, y):
        if x in self.mm:
            self.mm[x].append(y)
        else:
            self.mm[x] = [y]
            insort(self.lr, x)

    def get(self, x):
        if x in self.mm and self.mm[x] != []:
            print(*self.mm[x], sep='\n')

    def delete(self, x):
        if x in self.mm:
            self.mm[x] = []

    def dump(self, l, r):
        lb = bisect_left(self.lr, l)
        ub = bisect_right(self.lr, r)
        for i in range(lb, ub):
            k = self.lr[i]
            for v in self.mm[k]:
                print(f'{k} {v}')


mm = Multi_map()
for _ in range(int(input())):
    op, x, y = (input() + ' 1').split()[:3]
    if op == '0':
        mm.insert(x, int(y))
    elif op == '1':
        mm.get(x)
    elif op == '2':
        mm.delete(x)
    else:
        mm.dump(x, y)

