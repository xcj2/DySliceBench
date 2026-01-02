def e_flatten_prime_factorization(MOD=10**9 + 7):
    N = int(input())
    A = [int(i) for i in input().split()]

    def prime_factorization_dict(n):
        from collections import defaultdict
        """nを素因数分解したときの素数とその指数の辞書"""
        if n == 1:
            return {2: 0}  # 1は素数の0乗の積とみなす
        i, table = 2, defaultdict(int)
        while i**2 <= n:
            while n % i == 0:
                table[i] += 1
                n //= i
            i += 1
        if n > 1:
            table[n] = 1
        return table

    def prime_table(n):
        """n以下の素数のリスト(エラトステネスの篩)"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0と1は素数でない
        for j in range(2, int(n**0.5) + 1):
            if not is_prime[j]:
                continue
            for k in range(j * 2, n + 1, j):
                is_prime[k] = False  # jの倍数は素数でない
        return {i: 0 for i in range(n + 1) if is_prime[i]}

    lcm_prime = prime_table(10**6)
    for a in A:
        for base, exp in prime_factorization_dict(a).items():
            lcm_prime[base] = max(lcm_prime[base], exp)
    lcm = 1
    for base, exp in lcm_prime.items():
        lcm *= pow(base, exp, MOD)
        lcm %= MOD
    coefficient = sum(pow(a, MOD - 2, MOD) for a in A)
    return (lcm * coefficient) % MOD

print(e_flatten_prime_factorization())
