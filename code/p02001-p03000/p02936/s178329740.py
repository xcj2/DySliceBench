import sys
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

def main():
    n, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        g[a].append(b); g[b].append(a)
    node = [0]*n
    for i in range(q):
        p, x = map(int, input().split())
        p -= 1
        node[p] += x

    def dfs(v, p=-1):
        for u in g[v]:
            if u==p:
                continue
            node[u] += node[v]
            dfs(u, v)
    dfs(0)
    print(*node)

if __name__ == "__main__":
    main()
