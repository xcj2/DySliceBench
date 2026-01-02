import bisect
from operator import itemgetter
import math
import collections
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def gcd(a,b):
    while b % a:
        a,b = b, a % b
    return a

A,B,C,D = IL()

c = B//C - (A-1)//C
d = B//D - (A-1)//D
cd =B//(C*D//gcd(C,D)) - (A-1)//(C*D//gcd(C,D))

print((B-A+1)-(c+d)+cd)