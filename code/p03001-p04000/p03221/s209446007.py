import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits



def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))

def update(bit,i, dp):
    bit[i] = dp
    return bit

def query(bit, i):
    lis = [bit[j] for j in range(i)]
    return max(lis)


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

n,m=MAP()

py = [LIST() for _ in range(m)]
py = [[i,x[0],x[1]] for i,x in enumerate(py)]
lis=deepcopy(py)
lis.sort(key=lambda x: (x[1], x[2]))

ans = [""] * m

tmp=1
ct = 1

for x in lis:
    if tmp!=x[1]:
        tmp = x[1]
        ct = 1
    ans[x[0]] = '{:06}{:06}'.format(x[1], ct)
    ct += 1
        
for x in ans:
    print(x)