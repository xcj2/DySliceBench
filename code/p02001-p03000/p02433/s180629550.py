# -*- coding: utf-8 -*-
"""
Dynamic Arrays and List - List
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C&lang=jp

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
        x.prev = self.cur.prev
        self.cur.prev.next = x
        self.cur.prev = x
        x.next = self.cur
        self.cur = x

    def move(self, d):
        if d >= 0:
            for _ in range(d):
                self.cur = self.cur.next
        else:
            for _ in range(abs(d)):
                self.cur = self.cur.prev


    def erase(self):
        if self.cur == self.nil:
            return
        p = self.cur.next
        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev
        self.cur = p


lst = Lst()
for _ in range(int(input())):
    op, n = (input() + ' 1').split()[:2]
    if op == '0':
        lst.insert(int(n))
    elif op == '1':
        lst.move(int(n))
    else:
        lst.erase()

cur = lst.nil
while cur.next != lst.nil:
    cur = cur.next
    print(cur.key)

