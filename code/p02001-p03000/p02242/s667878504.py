inf = float("inf")


class Node():

    def __init__(self, _id):
        self.id = _id
        self.d = inf
        self.pi = None
        self.color = 0
        self.adj = {}

    def input_data(self, data):
        k = data[0]
        for i in range(k):
            self.adj[G[data[2 * i + 1]]] = data[2 * i + 2]

    def __hash__(self):
        return hash(self.id)

def dijkstra():
    while True:
        mincost = inf
        for i in G:
            if i.color != 1 and i.d < mincost:
                mincost = i.d
                u = i
        if mincost == inf:
            break
        u.color = 1
        for v in u.adj.keys():
            if v.color != 1 and u.d + u.adj[v] < v.d:
                v.pi = u
                v.d = u.d + u.adj[v]

if __name__ == "__main__":
    n = int(input())
    G = [Node(i) for i in range(n)]
    for _ in range(n):
        data = [int(i) for i in input().split()]
        G[data[0]].input_data(data[1:])
        if data[0] == 0:
            G[data[0]].d = 0
    dijkstra()
    [print(i.id, i.d) for i in G]
