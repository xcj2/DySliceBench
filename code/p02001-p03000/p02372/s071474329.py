from collections import deque


def solve(tree, root):
    def dfs1():
        """各頂点の部分木内で最も遠い頂点(葉)までの距離を求める"""
        q1 = deque([root])
        q2 = deque([root])
        while q1:
            v = q1.pop()
            for nxt_v, cost in tree[v]:
                if nxt_v in par:
                    continue
                else:
                    par[nxt_v] = v
                    q1.append(nxt_v)
                    q2.append(nxt_v)
        while q2:
            v = q2.pop()
            for nxt_v, cost in tree[v]:
                if nxt_v == par[v]:
                    continue
                else:
                    dist1[v] = max(dist1[v], dist1[nxt_v] + cost)
    
    def dfs2():
        """全方位木DPで各頂点の最も遠い頂点(葉)までの距離を求める"""
        q = deque([(root, 0)])
        while q:
            v, par_d = q.pop()
            tmp = [(0, -1)]
            for nxt_v, cost in tree[v]:
                if nxt_v == par[v]:
                    tmp.append((par_d + cost, nxt_v))
                else:
                    tmp.append((cost + dist1[nxt_v], nxt_v))
            tmp = sorted(tmp, reverse=True)
            dist2[v] = tmp[0][0]
            for nxt_v, cost in tree[v]:
                if nxt_v == par[v]:
                    continue
                if tmp[0][1] != nxt_v:
                    q.append((nxt_v, tmp[0][0]))
                else:
                    q.append((nxt_v, tmp[1][0]))

    par = {root: -1}
    dist1 = [0] * n
    dist2 = [0] * n
    dfs1()
    dfs2()
    return dist2
    
    
n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]
tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b, cost = info[i]
    tree[a].append((b, cost))
    tree[b].append((a, cost))
root = 0

ans = solve(tree, root)
for res in ans:
    print(res)
