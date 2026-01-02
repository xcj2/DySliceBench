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

curr=[1, 6, 36, 216, 1296, 7776, 46656, 279936, 9, 81, 729, 6561, 59049, 531441]
curr.sort()
# print(curr)

N=II()
DP=[10000000]*(N+1)
DP[N]=0

for i in reversed(range(0, N+1)):
    for c in curr:
        if i-c >= 0: DP[i-c] = min(DP[i]+1, DP[i-c])
print(DP[0])
