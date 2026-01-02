import collections

def read():
    N = int(input().strip())
    S = list()
    for i in range(N):
        has_nodes = list(input().strip())
        s = list()
        for i, has_node in enumerate(has_nodes):
            if has_node == '1':
                s.append(i)
        S.append(s)
    return N, S

def bfs(start, V, graph):
    q = collections.deque()
    q.appendleft(start)
    depth = [-1] * V
    depth[start] = 0
    while len(q) > 0:
        s = q.pop()
        for t in graph[s]:
            if depth[t] == -1:
                depth[t] = depth[s] + 1
                q.appendleft(t)
    return depth

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def make_groups(V, depth):
    max_depth = max(depth)
    groups = dict()
    for v in range(V):
        d = depth[v]
        if d in groups.keys():
            groups[d].append(v)
        else:
            groups[d] = [v]
    return groups

def has_edge_in_sibling_nodes(V, graph, depth):
    for i in range(V):
        for j in range(i+1, V):
            if depth[i] == depth[j]:
                if j in graph[i]:
                    return True
    return False


def solve(N, S):
    # 全ての頂点に対してbfs、条件を満たす最大の深さを出力
    max_depth = -1
    for i in range(N):
        depth = bfs(i, N, S)
        if not has_edge_in_sibling_nodes(N, S, depth):
            max_depth = max(max_depth, max(depth) + 1)
    return max_depth

if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
