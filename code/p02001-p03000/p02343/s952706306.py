#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""


input:
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0

output:
0
0
1
1
1
0
1
1

"""

import sys


class UnionFind(object):
    __slots__ = ('size', 'height_rank', 'ancestors')

    def __init__(self, size):
        self.size = int(size)
        self.height_rank = [0] * self.size
        self.ancestors = [i for i in range(self.size)]

    def __find(self, x):
        if x != self.ancestors[x]:
            self.ancestors[x] = self.__find(self.ancestors[x])
        return self.ancestors[x]

    def same(self, x, y):
        return self.__find(x) == self.__find(y)

    def __link(self, x, y):
        if self.height_rank[x] > self.height_rank[y]:
            self.ancestors[y] = x
        else:
            self.ancestors[x] = y
            if self.height_rank[x] == self.height_rank[y]:
                self.height_rank[y] += 1

    def union(self, x, y):
        self.__link(self.__find(x), self.__find(y))


def action(cmd_list):
    for each in cmd_list:
        cmd, ele_1, ele_2 = map(int, each)
        if cmd == 0:
            case.union(ele_1, ele_2)
        elif cmd == 1:
            print(int(case.same(ele_1, ele_2)))
    return case


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    e_num, c_num = map(int, _input[0].split())
    c_list = map(lambda x: x.split(), _input[1:])

    case = UnionFind(size=e_num)

    ans = action(c_list)