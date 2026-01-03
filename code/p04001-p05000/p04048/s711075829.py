import sys
import fractions
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n,x = MAP()

def cal(a,b):
    if a > b:
        aa = a
        a = b
        b = aa
    ref = b//a
    if b%a == 0:
        return a*(2*ref-1)
    return a*2*ref + cal(b%a,a)

print(n + cal(x,n-x))