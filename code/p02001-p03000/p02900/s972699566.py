def gcd(a,b):
    if a>b :
        while b!=0:
            a,b = b,a%b
        return a
    else :
        while a!=0:
            a,b = b%a,a
        return b
######################################
def pff(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    return pf
############################
import heapq
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

A, B = LI()
ans = int(1)

cur = gcd(A,B)

ansC = pff(cur)

ans = len(ansC)+1

print(ans)
