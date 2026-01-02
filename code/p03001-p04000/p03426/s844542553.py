import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W, D = ZZ()
    A = [ZZ() for _ in range(H)]
    Q = Z()
    query = [ZZ() for _ in range(Q)]

    pos = [(-1, -1) for _ in range(H*W+1)]
    for i in range(H):
        for j in range(W): pos[A[i][j]] = (i, j)
    cost = [0] * (H*W+1)

    def calc(now, c):
        cost[now] = c
        if now+D > H*W: return
        x, y = pos[now]
        nx, ny = pos[now+D]
        nc = abs(nx-x) + abs(ny-y) + c
        calc(now + D, nc)

    for n in range(1, D+1): calc(n, 0)

    for l, r in query: print(cost[r] - cost[l])

    return

if __name__ == '__main__':
    main()
