def f_silver_fox_vs_monster():
    # 参考: https://atcoder.jp/contests/abc153/submissions/9773604
    from bisect import bisect_right
    import sys
    input = sys.stdin.readline
    N, D, A = [int(i) for i in input().split()]
    Monsters = sorted([[int(i) for i in input().split()] for j in range(N)])

    class BIT(object):
        """Binary Indexed Tree (1-indexed)"""

        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, index):
            """array[1] から array[index] までの和を計算"""
            ret = 0
            while index > 0:
                ret += self.tree[index]
                index -= index & (-index)
            return ret

        def add(self, index, value):
            """array[index] に value を加算"""
            while index <= self.size:
                self.tree[index] += value
                index += index & (-index)

    position = [row[0] for row in Monsters]
    hit_point = [row[1] for row in Monsters]
    # [k]: 左から k 番目の敵を爆発の左端で攻撃したときに届く右端の敵のインデックス
    pos_right = [bisect_right(position, pos + 2 * D) for pos in position]

    ans = 0
    bomb_damage = BIT(N + 1)  # bomb_damage.sum(k): 左から k 番目の敵に与えた累計ダメージ
    for i in range(N):
        hp, damage, right = hit_point[i], bomb_damage.sum(i + 1), pos_right[i]
        if hp - damage > 0:
            num_defeat = (hp - damage + A - 1) // A  # 注目中の敵を倒すのに必要な爆発回数
            ans += num_defeat
            bomb_damage.add(i + 1, num_defeat * A)
            # ここから右の敵はダメージが通っていないことを反映
            bomb_damage.add(right + 1, -num_defeat * A)
    return ans

print(f_silver_fox_vs_monster())