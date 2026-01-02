import sys
import bisect
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
LS = LI()
LS.sort()

res = 0
for i in range(N):
    for j in range(i+1,N):
        upper = LS[i]+LS[j]
        lower = abs(LS[i]-LS[j])

        ui = bisect.bisect_left(LS, upper, j+1)
        li = bisect.bisect_left(LS, lower+1, j+1)
        num = ui-li
        res += num
print(res)
