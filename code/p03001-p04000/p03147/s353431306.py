import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N,H = ilint()
H = [0]+H[:]
H = [-(H[i+1]-H[i]) for i in range(N)]+[INF]
ans = 0
for l in range(N):
    while H[l]<0:
        r = 0
        while r<N and H[r]<=0:
            r += 1
        tmp = min(-H[l],H[r])
        ans += tmp
        H[l] += tmp
        H[r] -= tmp
print(ans)