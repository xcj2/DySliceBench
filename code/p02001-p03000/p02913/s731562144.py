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
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

def Z_algo(S):
    n=len(S)
    A=[0]*n
    A[0]=n
    i=1
    j=0
    while i<n:
        while i+j<n and S[j]==S[i+j]: j+=1
        A[i]=j
        if j==0:
            i+=1
            continue
        k=1
        while i+k<n and k+A[k]<j:
            A[i+k]=A[k]
            k+=1
        i+=k
        j-=k
    return A

N = I()
S = str(input())

T = ''.join(list(reversed(S)))

dp = [0]*N
for i in range(1,N):
    a = Z_algo(T[N-i-1:])
    b = []
    for j in range(len(a)):
        b.append(min(a[j],j))
    dp[i] = max(dp[i-1], max(b))

print(dp[N-1])