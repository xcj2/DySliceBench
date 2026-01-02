def main():
    N = int(input())

    ans = editorial(N)
    ans1 = editorial_dp(N)

    assert ans == ans1
    print(ans)


def editorial(N):
    MOD = 10 ** 9 + 7
    memo = [{} for i in range(N+1)]

    def ok(last4):
        for i in range(4):
            # 文字列ベースなので、隣接文字をswapしやすいように変換
            t = list(last4)
            if i >= 1:
                t[i-1], t[i] = t[i], t[i-1]
            if ''.join(t).count('AGC') >= 1:
                return False

        return True

    def dfs(cur, last3):
        if last3 in memo[cur]:
            return memo[cur][last3]

        # 問題なし
        if cur == N:
            return 1

        # 文字追加
        ret = 0
        for c in 'ACGT':
            # 機械的にswap全部試すチェック
            if ok(last3 + c):
                ret += dfs(cur + 1, last3[1:] + c)
                ret %= MOD
        memo[cur][last3] = ret

        return ret

    # TTT: editorial_dp と同様に無害な組合せ
    ans = dfs(0, 'TTT')
    return ans


def editorial_dp(N):
    """
    AGC
    ACG
    GAC
    ----
    追加+swap
    AG.C
    A.GC
    """
    import numpy as np
    from itertools import product

    T, A, G, C = range(4)
    MOD = 10 ** 9 + 7
    dp = np.zeros((N+1, 4, 4, 4), dtype=int)
    # AGCに関係ないTを初期状態とすればなんの影響もない
    dp[0, 0, 0, 0] = 1
    ng_pattern = (A, G, C)

    for i in range(N):
        for c1, c2, c3 in product(range(4), repeat=3):
            if dp[i, c1, c2, c3] == 0:
                continue

            for c4 in range(4):
                patterns = [
                    # 4文字目追加 3文字
                    (c2, c3, c4),
                    (c2, c4, c3),
                    (c3, c2, c4),
                    # 4文字目追加 4文字
                    (c1, c2, c4),
                    (c1, c3, c4),
                ]
                ng = any(ng_pattern == p for p in patterns)
                if ng:
                    continue

                dp[i+1, c2, c3, c4] += dp[i, c1, c2, c3]
                dp[i+1, c2, c3, c4] %= MOD

    ans = 0
    for c1, c2, c3 in product(range(4), repeat=3):
        ans += dp[N, c1, c2, c3]
        ans %= MOD

    return ans


def WA(N):
    """
    3 <= N <= 100
    4種類の文字: ACGT
    4^N 通りの文字列が存在する
    隣接文字2つを1回入れかることができる
    違反: AGC
    違反: 入力例1より
        ACG
        GAC

    2文字までは違反なし
    3文字では3つ違反, 上記の通り
        64-3 = 61
    4文字
        4文字目追加なので61 * 4
        3文字目の時点で3つで終わるパターンがある
        次に 下記パターンの文字が追加されるとNG
            AG C
            AC G
            GA C

        3文字のときに終わるパターンの構成
            AG: [.]AG NGなし    ACGT 4
            AC: [G]AC NGより    AC T 3
            GA: [.]GA NGなし    ACGT 4

        AG: 構成4 * OK:4-1
        AC: 構成3 * OK:4-1
        GA: 構成4 * OK:4-1
            61 + (61 * 4 - [4+3+4] * 1)

        pattern に周期がありそう
        全パターンから引くので、逆元を使いそう
    """
    ans = 61
    ag_ac_ga = [4, 3, 4]
    if N == 3:
        return ans

    MOD = 10 ** 9 + 7
    for i in range(4, N+1):
        ag_ac_ga = [x * 3 for x in ag_ac_ga]
        print(ans + ans * i)
        print(sum(ag_ac_ga))
        ans += ans * i - sum(ag_ac_ga) * 3
        # ans = ans * i - sum(ag_ac_ga)

    ans %= MOD

    aaa()
    return ans


def aaa():
    ans = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    x = "".join(map(str, [i, j, k, l]))
                    # ACGT: 0123
                    # AGC, ACG, GAC
                    y = any(z in x for z in ("021", "012", "201"))
                    ans.append((x, y))

    print(*ans, sep="\n")
    print(sum(x[1] for x in ans))
    print(len(ans))


if __name__ == "__main__":
    main()
