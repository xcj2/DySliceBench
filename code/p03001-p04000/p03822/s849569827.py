def examA():
    N = I()
    A = [0]*N; B = [0]*N
    for i in range(N):
        A[i], B[i] = LI()
    cum = 0
    for i in range(N)[::-1]:
        cum +=(-(cum+A[i]))%B[i]
        #print(cum)

    ans = cum
    print(ans)
    return

def examB():
    N = I()
    V = [[]for _ in range(N)]
    for i in range(1,N):
        a = I()-1
        V[a].append(i)
    #print(V)
    dp = [0]*N
    def dfs(n,s):
        children = []
        for i in V[s]:
            child = dfs(n,i)
            children.append(child)
        rep = 0
        children.sort()
        for i,c in enumerate(children[::-1],start = 1):
            rep = max(rep,i+c)
        dp[s] = rep
        return rep
    ans = dfs(N,0)
    print(ans)
    return

def examC():
    class segment_():
        def __init__(self, A, n, segfunc, ide_ele=0):
            #####単位元######要設定0or1orinf
            self.ide_ele = ide_ele
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
        def update1(self, k):
            k += self.num
            self.seg[k] += 1
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
            # qは含まない
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

    N, A, B = LI()
    S = [I()for _ in range(N)]
    S.insert(0,-inf)
    #print(S)
    if A>B:
        A,B = B,A
    for i in range(N-1):
        if S[i+2]-S[i]<A:
            print(0)
            return
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    num = N+1
    L = [0] * num
    Seg_sum = segment_(L, num, lambda a, b: a + b)
    la = 0; lb = -1
    Seg_sum.update(0,1)
    Seg_sum.update(1,1)
    for i in range(1,N):
        while(lb<i and S[i+1]-S[lb+1]>=B):
            lb += 1
        dp[i+1] = Seg_sum.query(0,lb+1)
        Seg_sum.update(i+1,dp[i+1])
        #dp[i+1] = sum(dp[:lb+1])
        if S[i+1]-S[i]<A:
            for a in range(la,i):
                Seg_sum.update(a,0)
                dp[a] = 0
            la = i
        #print(dp)
    #print(dp)

    ans = sum(dp)
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
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
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examB()

"""

"""