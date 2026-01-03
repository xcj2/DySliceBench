def examC(mod):
    N = I()
    A = LI()
    num = (N+1)%2
    loop = (N+1)//2
    cur = int(1)
    L = [0]*loop
    if num==0:
        L[0] +=1
    for i in range(N):
        L[A[i]//2] += 1
        if L[A[i]//2]>=3:
            cur = int(0)
            break
    for _ in range(N//2):
        cur = (cur*2)%mod
    print(cur)





import sys
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC(mod)
