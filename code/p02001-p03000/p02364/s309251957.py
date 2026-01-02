# coding: utf-8
# Your code here!

INF = 2000000000



class Node:
    def __init__(self, num):
        self.num = num
        self.parent = self
        self.rank = 0
    
def findSet(node):
    tmp = []
    while node.parent != node:
        tmp.append(node)
        node = node.parent
    
    while tmp:
        tmp.pop().parent = node
    return node

def unite(x, y):
    node1 = findSet(nodes[x])
    node2 = findSet(nodes[y])
    if node1.rank == node2.rank:
        node2.parent = node1
        node1.rank += 1
    elif node1.rank > node2.rank:
        node2.parent = node1
    else:
        node1.parent = node2

def same(x, y):
    node1 = findSet(nodes[x])
    node2 = findSet(nodes[y])
    return node1.parent == node2.parent





class Edge:
    def __init__(self, source, target, cost):
        self.source = source
        self.target = target
        self.cost = cost
    
def kruskal():
    edges.sort(key = lambda u:u.cost)
    
    for i in range(e):
        if findSet(edges[i].source) != findSet(edges[i].target):
            unite(edges[i].source.num, edges[i].target.num)
            K.append(edges[i])
    
    total = 0
    for tmp in K:
        total += tmp.cost
    print(total)


nums=list(map(int,input().split()))
n = nums[0]
e = nums[1]

edges = []
nodes = []
for i in range(n):
    nodes.append(Node(i))

for i in range(e):
    nums=list(map(int,input().split()))
    tmp = Edge(nodes[nums[0]], nodes[nums[1]], nums[2])
    edges.append(tmp)




K = []

kruskal()




