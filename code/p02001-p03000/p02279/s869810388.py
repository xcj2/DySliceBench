class Node:
    def __init__(self, node):
        self.node = node
        self.parent = -1
        self.depth = 0
        self.type = ""
        self.children = []

    def __str__(self):
        if self.parent == -1:
            self.type = "root"
        elif len(self.children) == 0:
            self.type = "leaf"
        else:
            self.type = "internal node"
        return "node {}: parent = {}, depth = {}, {}, {}".format(
            self.node, self.parent, self.depth, self.type, self.children)


def dfs(tree, v, p, d):
    from collections import deque
    que = deque()
    tree[v].parent = p
    tree[v].depth = d
    que.extend(tree[v].children)
    while len(que) > 0:
        c = que.pop()
        if tree[c].parent == -1:
            dfs(tree, c, v, d + 1)


def resolve():
    n = int(input())
    tree = [Node(i) for i in range(n)]
    V = [list(map(int, input().split())) for _ in range(n)]
    hasChild = set()
    childrens = set()
    for a, k, *c in V:
        if len(c) > 0:
            tree[a].children = c
            hasChild.add(a)
            childrens.update(c)
    root = hasChild - childrens
    if len(root) > 0:
        dfs(tree, root.pop(), -1, 0)
    print(*tree, sep="\n")


resolve()

