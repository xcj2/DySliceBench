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
        
def sgn(x):
    if x==0:
        return x
    return x//abs(x)

N,A = ilint()
tmp = A[0]
ans = 1
s = 0
for a in A[1:]:
    if s==0:
        s = sgn(a-tmp)
        tmp = a
    elif s*(a-tmp)>=0:
        tmp = a
    else:
        ans += 1
        tmp = a
        s = 0
print(ans)