import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
G = []

class Edge:
    def __init__(self, to, id):
        self.to = to
        self.id = id

ans = []

def dfs(v, fr, c):
    k = 1
    for g in G[v]:
        to = g.to
        id = g.id
        if to != fr:
            if k == c:
                k += 1
            ans[id] = k
            k += 1
            dfs(to, v, ans[id])
    

def main():
    global G, ans
    n = int(input().strip())
    ans = [0] * (n-1)
    G = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = list(map(int, input().strip().split()))
        G[a-1].append(Edge(b-1, i))
        G[b-1].append(Edge(a-1, i))
    dfs(0, -1, -1)

    print(len(set(ans)))
    for v in ans:
        print(v)

if __name__ == '__main__':
    main()
