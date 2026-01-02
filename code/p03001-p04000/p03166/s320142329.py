"""
AtCoder Educational DP Contest
https://atcoder.jp/contests/dp/tasks/dp_g

G - Longest path

"""
import collections
import functools
import sys
sys.setrecursionlimit(1000000)


def get_adj_list(pairs):
    adj = collections.defaultdict(list)
    for (i, j) in pairs:
        adj[i].append(j)
    return adj


def solve(pairs):
    adj_list = get_adj_list(pairs)

    @functools.lru_cache(1000000)
    def dfs(u):
        res = -1
        for v in adj_list[u]:
            res = max(res, dfs(v))
        return 1 + res

    # depths = [dfs(u) for u in range(1, N+1)]
    # print(depths)
    depths = (dfs(u) for u in range(1, N+1))
    return max(depths, default=0)


N, M = map(int, input().split())
pairs = [[int(s) for s in input().split()] for _ in range(M)]
res = solve(pairs)
print(res)
