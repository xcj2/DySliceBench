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

def gcd(x, y):
    if x < y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    div = x % y
    while div != 0:
        x = y
        y = div
        div = x % y
    return y

def lcm(x, y):
    return x*y//gcd(x, y)


A,B,C,D=LI()

Cnum = B//C - A//C + (not A % C)
Dnum = B//D - A//D + (not A % D)
# print(Cnum)
# print(Dnum)
LC = lcm(C,D)
LCnum = B//LC - A//LC + (not A % LC)

BAISUU = ((Cnum + Dnum) - LCnum)
print((B-A+1) - ((Cnum + Dnum) - LCnum))