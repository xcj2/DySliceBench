from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random  # randome is not available at Codeforces
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
inf=float('inf')
#eps=10**(-10)
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
show_flg=True

n=I()
d=LI()
ans=0
for i in range(n):
    for j in range(i+1,n):
        ans+=d[i]*d[j]
print(ans)
