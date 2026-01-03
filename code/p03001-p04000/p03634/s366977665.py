import sys
sys.setrecursionlimit(10 ** 6)


def main():
    N = int(input())

    abc = []
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        abc.append((a, b, c))

    Q, K = map(int, input().split())
    xy = []
    for _ in range(Q):
        x, y = map(int, input().split())
        xy.append((x, y))

    ans = ref_pypy(N, abc, Q, K, xy)
    print(*ans, sep="\n")


def ref_pypy(N, abc, Q, K, xy):
    """https://atcoder.jp/contests/abc070/submissions/5331379"""
    L = [-1 for i in range(N+1)]
    L[K] = 0
    n = [[] for i in range(N+1)]
    for a, b, c in abc:
        n[a].append([b, c])
        n[b].append([a, c])

    def dfs(x):
        for i in n[x]:
            if L[i[0]] == -1:
                L[i[0]] = L[x]+i[1]
                dfs(i[0])

    dfs(K)

    ans = []
    for x, y in xy:
        ans.append(L[x] + L[y])

    return ans


if __name__ == "__main__":
    main()
