# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 土  9/ 8 21:24:49 2018

# Usage
#
"""
from operator import and_
from functools import reduce
def get_nlines():
    N = int(input())
    return [input() for i in range(N)]


def tsunagari_check(first, second):
    if first[-1] == second[0]:
        return True
    else:
        return False

def judge(data):
    """
    >>> judge(["hoge","english", "hoge"])
    False
    >>> judge(["basic","cpp","python"])
    True
    >>> judge(["agg","abc", "cba"])
    False
    """
    # 1st check
    if len(set(data)) == len(data):
        pass
    else:
        return False

    # 2nd check
    checked = [tsunagari_check(data[i], data[i+1]) for i in range(len(data)-1)]
    # print(checked)
    return reduce(and_, checked)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    RES = judge(get_nlines())
    if RES:
        print("Yes")
    else:
        print("No")
