#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

X,Y,Z,K = II()
A = III()
B = III()
C = III()

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

a = []
if X*Y*Z <= 10**6:
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                a.append(A[i]+B[j]+C[k])
    a.sort(reverse=True)
    for i in range(K):
        print(a[i])
else:
    for i in range(X):
        if i==0: jmax = Y
        else: jmax = min(Y,math.ceil(5000/i))
        for j in range(jmax):
            if i*j==0: kmax = Z
            else: kmax = min(Z,math.ceil(5000/i/j))
            for k in range(kmax):
                a.append(A[i]+B[j]+C[k])
    a.sort(reverse=True)   
    for i in range(K):
        print(a[i])