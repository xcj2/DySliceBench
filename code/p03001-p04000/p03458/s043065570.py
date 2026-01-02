import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()


def main():
    n, k = map(int, input().split())
    K = k * 2
    """
    K * Kに点を全て移したので、この中で黒模様の左下の頂点を全探索。
    二次元累積和で各場合についてO(1)で計算可能。

    まず前準備として白マスはxかyに関してkずらすことで黒マスにできる。こうすれば記述量はもっと減らせた。
    """
    hope = [[0] * (K + 1) for _ in range(K + 1)]
    for _ in range(n):
        x, y, c = input().split()
        x, y = int(x), int(y)
        if c == 'B':
            """あとで累積和を0-indexedで取る都合上、頂点座標は1-indexedにしておく。"""
            hope[1 + y % K][1 + x % K] += 1
        if c == 'W':
            hope[1 + (y + k) % K][1 + x % K] += 1

    """
    二次元累積和の書き方に悩んでたのは失態。
    やってみて気づいたが、やはり累積和は0-indexedにしないと後々の取り扱いが非常に面倒。
    """
    sumB = [[0] * (K + 1) for _ in range(K + 1)]
    for y in range(1, K + 1):
        for x in range(1, K + 1):
            sumB[y][x] = sumB[y-1][x] + sumB[y][x-1] + hope[y][x] - sumB[y-1][x-1]

    def calc_sum(x0, y0, x1, y1):
        # (x0, y0)が左下、(x1, y1)が右上となる矩形領域の値を返す
        return sumB[y1][x1] - sumB[y0-1][x1] - sumB[y1][x0-1] + sumB[y0-1][x0-1]

    """
    あとは黒四角の左下頂点(x, y)に関して全探索。
    """
    ans = 0
    for y in range(1, K+1):
        for x in range(1, k+1):
            if y <= k:
                val = (calc_sum(1, 1, x-1, y-1) + calc_sum(x, y, x+k-1, y+k-1)
                        + calc_sum(x+k, y+k, K, K) + calc_sum(x+k, 1, K, y-1)
                        + calc_sum(1, y+k, x-1, K))
                ans = max(ans, val)
            else:
                val = (calc_sum(x, 1, x+k-1, y-k-1) + calc_sum(1, y-k, x-1, y-1)
                        + calc_sum(x+k, y-k, K, y-1) + calc_sum(x, y, x+k-1, K))
                ans = max(ans, val)
    print(ans)



if __name__ == "__main__":
    main()
