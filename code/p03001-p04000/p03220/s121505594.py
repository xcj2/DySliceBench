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

n = INT()

T,A = MAP()
h = LIST()

ans = [INF, INF]
sa=INF

for i, x in enumerate(h):
    if abs(A - T + x * 0.006) < sa:
        ans = [i + 1, x]
        sa=abs(A - T + x * 0.006)

print(ans[0])
        
        
