from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

a = [1]*(10**5+1)
a[0] = a[1] = a[2] = 0

for i in range(2, ceil(sqrt(10**5)+1)):
    for j in range(i*2, len(a), i):
        a[j] = 0
        if j*2 - 1 < len(a):
            a[j*2-1] = 0

q = INT()
p = [LIST() for i in range(q)]
s = list(accumulate(a))

for i in range(q):
    print(s[p[i][1]]-s[p[i][0]-1])