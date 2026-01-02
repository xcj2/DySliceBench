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
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N,M = mint()
C = []
for _ in range(M):
    s,c = mint()
    C.append([s,c])

for x in range(10**(N-1)-(N==1),10**N):
    x = str(x)
    if all([x[s-1]==str(c) for s,c in C]):
        print(x)
        exit()
print(-1)