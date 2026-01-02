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
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,M = II()
A,B = Line(N-1+M,2)

parent = [[] for _ in range(N)]
parent_num = [0]*N
pt = [[] for _ in range(N)]

for i in range(N-1+M):
    parent[B[i]-1].append(A[i]-1)
    parent_num[B[i]-1] += 1
    pt[A[i]-1].append(B[i]-1)

for i in range(N):
    if parent[i]==[]:
        root = i

ans = ['0']*N
q = [root]
while q:
    q_new = []
    for q1 in q:
        for v in pt[q1]:
            if parent_num[v]==1:
                ans[v] = q1+1
                q_new.append(v)
            parent_num[v] -= 1
    q = q_new

for i in range(N):
    print(ans[i])