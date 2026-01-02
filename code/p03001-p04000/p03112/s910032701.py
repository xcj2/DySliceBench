import sys,collections,math,itertools,bisect;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

A,B,Q = Is()
As,Bs = [],[]
for i in range(A):
    As.append(I())
for i in range(B):
    Bs.append(I())
for i in range(Q):
    x = I()
    a = bisect.bisect_left(As,x)
    b = bisect.bisect_left(Bs,x)
    ans = 10**11
    As.append(10**11) if a == A else 0
    Bs.append(10**11) if b == B else 0
    AR = As[a] - x
    AL = x - As[a-1] if 0 < a  else 10**11
    BR = Bs[b] - x 
    BL = x - Bs[b-1] if 0 < b  else 10**11
    print(min(max(AL,BL),max(AR,BR),AL+BR+min(AL,BR),BL+AR+min(BL,AR)))
