def solve(n, h, a):
    size = 1 << ((n + 1) - 1).bit_length()  # 元の配列サイズ以上の最小の二冪 == 最下段
    # 高さに対する美しさの最大値なので、高さ[0,n]の(n+1)要素に対して、segを考える
    seg = [0] * (size * 2 - 1)

    def update(seg, k, x):
        k += size - 1
        seg[k] = x  # 値を更新する
        while k > 0:
            k = (k - 1) // 2  # 親のindex
            seg[k] = max(seg[k * 2 + 1], seg[k * 2 + 2])

    def get(seg, a, b, k=0, l=0, r=-1):
        # [a,b)区間の処理結果を返す
        # 注目区間[l,r)
        if r < 0:
            r = size

        if r <= a or b <= l:
            return 0
        # 区間が重ならない

        if a <= l and r <= b:
            return seg[k]
        # 完全被覆

        m = (l + r) // 2
        return max(get(seg, a, b, k * 2 + 1, l, m), get(seg, a, b, k * 2 + 2, m, r))
        # 部分被覆

    for h_, a_ in zip(h, a):
        update(seg, h_, get(seg, 0, h_) + a_)
        # 1回あたり更新するのは1箇所だから、iを状態にもつ必要はなくて、配列を使い回すことができる
        # 区間maxが高速に計算できればいいから、セグメント木を使えばできる
    return get(seg, 0, n + 1)


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = tuple(map(int, input().split()))
    a = tuple(map(int, input().split()))
    print(solve(n, h, a))

# https://kyopro-friends.hatenablog.com/entry/2019/01/12/231035
