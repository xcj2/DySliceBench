import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import defaultdict

def main():
    N = II()
    edges = defaultdict(list)
    for _ in range(N):
        x, y = LI()
        edges[x].append(-y)
        edges[-y].append(x)
    visited = defaultdict(int)
    if max(len(li) for li in edges.values()) == 2 and N >= 10 ** 4:
        m, p = 0, 0
        for k in edges.keys():
            if k < 0:
                m += 1
            else:
                p += 1
        return m * p - N
    def solve(v):
        visited[v] = 1
        ret = [v]
        for u in edges[v]:
            if not visited[u]:
                ret += solve(u)
        return ret
    ans = -N
    for node in edges:
        if not visited[node]:
            li = solve(node)
            m, p = 0, 0
            for z in li:
                if z < 0:
                    m += 1
                else:
                    p += 1
            ans += m * p
    return ans

print(main())