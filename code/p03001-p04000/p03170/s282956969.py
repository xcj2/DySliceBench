import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N,K=LI()
INL=LI()
DP=[False]*(K+1)

for i in range(0,K+1):
    for v in INL:
        if v+i <= K:
            DP[v+i] = DP[v+i] or not DP[i]

# print(DP)
print('First' if DP[K] else 'Second')
