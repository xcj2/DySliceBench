import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N = int(input())
x0,y0,t0 = 0,0,0
ans = True
for _ in range(N):
    t,x,y = mint()
    tmp = (t-t0)-(abs(x-x0)+abs(y-y0))
    if not (tmp>=0 and tmp%2==0):
        ans = False
        break
    x0,y0,t0 = x,y,t
judge(ans)