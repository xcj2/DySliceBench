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

from collections import defaultdict
from bisect import bisect_right

s = ns()
t = ns()

ok = True

sset = set(list(s))
for ti in t:
    if ti not in sset:
        ok = False
        break

if not ok:
    print(-1)

else:
    n = len(s)

    charidx = defaultdict(list)

    for i, si in enumerate(s):
        charidx[si].append(i)
    for i, si in enumerate(s):
        charidx[si].append(n+i)

    ks = charidx.keys()

    move = [{ki: -1 for ki in ks} for _ in range(n)]

    for i, si in enumerate(s):
        for ki in ks:
            idxlist = charidx[ki]
            nexidx = bisect_right(idxlist, i)
            move[i][ki] = (idxlist[nexidx] - i) % (n+1)

    cur = s.index(t[:1])
    ans = cur
    for ti in t[1:]:
        nex = move[cur][ti]
        ans += nex
        cur = (cur + nex) % n

    print(ans+1)
