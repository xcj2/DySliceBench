import sys
from collections import deque

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def paint_col(adj, cols, i, col):
    nxt = deque([i])

    while nxt:
        u = nxt.popleft()
        cols[u] = col
        for child in adj[u]:
            if cols[child] == 0:
                nxt.append(child)

def solve():
    n, m = map(int, input().split())
    adj = [[] for i in range(n)]

    for i in range(m):
        s, t = map(int, input().split())
        adj[s].append(t)
        adj[t].append(s)

    cols = [0] * n
    col = 1

    for i in range(n):
        if cols[i] == 0:
            paint_col(adj, cols, i, col)
            col += 1

    q = int(input())

    for i in range(q):
        s, t = map(int, input().split())

        if cols[s] == cols[t]:
            ans = 'yes'
        else:
            ans = 'no'

        print(ans)

if __name__ == '__main__':
    solve()