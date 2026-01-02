import sys
readline = sys.stdin.readline
class Tree:
    __slots__ = ['id', 'p', 'sibling', 'degree', 'depth', 'height', 'type', 'c']
    def __init__(self, id):
        self.id = id
        self.p = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = "leaf"
        self.c = []
    def __str__(self):
        return f"node {self.id}: parent = {self.p}, sibling = {self.sibling}, degree = {self.degree}, depth = {self.depth}, height = {self.height}, {self.type}"
n = int(input())
tree = tuple(Tree(i) for i in range(n))
for _ in range(n):
    id, *c = map(int, readline().replace("-1", "").split())
    if c != []:
        tree[id].type = "internal node"
        tree[id].c = c
        for j in c:
            tree[j].p = id
        len_c = len(c)
        tree[id].degree = len_c
        if len_c == 2:
            tree[c[0]].sibling = c[1]
            tree[c[1]].sibling = c[0]
root = 0
while tree[root].p != -1:
    root = tree[root].p
tree[root].type = "root"
def depth_height_check(id, d):
    d += 1
    height = 0
    for i in tree[id].c:
        tree[i].depth = d
        if tree[i].type != "leaf":
            tree[i].height = depth_height_check(i, d) + 1
            height = max(height, tree[i].height)
    return height
tree[root].height = depth_height_check(root, 0) + 1 if n > 1 else 0
print("\n".join(map(str, tree)))

