import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
inf = 10**17
mod = 10**9 + 7

n=I()
data=MXI()
s=sorted(data, key=lambda x: x[1])
sm=0
for i in range(n):
    sm+=s[i][0]
    if sm<=s[i][1]:
        continue
    else:
        print("No")
        sys.exit()
print("Yes")