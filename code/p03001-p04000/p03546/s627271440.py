import heapq


class dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.visited = [-1 for i in range(len(adj))]
        self.heap = []

    def allSearch(self, _start):
        # スタート地点を設定
        heapq.heappush(self.heap, [0, _start])
        # ダイクストラ法でスタート地点からの距離を算出
        while 1:
            if len(self.heap) == 0:
                break
            start = heapq.heappop(self.heap)
            # 同じノードへ複数候補がある場合がある、一度訪れたノードへの候補は削除する
            if self.visited[start[1]] != -1:
                continue
            # 確定した距離をvisitテーブルに保持
            self.visited[start[1]] = start[0]
            for i in range(len(self.adj)):
                if self.visited[i] == -1 and self.adj[start[1]][i] != 0:
                    heapq.heappush(self.heap, [self.adj[start[1]][i] + self.visited[start[1]], i])
        # print("start:{} score:{}".format(_start, max(self.visited)))
        return self.visited


def func(h, w, c, a):
    cost = [0 for _ in range(10)]
    for i in range(len(c)):
        dij = dijkstra(adj=c)
        cost[i] = dij.allSearch(i)[1]
    # print(cost)
    totalCost = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] >= 0:
                totalCost += cost[a[i][j]]
    return totalCost
h, w = [int(i) for i in input().split()]
c = [[0 for _ in range(10)] for _ in range(10)]
a = [[0 for _ in range(w)] for _ in range(h)]
for i in range(10):
    c[i] = [int(i) for i in input().split()]
for i in range(h):
    a[i] = [int(i) for i in input().split()]
print(func(h, w, c, a))
"""
print(func(2, 4, [[0, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 0, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 0, 9, 9, 9, 9, 9, 9, 9],
                  [9, 9, 9, 0, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 0, 9, 9, 9, 9, 2], [9, 9, 9, 9, 9, 0, 9, 9, 9, 9],
                  [9, 9, 9, 9, 9, 9, 0, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 0, 9, 9], [9, 9, 9, 9, 2, 9, 9, 9, 0, 9],
                  [9, 2, 9, 9, 9, 9, 9, 9, 9, 0]], [[-1, -1, -1, -1], [8, 1, 1, 8]]))
print(func(5, 5, [[0, 999, 999, 999, 999, 999, 999, 999, 999, 999], [999, 0, 999, 999, 999, 999, 999, 999, 999, 999],
                  [999, 999, 0, 999, 999, 999, 999, 999, 999, 999], [999, 999, 999, 0, 999, 999, 999, 999, 999, 999],
                  [999, 999, 999, 999, 0, 999, 999, 999, 999, 999], [999, 999, 999, 999, 999, 0, 999, 999, 999, 999],
                  [999, 999, 999, 999, 999, 999, 0, 999, 999, 999], [999, 999, 999, 999, 999, 999, 999, 0, 999, 999],
                  [999, 999, 999, 999, 999, 999, 999, 999, 0, 999], [999, 999, 999, 999, 999, 999, 999, 999, 999, 0]],
           [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
print(func(3, 5, [[0, 4, 3, 6, 2, 7, 2, 5, 3, 3], [4, 0, 5, 3, 7, 5, 3, 7, 2, 7], [5, 7, 0, 7, 2, 9, 3, 2, 9, 1],
                  [3, 6, 2, 0, 2, 4, 6, 4, 2, 3], [3, 5, 7, 4, 0, 6, 9, 7, 6, 7], [9, 8, 5, 2, 2, 0, 4, 7, 6, 5],
                  [5, 4, 6, 3, 2, 3, 0, 5, 4, 3], [3, 6, 2, 3, 4, 2, 4, 0, 8, 9], [4, 6, 5, 4, 3, 5, 3, 2, 0, 8],
                  [2, 1, 3, 4, 5, 7, 8, 6, 4, 0]], [[3, 5, 2, 6, 1], [2, 5, 3, 2, 1], [6, 9, 2, 5, 6]]))
"""
# print("print(func({}, {}, {}, {}))".format(h, w, c, a))
