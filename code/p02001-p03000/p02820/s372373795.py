import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N,K=LI()
SC=LI()
T=input()

DP=[[[0]*3 for _ in range(K)] for _ in range(N//K + (1 if N%K else 0))]

for i in range(N):
    cur = i//K
    rest = i%K
    v = 0 if T[i] == 'r' else (1 if T[i] == 's' else 2)
    if cur > 0:
        # 負ける場合
        DP[cur][rest][v] = max(DP[cur-1][rest][(v+1)%3], DP[cur-1][rest][(v+2)%3])
        DP[cur][rest][(v+1)%3] = max(DP[cur-1][rest][v], DP[cur-1][rest][(v+2)%3])
        # 勝つ場合
        DP[cur][rest][(v+2)%3] = max(DP[cur-1][rest][v], DP[cur-1][rest][(v+1)%3]) + SC[(v+2)%3]
    else:
        # 負ける場合
        DP[cur][rest][v] = 0
        DP[cur][rest][(v+1)%3] = 0
        # 勝つ場合
        DP[cur][rest][(v+2)%3] = SC[(v+2)%3]

res = 0

for i in range(N-K, N):
    cur = i//K
    rest = i%K
    # print(DP[cur][rest])
    res += max(DP[cur][rest])
print(res)
