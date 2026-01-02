import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
mlmis = lambda: [-int(x) for x in input().split()]
INF = float('inf')
def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok
#


def main():
    N = ii()
    class Edge:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.color = None
        def get_con(self, i):
            return self.b if self.a==i else self.a
    edges = []
    tree = tuple([] for _ in range(N))
    for _ in range(N-1):
        a, b = mis()
        a -= 1
        b -= 1
        edge = Edge(a, b)
        edges.append(edge)
        tree[a].append(edge)
        tree[b].append(edge)
    tasks = [(0, 0)]
    max_color = 1
    for used, node in tasks:
        color = 1
        for edge in tree[node]:
            if color == used:
                color += 1
            if edge.color is not None:
                continue
            edge.color = color
            tasks.append((color, edge.get_con(node)))
            max_color = max(max_color, color)
            color += 1
    print(max_color)
    for edge in edges:
        print(edge.color)



main()
