import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
G = []
class Edge:
    def __init__(self, to, w):
        self.to = to
        self.w = w

def dfs(s, d, fr, dist):
    dist[s] = d
    for edge in G[s]:
        if edge.to != fr:
            dfs(edge.to, d + edge.w, s, dist)


def main():
    global G
    n = int(input().strip())
    G = [[] for _ in range(n)]
    d1 = [0] * n
    d2 = [0] * n
    for i in range(n-1):
        s, t, w = map(int, input().strip().split())
        G[s].append(Edge(t, w))
        G[t].append(Edge(s, w))
    dfs(0, 0, -1, d1)
    j = d1.index(max(d1))
    dfs(j, 0, -1, d2)
    print(max(d2))


if __name__ == '__main__':
    main()

