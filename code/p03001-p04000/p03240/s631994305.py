import sys


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

    if "PyPy" in sys.version:
        ans4 = loop_xyh_N(x, y, h)
        print(*ans4)
    else:
        # ans = no_sub(x, y, h)
        ans1 = editorial_movie(x, y, h)
        ans2 = editorial_pdf(x, y, h)
        ans3 = ref_sub_xyn(x, y, h)
        print(*ans2)
        assert ans1 == ans2 == ans3


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
        h(x,y) > 0:
            H            - |x - Cx| - |y - Cy| > 0
            H  = h(x, y) + |x - Cx| - |y - Cy|
        h(x,y) = 0:
            H            - |x - Cx| - |y - Cy| <= 0
            H <= h(x, y) + |x - Cx| + |y - Cy|
            頂点なら制約を満たしていない
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


def ref_sub_xyn(x, y, h):
    """
    https://beta.atcoder.jp/contests/abc112/submissions/3348987
    """
    for cx in range(100 + 1):
        for cy in range(100 + 1):
            # 頂点候補をだしておき、0なら1に補正して確実に頂点候補とする
            # h_min, h_max は矛盾の確認用に２つ用意
            h_min = h[0] + abs(x[0] - cx) + abs(y[0] - cy)
            h_max = h_min
            if h[0] == 0:
                h_min = 1

            for _x, _y, _h in zip(x[1:], y[1:], h[1:]):
                # min: TODO
                h_max = min(h_max, _h + abs(_x - cx) + abs(_y - cy))
                if _h != 0:
                    h_min = max(h_min, _h + abs(_x - cx) + abs(_y - cy))

            if h_min == h_max:
                return cx, cy, h_min


def editorial_pdf(x, y, h):
    """
    条件を満たすピラミッドがただ 1 つなのであれば、必ず以下のものが 1 個以上存在します。
        • 調査で得られた情報のうち、hi ≥ 1 を満たす情報 (xi, yi, hi)。

    なぜなら、全部 hi = 0 であるとき、
    調査を行っていない整数座標を中心とする高さ 1 のピラミッドが条件を満たしてしまうので、
        最低でも 101×101− N 個、N = 100 の場合 10, 101 個以上の条件を満たすピラミッドが存在することになるからです。
        そこで、前述の条件を満たす情報のうち 1 個を (xt, yt, ht) とおきます。
    """
    # 候補, 調査点の高さ0のときはない（解説より）
    gx, gy, gh = (-1, -1, -1)
    for _x, _y, _h in zip(x, y, h):
        if _h >= 1:
            gx, gy, gh = _x, _y, _h

    for cx in range(100 + 1):
        for cy in range(100 + 1):
            v = gh + abs(gx - cx) + abs(gy - cy)
            v = max(v, 0)
            flag = True

            for _x, _y, _h in zip(x, y, h):
                # _h との検証
                vv = v - abs(_x - cx) - abs(_y - cy)
                vv = max(vv, 0)
                if _h != vv:
                    flag = False

            if flag:
                return cx, cy, v


def loop_xyh_N(x, y, h):
    h_base = max(h)

    for cx in range(100 + 1):
        for cy in range(100 + 1):
            # 探索範囲100x100より、調査点の候補より200以内
            for ch in range(h_base, h_base + 200 + 1):
                ok = True
                for _x, _y, _h in zip(x, y, h):
                    tmp = _h + abs(_x - cx) + abs(_y - cy)
                    if _h > 0 and ch != tmp:
                        ok = False
                        break
                    elif _h == 0 and ch > tmp:
                        ok = False
                        break

                if ok:
                    return cx, cy, ch


def f2(x, y, h):
    chs = []
    for _x, _y, _h in zip(x, y, h):
        for cx in range(0, 100 + 1):
            for cy in range(0, 100 + 1):
                tmp = h_H(cx, cy, _x, _y)
                print((_x, _y), (cx, cy), _h, tmp, sep="\t")

    return 1


if __name__ == '__main__':
    main()
