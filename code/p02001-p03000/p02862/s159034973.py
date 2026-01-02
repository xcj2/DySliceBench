import math
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

X,Y=LI()

a = (2*X - Y) // 3
b = (2*Y - X) // 3

FACT = [1]*1000001
for i in range(1, 1000001):
    FACT[i] = (FACT[i-1]*i)%MOD

if (2*X - Y)%3 == 0 and (2*Y - X)%3 == 0 and a >= 0 and b >= 0:
    print(DIV(DIV(FACT[a+b], FACT[a]), FACT[b]))
else:
    print(0)
