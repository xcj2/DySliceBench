class Sieve:
    """区間[2,n]の値を素因数分解する"""

    def __init__(self, n=1):
        primes = []
        f = [0] * (n + 1)
        f[0] = f[1] = -1
        for i in range(2, n + 1):  # 素数を探す
            if f[i]: continue
            primes.append(i)
            f[i] = i  # 素数には自身を代入
            for j in range(i * i, n + 1, i):  # 合成数に素因数を書き込む
                if not f[j]:
                    f[j] = i  # 最小の素因数を代入
        self.primes = primes
        self.f = f

    def is_prime(self, x) -> bool:  # 素数判定
        return self.f[x] == x

    def factor_list(self, x) -> list:  # 素因数分解の昇順リスト, [2,2,3,5,...]
        res = []
        while x != 1:
            res.append(self.f[x])
            x //= self.f[x]
        return res

    def factor(self, x) -> list:  # 素因数分解の頻度リスト, [[2,x],[3,y],[5,z],...]
        fl = self.factor_list(x)
        if not fl: return []
        res = [[fl[0], 0]]
        for p in fl:
            if res[-1][0] == p:
                res[-1][1] += 1
            else:
                res.append([p, 1])
        return res


def main():
    from collections import defaultdict

    MOD = 10 ** 9 + 7
    A_MX = 10 ** 6

    N = int(input())
    *a, = map(int, input().split())

    s = Sieve(n=A_MX)

    dict_lcm = defaultdict(int)
    for x in a:
        for prime, cnt in s.factor(x):
            dict_lcm[prime] = max(dict_lcm[prime], cnt)

    lcm = 1
    for prime, count in dict_lcm.items():
        lcm = lcm * pow(prime, count, MOD) % MOD

    ans = 0
    for x in a:
        ans = (ans + pow(x, MOD - 2, MOD)) % MOD
    ans = ans * lcm % MOD
    print(ans)


if __name__ == '__main__':
    main()
