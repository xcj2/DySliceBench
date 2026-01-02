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

N = I()
A = III()
B = III()

def index_sort(A):
    a = []
    for i,x in enumerate(A):
        a.append([i,x])
    asort = sorted(a,key=lambda x: x[1])
    return [asort[i][0] for i in range(len(a))]

A2 = sorted(A)
B2 = sorted(B)

for i in range(N):
    if A2[i]>B2[i]:
        print('No')
        exit()

Aindex = index_sort(A)
Bindex = index_sort(B)
move = [0]*N
for i in range(N):
    move[Aindex[i]] = Bindex[i]

now = 0
for i in range(N):
    if move[now]==0 and i!=N-1:
        print('Yes')
        exit()
    now = move[now]

for i in range(N-1):
    if B2[i]>=A2[i+1]:
        print('Yes')
        exit()

print('No')