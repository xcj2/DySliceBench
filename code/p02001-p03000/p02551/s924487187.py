def main():
    examF()

def examA():
    S = SI()
    if S[-1]=="s":
        ans = S+"es"
    else:
        ans = S+"s"
    print(ans)
    return

def examB():
    N = I()
    D = [LI()for _ in range(N)]
    current = 0
    for d1,d2 in D:
        if d1==d2:
            current += 1
        else:
            current = 0
        if current==3:
            print("Yes")
            return
    print("No")
    return

def examC():
    N = I()
    cnt = 0
    for i in range(1,N):
        for j in range(1,1+N//i-(N%i==0)):
            cnt += 1
    ans = cnt
    print(ans)
    return

def examD():
    N, K = LI()
    LR = [LI()for _ in range(K)]
    dp = [0]*N
    S = [0]*N
    dp[0] = 1
    S[0] = 1
    for i in range(1,N):
        cur = 0
        for l,r in LR:
            if i<l:
                continue
            cur += S[i-l]
            if i<r+1:
                continue
            cur -= S[i-r-1]
            cur += mod2
            cur %= mod2

        dp[i] = cur
        S[i] = S[i-1] + cur
        S[i] %= mod2

    ans = dp[-1]
    print(ans)
    return

def examE():
    N, X, M = LI()
    cnt = 0
    L = []
    used = [-1]*(M+1)

    for i in range(N):
        used[X] = i
        L.append(X)
        cnt += X
        X = pow(X,2,M)
        if X==1 or X==0:
            cnt += (N-i-1)*X
            break
        if used[X]>=0:
            loop = i - used[X] + 1
            S = sum(L[used[X]:i+1])
            rest = N-i-1
            cnt += (rest//loop) * S + sum(L[used[X]:used[X]+rest%loop])
            break
    #print(L)
    #print(used)
    ans = cnt
    print(ans)
    return
def examF():
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
    N, Q = LI()
    SH = SegmentTree(N,N-2,lambda a, b: min(a,b))
    SW = SegmentTree(N,N-2,lambda a, b: min(a,b))
    cnt = 0
    for q in range(Q):
        t, x = LI()
        if t==1:
            up_w_0 = SH.query(x - 2)
            cnt += up_w_0
            SW.update(0, up_w_0, x - 2)
            #print(q,up_w_0)
        elif t==2:
            left_h_0 = SW.query(x-2)
            cnt += left_h_0
            SH.update(0,left_h_0,x-2)
            #print(q,left_h_0,x-2)
        #print(cnt)
    #print(cnt)
    ans = (N-2)**2 - cnt
    print(ans)
    return

from decimal import getcontext,Decimal as dec
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
global mod,mod2,inf,alphabet,alphabet_convert,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 1<<31
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    main()

"""
10 4 6 
"""