#!/usr/bin/env python3
import collections
import itertools as it
import math
import numpy as np
import functools
 
#  = input()
n  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))
t  = [int(input()) for i in range(n)]
#
# c = collections.Counter()

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def multiple(a, b):
    return a*b // euclid(a, b)

def gcd(nums):
    return functools.reduce(euclid, nums)

def lcm(nums):
        return functools.reduce(multiple, nums)

print(lcm(t))
