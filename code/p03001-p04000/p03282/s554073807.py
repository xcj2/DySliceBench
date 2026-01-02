import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import operator as op
import collections as cl
import functools as ft

def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()


def count_first_1(s):
    count = 0
    first_letter = ''

    for letter in s:
        if letter == '1':
            count += 1
        else:
            first_letter = letter
            break

    return count, first_letter


if __name__ == "__main__":
    s = S()
    k = I()

    count, first_letter = count_first_1(s)

    if not first_letter:
        result = '1'

    elif count >= k:
        result = '1'

    else:
        result = first_letter

    print(result)
