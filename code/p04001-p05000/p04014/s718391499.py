def examD():
    def f(b, n):
        if n < b:
            return n
        else:
            return f(b, n // b) + n % b
    n = I(); s = I()
    ans = -1
    if s==n:
        ans = n+1
    else:
        loop = int(n**(0.5))
        for b in range(2,loop+1):
            if f(b,n)==s:
                ans = b
                break
    if ans==-1:
        for p in range(loop+1,0,-1):
            b = (n-s)//p + 1
            if b >= 2 and f(b,n)==s:
                    ans = b
                    break

    print(ans)

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
