def main():
    """
    1 <= N      <= 100
    0 <= xi, yi <= 100
    0 <= hi     <= 10^9
    """
    N = int(input())
    x, y, h = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    # ans = no_sub(x, y, h)
    ans = editorial_movie(x, y, h)
    print(*ans)


def h_H(cx, cy, x, y):
    return - abs(x - cx) - abs(y - cy)


def no_sub(x, y, h):
    max_h = -1
    ans = None
    dict_h = {(_x, _y): _h for _x, _y, _h in zip(x, y, h)}
    for _x, _y, _h in zip(x, y, h):
        for cx in range(1, 100+1):
            for cy in range(1, 100+1):
                tmp = h_H(cx, cy, _x, _y)
                pos = (cx, cy)
                H = _h - tmp
                if pos in dict_h and H != dict_h[pos]:
                    continue

                if H > max_h:
                    max_h = H
                    ans = _x, _y, H

                # print((_x, _y), (cx, cy), _h, tmp, sep="\t")

    return ans


def editorial_movie(x, y, h):
    """
    H >= 1, これ重要
        コンテスト中にこれを意識していなかった
        入力の制約しか意識していなかった

    h(x, y) = max(H - |x - Cx| - |y - Cy|, 0)
    より
        h(x,y) > 0: H  = h(x, y) + |x - Cx| - |y - Cy|
        h(x,y) = 0:
            頂点なら制約を満たしていない
                    H <= h(x, y) + |x - Cx| - |y - Cy|
    """
    for cx in range(100 + 1):
        for cy in range(100 + 1):
            # 頂上がどれくらいの高さであってほしいか。
            # -1はまだ良く分からない時。0以上は確定してるとき
            # -2はダメだって分かった時
            need_h = -1

            # h=0 より大きい場合の検証
            for _x, _y, _h in zip(x, y, h):
                if not _h > 0:
                    continue

                # 頂点候補座標および調査座標の組合せにおいてHになるべき値
                tmp = _h + abs(_x - cx) + abs(_y - cy)
                if need_h == -1:
                    need_h = tmp
                elif need_h != tmp:
                    need_h = -2
                    break

            if need_h == -2:
                continue

            # h=0 の検証
            for _x, _y, _h in zip(x, y, h):
                if not _h == 0:
                    continue

                # _h == 0 より、計算式上では省略してマンハッタン距離のみ求めている
                dist = abs(_x - cx) + abs(_y - cy)
                if need_h > dist:
                    need_h = -2
                    break

            if need_h == -2:
                continue

            return cx, cy, need_h


if __name__ == '__main__':
    main()
