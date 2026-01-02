import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
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


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


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
        heapq.heappush(q, (0, s))  # (cost, 探索候補ノード)
        v = collections.defaultdict(bool)  # 確定済かどうか
        while len(q):
            # ノードuにおけるコストはk
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:  # cost is ud from u to uv
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev

    # def getDijkstraShortestPath(self, start, goal):
    #     """
    #     Parameters
    #     ----------
    #     start:int
    #         start node
    #     goal:int
    #         goal node

    #     Return
    #     ----------
    #     ShortestPath:list(int)
    #         shortest path
    #     """
    #     _, prev = self.Dijkstra_search(start)
    #     shortestPath = []
    #     node = goal
    #     while node is not None:
    #         shortestPath.append(node)
    #         node = prev[node]
    #     return shortestPath[::-1]


N, M = map(int, input().split())
graph = Dijkstra()
for i in range(M):
    a, b = map(int, input().split())
    # 0-indexじゃなくてもいい
    graph.add(a, b, 1, directed=False)
ans = []
_, prev = graph.Dijkstra_search(1)
for i in range(2, N + 1):
    if prev[i] is None:
        print("No")
        exit()
    else:
        ans.append(prev[i])
print("Yes")
print("\n".join(map(str, ans)))
