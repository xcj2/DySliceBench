import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        Parameters
        ----------
        u:int
            from node
        v:int
            to node
        d:int
            cost
        directed:bool
            there is direction
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

    def delete(self, u, v):
        """
        Parameters
        ----------
        u:int
            from node
        v:int
            to node
        """
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        Parameters
        ----------
        s:int
            start node

        Return
        ----------
        d:dict(int:int)
            shortest cost from start node to each node 
            {to : cost}

        prev:dict(int:int)
            previous node on the shortest path
            {from : to}
        """
        d = collections.defaultdict(lambda: float('inf'))
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s)) # (cost, 探索候補ノード)
        v = collections.defaultdict(bool) # 確定済かどうか
        while len(q):
            # ノードuにおけるコストはk
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]: # cost is ud from u to uv
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev

    def getDijkstraShortestPath(self, start, goal):
        """
        Parameters
        ----------
        start:int
            start node
        goal:int
            goal node

        Return
        ----------
        ShortestPath:list(int)
            shortest path
        """
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]

n, m, s = inpl()
LIMIT_SILVER = 2500
s=min(s,LIMIT_SILVER-1)
graph = Dijkstra()
for i in range(m):
    u,v,a,b = inpl()
    for j in range(a,LIMIT_SILVER):
        graph.add((u,j), (v,j-a), b, directed=True)
        graph.add((v,j), (u,j-a), b, directed=True)
for i in range(n):
    c,d = inpl()
    for j in range(c,LIMIT_SILVER):
        graph.add((i + 1, j - c), (i + 1, j), d, directed=True)
# print(graph.e)
costs,_ = graph.Dijkstra_search((1,s))
# print(costs)
for i in range(2, n + 1):
    ans=INF
    for j in range(2500):
        ans = min(ans, costs[(i, j)])
    print(ans)
# path = graph.getDijkstraShortestPath((1, s), (3, 0))
# print(path)

