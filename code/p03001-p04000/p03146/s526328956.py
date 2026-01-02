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
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

va=I()
if va==1:
    print(4)
    sys.exit()
if va==2:
    print(4)
    sys.exit()
if va==4:
    print(4)
    sys.exit()
else:
    for i in range(1,10**6+10):
        if va%2==0:
            va=va//2
        else:
            va=3*va+1
        if va==4:
            print(i+4)
            sys.exit()