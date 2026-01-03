def examC():
    N = I()
    St = [S() for _ in range(N)]
    d = [[0]*N for _ in range(26)]
    ans = ""
    for i in range(N):
        for s in St[i]:
            d[ord(s)-97][i] += 1
    for i in range(26):
        cur = min(d[i])
        for _ in range(cur):
            ans = ans + chr(i+97)
    print(ans)


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
