N = int(input())
U, V, W = [], [], []
T = [[] for _ in range(N)]
# tree
class Tree(object):
    def __init__(self, us, vs, ws):
        self.con_table = [[] for _ in range(len(us) + 1)]
        self.weights = dict()
        for (u, v, w) in zip(us, vs, ws):
            self.con_table[u-1].append(v-1)
            self.con_table[v-1].append(u-1)
            self.weights[(u-1, v-1)] = w
        self.init_search()

    def init_search(self):
        self.visited = [False for _ in range(len(self.con_table))]

dists = [None for _ in range(N)]

from collections import deque

def dfs(tree, s):
    tree.init_search()
    dists[s] = 0
    while not all(tree.visited):
        search = deque()
        tree.visited[s] = True
        search.append(s)
        while len(search) > 0:
            v = search.pop()
            for u in tree.con_table[v]:
                if not tree.visited[u]:
                    dists[u] = dists[v] + tree.weights[(min(u, v), max(u, v))]
                    tree.visited[u] = True
                    search.append(u)

for _ in range(N-1):
    u, v, w = map(int, input().split())
    U.append(u)
    V.append(v)
    W.append(w)

tree = Tree(U, V, W)

dfs(tree, 0)

print('\n'.join(('0' if d % 2 == 0 else '1') for d in dists))
