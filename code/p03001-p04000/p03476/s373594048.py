def d_2017_like_number():
    Q = int(input())
    I = [[int(i) for i in input().split()] for j in range(Q)]

    def prime_table(n):
        """n 以下の整数がそれぞれ素数かどうかのリスト (エラトステネスの篩)"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0と1は素数でない
        for j in range(2, int(n**0.5) + 1):
            if not is_prime[j]:
                continue
            for k in range(j * 2, n + 1, j):
                is_prime[k] = False  # jの倍数は素数でない
        return is_prime

    def calc_like2017(m, p):
        # i 番目の要素が、1 以上 i 以下の "2017に似た数" の個数となるリストを返す
        # m 以下の素数のリスト p を予め作っておく必要がある
        c = [0] * (m + 1)  # 0番目は0と定義する
        for i in range(3, m + 1, 2):  # 0, 1, 2 は定義上2017に似た数にならない
            if p[i] and p[(i + 1) // 2]:
                c[i] += 1
        for i in range(3, m + 1):
            c[i] += c[i - 1]
        return c

    like2017 = calc_like2017(10**5, prime_table(10**5))
    ans = [like2017[r] - like2017[l - 1] for l, r in I]
    return '\n'.join(map(str, ans))

print(d_2017_like_number())