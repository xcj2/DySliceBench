def examA():
    H,A = LI()
    ans = (H-1)//A+1
    print(ans)
    return

def examB():
    H, N = LI()
    A = LI()
    if H>sum(A):
        print("No")
    else:
        print("Yes")
    return

def examC():
    N, K = LI()
    H = LI()
    H.sort()
    ans = sum(H[:max(0,N-K)])
    print(ans)
    return

def examD():
    H = I()
    ans = 2**(H.bit_length())-1
    print(ans)
    return

def examE():
    H, N = LI()
    A = [0]*N; B = [0]*N
    for i in range(N):
        A[i],B[i] = LI()
    dp = [inf]*(H+1)
    dp[0] = 0
    ans = inf
    for j in range(N):
        a,b = A[j],B[j]
        for i in range(H+1-a):
            dp[i + a] = min(dp[i + a], dp[i] + b)
        for i in range(min(a + 1, H + 1)):
            dp[H] = min(dp[H], dp[H-i] + b)
    ans = dp[H]
    print(ans)
    return

def examF():
    class segment_():
        def __init__(self, A, n, segfunc):
            #####単位元######要設定0or1orinf
            self.ide_ele = 0
            ####################
            self.num = 1 << (n - 1).bit_length()
            self.seg = [self.ide_ele] * 2 * self.num
            self.segfunc = segfunc
            # set_val
            for i in range(n):
                self.seg[i + self.num] = A[i]
                # built
            for i in range(self.num - 1, 0, -1):
                self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

        def update(self, k, r):
            k += self.num
            self.seg[k] = r
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        # 値xに1加算
        def update_add(self, k,u):
            k += self.num
            self.seg[k] += u
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def updateneg1(self, k):
            k += self.num
            self.seg[k] -= 1
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def query(self, p, q):
            if q < p:
                return self.ide_ele
            p += self.num;
            q += self.num
            res = self.ide_ele
            while p < q:
                if p & 1 == 1:
                    res = self.segfunc(res, self.seg[p])
                    p += 1
                if q & 1 == 1:
                    q -= 1
                    res = self.segfunc(res, self.seg[q])
                p >>= 1;
                q >>= 1
            return res
    N, D, A = LI()
    XH = [LI() for _ in range(N)]
    XH.sort(key = lambda x:x[0])
    X = [0]*N
    for i in range(N):
        X[i] = XH[i][0]
    B = [0] * (N + 1)
    S = segment_(B,(N+1),lambda a, b: a+b)
    ans = 0
    for i in range(N):
        cur = (XH[i][1]-1)//A +1
        left = bisect.bisect_left(X,X[i]-D*2)
#        print(now)
        cur -= min(S.query(left,i),cur)
        ans +=cur
        S.update_add(i,cur)
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
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examE()

"""

"""