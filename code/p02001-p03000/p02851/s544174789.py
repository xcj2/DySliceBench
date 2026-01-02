def examE():
    N, K = LI()
    A = LI()
    sumA = [0]*(N+1)
    for i in range(1,N+1):
        sumA[i] = sumA[i-1]+A[i-1]
    d = defaultdict(int)
    ans = 0
    #連想配列 先頭からの番号　余分な量
    que = deque()
    for i,a in enumerate(sumA):
        #K番目以降は一番左のやつ消していく
        if que and que[0][0] <= (i-K):
            d[que.popleft()[1]] -= 1
        cur = (a-i)%K
        ans +=d[cur]
        d[cur] +=1
        que.append((i,cur))
#        print(ans,que,d,a-i)
    print(ans)
    return

def examF():
    return

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examE()
