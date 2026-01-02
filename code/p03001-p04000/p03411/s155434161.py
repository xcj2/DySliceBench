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

from operator import itemgetter

n = ni()
ab = [tuple(li()) for i in range(n)]
cd = [tuple(li()) for i in range(n)]

ab.sort(key=itemgetter(0), reverse=True)
cd.sort(key=itemgetter(1))

cd_used = [False]*n

ans = 0
for ai, bi in ab:
    for j, (cj, dj) in enumerate(cd):
        if ai < cj and bi < dj and (not cd_used[j]):
            cd_used[j] = True
            ans += 1

            break

print(ans)