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
input=sys.stdin.readline
show_flg=False
show_flg=True

n,k,q=MI()
a=[]
p=[k-q]*n
for i in range(q):
    a.append(I())
    
while a:
    x=a.pop()
    p[x-1]+=1

for i in range(n):
    if p[i]>0:
        an=0
    else:
        an=1
        
    print(YN[an])
