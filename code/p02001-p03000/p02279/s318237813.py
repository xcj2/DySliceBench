class Vertex:
    _id = -1
    _children = []
    _parent = -1
    _depth = 0
    _type = "root"

    def __init__(self, i, c):
        self._id = i
        self._children = c

    def getId(self):
        return self._id

    def getChildren(self):
        return self._children

    def getParent(self):
        return self._parent

    def getDepth(self):
        return self._depth

    def getType(self):
        return self._type

    def setParent(self, p):
        self._parent = p

    def setDepth(self, d):
        self._depth = d

    def setType(self, t):
        self._type = t

    def print(self):
        print("node {}: parent = {}, depth = {}, {}, {}".format(self._id, self._parent, self._depth, self._type, self._children))


n = int(input())
tree = [0 for i in range(n)]

# 節点
for i in range(n):
    u = list(map(int, input().split(' ')))
    tree[u[0]] = Vertex(u[0], u[2:u[1]+2])

# 親を設定
for w in tree:
    for c in w.getChildren():
        tree[c].setParent(w.getId())
        tree[c].setType("internal node")

# 葉と親を判定
for w in tree:
    if w.getChildren() == []:
        w.setType("leaf")
    if w.getParent() == -1:
        w.setType("root")

# DFS
def dfs(v, depth):
    v.setDepth(depth)
    for child in v.getChildren():
        dfs(tree[child], depth+1)

# 根を探す
root = tree[0]
for w in tree:
    if w.getType() == "root":
        root = w

dfs(root, 0)

# 回答を出力
for w in tree:
    w.print()
