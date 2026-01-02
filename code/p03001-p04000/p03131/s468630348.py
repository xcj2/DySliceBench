# import sys
# input = sys.stdin.readline
# import re
import collections
import bisect
import math
import fractions
import collections
import itertools
from functools import reduce

def main():
    k, a, b = input_list()
    if b - a > 2:
        bis = a
        k -= a - 1
        if k % 2 == 1:
            bis += 1
            k -= 1
        bis += (k//2)*(b-a)
        print(bis)
    else:
        print(k+1)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == '__main__':
    main()

