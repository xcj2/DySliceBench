# a**bのmodを取りたい時に高速にできる
def modpow(a, n, mod):
    res = 1
    # 45 = 101101
    # ここでいう、1X11X1の部分飲み計算すれば良い
    # a**45 = a**32 + a**8 + a**4 + a**1なので、これだけ計算すれば良い
    # そしてそのためには、45を2進数に変えて、右ビットシフトしていけばok
    # なので、n >>= 1をする
    # ex)45,22,11,5,2,1
    while (n > 0):
        # print(n, a, res)
        # 3&1みたいな論理積とった結果、両方1のものがあった場合にresにたす
        if n & 1:
            res = res * a % mod
        # a = 掛け算の結果を更新する。
        # a*b の mod(c)は。a mod(c)*b mod(c)と同じなので、掛け算するaもmodをとっていく
        a = a * a % mod
        # n>>1で、1桁ずつ減らしていく
        # 101101 > 10110みたいな
        # 先頭の1文字が減るわけではない。45->45-32みたいな感じではない
        # でも、やりたいのは、1X11X1の部分のみ計算するための、右bitシフトなので45->22の部分に特に意味はない
        # 101101 > 10110をすることで末尾が一つずつ消していけることが重要
        # n=n>>1をすることで二進法展開ができる
        n = n >> 1
    return res


def modcomb(n, r, mod):
    if r > n - r:
        r = n - r
    nPr, rPr = 1, 1
    for i in range(r):
        nPr = nPr * (n - i) % mod
        rPr = rPr * (i + 1) % mod
    # print(n, r, nPr, rPr)
    # nCrのmodを高速に取りたい
    # nCr は nPr / rPr
    # 1/(33333P33333)のmodを取りたい
    # 1/277540578 のmodを取りたい
    # print(nPr, modpow(rPr, mod - 2, mod))
    # nCrのmodを高速にとる。nPr / rPr を nPr * (1/rPr)に分ける
    # modにおいて、rPrにbをかけると1になる。そのようなbがrPrの逆元である
    return nPr * modpow(rPr, mod - 2, mod) % mod


def main():
    X, Y = map(int, input().split())
    n = (-X + 2 * Y) / 3
    m = (2 * X - Y) / 3
    # これで(i+1,j+2)をとる回数がn回(i+2,j+1)をとる回数がm回だとわかる
    # 少数が出てきたら計算できないので0を返す
    if not(n.is_integer() and m.is_integer()):
        return 0
    if n >= 0 and m >= 0:
        # n+mCnを計算する。modを高速にとる
        return modcomb(int(n + m), int(n), mod=10 ** 9 + 7)
    else:
        return 0


print(main())
# print(modpow(277540578, 10**9 + 5, 10**9 + 7))
