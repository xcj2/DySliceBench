# -*- coding: utf-8 -*-
"""
Dynamic Arrays and List - Vector
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_A&lang=jp

"""
import sys


class Vector:
    def __init__(self):
        self.n = 0
        self.d = dict()

    def push(self, x):
        self.d[self.n] = x
        self.n += 1

    def access(self, p):
        return self.d[p]

    def pop(self):
        self.n -= 1


def main(args):
    v = Vector()
    q = int(input())
    for _ in range(q):
        op, x = (input() + ' 1').split()[:2]
        if op == '0':
            v.push(int(x))
        elif op == '1':
            print(v.access(int(x)))
        else:
            v.pop()


if __name__ == '__main__':
    main(sys.argv[1:])

