def tree_height(T, w):
    N = len(T)
    # Consider T to be rooted at r = 0
    downward = [0] * N # the height of the subtree rooted at each v
    upward = [-1] * N # the height of the subtree which contains the root r and is rooted at each v
    height = [-1] * N
    def dfs1(r):
        nonlocal downward
        stack = [(r, -1, 0)] # (vertex, parent, status)
        while stack:
            v, p, st = stack.pop()
            if st == 0: # visited v for the first time
                n_children = 0
                for u in T[v]:
                    if u == p: continue
                    if n_children == 0:
                        stack += [(v, p, 2), (u, v, 0)]
                        n_children += 1
                    else:
                        stack += [(v, p, 1), (u, v, 0)]
                        n_children += 1
                if n_children == 0: # v is a leaf
                    if p != -1:
                        downward[p] = max(downward[p], downward[v] + w[p][v])
            elif st == 1: # now searching
                continue
            else: # search finished
                if p != -1:
                    downward[p] = max(downward[p], downward[v] + w[p][v])
    
    def dfs2(r):
        nonlocal upward, height
        stack = [(r, -1, 0)] # (vertex, parent, status)
        while stack:
            v, p, st = stack.pop()
            if p == -1:
                upward[v] = 0
                height[v] = max(upward[v], downward[v])
            if st == 0: # visited v for the first time
                max1, max2 = sorted([0, -1] + [downward[child] + w[child][v] for child in T[v] if child != p], reverse=True)[:2]
                n_children = 0
                for u in T[v]:
                    if u == p: continue
                    temp = max1
                    if downward[u] + w[u][v] == max1: temp = max2
                    if n_children == 0:
                        stack += [(v, p, 2), (u, v, 0)]
                        upward[u] = max(upward[v], temp) + w[u][v]
                        height[u] = max(upward[u], downward[u])
                        n_children += 1
                    else:
                        stack += [(v, p, 1), (u, v, 0)]
                        upward[u] = max(upward[v], temp) + w[u][v]
                        height[u] = max(upward[u], downward[u])
                        n_children += 1
                if n_children == 0:
                    continue
            elif st == 1: # now searching
                continue
            else: # search finished
                continue
    dfs1(0)
    dfs2(0)
    return height
    
N = int(input())
E = [[] for _ in range(N)]
weight = [{} for _ in range(N)]
for _ in range(N-1):
    s, t, w = map(int, input().split())
    E[s].append(t); E[t].append(s)
    weight[s].setdefault(t, w); weight[t].setdefault(s, w)
height = tree_height(E, weight)
print(*height, sep='\n')
