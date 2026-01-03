#ARC074-F Lotus Leaves
"""
この問題は最小カットに帰着できる。但し、h*wの頂点を持つと間に合わないので、H軸とW軸を独立に考える。
縦H個、横W個の頂点を持つ。
ある座標h,wがoの時、頂点H[h]とW[w]と容量1のネットワークでつなぐ。[sourse,h0,h1,...hH,w0,w1,...wW,sink]
startとgoalを最大流の始点、終点として持つのではなく、それとは別にsourse,sinkの2頂点を作る。
startとsourse,goalとsinkを容量INFでつなぐことにより、より簡単に最小カットを求めることが可能になる。
よって、グラフ長はH*W+2となる。
ネットワーク自体は無向なので、undirectedを使用する。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

#maspyさんの方(sourceとsinkを追加する方法)
"""
class Dinicの使い方:
initは、Dinic(頂点数,始点,終点)で行う。
最大流の典型として、実際に問題に与えられる始点、終点とは別に、その始点sと終点tを、
新たに作成したsource(S)とsink(T)にcap=INFでつなげることで、実質始点と終点をそのままで使用することができる。
このテクニックにより簡単になる問題が多いので、いっそそれを前提にしちゃえというのがこのテンプレ。
与えられるグラフの頂点数をNとして、N+2(sourceとsinkの+2)で初期化し、source=0,sink=N+1とすると良い。
辺を張る際に、
有向グラフの場合は、add_edge(from,to,capacity)
無向グラフの場合は、add_edge_undirected(from,to,capacity)　とする。
最後にmax_flowで最大流を求めるが、INFが10**18と非常に大きいのは、sourceからsinkへのパスが存在しなかった場合、
INF以上の値が帰ってくる為である。
「もしそのような最大流が存在しないなら-1を出力」というような条件で、
f = max_flow()
if f == INF:
    print(-1)
とやると、fがINFより大きい場合があるので、
if f >= INF:
    print(-1)
else:
    print(f)
とする必要がある。 
"""
from collections import deque
class Dinic():
    def __init__(self, N, source, sink):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.source = source
        self.sink = sink
 
    def add_edge(self, fr, to, cap):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, n2])
        self.G[to].append([fr, 0, n1]) # 逆辺を cap 0 で追加
        
    def add_edge_undirected(self, fr, to, cap):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, n2])
        self.G[to].append([fr, cap, n1]) # 逆辺を cap capで追加
        
    def bfs(self):
        level = [0] * self.N
        G = self.G; source = self.source; sink = self.sink
        q = deque([source])
        level[source] = 1
        pop = q.popleft; append = q.append
        while q:
            v = pop()
            lv = level[v] + 1
            for to, cap, rev in G[v]:
                if not cap:
                    continue
                if level[to]:
                    continue
                level[to] = lv
                if to == sink:
                    self.level = level
                    return
                append(to)
        self.level = level
        
    def dfs(self,v,f):
        if v == self.sink:
            return f
        G = self.G
        prog = self.progress
        level = self.level
        lv = level[v]
        E = G[v]
        for i in range(prog[v],len(E)):
            to, cap, rev = E[i]
            prog[v] = i
            if not cap:
                continue
            if level[to] <= lv:
                continue
            x = f if f < cap else cap
            ff = self.dfs(to, x)
            if ff:
                E[i][1] -= ff
                G[to][rev][1] += ff
                return ff
        return 0
    
    def max_flow(self):
        INF = 10**18
        flow = 0
        while True:
            self.bfs()
            if not self.level[self.sink]:
                return flow
            self.progress = [0] * self.N
            while True:
                f = self.dfs(self.source, INF)
                if not f:
                    break
                flow += f
        return flow

H,W = map(int,readline().split())
maze = []
for _ in range(H):
    maze += [list(readline().rstrip().decode())]

source = 0
sink = H+W+1
network = Dinic(H+W+2,source,sink)
INF = 10**18

for i in range(1,H+1):
    for j,ox in enumerate(maze[i-1],1):
        if ox == "x":
            continue
        elif ox == "o":
            network.add_edge_undirected(i,H+j,1)
        elif ox == "S":
            network.add_edge_undirected(source,i,INF)
            network.add_edge_undirected(source,H+j,INF)
        elif ox == "T":
            network.add_edge_undirected(i,sink,INF)
            network.add_edge_undirected(H+j,sink,INF)

f = network.max_flow()
if f >= INF:
    print(-1)
else:
    print(f)

