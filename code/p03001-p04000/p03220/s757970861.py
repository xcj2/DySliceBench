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
    examB()
