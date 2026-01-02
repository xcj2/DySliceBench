# # AOJ 2200
#
# INF = float('inf')
#
#
# def floyd_warshall(d):
#     v = len(d)
#     for k in range(v):
#         dk = d[k]
#         for i in range(v):
#             di = d[i]
#             for j in range(v):
#                 di[j] = min(di[j], di[k] + dk[j])
#
#
# def main():
#     while True:
#         N, M = map(int, input().split())
#         if N == M == 0:
#             break
#
#         sea = [[INF] * N for i in range(N)]
#         land = [[INF] * N for i in range(N)]
#         for i in range(N):
#             sea[i][i] = land[i][i] = 0
#
#         for i in range(M):
#             x, y, t, sl = input().split()
#             x = int(x) - 1
#             y = int(y) - 1
#             t = int(t)
#             if sl == 'S':
#                 sea[x][y] = sea[y][x] = min(sea[x][y], t)
#             else:
#                 land[x][y] = land[y][x] = min(land[x][y], t)
#
#         R = int(input())
#         z = list(map(lambda x: int(x) - 1, input().split()))
#
#         floyd_warshall(sea)
#         floyd_warshall(land)
#
#         dp = [INF] * N
#         dp[z[0]] = 0
#         for k in range(1, R):
#             ndp = [INF] * N
#             z1 = z[k-1]
#             z2 = z[k]
#             land_z1 = land[z1]
#             land_z2 = land[z2]
#             land_z1_z2 = land_z1[z2]
#
#             for i in range(N):
#                 tmp = dp[i] + land_z1_z2
#                 land_i_z2 = land_z2[i]
#                 sea_i = sea[i]
#
#                 for j in range(N):
#                     # ship originally at j
#                     # z1 -> (land) -> j -> (sea) -> i -> (land) -> z2
#                     tmp = min(tmp, dp[j] + land_z1[j] + sea_i[j] + land_i_z2)
#
#                 ndp[i] = tmp
#             dp = ndp
#         print(min(dp))
#
#
# if __name__ == '__main__':
#     main()

inf = float("INF")

class Warshall_Floyd:

    def __init__(self, n, dist):
        self.dist = dist
        self.n = n

    def search(self):
        n = self.n
        dist = self.dist
        for i in range(n):
            dist[i][i] = 0

        for i in range(n):
            di = dist[i]
            for j in range(n):
                dj = dist[j]
                if i == j:
                    continue
                for k in range(n):
                    if dj[k] > dj[i] + di[k]:
                        dj[k] = dj[i] + di[k]

        return dist

import sys


def main(n, m):
    dps = [[inf] * n for i in range(n)]
    dpl = [[inf] * n for i in range(n)]

    for _ in range(m):
        x, y, t, sl = input().split()
        x, y, t = map(lambda x: int(x) - 1, [x, y, t])
        t += 1
        if sl == "S":
            dps[x][y] = t
            dps[y][x] = t
        if sl == "L":
            dpl[x][y] = t
            dpl[y][x] = t

    l = Warshall_Floyd(n, dpl)
    s = Warshall_Floyd(n, dps)
    dpl = l.search()
    dps = s.search()

    r = int(input())
    v = list(map(lambda x: int(x) - 1, input().split()))
    dp1 = [inf] * n
    dp1[v[0]] = 0

    for i in range(r-1):
        b = v[i]
        c = v[i + 1]
        dp2 = [0] * n
        dplb = dpl[b]
        dpk = [dp1[k] + dplb[k] for k in range(n)]

        for j in range(n):
            # 陸路のみ
            # 船の位置は変わらず
            dp2[j] = dp1[j] + dplb[c]

            dpljc = dpl[j][c]
            dpsj = dps[j]
            tmp = dp2[j]

            for k in range(n):
                # 海路あり
                # kに船があるとき
                # v[i-1]→(陸路)→k→(海路)→j→(陸路)→v[i]
                # この時船はjに保管される
                tmp1 = dpk[k] + dpsj[k] + dpljc
                if tmp > tmp1:
                    tmp = tmp1

            dp2[j] = tmp

        dp1 = dp2

    print(min(dp1))


while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    main(n, m)

