def solve(m, a) -> int:
    from bisect import bisect_left
    from itertools import accumulate

    *a, = sorted(a)
    n = len(a)

    acc = (0,) + tuple(accumulate(a))

    def is_ok(h):
        ret = 0
        for x in a:
            j = bisect_left(a, h - x)
            ret += (n - j)
            if ret >= m:
                return True
        return False

    def binary_search():
        """M通り以上の握手ができる幸福度の上限"""
        ok = 0
        ng = a[-1] * 2 + 1
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    sup = binary_search()  # 上限

    ret = 0
    rest = m
    for x in a:
        j = bisect_left(a, sup + 1 - x)  # 前の投稿はsup+1に直していなかった
        # sup+1以上になるような握手を全て行った残りの握手回数restはすべてsupになるはず
        use = n - j
        rest -= use

        ret += use * x + (acc[n] - acc[n - use])

    ret += rest * sup

    return ret


def main():
    n, m = map(int, input().split())
    *a, = map(int, input().split())
    print(solve(m, a))


if __name__ == '__main__':
    main()

# k 回目の握手で、左手でゲスト xk と、右手でゲスト yk と手を握ったとする。
# このとき、 (xp,yp)=(xq,yq) を満たすような p,q(1≤p<q≤M) が存在しない。
#
# サンプル2の3,5は重複があるが、3a,3bとおくと
# (3a,v)と(3b,v)は値が等しい組なので、両方選べない
# よって、Aをset(A)に変換する必要がある
# と考えたが、それだとサンプルが合わない
#
# (3a,v)と(3b,v)を区別する場合の値を返すコードを提出してみる
