# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created:  2016-10-10
#

# Usage
#
"""

def read_value():
    first_line = input()
    status = first_line.split(" ")

    num_of_contestant = int(status[0])
    basis = int(status[1])
    oversea_limit = int(status[2])

    second_line = input()
    rank_str = second_line

    return [num_of_contestant, basis, oversea_limit, rank_str]


def check_japan(rank, basis, oversea_limit):
    if rank < basis + oversea_limit:
        return "Yes"
    else:
        return "No"

def check_overseas(rank, oversea_rank, basis, oversea_limit):
    if rank < basis + oversea_limit and oversea_rank <= oversea_limit:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    input_items = read_value()

    basis = input_items[1]
    oversea_limit = input_items[2]
    rank_str = input_items[3]

    oversea_rank = 0
    passed = 0

    for rank, type in enumerate(rank_str):
        if type == "a":
            if check_japan(passed, basis, oversea_limit) == "Yes":
                print("Yes")
                passed += 1
            else:
                print("No")

        if type == "b":
            oversea_rank += 1
            if check_overseas(passed, oversea_rank, basis, oversea_limit) == "Yes":
                print("Yes")
                passed += 1
            else:
                print("No")

        if type == "c":
            print("No")
