# coding: utf-8
# Your code here!

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = -1
        self.sibling = -1
        self.children = []
        self.depth = 0
        self.height = 0
        self.ntype = None
    
    def __str__(self):
        return 'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.\
            format(self.id, self.parent, self.sibling, len(self.children), self.depth, self.height, self.ntype)
        
N = int(input())

nodes = [Node(i) for i in range(N)]

# 親子関係解決
for i in range(N):
    id, l, r = [int(i) for i in input().split()]
    deg = 0
    if l >= 0 and r >= 0:
        nodes[id].children += [l, r]
        nodes[l].parent = id
        nodes[l].sibling = r
        nodes[r].parent = id
        nodes[r].sibling = l
        nodes[id].ntype = 'internal node'
    elif l >= 0:
        nodes[l].parent = id
        nodes[id].children.append(l)
        nodes[id].ntype = 'internal node'
    elif r >= 0:
        nodes[r].parent = id
        nodes[id].children.append(r)
        nodes[id].ntype = 'internal node'
    else:  
        nodes[id].ntype = 'leaf'

# rootノード検索
root = -1
for i in range(N):
    if nodes[i].parent == -1:
        root = i
        nodes[i].ntype = 'root'
        break

def nfs(node, dep):
    node.depth = dep
    
    if not node.children:
        node.height = 0
        return 0
    
    for child in node.children:
        h = nfs(nodes[child], dep+1)
        node.height = max(node.height, h+1)
    
    return node.height

nfs(nodes[root], 0)

for node in nodes:
    print(node)


