from collections import Counter


def main():
    """
    1 <= N <= 10^5
    1 <= M <= 10^9

    正整数 N, M
    a1 * a2 * ... * aN = M となる長さNの数列a
    何通りあるか
    数列A1-ai != 数列A2-ai
    """
    N, M = map(int, input().split())

    ans = editorial(N, M)
    print(ans)


def factorize(N):
    """素因数分解

    TODO: もっと速い方法
    素因数がある場合は範囲をsqrtで狭められるが、ない場合愚直に探してしまう
    N以下の素数を見つけて、それだけで対応すれば速いはず
    """
    import math
    factors = []
    while True:
        if N % 2 == 0:
            factors.append(2)
            N //= 2
        else:
            break
    m = int(math.sqrt(N))
    i = 3
    while i <= m:
        add = False
        while True:
            if N % i == 0:
                factors.append(i)
                N //= i
                add = True
            else:
                break
        if add:
            m = int(math.sqrt(N))
        i += 2
    if N > 1:
        factors.append(N)
    return factors


def f(N, M):
    """
    M を素因数分解すると約数とそれらの個数がわかる
    それらの組合せを制約を満たすようにする
    1 * M, M * 1 をわすれないこと:
        1 * 1 * 1 * M もOK

    3 12
        1,1,12: 3P3 / 2!
        2,2,3:  3P3 / 2!
        3,4,1:  3P3
        6,2,1:  3P3

    http://sucrose.hatenablog.com/entry/2014/10/10/235805
    """
    ans = 0
    m = 10 ** 9 + 7
    factors = factorize(M)
    c = Counter(factors)
    print(c)
    return ans


def editorial(N, M):
    i = 2
    rest_M = M
    ans = 1
    mod = 10 ** 9 + 7
    while i ** 2 <= rest_M:
        div_count = 0
        while rest_M % i == 0:
            div_count += 1
            rest_M //= i

        if div_count > 0:
            # N - 1, nCr において div_count と同じ
            ans *= calc_comb(N + div_count - 1, div_count)
            ans %= mod

        i += 1

    if rest_M != 1:
        ans *= calc_comb(N + 1 - 1, N - 1)
        ans %= mod

    return ans


def calc_comb(n, r, mod=10 ** 9 + 7):
    if r > n - r:
        return calc_comb(n, n - r)

    ans_mul = 1
    ans_div = 1

    for i in range(r):
        # n! / (n - r)!
        ans_mul = ans_mul * (n - i) % mod
        # r!
        ans_div = ans_div * (i + 1) % mod

    # k^(-1) ≡ k^(n-2) (mod n)
    return ans_mul * mod_pow(ans_div, mod - 2) % mod


def mod_pow(a, p, mod=10 ** 9 + 7):
    if p == 0:
        return 1

    if p % 2 == 0:
        half_p = p // 2
        half = mod_pow(a, half_p)
        return half ** 2 % mod
    else:
        return a * mod_pow(a, p - 1) % mod


def mod_pow_bit(a, p, mod=10 ** 9 + 7):
    """
    http://keita-matsushita.hatenablog.com/entry/2016/12/05/184011
    """
    ans = 1
    while p > 0:
        if (p & 1) == 1:
            ans = ans * a % mod

        a = a ** 2 % mod
        p >>= 1

    return ans


def ref(N, M):
    """
    https://mathtrain.jp/tyohukuc
        n 種類のものから重複を許して r 個選ぶ場合の数
        n H r = (n+r−1) C r

    3 12 の例で示せているのに、重複組合せという言葉が頭に浮かばなかった

    解説動画より
    modの世界における逆元?
        重複組合せ
            フェルマーの小定理
                ref: http://keita-matsushita.hatenablog.com/entry/2016/12/05/184011
            階乗と階乗逆元
        拡張ユークリッド互除法
            今回は出番なし
    """
    def create_tables(N, MOD):
        """
        http://drken1215.hatenablog.com/entry/2018/06/08/210000
        """
        fact_mod = [0] * (N + 1)
        simod = [0] * (N + 1)
        fact_inv_mod = [0] * (N + 1)

        fact_mod[0] = fact_mod[1] = 1
        simod[0] = simod[1] = 1
        fact_inv_mod[0] = fact_inv_mod[1] = 1

        for i in range(2, N + 1):
            fact_mod[i] = (fact_mod[i - 1] * i) % MOD
            simod[i] = MOD - simod[MOD % i] * (MOD // i) % MOD
            fact_inv_mod[i] = (fact_inv_mod[i - 1] * simod[i]) % MOD
            # inv 配列が確実に不要な場面 とは？ (ここでのsimod)
            # inv[n] を逆元計算によって計算しておく
            # finv[i-1] = finv[i] * i % MOD によって finv 配列を後ろから計算していく

        return fact_mod, fact_inv_mod

    def create_fact_mod(N, MOD):
        fact_mod = [0] * (N + 1)
        fact_mod[0] = 1
        fact_mod[1] = 1

        # 階乗のテーブル作成, 累積積によって計算量を落としている
        for i in range(2, N + 1):
            fact_mod[i] = (fact_mod[i - 1] * i) % MOD

        return fact_mod

    def create_seq_inv_mod(N, MOD):
        simod = [0] * (N + 1)
        simod[0] = 1  # 0のままでもよい?
        simod[1] = 1

        # 階乗逆元のテーブル用に作成
        for i in range(2, N + 1):
            simod[i] = (MOD - MOD // i) * simod[MOD % i] % MOD
            # 下記との違いはなにか？
            # simod[i] = MOD - simod[MOD % i] * (MOD // i) % MOD

        return simod

    def create_fact_inv_mod(N, MOD, simod):
        fact_inv_mod = [0] * (N + 1)
        fact_inv_mod[0] = 1
        fact_inv_mod[1] = 1

        # 階乗逆元のテーブル作成
        for i in range(2, N + 1):
            fact_inv_mod[i] = (fact_inv_mod[i - 1] * simod[i]) % MOD

        return fact_inv_mod

    def comb_mod(N, R, fact_mod, fact_inv_mod, MOD):
        """
        組合せ nCr: n! / ((n-r)! * r!)
        上記のmodを逆元を使って表現

        f[n] * f[r] % MOD * f[n-r] % MOD 
        これのために事前にテーブルを作っていた
        """
        return fact_mod[N] * fact_inv_mod[N - R] * fact_inv_mod[R] % MOD

    ans = 1
    m = 10 ** 9 + 7
    factors = factorize(M)
    c = Counter(factors)

    # N + 10 でRE: 重複組合せなのでN以上になるため、約数2が32個あればそうなる
    # https://beta.atcoder.jp/contests/abc110/submissions/3253308
    # http://betrue12.hateblo.jp/entry/2018/09/24/020414
    fact_mod = create_fact_mod(N + 100, m)
    simod = create_seq_inv_mod(N + 100, m)
    fact_inv_mod = create_fact_inv_mod(N + 100, m, simod)

    # 重複組合せ: n! / (a! * (b - a)!)
    # 重複組合せ を 各素因数における組合せ結果の掛け合わせで表現
    for i in c.values():
        ans *= comb_mod(N - 1 + i, i, fact_mod, fact_inv_mod, m)
        ans %= m

    return ans


if __name__ == '__main__':
    main()
