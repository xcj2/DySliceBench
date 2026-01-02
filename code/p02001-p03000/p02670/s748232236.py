def examA():
    T = I()
    ans = [inf]*T
    for t in range(T):
        N, A, B, C, D = LI()
        num = [[2,A],[3,B],[5,C]]
        dp = defaultdict(lambda: inf)
        dp[N] = 0
        que = deque()
        que.append(N)
        while(que):
            now = que.pop()
            if now==0:
                continue
            cur = dp[now] + D*now
            if cur<dp[0]:
                dp[0] = cur
            cur = dp[now]
            for n,K in num:
                curn = cur + (now % n) * D + K
                if curn < dp[(now - now % n) // n]:
                    dp[(now - now % n) // n] = curn
                    que.append((now - now % n) // n)
                curn_ = cur + (-now % n) * D + K
                if curn_ < dp[(now + (-now % n)) // n]:
                    dp[(now + (-now % n)) // n] = curn_
                    que.append((now + (-now % n)) // n)
        ans[t] = dp[0]
    for v in ans:
        print(v)
    return

def examB():
    N = I()
    P = LI()
    L = [[min(i,j,N+1-i,N+1-j)for i in range(1,N+1)]for j in range(1,N+1)]
    exist = [[1]*N for _ in range(N)]
    cost = 0
    def bfs(s):
        que = deque()
        que.appendleft(s)

        def calc_L(h, w, h1, w1):
            c = L[h][w] + exist[h + h1][w + w1]
            if c < L[h + h1][w + w1]:
                L[h + h1][w + w1] = c
                s1 = (h + h1) * N + (w + w1) + 1
                # print("append",s1)
                que.appendleft(s1)
            return

        while(que):
            now = que.pop()
            h,w = (now-1)//N,(now-1)%N
            if 0<h:
                calc_L(h,w,-1,0)
            if h+1<N:
                calc_L(h,w,1,0)
            if 0<w:
                calc_L(h,w,0,-1)
            if w+1<N:
                calc_L(h,w,0,1)

        return

    #for l in L:
        #print(l)
    #print("start")
    for p in P:
        h,w = (p-1)//N,(p-1)%N
        exist[h][w] = 0
        if 0<L[h][w]:
            L[h][w] -= 1
        bfs(p)
        cost += L[h][w]
        #print(p,cost)
    #for l in exist:
        #print(l)
    ans = cost
    print(ans)
    return

def examB2():
    N = I()
    P = LI()
    L = [min(i,j,N+1-i,N+1-j) for i in range(1,N+1) for j in range(1,N+1)]
    exist = [1]*(N**2)
    cost = 0
    def bfs(s):
        que = deque()
        que.appendleft(s)

        def calc_L(s, s1):
            c = L[s] + exist[s1]
            if c < L[s1]:
                L[s1] = c
                que.appendleft(s1)
            return

        while(que):
            now = que.pop()
            if 0<now:
                calc_L(now,now-1)
            if now+1<N**2:
                calc_L(now,now+1)
            if 0<=now-N:
                calc_L(now,now-N)
            if now+N<N**2:
                calc_L(now,now+N)

        return

    for p in P:
        p -= 1
        exist[p] = 0
        if 0<L[p]:
            L[p] -= 1
        bfs(p)
        cost += L[p]
    ans = cost
    print(ans)
    return

def examC():
    ans = 0
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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
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

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examB2()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""