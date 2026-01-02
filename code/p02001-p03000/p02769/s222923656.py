class Calc:
    def __init__(self, max_value, mod):
        """combination(max_value, all)"""
        fact = [-1] * (max_value + 1)
        fact[0] = 1
        fact[1] = 1
        for x in range(2, max_value + 1):
            fact[x] = x * fact[x - 1] % mod

        invs = [1] * (max_value + 1)
        invs[max_value] = pow(fact[max_value], mod - 2, mod)
        for x in range(max_value - 1, 0, -1):
            invs[x] = invs[x + 1] * (x + 1) % mod

        self.fact = fact
        self.invs = invs
        self.mod = mod

    def combination(self, n, r):
        if n - r < r: return self.combination(n, n - r)
        if r < 0: return 0
        if r == 0: return 1
        if r == 1: return n
        return self.fact[n] * self.invs[r] * self.invs[n - r] % self.mod


def main():
    mod = 10 ** 9 + 7

    n, k = map(int, input().split())

    cl = Calc(max_value=n, mod=mod)

    m = min(k, n - 1)

    ret = 0
    for i in range(m + 1):
        t = cl.combination(n, i)
        t = t * cl.combination(n - 1, i) % mod
        ret = (ret + t) % mod

    print(ret)


if __name__ == '__main__':
    main()

# 解説放送

# 和がn
# 0はk個以下

# 0の個数を固定して、
# [0,k]個の0について総和を取る

# 0がi箇所
# 1以上がn-i箇所 -> 扱いにくいので、全体から1を引いて0以上にする
# 和がn

# 0以上がn-i箇所
# 和がn-(n-i)=i

# n-i箇所にi個のボールを入れる問題になる
# H(n-i,i)

# n-i-1本の仕切り線とi個のボールの並べ方になる
# choose((n-i-1)+i,i)
