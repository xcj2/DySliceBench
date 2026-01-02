import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()


alphasm=[chr(i) for i in range(97, 97+26)]
s=input().rstrip()
t=input().rstrip()
u=Counter(list(s))
v=Counter(list(t))
a,b=[],[]
for i in alphasm:
    a.append(u[i])
    b.append(v[i])
a.sort()
b.sort()
if a==b:
    print("Yes")
else:
    print("No")