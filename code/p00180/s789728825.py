import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, M = map(int, readline().split())
    if N == 0:
        return False
    *p, = range(N)
    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px == py:
            return 0
        if px < py:
            p[py] = px
        else:
            p[px] = py
        return 1

    E = []
    for i in range(M):
        a, b, c = map(int, readline().split())
        E.append((c, a, b))
    E.sort()
    ans = 0
    for c, a, b in E:
        if unite(a-1, b-1):
            ans += c
    write("%d\n" % ans)
    return True
while solve():
    ...
