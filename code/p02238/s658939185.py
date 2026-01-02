class Vertex:
    _id = -1
    _children = []
    _visited = False
    _visited_time = 0
    _all_visited_time = 0

    def __init__(self, i, c):
        self._id = i
        self._children = c

    def getId(self):
        return self._id

    def getChildren(self):
        return self._children

    def isVisited(self):
        return self._visited

    def getVisitedTime(self):
        return self._visited_time

    def setVisitedTime(self, t):
        self._visited_time = t
        self._visited = True

    def getAllVisitedTime(self):
        return self._all_visited_time

    def setAllVisitedTime(self, t):
        self._all_visited_time = t

    def print(self):
        print("{} {} {}".format(self._id, self._visited_time, self._all_visited_time))


n = int(input())
graph = [0 for i in range(n)]
time = 0

# 頂点登録
for i in range(n):
    u = list(map(int, input().split(' ')))
    adj = []
    if u[1] > 0:
        adj = u[2:u[1]+2]
    graph[u[0]-1] = Vertex(u[0], adj)

# DFS
def dfs(v):
    global time
    time += 1
    v.setVisitedTime(time)
    for child in v.getChildren():
        if not graph[child-1].isVisited():
            dfs(graph[child-1])
    time += 1
    v.setAllVisitedTime(time)

# DFS実行
for v in graph:
    if not v.isVisited():
        dfs(v)

# 回答を出力
for v in graph:
    v.print()
