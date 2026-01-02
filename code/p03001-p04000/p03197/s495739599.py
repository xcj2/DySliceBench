def pff(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    return pf
def examC():
    N, P = LI()
    d = pff(P)
#    print(d)
    ans = 1
    for key,i in d.items():
        ans *= key**(i//N)
    print(ans)
    return

def examD():
    N = I()
    A = [I() for _ in range(N)]
    ans = "second"
    for i in A:
        if i%2==1:
            ans = "first"
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
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examD()
