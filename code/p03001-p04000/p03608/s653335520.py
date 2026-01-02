import itertools
import sys

INF = 10 ** 9

def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M, R = ZZ()
    r = ZZ()
    d = [[INF] * (N) for _ in range(N)]
    for i in range(N): d[i][i] = 0
    for _ in range(M):
        a, b, c = ZZ()
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N): d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    ans = INF
    for v in itertools.permutations(r, R):
        cc = 0
        for i in range(R-1): cc += d[v[i]-1][v[i+1]-1]
        ans = min(ans, cc)
    print(ans)

    return

if __name__ == '__main__':
    main()
