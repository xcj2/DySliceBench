import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

ok = [False for i in range(2505)]
def Bellmanford(edges, n, s):
    d = [float("inf") for i in range(n)]
    d[s] = 0


    for i in range(n):
        for x, y, z in edges:
            if not ok[x] or not ok[y]:#0からn-1へ到達できない点は無視
                continue
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                if i == n - 1:
                    print(-1)
                    exit()
    print(max(0, -d[n - 1]))


def main():
    n, m, p = map(int, input().split())

    to = [[] for i in range(n + 1)]
    rto = [[] for i in range(n + 1)]
    e = []
    for i in range(m):
        a, b, c = map(int, input().split())
        to[a - 1].append(b - 1)
        rto[b - 1].append(a - 1)
        e.append((a - 1, b - 1, p - c))

    #0 から n-1にたどり着けるか調べる
    can_reach_to = [False for i in range(n+1)]
    can_reach_rto = [False for i in range(n+1)]
    def todfs(i):
        if can_reach_to[i]:
            return 0
        can_reach_to[i] = True
        for v in to[i]:
            todfs(v)
    def rtodfs(i):
        if can_reach_rto[i]:
            return 0
        can_reach_rto[i] = True
        for v in rto[i]:
            rtodfs(v)
    todfs(0)
    rtodfs(n-1)
    for i in range(n):
        ok[i] = (can_reach_to[i] & can_reach_rto[i])

    d = Bellmanford(e, n, 0)


if __name__ == '__main__':
    main()
