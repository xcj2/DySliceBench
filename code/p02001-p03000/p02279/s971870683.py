import sys
readline = sys.stdin.readline
class Tree:
    __slots__ = ['id', 'p', 'depth', 'type', 'c']
    def __init__(self, id):
        self.id = id
        self.p = -1
        self.depth = -1
        self.type = "leaf"
        self.c = []
    def __str__(self):
        return f"node {self.id}: parent = {self.p}, depth = {self.depth}, {self.type}, {self.c}"
n = int(input())
li = tuple(Tree(i) for i in range(n))
for _ in range(n):
    id, k, *c = map(int, readline().split())
    if k != 0:
        li[id].type = "internal node"
        li[id].c = c
        for j in c:
            li[j].p = id
root = 0
while li[root].p != -1:
    root = li[root].p
li[root].type = "root"
li[root].depth = 0
def depth_check(id, d):
    d += 1
    for i in li[id].c:
        li[i].depth = d
        if li[i].type != "leaf":
            depth_check(i, d)
depth_check(root, 0)
print(*li, sep="\n")

