def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline

    class SegTree():
        def __init__(self, N):
            # N:  処理する区間の長さ
            self.N0 = 2 ** (N - 1).bit_length()
            self.INF = 2100000000
            self.seg_min = [-self.INF] * (2 * self.N0)

        def update(self, index, value):
            index += self.N0 - 1
            self.seg_min[index] = value
            while index > 0:
                index = (index - 1) >> 1
                L = self.seg_min[index * 2 + 1]
                R = self.seg_min[index * 2 + 2]
                if L > R:
                    self.seg_min[index] = L
                else:
                    self.seg_min[index] = R
                # self.seg_min[index] = min(self.seg_min[index * 2 + 1], self.seg_min[index * 2 + 2])

        def query(self, first, last):
            first += self.N0 - 1
            last += self.N0 - 1
            ret = -self.INF
            while first <= last:
                if not first & 1:
                    ret_new = self.seg_min[first]
                    if ret_new > ret:
                        ret = ret_new
                    # ret = min(ret, self.seg_min[first])
                if last & 1:
                    ret_new = self.seg_min[last]
                    if ret_new > ret:
                        ret = ret_new
                    # ret = min(ret, self.seg_min[last])
                first = first >> 1
                last = (last >> 1) - 1
            return ret

    mod = 998244353
    N = int(input())
    info = []
    X = []
    for _ in range(N):
        x, d = map(int, input().split())
        info.append((x, x+d))
        X.append(x)
    info.sort(key=lambda p: p[0])
    X.sort()
    segtree = SegTree(N+1)
    for i in range(N):
        segtree.update(i+1, info[i][1])

    dp = [0] * (N+1)
    dp[-1] = 1
    for i in range(N-1, -1, -1):
        l, r = info[i]
        j = bisect_left(X, r)
        rmax = segtree.query(i+1, j)
        #print(i+1, j, rmax)
        segtree.update(i+1, rmax)
        j2 = bisect_left(X, rmax)
        dp[i] = (dp[i+1] + dp[j2])%mod
    print(dp[0])
    #print(dp)


if __name__ == '__main__':
    main()
