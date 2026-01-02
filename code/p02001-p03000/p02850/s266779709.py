import sys
sys.setrecursionlimit(1000000000)

N = int(input())


class Node:
    def __init__(self, index):
        self.index = index
        self.edges = []

class Edge:
    def __init__(self, index, a, b):
        self.a = a
        self.b = b
        self.index = index
        self.color = 0

    def to(self, fm):
        if fm == self.a:
            return self.b
        elif fm == self.b:
            return self.a
        else:
            return None


nodes = [Node(i) for i in range(N)]
edges = []
for i in range(N-1):
    a, b = map(int, input().split())
    edge = Edge(i, a-1, b-1)
    edges.append(edge)
    nodes[a-1].edges.append(i)
    nodes[b-1].edges.append(i)

passed = set()


def rec(node, via_color, K):
    passed.add(node.index)
    color = 1
    for edge_index in node.edges:
        edge = edges[edge_index]
        to_node_index = edge.to(node.index)
        if to_node_index in passed:
            continue
        if color == via_color:
            color += 1
        edge.color = color
        K = rec(nodes[to_node_index], color, K)
        color += 1
    return max(color-1, K)


K = rec(nodes[0], 0, 1)
print(K)
for edge in edges:
    print(edge.color)