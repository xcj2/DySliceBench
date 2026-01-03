# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-09-28
#

# Usage
#
"""
import sys

def input_single_line():
    """Receive Inputs."""
    return input()

def input_two_line():
    """Receive Two Lined Inputs.
    Like this.

    N
    1 2 3 4 5
    """
    sys.stdin.readline()
    target = sys.stdin.readline()
    target = target.rstrip("\n")
    target = target.split(" ")

    return target


def search_lovers(target_list: list) -> None:
    """Search Simple.
    >>> target_list = [2, 3, 1]
    >>> search_lovers(target_list)
    0
    >>> target_list = [2, 1, 4, 3]
    >>> search_lovers(target_list)
    2
    >>> target_list = [5, 5, 5, 5, 1]
    >>> search_lovers(target_list)
    1
    """
    target_list = [int(i) - 1 for i in target_list]
    lovers = []
    ans = 0
    for i, n in enumerate(target_list):
        if target_list[n] == i:
            ans = ans + 1

    print(int(ans/2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    target = input_two_line()

    search_lovers(target)

