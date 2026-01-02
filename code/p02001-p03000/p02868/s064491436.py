def examA():
    N = I()
    ans = (N-1)//2
    print(ans)
    return

def examB():
    N = I()
    D = LI()
    d = Counter(D)
    loop = max(d.keys())
    if D[0]!=0 or d[0]!=1:
        print(0)
        return
#    print(d,loop)
    ans = 1; cur = 1
    for i in range(loop+1):
        if d[i]==0:
            print(0)
            return
        for _ in range(d[i]):
            ans *= cur
            ans %= mod2
        cur = d[i]
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    class Dijkstra(object):
        """
        construct: O(ElogV)
        """

        def __init__(self, edges, start=0):
            """
            :param list of list of list of int edges:
            :param int start=0:
            """
            self.__dist = [inf] * len(edges)
            self.__dist[start] = 0
            self.__calculate(edges, start)

        @property
        def dist(self):
            return self.__dist

        def __calculate(self, edges, start):
            Q = [(0, start)]  # (dist,vertex)
            while (Q):
                dist, v = heapq.heappop(Q)
                if self.dist[v] < dist: continue  # 候補として挙がったd,vだが、他に短いのがある
                for u, cost in edges[v]:
                    if self.dist[u] > self.dist[v] + cost:
                        self.__dist[u] = self.dist[v] + cost
                        heapq.heappush(Q, (self.dist[u], u))
    N, M = LI()
    V = [[]for _ in range(N)]
    for _ in range(M):
        l, r, c = LI()
        l -=1; r -=1
        V[l].append((r,c))
    for i in range(N-1):
        V[i+1].append((i,0))
#    print(V)
    D = Dijkstra(V)
    ans = D.dist[N-1]
    if ans==inf:
        ans = -1
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

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()

"""

"""