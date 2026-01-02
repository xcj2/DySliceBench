def f_encolsed_points(MOD=998244353):
    # 参考: https://atcoder.jp/contests/abc136/submissions/6696160
    import sys
    input = sys.stdin.readline

    class BIT(object):
        """Binary Indexed Tree (1-indexed)"""

        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, index):
            """tree[1]からtree[index]までの和を計算"""
            ret = 0
            while index > 0:
                ret += self.tree[index]
                index -= index & (-index)
            return ret

        def add(self, index, value=1):
            """tree[index]にvalueを加算"""
            while index <= self.size:
                self.tree[index] += value
                index += index & (-index)

    N = int(input())
    Pos = [[int(i) for i in input().split()] for j in range(N)]

    Pos.sort()  # x座標でソートする
    _, pos_y = zip(*Pos)
    y_comp = {y: i for i, y in enumerate(sorted(pos_y), 1)}  # y座標を圧縮

    pow_2 = [1]
    for _ in range(N):
        pow_2.append(pow_2[-1] * 2 % MOD)

    ans = 0
    tree = BIT(N)
    # x座標が小さな点から順に考える
    for left, (_x, _y) in enumerate(Pos):
        y = y_comp[_y]

        # それぞれ、注目している点の 右|下|上 にいくつ点が存在するか
        right = N - 1 - left
        down = y - 1
        up = N - 1 - down

        lower_left = tree.sum(y)
        tree.add(y, 1)
        upper_left = left - lower_left
        lower_right = down - lower_left
        upper_right = right - lower_right

        # 包除原理(全体 - 上下左右 + 左上左下右上右下 - それ自体)
        count = (pow_2[N]
                 - (pow_2[up] + pow_2[down] + pow_2[left] + pow_2[right])
                 + (pow_2[upper_left] + pow_2[lower_left] + pow_2[upper_right] + pow_2[lower_right])
                 - 1)
        ans += count
        ans %= MOD
    return ans

print(f_encolsed_points())