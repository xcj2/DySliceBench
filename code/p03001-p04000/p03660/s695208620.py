import bisect
from operator import itemgetter
import math
import copy
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(x):
    if visited[x] == False:
        visited[x] = True
        path.append(x)
        if x == N:
            return True
        for i in root[x]:
            if tami(i):
                return True
        else:
            del path[-1]
    return False

def nas(x):
    global cnt
    if (visited[x] == False) and (data[x] == 0):
        visited[x] = True
        cnt += 1
        for i in root[x]:
            nas(i)

N = I()
ab = [IL() for i in range(N-1)]
data = np.array([0]*(N+1))
root = [[]*(N+1) for i in range(N+1)]
visited = [False]*(N+1)

path = []
f = 0
for a,b in ab:
    root[a].append(b)
    root[b].append(a)

tami(1)
middle_No = path[math.ceil(len(path)/2)-1]
data[middle_No] = 1

visited = [False]*(N+1)
cnt = 0
nas(N)

Snuke = cnt
Fennec = N - Snuke

if Fennec > Snuke:
    print("Fennec")
else:
    print("Snuke")
