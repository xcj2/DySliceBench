import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()

edges = []
if N%2==0:
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i+j==N+1:
                continue
            else:
                edges.append((i,j))
else:
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i+j==N:
                continue
            else:
                edges.append((i,j))

print(len(edges))
for e in edges:
    print(*e)