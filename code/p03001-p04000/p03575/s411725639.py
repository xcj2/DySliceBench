N, M = map(int, input().split())

class Bridge:
    def __init__(self, nodeA, nodeB):
        self.edges = [BridgeEdge(nodeA), BridgeEdge(nodeB)]

class BridgeEdge:
    def __init__(self, node):
        self.node = node
        self.judge = 0

class Node:
    def __init__(self, id):
        self.id = id
        self.bridges = []
    def addEdge(self, bridgeEdge):
        self.bridges.append(bridgeEdge)


nodes = [Node(i) for i in range(N+1)]
bridges = []
for A, B in (map(int, input().split()) for _ in range(M)):
    b = Bridge(nodes[A], nodes[B])
    nodes[A].addEdge(b.edges[1])
    nodes[B].addEdge(b.edges[0])
    bridges.append(b)


s = [(None, nodes[1])]
idx = 0
while idx < len(s):
    pre, cur = s[idx]
    idx += 1

    for nxt in cur.bridges:
        if not pre is nxt.node and nxt.judge < 2:
            nxt.judge += 1
            s.append((cur, nxt.node))

cnt = 0
for bd in bridges:
    if sum(1 for b in bd.edges if b.judge <= 1) > 0:
        cnt += 1

print(cnt)
