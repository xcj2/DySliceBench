def d_median_of_medians(N, A):
    class BIT(object):
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (self.size + 1)

        def __str__(self):
            return '[{}]'.format(', '.join(map(str, self.tree)))

        def sum(self, index):
            # 1からindexまでの和を計算
            ret = 0
            x = index
            while x > 0:
                ret += self.tree[x]
                x -= x & (-x)
            return ret

        def add(self, index, value):
            # tree[index]にvalueを加算
            x = index
            while x <= self.size:
                self.tree[x] += value
                x += x & (-x)

    def pair(x):
        a_prime = [-1] * N
        for k in range(N):
            if A[k] >= x:
                a_prime[k] = 1  # x未満か否かを{-1, 1}に圧縮

        s = [0]
        min_s = 0
        max_s = 0
        tmp = 0
        # 累積和と最小値, 最大値を同時に計算
        for a in a_prime:
            tmp += a
            min_s = min(min_s, tmp)
            max_s = max(max_s, tmp)
            s.append(tmp)

        bit_size = max_s - min_s + 1  # BITのサイズ
        bit = BIT(bit_size)
        ans = 0
        for sk in s:
            sk -= (min_s - 1)  # sの最小値を1に調整
            ans += bit.sum(sk)
            bit.add(sk, 1)
        return ans

    # l<=rとなる(l, r)の取り方について、その半分以上の値を返す最大の値が中央値
    border_median = (N * (N + 1) // 2 + 1) // 2
    ok = 0
    ng = 10**9 + 1  # 数列の要素の値の制約から、この値は中央値になりえない
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if pair(mid) >= border_median:
            ok = mid
        else:
            ng = mid
    ans = ok
    return ans

N = int(input())
A = [int(i) for i in input().split()]
print(d_median_of_medians(N, A))