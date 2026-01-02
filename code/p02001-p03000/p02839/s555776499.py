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

H,W = II()
A,B,C = [],[],[]
for i in range(H):
    A.append(III())
for i in range(H):
    B.append(III())
for i in range(H):
    C.append([abs(A[i][j]-B[i][j]) for j in range(W)])

def calc(n):
    return n+80*(H+W-1)

d = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i==0 and j==0:
            d[i][j] = 2**calc(-C[i][j]) | 2**calc(C[i][j])
        elif i==0:
            d[i][j] = (d[i][j-1]<<C[i][j]) | (d[i][j-1]>>C[i][j])
        elif j==0:
            d[i][j] = (d[i-1][j]<<C[i][j]) | (d[i-1][j]>>C[i][j])
        else:
            d[i][j] = (d[i][j-1]<<C[i][j]) | (d[i][j-1]>>C[i][j]) | \
                        (d[i-1][j]<<C[i][j]) | (d[i-1][j]>>C[i][j])

ans = (H+W-1)*80+1
for i in range(160*(H+W-1)+1):
    if (d[H-1][W-1]>>i)&1:
        val = abs(i-80*(H+W-1))
        if val<ans:
            ans = val

print(ans)