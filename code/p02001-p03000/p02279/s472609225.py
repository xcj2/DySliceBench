# coding: utf-8
# Your code here!

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parent = -1
        self.depth = 0
        self.ntype = None
    
    def __str__(self):
        return 'node {}: parent = {}, depth = {}, {}, {}'\
            .format(self.id, self.parent, self.depth, self.ntype, self.children)

N = int(input())
nodes = [Node(i) for i in range(N)]

for _ in range(N):
    elm = [int(i) for i in input().split()]
    if elm[1] > 0:
        nodes[elm[0]].children = elm[2:]
        nodes[elm[0]].ntype = 'internal node'
        for n in elm[2:]:
            nodes[n].parent = elm[0]
    else:
        nodes[elm[0]].ntype = 'leaf'

root = 0
for node in nodes:
    if node.parent == -1:
        node.ntype = 'root'
        root = node.id
        break
        
def dfs(id, depth):
    node = nodes[id]
    node.depth = depth
    if node.children:
        for child in node.children:
            dfs(child, depth+1)
    else:
        return

dfs(root, 0)

for node in nodes:
    print(node)
    
