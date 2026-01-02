"""
最大フローとして解き直してみる
"""

from collections import deque
from collections import defaultdict
class Dinic:
    def __init__(self):
        # self.N = N
        self.G = defaultdict(list)
    
    def add_edge(self, fr, to, cap):
        """
        :param fr: 始点
        :param to: 終点
        :param cap: 容量
        """
        # forwardの最後には、キャパのうちどれだけ使ったかが入る
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[-1] = backward
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        """
        :param v1: 始点
        :param v2: 終点
        :param cap1: 容量1
        :param cap2: 容量2
        """
        edge1 = [v2, cap1, None]
        edge2 = [v1, cap2, edge1]
        edge1[-1] = edge2
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        """
        :param s: bfsの始点(source)
        :param t: bfsの終点(sink)
        :return: tに到達したかどうか。(sourceからの距離を保存しながら)
        """
        self.level = level = [-1]*len(self.G)
        q = deque([s])
        level[s] = 0
        G = self.G
        while len(q) > 0:
            v = q.popleft()
            lv = level[v] + 1
            nexts = G[v]
            for w, cap, _ in nexts:
                if cap > 0 and level[w] == -1:
                    level[w] = lv
                    q.append(w)
        is_reach = (level[t] > 0)
        return is_reach

    def dfs(self, v, t, f):
        """
        :param v: 点v
        :param t: 終点(sink)
        :param f: v時点でのフロー
        :return: 終点到達時のフローを返す
        """   
        if v == t:
            return f
        level = self.level
        nexts = self.G[v]
        for edge in nexts:
            w, cap, rev = edge
            # まだキャパがあるならば
            if cap > 0 and level[v] < level[w]:
                # キャパが余ってるなら全部流すし
                # カツカツならキャパのmaxまで流す
                d = self.dfs(w, t, min(f, cap))
                # 帰りがけに、更新
                if d > 0:
                    # 順方向のキャパをd下げる
                    # 逆方向のキャパをd増やす
                    edge[1] -= d
                    rev[1] += d
                    return d
        # 次の道が見つからなければ終了
        return 0
    
    def flow(self, s, t):
        """
        :param s: 始点
        :param t: 終点
        :return : 最大フロー
        """
        flow = 0
        INF = 10**10
        G = self.G
        # ルートが存在する限り、続ける
        while self.bfs(s, t):
            f = INF
            while f > 0:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

# 入力受け取り
N = int(input())
dinic = Dinic()
reds = []
for i in range(N):
    a,b = map(int, input().split())
    reds.append((a,b))
blues = []
for i in range(N):
    a,b = map(int, input().split())
    blues.append((a,b))

# マッチングできるペアをグラフに。(red=blueの二部グラフになる。)
cnt = 0
edges = defaultdict(list)
source = 2*N
sink = 2*N+1
# source -> 各青の頂点へ
for i in range(len(blues)):
    dinic.add_edge(source,i,1)
# 各赤の頂点 -> sink
for j in range(len(reds)):
    dinic.add_edge(j+N, sink, 1)
    
for i,(c,d) in enumerate(blues):
    for j,(a,b) in enumerate(reds):
        if c > a and d > b:
            dinic.add_edge(i, N+j, 1)

ans = dinic.flow(source, sink)
print(ans)

