from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
ts=time.time()
sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
show_flg=True

an=0
n,m=MI()
a=LI()
q=[]
for i in a:
    heappush(q,-i)

for i in range(m):
    x=-heappop(q)
    x//=2
    heappush(q,-x)
print(-sum(q))