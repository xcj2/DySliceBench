
import sys
def I():
    return int(sys.stdin.readline().rstrip())

def MI():
    return map(int, sys.stdin.readline().rstrip().split())


def main():
    N = I()
    dist = [[100] * (N + 1) for _ in range(N + 1)]  # 2点間の最短距離
    edges = {}

    for i in range(N - 1):
        a, b = MI()
        dist[a][b] = 1
        dist[b][a] = 1
        edges[(a, b)] = i
        edges[(b, a)] = i

    for i in range(1, N + 1):
        dist[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    M = I()
    A = []  # uとvを結ぶ経路上にある辺の集合
    for _ in range(M):
        u, v = MI()
        B = set()
        while True:
            if dist[u][v] == 1:
                B.add(edges[(u, v)])
                break
            else:
                for i in range(1, N + 1):
                    if dist[u][i] == dist[u][v] - 1 and dist[i][v] == 1:
                        B.add(edges[(i, v)])
                        v = i
                        break
        A.append(B)

    # 包除原理

    ans = 0
    for i in range(2 ** M):
        C = set()
        a = 0
        for j in range(M):
            if (i >> j) & 1:
                C |= A[j]
                a += 1
        l = len(C)
        a %= 2
        ans += (-1) ** a * 2 ** (N - 1 - l)

    print(ans)

if __name__ == '__main__':
    main()
