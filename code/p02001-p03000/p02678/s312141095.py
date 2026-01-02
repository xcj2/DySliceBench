from sys import stdin
from collections import deque


class BreadthFirstSearch:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.adj_list = [[] for _ in range(self.n)]

    # Edge数分回すことを想定
    def add_edge(self, start, end, undirected=True):
        self.adj_list[start].append(end)
        if undirected:
            self.adj_list[end].append(start)

    # depth = distance
    def search(self, start_node):
        order = [-1] * self.n  # a bfs ordering of each vertex
        parent = [-1] * self.n  # parent of each vertex in the bfs search tree
        depth = [-1] * self.n  # the depth of each vertex
        q = deque([(start_node, -1, 0)])  # (vertex, parent, depth)
        num = 0  # current ordering
        while len(q) > 0:
            v, p, d = q.popleft()
            if order[v] < 0:  # visited v for the first time
                order[v] = num
                parent[v] = p
                depth[v] = d
                num += 1
                for u in self.adj_list[v]:
                    if order[u] >= 0:
                        continue
                    q.append((u, v, d+1))
        return order, parent, depth


def get_result(data):
    N, M = data[0]
    A = data[1:]
    solver = BreadthFirstSearch(N)
    for val in A:
        solver.add_edge(val[0]-1, val[1]-1)
    order, parent, depth = solver.search(0)
    print('Yes')
    for p in parent[1:]:
        print(p+1)
    return None


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    # print(result)
