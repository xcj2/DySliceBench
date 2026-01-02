import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2,gcd
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

ans=[]

while 1:
    n,m=MAP()
    if n==0 and m==0:
        break
    else:
        a=LIST()
        
        lis=[sum(x) for x in list(combinations(a,2)) if sum(x)<=m]
        if not lis:
            ans.append('NONE')
        else:
            ans.append(max(lis))

for x in ans:
    print(x)




