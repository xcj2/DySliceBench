import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    x, y = list(map(lambda x: int(x)-1, input().split()))
    edges[x].append(y)


def memoize(f):
    memo = [-1]*n

    def memoized(args):
        if memo[args] != -1:
            return memo[args]
        else:
            memo[args] = f(args)
            return memo[args]
    return memoized


@memoize
def longest_path(v):
    retval = 0
    for v2 in edges[v]:
        retval = max(retval, longest_path(v2)+1)
    return retval


ans = 0
for i in range(n):
    ans = max(ans, longest_path(i))
print(ans)