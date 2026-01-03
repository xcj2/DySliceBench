def examD():
    N, A, B = LI()
    h = [I() for _ in range(N)]
    upper = max(h); lower = 1; cur = (upper+lower)//2
    while (True):
        curne = 0
        for i in h:
            if i-cur*B>0:
                curne  += (i-cur*B-1)//(A-B) +1
        if upper - lower >= 2:
            if curne > cur:
                #条件満たさない
                lower = cur
                cur = (cur + upper) // 2
            else:
                upper = cur
                cur = (cur + lower) // 2
        else:
            if curne > cur:
                #条件満たさない
                cur = upper
                curne = 0
                for i in h:
                    if i - cur * B > 0:
                        curne += (i - cur * B - 1) // (A - B) + 1
                if curne > cur:
                    break
            else:
                cur = lower
                curne = 0
                for i in h:
                    if i - cur * B > 0:
                        curne += (i - cur * B - 1) // (A - B) + 1
                if curne < cur:
                    ans = lower
                    break
            ans = upper
            break
    print(ans)



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

examD()
