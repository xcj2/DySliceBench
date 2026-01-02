#!/usr/bin/env python
# coding: utf-8

from collections import namedtuple
from heapq import *


class Elem:
    def __init__(self, v, a, b, c):
        self.v = v
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        return self.v > other.v

    def __str__(self):
        return "{} {} {} {}".format(self.v, self.a, self.b, self.c)

    def __repr__(self):
        return self.__str__()

    def id(self):
        return self.a*1000*1000+self.b*1000+self.c

X, Y, Z, K = list(map(int, input().split()))
la = list(map(int, input().split()))
lb = list(map(int, input().split()))
lc = list(map(int, input().split()))
la.sort(reverse=True)
lb.sort(reverse=True)
lc.sort(reverse=True)
ids = set()

def next(e):
    elems = []
    if e.a < len(la)-1:
        elems.append(Elem(la[e.a+1]+lb[e.b]+lc[e.c],e.a+1,e.b,e.c))
    if e.b < len(lb)-1:
        elems.append(Elem(la[e.a]+lb[e.b+1]+lc[e.c],e.a,e.b+1,e.c))
    if e.c < len(lc)-1:
        elems.append(Elem(la[e.a]+lb[e.b]+lc[e.c+1],e.a,e.b,e.c+1))
    return elems

def main():
    best = Elem(la[0]+lb[0]+lc[0], 0, 0, 0)
    h = []
    heappush(h, best)
    cnt = 0
    while True:
        if len(h) == 0:
            break
        e = heappop(h)
        if e.id() in ids:
            continue
        ids.add(e.id())
        elems = next(e)
        for ne in elems:
            heappush(h, ne)
        print(e.v)
        cnt += 1
        if cnt == K:
            break


if __name__ == '__main__':
    main()
