import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from bisect import bisect_right

s = ns()
t = ns()

# 判定
ok = True
sset = set(list(s))
tset = set(list(t))
for ti in tset:
    if ti not in sset:
        ok = False

if not ok:
    print(-1)
else:
    n = len(s)
    nex = [[] for _ in range(26)]
    sdouble = s + s
    orda = ord("a")
    for i, si in enumerate(sdouble):
        nex[ord(si) - orda].append(i)

    bef = t[:1]
    cur = s.index(t[:1])
    ans = cur

    for ti in t[1:]:
        chridx = ord(ti) - orda
        dest = bisect_right(nex[chridx], cur)
        ans += (nex[chridx][dest] - cur)
        cur = ans % n

    print(ans+1)