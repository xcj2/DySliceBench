import sys
from itertools import permutations

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

cnt = 0

def dfs(N, Adj, p, pos, mask):
    global cnt

    if pos == N:
        for i in range(N - 1):
            if not Adj[p[i]][p[i + 1]]:
                break
        else:
            cnt += 1

        return None

    for i in range(N):
        if mask & (1 << i):
            p[pos] = i
            dfs(N, Adj, p, pos + 1, (mask ^ (1 << i)))

    return None

def solve():
    global cnt
    cnt = 0

    N, M = map(int, input().split())
    Adj = [[0]*N for i in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        Adj[a][b] = 1
        Adj[b][a] = 1

    p = list(range(N))
    dfs(N, Adj, p, 1, (2 << N) - 1 - 1)

    print(cnt)

if __name__ == '__main__':
    solve()