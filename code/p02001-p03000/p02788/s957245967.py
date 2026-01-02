def examA():
    N = I()
    L = LI()
    L.sort()
    if sum(L)<=L[-1]*2:
        print("No")
    else:
        print("Yes")
    return

def examB():
    N, M = LI()
    A = [LI()for _ in range(N)]
    A.sort(key=lambda x:x[0])
    ans = 0
    for a,b in A:
        if M<=b:
            ans += a*M
            break
        ans += a*b
        M -= b
    print(ans)
    return

def examC():
    N = I()
    S = [SI()for _ in range(N)]
    D = defaultdict(int)
    for s in S:
        cur = []
        for i,j in Counter(s).items():
            cur.append((i,j))
        #print(cur)
        cur.sort()
        cur = tuple(cur)
        D[cur] += 1
    ans = 0
    for d in D.values():
        ans += (d-1)*d//2
    print(ans)
    return

def examD():
    N, K = LI()
    A = LI()
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i]+A[i]
    ans = 0
    for i in range(N):
        l = i-1; r = N
        if S[-1]-S[i]<K:
            break
        while(r-l>1):
            now = (l+r)//2
            if S[now]-S[i]<K:
                l = now
            else:
                r = now
        #print(i,r)
        ans += (N-r+1)
    print(ans)
    return

def examE():
    # 区間加算、上書き、一点取得
    class SegmentTree:
        def __init__(self, n, ele, segfun):
            #####単位元######要設定0or1orinf
            self.ide_ele = ele
            self.segfun = segfun
            ####################
            self.n = n
            self.N0 = 1 << n.bit_length()
            self.data = [self.ide_ele] * (self.N0 * 2)

        def update_add(self, l, r, val):
            l += self.N0
            r += self.N0
            while l < r:
                if l & 1:
                    self.data[l] += val
                    l += 1
                if r & 1:
                    self.data[r - 1] += val
                    r -= 1
                l //= 2
                r //= 2

        def update(self, l, r, val):
            l += self.N0
            r += self.N0
            while l < r:
                if l & 1:
                    self.data[l] = self.segfun(self.data[l], val)
                    l += 1
                if r & 1:
                    self.data[r - 1] = self.segfun(self.data[r - 1], val)
                    r -= 1
                l //= 2
                r //= 2

        def query(self, i):
            i += len(self.data) // 2
            ret = self.data[i]
            while i > 0:
                i //= 2
                ret = self.segfun(ret, self.data[i])
            return ret

    N, D, A = LI()
    X = [LI()for _ in range(N)]
    X.sort()
    L = [0]*N
    for i in range(N):
        L[i] = X[i][0]
    S = SegmentTree(N,0,lambda a, b: a+b)
    ans = 0
    for i,[x,h] in enumerate(X):
        H = h - S.query(i)
        if H<=0:
            continue
        ne = bisect.bisect_right(L,x+2*D)
        #print(ne)
        need = (H-1)//A + 1
        S.update(i,ne,need*A)
        ans += need
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""