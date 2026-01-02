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
    n = int(input())
    h = list(input_list())
    count = 0
    while True:
        if list(set(h)) == [0]:
            break
        flag = False
        count += 1
        for i, v in enumerate(h):
            if v != 0:
                flag = True
                h[i] -= 1
            else:
                if flag:
                    break
    print(count)

def minus(numbers):
    for i, n in enumerate(numbers):
        if n == 0:
            break
        numbers[i] -= 1
    return numbers


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == '__main__':
    main()

