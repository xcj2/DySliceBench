# D - AtCoder Express 2
# https://atcoder.jp/contests/abc106/tasks/abc106_d

import sys

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in list(ss)]
ss2nnn = lambda ss: [s2nn(s) for s in list(ss)]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline() for _ in range(n)]
ii2nnn = lambda n: ss2nnn(ii2ss(n))

# N 個の都市
# M 本の列車
# Q 個の興味
def main_lte(N, M, Q, LRm, PQq):
    for p, q in PQq:
        ans = 0
        for l, r in LRm:
            if p <= l and r <= q:
                ans += 1
        print(ans)

def main_lte2(N, M, Q, LRm, PQq):
    table = [[0] * (N+1) for _ in range(N+1)]
    for l, r in LRm:
        table[l][r] += 1
    for p, q in PQq:
        ans = 0
        for i in range(p, q+1):
            for j in range(i, q+1):
                ans += table[i][j]
        print(ans)

def main_lte3(N, M, Q, LRm, PQq):
    table = [[0] * (N+1) for _ in range(N+1)]
    for l, r in LRm:
        table[l][r] += 1
    # 累積輪
    table2 = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            table2[i][j] = table2[i][j-1] + table[i][j]
    for p, q in PQq:
        ans = 0
        for i in range(p, q+1):
            ans += table2[i][q] - table2[i][p-1]
        print(ans)

def main(N, M, Q, LRm, PQq):
    table = [[0] * (N+1) for _ in range(N+1)]
    for l, r in LRm:
        table[l][r] += 1
    # 二次元累積輪
    for i in range(1, N+1):
        for j in range(1, N+1):
            table[i][j] += table[i][j-1]
    for i in range(1, N+1):
        for j in range(1, N+1):
            table[i][j] += table[i-1][j]
    for p, q in PQq:
        ans = table[q][q] + table[p-1][p-1] - table[p-1][q] - table[q][p-1]
        print(ans)

N, M, Q = i2nn()
LRm = ii2nnn(M)
PQq = ii2nnn(Q)
main(N, M, Q, LRm, PQq)
