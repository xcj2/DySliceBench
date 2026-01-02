from sys import stdin
from collections import defaultdict
readline = stdin.readline

#readline = open('GRL_5_B-in10.txt').readline

def main():
    n = int(readline())
    g = defaultdict(list)
    for _ in range(n - 1):
        s, t, d = map(int, readline().split())
        g[s].append([d, t])
        g[t].append([d, s])

    dp = defaultdict(dict)
    for i in postorder(g, n):
        for di, ti in g[i]:
            dp[i][ti] = di
            candidate = [v for k, v in dp[ti].items() if k != i]
            if candidate:
                dp[i][ti] += max(candidate)
    height = [None] * n
    for i in preorder(g, n):
        import operator
        candidate = list(dp[i].items())
        candidate.sort(key=operator.itemgetter(1))
        height[i] = candidate[-1][1] if candidate else 0
        for d, t in g[i]:
            dp[t][i] = d
            if 1 < len(candidate):
                k = -1 if candidate[-1][0] != t else -2
                dp[t][i] += candidate[k][1]
    print('\n'.join(map(str, height)))


def postorder(g, n):
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        parent_stack = []
        dfs_stack = [(i, None)]
        while dfs_stack:
            u, prev = dfs_stack.pop()
            visited |= {u}
            dfs_stack.extend((t, u) for d, t in g[u] if t != prev)
            while parent_stack and parent_stack[-1] != prev:
                yield parent_stack.pop()
            parent_stack.append(u)
        while parent_stack:
            yield parent_stack.pop()


def preorder(g, n):
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        dfs_stack = [(i, None)]
        while dfs_stack:
            u, prev = dfs_stack.pop()
            visited |= {u}
            yield(u)
            dfs_stack.extend((t, u) for d, t in g[u] if t != prev)

main()