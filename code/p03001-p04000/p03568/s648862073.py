# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 日 10/22 21:08:14 2017

# Usage
#
"""
from functools import reduce
from itertools import repeat


def multipler(x, y):
    return x*y

def hundred_or_one(l: list):
    return [True if x == 100 else False for x in l]
    # return [True if x == 1 or x == 100 else False for x in l]

def check_odds(l :list):
    return [True if x % 2 == 0 else False for x in l]

def check_hun(l: list):
    return [True if x == 100 else False for x in l]

def main(num, data:list):
    """
    >>> main(1, [2])
    1
    >>> main(1, [3])
    2
    >>> main(10, [90,52,56,71,44,8,13,30,57,84])
    58921
    >>> main(2, [2,3])
    7
    >>> main(2, [100,100])
    3
    >>> main(1, [100])
    1
    >>> main(2, [1,1])
    8
    >>> main(1, [1])
    2
    >>> main(2, [1,2])
    7
    >>> main(2, [1,3])
    8
    >>> main(2, [1,100])
    5
    >>> main(3, [1,1,100])

    >>> main(3, [1,100,100])
    """
    hun_one = hundred_or_one(data)
    odds = check_odds(data)  # 偶数の数
    huns = check_hun(data)

    basis = [3 for t in hun_one]

    # basis = [2 if t else 3 for t in hun_one]
    remover = [2 if o else 1 for o in odds]

    remover_num = int(reduce(multipler, remover))
    # if sum(huns) > 0:
    #     remover_num = int(remover_num / 2 ** sum(huns))

    basic_answer = reduce(multipler, basis)
    # print(basic_answer)
    # print(remover_num)
    return basic_answer - remover_num

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    num = int(input())
    data = input().split(" ")
    data = [int(i) for i in data]

    print(main(num, data))
