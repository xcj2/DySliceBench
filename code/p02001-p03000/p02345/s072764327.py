#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
3 5
0 0 1
0 1 2
0 2 3
1 0 2
1 1 2

output:
1
2
"""

import sys
import math


class SegmentTree(object):
    __slots__ = ('dat', 'tree_range')

    def __init__(self, n):
        """
        Init a SegmentTree with update and find for range minimum queries.
        """
        self.tree_range = pow(2, math.ceil(math.log2(n)))
        self.dat = [float('inf')] * (2 * self.tree_range - 1)

    # let A[k]=a
    def update(self, k, a):
        k += self.tree_range - 1
        self.dat[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = min(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    # get min(A[s] A[s+1] ... A[t])
    def find(self, s, t, k=0, l=0, r=float('inf')):
        if r <= s or t <= l:
            return float('inf')
        elif s <= l <= r <= t:
            return self.dat[k]
        else:
            vl = self.find(s, t, k * 2 + 1, l, (l + r) // 2)
            vr = self.find(s, t, k * 2 + 2, (l + r) // 2, r)
            return min(vl, vr)


def action(cmd_list):
    case = SegmentTree(n_num)
    end = pow(2, math.ceil(math.log2(n_num)))
    init_max = pow(2, 31) - 1

    for query in cmd_list:
        cmd, ele_1, ele_2 = map(int, query)
        if cmd == 0:
            case.update(ele_1, ele_2)
        elif cmd == 1:
            assert ele_1 <= ele_2
            res = case.find(s=ele_1, t=ele_2 + 1, r=end)
            if math.isinf(res):
                print(init_max)
            else:
                print(res)

    return case


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    n_num, q_num = map(int, _input[0].split())
    q_list = map(lambda x: x.split(), _input[1:])

    ans = action(q_list)