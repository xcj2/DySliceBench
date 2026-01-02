import sys
from collections import deque
from functools import *
from itertools import *

N = int(input())
As = list(map(int, input().split()))

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    a , b = (a, b) if a > b else (b, a)
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
        pass
    return b

def gcd_acc(acc, x):
    if len(acc) == 0:
        acc.append(x)
        return acc
    last = acc[-1]
    acc.append(gcd(last, x))
    return acc

def candidates(As):
    length = len(As)
    L = iter(reduce(gcd_acc, As, deque()))
    R = reversed(reduce(gcd_acc, reversed(As), deque()))
    next(R)

    yield next(R)

    if length == 1:
        return

    for _ in range(length-2):
        yield gcd(next(L), next(R))
        pass
    yield next(L)
    pass

print(max(candidates(As)))

