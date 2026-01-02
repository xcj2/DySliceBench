###########################################
class Bit():
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        return
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        return
def programer1B():
    N, K = LI()
    A = LI()
    bit = Bit(max(A))
    cur = 0
    for i, a in enumerate(A):
        bit.add(a, 1)
        cur += i + 1 - bit.sum(a)
    As = 0
    A.sort()
    now = 0
    for i in range(1,N):
        if A[i]!=A[i-1]:
            now = i
        As += now
#    print(cur,As)
    ans = (As*(K**2) - (As-2*cur)*K)//2
    ans %=mod
    print(ans)
    return

def ABC106():
    N, M, Q = LI()
    R = []
    for i in range(M):
        l, r = LI()
        R.append([l,r,0])
    for i in range(Q):
        p, q = LI()
        R.append([p,q,i+1])
    R.sort(key=lambda x:x[1])
#    print(R)
    B = Bit(N+1)
    ans = [0]*Q
    for x,y,t in R:
        if t==0:
            B.add(x,1)
        else:
            cur = B.sum(y+1) - B.sum(x-1)
            ans[t-1] = cur
    for v in ans:
        print(v)
    return

####################################################################
import sys, copy, bisect, itertools, heapq, math
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LSI(): return list(map(str, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod, mod2, inf
mod = 10 ** 9 + 7
mod2 = 998244353
inf = 10 ** 18

if __name__ == '__main__':
#    programer1B()
    ABC106()
