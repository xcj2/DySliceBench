import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        edges[a].append(b)
        edges[b].append(a)

    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x

    def dfs(cur, par):
        for nex in edges[cur]:
            if nex == par:
                continue
            counter[nex] += counter[cur]
            dfs(nex, cur)

    dfs(0, -1)
    print(*counter, sep=" ")


if __name__ == "__main__":
    main()
