import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
G = []
ans = []

class Edge:
    def __init__(self, to, id):
        self.to = to
        self.id = id

def dfs(v, fr, frk):
    global ans
    k = 1
    for e in G[v]:
        if e.to != fr:
            if k == frk:
                k += 1
            ans[e.id] = k
            dfs(e.to, v, k)
            k += 1

def main():
    global G, ans
    n = int(input().strip())
    ans = [0] * (n-1)
    G = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = list(map(int, input().strip().split()))
        a -= 1
        b -= 1
        G[a].append(Edge(b, i))
        G[b].append(Edge(a, i))
    dfs(0, -1, -1)
    maxk = 0
    for l in G:
        maxk = max(maxk, len(l))
    print(maxk)
    for p in ans:
        print(p)

if __name__ == '__main__':
    main()
