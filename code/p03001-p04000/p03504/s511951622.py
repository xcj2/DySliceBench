def examA():
    C1 = SI()
    C2 = SI()
    ans = "YES"
    if C1[0]!=C2[2] or C1[1]!=C2[1] or C1[2]!=C2[0]:
        ans = "NO"
    print(ans)
    return

def examB():
    A, B, C, X, Y = LI()
    loop = max(X,Y)
    ans = inf
    for i in range(loop+1):
        cost = i*2*C
        if X>i:
            cost += A*(X-i)
        if Y>i:
            cost += B*(Y-i)
        ans = min(ans,cost)
    print(ans)
    return

def examC():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x
    N, x = LI()
    X = LI()
    if N==1:
        print(abs(X[0]-x))
        return
    for i in range(N):
        X[i] = abs(X[i]-x)
    now = gcd(X[0],X[1])
    for i in range(2,N):
        now = gcd(now,X[i])
    ans = now
    print(ans)
    return

def examD():
    N = I()
    C = [LI()for _ in range(N-1)]
    ans = [inf]*N
    for i in range(N):
        cur = 0
        for j in range(i,N-1):
            c, s, f = C[j]
            next = 0
            if cur<=s:
                cur = s+c
            else:
                cur = (1+(cur-1)//f)*f + c
        ans[i] = cur
    for v in ans:
        print(v)
    return

def examE():
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
        def add(self, k, x=1):
            k += self.num
            self.seg[k] += x
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
    N, C = LI()
    S = defaultdict(list)
    T = 0
    for _ in range(N):
        s,t,c = LI()
        c -= 1
        T = max(t,T)
        S[c].append([s,t])
    Seg = segment_([0]*(T+1), (T+1), lambda a, b: a + b)
    for i in range(C):
        if not S[i]:
            continue
        S[i].sort()
        #print(S[i])
        Seg.add(S[i][0][0])
        Seg.add(S[i][0][1] + 1, -1)
        for j in range(1,len(S[i])):
            s,t = S[i][j]
            if S[i][j-1][1]==s:
                Seg.add(s + 1)
                Seg.add(t + 1, -1)
            else:
                Seg.add(s)
                Seg.add(t + 1, -1)
    ans = 0
    for j in range(T):
        cur = Seg.query(0,j+1)
        ans = max(ans,cur)
    print(ans)
    return

def examF():
    class combination():
        # 素数のmod取るときのみ　速い
        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod
    N, M, K = LI()
    B = N*M
    C = combination(B,mod)
    ans = 0
    for i in range(N):
        for j in range(M):
            if i>0 and j>0:
                ans += (i+j)*(N - i) * (M - j) * C.comb(B - 2, K-2) *2
            else:
                ans += (i+j)*(N - i) * (M - j) * C.comb(B - 2, K-2)
            ans %= mod
            #print(ans)
    print(ans)
    return

from decimal import Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
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