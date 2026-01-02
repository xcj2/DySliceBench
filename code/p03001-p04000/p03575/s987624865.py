import sys
from collections import defaultdict
import copy

def is_connect(adj):
    is_already = defaultdict(bool)
    is_already[list(adj.keys())[0]] = True;

    queue = []
    queue.append(1)
    while len(queue) > 0:
        v = queue.pop()
        for node in adj[v]:
            if not is_already[node]:
                is_already[node] = True
                queue.append(node)

    return all([is_already[node] for node in adj.keys()])

def solve(n,m,adj,edges):
    ans = 0
    for (v1, v2) in edges:
        tmp_adj = copy.deepcopy(adj)
        tmp_adj[v1].remove(v2)
        tmp_adj[v2].remove(v1)
        if not is_connect(tmp_adj):
            ans += 1

    return ans

def main():
    s = sys.stdin.readline().rstrip()
    lst = s.split(' ')
    n = int(lst[0])
    m = int(lst[1])

    adj = defaultdict(list)
    edges = []

    for i in range(m):
        s = sys.stdin.readline().rstrip()
        lst = s.split(' ')
        a = int(lst[0])
        b = int(lst[1])
        edges.append((a,b))
        if not b in adj[a]:
            adj[a].append(b)

        if not a in adj[b]:
            adj[b].append(a)

    ans = solve(n,m,adj,edges)
    print(ans)
    return 0

if __name__ == '__main__':
    sys.exit(main())
