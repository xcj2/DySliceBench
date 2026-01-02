# -*- coding: utf-8 -*-

# See:
# http://drken1215.hatenablog.com/entry/2018/06/08/210000
max_value = 500050
mod = 10 ** 9 + 7

fac = [0 for _ in range(max_value)]
finv = [0 for _ in range(max_value)]
inv = [0 for _ in range(max_value)]


def com_init():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, max_value):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def com(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def main():
    n, k = map(int, input().split())
    # abst: 数列の並び順が問題にならない場合は、ソートするのも選択肢に入れる
    a = sorted(list(map(int, input().split())))
    com_init()
    ans = 0

    # KeyInsight
    # Σf(x) = Σmax(x) - Σmin(x)と置き換えられる
    # abst: 等価な性質を利用して、シンプルな問題に
    # See:
    # https://www.youtube.com/watch?v=1oLDDdWRu6Y&feature=youtu.be
    # 最大値が選ばれるパターン
    for index, ai in enumerate(a):
        # abst: ◯◯◯◯◯◯◯ (昇順に並び替えた数字のイメージ)
        #            ↑
        # 矢印の位置が最大値となる場合、左から5つのうちk - 1個を自由に選べる
        # この例だと、5Ck-1個
        # abst: 視点をある位置に固定する
        # abst: 条件を満たす場合は二項係数を使うことで組み合わせを高速に数えられる
        # nCrを高速に計算する&ライブラリ化
        now = com(index, k - 1)
        ans += now * ai

    # 最小値が選ばれるパターン
    # abst: 数列の並びを逆順に
    for index, ai in enumerate(a[::-1]):
        now = com(index, k - 1)
        ans -= now * ai

    print(ans % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
