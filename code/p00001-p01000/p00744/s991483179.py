#ARC092-C 2D Plane 2N Points
"""
重みなし2部マッチング問題
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

#ネットワークフロー
#最大流,最小カット
import queue
class Dinic():
    #Dinic法,O(|E||V|**2) ※但し、実際にはもっと高速な動作

    def __init__(self, v, inf = 10**10):
        # v:頂点数
        # G:辺情報.各頂点に対し、[行き先,重み,(この辺を含めず)既に存在する行き先の辺数]
        # level:startからの距離(これはcapacityを考慮しない) bfsで毎回リセットされる
        # iter:各頂点について、どこまで調べ終わったかを記録する
        self.V = v
        self.inf = inf
        self.G = [[] for _ in range(v)]
        self.level = [0 for _ in range(v)]
        self.iter = [0 for _ in range(v)]

    def add_edge(self, from_, to, cap):
        # to: 行き先, cap: 容量, rev: 反対側の辺

        # 無向グラフの場合、G[to]の方のcapを0→capにする必要があるので注意.('rev'はそのままで良い)

        self.G[from_].append({'to':to, 'cap':cap, 'rev':len(self.G[to])})
        self.G[to].append({'to':from_, 'cap':0, 'rev':len(self.G[from_])-1})

    # sからの最短距離をbfsで計算
    def bfs(self, s):
        self.level = [-1 for _ in range(self.V)]
        self.level[s] = 0
        que = queue.Queue()
        que.put(s)
        while not que.empty():
            v = que.get()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    que.put(e['to'])

    # 増加パスをdfsで探す
    def dfs(self, v, t, f):
        if v == t: return f
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]: #流れているかつ、levelが大きいなら
                d = self.dfs(e['to'], t, min(f, e['cap'])) # d:流量
                if d > 0:
                    e['cap'] -= d #使用済みの分だけcapから引く
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d

        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s) #levelの更新
            # bfsでtに到達不可なら終了
            if self.level[t] < 0 : return flow
            #イテレータの初期化(イテレータ：各頂点に対し、どこまで調べ終わったか)
            self.iter = [0 for _ in range(self.V)]
            f = self.dfs(s, t, self.inf) #f:そのパスの流量
            while f > 0:
                flow += f
                f = self.dfs(s,t, self.inf)

"""素因数分解"""
def factrize(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            #もし素因数を重複させたくないならここを加えてfct.append(b)を消す
            if not b in fct:
                fct.append(b)
        b = b+1
    if n > 1:
        fct.append(n)
    return fct #リストが帰る
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a//gcd(a,b)*b)
while True:
    m,n = map(int,readline().split())
    if m == 0 and n == 0:
        break

    network = Dinic(m+n+2)
    source = 0
    sink = m+n+1
    blue = []
    red = []
    while len(blue) < m:
        blue += list(map(int,readline().split()))
    while len(red) < n:
        red += list(map(int,readline().split()))
    
    for i in range(m):
        for j in range(n):
            if gcd(blue[i],red[j]) > 1:
                network.add_edge(i+1,m+j+1,1)
    for i in range(m):
        network.add_edge(source,i+1,1)
    for i in range(n):
        network.add_edge(m+i+1,sink,1)
    print(network.max_flow(source,sink))
        

    

    
    





