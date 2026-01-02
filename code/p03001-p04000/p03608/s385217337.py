def warshall_floyd(paths, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                paths[i][j] = min(paths[i][j], paths[i][k] + paths[k][j])


def iter_patterns(l):
    if len(l) == 1:
        return [l]
    patterns = []
    for i in range(len(l)):
        patterns += [[l[i]] + p for p in iter_patterns(l[:i] + l[i+1:])]
    return patterns


def main():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    paths = [[float("inf")] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        paths[A-1][B-1] = C
        paths[B-1][A-1] = C
    for i in range(N):
        paths[i][i] = 0
    warshall_floyd(paths, N)
    retval = float("inf")
    for p in iter_patterns(r):
        dist = 0
        for i in range(R-1):
            dist += paths[p[i]-1][p[i+1]-1]
        retval = min(retval, dist)
    print(retval)


if __name__ == "__main__":
    main()
