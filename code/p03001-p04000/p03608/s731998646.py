import sys
from itertools import permutations
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LLI(n): return [[int(x) for x in input().split()] for _ in range(n)]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


N,M,R = LI()
RS=LI()
mp = [[10**10]*(N+1) for _ in range(N+1)]
for a,b,c in LLI(M):
    mp[a][b] = c
    mp[b][a] = c

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

res = INTMAX
for l in permutations(RS):
    sc = 0
    for i in range(R-1): 
        sc += mp[l[i]][l[i+1]]
    res = min(res,sc)
print(res)
