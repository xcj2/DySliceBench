import collections


class Graph:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.edges = [[] for _ in range(n_nodes)]

    def add_edge(self, s, t):
        self.edges[s].append(t)
        self.edges[t].append(s)


n = int(input())
graph = Graph(n)
for i in range(n):
    s = input().rstrip()
    for j in range(i + 1, n):
        if s[j] == '1':
            graph.add_edge(i, j)


def check(node):
    for new_node in graph.edges[node]:
        if orders[new_node] == -1:
            q.append(new_node)
            orders[new_node] = orders[node] + 1
        elif abs(orders[new_node] - orders[node]) != 1:
            return False
    return True


res = []
for i in range(n):
    orders = [-1] * n
    q = collections.deque()
    q.append(i)
    orders[i] = 1
    while q:
        node = q.popleft()
        ok = check(node)
        if not ok:
            break
    else:
        res.append(max(orders))
if len(res) == 0:
    print(-1)
else:
    print(max(res))