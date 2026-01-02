from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = inp()
aa = inpl()
aa.sort()

def product():
    if N%3 == 0:
        ax = aa[0:N//3]
        bx = aa[N//3:N//3*2]
        cx = aa[N//3*2:]
        if len(set(ax)) != 1:
            return 'No'
        if len(set(bx)) != 1:
            return 'No'
        if len(set(cx)) != 1:
            return 'No'
        if ax[0]^bx[0] != cx[0]:
            return 'No'
        if bx[0]^cx[0] != ax[0]:
            return 'No'
        if cx[0]^ax[0] != bx[0]:
            return 'No'
        return 'Yes'

    else:
        for a in aa:
            if a != aa[0]:
                return 'No'
        return 'Yes'



print(product())
