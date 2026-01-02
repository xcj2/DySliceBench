def examA():
    N = DI()/dec(7)
    ans = N
    print(N)
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
    class LCA(object):
        def __init__(self, G, root=0):
            self.G = G
            self.root = root
            self.n = len(G)
            self.logn = (self.n - 1).bit_length()
            self.depth = [-1 if i != root else 0 for i in range(self.n)]
            self.parent = [[-1] * self.n for _ in range(self.logn)]
            self.W = [-1 if i != root else 0 for i in range(self.n)]
            self.dfs()
            self.doubling()
            # print(self.depth)
            # print(self.parent)
            # print(self.W)

        def dfs(self):
            que = [self.root]
            while que:
                u = que.pop()
                for v, (d, c) in self.G[u].items():
                    if self.depth[v] == -1:
                        self.depth[v] = self.depth[u] + 1
                        self.parent[0][v] = u
                        self.W[v] = self.W[u] + d
                        que += [v]

        def doubling(self):
            for i in range(1, self.logn):
                for v in range(self.n):
                    if self.parent[i - 1][v] != -1:
                        self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

        def get(self, u, v):
            if self.depth[v] < self.depth[u]:
                u, v = v, u
            du = self.depth[u]
            dv = self.depth[v]
            for i in range(self.logn):  # depthの差分だけuを遡らせる
                if (dv - du) >> i & 1:
                    v = self.parent[i][v]
            if u == v: return u  # 高さ揃えた時点で一致してたら終わり
            for i in range(self.logn - 1, -1, -1):  # そうでなければ上から二分探索
                pu, pv = self.parent[i][u], self.parent[i][v]
                if pu != pv:
                    u, v = pu, pv
            return self.parent[0][u]

    # (参考) https://qiita.com/ophhdn/items/48710bfab29d1fdc4577
    def euler_tour(G, root=0):
        n = len(G)
        euler = []
        dq = deque([root])
        dq2 = deque()
        visited = [0] * n
        while dq:
            u = dq.pop()
            euler += [u]
            if visited[u]:
                continue
            for v in G[u].keys():
                if visited[v]:
                    dq += [v]
                # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
                else:
                    dq2 += [v]
            dq.extend(dq2)
            dq2 = deque()
            visited[u] = 1
        return euler

    N, q = LI()
    V = [{} for _ in range(N)]
    for _ in range(N - 1):
        a, b, c, d = LI()
        V[a - 1][b - 1] = (d, c)
        V[b - 1][a - 1] = (d, c)
    lca = LCA(V)
    # クエリ先読み(しないと必要な色の情報O(n**2)とかいる)
    # クエリに関係あるのはu,vとlca頂点の3つ
    # 頂点uは色xを変えるクエリを持つ
    colors = [set() for _ in range(N)]
    Q = [LI()for _ in range(q)]
    for x, y, u, v in Q:
        u -= 1; v -= 1
        a = lca.get(u,v)
        colors[u].add(x)
        colors[v].add(x)
        colors[a].add(x)
    # オイラーツアー
    # 上記クエリで必要な値だけを、オイラーツアーで訪れたタイミングで取得する。
    ET = euler_tour(V)
    #print(ET)

    # クエリごとの根からの色の数、長さの合計を記録
    Q_color = [{}for _ in range(N)]
    Q_length = [{}for _ in range(N)]
    for color in colors[0]:
        Q_color[0][color] = 0
        Q_length[0][color] = 0

    # 色iが何個あるか
    S_color = defaultdict(int)
    # 色iの距離の合計
    S_length = defaultdict(int)

    visited = [False]*N
    visited[0] = True
    for i in range(len(ET)-1):
        now,ne = ET[i],ET[i+1]
        d,c = V[now][ne]
        # 帰りはマイナス
        if visited[ne]:
            S_color[c] -= 1
            S_length[c] -= d
            continue
        else:
            S_color[c] += 1
            S_length[c] += d

        for color in colors[ne]:
            Q_color[ne][color] = S_color[color]
            Q_length[ne][color] = S_length[color]

        visited[ne] = True

    ans = [0]*q
    for i,(x,y,u,v) in enumerate(Q):
        u -= 1; v -= 1
        a = lca.get(u, v)
        child_1 = lca.W[u] + (Q_color[u][x]*y - Q_length[u][x])
        child_2 = lca.W[v] + (Q_color[v][x]*y - Q_length[v][x])
        parent = lca.W[a] + (Q_color[a][x]*y - Q_length[a][x])
        #print(child_1,child_2,parent)

        ans[i] = child_1 + child_2 - parent * 2

    for v in ans:
        print(v)
    return


from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""