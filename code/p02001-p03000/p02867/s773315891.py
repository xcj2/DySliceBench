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

from bisect import bisect_left

#インデックス付きソート
#(index,value)の順に格納
def index_sort(A):
    a = []
    for i,x in enumerate(A):
        a.append([i,x])
    return sorted(a,key=lambda x: x[1])

A2 = sorted(A)
B2 = sorted(B)

for i in range(N):
    if A2[i]>B2[i]:
        print('No')
        exit()

for i in range(N-1):
    if B2[i]>=A2[i+1]:
        print('Yes')
        exit()

A3 = index_sort(A)
B3 = index_sort(B)

for i in range(2,N)[::-1]:
    bindex = B3[i][0]
    aindex = A3[i][0]
    if aindex==bindex:
        print('Yes')
        exit()
    p1 = bisect_left(A2,A[bindex])
    A[aindex],A[bindex] = A[bindex],A[aindex]
    A3[i][0],A3[p1][0] = A3[p1][0],A3[i][0]

for i in range(N):
    if A[i]>B[i]:
        print('No')
        exit()
print('Yes')