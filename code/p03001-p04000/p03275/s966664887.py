def examA():
    N, i = LI()
    ans = N - i + 1
    print(ans)
    return

def examB():
    H, W = LI()
    A = [SI() for _ in range(H)]
    h = [[]for _ in range(H)]
    for i in range(W):
        flag = False
        for j in range(H):
            if A[j][i]=="#":
                flag = True
                break
        if flag:
            for j in range(H):
                h[j].append(A[j][i])
    #print(h)
    ans = []
    for i,a in enumerate(h):
        if "#" in a:
            ans.append(i)
    for v in ans:
        print("".join(map(str,h[v])))
    return

def examC():
    N, K = LI()
    X = LI()
    ans = inf
    for i in range(N-K+1):
        if X[i]<0 and X[i+K-1]>0:
            cur = (-X[i] + X[i+K-1]) + min(-X[i], X[i+K-1])
        else:
            cur = max(-X[i], X[i+K-1])
        ans = min(ans,cur)
    print(ans)
    return

def examD():
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
    def inversion_number(n,A):
        bit = Bit(n+1)
        rep = 0
        for i, a in enumerate(A):
            bit.add(a, 1)
            rep += i + 1 - bit.sum(a)
        return rep
    N = I()
    A = LI()
    judge = (N*(N+1)//2 + 1)//2
    l = 0; r = max(A)+1
    while(r-l>1):
        #print(l,r)
        now = (l+r)//2
        S = [0]*(N+1)
        cur = N*(N+1)//2
        for i in range(N):
            if A[i]>=now:
                S[i+1] += 1
            else:
                S[i+1] -= 1
                # cur -= 1
        for i in range(1,N):
            S[i+1] += S[i]
            S[i] += N+1
        S[0] += N+1
        S[N] += N+1
        #print(S)
        cur -= inversion_number(2*N+10,S)
        #print(judge,cur,S,now)
        #print(cur,now)
        #input()
        if cur>=judge:
            l = now
        else:
            r = now

    ans = l
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
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

if __name__ == '__main__':
    examD()

"""

"""