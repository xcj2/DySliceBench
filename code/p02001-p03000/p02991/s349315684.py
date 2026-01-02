from queue import Queue
import heapq
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(x): print(x, file=sys.stderr)
# template


class Graph():
    """
    Graph のテンプレート
    Parameters
    --------
        n (int): グラフのサイズ。
    Options
    --------
        Weighted = False: 重み付きかどうか
        Directed = False: 有向かどうか
        Matrix = False:　グラフの表現を隣接リストにするか隣接行列にするか。デフォルトは隣接リスト。
    Methods
    -------
        add_edge(start,end,(weight))
            start から end に重さ weight の辺を張る。重みなしグラフの場合は weight を省略する。
        dijkstra(start): O((E+V)logV)
            start から各頂点への最短距離を返す。負の辺があると無理。
        bellman_ford(start): O(EV)
            start から各頂点への最短距離を返す。負の辺があってもいけるが遅い。
    """

    def __init__(self, n, Weighted=False, Directed=False, Matrix=False):
        self.sz = n
        self.is_Weighted = Weighted
        self.is_Directed = Directed
        self.is_Matrix = Matrix
        if Matrix:
            if Weighted:
                self.graph = [[float('inf') for _i in range(n)]
                              for _j in range(n)]
            else:
                self.graph = [[0 for _i in range(n)] for _j in range(n)]
        else:
            self.graph = [[] for _i in range(n)]

    def _weighted_add_edge(self, x, y, w):
        if self.is_Matrix:
            self.graph[x][y] = w
        else:
            self.graph[x].append((y, w))

    def _unweighted_add_edge(self, x, y):
        if self.is_Matrix:
            self.graph[x][y] = 1
        else:
            self.graph[x].append(y)

    def add_edge(self, x, y, *w):
        if self.is_Directed:
            if self.is_Weighted:
                self._weighted_add_edge(x, y, w[0])
            else:
                self._unweighted_add_edge(x, y)
        else:
            if self.is_Weighted:
                self._weighted_add_edge(x, y, w[0])
                self._weighted_add_edge(y, x, w[0])
            else:
                self._unweighted_add_edge(x, y)
                self._unweighted_add_edge(y, x)

    def __getitem__(self, n):
        return self.graph[n]

    def __setitem__(self, n, v):
        if not self.is_Weighted and not self.is_Matrix:
            self.graph[n] = v

    def __str__(self):
        return str([self.graph[i] for i in range(self.sz)])

    def dijkstra(self, s):
        """
        単一始点最短距離を求める関数。dijkstra(s)でsからの任意の頂点への最短距離を求める。到達できなければfloat('inf')を返す。

        Warning
        ----------
            隣接リスト形式の重み付きグラフにしか対応していないので注意すること。重みなしグラフならば bfs を使うか，グラフ構築時にあらかじめ重み　1　にしておく。
        Parameters
        ----------
            s (int): 最短距離を求める start の頂点
        Returns
        ----------
            d (list): d[i] に start から i までの最短距離の入った list
        """
        if self.is_Matrix:
            print("隣接リスト形式で入力してください")
            raise TypeError
        d = [float('inf') for _ in range(self.sz)]
        b = [-1 for _ in range(self.sz)]  # 最短経路で各頂点の直前を表す list （経路復元）
        q = []
        d[s] = 0
        heapq.heappush(q, (d[s], s))
        while not len(q) == 0:
            p = heapq.heappop(q)
            v = p[-1]
            if d[v] < p[0]:
                continue
            if self.is_Weighted:
                for e in self.graph[v]:
                    u = e[0]
                    c = e[-1]
                    if d[u] > d[v] + c:
                        d[u] = d[v] + c
                        b[u] = v
                        heapq.heappush(q, (d[u], u))
            else:
                for e in self.graph[v]:
                    u = e
                    if d[u] > d[v] + 1:
                        d[u] = d[v] + 1
                        b[u] = v
                        heapq.heappush(q, (d[u], u))
        return d

    def bellman_ford(self, s):
        """
        単一始点最短距離を求める関数。bellman_ford(s)でsからの任意の頂点への最短距離を求める。到達できなければ　float('inf')　を返す。負のサイクルがある場合は False のみを返す。

        Warning
        ----------
            隣接リスト形式の重み付きグラフにしか対応していないので注意すること。重みなしグラフならばグラフ構築時にあらかじめ重み　1　にしておく。
        Parameters
        ----------
            s (int): 最短距離を求める start の頂点
        Returns
        ----------
            d (list): d[i] に start から i までの最短距離の入った list
            または
            False: 負のサイクルがある場合
        """
        d = [float('inf') for _ in range(self.sz)]
        d[s] = 0
        for i in range(self.sz - 1):
            for v in range(self.sz):
                for e in self.graph[v]:
                    u = e[0]
                    c = e[-1]
                    if d[v] == float('inf'):
                        continue
                    d[u] = min(d[u], d[v] + c)
        for v in range(self.sz):
            for e in self.graph[v]:
                u = e[0]
                c = e[-1]
                if d[v] == float('inf'):
                    continue
                if d[u] > d[v] + c:
                    return False
        return d

    def warshall_froyd(self):
        d = self.graph
        for i in range(self.sz):
            d[i][i] = 0
        for k in range(self.sz):
            for i in range(self.sz):
                for j in range(self.sz):
                    if d[i][k] != float('inf') and d[k][j] != float('inf'):
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d


def AOJ_ALDS_1_11_A():
    # 隣接リスト形式の重みなしグラフ
    n = ii()
    g = Graph(n)
    for i in range(n):
        u, k, *v = mi()
        g[u - 1] = list(map(lambda x: x - 1, v))
    # 隣接行列形式の重みなしグラフ
    mat_g = Graph(n, Matrix=True)
    for i in range(n):
        for j in g[i]:
            mat_g[i][j] = 1
    for i in range(n):
        print(*mat_g[i])
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A&lang=jp


def AOJ_ALDS_1_11_B():
    # 隣接リスト形式の重みなしグラフ
    n = ii()
    g = Graph(n)
    for i in range(n):
        u, k, *v = mi()
        g[u - 1] = list(map(lambda x: x - 1, v))
    d = [-1] * n
    f = [-1] * n
    time = 0

    def dfs(G, v):
        nonlocal time
        time += 1
        d[v] = time
        for nv in G[v]:
            if d[nv] != -1:
                continue
            dfs(G, nv)
        time += 1
        f[v] = time

    for v in range(n):
        if d[v] != -1:
            continue
        dfs(g, v)
    for i in range(n):
        print(i + 1, d[i], f[i])
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=jp


def AOJ_ALDS_1_11_C():
    """
    各頂点の0からの最短距離を bfs で求める
    """
    q = Queue()
    n = ii()
    dist = [-1 for _ in range(n)]
    g = Graph(n)
    for i in range(n):
        u, k, *v = mi()
        g[u - 1] = list(map(lambda x: x - 1, v))
    q.put(0)
    dist[0] = 0
    while not q.empty():
        v = q.get()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.put(nv)
    for i in range(n):
        print(i + 1, dist[i])
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=jp


def AOJ_GRL_1_A():
    n, m, start = mi()
    g = Graph(n, Weighted=True, Directed=True)
    for i in range(m):
        s, t, w = mi()
        g.add_edge(s, t, w)
    for i in g.dijkstra(start):
        if i == float('inf'):
            print('INF')
        else:
            print(i)
    # debug(g)
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=jp


def AOJ_ALDS_1_11_C_kai():
    """
    各頂点の0からの最短距離を dijkstra で求める
    """
    n = ii()
    g = Graph(n, Directed=True)
    for i in range(n):
        u, k, *v = mi()
        for j in v:
            g.add_edge(u - 1, j - 1)
    dist = g.dijkstra(0)
    for i in range(n):
        if dist[i] == float('inf'):
            print(i + 1, -1)
        else:
            print(i + 1, dist[i])
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=jp


def AOJ_GRL_1_B():
    n, m, start = mi()
    g = Graph(n, Weighted=True, Directed=True)
    for i in range(m):
        s, t, w = mi()
        g.add_edge(s, t, w)
    d = g.bellman_ford(start)
    if d == False:
        print("NEGATIVE CYCLE")
    else:
        d = list(map(lambda x: x if x != float('inf') else 'INF', d))
        for i in d:
            print(i)
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp


def AOJ_GRL_1_C():
    n, m = mi()
    g = Graph(n, Weighted=True, Directed=True, Matrix=True)
    for i in range(m):
        s, t, w = mi()
        g.add_edge(s, t, w)
    d = g.warshall_froyd()
    d = [list(map(lambda x: x if x != float('inf') else 'INF', d[i]))
         for i in range(n)]
    for i in range(n):
        if d[i][i] < 0:
            print('NEGATIVE CYCLE')
            sys.exit()
    for i in d:
        print(*i)
# verified on 2019/07/02
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=jp


def ABC132_E():
    N, M = mi()
    g = Graph(3 * N, Directed=True)
    for i in range(M):
        a, b = mi()
        g.add_edge(a - 1, b + N - 1)
        g.add_edge(a + N - 1, b + 2 * N - 1)
        g.add_edge(a + 2 * N - 1, b - 1)
    S, T = mi()
    ans = g.dijkstra(S - 1)[T - 1]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans // 3)


if __name__ == '__main__':
    # AOJ_ALDS_1_11_A()
    # AOJ_ALDS_1_11_B()
    # AOJ_ALDS_1_11_C()
    # AOJ_GRL_1_A()
    # AOJ_ALDS_1_11_C_kai()
    # AOJ_GRL_1_B()
    # AOJ_GRL_1_C()
    ABC132_E()
