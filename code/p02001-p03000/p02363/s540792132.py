# GRL_1_C - All Pairs Shortest Path
def floyd_warshall(dist: "Array[Array[int]]") -> None:
    """
    Compute the shortest paths of all pairs.
    """
    V = len(dist)
    for i in range(V):  # intermediate point
        for j, c2 in enumerate(dist[j][i] for j in range(V)):  #  source
            for k, (c1, c3) in enumerate(zip(dist[j], dist[i])):  # target
                if c2 + c3 < c1:
                    dist[j][k] = c2 + c3


def detect_negative_cycle(dist: "Array[Array[int]]") -> bool:
    return any(d[i] < 0 for i, d in enumerate(dist))


def main():
    N, M, *E = map(int, open(0).read().split())
    dist = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for v, u, c in zip(*[iter(E)] * 3):
        dist[v][u] = c
    floyd_warshall(dist)
    if detect_negative_cycle(dist):
        print("NEGATIVE CYCLE")
    else:
        for d in dist:
            cur = [i if i != float("inf") else "INF" for i in d]
            print(" ".join(map(str, cur)))


if __name__ == "__main__":
    main()
