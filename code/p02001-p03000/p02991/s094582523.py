import sys
N, M = map(int, input().split())

class Bridge:
    def __init__(self, nodeA, nodeB):
        self.edges = [BridgeEdge(nodeA, self), BridgeEdge(nodeB, self)]
        nodeA.addEdge(self.edges[1])
        #nodeB.addEdge(self.edges[0])

class BridgeEdge:
    def __init__(self, node, edge):
        self.edge = edge
        self.node = node
        self.flag = 0

class Node:
    def __init__(self, id):
        self.id = id
        self.bridges = []
    def addEdge(self, bridgeEdge):
        self.bridges.append(bridgeEdge)
    def __repr__(self):
        return "({})".format(self.id)

nodes = [Node(i) for i in range(N+1)]

for ui, vi in (map(int, input().split()) for _ in range(M)):
    Bridge(nodes[ui], nodes[vi])

S, T = map(int, input().split())

#nodes[S].flag = 1
s = [(None, nodes[S], 0)]
idx = 0
isOK = False
while idx < len(s):
    pre, cur, level = s[idx]
    idx += 1
    nxtlevel = level + 1
    nxtflag = 1 << (nxtlevel % 3)

    for nxt in cur.bridges:
        if (nxt.flag & nxtflag) == 0:
            nxt.flag |= nxtflag 
            if nxt.node is nodes[T] and nxtflag == 1:
                isOK = True
                break
            s.append((cur, nxt.node, nxtlevel))
    else:
        continue
    break
if isOK:
    print(nxtlevel//3)
else:
    print(-1)

