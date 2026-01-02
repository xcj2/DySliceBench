import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N=II()
INL=list(map(float, LS()))
DP=[0.0]*(N+1)
DP[0]=1.0

for p in INL:
    for i in reversed(range(N)):
        DP[i+1] = DP[i+1]*(1.0-p) + DP[i]*p

# print(DP)
print(DP[N//2+1])