def main():
    """
    input:
        1 <= H <= 100
        1 <= W <= 8
        1 <= K <= W

    output:
        数列の項の最大公約数の最大値
    """
    H, W, K = map(int, input().split())

    # ans = visualize(H, W, K)
    ans = editorial(H, W, K)
    print(ans)


def f(H, W, K):
    """
    1-2の間に横棒を引く
    引き方: 0-H に引く組合せ
        x = sum(nCr(H, i) for i in range(H+1))

    2-3の間に横棒を引く
    引き方: 1-2の引いた部分以外に引くことができる
        startが1からなのでたどり方的に上に引く必要がないが
        それも正しい可能性のあるあみだくじなので考慮する

        x = 0
        for i in range(H+1):
            # i 本引いてあるなら、引いてない部分がMAX
            for j in range(H-i+1):
                x += sum(nCr(j, k) for k in range(j))

    たどり方
    1の一番高い棒から2へ向かう or なければそのまま下へ
    2から1or3の棒へ向かう or なければ下へ

    Kにたどり着くパターン or (全パターン - たどりつけないパターン)
        たぶん、縦と横を独立に考える。なんとなく
        下にH
        横にK-1, 右を+1左を-1としたとき
    """
    mod = 10 ** 9 + 7
    ans = 0

    return ans % mod


def visualize(H, W, K):
    valid_k = []
    for k in range(1 << (W - 1)):
        if not k & (k << 1):
            valid_k.append(k)

    for i in range(H):
        print("row", i+1)
        for j in range(W):
            for k in valid_k:
                h_bar = "{:08b}".format(k)[-(W-1):]
                h_bar = h_bar.replace("1", "_").replace("0", " ")

                header = " " + " ".join(str(i) for i in range(W)) + " "
                header = header.replace(" {} ".format(j), "[{}]".format(j))

                print(header)
                print(" |" + "|".join(list(h_bar)) + "| ")
                print(" " + " ".join("|" for _ in range(W)) + " ")
                print()

    return 1


def is_connected(k, W):
    # 2つの横線がつながっていないか
    ok = True
    for l in range(W - 2):
        if k >> l & 1 and k >> (l + 1) & 1:
            ok = False
            break

    ok2 = "11" not in bin(k)
    ok3 = not (k & (k << 1))
    assert ok == ok2 == ok3

    return ok


def editorial(H, W, K):
    mod = 10 ** 9 + 7
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    # dp[H+1][W]
    # dp[i][j]: 上からicmまでの時点で、1からjに行ける数
    # dp[i + 1][a] += dp[i][j]: 下に1つ進んだとき、aに行ける数
    for i in range(H):
        for j in range(W):
            k_max = 1 << (W - 1)
            for k in range(k_max):
                # 2つの横線がつながっていないか
                ok = is_connected(k, W)
                if not ok:
                    continue

                #  pos:            L   S   R
                #  v_bar:   [j-1]_____[j]_____[j+1]
                #  h_bar:         j-1     j
                a = 0  # straight
                if j >= 1 and k >> (j - 1) & 1:  # left
                    a = - 1
                elif j < W - 1 and k >> j & 1:  # right
                    a = 1

                dp[i + 1][j + a] += dp[i][j]
                dp[i + 1][j + a] %= mod

    return dp[H][K - 1]


def a(H, W, K):
    """
    https://twitter.com/Py2K4/status/1059078331407028226
    """


def editorial_fib(H, W, K):
    """
    https://twitter.com/259_Momone/status/1059085685208956928
    導出: 棒が2本連続しない
    """


if __name__ == '__main__':
    main()
