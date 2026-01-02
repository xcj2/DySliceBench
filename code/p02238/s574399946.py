import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

time = 0

def dfs(u, adj, d, f, sumi):
    global time
    sumi.add(u)
    time += 1
    d[u] = time

    for v in adj[u]:
        if v not in sumi:
            dfs(v, adj, d, f, sumi)
            
    time += 1

    f[u] = time


def solve():
    n = int(input())
    adj = [None] * n

    for i in range(n):
        u, k, *vs = [int(j) - 1 for j in input().split()]
        # debug(vs, locals())
        adj[u] = vs

    # debug(adj, locals())
    
    d = [0] * n
    f = [0] * n
    sumi = {0}
    mitan = set(range(1, n))

    dfs(0, adj, d, f, sumi)
    mitan -= sumi
    # debug(mitan, locals())

    
    while mitan:
        u = min(mitan)
        dfs(u, adj, d, f, sumi)
        mitan -= sumi
        # debug(mitan, locals())
        

    for i in range(n):
        print(i + 1, d[i], f[i])

    pass

if __name__ == '__main__':
    solve()