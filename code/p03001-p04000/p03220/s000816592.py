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
T,A=LI()
INL=LI()

res = float(INTMAX)
name = 0
for i, h in enumerate(INL,1):
    if abs(A - (T - h*0.006)) < res:
        res = abs(A - (T - h*0.006))
        name = i

print(name)