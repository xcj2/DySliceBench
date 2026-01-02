# input
n = int(input())
edges = set(tuple(int(i) for i in input().split()) for _ in range(n-1))


from collections import deque


def make_connection(tree):
    con = [[] for _ in range(n+1)]
    for edge in tree:
        con[edge[0]].append(edge[1])
        con[edge[1]].append(edge[0])
    return con


def diameter(tree):
    c = make_connection(tree)
    _, s = farest(tree, c, 1)
    diam, _ = farest(tree, c, s)
    return diam


def farest(tree, con, i):
    dp = [None for _ in range(n+1)]
    dp[i] = 0
    cand_q = deque()
    cand_q.append(i)

    while len(cand_q) > 0:
        u = cand_q.popleft()

        for v in con[u]:
            if dp[v] is None:
                cand_q.append(v)
                dp[v] = dp[u] + 1
    max_ = max(dp[1:])
    i_max = dp.index(max_)
    return max_, i_max


d = diameter(edges)


print('Second' if d % 3 == 1 else 'First')
