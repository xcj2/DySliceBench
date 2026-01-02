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
INL=LI()

a = [0]*N
for i in range(N):
    a[0] += INL[i] if i%2 == 0 else -INL[i]

for i in range(1, N):
    a[i] = 2*INL[i-1]-a[i-1]

print(*a)
