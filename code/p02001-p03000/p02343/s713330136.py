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
    __slots__ = ('size', 'tree_height_rank_list', 'ancestor_list')

    def __init__(self, size):
        self.size = int(size)
        self.tree_height_rank_list = [0] * self.size
        self.ancestor_list = [i for i in range(self.size)]

    def __find(self, x):
        if x != self.ancestor_list[x]:
            self.ancestor_list[x] = self.__find(self.ancestor_list[x])
        return self.ancestor_list[x]

    def same(self, x, y):
        return self.__find(x) == self.__find(y)

    def __link(self, x, y):
        if self.tree_height_rank_list[x] > self.tree_height_rank_list[y]:
            self.ancestor_list[y] = x
        else:
            self.ancestor_list[x] = y
            if self.tree_height_rank_list[x] == self.tree_height_rank_list[y]:
                self.tree_height_rank_list[y] += 1

    def union(self, x, y):
        self.__link(self.__find(x), self.__find(y))


def action(cmd_list):
    for each in cmd_list:
        cmd, ele_1, ele_2 = map(int, each)
        if cmd == 0:
            case.union(ele_1, ele_2)
        elif cmd == 1:
            if case.same(ele_1, ele_2):
                print('1')
            else:
                print('0')
    return case


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    e_num, c_num = map(int, _input[0].split())
    c_list = map(lambda x: x.split(), _input[1:])

    case = UnionFind(size=e_num)

    ans = action(c_list)