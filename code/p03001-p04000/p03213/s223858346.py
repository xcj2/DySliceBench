def main():
    """
    input:
        1 <= N <= 100

    output:
        N! の約数のうち、七五数 は何個
        七五数とは約数をちょうど 75個持つ正の整数
    """
    N = int(input())

    ans = f(N)
    print(ans)


def f(N):
    """素因数分解までは浮かんだ
    """
    factor_all = [[] for _ in range(N + 1)]
    factors = [0] * (N + 1)
    for i in range(2, N + 1):
        # N_max=100 より √i にしなくても高速なので簡易に実装
        x = i
        for div in range(2, x + 1):
            while x % div == 0:
                factors[div] += 1
                factor_all[i].append(div)
                x //= div

    # print(factors)
    # print(factor_all)
    ans1 = editorial(factors)
    ans2 = ref(factors)
    assert ans1 == ans2

    return ans1


def editorial(factors):
    factors = factors

    def a(x):
        n = 0
        for f in factors:
            if f >= x - 1:
                n += 1

        return n

    # どういうこと？
    # 75: 1つの素数で0~74乗なのでわかる
    # -1: => 0乗は1だから、他のパターンでも起こるので除外？
    # 75,
    ans = a(75)
    ans += a(25) * (a(3) - 1)
    ans += a(15) * (a(5) - 1)
    ans += a(5) * (a(5) - 1) * (a(3) - 2) // 2

    return ans


def ref(factors):
    """https://beta.atcoder.jp/contests/abc114/submissions/3704878
    """
    # 2以上の理由: n=1ではその数字は素数なので約数が1と自信しかないので意味がない
    # a^1 * b^2 * c^3: 1*2*3=6通り と使っても約数の数が変わらない
    nums = [n for n in factors if n >= 2]

    # 75 の約数
    divs = [i for i in range(1, 75+1) if 75 % i == 0]

    # dp[i][j]
    # i: 1-index baseで nums[1]...nums[n]までの n種類の素因数についてi番目まで利用
    # j: 約数の数0-75 まで
    # どんな数でも1では割れるので1, 1は素数に含めない
    n_nums = len(nums)
    dp = [[0] * (75 + 1) for _ in range(n_nums + 1)]
    dp[0][1] = 1

    # 75個なので,75の約数の組合せでしか割れないのは分かるが
    # 2重ループでよいのか？: [1, 3. 15, 25, 75]
    from itertools import product
    div_pairs = [(d1, d2)
                 for d1, d2 in product(divs, repeat=2)
                 if d1 * d2 <= 75]

    for i in range(n_nums):
        for d1, d2 in div_pairs:
            # TODO: 75 = 3^1 * 5^2, そもそも 3*15=3^2*5, 3*3, は必要なのか？
            if d1 * d2 in (45, 9):
                continue

            # 遷移
            # i−1 番目の素因数まででできた約数が d1 個で、
            # i 番目の素因数を d2−1 個選ぶ、という選び方
            # => editorial 内の a func の f >= x - 1 と同じ

            # nums[i] + 1 >= d2: より下記のほうが意味がわかりそう
            if nums[i] >= d2 - 1:
                # print(i, nums[i], (d1, d2), d1 * d2,
                #       dp[i][d1], dp[i+1][d1 * d2], sep="\t")
                dp[i+1][d1 * d2] += dp[i][d1]

    ans = dp[n_nums][75]
    return ans


if __name__ == '__main__':
    main()
