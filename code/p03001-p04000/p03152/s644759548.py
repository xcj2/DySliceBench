def main():
    N, M = map(int, input().split())
    *A, = map(int, input().split())
    *B, = map(int, input().split())

    ans = f(N, M, A, B)
    print(ans)


def f(N, M, A, B):
    """
    1 ≤ N  ≤ 1000
    1 ≤ M  ≤ 1000
    1 ≤ Ai ≤ N×M <= 10^6
    1 ≤ Bj ≤ N×M <= 10^6

    書き方
        1マス目: N*M   通り
        2マス目: N*M-1 通り
        (N*M)! 通り: TLE

    A * B による組合せ:
        クロスしたマスそれぞれ行列の最大値が異なるなら、小さい方以下を書く
        クロスしたマスそれぞれ行列の最大値が同じならそこに書くしかない
            よって、他の行列にその値がある場合は書けない
        両方考慮しないと書けるか分からない
        A * B: TLE
    """
    ans = editorial(N, M, A, B)
    return ans


def editorial(N, M, A, B):
    """
    最大値をsortしておくと考えやすい
    考える順を逆順sortしておくと考えやすい
        ある数字の次の数字は
        そこまでしか置けない
        それ以前には置ける
    行6ならば
        列6以上にしか置けない
        列4に置くと最大値4を超えてしまう
        2通り
      9 8 4
    9|9| | |
    8| |8| |
    6| | | |

    7ならば
        行8以上には置ける: 2通り
        列8以上には置ける: 2通り
        2*2 = 4
        9と8はすでに置いてあるので-2
            全体からこれ以降をすべて除けば今まで使った数
            N * M - 7 = 3 * 3 - 7 = 2
        よって 2通り
    """
    A = sorted(A)  # , reverse=True)
    B = sorted(B)  # , reverse=True)
    # 探索の高速化と行列での最大値重複判定setの代わり
    d_a = {a: None for a in A}
    d_b = {b: None for b in B}
    if len(d_a) != N:
        return 0
    if len(d_b) != M:
        return 0

    def f(xs, y):
        """これのためにsort, yを超える個数
        sortしてあるので二分探索でもよい: TLEになるので必須
        """
        from bisect import bisect_left
        idx = bisect_left(xs, y)
        return len(xs) - idx

    def f_slow(xs, y):
        for i, x in enumerate(xs):
            if x < y:
                return i

        return i + 1

    ans = 1
    MOD = 10 ** 9 + 7
    for i in range(1, N * M + 1)[::-1]:
        in_a = i in d_a
        in_b = i in d_b

        a, b = 0, 0
        if in_a and in_b:
            # 場所固定
            pass
        elif in_a:
            # 片方の行・列から候補を探す
            b = f(B, i)
            ans = ans * b % MOD
        elif in_b:
            a = f(A, i)
            ans = ans * a % MOD
        else:
            a = f(B, i)
            b = f(A, i)
            # 候補
            # すべてのマスに対して前までの数字は埋まっている
            cells = a * b
            used = (N * M - i)
            ans = (cells - used) * ans % MOD
            # print("\t", cells, used)

        # print(i, ans, a, b, in_a, in_b)

    return ans


if __name__ == '__main__':
    main()
