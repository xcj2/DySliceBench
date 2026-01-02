# -*- coding: utf-8 -*-
"""
Basic Data Structures - Splice
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_2_D&lang=jp

"""

class Node:
    def __init__(self, value=0):
        self.key = value
        self.prev, self.next = None, None

class Lst:
    def __init__(self):
        self.nil = Node('END')
        self.nil.next = self.nil
        self.nil.prev = self.nil
        self.cur = self.nil

    def insert(self, value):
        x = Node(value)
        x.prev = self.cur
        x.prev.next = x
        x.next = self.nil
        self.cur = x

    def dump(self):
        res = []
        cur = self.nil
        while cur.next.key != 'END':
            cur = cur.next
            res.append(cur.key)
        print(*res)

class Sp:
    def __init__(self, n):
        self.lst = [Lst() for _ in range(n)]

    def insert(self, t, x):
        self.lst[t].insert(x)

    def dump(self, t):
        self.lst[t].dump()

    def splice(self, s, t):
        self.lst[t].cur.next = self.lst[s].nil.next
        self.lst[s].nil.next.prev = self.lst[t].cur
        self.lst[t].cur = self.lst[s].cur
        self.lst[s] = Lst()


n, q = map(int, input().split())
lst = Sp(n)
for _ in range(int(q)):
    op, t, x = (input() + ' 1').split()[:3]
    if op == '0':
        lst.insert(int(t), int(x))
    elif op == '1':
        lst.dump(int(t))
    else:
        lst.splice(int(t), int(x))

