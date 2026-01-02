from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dfs(bu, bv, u=0):
        for cu in to[u]:
            if (u, cu) == (bu, bv) or (u, cu) == (bv, bu): continue
            if fin[cu]: continue
            fin[cu] = True
            dfs(bu, bv, cu)

    to = defaultdict(list)
    ee = []
    n, m = MI()
    for _ in range(m):
        a, b = map(int1, input().split())
        to[a].append(b)
        to[b].append(a)
        ee.append([a, b])
    ans = 0
    for u, v in ee:
        fin = [False] * n
        fin[0] = True
        dfs(u, v)
        if sum(fin) < n: ans += 1
    print(ans)

main()
