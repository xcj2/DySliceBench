#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,cos,radians,sqrt
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n=I()
lis=LI()
v=sorted(lis)
u=sorted(lis)[-1]
dis=[]
if u%2==0:
    k=u//2
    for i in range(n-1):
        dis.append(abs(v[i]-k))
    l=sorted(dis)[0]
    for i in range(n-1):
        if dis[i]==l:
            print(u,v[i])
            sys.exit()
else:
    k=(u-1)//2
    m=(u+1)//2
    for i in range(n-1):
        dis.append(abs(v[i]-k))
        dis.append(abs(v[i]-m))
    l=sorted(dis)[0]
    #print(l)
    for i in range(len(dis)):
        if l==dis[i]:
            print(u,v[i//2])
            sys.exit()