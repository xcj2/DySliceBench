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
from collections import Counter

def main():
    N, M = LI()
    edges = [[] for _ in range(N)]
    for _ in range(M):
        x, y, xxx = LI_()
        edges[x].append(y)
        edges[y].append(x)
    ans = 0
    visited = [0] * N
    def connect(k):
        visited[k] = 1
        for e in edges[k]:
            if visited[e] == 0:
                connect(e)
    for i in range(N):
        if visited[i] == 0:
            ans += 1
            connect(i)
    return ans

print(main())