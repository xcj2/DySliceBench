def examA():
    N, M = LI()
    l = 1; r = N
    for _ in range(M):
        L, R = LI()
        l = max(L,l)
        r = min(R,r)
    ans = max(0,r-l+1)
    print(ans)
    return

def examB():
    N = I()
    S = [I()for _ in range(N)]
    rest = []
    for s in S:
        if s%10==0:
            continue
        rest.append(s)
    if sum(S)%10==0:
        if not rest:
            print(0)
            return
        ans = sum(S) - min(rest)
    else:
        ans = sum(S)
    print(ans)
    return

def examC():
    N, K = LI()
    K -= 1
    A = LI()
    L = A.index(1)
    #print(L)
    ans = (N-1+K-1)//K
    print(ans)
    return

def examD():
    def ketadp(a):
        n = len(a)
        dp = defaultdict(int)
        dp[0, 0, 0, 0, 0] = 1
        for i, less, has3, has5, has7 in itertools.product(range(n), (0, 1), (0, 1), (0,1), (0,1)):
            max_d = 7 if less else int(a[i])
            for d in range(max_d + 1):
                if d==0 and has3==0 and has5==0 and has7==0:
                    dp[i + 1, 1, has3, has5, has7] += dp[i, less, has3, has5, has7]
                if not (d==3 or d==5 or d==7):
                    continue
                less_ = less or d < max_d
                has3_ = has3 or d == 3
                has5_ = has5 or d == 5
                has7_ = has7 or d == 7
                dp[i + 1, less_, has3_, has5_, has7_] += dp[i, less, has3, has5, has7]

        ans = sum(dp[n, less, 1, 1, 1] for less in (0, 1))
        return ans
    N = SI()
    ans = ketadp(N)
    print(ans)
    return

def examE():
    N = I()
    A = [I()for _ in range(N)]
    que = deque()
    que.append(A[0])
    for a in A[1:]:
        cur = bisect.bisect_left(que,a)
        if cur==0:
            que.appendleft(a)
        else:
            que[cur-1] = a
    ans = len(que)
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