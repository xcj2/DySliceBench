# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 日  1/13 22:32:34 2019

# Usage
#
"""
def get_input():
    _ = input()
    A = [int(i) for i in input().split(" ")]
    B = [int(i) for i in input().split(" ")]

    return A, B


def solve(A, B):
    """
    >>> solve([2,3,5],[3,4,1])
    >>> solve([2,3,3],[2,2,1])
    """
    need_magic = [a_each - b_each for a_each,b_each in zip(A,B)]
    if sum(need_magic) < 0:
        return -1
    else:
        plus = [x for x in need_magic if x > 0]
        minus = [x for x in need_magic if x < 0]
        return check_needs(plus, minus)


def check_needs(plus, minus):
    target = sum(minus)
    count = 0
    for magic in sorted(plus, reverse=True):
        if target >= 0:
            break
        target += magic
        count += 1
    return count + len(minus)


if __name__ == '__main__':
    a = get_input()
    print(solve(a[0], a[1]))
