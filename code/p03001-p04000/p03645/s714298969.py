import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    repn = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        repn[a - 1].append(b - 1)
        repn[b - 1].append(a - 1)
    visited = [0] * N

    def dfs(u, n):
        if n >= 2:
            visited[u] = 1
            return
        visited[u] = 1
        for v in repn[u]:
            if visited[v] != 0: continue
            dfs(v, n + 1)

    dfs(0, 0)
    if visited[N - 1] == 1:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
