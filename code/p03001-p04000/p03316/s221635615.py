# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 土  6/23 21:14:29 2018

# Usage
#
"""
import sys
def get_input():
    line = sys.stdin.readline()

    return line.rstrip()

def sum_digit(target: str):
    """
    >>> sum_digit("190")
    10
    >>> sum_digit("0")
    0
    """
    sumup = 0
    for digit in target:
        sumup = sumup + int(digit)

    return sumup

def check_sum(target, sumup):
    """
    >>> target = "999999999"
    >>> check_sum(target, sum_digit(target))
    Yes
    >>> target = "101"
    >>> check_sum(target, sum_digit(target))
    >>> target = "12"
    >>> check_sum(target, sum_digit(target))
    """

    target = int(target)

    try:
        if target % sumup == 0:
            print("Yes")
        else:
            print("No")
    except ZeroDivisionError:
        print("No")

if __name__ == '__main__':
    stdin = get_input()
    check_sum(stdin, sum_digit(stdin))