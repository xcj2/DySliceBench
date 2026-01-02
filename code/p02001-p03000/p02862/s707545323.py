
class ModOperator:
    def __init__(self, MOD: int = 10 ** 9 + 7):
        self.MOD = MOD

    # x^n % MOD
    def mod_pow(self, x: int, n: int):
        bi = str(format(n, "b"))
        res = 1
        a = x
        for i in range(len(bi)):
            if n >> i & 1:
                res = (res * a) % self.MOD
            a = (a * a) % self.MOD
        return res
    
    # x! % MOD
    def mod_fact(self, x: int):
        res = 1
        for i in range(1, x + 1):
            res = res * i % self.MOD
        return res % self.MOD

    # x * (x - 1) * ... * (x - y + 1) % MOD
    def mod_partial_fact(self, x: int, y: int):
        res = 1
        for i in range(x - y + 1, x + 1):
            res = res * i % self.MOD
        return res % self.MOD

    # inverse of a number
    def mod_inv(self, x: int):
        return self.mod_pow(x, self.MOD - 2)
    
    # conmination nCk
    def mod_comb(self, n: int, k: int):
        numerator = self.mod_partial_fact(n, k)
        denomintator = self.mod_fact(k)
        return numerator * self.mod_inv(denomintator) % self.MOD


def main():
    X, Y = map(int, input().split())

    p = (X + Y) // 3
    q = (X + Y) % 3
    if q == 0 and p <= X <= 2 * p and p <= Y <= 2 * p:
        op = ModOperator()
        res = op.mod_comb(p, X - p)
    else:
        res = 0
    print(res)

if __name__ == '__main__':
    main()