import sys
readline = sys.stdin.readline
write = sys.stdout.write
def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

EPS = -1e-9
def convex_hull(ps):
    qs = []
    n = len(ps)
    for p in ps:
        while len(qs)>1 and cross3(qs[-1], qs[-2], p) > -EPS:
            qs.pop()
        qs.append(p)
    t = len(qs)
    for i in range(n-2, -1, -1):
        p = ps[i]
        while len(qs)>t and cross3(qs[-1], qs[-2], p) > -EPS:
            qs.pop()
        qs.append(p)
    return qs

def solve():
    N = int(readline())
    if N == 0:
        return False
    P = [list(map(float, readline().split(","))) for i in range(N)]
    P.sort()
    Q = convex_hull(P)
    write("%d\n" % (N - len(Q) + 1))
    return True
while solve():
    ...
