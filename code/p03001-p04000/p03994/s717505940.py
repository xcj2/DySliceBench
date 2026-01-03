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
    n = sys.stdin.readline()
    n = n.rstrip("\n")
    target = sys.stdin.readline()
    target = target.rstrip("\n")
    # target = target.split(" ")

    return n, target


def check_a_becombility(one_str: str) -> int:
    """Check how can this str become "a"
    >>> check_a_becombility("a")
    0
    >>> check_a_becombility("z")
    1
    >>> check_a_becombility("b")
    25
    """
    if ord(one_str) == 97:
        return 0  # Because this is "a"

    return 123 - ord(one_str)


def make_suzuki_process(target_str :str, chance: int) -> str:
    """Suzuki Process.
    >>> make_suzuki_process("xyz", 4)
    'aya'
    >>> make_suzuki_process("a", 25)
    'z'
    >>> make_suzuki_process("codefestival", 100)
    'aaaafeaaivap'
    >>> make_suzuki_process("aaaa", 1000)
    'aaam'
    >>> make_suzuki_process("a", 26)
    'a'
    """
    target_str = list(target_str)
    costs = [check_a_becombility(i) for i in target_str]

    for pos, each_cost in enumerate(costs):
        if chance - each_cost >= 0:
            chance = chance - each_cost
            target_str[pos] = "a"

    if chance > 0:
        target_str[-1] = chr(ord(target_str[-1]) + chance % 26)

    return "".join(target_str)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    inputted = input_two_line()

    print(make_suzuki_process(inputted[0], int(inputted[1])))
