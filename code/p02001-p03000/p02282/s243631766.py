#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
input:
5
1 2 3 4 5
3 2 4 1 5

output:
3 4 2 5 1
"""

import sys


# recursively defines a binary tree
# node.left or node.right may also be a binary tree
class TreeNode:
    __slots__ = ('val', 'left', 'right')

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def rec(pre_order, in_order, post_order):
    if not pre_order:
        return None, list()
    else:
        rt = TreeNode(pre_order[0])
        rt_pos = in_order.index(pre_order[0])
        rt.left = rec(pre_order[1:1 + rt_pos], in_order[:rt_pos], post_order)
        rt.right = rec(pre_order[rt_pos + 1:], in_order[rt_pos + 1:], post_order)

        # append rt.val at last to implement post_order node scan
        post_order.append(rt.val)
        return rt, post_order


def solve():
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    pre_order = list(map(int, _input[1].split()))
    in_order = list(map(int, _input[2].split()))
    # assert len(pre_order) == len(in_order) == array_length
    
    post_order = list()
    ans = rec(pre_order=pre_order, in_order=in_order, post_order=post_order)
    print(*ans[1])
    return None


if __name__ == '__main__':
    solve()