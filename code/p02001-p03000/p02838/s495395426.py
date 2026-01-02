from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
a = LIST()

ans = 0
k = 1
for i in range(60):
    s = 0
    t = 0
    for j in range(n):
        if a[j] % 2 == 0:
            s += 1
        else:
            t += 1
        a[j] //= 2
    ans = ( ans + s * t * k ) % ( 10**9 + 7 )
    k *= 2
print(ans)