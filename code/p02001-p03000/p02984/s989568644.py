import sys
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

n = INT()
a = LIST()

b = [0]*n
b[0] = a[0]
for i in range(1,n):
    b[i] = a[i] - b[i-1]
c = [0]*(n-1)
for i in range(n-1):
    c[i] = b[i]*2 + ((-1)**(i+1))*b[n-1]

print(str(b[n-1]) + " ",end = "")
for i in range(n-1):
    print(str(c[i]) + " ", end = "")