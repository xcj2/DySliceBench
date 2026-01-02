class Tree():
    def __init__(self, n, edge):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - 1].append(e[1] - 1)
            self.tree[e[1] - 1].append(e[0] - 1)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)

    def euler_tour(self):
        res = []
        begin = [None for _ in range(self.n)]
        end = [None for _ in range(self.n)]
        visited = [0 for _ in range(self.n)]
        visited[self.root] = 1
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node >= 0:
                res.append(node)
                stack.append(~node)
                if begin[node] is None:
                    begin[node] = len(res) - 1
                for adj in self.tree[node]:
                    if visited[adj]:
                        continue
                    visited[adj] = 1
                    stack.append(adj)
            else:
                end[~node] = len(res)
                if ~node != self.root:
                    res.append(self.parent[~node])
        return res, begin, end


from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

T = Tree(N, E)
T.setroot(0)

et, _, _ = T.euler_tour()
res = [None for _ in range(N)]
lis = []
rec = [None for _ in range(N)]
prev = None

for node in et:
    if res[node] is None:
        if not lis or A[node] > lis[-1]:
            lis.append(A[node])
        else:
            idx = bisect_left(lis, A[node])
            rec[node] = (idx, lis[idx])
            lis[idx] = A[node]
        res[node] = len(lis)

    else:
        if rec[prev] is not None:
            lis[rec[prev][0]] = rec[prev][1]
        else:
            lis.pop()

    prev = node

print('\n'.join(map(str, res)))