def examA():
    X = [I() for _ in range(5)]
    k = I()
    X.sort()
    ans = "Yay!"
    if X[-1]-X[0]>k:
        ans = ":("
    print(ans)
    return

def examB():
    X = [I() for _ in range(5)]
    ans = 0
    for i in range(5):
        ans += (X[i]+9)//10 *10
        X[i] = (X[i]-1)%10
    ans -= (9-min(X))
    print(ans)
    return

def examC():
    N = I()
    X = [I() for _ in range(5)]
    ans = max(0,(N-1)//min(X))+5
    print(ans)
    return

def examD():
    X, Y, Z, K = LI()
    A = LI(); B = LI(); C = LI()
    A.sort(reverse = True); B.sort(reverse = True); C.sort(reverse = True)
    que = [(-(A[0]+B[0]+C[0]),0,0,0)]
    heapify(que)
    used = defaultdict(bool)
    used[(0,0,0)] = True
    ans = []
    for _ in range(K):
        now,x,y,z = heappop(que)
        ans.append(-now)
        for ix,iy,iz in [[1,0,0],[0,1,0],[0,0,1]]:
            if used[(ix+x,iy+y,iz+z)]:
                continue
            used[(ix+x, iy+y, iz+z)] = True
            if ix+x>=X or iy+y>=Y or iz+z>=Z:
                continue
            next = A[ix+x]+B[iy+y]+C[iz+z]
            heappush(que,(-next,ix+x,iy+y,iz+z))
    for v in ans:
        print(v)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examD()
