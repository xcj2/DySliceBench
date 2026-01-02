import sys
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()
A = LIST()
ans = [0]*n
for i in range(n-1,-1,-1):
    res = 0
    j = 0
    while (j+1) *(i+1) <= n:
        res += ans[(j+1)*(i+1)-1]
        j += 1
    if res%2 != A[i]:
        ans[i] = 1
print(ans.count(1))
for i in range(n):
    if ans[i] == 1:
        print(str(i+1)+' ', end = '')
    
