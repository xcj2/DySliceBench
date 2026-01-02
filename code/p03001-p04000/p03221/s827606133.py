def examA():
    X, Y = LI()
    ans = X + Y//2
    print(ans)
    return

def examB():
    N = I()
    T, A = LI()
    H = LI()
    cur = 10**9; ans = 0
    for i in range(N):
        now = abs(A - (T - H[i]*0.006))
        if cur>now:
            cur = now
            ans = i
    print(ans+1)
    return

def examC():
    N, M = LI()
    PY = [[]for _ in range(M)]
    d = defaultdict(int)
    ans = [[]for _ in range(M)]
    for i in range(M):
        PY[i] = LI()
        PY[i].append(i)
    PY.sort(key=lambda x:x[1])
    for p,y,s in PY:
        d[p] +=1
        cur = str(p).zfill(6) + str(d[p]).zfill(6)
        ans[s] = cur
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
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examC()
