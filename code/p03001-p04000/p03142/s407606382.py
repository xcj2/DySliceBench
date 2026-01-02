def examD():
    N, M = LI()
    V = [[] for _ in range(N)]
    ans = [0]*N
    Cnt=[0]*(N+1); Cnt[N]=1
    for i in range(N+M-1):
        a, b = LI()
        V[a-1].append(b-1)
        Cnt[b-1] += 1
    root = Cnt.index(min(Cnt))
    que = [root]
#    print(Cnt)
#    print(root)
    while que:
        v = que.pop()
        for u in V[v]:
            if Cnt[u] == 1:
                ans[u] = v+1
                que.append(u)
            else:
                Cnt[u] -= 1
    print(*ans, sep='\n')
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examD()
