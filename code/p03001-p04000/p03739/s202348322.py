def examC():
    N = I()
    a = LI()
    ansC = []
    """
        if a[0]<0:
        for i in range(N):
            a[i] = -a[i]
    """
    for l in range(2):
        sumA = 0
        ans = 0
        for i in range(N):
            sumA += a[i]
            if (i + l) % 2 == 0:
                if sumA >= 0:
                    ans += abs(sumA)+1
                    sumA = -1
            else:
                if sumA <= 0:
                    ans += abs(sumA)+1
                    sumA = 1
        ansC.append(ans)
    print(min(ansC))

import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
