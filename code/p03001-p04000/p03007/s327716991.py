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


N=II()
INL=LI()

INL.sort()

ma = INL[-1]
mi = INL[0]

INL = INL[1:-1]

resl = []
if INL:
    if mi > 0:
        for i in INL:
            resl.append((mi,i))
            mi -= i
    else:
        for i in INL:
            if i < 0:
                resl.append((ma,i))
                ma -= i
            else:
                resl.append((mi,i))
                mi -= i

print(ma - mi)
for li in resl:
    print(li[0], li[1])
print(ma, mi)
