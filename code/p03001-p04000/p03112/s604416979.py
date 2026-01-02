def nibun(D, x):
    return bisect.bisect_left(D, x)  # 場所返す

import bisect
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)
A,B,Q =LI()
s = [0]*A
t = [0]*B
x = [0]*Q
for i in range(A):
    s[i] = I()
for i in range(B):
    t[i] = I()
for i in range(Q):
    x[i] = I()

ansy = int(0)
for i in range(Q):
    Scandi = [inf] * 2
    Tcandi = [inf] * 2
    xc = x[i]
    k = nibun(s,xc)
    if k>0:
        Scandi[0] = xc - s[k-1]
    if k<A:
        Scandi[1] = s[k] - xc

    k = nibun(t,x[i])
    if k>0:
        Tcandi[0] = xc - t[k-1]
    if k<B:
        Tcandi[1] = t[k] - xc

    anscandi = []
    for i in range(2):
        anst = Scandi[i]*2 + Tcandi[i-1]
        anscandi.append(anst)
        anst = Scandi[i] + Tcandi[i-1]*2
        anscandi.append(anst)
    anst = max(Scandi[0],Tcandi[0])
    anscandi.append(anst)
    anst = max(Scandi[1],Tcandi[1])
    anscandi.append(anst)


    ans = min(anscandi)
    print(ans)
#    print(anscandi)