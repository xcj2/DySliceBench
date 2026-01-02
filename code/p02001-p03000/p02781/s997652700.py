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
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

S=input()
K=II()
DP=[[[0]*len(S) for _ in range(K+1)] for _ in range(2)]

for i in range(int(S[0])+1):
    if i < int(S[0]) and i > 0:
        DP[1][1][0] += 1
    elif i == 0:
        DP[1][0][0] = 1
    else:
        DP[0][1][0] = 1

for i in range(1, len(S)):
    n = int(S[i])
    DP[1][0][i] = DP[1][0][i-1]
    for j in range(K):
        DP[1][j+1][i] = (
            # 0の場合
            DP[1][j+1][i-1] +
            # 0以外の場合
            9*DP[1][j][i-1])
        if n != 0:
            DP[1][j+1][i] += (n-1)*DP[0][j][i-1]
            DP[0][j+1][i] = DP[0][j][i-1]

    for j in range(K+1):
        if n != 0:
            DP[1][j][i] += DP[0][j][i-1]
        else:
            DP[0][j][i] = DP[0][j][i-1]

print(DP[1][K][len(S)-1] + DP[0][K][len(S)-1])
