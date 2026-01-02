import sys
from math import factorial
from collections import Counter
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

x, n = MAP()
p = LIST()
i = 0
while True:
    if x-i not in p:
        print(x-i)
        sys.exit()
    if x+i not in p:
        print(x+i)
        sys.exit()
    i += 1