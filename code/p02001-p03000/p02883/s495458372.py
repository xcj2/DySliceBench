import sys
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N,K=LI()
As=LI()
As.sort()
Fs=LI()
Fs.sort(reverse=True)

rgt = 10**12
lft = 0
while lft < rgt:
    cost = K
    half = (lft + rgt) // 2
    for i in range(N):
        if As[i]*Fs[i] > half:
            cost -= (As[i]*Fs[i] - half) // Fs[i]
            cost -= 1 if (half - As[i]*Fs[i]) % Fs[i] > 0 else 0

    if cost < 0:
        lft = half + 1
    else:
        rgt = half
    # print(lft, rgt)

print(rgt)
