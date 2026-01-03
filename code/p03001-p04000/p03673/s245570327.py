def examC():
    N = I()
    a = LI()
    v = [i for i in range(N)]
    if N%2==0:
        ans = a[::-2]
        ans.extend(a[0::2])
    else:
        ans = a[-1::-2]
        ans.extend(a[1::2])
    print(" ".join(map(str,ans)))



import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
