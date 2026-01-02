def examD():
    N, C = LI()
    S = [0] * N; T = [0] * N; c = [0] * N
    # s = t = c =0
    maxt = int(0)
    for i in range(N):
        s, t, a = LI()
        S[i], T[i] = s, t
        c[i] = a
        if maxt < t:
            maxt = t
    pairs = zip(S, T,c)
    sortedpairs = sorted(pairs, key=lambda x: x[1])
    sortedpairs = sorted(sortedpairs, key=lambda x: x[0])
    for i in range(N):
        S[i] = sortedpairs[i][0]
        T[i] = sortedpairs[i][1]
        c[i] = sortedpairs[i][2]
#    print(S)
#    print(T)
#    print(c)
    ans = int(0)
    time = [0] * (maxt + 2)
    timeC = [[] for _ in range(maxt + 2)]
    for i in range(N):
        ##########同じチャンネル
        timeC[T[i]].append(c[i])
        if not c[i] in timeC[S[i]]:
            time[S[i]] += 1
            time[T[i] + 1] -= 1
        else:
            time[S[i] + 1] += 1
            time[T[i] + 1] -= 1

    ansC = int(0)
    for i in range(maxt + 1):
        ansC += time[i]
        ans = max(ansC, ans)
    # print(time)
    print(ans)
    # print(timeC)

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
