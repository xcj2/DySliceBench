from collections import deque
import sys


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())


class Graph:
    def __init__(self, n, is_directed=False):
        """
        :param n: 頂点数
        :param is_directed: 有向グラフ(True)か無向グラフか(False)
        """
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.is_directed = is_directed

    def add_edge(self, u, v):
        """uからvへの(有向な)辺をつなぐ"""
        self.graph[u].append(v)
        if not self.is_directed:
            self.graph[v].append(u)

    def search(self, start, mode):
        '''開始地点から各頂点まで幅/深さ優先探索を行って得られた距離のリストを返す
        Args:
          start(int): 開始地点となる頂点
          mode(str): 幅優先探索(b)か深さ優先探索(d)を指定

        Returns:
          List[int]: 開始地点からの距離(未到達の場合は-1)
        '''
        dists = [-1] * self.n
        que = deque([start])
        dists[start] = 0
        if mode == 'b':
            get_v = que.popleft
        else:
            get_v = que.pop
        while que:
            now_v = get_v()
            for next_v in self.graph[now_v]:
                if dists[next_v] != -1:
                    continue
                que.append(next_v)
                dists[next_v] = dists[now_v] + 1
        return dists


n = I()
g = Graph(n, is_directed=True)
for _ in range(n):
    u, k, *v = LI()
    u -= 1
    if v == []:
        continue
    for vi in v:
        vi -= 1
        g.add_edge(u, vi)
res = g.search(0, 'b')
for i in range(n):
    print(i + 1, res[i])

