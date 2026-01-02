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
    ans = 0
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
    examA()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""