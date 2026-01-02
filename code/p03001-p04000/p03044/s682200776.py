import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import defaultdict

def main():
    N = II()
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = LI()
        u, v = u - 1, v - 1
        w = w % 2
        edges[u].append([v, w])
        edges[v].append([u, w])
    ans = [-1] * N
    ans[0] = 0
    def solve(k):
        for e, w in edges[k]:
            if ans[e] == -1:
                ans[e] = ans[k] if w == 0 else 1 - ans[k]
                solve(e)
    solve(0)
    for a in ans:
        print(a)
    return

main()