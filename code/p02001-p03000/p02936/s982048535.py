import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def readlines(n):
    for _ in range(n):
        a, b = map(int, input().split())
        yield a, b

def main():
    n, q = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for a, b in readlines(n-1):
        edges[a].append(b)
        edges[b].append(a)

    counter = [0] * (n+1)
    for q, x in readlines(q):
        counter[q] += x

    def dfs(u, prev):
        for v in edges[u]:
            if v == prev:
                continue
            counter[v] += counter[u]
            dfs(v, u)

    dfs(1, 0)

    print(" ".join(map(str, counter[1:])))

main()