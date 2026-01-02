#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
3
0.0 0.0
2.0 0.0
1.0 1.0

output:
1.41421356237
"""

import sys
from operator import attrgetter


class ClosestPair(object):
    def __init__(self, in_data):
        """
        Init closest pairs points set.
        """
        self.p_num = int(in_data[0])
        points = map(lambda x: x.split(), in_data[1:])
        p_list = [complex(float(x), float(y)) for x, y in points]
        # pre_sort by axis_X
        self.p_list = sorted(p_list, key=attrgetter('real'))

    def closest_pair(self, array, array_length):
        if array_length <= 1:
            return float('inf')
        mid_idx = array_length // 2
        div_line = array[mid_idx].real
        d_min = min(self.closest_pair(array[:mid_idx], mid_idx),
                    self.closest_pair(array[mid_idx:], array_length - mid_idx))

        # sort array_part by axis_Y while recursively comparing
        array.sort(key=attrgetter('imag'))

        min_stack = list()
        for ele in array:
            size = len(min_stack)

            # eliminate p which distance(p,div_line) >= d
            if abs(ele.real - div_line) >= d_min:
                continue

            for j in range(size):
                alt = ele - min_stack[size - j - 1]
                if alt.imag >= d_min:
                    break
                d_min = min(d_min, abs(alt))

            min_stack.append(ele)

        return d_min

    def solve(self):
        return self.closest_pair(array=self.p_list, array_length=self.p_num)


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    case = ClosestPair(in_data=_input)
    print('{:.6f}'.format(case.solve()))