from collections import deque
from collections import defaultdict


class Graph(object):
    """
    隣接リストによる無向グラフ
    重み無しで距離は１
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst):
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def get_nodes(self):
        return self.graph.keys()


if __name__ == "__main__":
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    g = Graph()
    for i in range(n-1):
        g.add_edge(i, i+1)
    g.add_edge(x, y)

    ans = [0] * (n-1)

    # BFSによる解法
    for i in range(n-1):
        # 始点からの距離
        # -1を未訪問とする
        dist = [-1] * n

        # 初期条件
        # 今回は頂点iから探索を行う
        dist[i] = 0
        que = deque([i])

        while len(que) != 0:
            vertex = que.popleft()
            for v in g.graph[vertex]:
                if dist[v] != -1:
                    pass
                else:
                    tmp = dist[vertex] + 1
                    dist[v] = tmp
                    if v > i:
                        ans[tmp-1] += 1
                    que.extend(g.graph[vertex])

    for a in ans:
        print(a)
