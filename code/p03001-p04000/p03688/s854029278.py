from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=sys.stdin.readline
show_flg=False
#show_flg=True

n=I()
a=LI()
m,M=min(a),max(a)
n_m=a.count(m)
n_M=a.count(M)

if m+1<M:
    ans=1
elif m+1==M:
    if n_M//2+n_m>=m+1>=n_m+1:
        ans=0
    else:
        ans=1
else:
    if m==n-1 or m<=n//2:
        ans=0
    else:
        ans=1

print(YN[ans])
