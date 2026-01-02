import sys

def f(a, D):
    N = len(D)
    p = []
    for i in range(N):
        if D[a][i] == 1:
            p.append(i)
    return p


def wfs(e, D):
    N = len(D)
    a, b = e[0], e[1]

    p = f(a, D)
    used = [a]
    while len(p) > 0:
        x = p.pop(0)
        used.append(x)

        if x == b:
            return True

        q = f(x, D)
        for j in q:
            if j in used:
                continue
            p.append(j)

    return False


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = []
    for _ in range(M):
        a, b = map(int, input().split())
        G.append((a-1, b-1))

    ans = 0
    for i in range(M):
        D = [[0 for _ in range(N)] for _ in range(N)]
        for j in range(M):
            if j == i:
                continue

            a, b = G[j][0], G[j][1]
            D[a][b] = 1
            D[b][a] = 1

        if not wfs(G[i], D):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
