import sys
input = sys.stdin.readline


def solve(N, M, edges):
    def is_connected(es):
        e = [[False]*(N+1) for _ in range(N+1)]
        for a, b in es:
            e[a][b] = True
            e[b][a] = True

        visited = [False]*(N+1)
        s = [1]
        while len(s) > 0:
            v = s.pop()
            visited[v] = True
            for i in range(1, N+1):
                if e[v][i] and not visited[i]:
                    s.append(i)

        for v in range(1, N+1):
            if not visited[v]:
                return False

        return True

    bridge = 0
    for i in range(M):
        if not is_connected(edges[:i] + edges[i+1:]):
            bridge += 1

    return bridge


def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
    print(solve(N, M, edges))


if __name__ == "__main__":
    main()
