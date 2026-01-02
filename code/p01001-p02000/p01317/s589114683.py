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


def m():
    def main(n, m):
        dps = [[inf] * n for i in range(n)]
        dpl = [[inf] * n for i in range(n)]

        for _ in range(m):
            x, y, t, sl = sys.stdin.readline().split()
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
        v = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
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
if __name__ == "__main__":
    m()
