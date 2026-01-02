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
RES=[0]*(N+1)
cnt = 0
for i in range(N, 0, -1):
    pt = 2*i
    sm = 0
    while pt <= N:
        sm += RES[pt]
        pt += i
    if (not sm & 1 and INL[i-1]) or (sm & 1 and not INL[i-1]):
        cnt += 1
        RES[i] = 1

print(cnt)
if cnt:
    for i in range(N+1):
        if RES[i]: print(i, end=' ')
    print('')
