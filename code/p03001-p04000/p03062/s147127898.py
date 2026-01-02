import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
import math
from functools import reduce


def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))

def SUM(x):return sum([abs(x) for x in a ])



sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

n = INT()

a = LIST()

ct = 0

p=[]

for i, x in enumerate(a):
    if x < 0:
        ct +=1
        p.append([i, x])
    elif x == 0:
        ct = 0
        p.clear()


saidai = SUM(a)
a_abs = [abs(x) for x in a]

if ct % 2 == 0:
    print(saidai)
else:
    a_min = min(a_abs)
    print(saidai-2*a_min)

    
    