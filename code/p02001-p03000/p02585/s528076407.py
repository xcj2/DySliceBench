import math
import sys
import os

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

N,K = LI()
P = LI()
C = LI()

P = list(map(lambda x:x-1,P))

res = -INF
used = [False] * N
ss = []

for i in range(N):
    # print('i',i)
    if used[i]:
        continue
    cur = i
    s = []
    while not used[cur]:
        used[cur] = True
        s.append(C[cur])
        cur = P[cur]
        # print(cur)
    ss.append(s)

# print(ss)

for vec in ss:
    M = len(vec)
    # 2周の累積和
    sum = [0]*(2*M + 1)
    for i in range(2*M):
        sum[i+1] = sum[i]+vec[i%M]
    
    # amari[r] := 連続するr個の最大値
    amari = [-INF]*M
    for i in range(M):
        for j in range(M):
            amari[j] = max(amari[j],sum[i+j] - sum[i])
    
    for r in range(M):
        if r>K:
            continue
        q = (K-r)//M
        if r==0 and q==0:
            continue
        if sum[M]>0:
            res = max(res, amari[r] + sum[M] * q)
        elif r > 0:
            res = max(res, amari[r])
print(res)


