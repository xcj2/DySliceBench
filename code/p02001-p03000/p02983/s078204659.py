def examA():
    N, A, B = LI()
    ans = min(A*N,B)
    print(ans)
    return

def examB():
    N, D = LI()
    X = [LI() for _ in range(N)]
    ans = 0
    for i,j in itertools.combinations(X,2):
        cur = 0
        for k in range(D):
            cur += (i[k]-j[k])**2
        cur **=0.5
        if cur==int(cur):
            ans +=1
    print(ans)
    return

def examC():
    L, R = LI()
    cur = []; ans = 10**9
    for i in range(L,min(2019+L,R)+1):
        if i%2019==0:
            ans = 0
            break
        else:
            cur.append(i%2019)
    if ans==0:
        print(ans)
        return
    N = len(cur)
    for i,j in itertools.combinations(cur,2):
        ans = min(ans,(i*j)%2019)
    print(ans)
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
    examC()
