import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


def main():
    def dfs(now, prev=-1):
        for next in edge[now]:
            if next == prev:
                continue
            score[next] += score[now]
            dfs(next, now)

    N, Q = map(int, input().split())
    edge = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    p = []
    x = []
    score = [0] * (N+1)
    for _ in range(Q):
        p, x = map(int, input().split())
        score[p] += x
    dfs(1)
    print(*score[1:])


if __name__ == "__main__":
    main()
